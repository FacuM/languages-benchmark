import csv

from tasks.compat import emit, join_path, open_text

THRESHOLDS = (250, 500, 750)
MAX_DEPTH = 3


def _gini(rows):
    total = len(rows)
    if total == 0:
        return 0.0
    ones = sum(row[3] for row in rows)
    zeros = total - ones
    p0 = float(zeros) / total
    p1 = float(ones) / total
    return 1.0 - p0 * p0 - p1 * p1


def _majority(rows):
    ones = sum(row[3] for row in rows)
    return 1 if ones * 2 >= len(rows) else 0


def _build(rows, depth):
    if depth == 0 or not rows:
        return ('leaf', _majority(rows) if rows else 0)
    pure = True
    first = rows[0][3]
    for row in rows:
        if row[3] != first:
            pure = False
            break
    if pure:
        return ('leaf', first)
    best = None
    best_score = float('inf')
    for feature in xrange(3):
        for threshold in THRESHOLDS:
            left = [row for row in rows if row[feature] <= threshold]
            right = [row for row in rows if row[feature] > threshold]
            if not left or not right:
                continue
            score = (len(left) * _gini(left) + len(right) * _gini(right)) / float(len(rows))
            if score < best_score:
                best_score = score
                best = (feature, threshold, left, right)
    if best is None:
        return ('leaf', _majority(rows))
    feature, threshold, left, right = best
    return ('node', feature, threshold, _build(left, depth - 1), _build(right, depth - 1))


def _predict(tree, row):
    if tree[0] == 'leaf':
        return tree[1]
    return _predict(tree[3] if row[tree[1]] <= tree[2] else tree[4], row)


def run(size, fixtures_root):
    path = join_path(fixtures_root, 'generated', 'decision_tree', '%s.csv' % size)
    handle = open_text(path)
    try:
        reader = csv.DictReader(handle)
        rows = [(int(r['f0']), int(r['f1']), int(r['f2']), int(r['label'])) for r in reader]
    finally:
        handle.close()
    tree = _build(rows, MAX_DEPTH)
    correct = 0
    pred_sum = 0
    for idx, row in enumerate(rows):
        pred = _predict(tree, row)
        if pred == row[3]:
            correct += 1
        pred_sum += pred * (idx + 1)
    emit(correct * 100000 + pred_sum)
