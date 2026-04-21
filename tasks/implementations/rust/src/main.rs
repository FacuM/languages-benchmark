mod tasks;

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let task = args.get(1).expect("task");
    if task == "start" {
        let service = args.get(2).expect("service");
        let size = args.get(3).expect("size");
        let port: u16 = env::var("PORT").unwrap_or_else(|_| "8000".to_string()).parse().unwrap();
        match service.as_str() {
            "simple_web_server" => tasks::simple_web_server::start(size, port, "/fixtures"),
            "rest_api" => tasks::rest_api::start(size, port, "/fixtures"),
            "sqlite_crud" => tasks::sqlite_crud::start(size, port, "/fixtures"),
            "chat_application" => tasks::chat_application::start(size, port, "/fixtures"),
            "socket_programming" => tasks::socket_programming::start(size, port, "/fixtures"),
            "gui_calculator" => tasks::gui_calculator::start(size, port, "/fixtures"),
            "data_visualization" => tasks::data_visualization::start(size, port, "/fixtures"),
            "basic_web_application" => tasks::basic_web_application::start(size, port, "/fixtures"),
            _ => panic!("unsupported service task: {}", service),
        }
        return;
    }

    let size = args.get(2).expect("size");
    match task.as_str() {
        "sort_integers" => tasks::sort_integers::run(size, "/fixtures"),
        "matrix_multiplication" => tasks::matrix_multiplication::run(size, "/fixtures"),
        "csv_parsing" => tasks::csv_parsing::run(size, "/fixtures"),
        "prime_sieve" => tasks::prime_sieve::run(size, "/fixtures"),
        "file_io_large" => tasks::file_io_large::run(size, "/fixtures"),
        "binary_search_tree" => tasks::binary_search_tree::run(size, "/fixtures"),
        "linear_regression" => tasks::linear_regression::run(size, "/fixtures"),
        "cli_file_search" => tasks::cli_file_search::run(size, "/fixtures"),
        "tic_tac_toe" => tasks::tic_tac_toe::run(size, "/fixtures"),
        "basic_blockchain" => tasks::basic_blockchain::run(size, "/fixtures"),
        "image_resizing" => tasks::image_resizing::run(size, "/fixtures"),
        "sentiment_analysis" => tasks::sentiment_analysis::run(size, "/fixtures"),
        "decision_tree" => tasks::decision_tree::run(size, "/fixtures"),
        "producer_consumer" => tasks::producer_consumer::run(size, "/fixtures"),
        "web_scraper" => tasks::web_scraper::run(size, "/fixtures"),
        "api_client" => tasks::api_client::run(size, "/fixtures"),
        "third_party_api" => tasks::third_party_api::run(size, "/fixtures"),
        "ai_service_integration" => tasks::ai_service_integration::run(size, "/fixtures"),
        _ => panic!("unsupported task: {}", task),
    }
}
