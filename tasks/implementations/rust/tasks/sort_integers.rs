use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/sort/{}.txt", fixtures_root, size)).unwrap();
    let mut values: Vec<i64> = text.split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
    values.sort();
    let total: i64 = values.iter().take(100).sum();
    println!("{}", total);
}
