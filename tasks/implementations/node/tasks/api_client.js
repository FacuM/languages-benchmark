const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const text = fs.readFileSync(`${fixturesRoot}/mocks/public_api_${size}.json`, 'utf8');
  let total = 0;
  for (const match of text.matchAll(/"id":\s*(\d+),\s*"name":\s*"([^"]+)",\s*"value":\s*(\d+)/g)) {
    total += Number(match[1]) + Number(match[3]) + match[2].length;
  }
  console.log(total);
};
