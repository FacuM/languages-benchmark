const { startTcpService } = require('./service_support');
module.exports.start = function(size, port, fixturesRoot) {
  startTcpService('chat_application', port);
};
