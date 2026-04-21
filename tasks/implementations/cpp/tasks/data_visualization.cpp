#include <string>

void start_http_service(const std::string&, int);

void start_data_visualization(const std::string& size, int port, const std::string& fixturesRoot) {
    start_http_service("data_visualization", port);
}
