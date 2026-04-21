<?php
function run_matrix_multiplication(string $size, string $fixturesRoot): void {
  $tokens = array_map('intval', preg_split('/\s+/', trim(file_get_contents($fixturesRoot . "/generated/matrix/{$size}.txt"))));
  $n = array_shift($tokens);
  $split = $n * $n;
  $a = array_slice($tokens, 0, $split);
  $b = array_slice($tokens, $split);
  $total = 0;
  for ($i = 0; $i < $n; $i++) {
    for ($j = 0; $j < $n; $j++) {
      $cell = 0;
      for ($k = 0; $k < $n; $k++) {
        $cell += $a[$i * $n + $k] * $b[$k * $n + $j];
      }
      $total += $cell;
    }
  }
  echo $total . PHP_EOL;
}
