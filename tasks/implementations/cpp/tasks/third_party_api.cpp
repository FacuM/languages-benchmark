#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <string>

static std::string read_file_tp(const std::string& path) {
    std::ifstream file(path);
    std::ostringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

void run_third_party_api(const std::string& size, const std::string& fixturesRoot) {
    std::string text = read_file_tp(fixturesRoot + "/mocks/twitter_like_" + size + ".json");
    std::regex re(R"re("id":\s*"([^"]+)",\s*"text":\s*"([^"]+)",\s*"likes":\s*(\d+))re");
    long long total = 0;
    for (std::sregex_iterator it(text.begin(), text.end(), re), end; it != end; ++it) total += (*it)[1].str().size() + (*it)[2].str().size() + std::stoll((*it)[3].str());
    std::cout << total << std::endl;
}
