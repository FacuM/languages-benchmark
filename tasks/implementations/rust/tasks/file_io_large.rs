use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn run(size: &str, fixtures_root: &str) {
    let path = format!("{}/generated/file_io/{}.txt", fixtures_root, size);
    let file = File::open(path).unwrap();
    let mut total = 0i64;
    for line in BufReader::new(file).lines() {
        total += line.unwrap().parse::<i64>().unwrap();
    }
    println!("{}", total);
}
