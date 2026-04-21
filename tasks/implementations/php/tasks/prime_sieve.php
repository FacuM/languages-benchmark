<?php
function run_prime_sieve(string $size, string $fixturesRoot): void {
  $limits = ['s' => 50000, 'm' => 125000, 'l' => 250000];
  $n = $limits[$size];
  $sieve = array_fill(0, $n + 1, true);
  $sieve[0] = false; $sieve[1] = false;
  for ($p = 2; $p * $p <= $n; $p++) {
    if ($sieve[$p]) {
      for ($i = $p * $p; $i <= $n; $i += $p) $sieve[$i] = false;
    }
  }
  $count = 0;
  foreach ($sieve as $isPrime) if ($isPrime) $count++;
  echo $count . PHP_EOL;
}
