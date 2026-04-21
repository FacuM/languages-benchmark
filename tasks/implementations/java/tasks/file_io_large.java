import java.nio.file.*;

class FileIOLarge {
    public static void run(String size, String fixturesRoot) throws Exception {
        long total = 0;
        for (String line : Files.readAllLines(Path.of(fixturesRoot, "generated", "file_io", size + ".txt"))) {
            total += Integer.parseInt(line.trim());
        }
        System.out.println(total);
    }
}
