const { startHttpService } = require('./service_support');
module.exports.start = function(size, port, fixturesRoot) {
  startHttpService('simple_web_server', port);
};
