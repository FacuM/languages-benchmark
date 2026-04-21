use std::fs;

const WIN_LINES: [[usize; 3]; 8] = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

fn winner(board: &[i64; 9], player: i64) -> bool {
    WIN_LINES.iter().any(|line| board[line[0]] == player && board[line[1]] == player && board[line[2]] == player)
}

pub fn run(size: &str, fixtures_root: &str) {
    let text = fs::read_to_string(format!("{}/generated/tic_tac_toe/{}.txt", fixtures_root, size)).unwrap();
    let mut total = 0i64;
    for line in text.lines() {
        if line.is_empty() { continue; }
        let moves: Vec<usize> = line.split_whitespace().map(|x| x.parse::<usize>().unwrap()).collect();
        let mut board = [0i64; 9];
        let mut move_count = 0i64;
        let mut game_winner = 0i64;
        for (idx, pos) in moves.iter().enumerate() {
            let player = if idx % 2 == 0 { 1 } else { 2 };
            board[*pos] = player;
            move_count = idx as i64 + 1;
            if winner(&board, player) { game_winner = player; break; }
        }
        let board_score: i64 = board.iter().enumerate().map(|(idx, value)| (idx as i64 + 1) * *value).sum();
        total += game_winner * 100 + move_count * 10 + board_score;
    }
    println!("{}", total);
}
