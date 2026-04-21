use std::fs;

pub fn run(size: &str, fixtures_root: &str) {
    const MOD: u64 = 4_294_967_291;
    const CAPACITY: usize = 64;
    let text = fs::read_to_string(format!("{}/generated/producer_consumer/{}.txt", fixtures_root, size)).unwrap();
    let values: Vec<u64> = text.split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();
    let mut buffer = [0u64; CAPACITY];
    let (mut head, mut tail, mut count, mut produced) = (0usize, 0usize, 0usize, 0usize);
    let mut consumed = 0u64;
    let mut checksum = 0u64;
    while produced < values.len() || count > 0 {
        while produced < values.len() && count < CAPACITY {
            buffer[tail] = values[produced];
            tail = (tail + 1) % CAPACITY;
            produced += 1;
            count += 1;
        }
        if count > 0 {
            let value = buffer[head];
            head = (head + 1) % CAPACITY;
            count -= 1;
            checksum = (checksum + value * (consumed + 1)) % MOD;
            consumed += 1;
        }
    }
    println!("{}", checksum);
}
