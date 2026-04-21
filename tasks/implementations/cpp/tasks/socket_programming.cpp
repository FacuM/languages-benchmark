#include <string>

void start_http_service(const std::string&, int);
void start_tcp_service(const std::string&, int);

void start_socket_programming(const std::string& size, int port, const std::string& fixturesRoot) {
    start_tcp_service("socket_programming", port);
}
