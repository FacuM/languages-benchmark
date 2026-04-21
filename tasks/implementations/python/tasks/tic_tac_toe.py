from pathlib import Path

WIN_LINES = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

def _winner(board, player: int) -> bool:
    return any(board[a] == player and board[b] == player and board[c] == player for a, b, c in WIN_LINES)

def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "tic_tac_toe" / f"{size}.txt"
    total = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        moves = [int(x) for x in line.split()]
        board = [0] * 9
        winner = 0
        move_count = 0
        for idx, pos in enumerate(moves):
            player = 1 if idx % 2 == 0 else 2
            board[pos] = player
            move_count = idx + 1
            if _winner(board, player):
                winner = player
                break
        board_score = sum((idx + 1) * value for idx, value in enumerate(board))
        total += winner * 100 + move_count * 10 + board_score
    print(total)
