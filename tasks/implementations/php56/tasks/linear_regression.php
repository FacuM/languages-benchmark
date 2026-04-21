<?php
require_once __DIR__ . '/compat.php';
function run_linear_regression($size, $fixturesRoot) {
  $handle = fopen($fixturesRoot . "/generated/linear_regression/{$size}.csv", 'r');
  fgetcsv($handle, 0, ',', '"', '\\');
  $n = 0.0; $sumX = 0.0; $sumY = 0.0; $sumXY = 0.0; $sumX2 = 0.0;
  while (($row = fgetcsv($handle, 0, ',', '"', '\\')) !== false) {
    $x = floatval($row[0]);
    $y = floatval($row[1]);
    $n += 1.0;
    $sumX += $x; $sumY += $y; $sumXY += $x * $y; $sumX2 += $x * $x;
  }
  fclose($handle);
  $slope = ($n * $sumXY - $sumX * $sumY) / ($n * $sumX2 - $sumX * $sumX);
  $intercept = ($sumY - $slope * $sumX) / $n;
  $checksum = round($slope * 1000000) + round($intercept * 1000000);
  echo intval($checksum) . PHP_EOL;
}
