const fs = require('fs');
const http = require('http');
const net = require('net');
const { execFileSync } = require('child_process');
const { URL } = require('url');
const DB_PATH = '/tmp/bench.sqlite';

function sqlite(query) {
  return execFileSync('sqlite3', [DB_PATH, query], { encoding: 'utf8' }).trim();
}

function startHttpService(task, port) {
  if (task === 'sqlite_crud') {
    sqlite('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value INTEGER);');
  }
  const server = http.createServer((req, res) => {
    const url = new URL(req.url, `http://127.0.0.1:${port}`);
    if (url.pathname === '/health') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('ok');
      return;
    }
    if (task === 'simple_web_server' && url.pathname === '/') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('hello-benchmark');
      return;
    }
    if (['gui_calculator', 'data_visualization', 'basic_web_application'].includes(task) && url.pathname === '/') {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(fs.readFileSync(`/fixtures/ui/${task}.html`, 'utf8'));
      return;
    }
    if (task === 'rest_api' && url.pathname === '/item') {
      const id = Number(url.searchParams.get('id') || '0');
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ id, value: id * 2 }));
      return;
    }
    if (task === 'sqlite_crud') {
      const id = Number(url.searchParams.get('id') || '0');
      if (url.pathname === '/create') {
        const value = Number(url.searchParams.get('value') || '0');
        sqlite(`INSERT OR REPLACE INTO items(id, value) VALUES(${id}, ${value});`);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'created', id }));
        return;
      }
      if (url.pathname === '/read') {
        const value = sqlite(`SELECT value FROM items WHERE id=${id} LIMIT 1;`);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ id, value: value ? Number(value) : null }));
        return;
      }
      if (url.pathname === '/update') {
        const value = Number(url.searchParams.get('value') || '0');
        sqlite(`UPDATE items SET value=${value} WHERE id=${id};`);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'updated', id }));
        return;
      }
      if (url.pathname === '/delete') {
        sqlite(`DELETE FROM items WHERE id=${id};`);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'deleted', id }));
        return;
      }
    }
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('not-found');
  });
  server.listen(port, '0.0.0.0');
}

function startTcpService(task, port) {
  const server = net.createServer((socket) => {
    const chunks = [];
    socket.on('data', (chunk) => chunks.push(chunk));
    socket.on('end', () => {
      if (!chunks.length) {
        socket.destroy();
        return;
      }
      const payload = Buffer.concat(chunks).toString('utf8');
      socket.end(task === 'chat_application' ? `chat:${payload}` : payload);
    });
  });
  server.listen(port, '0.0.0.0');
}

module.exports = { startHttpService, startTcpService };
