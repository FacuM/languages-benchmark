#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cstdint>

void run_producer_consumer(const std::string& size, const std::string& fixturesRoot) {
    constexpr std::uint64_t MOD = 4294967291ULL;
    constexpr int CAPACITY = 64;
    std::ifstream file(fixturesRoot + "/generated/producer_consumer/" + size + ".txt");
    std::vector<int> values;
    int value = 0;
    while (file >> value) values.push_back(value);
    std::vector<int> buffer(CAPACITY, 0);
    int head = 0, tail = 0, count = 0;
    std::size_t produced = 0;
    std::uint64_t consumed = 0;
    std::uint64_t checksum = 0;
    while (produced < values.size() || count > 0) {
        while (produced < values.size() && count < CAPACITY) {
            buffer[tail] = values[produced++];
            tail = (tail + 1) % CAPACITY;
            count++;
        }
        if (count > 0) {
            int current = buffer[head];
            head = (head + 1) % CAPACITY;
            count--;
            checksum = (checksum + static_cast<std::uint64_t>(current) * (consumed + 1ULL)) % MOD;
            consumed++;
        }
    }
    std::cout << checksum << std::endl;
}
