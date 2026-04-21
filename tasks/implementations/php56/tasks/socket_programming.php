<?php
require_once __DIR__ . '/service_support.php';
function start_socket_programming($size, $port, $fixturesRoot) {
  start_tcp_service('socket_programming', $port);
}
