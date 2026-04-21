#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void run_matrix_multiplication(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/matrix/" + size + ".txt");
    int n;
    file >> n;
    std::vector<int> nums(2 * n * n);
    for (int& num : nums) file >> num;
    int split = n * n;
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int cell = 0;
            for (int k = 0; k < n; ++k) {
                cell += nums[i * n + k] * nums[split + k * n + j];
            }
            total += cell;
        }
    }
    std::cout << total << std::endl;
}
