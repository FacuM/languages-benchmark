const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const lines = fs.readFileSync(`${fixturesRoot}/generated/linear_regression/${size}.csv`, 'utf8').trim().split(/\r?\n/);
  let n = 0, sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
  for (let i = 1; i < lines.length; i++) {
    const [xRaw, yRaw] = lines[i].split(',');
    const x = Number(xRaw);
    const y = Number(yRaw);
    n += 1;
    sumX += x; sumY += y; sumXY += x * y; sumX2 += x * x;
  }
  const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
  const intercept = (sumY - slope * sumX) / n;
  const checksum = Math.round(slope * 1000000) + Math.round(intercept * 1000000);
  console.log(checksum);
};
