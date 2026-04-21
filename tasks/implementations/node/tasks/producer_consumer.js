const fs = require('fs');
const MOD = 4294967291n;
const CAPACITY = 64;

module.exports = function(size, fixturesRoot) {
  const values = fs.readFileSync(`${fixturesRoot}/generated/producer_consumer/${size}.txt`, 'utf8').trim().split(/\s+/).map(Number);
  const buffer = new Array(CAPACITY).fill(0);
  let head = 0, tail = 0, count = 0, produced = 0, consumed = 0;
  let checksum = 0n;
  while (produced < values.length || count > 0) {
    while (produced < values.length && count < CAPACITY) {
      buffer[tail] = values[produced];
      tail = (tail + 1) % CAPACITY;
      produced += 1;
      count += 1;
    }
    if (count > 0) {
      const value = buffer[head];
      head = (head + 1) % CAPACITY;
      count -= 1;
      checksum = (checksum + BigInt(value) * BigInt(consumed + 1)) % MOD;
      consumed += 1;
    }
  }
  console.log(checksum.toString());
};
