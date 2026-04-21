<?php
class BSTNode {
  public $value;
  public $left = null;
  public $right = null;
  public function __construct(int $value) { $this->value = $value; }
}

function bst_insert(?BSTNode $root, int $value): BSTNode {
  if ($root === null) return new BSTNode($value);
  $node = $root;
  while (true) {
    if ($value < $node->value) {
      if ($node->left === null) { $node->left = new BSTNode($value); return $root; }
      $node = $node->left;
    } elseif ($value > $node->value) {
      if ($node->right === null) { $node->right = new BSTNode($value); return $root; }
      $node = $node->right;
    } else {
      return $root;
    }
  }
}

function bst_contains(?BSTNode $root, int $value): bool {
  $node = $root;
  while ($node !== null) {
    if ($value < $node->value) $node = $node->left;
    elseif ($value > $node->value) $node = $node->right;
    else return true;
  }
  return false;
}

function run_binary_search_tree(string $size, string $fixturesRoot): void {
  $tokens = array_map('intval', preg_split('/\s+/', trim(file_get_contents($fixturesRoot . "/generated/bst/{$size}.txt"))));
  $insertCount = $tokens[0];
  $inserts = array_slice($tokens, 1, $insertCount);
  $queryIndex = 1 + $insertCount;
  $queryCount = $tokens[$queryIndex];
  $queries = array_slice($tokens, $queryIndex + 1, $queryCount);
  $root = null;
  foreach ($inserts as $value) $root = bst_insert($root, $value);
  $total = 0;
  foreach ($queries as $value) if (bst_contains($root, $value)) $total += $value;
  echo $total . PHP_EOL;
}
