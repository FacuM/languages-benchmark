use std::fs;

struct Node {
    value: i64,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

fn insert(root: &mut Option<Box<Node>>, value: i64) {
    let mut cursor = root;
    loop {
        match cursor {
            Some(node) => {
                if value < node.value {
                    cursor = &mut node.left;
                } else if value > node.value {
                    cursor = &mut node.right;
                } else {
                    return;
                }
            }
            None => {
                *cursor = Some(Box::new(Node { value, left: None, right: None }));
                return;
            }
        }
    }
}

fn contains(root: &Option<Box<Node>>, value: i64) -> bool {
    let mut cursor = root.as_ref();
    while let Some(node) = cursor {
        if value < node.value {
            cursor = node.left.as_ref();
        } else if value > node.value {
            cursor = node.right.as_ref();
        } else {
            return true;
        }
    }
    false
}

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/bst/{}.txt", fixtures_root, size)).unwrap();
    let tokens: Vec<i64> = text.split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
    let insert_count = tokens[0] as usize;
    let mut root: Option<Box<Node>> = None;
    for value in &tokens[1..1 + insert_count] {
        insert(&mut root, *value);
    }
    let query_index = 1 + insert_count;
    let query_count = tokens[query_index] as usize;
    let mut total = 0i64;
    for value in &tokens[query_index + 1..query_index + 1 + query_count] {
        if contains(&root, *value) {
            total += *value;
        }
    }
    println!("{}", total);
}
