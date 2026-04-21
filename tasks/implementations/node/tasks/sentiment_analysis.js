const fs = require('fs');
const POSITIVE = new Set(['good', 'great', 'happy', 'clean', 'fast', 'love']);
const NEGATIVE = new Set(['bad', 'sad', 'dirty', 'slow', 'hate', 'poor']);
module.exports = function(size, fixturesRoot) {
  const lines = fs.readFileSync(`${fixturesRoot}/generated/sentiment/${size}.txt`, 'utf8').trim().split(/\r?\n/);
  let total = 0;
  for (const line of lines) {
    for (const token of line.split(/\s+/)) {
      if (POSITIVE.has(token)) total += 1;
      else if (NEGATIVE.has(token)) total -= 1;
    }
  }
  console.log(total);
};
