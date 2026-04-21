import json
import os
import socket
import subprocess

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs, urlparse

from tasks.compat import join_path, read_text

DB_PATH = '/tmp/bench.sqlite'


def _sqlite(query):
    proc = subprocess.Popen(['sqlite3', DB_PATH, query], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _stderr = proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError('sqlite3 failed')
    if not isinstance(stdout, str):
        stdout = stdout.decode('utf-8')
    return stdout.strip()


def start_http_service(task, port):
    if task == 'sqlite_crud':
        _sqlite('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value INTEGER);')

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            path = parsed.path or '/'
            if path == '/health':
                self._respond(200, 'text/plain', 'ok')
                return
            if task == 'simple_web_server' and path == '/':
                self._respond(200, 'text/plain', 'hello-benchmark')
                return
            if task in ('gui_calculator', 'data_visualization', 'basic_web_application') and path == '/':
                body = read_text(join_path('/fixtures', 'ui', task + '.html'))
                self._respond(200, 'text/html; charset=utf-8', body)
                return
            if task == 'rest_api' and path == '/item':
                item_id = int(query.get('id', ['0'])[0])
                self._respond_json({'id': item_id, 'value': item_id * 2})
                return
            if task == 'sqlite_crud':
                item_id = int(query.get('id', ['0'])[0])
                if path == '/create':
                    value = int(query.get('value', ['0'])[0])
                    _sqlite('INSERT OR REPLACE INTO items(id, value) VALUES({0}, {1});'.format(item_id, value))
                    self._respond_json({'status': 'created', 'id': item_id})
                    return
                if path == '/read':
                    value = _sqlite('SELECT value FROM items WHERE id={0} LIMIT 1;'.format(item_id))
                    self._respond_json({'id': item_id, 'value': int(value) if value else None})
                    return
                if path == '/update':
                    value = int(query.get('value', ['0'])[0])
                    _sqlite('UPDATE items SET value={0} WHERE id={1};'.format(value, item_id))
                    self._respond_json({'status': 'updated', 'id': item_id})
                    return
                if path == '/delete':
                    _sqlite('DELETE FROM items WHERE id={0};'.format(item_id))
                    self._respond_json({'status': 'deleted', 'id': item_id})
                    return
            self._respond(404, 'text/plain', 'not-found')

        def log_message(self, *_args):
            return

        def _respond(self, status, content_type, body):
            if isinstance(body, unicode):
                payload = body.encode('utf-8')
            else:
                payload = body
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def _respond_json(self, obj):
            self._respond(200, 'application/json', json.dumps(obj))

    HTTPServer(('0.0.0.0', port), Handler).serve_forever()


def start_tcp_service(task, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', port))
    server.listen(128)
    try:
        while True:
            conn, _addr = server.accept()
            try:
                data = conn.recv(4096)
                if not data:
                    continue
                if not isinstance(data, str):
                    payload = data.decode('utf-8')
                else:
                    payload = data
                response = ('chat:' + payload) if task == 'chat_application' else payload
                conn.sendall(response if isinstance(response, str) else response.encode('utf-8'))
            finally:
                conn.close()
    finally:
        server.close()
