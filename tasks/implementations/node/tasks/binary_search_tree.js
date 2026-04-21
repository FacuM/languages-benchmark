const fs = require('fs');
class Node {
  constructor(value) { this.value = value; this.left = null; this.right = null; }
}
function insert(root, value) {
  if (!root) return new Node(value);
  let node = root;
  while (true) {
    if (value < node.value) {
      if (!node.left) { node.left = new Node(value); return root; }
      node = node.left;
    } else if (value > node.value) {
      if (!node.right) { node.right = new Node(value); return root; }
      node = node.right;
    } else {
      return root;
    }
  }
}
function contains(root, value) {
  let node = root;
  while (node) {
    if (value < node.value) node = node.left;
    else if (value > node.value) node = node.right;
    else return true;
  }
  return false;
}
module.exports = function(size, fixturesRoot) {
  const tokens = fs.readFileSync(`${fixturesRoot}/generated/bst/${size}.txt`, 'utf8').trim().split(/\s+/).map(Number);
  const insertCount = tokens[0];
  const inserts = tokens.slice(1, 1 + insertCount);
  const queryIndex = 1 + insertCount;
  const queryCount = tokens[queryIndex];
  const queries = tokens.slice(queryIndex + 1, queryIndex + 1 + queryCount);
  let root = null;
  for (const value of inserts) root = insert(root, value);
  let total = 0;
  for (const value of queries) if (contains(root, value)) total += value;
  console.log(total);
};
