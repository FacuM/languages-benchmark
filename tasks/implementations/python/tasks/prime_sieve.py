LIMITS = {"s": 50000, "m": 125000, "l": 250000}

def run(size: str, fixtures_root: str) -> None:
    n = LIMITS[size]
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    print(sum(1 for x in sieve if x))
