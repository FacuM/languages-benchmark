import json
import socket
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

DB_PATH = "/tmp/bench.sqlite"


def _sqlite(query: str) -> str:
    proc = subprocess.run(["sqlite3", DB_PATH, query], check=True, capture_output=True, text=True)
    return proc.stdout.strip()


def start_http_service(task: str, port: int) -> None:
    if task == "sqlite_crud":
        _sqlite("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value INTEGER);")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            if parsed.path == "/health":
                self._respond(200, "text/plain", "ok")
                return
            if task == "simple_web_server" and parsed.path == "/":
                self._respond(200, "text/plain", "hello-benchmark")
                return
            if task in {"gui_calculator", "data_visualization", "basic_web_application"} and parsed.path == "/":
                body = (Path("/fixtures") / "ui" / f"{task}.html").read_text(encoding="utf-8")
                self._respond(200, "text/html; charset=utf-8", body)
                return
            if task == "rest_api" and parsed.path == "/item":
                item_id = int(query.get("id", ["0"])[0])
                self._respond_json({"id": item_id, "value": item_id * 2})
                return
            if task == "sqlite_crud":
                item_id = int(query.get("id", ["0"])[0])
                if parsed.path == "/create":
                    value = int(query.get("value", ["0"])[0])
                    _sqlite(f"INSERT OR REPLACE INTO items(id, value) VALUES({item_id}, {value});")
                    self._respond_json({"status": "created", "id": item_id})
                    return
                if parsed.path == "/read":
                    value = _sqlite(f"SELECT value FROM items WHERE id={item_id} LIMIT 1;")
                    self._respond_json({"id": item_id, "value": int(value) if value else None})
                    return
                if parsed.path == "/update":
                    value = int(query.get("value", ["0"])[0])
                    _sqlite(f"UPDATE items SET value={value} WHERE id={item_id};")
                    self._respond_json({"status": "updated", "id": item_id})
                    return
                if parsed.path == "/delete":
                    _sqlite(f"DELETE FROM items WHERE id={item_id};")
                    self._respond_json({"status": "deleted", "id": item_id})
                    return
            self._respond(404, "text/plain", "not-found")

        def log_message(self, *_args):
            return

        def _respond(self, status: int, content_type: str, body: str):
            payload = body.encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def _respond_json(self, obj):
            self._respond(200, "application/json", json.dumps(obj))

    HTTPServer(("0.0.0.0", port), Handler).serve_forever()


def start_tcp_service(task: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("0.0.0.0", port))
        server.listen()
        while True:
            conn, _ = server.accept()
            with conn:
                data = conn.recv(4096)
                if not data:
                    continue
                payload = data.decode("utf-8")
                response = ("chat:" + payload) if task == "chat_application" else payload
                conn.sendall(response.encode("utf-8"))
