#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void run_image_resizing(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/image/" + size + ".ppm");
    std::string magic;
    int width = 0, height = 0, max_value = 0;
    file >> magic >> width >> height >> max_value;
    std::vector<int> data(width * height * 3);
    for (int& value : data) file >> value;
    long long checksum = 0;
    for (int y = 0; y < height / 2; ++y) {
        for (int x = 0; x < width / 2; ++x) {
            int idx = ((y * 2) * width + (x * 2)) * 3;
            checksum += data[idx] + data[idx + 1] + data[idx + 2];
        }
    }
    std::cout << checksum << std::endl;
}
