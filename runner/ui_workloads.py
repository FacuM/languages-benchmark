from __future__ import annotations

from dataclasses import dataclass
import subprocess
import time

UI_CONFIG = {
    "gui_calculator": {"port": 8000},
    "data_visualization": {"port": 8000},
    "basic_web_application": {"port": 8000},
}


@dataclass(slots=True)
class UIWorkloadResult:
    stdout: str
    stderr: str
    returncode: int
    wall_seconds: float


def ui_port(task_id: str) -> int:
    return UI_CONFIG[task_id]["port"]


def run_ui_workload(engine_binary: str, task_id: str, size: str, service_container_id: str, container_port: int) -> UIWorkloadResult:
    cmd = [
        engine_binary,
        "run",
        "--rm",
        "--network",
        f"container:{service_container_id}",
        "languages-benchmark:ui-driver",
        "python",
        "/app/ui_driver.py",
        task_id,
        size,
        f"http://127.0.0.1:{container_port}/",
    ]
    started = time.perf_counter()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return UIWorkloadResult(stdout=proc.stdout, stderr=proc.stderr, returncode=proc.returncode, wall_seconds=time.perf_counter() - started)
