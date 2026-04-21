const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const tokens = fs.readFileSync(`${fixturesRoot}/generated/matrix/${size}.txt`, 'utf8').trim().split(/\s+/).map(Number);
  const n = tokens[0];
  const nums = tokens.slice(1);
  const split = n * n;
  const a = nums.slice(0, split);
  const b = nums.slice(split);
  let total = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      let cell = 0;
      for (let k = 0; k < n; k++) {
        cell += a[i * n + k] * b[k * n + j];
      }
      total += cell;
    }
  }
  console.log(total);
};
