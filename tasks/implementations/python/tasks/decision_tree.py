import csv
from pathlib import Path

THRESHOLDS = (250, 500, 750)
MAX_DEPTH = 3


def _gini(rows):
    total = len(rows)
    if total == 0:
        return 0.0
    ones = sum(row[3] for row in rows)
    zeros = total - ones
    p0 = zeros / total
    p1 = ones / total
    return 1.0 - p0 * p0 - p1 * p1


def _majority(rows):
    ones = sum(row[3] for row in rows)
    return 1 if ones * 2 >= len(rows) else 0


def _build(rows, depth):
    if depth == 0 or not rows or all(row[3] == rows[0][3] for row in rows):
        return ("leaf", _majority(rows) if rows else 0)
    best = None
    best_score = float("inf")
    for feature in range(3):
        for threshold in THRESHOLDS:
            left = [row for row in rows if row[feature] <= threshold]
            right = [row for row in rows if row[feature] > threshold]
            if not left or not right:
                continue
            score = (len(left) * _gini(left) + len(right) * _gini(right)) / len(rows)
            if score < best_score:
                best_score = score
                best = (feature, threshold, left, right)
    if best is None:
        return ("leaf", _majority(rows))
    feature, threshold, left, right = best
    return ("node", feature, threshold, _build(left, depth - 1), _build(right, depth - 1))


def _predict(tree, row):
    kind = tree[0]
    if kind == "leaf":
        return tree[1]
    _, feature, threshold, left, right = tree
    return _predict(left if row[feature] <= threshold else right, row)


def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "decision_tree" / f"{size}.csv"
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = [(int(r["f0"]), int(r["f1"]), int(r["f2"]), int(r["label"])) for r in reader]
    tree = _build(rows, MAX_DEPTH)
    correct = 0
    pred_sum = 0
    for idx, row in enumerate(rows):
        pred = _predict(tree, row)
        if pred == row[3]:
            correct += 1
        pred_sum += pred * (idx + 1)
    print(correct * 100000 + pred_sum)
