from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import os
import platform
import subprocess
from typing import Any


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=False)


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        with path.open("w", encoding="utf-8") as handle:
            handle.write("")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def collect_host_metadata(engine_binary: str) -> dict:
    machine = platform.machine()
    metadata = {
        "hostname": platform.node(),
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "machine": machine,
        "architecture": normalize_architecture(machine),
        "python_version": platform.python_version(),
        "cpu_count": os.cpu_count(),
        "cpu_model": _cpu_model(),
        "engine_binary": engine_binary,
        "engine_version": _command_output([engine_binary, "--version"]),
    }
    return metadata


def normalize_architecture(value: str | None) -> str:
    text = (value or "").strip().lower().replace("-", "_")
    aliases = {
        "amd64": "x86_64",
        "x64": "x86_64",
        "x86_64": "x86_64",
        "aarch64": "aarch64",
        "arm64": "aarch64",
        "armv7l": "armv7l",
        "armv6l": "armv6l",
        "ppc64le": "ppc64le",
        "s390x": "s390x",
        "riscv64": "riscv64",
    }
    return aliases.get(text, text or "unknown")


def git_metadata(cwd: Path) -> dict[str, Any]:
    commit = _command_output(["git", "-C", str(cwd), "rev-parse", "HEAD"])
    short = _command_output(["git", "-C", str(cwd), "rev-parse", "--short", "HEAD"])
    branch = _command_output(["git", "-C", str(cwd), "rev-parse", "--abbrev-ref", "HEAD"])
    dirty_proc = subprocess.run(
        ["git", "-C", str(cwd), "status", "--porcelain"],
        capture_output=True,
        text=True,
    )
    return {
        "commit": commit,
        "commit_short": short,
        "branch": branch,
        "dirty": bool((dirty_proc.stdout or "").strip()) if dirty_proc.returncode == 0 else None,
    }


def _cpu_model() -> str | None:
    cpuinfo = Path("/proc/cpuinfo")
    if cpuinfo.exists():
        for line in cpuinfo.read_text(encoding="utf-8", errors="ignore").splitlines():
            if ":" in line and line.split(":", 1)[0].strip().lower() == "model name":
                return line.split(":", 1)[1].strip()
    return platform.processor() or None


def _command_output(cmd: list[str]) -> str | None:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except Exception:  # noqa: BLE001
        return None
    return proc.stdout.strip() or proc.stderr.strip() or None
