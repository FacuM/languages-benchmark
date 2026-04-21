#include <string>

void start_http_service(const std::string&, int);
void start_tcp_service(const std::string&, int);

void start_chat_application(const std::string& size, int port, const std::string& fixturesRoot) {
    start_tcp_service("chat_application", port);
}
