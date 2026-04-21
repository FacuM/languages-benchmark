use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/linear_regression/{}.csv", fixtures_root, size)).unwrap();
    let mut n = 0f64;
    let mut sum_x = 0f64;
    let mut sum_y = 0f64;
    let mut sum_xy = 0f64;
    let mut sum_x2 = 0f64;
    for line in text.lines().skip(1) {
        let mut parts = line.split(',');
        let x = parts.next().unwrap().parse::<f64>().unwrap();
        let y = parts.next().unwrap().parse::<f64>().unwrap();
        n += 1.0;
        sum_x += x;
        sum_y += y;
        sum_xy += x * y;
        sum_x2 += x * x;
    }
    let slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x);
    let intercept = (sum_y - slope * sum_x) / n;
    let checksum = (slope * 1_000_000.0).round() as i64 + (intercept * 1_000_000.0).round() as i64;
    println!("{}", checksum);
}
