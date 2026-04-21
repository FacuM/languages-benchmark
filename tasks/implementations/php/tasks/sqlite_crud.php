<?php
require_once __DIR__ . '/service_support.php';
function start_sqlite_crud(string $size, int $port, string $fixturesRoot): void {
  start_http_service('sqlite_crud', $port);
}
