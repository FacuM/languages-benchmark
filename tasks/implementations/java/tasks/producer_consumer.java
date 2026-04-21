import java.nio.file.*;
import java.util.*;

class ProducerConsumer {
    static final long MOD = 4_294_967_291L;
    static final int CAPACITY = 64;

    public static void run(String size, String fixturesRoot) throws Exception {
        String[] tokens = Files.readString(Path.of(fixturesRoot, "generated", "producer_consumer", size + ".txt")).trim().split("\\s+");
        int[] values = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) values[i] = Integer.parseInt(tokens[i]);
        int[] buffer = new int[CAPACITY];
        int head = 0, tail = 0, count = 0, produced = 0, consumed = 0;
        long checksum = 0L;
        while (produced < values.length || count > 0) {
            while (produced < values.length && count < CAPACITY) {
                buffer[tail] = values[produced++];
                tail = (tail + 1) % CAPACITY;
                count++;
            }
            if (count > 0) {
                int value = buffer[head];
                head = (head + 1) % CAPACITY;
                count--;
                checksum = (checksum + (long) value * (consumed + 1L)) % MOD;
                consumed++;
            }
        }
        System.out.println(checksum);
    }
}
