const { startHttpService } = require('./service_support');
module.exports.start = function(size, port, fixturesRoot) {
  startHttpService('data_visualization', port);
};
