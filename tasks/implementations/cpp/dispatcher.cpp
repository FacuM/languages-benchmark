#include <cstdlib>
#include <iostream>
#include <string>

void run_sort_integers(const std::string&, const std::string&);
void run_matrix_multiplication(const std::string&, const std::string&);
void run_csv_parsing(const std::string&, const std::string&);
void run_prime_sieve(const std::string&, const std::string&);
void run_file_io_large(const std::string&, const std::string&);
void run_binary_search_tree(const std::string&, const std::string&);
void run_linear_regression(const std::string&, const std::string&);
void run_cli_file_search(const std::string&, const std::string&);
void run_tic_tac_toe(const std::string&, const std::string&);
void run_basic_blockchain(const std::string&, const std::string&);
void run_image_resizing(const std::string&, const std::string&);
void run_sentiment_analysis(const std::string&, const std::string&);
void run_decision_tree(const std::string&, const std::string&);
void run_producer_consumer(const std::string&, const std::string&);
void run_web_scraper(const std::string&, const std::string&);
void run_api_client(const std::string&, const std::string&);
void run_third_party_api(const std::string&, const std::string&);
void run_ai_service_integration(const std::string&, const std::string&);
void start_simple_web_server(const std::string&, int, const std::string&);
void start_rest_api(const std::string&, int, const std::string&);
void start_sqlite_crud(const std::string&, int, const std::string&);
void start_chat_application(const std::string&, int, const std::string&);
void start_socket_programming(const std::string&, int, const std::string&);
void start_gui_calculator(const std::string&, int, const std::string&);
void start_data_visualization(const std::string&, int, const std::string&);
void start_basic_web_application(const std::string&, int, const std::string&);

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "usage: task size" << std::endl;
        return 2;
    }
    std::string task = argv[1];
    if (task == "start") {
        if (argc < 4) {
            std::cerr << "usage: start task size" << std::endl;
            return 2;
        }
        std::string service = argv[2];
        std::string size = argv[3];
        int port = std::atoi(std::getenv("PORT") ? std::getenv("PORT") : "8000");
        if (service == "simple_web_server") start_simple_web_server(size, port, "/fixtures");
        else if (service == "rest_api") start_rest_api(size, port, "/fixtures");
        else if (service == "sqlite_crud") start_sqlite_crud(size, port, "/fixtures");
        else if (service == "chat_application") start_chat_application(size, port, "/fixtures");
        else if (service == "socket_programming") start_socket_programming(size, port, "/fixtures");
        else if (service == "gui_calculator") start_gui_calculator(size, port, "/fixtures");
        else if (service == "data_visualization") start_data_visualization(size, port, "/fixtures");
        else if (service == "basic_web_application") start_basic_web_application(size, port, "/fixtures");
        else {
            std::cerr << "unsupported service task: " << service << std::endl;
            return 2;
        }
        return 0;
    }
    std::string size = argv[2];
    if (task == "sort_integers") run_sort_integers(size, "/fixtures");
    else if (task == "matrix_multiplication") run_matrix_multiplication(size, "/fixtures");
    else if (task == "csv_parsing") run_csv_parsing(size, "/fixtures");
    else if (task == "prime_sieve") run_prime_sieve(size, "/fixtures");
    else if (task == "file_io_large") run_file_io_large(size, "/fixtures");
    else if (task == "binary_search_tree") run_binary_search_tree(size, "/fixtures");
    else if (task == "linear_regression") run_linear_regression(size, "/fixtures");
    else if (task == "cli_file_search") run_cli_file_search(size, "/fixtures");
    else if (task == "tic_tac_toe") run_tic_tac_toe(size, "/fixtures");
    else if (task == "basic_blockchain") run_basic_blockchain(size, "/fixtures");
    else if (task == "image_resizing") run_image_resizing(size, "/fixtures");
    else if (task == "sentiment_analysis") run_sentiment_analysis(size, "/fixtures");
    else if (task == "decision_tree") run_decision_tree(size, "/fixtures");
    else if (task == "producer_consumer") run_producer_consumer(size, "/fixtures");
    else if (task == "web_scraper") run_web_scraper(size, "/fixtures");
    else if (task == "api_client") run_api_client(size, "/fixtures");
    else if (task == "third_party_api") run_third_party_api(size, "/fixtures");
    else if (task == "ai_service_integration") run_ai_service_integration(size, "/fixtures");
    else {
        std::cerr << "unsupported task: " << task << std::endl;
        return 2;
    }
    return 0;
}
