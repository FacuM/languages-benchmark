<?php
require_once __DIR__ . '/service_support.php';
function start_data_visualization($size, $port, $fixturesRoot) {
  start_http_service('data_visualization', $port);
}
