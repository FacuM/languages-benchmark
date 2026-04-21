#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>

void run_sentiment_analysis(const std::string& size, const std::string& fixturesRoot) {
    static const std::unordered_set<std::string> positive = {"good", "great", "happy", "clean", "fast", "love"};
    static const std::unordered_set<std::string> negative = {"bad", "sad", "dirty", "slow", "hate", "poor"};
    std::ifstream file(fixturesRoot + "/generated/sentiment/" + size + ".txt");
    std::string line, token;
    long long total = 0;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        while (ss >> token) {
            if (positive.contains(token)) total += 1;
            else if (negative.contains(token)) total -= 1;
        }
    }
    std::cout << total << std::endl;
}
