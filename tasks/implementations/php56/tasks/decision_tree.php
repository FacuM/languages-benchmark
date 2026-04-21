<?php
require_once __DIR__ . '/compat.php';
const DT_THRESHOLDS = [250, 500, 750];
const DT_MAX_DEPTH = 3;

function dt_gini($rows) {
  $total = count($rows);
  if ($total === 0) return 0.0;
  $ones = 0;
  foreach ($rows as $row) $ones += $row[3];
  $zeros = $total - $ones;
  $p0 = $zeros / $total;
  $p1 = $ones / $total;
  return 1.0 - $p0 * $p0 - $p1 * $p1;
}

function dt_majority($rows) {
  $ones = 0;
  foreach ($rows as $row) $ones += $row[3];
  return $ones * 2 >= count($rows) ? 1 : 0;
}

function dt_build($rows, $depth) {
  if ($depth === 0 || count($rows) === 0) return ['leaf', count($rows) ? dt_majority($rows) : 0];
  $pure = true;
  foreach ($rows as $row) { if ($row[3] !== $rows[0][3]) { $pure = false; break; } }
  if ($pure) return ['leaf', $rows[0][3]];
  $best = null;
  $bestScore = INF;
  for ($feature = 0; $feature < 3; $feature++) {
    foreach (DT_THRESHOLDS as $threshold) {
      $left = [];
      $right = [];
      foreach ($rows as $row) {
        if ($row[$feature] <= $threshold) $left[] = $row; else $right[] = $row;
      }
      if (!$left || !$right) continue;
      $score = (count($left) * dt_gini($left) + count($right) * dt_gini($right)) / count($rows);
      if ($score < $bestScore) {
        $bestScore = $score;
        $best = [$feature, $threshold, $left, $right];
      }
    }
  }
  if ($best === null) return ['leaf', dt_majority($rows)];
  $feature = $best[0];
  $threshold = $best[1];
  $left = $best[2];
  $right = $best[3];
  return ['node', $feature, $threshold, dt_build($left, $depth - 1), dt_build($right, $depth - 1)];
}

function dt_predict($tree, $row) {
  if ($tree[0] === 'leaf') return $tree[1];
  return $row[$tree[1]] <= $tree[2] ? dt_predict($tree[3], $row) : dt_predict($tree[4], $row);
}

function run_decision_tree($size, $fixturesRoot) {
  $handle = fopen($fixturesRoot . "/generated/decision_tree/{$size}.csv", 'r');
  fgetcsv($handle, 0, ',', '"', '\\');
  $rows = [];
  while (($row = fgetcsv($handle, 0, ',', '"', '\\')) !== false) {
    $rows[] = [intval($row[0]), intval($row[1]), intval($row[2]), intval($row[3])];
  }
  fclose($handle);
  $tree = dt_build($rows, DT_MAX_DEPTH);
  $correct = 0;
  $predSum = 0;
  foreach ($rows as $idx => $row) {
    $pred = dt_predict($tree, $row);
    if ($pred === $row[3]) $correct += 1;
    $predSum += $pred * ($idx + 1);
  }
  echo ($correct * 100000 + $predSum) . PHP_EOL;
}
