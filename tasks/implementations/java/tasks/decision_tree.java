import java.nio.file.*;
import java.util.*;

class DecisionTree {
    static final int[] THRESHOLDS = {250, 500, 750};
    static final int MAX_DEPTH = 3;

    static final class Node {
        boolean leaf;
        int value;
        int feature;
        int threshold;
        Node left;
        Node right;
    }

    static double gini(List<int[]> rows) {
        if (rows.isEmpty()) return 0.0;
        int ones = 0;
        for (int[] row : rows) ones += row[3];
        int zeros = rows.size() - ones;
        double p0 = zeros / (double) rows.size();
        double p1 = ones / (double) rows.size();
        return 1.0 - p0 * p0 - p1 * p1;
    }

    static int majority(List<int[]> rows) {
        int ones = 0;
        for (int[] row : rows) ones += row[3];
        return ones * 2 >= rows.size() ? 1 : 0;
    }

    static Node leaf(int value) {
        Node node = new Node();
        node.leaf = true;
        node.value = value;
        return node;
    }

    static Node build(List<int[]> rows, int depth) {
        if (depth == 0 || rows.isEmpty()) return leaf(rows.isEmpty() ? 0 : majority(rows));
        boolean pure = true;
        for (int[] row : rows) if (row[3] != rows.get(0)[3]) { pure = false; break; }
        if (pure) return leaf(rows.get(0)[3]);
        Node bestNode = null;
        double bestScore = Double.POSITIVE_INFINITY;
        for (int feature = 0; feature < 3; feature++) {
            for (int threshold : THRESHOLDS) {
                List<int[]> left = new ArrayList<>();
                List<int[]> right = new ArrayList<>();
                for (int[] row : rows) {
                    if (row[feature] <= threshold) left.add(row); else right.add(row);
                }
                if (left.isEmpty() || right.isEmpty()) continue;
                double score = (left.size() * gini(left) + right.size() * gini(right)) / rows.size();
                if (score < bestScore) {
                    bestScore = score;
                    Node node = new Node();
                    node.feature = feature;
                    node.threshold = threshold;
                    node.left = build(left, depth - 1);
                    node.right = build(right, depth - 1);
                    bestNode = node;
                }
            }
        }
        return bestNode == null ? leaf(majority(rows)) : bestNode;
    }

    static int predict(Node node, int[] row) {
        if (node.leaf) return node.value;
        return predict(row[node.feature] <= node.threshold ? node.left : node.right, row);
    }

    public static void run(String size, String fixturesRoot) throws Exception {
        List<String> lines = Files.readAllLines(Path.of(fixturesRoot, "generated", "decision_tree", size + ".csv"));
        List<int[]> rows = new ArrayList<>();
        for (int i = 1; i < lines.size(); i++) {
            String[] parts = lines.get(i).split(",");
            rows.add(new int[] {Integer.parseInt(parts[0]), Integer.parseInt(parts[1]), Integer.parseInt(parts[2]), Integer.parseInt(parts[3])});
        }
        Node tree = build(rows, MAX_DEPTH);
        long correct = 0;
        long predSum = 0;
        for (int i = 0; i < rows.size(); i++) {
            int pred = predict(tree, rows.get(i));
            if (pred == rows.get(i)[3]) correct += 1;
            predSum += (long) pred * (i + 1L);
        }
        System.out.println(correct * 100000L + predSum);
    }
}
