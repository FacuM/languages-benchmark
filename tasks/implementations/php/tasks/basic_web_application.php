<?php
require_once __DIR__ . '/service_support.php';
function start_basic_web_application(string $size, int $port, string $fixturesRoot): void {
  start_http_service('basic_web_application', $port);
}
