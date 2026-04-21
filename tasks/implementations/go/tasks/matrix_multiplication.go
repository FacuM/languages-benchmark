package main

import (
    "fmt"
    "os"
    "path/filepath"
    "strconv"
    "strings"
)

func RunMatrixMultiplication(size string, fixturesRoot string) {
    text, _ := os.ReadFile(filepath.Join(fixturesRoot, "generated", "matrix", size+".txt"))
    tokens := strings.Fields(string(text))
    n, _ := strconv.Atoi(tokens[0])
    nums := make([]int, len(tokens)-1)
    for i, t := range tokens[1:] { nums[i], _ = strconv.Atoi(t) }
    split := n * n
    a := nums[:split]
    b := nums[split:]
    total := 0
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            cell := 0
            for k := 0; k < n; k++ {
                cell += a[i*n+k] * b[k*n+j]
            }
            total += cell
        }
    }
    fmt.Println(total)
}
