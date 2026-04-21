<?php
require_once __DIR__ . '/compat.php';
const SENTIMENT_POSITIVE = ['good' => true, 'great' => true, 'happy' => true, 'clean' => true, 'fast' => true, 'love' => true];
const SENTIMENT_NEGATIVE = ['bad' => true, 'sad' => true, 'dirty' => true, 'slow' => true, 'hate' => true, 'poor' => true];

function run_sentiment_analysis($size, $fixturesRoot) {
  $lines = file($fixturesRoot . "/generated/sentiment/{$size}.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
  $total = 0;
  $positive = SENTIMENT_POSITIVE;
  $negative = SENTIMENT_NEGATIVE;
  foreach ($lines as $line) {
    foreach (preg_split('/\s+/', trim($line)) as $token) {
      if (isset($positive[$token])) $total += 1;
      elseif (isset($negative[$token])) $total -= 1;
    }
  }
  echo $total . PHP_EOL;
}
