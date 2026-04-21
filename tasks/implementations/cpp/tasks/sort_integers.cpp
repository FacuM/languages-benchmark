#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void run_sort_integers(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/sort/" + size + ".txt");
    std::vector<int> values;
    int value;
    while (file >> value) values.push_back(value);
    std::sort(values.begin(), values.end());
    long long total = 0;
    for (int i = 0; i < 100 && i < static_cast<int>(values.size()); ++i) total += values[i];
    std::cout << total << std::endl;
}
