<?php
require_once __DIR__ . '/compat.php';
const DB_PATH = '/tmp/bench.sqlite';

function sqlite_query_raw($query) {
  $command = 'sqlite3 ' . escapeshellarg(DB_PATH) . ' ' . escapeshellarg($query);
  $output = shell_exec($command);
  return trim($output === null ? '' : $output);
}

function start_http_service($task, $port) {
  if ($task === 'sqlite_crud') {
    sqlite_query_raw('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value INTEGER);');
  }
  $server = stream_socket_server("tcp://0.0.0.0:$port", $errno, $errstr);
  if ($server === false) {
    fwrite(STDERR, "server error: $errstr
");
    exit(1);
  }
  while ($conn = @stream_socket_accept($server, -1)) {
    $request = '';
    while (!lb_contains($request, "

")) {
      $chunk = fread($conn, 4096);
      if ($chunk === '' || $chunk === false) break;
      $request .= $chunk;
      if (strlen($request) > 65535) break;
    }
    list($status, $type, $body) = handle_http_request($task, $request);
    $response = "HTTP/1.1 $status
Content-Type: $type
Content-Length: " . strlen($body) . "
Connection: close

" . $body;
    fwrite($conn, $response);
    fclose($conn);
  }
}

function handle_http_request($task, $request) {
  $line = strtok($request, "
");
  if ($line === false) $line = 'GET / HTTP/1.1';
  $parts = explode(' ', $line);
  $target = isset($parts[1]) ? $parts[1] : '/';
  $parsed = parse_url($target);
  $path = isset($parsed['path']) ? $parsed['path'] : '/';
  parse_str(isset($parsed['query']) ? $parsed['query'] : '', $query);

  if ($path === '/health') return array('200 OK', 'text/plain', 'ok');
  if ($task === 'simple_web_server' && $path === '/') return array('200 OK', 'text/plain', 'hello-benchmark');
  if ($task === 'rest_api' && $path === '/item') {
    $id = intval(lb_get($query, 'id', 0));
    return array('200 OK', 'application/json', json_encode(array('id' => $id, 'value' => $id * 2)));
  }
  if (in_array($task, array('gui_calculator', 'data_visualization', 'basic_web_application'), true) && $path === '/') {
    return array('200 OK', 'text/html; charset=utf-8', file_get_contents('/fixtures/ui/' . $task . '.html'));
  }
  if ($task === 'sqlite_crud') {
    $id = intval(lb_get($query, 'id', 0));
    if ($path === '/create') {
      $value = intval(lb_get($query, 'value', 0));
      sqlite_query_raw("INSERT OR REPLACE INTO items(id, value) VALUES($id, $value);");
      return array('200 OK', 'application/json', json_encode(array('status' => 'created', 'id' => $id)));
    }
    if ($path === '/read') {
      $value = sqlite_query_raw("SELECT value FROM items WHERE id=$id LIMIT 1;");
      return array('200 OK', 'application/json', json_encode(array('id' => $id, 'value' => $value === '' ? null : intval($value))));
    }
    if ($path === '/update') {
      $value = intval(lb_get($query, 'value', 0));
      sqlite_query_raw("UPDATE items SET value=$value WHERE id=$id;");
      return array('200 OK', 'application/json', json_encode(array('status' => 'updated', 'id' => $id)));
    }
    if ($path === '/delete') {
      sqlite_query_raw("DELETE FROM items WHERE id=$id;");
      return array('200 OK', 'application/json', json_encode(array('status' => 'deleted', 'id' => $id)));
    }
  }
  return array('404 Not Found', 'text/plain', 'not-found');
}

function start_tcp_service($task, $port) {
  $server = stream_socket_server("tcp://0.0.0.0:$port", $errno, $errstr);
  if ($server === false) {
    fwrite(STDERR, "server error: $errstr
");
    exit(1);
  }
  while ($conn = @stream_socket_accept($server, -1)) {
    $payload = stream_get_contents($conn);
    if ($payload === false || $payload === '') {
      fclose($conn);
      continue;
    }
    $response = $task === 'chat_application' ? 'chat:' . $payload : $payload;
    fwrite($conn, $response);
    fclose($conn);
  }
}
