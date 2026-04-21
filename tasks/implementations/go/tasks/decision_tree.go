package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strconv"
    "strings"
)

var dtThresholds = []int{250, 500, 750}

type dtNode struct {
    leaf      bool
    value     int
    feature   int
    threshold int
    left      *dtNode
    right     *dtNode
}

func dtGini(rows [][]int) float64 {
    if len(rows) == 0 { return 0 }
    ones := 0
    for _, row := range rows { ones += row[3] }
    zeros := len(rows) - ones
    p0 := float64(zeros) / float64(len(rows))
    p1 := float64(ones) / float64(len(rows))
    return 1 - p0*p0 - p1*p1
}

func dtMajority(rows [][]int) int {
    ones := 0
    for _, row := range rows { ones += row[3] }
    if ones*2 >= len(rows) { return 1 }
    return 0
}

func dtBuild(rows [][]int, depth int) *dtNode {
    if depth == 0 || len(rows) == 0 { return &dtNode{leaf: true, value: dtMajority(rows)} }
    pure := true
    for _, row := range rows { if row[3] != rows[0][3] { pure = false; break } }
    if pure { return &dtNode{leaf: true, value: rows[0][3]} }
    var best *dtNode
    bestScore := 1e9
    for feature := 0; feature < 3; feature++ {
        for _, threshold := range dtThresholds {
            left := make([][]int, 0)
            right := make([][]int, 0)
            for _, row := range rows {
                if row[feature] <= threshold { left = append(left, row) } else { right = append(right, row) }
            }
            if len(left) == 0 || len(right) == 0 { continue }
            score := (float64(len(left))*dtGini(left) + float64(len(right))*dtGini(right)) / float64(len(rows))
            if score < bestScore {
                bestScore = score
                best = &dtNode{leaf: false, feature: feature, threshold: threshold, left: dtBuild(left, depth-1), right: dtBuild(right, depth-1)}
            }
        }
    }
    if best == nil { return &dtNode{leaf: true, value: dtMajority(rows)} }
    return best
}

func dtPredict(node *dtNode, row []int) int {
    if node.leaf { return node.value }
    if row[node.feature] <= node.threshold { return dtPredict(node.left, row) }
    return dtPredict(node.right, row)
}

func RunDecisionTree(size string, fixturesRoot string) {
    file, _ := os.Open(filepath.Join(fixturesRoot, "generated", "decision_tree", size+".csv"))
    defer file.Close()
    scanner := bufio.NewScanner(file)
    rows := make([][]int, 0)
    first := true
    for scanner.Scan() {
        if first { first = false; continue }
        parts := strings.Split(scanner.Text(), ",")
        row := make([]int, 4)
        for i, part := range parts {
            row[i], _ = strconv.Atoi(part)
        }
        rows = append(rows, row)
    }
    tree := dtBuild(rows, 3)
    correct := 0
    predSum := 0
    for idx, row := range rows {
        pred := dtPredict(tree, row)
        if pred == row[3] { correct++ }
        predSum += pred * (idx + 1)
    }
    fmt.Println(correct*100000 + predSum)
}
