#include <fstream>
#include <iostream>
#include <string>

void run_file_io_large(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/file_io/" + size + ".txt");
    long long total = 0;
    long long value = 0;
    while (file >> value) total += value;
    std::cout << total << std::endl;
}
