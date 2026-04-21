const fs = require('fs');
const THRESHOLDS = [250, 500, 750];
const MAX_DEPTH = 3;

function gini(rows) {
  if (rows.length === 0) return 0;
  let ones = 0;
  for (const row of rows) ones += row[3];
  const zeros = rows.length - ones;
  const p0 = zeros / rows.length;
  const p1 = ones / rows.length;
  return 1 - p0 * p0 - p1 * p1;
}

function majority(rows) {
  let ones = 0;
  for (const row of rows) ones += row[3];
  return ones * 2 >= rows.length ? 1 : 0;
}

function build(rows, depth) {
  if (depth === 0 || rows.length === 0) return { kind: 'leaf', value: rows.length ? majority(rows) : 0 };
  if (rows.every((row) => row[3] === rows[0][3])) return { kind: 'leaf', value: rows[0][3] };
  let best = null;
  let bestScore = Infinity;
  for (let feature = 0; feature < 3; feature++) {
    for (const threshold of THRESHOLDS) {
      const left = [];
      const right = [];
      for (const row of rows) {
        if (row[feature] <= threshold) left.push(row); else right.push(row);
      }
      if (!left.length || !right.length) continue;
      const score = (left.length * gini(left) + right.length * gini(right)) / rows.length;
      if (score < bestScore) {
        bestScore = score;
        best = { feature, threshold, left, right };
      }
    }
  }
  if (!best) return { kind: 'leaf', value: majority(rows) };
  return { kind: 'node', feature: best.feature, threshold: best.threshold, left: build(best.left, depth - 1), right: build(best.right, depth - 1) };
}

function predict(tree, row) {
  if (tree.kind === 'leaf') return tree.value;
  return predict(row[tree.feature] <= tree.threshold ? tree.left : tree.right, row);
}

module.exports = function(size, fixturesRoot) {
  const lines = fs.readFileSync(`${fixturesRoot}/generated/decision_tree/${size}.csv`, 'utf8').trim().split(/\r?\n/);
  const rows = [];
  for (let i = 1; i < lines.length; i++) rows.push(lines[i].split(',').map(Number));
  const tree = build(rows, MAX_DEPTH);
  let correct = 0;
  let predSum = 0;
  for (let i = 0; i < rows.length; i++) {
    const pred = predict(tree, rows[i]);
    if (pred === rows[i][3]) correct += 1;
    predSum += pred * (i + 1);
  }
  console.log(correct * 100000 + predSum);
};
