import java.nio.file.*;

class BinarySearchTree {
    static final class Node {
        int value; Node left; Node right;
        Node(int value) { this.value = value; }
    }

    static Node insert(Node root, int value) {
        if (root == null) return new Node(value);
        Node node = root;
        while (true) {
            if (value < node.value) {
                if (node.left == null) { node.left = new Node(value); return root; }
                node = node.left;
            } else if (value > node.value) {
                if (node.right == null) { node.right = new Node(value); return root; }
                node = node.right;
            } else {
                return root;
            }
        }
    }

    static boolean contains(Node root, int value) {
        Node node = root;
        while (node != null) {
            if (value < node.value) node = node.left;
            else if (value > node.value) node = node.right;
            else return true;
        }
        return false;
    }

    public static void run(String size, String fixturesRoot) throws Exception {
        String[] tokens = Files.readString(Path.of(fixturesRoot, "generated", "bst", size + ".txt")).trim().split("\\s+");
        int insertCount = Integer.parseInt(tokens[0]);
        Node root = null;
        for (int i = 0; i < insertCount; i++) root = insert(root, Integer.parseInt(tokens[1 + i]));
        int queryCountIndex = 1 + insertCount;
        int queryCount = Integer.parseInt(tokens[queryCountIndex]);
        long total = 0;
        for (int i = 0; i < queryCount; i++) {
            int value = Integer.parseInt(tokens[queryCountIndex + 1 + i]);
            if (contains(root, value)) total += value;
        }
        System.out.println(total);
    }
}
