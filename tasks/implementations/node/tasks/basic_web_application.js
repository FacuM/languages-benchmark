const { startHttpService } = require('./service_support');
module.exports.start = function(size, port, fixturesRoot) {
  startHttpService('basic_web_application', port);
};
