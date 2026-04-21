<?php
require_once __DIR__ . '/service_support.php';
function start_chat_application(string $size, int $port, string $fixturesRoot): void {
  start_tcp_service('chat_application', $port);
}
