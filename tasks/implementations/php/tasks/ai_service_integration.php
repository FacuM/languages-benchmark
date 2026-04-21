<?php
function run_ai_service_integration(string $size, string $fixturesRoot): void {
  $text = file_get_contents($fixturesRoot . "/mocks/ai_service_{$size}.json");
  preg_match('/"model":\s*"([^"]+)"/', $text, $model);
  preg_match_all('/"prompt":\s*"([^"]+)",\s*"output":\s*"([^"]+)",\s*"tokens":\s*(\d+)/', $text, $matches, PREG_SET_ORDER);
  $total = strlen($model[1]);
  foreach ($matches as $match) $total += strlen($match[1]) + strlen($match[2]) + intval($match[3]);
  echo $total . PHP_EOL;
}
