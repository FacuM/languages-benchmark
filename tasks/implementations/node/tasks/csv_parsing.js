const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const lines = fs.readFileSync(`${fixturesRoot}/generated/csv/${size}.csv`, 'utf8').trim().split(/\n/);
  let total = 0;
  for (let i = 1; i < lines.length; i++) {
    const parts = lines[i].split(',');
    total += Number(parts[1]) + Number(parts[2]);
  }
  console.log(total);
};
