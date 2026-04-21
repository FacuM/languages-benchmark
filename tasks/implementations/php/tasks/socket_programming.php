<?php
require_once __DIR__ . '/service_support.php';
function start_socket_programming(string $size, int $port, string $fixturesRoot): void {
  start_tcp_service('socket_programming', $port);
}
