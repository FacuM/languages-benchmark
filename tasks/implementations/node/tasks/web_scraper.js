const fs = require('fs');
module.exports = function(size, fixturesRoot) {
  const base = `${fixturesRoot}/mock_site/${size}`;
  const index = fs.readFileSync(`${base}/index.html`, 'utf8');
  const links = [...index.matchAll(/href="([^"]+)"/g)].map((m) => m[1]);
  let total = 0;
  links.forEach((link, idx) => {
    const text = fs.readFileSync(`${base}/${link}`, 'utf8');
    const title = (text.match(/<h2>(.*?)<\/h2>/i) || [])[1] || '';
    const body = (text.match(/<p>(.*?)<\/p>/i) || [])[1] || '';
    total += (idx + 1) * (title.length + body.length);
  });
  console.log(total);
};
