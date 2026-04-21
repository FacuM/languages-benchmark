<?php
require_once __DIR__ . '/compat.php';
const TTT_LINES = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

function ttt_winner($board, $player) {
  foreach (TTT_LINES as $line) {
    $a = $line[0];
    $b = $line[1];
    $c = $line[2];
    if ($board[$a] === $player && $board[$b] === $player && $board[$c] === $player) return true;
  }
  return false;
}

function run_tic_tac_toe($size, $fixturesRoot) {
  $lines = file($fixturesRoot . "/generated/tic_tac_toe/{$size}.txt", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
  $total = 0;
  foreach ($lines as $line) {
    $moves = array_map('intval', preg_split('/\s+/', trim($line)));
    $board = array_fill(0, 9, 0);
    $winner = 0;
    $moveCount = 0;
    foreach ($moves as $idx => $pos) {
      $player = $idx % 2 === 0 ? 1 : 2;
      $board[$pos] = $player;
      $moveCount = $idx + 1;
      if (ttt_winner($board, $player)) { $winner = $player; break; }
    }
    $boardScore = 0;
    foreach ($board as $idx => $value) $boardScore += ($idx + 1) * $value;
    $total += $winner * 100 + $moveCount * 10 + $boardScore;
  }
  echo $total . PHP_EOL;
}
