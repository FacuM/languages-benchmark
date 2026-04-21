<?php
function run_web_scraper(string $size, string $fixturesRoot): void {
  $base = $fixturesRoot . "/mock_site/{$size}";
  $index = file_get_contents($base . '/index.html');
  preg_match_all('/href="([^"]+)"/', $index, $matches);
  $total = 0;
  foreach ($matches[1] as $idx => $link) {
    $page = file_get_contents($base . '/' . $link);
    preg_match('/<h2>(.*?)<\/h2>/', $page, $title);
    preg_match('/<p>(.*?)<\/p>/', $page, $body);
    $total += ($idx + 1) * (strlen($title[1]) + strlen($body[1]));
  }
  echo $total . PHP_EOL;
}
