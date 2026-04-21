#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

void run_csv_parsing(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/csv/" + size + ".csv");
    std::string line;
    std::getline(file, line);
    long long total = 0;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string part;
        int idx = 0;
        while (std::getline(ss, part, ',')) {
            if (idx == 1 || idx == 2) total += std::stoi(part);
            idx++;
        }
    }
    std::cout << total << std::endl;
}
