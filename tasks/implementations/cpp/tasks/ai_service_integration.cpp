#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <string>

static std::string read_file_ai(const std::string& path) {
    std::ifstream file(path);
    std::ostringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

void run_ai_service_integration(const std::string& size, const std::string& fixturesRoot) {
    std::string text = read_file_ai(fixturesRoot + "/mocks/ai_service_" + size + ".json");
    std::smatch model_match;
    std::regex_search(text, model_match, std::regex(R"re("model":\s*"([^"]+)")re"));
    std::regex re(R"re("prompt":\s*"([^"]+)",\s*"output":\s*"([^"]+)",\s*"tokens":\s*(\d+))re");
    long long total = model_match[1].str().size();
    for (std::sregex_iterator it(text.begin(), text.end(), re), end; it != end; ++it) total += (*it)[1].str().size() + (*it)[2].str().size() + std::stoll((*it)[3].str());
    std::cout << total << std::endl;
}
