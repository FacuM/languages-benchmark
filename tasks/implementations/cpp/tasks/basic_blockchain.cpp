#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdint>

void run_basic_blockchain(const std::string& size, const std::string& fixturesRoot) {
    constexpr std::uint64_t MOD = 4294967291ULL;
    constexpr std::uint64_t MULT = 16777619ULL;
    std::ifstream file(fixturesRoot + "/generated/blockchain/" + size + ".txt");
    std::string line;
    std::uint64_t prev_hash = 2166136261ULL;
    std::uint64_t total = 0;
    std::uint64_t index = 0;
    while (std::getline(file, line)) {
        if (line.empty()) continue;
        std::stringstream ss(line);
        std::uint64_t hash_value = prev_hash;
        std::uint64_t tx = 0;
        while (ss >> tx) hash_value = (hash_value * MULT + tx + index + 1ULL) % MOD;
        total = (total + hash_value) % MOD;
        prev_hash = hash_value;
        index++;
    }
    std::cout << total << std::endl;
}
