<?php
function run_third_party_api(string $size, string $fixturesRoot): void {
  $text = file_get_contents($fixturesRoot . "/mocks/twitter_like_{$size}.json");
  preg_match_all('/"id":\s*"([^"]+)",\s*"text":\s*"([^"]+)",\s*"likes":\s*(\d+)/', $text, $matches, PREG_SET_ORDER);
  $total = 0;
  foreach ($matches as $match) $total += strlen($match[1]) + strlen($match[2]) + intval($match[3]);
  echo $total . PHP_EOL;
}
