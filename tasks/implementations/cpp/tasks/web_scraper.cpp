#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <string>

static std::string read_file_ws(const std::string& path) {
    std::ifstream file(path);
    std::ostringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

void run_web_scraper(const std::string& size, const std::string& fixturesRoot) {
    std::string base = fixturesRoot + "/mock_site/" + size;
    std::string index = read_file_ws(base + "/index.html");
    std::regex link_re("href=\"([^\"]+)\"");
    std::regex title_re("<h2>(.*?)</h2>");
    std::regex body_re("<p>(.*?)</p>");
    long long total = 0;
    int idx = 0;
    for (std::sregex_iterator it(index.begin(), index.end(), link_re), end; it != end; ++it, ++idx) {
        std::string page = read_file_ws(base + "/" + (*it)[1].str());
        std::smatch title_match, body_match;
        std::regex_search(page, title_match, title_re);
        std::regex_search(page, body_match, body_re);
        total += static_cast<long long>(idx + 1) * (title_match[1].str().size() + body_match[1].str().size());
    }
    std::cout << total << std::endl;
}
