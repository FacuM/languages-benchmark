#include <string>

void start_http_service(const std::string&, int);

void start_basic_web_application(const std::string& size, int port, const std::string& fixturesRoot) {
    start_http_service("basic_web_application", port);
}
