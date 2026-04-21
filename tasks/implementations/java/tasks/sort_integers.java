import java.nio.file.*;
import java.util.*;

class SortIntegers {
    public static void run(String size, String fixturesRoot) throws Exception {
        List<String> lines = Files.readAllLines(Path.of(fixturesRoot, "generated", "sort", size + ".txt"));
        List<Integer> values = new ArrayList<>();
        for (String line : lines) values.add(Integer.parseInt(line.trim()));
        Collections.sort(values);
        long total = 0;
        for (int i = 0; i < Math.min(100, values.size()); i++) total += values.get(i);
        System.out.println(total);
    }
}
