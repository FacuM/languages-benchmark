const fs = require('fs');
const MOD = 4294967291n;
const MULT = 16777619n;
module.exports = function(size, fixturesRoot) {
  const lines = fs.readFileSync(`${fixturesRoot}/generated/blockchain/${size}.txt`, 'utf8').trim().split(/\r?\n/);
  let prevHash = 2166136261n;
  let total = 0n;
  for (let index = 0; index < lines.length; index++) {
    let hashValue = prevHash;
    for (const token of lines[index].split(/\s+/)) {
      hashValue = (hashValue * MULT + BigInt(token) + BigInt(index + 1)) % MOD;
    }
    total = (total + hashValue) % MOD;
    prevHash = hashValue;
  }
  console.log(total.toString());
};
