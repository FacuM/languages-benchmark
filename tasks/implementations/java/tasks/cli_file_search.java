import java.nio.file.*;
import java.util.stream.*;

class CliFileSearch {
    public static void run(String size, String fixturesRoot) throws Exception {
        long total = 0;
        try (Stream<Path> paths = Files.walk(Path.of(fixturesRoot, "generated", "search", size))) {
            for (Path path : (Iterable<Path>) paths.filter(Files::isRegularFile)::iterator) {
                if (path.toString().endsWith(".txt")) {
                    for (String line : Files.readAllLines(path)) {
                        if (line.contains("needle")) total += 1;
                    }
                }
            }
        }
        System.out.println(total);
    }
}
