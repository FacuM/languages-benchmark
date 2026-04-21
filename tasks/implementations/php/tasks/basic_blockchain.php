<?php
const BC_MOD = 4294967291;
const BC_MULT = 16777619;

function run_basic_blockchain(string $size, string $fixturesRoot): void {
  $lines = file($fixturesRoot . "/generated/blockchain/{$size}.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
  $prevHash = 2166136261;
  $total = 0;
  foreach ($lines as $index => $line) {
    $hashValue = $prevHash;
    foreach (preg_split('/\s+/', trim($line)) as $token) {
      $hashValue = ($hashValue * BC_MULT + intval($token) + $index + 1) % BC_MOD;
    }
    $total = ($total + $hashValue) % BC_MOD;
    $prevHash = $hashValue;
  }
  echo $total . PHP_EOL;
}
