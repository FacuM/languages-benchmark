class PrimeSieve {
    public static void run(String size, String fixturesRoot) {
        int n = switch (size) { case "s" -> 50000; case "m" -> 125000; default -> 250000; };
        boolean[] sieve = new boolean[n + 1];
        java.util.Arrays.fill(sieve, true);
        sieve[0] = false; sieve[1] = false;
        for (int p = 2; p * p <= n; p++) {
            if (sieve[p]) {
                for (int i = p * p; i <= n; i += p) sieve[i] = false;
            }
        }
        int count = 0;
        for (boolean prime : sieve) if (prime) count++;
        System.out.println(count);
    }
}
