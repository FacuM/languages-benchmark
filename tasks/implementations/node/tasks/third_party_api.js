const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const text = fs.readFileSync(`${fixturesRoot}/mocks/twitter_like_${size}.json`, 'utf8');
  let total = 0;
  for (const match of text.matchAll(/"id":\s*"([^"]+)",\s*"text":\s*"([^"]+)",\s*"likes":\s*(\d+)/g)) {
    total += match[1].length + match[2].length + Number(match[3]);
  }
  console.log(total);
};
