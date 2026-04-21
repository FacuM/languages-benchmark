use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/matrix/{}.txt", fixtures_root, size)).unwrap();
    let tokens: Vec<i64> = text.split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
    let n = tokens[0] as usize;
    let nums = &tokens[1..];
    let split = n * n;
    let a = &nums[..split];
    let b = &nums[split..];
    let mut total = 0i64;
    for i in 0..n {
        for j in 0..n {
            let mut cell = 0i64;
            for k in 0..n {
                cell += a[i * n + k] * b[k * n + j];
            }
            total += cell;
        }
    }
    println!("{}", total);
}
