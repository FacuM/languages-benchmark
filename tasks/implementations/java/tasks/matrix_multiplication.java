import java.nio.file.*;
import java.util.*;

class MatrixMultiplication {
    public static void run(String size, String fixturesRoot) throws Exception {
        String text = Files.readString(Path.of(fixturesRoot, "generated", "matrix", size + ".txt"));
        String[] tokens = text.trim().split("\\s+");
        int n = Integer.parseInt(tokens[0]);
        int[] nums = new int[tokens.length - 1];
        for (int i = 1; i < tokens.length; i++) nums[i - 1] = Integer.parseInt(tokens[i]);
        int split = n * n;
        long total = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int cell = 0;
                for (int k = 0; k < n; k++) {
                    cell += nums[i * n + k] * nums[split + k * n + j];
                }
                total += cell;
            }
        }
        System.out.println(total);
    }
}
