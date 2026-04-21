<?php
require_once __DIR__ . '/service_support.php';
function start_gui_calculator($size, $port, $fixturesRoot) {
  start_http_service('gui_calculator', $port);
}
