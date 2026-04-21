<?php
require_once __DIR__ . '/service_support.php';
function start_simple_web_server(string $size, int $port, string $fixturesRoot): void {
  start_http_service('simple_web_server', $port);
}
