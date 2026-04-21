import java.nio.file.*;
import java.util.*;

class SentimentAnalysis {
    static final Set<String> POSITIVE = Set.of("good", "great", "happy", "clean", "fast", "love");
    static final Set<String> NEGATIVE = Set.of("bad", "sad", "dirty", "slow", "hate", "poor");

    public static void run(String size, String fixturesRoot) throws Exception {
        long total = 0;
        for (String line : Files.readAllLines(Path.of(fixturesRoot, "generated", "sentiment", size + ".txt"))) {
            for (String token : line.trim().split("\\s+")) {
                if (POSITIVE.contains(token)) total += 1;
                else if (NEGATIVE.contains(token)) total -= 1;
            }
        }
        System.out.println(total);
    }
}
