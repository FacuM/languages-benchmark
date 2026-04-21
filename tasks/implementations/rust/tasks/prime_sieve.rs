pub fn run(size: &str, _fixtures_root: &str) {
    let n = match size { "s" => 50_000, "m" => 125_000, _ => 250_000 };
    let mut sieve = vec![true; n + 1];
    sieve[0] = false; sieve[1] = false;
    let mut p = 2usize;
    while p * p <= n {
        if sieve[p] {
            let mut i = p * p;
            while i <= n { sieve[i] = false; i += p; }
        }
        p += 1;
    }
    let count = sieve.iter().filter(|x| **x).count();
    println!("{}", count);
}
