package main

import (
    "fmt"
    "os"
    "strconv"
)

func main() {
    if len(os.Args) < 3 {
        panic("usage: task size")
    }
    if os.Args[1] == "start" {
        if len(os.Args) < 4 {
            panic("usage: start task size")
        }
        taskID := os.Args[2]
        size := os.Args[3]
        port, _ := strconv.Atoi(os.Getenv("PORT"))
        switch taskID {
        case "simple_web_server":
            StartSimpleWebServer(size, port, "/fixtures")
        case "rest_api":
            StartRestApi(size, port, "/fixtures")
        case "sqlite_crud":
            StartSqliteCrud(size, port, "/fixtures")
        case "chat_application":
            StartChatApplication(size, port, "/fixtures")
        case "socket_programming":
            StartSocketProgramming(size, port, "/fixtures")
        case "gui_calculator":
            StartGuiCalculator(size, port, "/fixtures")
        case "data_visualization":
            StartDataVisualization(size, port, "/fixtures")
        case "basic_web_application":
            StartBasicWebApplication(size, port, "/fixtures")
        default:
            fmt.Fprintln(os.Stderr, "unsupported service task:", taskID)
            os.Exit(2)
        }
        return
    }
    taskID := os.Args[1]
    size := os.Args[2]
    switch taskID {
    case "sort_integers":
        RunSortIntegers(size, "/fixtures")
    case "matrix_multiplication":
        RunMatrixMultiplication(size, "/fixtures")
    case "csv_parsing":
        RunCSVParsing(size, "/fixtures")
    case "prime_sieve":
        RunPrimeSieve(size, "/fixtures")
    case "file_io_large":
        RunFileIOLarge(size, "/fixtures")
    case "binary_search_tree":
        RunBinarySearchTree(size, "/fixtures")
    case "linear_regression":
        RunLinearRegression(size, "/fixtures")
    case "cli_file_search":
        RunCliFileSearch(size, "/fixtures")
    case "tic_tac_toe":
        RunTicTacToe(size, "/fixtures")
    case "basic_blockchain":
        RunBasicBlockchain(size, "/fixtures")
    case "image_resizing":
        RunImageResizing(size, "/fixtures")
    case "sentiment_analysis":
        RunSentimentAnalysis(size, "/fixtures")
    case "decision_tree":
        RunDecisionTree(size, "/fixtures")
    case "producer_consumer":
        RunProducerConsumer(size, "/fixtures")
    case "web_scraper":
        RunWebScraper(size, "/fixtures")
    case "api_client":
        RunApiClient(size, "/fixtures")
    case "third_party_api":
        RunThirdPartyApi(size, "/fixtures")
    case "ai_service_integration":
        RunAiServiceIntegration(size, "/fixtures")
    default:
        fmt.Fprintln(os.Stderr, "unsupported task:", taskID)
        os.Exit(2)
    }
}
