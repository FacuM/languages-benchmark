from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import time


TIME_SENTINELS = {
    "user": "__CPU_USER=",
    "system": "__CPU_SYS=",
    "wall": "__WALL=",
    "rss": "__RSS_KB=",
}


@dataclass(slots=True)
class ExecutionMetrics:
    cpu_seconds: float | None
    wall_seconds: float | None
    max_rss_mb: float | None
    stdout: str
    stderr: str
    returncode: int
    host_wall_seconds: float | None
    repeat_count: int


@dataclass(slots=True)
class ServiceHandle:
    container_id: str
    host_port: int
    container_port: int


class ContainerEngine:
    def __init__(self, binary: str = "docker") -> None:
        self.binary = binary

    def validate(self) -> None:
        subprocess.run([self.binary, "--version"], check=True, capture_output=True, text=True)

    def build(self, tag: str, dockerfile: Path, context: Path, build_args: dict[str, str] | None = None) -> None:
        cmd = [self.binary, "build", "-t", tag, "-f", str(dockerfile)]
        for key, value in (build_args or {}).items():
            cmd += ["--build-arg", f"{key}={value}"]
        cmd.append(str(context))
        subprocess.run(
            cmd,
            check=True,
            text=True,
        )

    def inspect_runtime(self, image: str, command: str) -> str | None:
        proc = subprocess.run(
            [self.binary, "run", "--rm", image, "sh", "-lc", command],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            return None
        return proc.stdout.strip() or proc.stderr.strip() or None

    def run_single(
        self,
        *,
        image: str,
        args: list[str],
        fixtures_dir: Path,
        cpu_limit: str,
        memory_limit: str,
        network_disabled: bool,
        repeat_count: int = 1,
    ) -> ExecutionMetrics:
        cmd = [
            self.binary,
            "run",
            "--rm",
            "--cpus",
            cpu_limit,
            "--memory",
            memory_limit,
            "-v",
            f"{fixtures_dir}:/fixtures:ro",
        ]
        if network_disabled:
            cmd += ["--network", "none"]
        cmd += [image, "sh", "-lc", _timed_loop_script(args, repeat_count)]
        started = time.perf_counter()
        proc = subprocess.run(cmd, text=True, capture_output=True)
        host_wall_seconds = time.perf_counter() - started
        cpu_seconds = _parse_cpu_seconds(proc.stderr)
        wall_seconds = _parse_wall_seconds(proc.stderr)
        rss_mb = _parse_rss_mb(proc.stderr)
        divisor = max(repeat_count, 1)
        return ExecutionMetrics(
            cpu_seconds=(cpu_seconds / divisor) if cpu_seconds is not None else None,
            wall_seconds=(wall_seconds / divisor) if wall_seconds is not None else host_wall_seconds / divisor,
            max_rss_mb=rss_mb,
            stdout=proc.stdout,
            stderr=proc.stderr,
            returncode=proc.returncode,
            host_wall_seconds=host_wall_seconds / divisor,
            repeat_count=repeat_count,
        )

    def start_service(
        self,
        *,
        image: str,
        task_id: str,
        size: str,
        fixtures_dir: Path,
        cpu_limit: str,
        memory_limit: str,
        container_port: int,
    ) -> ServiceHandle:
        cmd = [
            self.binary,
            "run",
            "-d",
            "--cpus",
            cpu_limit,
            "--memory",
            memory_limit,
            "-v",
            f"{fixtures_dir}:/fixtures:ro",
            "-e",
            f"PORT={container_port}",
            "-p",
            f"127.0.0.1::{container_port}",
            image,
            "/app/run.sh",
            "start",
            task_id,
            size,
        ]
        proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
        container_id = proc.stdout.strip()
        host_port = self._mapped_port(container_id, container_port)
        return ServiceHandle(container_id=container_id, host_port=host_port, container_port=container_port)

    def stop_service(self, container_id: str) -> None:
        subprocess.run([self.binary, "rm", "-f", container_id], capture_output=True, text=True)

    def container_logs(self, container_id: str) -> tuple[str, str]:
        proc = subprocess.run([self.binary, "logs", container_id], capture_output=True, text=True)
        return proc.stdout, proc.stderr

    def container_cpu_seconds(self, container_id: str) -> float | None:
        proc = subprocess.run(
            [self.binary, "exec", container_id, "sh", "-lc", "if [ -f /sys/fs/cgroup/cpu.stat ]; then awk '/usage_usec/ {print \"u:\"$2}' /sys/fs/cgroup/cpu.stat; elif [ -f /sys/fs/cgroup/cpuacct/cpuacct.usage ]; then printf 'n:'; cat /sys/fs/cgroup/cpuacct/cpuacct.usage; fi"],
            capture_output=True,
            text=True,
        )
        text = proc.stdout.strip()
        if text.startswith("u:"):
            return float(text[2:]) / 1_000_000.0
        if text.startswith("n:"):
            return float(text[2:]) / 1_000_000_000.0
        return None

    def container_memory_peak_mb(self, container_id: str) -> float | None:
        proc = subprocess.run(
            [self.binary, "exec", container_id, "sh", "-lc", "if [ -f /sys/fs/cgroup/memory.peak ]; then cat /sys/fs/cgroup/memory.peak; elif [ -f /sys/fs/cgroup/memory.max_usage_in_bytes ]; then cat /sys/fs/cgroup/memory.max_usage_in_bytes; elif [ -f /sys/fs/cgroup/memory/memory.max_usage_in_bytes ]; then cat /sys/fs/cgroup/memory/memory.max_usage_in_bytes; fi"],
            capture_output=True,
            text=True,
        )
        text = proc.stdout.strip()
        if not text:
            return None
        return float(text) / (1024.0 * 1024.0)

    def _mapped_port(self, container_id: str, container_port: int) -> int:
        proc = subprocess.run(
            [self.binary, "port", container_id, f"{container_port}/tcp"],
            check=True,
            capture_output=True,
            text=True,
        )
        text = proc.stdout.strip().splitlines()[0]
        return int(text.rsplit(":", 1)[1])


def _timed_loop_script(args: list[str], repeat_count: int) -> str:
    quoted_args = " ".join(_shell_quote(arg) for arg in args)
    work_cmd = f"/app/run.sh {quoted_args} > /tmp/bench.stdout 2> /tmp/bench.stderr"
    loop_cmd = (
        "i=0; "
        f"while [ \"$i\" -lt {repeat_count} ]; do {work_cmd} || exit $?; "
        "i=$((i+1)); "
        "done"
    )
    time_format = "\\n".join(
        [
            f"{TIME_SENTINELS['user']}%U",
            f"{TIME_SENTINELS['system']}%S",
            f"{TIME_SENTINELS['wall']}%e",
            f"{TIME_SENTINELS['rss']}%M",
        ]
    )
    return (
        f"/usr/bin/time -f {_shell_quote(time_format)} -o /tmp/bench.time "
        f"sh -lc {_shell_quote(loop_cmd)}; "
        "status=$?; "
        "cat /tmp/bench.stdout; "
        "cat /tmp/bench.stderr >&2; "
        "cat /tmp/bench.time >&2; "
        "exit $status"
    )


def _shell_quote(value: str) -> str:
    return "'" + value.replace("'", "'\"'\"'") + "'"


def _parse_cpu_seconds(text: str) -> float | None:
    user = _match_float(text, rf"{re.escape(TIME_SENTINELS['user'])}([0-9.]+)")
    system = _match_float(text, rf"{re.escape(TIME_SENTINELS['system'])}([0-9.]+)")
    if user is None and system is None:
        return None
    return (user or 0.0) + (system or 0.0)


def _parse_wall_seconds(text: str) -> float | None:
    return _match_float(text, rf"{re.escape(TIME_SENTINELS['wall'])}([0-9.]+)")


def _parse_rss_mb(text: str) -> float | None:
    rss_kb = _match_float(text, rf"{re.escape(TIME_SENTINELS['rss'])}([0-9.]+)")
    if rss_kb is None:
        return None
    return rss_kb / 1024.0


def _match_float(text: str, pattern: str) -> float | None:
    match = re.search(pattern, text)
    if not match:
        return None
    return float(match.group(1))
