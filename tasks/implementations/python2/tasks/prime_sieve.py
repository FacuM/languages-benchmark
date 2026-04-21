from tasks.compat import emit

LIMITS = {'s': 50000, 'm': 125000, 'l': 250000}


def run(size, fixtures_root):
    n = LIMITS[size]
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    p = 2
    while p * p <= n:
        if sieve[p]:
            for idx in xrange(p * p, n + 1, p):
                sieve[idx] = False
        p += 1
    emit(sum(1 for flag in sieve if flag))
