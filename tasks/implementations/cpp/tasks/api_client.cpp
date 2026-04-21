#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <string>

static std::string read_file_api(const std::string& path) {
    std::ifstream file(path);
    std::ostringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

void run_api_client(const std::string& size, const std::string& fixturesRoot) {
    std::string text = read_file_api(fixturesRoot + "/mocks/public_api_" + size + ".json");
    std::regex re(R"re("id":\s*(\d+),\s*"name":\s*"([^"]+)",\s*"value":\s*(\d+))re");
    long long total = 0;
    for (std::sregex_iterator it(text.begin(), text.end(), re), end; it != end; ++it) total += std::stoll((*it)[1].str()) + std::stoll((*it)[3].str()) + (*it)[2].str().size();
    std::cout << total << std::endl;
}
