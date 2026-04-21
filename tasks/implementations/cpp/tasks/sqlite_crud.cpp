#include <string>

void start_http_service(const std::string&, int);
void start_tcp_service(const std::string&, int);

void start_sqlite_crud(const std::string& size, int port, const std::string& fixturesRoot) {
    start_http_service("sqlite_crud", port);
}
