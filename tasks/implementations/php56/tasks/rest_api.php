<?php
require_once __DIR__ . '/service_support.php';
function start_rest_api($size, $port, $fixturesRoot) {
  start_http_service('rest_api', $port);
}
