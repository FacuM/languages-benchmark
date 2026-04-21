<?php
const SENTIMENT_POSITIVE = ['good' => true, 'great' => true, 'happy' => true, 'clean' => true, 'fast' => true, 'love' => true];
const SENTIMENT_NEGATIVE = ['bad' => true, 'sad' => true, 'dirty' => true, 'slow' => true, 'hate' => true, 'poor' => true];

function run_sentiment_analysis(string $size, string $fixturesRoot): void {
  $lines = file($fixturesRoot . "/generated/sentiment/{$size}.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
  $total = 0;
  foreach ($lines as $line) {
    foreach (preg_split('/\s+/', trim($line)) as $token) {
      if (isset(SENTIMENT_POSITIVE[$token])) $total += 1;
      elseif (isset(SENTIMENT_NEGATIVE[$token])) $total -= 1;
    }
  }
  echo $total . PHP_EOL;
}
