const fs = require('fs');
const path = require('path');
function walk(dir) {
  let total = 0;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) total += walk(fullPath);
    else if (entry.isFile() && entry.name.endsWith('.txt')) {
      for (const line of fs.readFileSync(fullPath, 'utf8').split(/\r?\n/)) {
        if (line.includes('needle')) total += 1;
      }
    }
  }
  return total;
}
module.exports = function(size, fixturesRoot) {
  console.log(walk(`${fixturesRoot}/generated/search/${size}`));
};
