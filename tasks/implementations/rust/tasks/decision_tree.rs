use std::fs;

const THRESHOLDS: [i64; 3] = [250, 500, 750];

#[derive(Clone)]
enum Node {
    Leaf(i64),
    Split { feature: usize, threshold: i64, left: Box<Node>, right: Box<Node> },
}

fn gini(rows: &[Vec<i64>]) -> f64 {
    if rows.is_empty() { return 0.0; }
    let ones: i64 = rows.iter().map(|row| row[3]).sum();
    let zeros = rows.len() as i64 - ones;
    let p0 = zeros as f64 / rows.len() as f64;
    let p1 = ones as f64 / rows.len() as f64;
    1.0 - p0 * p0 - p1 * p1
}

fn majority(rows: &[Vec<i64>]) -> i64 {
    let ones: i64 = rows.iter().map(|row| row[3]).sum();
    if ones * 2 >= rows.len() as i64 { 1 } else { 0 }
}

fn build(rows: &[Vec<i64>], depth: usize) -> Node {
    if depth == 0 || rows.is_empty() { return Node::Leaf(if rows.is_empty() { 0 } else { majority(rows) }); }
    if rows.iter().all(|row| row[3] == rows[0][3]) { return Node::Leaf(rows[0][3]); }
    let mut best: Option<(usize, i64, Vec<Vec<i64>>, Vec<Vec<i64>>)> = None;
    let mut best_score = f64::INFINITY;
    for feature in 0..3 {
        for threshold in THRESHOLDS {
            let mut left = Vec::new();
            let mut right = Vec::new();
            for row in rows {
                if row[feature] <= threshold { left.push(row.clone()); } else { right.push(row.clone()); }
            }
            if left.is_empty() || right.is_empty() { continue; }
            let score = (left.len() as f64 * gini(&left) + right.len() as f64 * gini(&right)) / rows.len() as f64;
            if score < best_score {
                best_score = score;
                best = Some((feature, threshold, left, right));
            }
        }
    }
    if let Some((feature, threshold, left, right)) = best {
        Node::Split { feature, threshold, left: Box::new(build(&left, depth - 1)), right: Box::new(build(&right, depth - 1)) }
    } else {
        Node::Leaf(majority(rows))
    }
}

fn predict(node: &Node, row: &[i64]) -> i64 {
    match node {
        Node::Leaf(value) => *value,
        Node::Split { feature, threshold, left, right } => {
            if row[*feature] <= *threshold { predict(left, row) } else { predict(right, row) }
        }
    }
}

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/decision_tree/{}.csv", fixtures_root, size)).unwrap();
    let mut rows: Vec<Vec<i64>> = Vec::new();
    for line in text.lines().skip(1) {
        rows.push(line.split(',').map(|x| x.parse::<i64>().unwrap()).collect());
    }
    let tree = build(&rows, 3);
    let mut correct = 0i64;
    let mut pred_sum = 0i64;
    for (idx, row) in rows.iter().enumerate() {
        let pred = predict(&tree, row);
        if pred == row[3] { correct += 1; }
        pred_sum += pred * (idx as i64 + 1);
    }
    println!("{}", correct * 100000 + pred_sum);
}
