<?php
function run_file_io_large(string $size, string $fixturesRoot): void {
  $path = $fixturesRoot . "/generated/file_io/{$size}.txt";
  $handle = fopen($path, 'r');
  $total = 0;
  while (($line = fgets($handle)) !== false) {
    $total += intval(trim($line));
  }
  fclose($handle);
  echo $total . PHP_EOL;
}
