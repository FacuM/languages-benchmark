import java.nio.file.*;
import java.util.*;

class BasicBlockchain {
    static final long MOD = 4_294_967_291L;
    static final long MULT = 16_777_619L;

    public static void run(String size, String fixturesRoot) throws Exception {
        List<String> lines = Files.readAllLines(Path.of(fixturesRoot, "generated", "blockchain", size + ".txt"));
        long prevHash = 2_166_136_261L;
        long total = 0L;
        for (int index = 0; index < lines.size(); index++) {
            String line = lines.get(index);
            if (line.isBlank()) continue;
            long hashValue = prevHash;
            for (String token : line.trim().split("\\s+")) {
                hashValue = (hashValue * MULT + Long.parseLong(token) + index + 1L) % MOD;
            }
            total = (total + hashValue) % MOD;
            prevHash = hashValue;
        }
        System.out.println(total);
    }
}
