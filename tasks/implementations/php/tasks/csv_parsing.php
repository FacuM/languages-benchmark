<?php
function run_csv_parsing(string $size, string $fixturesRoot): void {
  $handle = fopen($fixturesRoot . "/generated/csv/{$size}.csv", 'r');
  $total = 0;
  fgetcsv($handle, 0, ',', '"', '\\');
  while (($row = fgetcsv($handle, 0, ',', '"', '\\')) !== false) {
    $total += intval($row[1]) + intval($row[2]);
  }
  fclose($handle);
  echo $total . PHP_EOL;
}
