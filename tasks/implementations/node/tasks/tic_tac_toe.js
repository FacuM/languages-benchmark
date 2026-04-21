const fs = require('fs');
const WIN_LINES = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
function winner(board, player) {
  return WIN_LINES.some(([a, b, c]) => board[a] === player && board[b] === player && board[c] === player);
}
module.exports = function(size, fixturesRoot) {
  const lines = fs.readFileSync(`${fixturesRoot}/generated/tic_tac_toe/${size}.txt`, 'utf8').trim().split(/\r?\n/);
  let total = 0;
  for (const line of lines) {
    const moves = line.split(/\s+/).map(Number);
    const board = new Array(9).fill(0);
    let moveCount = 0;
    let gameWinner = 0;
    for (let i = 0; i < moves.length; i++) {
      const player = i % 2 === 0 ? 1 : 2;
      board[moves[i]] = player;
      moveCount = i + 1;
      if (winner(board, player)) { gameWinner = player; break; }
    }
    const boardScore = board.reduce((acc, value, idx) => acc + value * (idx + 1), 0);
    total += gameWinner * 100 + moveCount * 10 + boardScore;
  }
  console.log(total);
};
