import java.nio.file.*;
import java.util.*;

class CSVParsing {
    public static void run(String size, String fixturesRoot) throws Exception {
        List<String> lines = Files.readAllLines(Path.of(fixturesRoot, "generated", "csv", size + ".csv"));
        long total = 0;
        for (int i = 1; i < lines.size(); i++) {
            String[] parts = lines.get(i).split(",");
            total += Integer.parseInt(parts[1]) + Integer.parseInt(parts[2]);
        }
        System.out.println(total);
    }
}
