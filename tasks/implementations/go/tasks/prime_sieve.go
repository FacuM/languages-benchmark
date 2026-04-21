package main

import "fmt"

func RunPrimeSieve(size string, fixturesRoot string) {
    limits := map[string]int{"s": 50000, "m": 125000, "l": 250000}
    n := limits[size]
    sieve := make([]bool, n+1)
    for i := 2; i <= n; i++ { sieve[i] = true }
    for p := 2; p*p <= n; p++ {
        if sieve[p] {
            for i := p * p; i <= n; i += p { sieve[i] = false }
        }
    }
    count := 0
    for _, prime := range sieve { if prime { count++ } }
    fmt.Println(count)
}
