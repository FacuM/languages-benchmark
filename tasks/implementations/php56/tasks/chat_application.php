<?php
require_once __DIR__ . '/service_support.php';
function start_chat_application($size, $port, $fixturesRoot) {
  start_tcp_service('chat_application', $port);
}
