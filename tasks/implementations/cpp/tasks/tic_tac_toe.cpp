#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

static const int WIN_LINES[8][3] = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}};

static bool winner(const std::vector<int>& board, int player) {
    for (const auto& line : WIN_LINES) {
        if (board[line[0]] == player && board[line[1]] == player && board[line[2]] == player) return true;
    }
    return false;
}

void run_tic_tac_toe(const std::string& size, const std::string& fixturesRoot) {
    std::ifstream file(fixturesRoot + "/generated/tic_tac_toe/" + size + ".txt");
    std::string line;
    long long total = 0;
    while (std::getline(file, line)) {
        if (line.empty()) continue;
        std::stringstream ss(line);
        std::vector<int> moves;
        int value = 0;
        while (ss >> value) moves.push_back(value);
        std::vector<int> board(9, 0);
        int move_count = 0;
        int game_winner = 0;
        for (int i = 0; i < static_cast<int>(moves.size()); ++i) {
            int player = i % 2 == 0 ? 1 : 2;
            board[moves[i]] = player;
            move_count = i + 1;
            if (winner(board, player)) { game_winner = player; break; }
        }
        int board_score = 0;
        for (int i = 0; i < 9; ++i) board_score += (i + 1) * board[i];
        total += game_winner * 100LL + move_count * 10LL + board_score;
    }
    std::cout << total << std::endl;
}
