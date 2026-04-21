<?php
require_once __DIR__ . '/compat.php';
function run_cli_file_search($size, $fixturesRoot) {
  $root = $fixturesRoot . "/generated/search/{$size}";
  $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($root, FilesystemIterator::SKIP_DOTS));
  $total = 0;
  foreach ($iterator as $file) {
    if ($file->isFile() && $file->getExtension() === 'txt') {
      $handle = fopen($file->getPathname(), 'r');
      while (($line = fgets($handle)) !== false) {
        if (strpos($line, 'needle') !== false) $total += 1;
      }
      fclose($handle);
    }
  }
  echo $total . PHP_EOL;
}
