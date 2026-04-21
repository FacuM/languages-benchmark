<?php
require_once __DIR__ . '/service_support.php';
function start_sqlite_crud($size, $port, $fixturesRoot) {
  start_http_service('sqlite_crud', $port);
}
