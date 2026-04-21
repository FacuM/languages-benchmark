<?php
const PC_MOD = 4294967291;
const PC_CAPACITY = 64;

function run_producer_consumer(string $size, string $fixturesRoot): void {
  $values = array_map('intval', preg_split('/\s+/', trim(file_get_contents($fixturesRoot . "/generated/producer_consumer/{$size}.txt"))));
  $buffer = array_fill(0, PC_CAPACITY, 0);
  $head = 0; $tail = 0; $count = 0; $produced = 0; $consumed = 0; $checksum = 0;
  $total = count($values);
  while ($produced < $total || $count > 0) {
    while ($produced < $total && $count < PC_CAPACITY) {
      $buffer[$tail] = $values[$produced];
      $tail = ($tail + 1) % PC_CAPACITY;
      $produced += 1;
      $count += 1;
    }
    if ($count > 0) {
      $value = $buffer[$head];
      $head = ($head + 1) % PC_CAPACITY;
      $count -= 1;
      $checksum = ($checksum + $value * ($consumed + 1)) % PC_MOD;
      $consumed += 1;
    }
  }
  echo $checksum . PHP_EOL;
}
