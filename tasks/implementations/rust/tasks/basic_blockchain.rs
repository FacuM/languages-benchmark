use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    const MOD: u64 = 4_294_967_291;
    const MULT: u64 = 16_777_619;
    let text = fs::read_to_string(format!("{}/generated/blockchain/{}.txt", fixtures_root, size)).unwrap();
    let mut prev_hash: u64 = 2_166_136_261;
    let mut total: u64 = 0;
    for (index, line) in text.lines().enumerate() {
        if line.is_empty() { continue; }
        let mut hash_value = prev_hash;
        for token in line.split_whitespace() {
            let tx = token.parse::<u64>().unwrap();
            hash_value = (hash_value * MULT + tx + index as u64 + 1) % MOD;
        }
        total = (total + hash_value) % MOD;
        prev_hash = hash_value;
    }
    println!("{}", total);
}
