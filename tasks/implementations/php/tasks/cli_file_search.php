<?php
function run_cli_file_search(string $size, string $fixturesRoot): void {
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
