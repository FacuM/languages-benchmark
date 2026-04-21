<?php
require_once __DIR__ . '/compat.php';
function run_sort_integers($size, $fixturesRoot) {
  $path = $fixturesRoot . "/generated/sort/{$size}.txt";
  $values = array_map('intval', preg_split('/\s+/', trim(file_get_contents($path))));
  sort($values, SORT_NUMERIC);
  echo array_sum(array_slice($values, 0, 100)) . PHP_EOL;
}
