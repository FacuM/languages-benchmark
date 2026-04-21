const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const path = `${fixturesRoot}/generated/sort/${size}.txt`;
  const values = fs.readFileSync(path, 'utf8').trim().split(/\s+/).map(Number).sort((a, b) => a - b);
  const total = values.slice(0, 100).reduce((acc, item) => acc + item, 0);
  console.log(total);
};
