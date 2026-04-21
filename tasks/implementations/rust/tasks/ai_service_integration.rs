use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/mocks/ai_service_{}.json", fixtures_root, size)).unwrap();
    let mut total = quoted_value(&text, "\"model\": ").len() as i64;
    for line in text.lines() {
        if line.contains("\"prompt\"") && line.contains("\"output\"") && line.contains("\"tokens\"") {
            let prompt = quoted_value(line, "\"prompt\": ");
            let output = quoted_value(line, "\"output\": ");
            let tokens = number_after(line, "\"tokens\":");
            total += prompt.len() as i64 + output.len() as i64 + tokens;
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
