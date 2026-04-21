const LIMITS = { s: 50000, m: 125000, l: 250000 };
module.exports = function(size) {
  const n = LIMITS[size];
  const sieve = new Array(n + 1).fill(true);
  sieve[0] = sieve[1] = false;
  for (let p = 2; p * p <= n; p++) {
    if (sieve[p]) {
      for (let i = p * p; i <= n; i += p) sieve[i] = false;
    }
  }
  let count = 0;
  for (const entry of sieve) if (entry) count++;
  console.log(count);
};
