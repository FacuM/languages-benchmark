const sortRun = require('./tasks/sort_integers');
const matrixRun = require('./tasks/matrix_multiplication');
const csvRun = require('./tasks/csv_parsing');
const primeRun = require('./tasks/prime_sieve');
const fileIoRun = require('./tasks/file_io_large');
const bstRun = require('./tasks/binary_search_tree');
const linearRegressionRun = require('./tasks/linear_regression');
const cliFileSearchRun = require('./tasks/cli_file_search');
const ticTacToeRun = require('./tasks/tic_tac_toe');
const basicBlockchainRun = require('./tasks/basic_blockchain');
const imageResizingRun = require('./tasks/image_resizing');
const sentimentAnalysisRun = require('./tasks/sentiment_analysis');
const decisionTreeRun = require('./tasks/decision_tree');
const producerConsumerRun = require('./tasks/producer_consumer');
const webScraperRun = require('./tasks/web_scraper');
const apiClientRun = require('./tasks/api_client');
const thirdPartyApiRun = require('./tasks/third_party_api');
const aiServiceIntegrationRun = require('./tasks/ai_service_integration');
const simpleWebServer = require('./tasks/simple_web_server');
const restApi = require('./tasks/rest_api');
const sqliteCrud = require('./tasks/sqlite_crud');
const chatApplication = require('./tasks/chat_application');
const socketProgramming = require('./tasks/socket_programming');
const guiCalculator = require('./tasks/gui_calculator');
const dataVisualization = require('./tasks/data_visualization');
const basicWebApplication = require('./tasks/basic_web_application');

const dispatch = {
  sort_integers: sortRun,
  matrix_multiplication: matrixRun,
  csv_parsing: csvRun,
  prime_sieve: primeRun,
  file_io_large: fileIoRun,
  binary_search_tree: bstRun,
  linear_regression: linearRegressionRun,
  cli_file_search: cliFileSearchRun,
  tic_tac_toe: ticTacToeRun,
  basic_blockchain: basicBlockchainRun,
  image_resizing: imageResizingRun,
  sentiment_analysis: sentimentAnalysisRun,
  decision_tree: decisionTreeRun,
  producer_consumer: producerConsumerRun,
  web_scraper: webScraperRun,
  api_client: apiClientRun,
  third_party_api: thirdPartyApiRun,
  ai_service_integration: aiServiceIntegrationRun,
};

const serviceDispatch = {
  simple_web_server: simpleWebServer.start,
  rest_api: restApi.start,
  sqlite_crud: sqliteCrud.start,
  chat_application: chatApplication.start,
  socket_programming: socketProgramming.start,
  gui_calculator: guiCalculator.start,
  data_visualization: dataVisualization.start,
  basic_web_application: basicWebApplication.start,
};

if (process.argv[2] === 'start') {
  const [taskId, size] = process.argv.slice(3);
  if (!serviceDispatch[taskId]) {
    console.error(`unsupported service task: ${taskId}`);
    process.exit(2);
  }
  serviceDispatch[taskId](size, Number(process.env.PORT || '8000'), '/fixtures');
} else {
  const [taskId, size] = process.argv.slice(2);
  if (!dispatch[taskId]) {
    console.error(`unsupported task: ${taskId}`);
    process.exit(2);
  }
  dispatch[taskId](size, '/fixtures');
}
