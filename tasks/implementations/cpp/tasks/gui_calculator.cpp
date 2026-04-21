#include <string>

void start_http_service(const std::string&, int);

void start_gui_calculator(const std::string& size, int port, const std::string& fixturesRoot) {
    start_http_service("gui_calculator", port);
}
