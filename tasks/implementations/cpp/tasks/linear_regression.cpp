#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

void run_linear_regression(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/linear_regression/" + size + ".csv");
    std::string line;
    std::getline(file, line);
    double n = 0.0, sum_x = 0.0, sum_y = 0.0, sum_xy = 0.0, sum_x2 = 0.0;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string x_part, y_part;
        std::getline(ss, x_part, ',');
        std::getline(ss, y_part, ',');
        double x = std::stod(x_part);
        double y = std::stod(y_part);
        n += 1.0;
        sum_x += x; sum_y += y; sum_xy += x * y; sum_x2 += x * x;
    }
    double slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x);
    double intercept = (sum_y - slope * sum_x) / n;
    long long checksum = std::llround(slope * 1000000.0) + std::llround(intercept * 1000000.0);
    std::cout << checksum << std::endl;
}
