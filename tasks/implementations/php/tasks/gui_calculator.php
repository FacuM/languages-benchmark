<?php
require_once __DIR__ . '/service_support.php';
function start_gui_calculator(string $size, int $port, string $fixturesRoot): void {
  start_http_service('gui_calculator', $port);
}
