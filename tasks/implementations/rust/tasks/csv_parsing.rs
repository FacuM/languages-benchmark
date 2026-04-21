use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/csv/{}.csv", fixtures_root, size)).unwrap();
    let mut total = 0i64;
    for line in text.lines().skip(1) {
        let parts: Vec<&str> = line.split(',').collect();
        total += parts[1].parse::<i64>().unwrap() + parts[2].parse::<i64>().unwrap();
    }
    println!("{}", total);
}
