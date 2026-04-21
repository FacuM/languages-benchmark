const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const text = fs.readFileSync(`${fixturesRoot}/mocks/ai_service_${size}.json`, 'utf8');
  const model = ((text.match(/"model":\s*"([^"]+)"/) || [])[1]) || '';
  let total = model.length;
  for (const match of text.matchAll(/"prompt":\s*"([^"]+)",\s*"output":\s*"([^"]+)",\s*"tokens":\s*(\d+)/g)) {
    total += match[1].length + match[2].length + Number(match[3]);
  }
  console.log(total);
};
