const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const tokens = fs.readFileSync(`${fixturesRoot}/generated/image/${size}.ppm`, 'utf8').trim().split(/\s+/);
  const width = Number(tokens[1]);
  const height = Number(tokens[2]);
  const data = tokens.slice(4).map(Number);
  let checksum = 0;
  for (let y = 0; y < height / 2; y++) {
    for (let x = 0; x < width / 2; x++) {
      const idx = ((y * 2) * width + (x * 2)) * 3;
      checksum += data[idx] + data[idx + 1] + data[idx + 2];
    }
  }
  console.log(checksum);
};
