use std::fs;
use std::path::Path;

fn walk(path: &Path) -> i64 {
    let mut total = 0i64;
    for entry in fs::read_dir(path).unwrap() {
        let entry = entry.unwrap();
        let entry_path = entry.path();
        if entry_path.is_dir() {
            total += walk(&entry_path);
        } else if entry_path.extension().and_then(|ext| ext.to_str()) == Some("txt") {
            let text = fs::read_to_string(entry_path).unwrap();
            for line in text.lines() {
                if line.contains("needle") {
                    total += 1;
                }
            }
        }
    }
    total
}

pub fn run(size: &str, fixtures_root: &str) {
    let root = Path::new(fixtures_root).join("generated").join("search").join(size);
    println!("{}", walk(&root));
}
