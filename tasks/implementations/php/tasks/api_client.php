<?php
function run_api_client(string $size, string $fixturesRoot): void {
  $text = file_get_contents($fixturesRoot . "/mocks/public_api_{$size}.json");
  preg_match_all('/"id":\s*(\d+),\s*"name":\s*"([^"]+)",\s*"value":\s*(\d+)/', $text, $matches, PREG_SET_ORDER);
  $total = 0;
  foreach ($matches as $match) $total += intval($match[1]) + intval($match[3]) + strlen($match[2]);
  echo $total . PHP_EOL;
}
