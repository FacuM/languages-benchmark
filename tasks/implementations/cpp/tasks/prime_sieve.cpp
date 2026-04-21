#include <iostream>
#include <string>
#include <vector>

void run_prime_sieve(const std::string& size, const std::string& fixturesRoot) {
    int n = size == "s" ? 50000 : size == "m" ? 125000 : 250000;
    std::vector<bool> sieve(n + 1, true);
    sieve[0] = sieve[1] = false;
    for (int p = 2; p * p <= n; ++p) {
        if (sieve[p]) {
            for (int i = p * p; i <= n; i += p) sieve[i] = false;
        }
    }
    int count = 0;
    for (bool prime : sieve) if (prime) count++;
    std::cout << count << std::endl;
}
