import java.nio.file.*;
import java.util.*;

class TicTacToe {
    static final int[][] WIN_LINES = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}};

    static boolean winner(int[] board, int player) {
        for (int[] line : WIN_LINES) {
            if (board[line[0]] == player && board[line[1]] == player && board[line[2]] == player) return true;
        }
        return false;
    }

    public static void run(String size, String fixturesRoot) throws Exception {
        List<String> lines = Files.readAllLines(Path.of(fixturesRoot, "generated", "tic_tac_toe", size + ".txt"));
        long total = 0;
        for (String line : lines) {
            if (line.isBlank()) continue;
            String[] parts = line.trim().split("\\s+");
            int[] board = new int[9];
            int moveCount = 0;
            int gameWinner = 0;
            for (int i = 0; i < parts.length; i++) {
                int player = i % 2 == 0 ? 1 : 2;
                board[Integer.parseInt(parts[i])] = player;
                moveCount = i + 1;
                if (winner(board, player)) { gameWinner = player; break; }
            }
            int boardScore = 0;
            for (int i = 0; i < board.length; i++) boardScore += (i + 1) * board[i];
            total += gameWinner * 100L + moveCount * 10L + boardScore;
        }
        System.out.println(total);
    }
}
