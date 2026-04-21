<?php
function run_image_resizing(string $size, string $fixturesRoot): void {
  $tokens = preg_split('/\s+/', trim(file_get_contents($fixturesRoot . "/generated/image/{$size}.ppm")));
  $width = intval($tokens[1]);
  $height = intval($tokens[2]);
  $data = array_map('intval', array_slice($tokens, 4));
  $checksum = 0;
  for ($y = 0; $y < intdiv($height, 2); $y++) {
    for ($x = 0; $x < intdiv($width, 2); $x++) {
      $idx = (($y * 2) * $width + ($x * 2)) * 3;
      $checksum += $data[$idx] + $data[$idx + 1] + $data[$idx + 2];
    }
  }
  echo $checksum . PHP_EOL;
}
