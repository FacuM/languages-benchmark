#include <string>

void start_http_service(const std::string&, int);
void start_tcp_service(const std::string&, int);

void start_rest_api(const std::string& size, int port, const std::string& fixturesRoot) {
    start_http_service("rest_api", port);
}
