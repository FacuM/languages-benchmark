public class Dispatcher {
    public static void main(String[] args) throws Exception {
        if ("start".equals(args[0])) {
            String task = args[1];
            String size = args[2];
            int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8000"));
            switch (task) {
                case "simple_web_server" -> SimpleWebServer.start(size, port, "/fixtures");
                case "rest_api" -> RestApi.start(size, port, "/fixtures");
                case "sqlite_crud" -> SqliteCrud.start(size, port, "/fixtures");
                case "chat_application" -> ChatApplication.start(size, port, "/fixtures");
                case "socket_programming" -> SocketProgramming.start(size, port, "/fixtures");
                case "gui_calculator" -> GuiCalculator.start(size, port, "/fixtures");
                case "data_visualization" -> DataVisualization.start(size, port, "/fixtures");
                case "basic_web_application" -> BasicWebApplication.start(size, port, "/fixtures");
                default -> throw new IllegalArgumentException("unsupported service task: " + task);
            }
            return;
        }
        String task = args[0];
        String size = args[1];
        switch (task) {
            case "sort_integers" -> SortIntegers.run(size, "/fixtures");
            case "matrix_multiplication" -> MatrixMultiplication.run(size, "/fixtures");
            case "csv_parsing" -> CSVParsing.run(size, "/fixtures");
            case "prime_sieve" -> PrimeSieve.run(size, "/fixtures");
            case "file_io_large" -> FileIOLarge.run(size, "/fixtures");
            case "binary_search_tree" -> BinarySearchTree.run(size, "/fixtures");
            case "linear_regression" -> LinearRegression.run(size, "/fixtures");
            case "cli_file_search" -> CliFileSearch.run(size, "/fixtures");
            case "tic_tac_toe" -> TicTacToe.run(size, "/fixtures");
            case "basic_blockchain" -> BasicBlockchain.run(size, "/fixtures");
            case "image_resizing" -> ImageResizing.run(size, "/fixtures");
            case "sentiment_analysis" -> SentimentAnalysis.run(size, "/fixtures");
            case "decision_tree" -> DecisionTree.run(size, "/fixtures");
            case "producer_consumer" -> ProducerConsumer.run(size, "/fixtures");
            case "web_scraper" -> WebScraper.run(size, "/fixtures");
            case "api_client" -> ApiClient.run(size, "/fixtures");
            case "third_party_api" -> ThirdPartyApi.run(size, "/fixtures");
            case "ai_service_integration" -> AiServiceIntegration.run(size, "/fixtures");
            default -> throw new IllegalArgumentException("unsupported task: " + task);
        }
    }
}
