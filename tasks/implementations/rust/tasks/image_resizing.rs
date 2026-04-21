use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/image/{}.ppm", fixtures_root, size)).unwrap();
    let tokens: Vec<i64> = text.split_whitespace().skip(1).map(|x| x.parse::<i64>().unwrap_or(0)).collect();
    let width = tokens[0] as usize;
    let height = tokens[1] as usize;
    let data = &tokens[3..];
    let mut checksum = 0i64;
    for y in 0..(height / 2) {
        for x in 0..(width / 2) {
            let idx = ((y * 2) * width + (x * 2)) * 3;
            checksum += data[idx] + data[idx + 1] + data[idx + 2];
        }
    }
    println!("{}", checksum);
}
