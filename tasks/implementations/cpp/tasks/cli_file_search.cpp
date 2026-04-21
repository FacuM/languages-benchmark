#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>

void run_cli_file_search(const std::string& size, const std::string& fixturesRoot) {
    namespace fs = std::filesystem;
    fs::path root = fs::path(fixturesRoot) / "generated" / "search" / size;
    long long total = 0;
    for (const auto& entry : fs::recursive_directory_iterator(root)) {
        if (!entry.is_regular_file() || entry.path().extension() != ".txt") continue;
        std::ifstream file(entry.path());
        std::string line;
        while (std::getline(file, line)) {
            if (line.find("needle") != std::string::npos) total += 1;
        }
    }
    std::cout << total << std::endl;
}
