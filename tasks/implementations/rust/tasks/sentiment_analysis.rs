use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/sentiment/{}.txt", fixtures_root, size)).unwrap();
    let mut total = 0i64;
    for token in text.split_whitespace() {
        match token {
            "good" | "great" | "happy" | "clean" | "fast" | "love" => total += 1,
            "bad" | "sad" | "dirty" | "slow" | "hate" | "poor" => total -= 1,
            _ => {}
        }
    }
    println!("{}", total);
}
