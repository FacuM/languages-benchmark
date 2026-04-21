const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const path = `${fixturesRoot}/generated/file_io/${size}.txt`;
  let total = 0;
  for (const line of fs.readFileSync(path, 'utf8').trim().split(/\s+/)) {
    total += Number(line);
  }
  console.log(total);
};
