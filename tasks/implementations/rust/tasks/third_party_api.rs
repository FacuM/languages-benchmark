use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/mocks/twitter_like_{}.json", fixtures_root, size)).unwrap();
    let mut total = 0i64;
    for line in text.lines() {
        if line.contains("\"id\"") && line.contains("\"text\"") && line.contains("\"likes\"") {
            let id = quoted_value(line, "\"id\": ");
            let body = quoted_value(line, "\"text\": ");
            let likes = number_after(line, "\"likes\":");
            total += id.len() as i64 + body.len() as i64 + likes;
        }
    }
    println!("{}", total);
}

fn number_after(text: &str, needle: &str) -> i64 {
    let start = text.find(needle).unwrap() + needle.len();
    let digits: String = text[start..]
        .chars()
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| c.is_ascii_digit())
        .collect();
    digits.parse::<i64>().unwrap()
}

fn quoted_value(text: &str, needle: &str) -> String {
    let start = text.find(needle).unwrap() + needle.len();
    let rest = &text[start..];
    let first_quote = rest.find('"').unwrap();
    let rest2 = &rest[first_quote + 1..];
    let end = rest2.find('"').unwrap();
    rest2[..end].to_string()
}
