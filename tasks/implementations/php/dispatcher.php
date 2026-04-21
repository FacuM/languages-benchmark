<?php
$dispatch = [
  'sort_integers' => ['tasks/sort_integers.php', 'run_sort_integers'],
  'matrix_multiplication' => ['tasks/matrix_multiplication.php', 'run_matrix_multiplication'],
  'csv_parsing' => ['tasks/csv_parsing.php', 'run_csv_parsing'],
  'prime_sieve' => ['tasks/prime_sieve.php', 'run_prime_sieve'],
  'file_io_large' => ['tasks/file_io_large.php', 'run_file_io_large'],
  'binary_search_tree' => ['tasks/binary_search_tree.php', 'run_binary_search_tree'],
  'linear_regression' => ['tasks/linear_regression.php', 'run_linear_regression'],
  'cli_file_search' => ['tasks/cli_file_search.php', 'run_cli_file_search'],
  'tic_tac_toe' => ['tasks/tic_tac_toe.php', 'run_tic_tac_toe'],
  'basic_blockchain' => ['tasks/basic_blockchain.php', 'run_basic_blockchain'],
  'image_resizing' => ['tasks/image_resizing.php', 'run_image_resizing'],
  'sentiment_analysis' => ['tasks/sentiment_analysis.php', 'run_sentiment_analysis'],
  'decision_tree' => ['tasks/decision_tree.php', 'run_decision_tree'],
  'producer_consumer' => ['tasks/producer_consumer.php', 'run_producer_consumer'],
  'web_scraper' => ['tasks/web_scraper.php', 'run_web_scraper'],
  'api_client' => ['tasks/api_client.php', 'run_api_client'],
  'third_party_api' => ['tasks/third_party_api.php', 'run_third_party_api'],
  'ai_service_integration' => ['tasks/ai_service_integration.php', 'run_ai_service_integration'],
];

$serviceDispatch = [
  'simple_web_server' => ['tasks/simple_web_server.php', 'start_simple_web_server'],
  'rest_api' => ['tasks/rest_api.php', 'start_rest_api'],
  'sqlite_crud' => ['tasks/sqlite_crud.php', 'start_sqlite_crud'],
  'chat_application' => ['tasks/chat_application.php', 'start_chat_application'],
  'socket_programming' => ['tasks/socket_programming.php', 'start_socket_programming'],
  'gui_calculator' => ['tasks/gui_calculator.php', 'start_gui_calculator'],
  'data_visualization' => ['tasks/data_visualization.php', 'start_data_visualization'],
  'basic_web_application' => ['tasks/basic_web_application.php', 'start_basic_web_application'],
];

function resolve_callable($mapping, $task) {
  list($file, $fn) = $mapping[$task];
  require_once __DIR__ . '/' . $file;
  return $fn;
}

if ((isset($argv[1]) ? $argv[1] : '') === 'start') {
  $task = isset($argv[2]) ? $argv[2] : '';
  $size = isset($argv[3]) ? $argv[3] : 's';
  if (!array_key_exists($task, $serviceDispatch)) {
    fwrite(STDERR, "unsupported service task: $task
");
    exit(2);
  }
  $port = intval(getenv('PORT') ?: '8000');
  $callable = resolve_callable($serviceDispatch, $task);
  $callable($size, $port, '/fixtures');
  exit(0);
}

$task = isset($argv[1]) ? $argv[1] : '';
$size = isset($argv[2]) ? $argv[2] : 's';
if (!array_key_exists($task, $dispatch)) {
  fwrite(STDERR, "unsupported task: $task
");
  exit(2);
}
$callable = resolve_callable($dispatch, $task);
$callable($size, '/fixtures');
