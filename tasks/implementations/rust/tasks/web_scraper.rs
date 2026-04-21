use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let base = format!("{}/mock_site/{}", fixtures_root, size);
    let index = fs::read_to_string(format!("{}/index.html", base)).unwrap();
    let mut total = 0i64;
    let mut idx = 0i64;
    for link in index.match_indices("href=\"") {
        let start = link.0 + 6;
        let rest = &index[start..];
        let end = rest.find('"').unwrap();
        let path = &rest[..end];
        let page = fs::read_to_string(format!("{}/{}", base, path)).unwrap();
        let title = between(&page, "<h2>", "</h2>");
        let body = between(&page, "<p>", "</p>");
        idx += 1;
        total += idx * (title.len() as i64 + body.len() as i64);
    }
    println!("{}", total);
}

fn between<'a>(text: &'a str, left: &str, right: &str) -> &'a str {
    let start = text.find(left).unwrap() + left.len();
    let rest = &text[start..];
    let end = rest.find(right).unwrap();
    &rest[..end]
}
