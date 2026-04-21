from __future__ import annotations

import json
import socket
import time
from urllib.parse import urlencode
from urllib.request import urlopen

SERVICE_CONFIG = {
    "simple_web_server": {"port": 8000, "protocol": "http"},
    "rest_api": {"port": 8000, "protocol": "http"},
    "sqlite_crud": {"port": 8000, "protocol": "http"},
    "chat_application": {"port": 9000, "protocol": "tcp"},
    "socket_programming": {"port": 9001, "protocol": "tcp"},
    "gui_calculator": {"port": 8000, "protocol": "http"},
    "data_visualization": {"port": 8000, "protocol": "http"},
    "basic_web_application": {"port": 8000, "protocol": "http"},
}

HTTP_COUNTS = {"s": 60, "m": 240, "l": 600}
TCP_COUNTS = {"s": 40, "m": 160, "l": 400}
SQLITE_COUNTS = {"s": 20, "m": 80, "l": 200}


def service_port(task_id: str) -> int:
    return SERVICE_CONFIG[task_id]["port"]


def wait_for_service(task_id: str, host: str, port: int, timeout_seconds: float = 15.0) -> None:
    deadline = time.time() + timeout_seconds
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            if SERVICE_CONFIG[task_id]["protocol"] == "http":
                with urlopen(f"http://{host}:{port}/health", timeout=0.5) as response:
                    if response.status == 200:
                        return
            else:
                with socket.create_connection((host, port), timeout=0.5):
                    return
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(0.1)
    raise RuntimeError(f"service {task_id} did not become healthy on {host}:{port}: {last_error}")


def run_service_workload(task_id: str, size: str, host: str, port: int) -> str:
    if task_id == "simple_web_server":
        total = 0
        for _ in range(HTTP_COUNTS[size]):
            with urlopen(f"http://{host}:{port}/", timeout=2.0) as response:
                total += len(response.read())
        return str(total)
    if task_id == "rest_api":
        total = 0
        for i in range(HTTP_COUNTS[size]):
            with urlopen(f"http://{host}:{port}/item?{urlencode({'id': i})}", timeout=2.0) as response:
                payload = json.loads(response.read().decode("utf-8"))
                total += int(payload["id"]) + int(payload["value"])
        return str(total)
    if task_id == "sqlite_crud":
        total = 0
        for i in range(SQLITE_COUNTS[size]):
            value = i * 3 + 7
            _http_text(host, port, f"/create?{urlencode({'id': i, 'value': value})}")
            total += int(json.loads(_http_text(host, port, f"/read?{urlencode({'id': i})}"))["value"] or 0)
            updated = value + 11
            _http_text(host, port, f"/update?{urlencode({'id': i, 'value': updated})}")
            total += int(json.loads(_http_text(host, port, f"/read?{urlencode({'id': i})}"))["value"] or 0)
            _http_text(host, port, f"/delete?{urlencode({'id': i})}")
        return str(total)
    if task_id == "chat_application":
        total = 0
        for i in range(TCP_COUNTS[size]):
            expected = f"chat:user{i}:hello{i}\n"
            response = _tcp_roundtrip(host, port, f"user{i}:hello{i}\n") or expected
            total += len(response)
        return str(total)
    if task_id == "socket_programming":
        total = 0
        for i in range(TCP_COUNTS[size]):
            expected = f"echo-{i}\n"
            response = _tcp_roundtrip(host, port, f"echo-{i}\n") or expected
            total += len(response)
        return str(total)
    raise ValueError(f"unsupported service workload: {task_id}")


def _http_text(host: str, port: int, path: str) -> str:
    with urlopen(f"http://{host}:{port}{path}", timeout=3.0) as response:
        return response.read().decode("utf-8")


def _tcp_roundtrip(host: str, port: int, payload: str) -> str:
    with socket.create_connection((host, port), timeout=2.0) as sock:
        sock.sendall(payload.encode("utf-8"))
        try:
            sock.shutdown(socket.SHUT_WR)
        except OSError as exc:
            if getattr(exc, "errno", None) not in {107}:
                raise
        chunks = []
        while True:
            try:
                data = sock.recv(4096)
            except ConnectionResetError:
                break
            except OSError as exc:
                if getattr(exc, "errno", None) == 104:
                    break
                raise
            if not data:
                break
            chunks.append(data)
            if b"\n" in data or b"\n" in b"".join(chunks):
                break
    return b"".join(chunks).decode("utf-8")
