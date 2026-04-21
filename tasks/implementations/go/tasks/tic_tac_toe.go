package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strconv"
    "strings"
)

var tttLines = [8][3]int{{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}}

func tttWinner(board [9]int, player int) bool {
    for _, line := range tttLines {
        if board[line[0]] == player && board[line[1]] == player && board[line[2]] == player { return true }
    }
    return false
}

func RunTicTacToe(size string, fixturesRoot string) {
    file, _ := os.Open(filepath.Join(fixturesRoot, "generated", "tic_tac_toe", size+".txt"))
    defer file.Close()
    scanner := bufio.NewScanner(file)
    total := 0
    for scanner.Scan() {
        line := strings.TrimSpace(scanner.Text())
        if line == "" { continue }
        parts := strings.Fields(line)
        board := [9]int{}
        moveCount := 0
        gameWinner := 0
        for idx, token := range parts {
            pos, _ := strconv.Atoi(token)
            player := 1
            if idx%2 == 1 { player = 2 }
            board[pos] = player
            moveCount = idx + 1
            if tttWinner(board, player) { gameWinner = player; break }
        }
        boardScore := 0
        for idx, value := range board { boardScore += (idx + 1) * value }
        total += gameWinner*100 + moveCount*10 + boardScore
    }
    fmt.Println(total)
}
