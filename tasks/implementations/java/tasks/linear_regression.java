import java.nio.file.*;
import java.util.*;

class LinearRegression {
    public static void run(String size, String fixturesRoot) throws Exception {
        List<String> lines = Files.readAllLines(Path.of(fixturesRoot, "generated", "linear_regression", size + ".csv"));
        double n = 0.0, sumX = 0.0, sumY = 0.0, sumXY = 0.0, sumX2 = 0.0;
        for (int i = 1; i < lines.size(); i++) {
            String[] parts = lines.get(i).split(",");
            double x = Double.parseDouble(parts[0]);
            double y = Double.parseDouble(parts[1]);
            n += 1.0;
            sumX += x; sumY += y; sumXY += x * y; sumX2 += x * x;
        }
        double slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
        double intercept = (sumY - slope * sumX) / n;
        long checksum = Math.round(slope * 1_000_000d) + Math.round(intercept * 1_000_000d);
        System.out.println(checksum);
    }
}
