package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "sort"
    "strconv"
)

func RunSortIntegers(size string, fixturesRoot string) {
    path := filepath.Join(fixturesRoot, "generated", "sort", size+".txt")
    file, _ := os.Open(path)
    defer file.Close()
    scanner := bufio.NewScanner(file)
    values := make([]int, 0)
    for scanner.Scan() {
        n, _ := strconv.Atoi(scanner.Text())
        values = append(values, n)
    }
    sort.Ints(values)
    total := 0
    for i := 0; i < 100 && i < len(values); i++ { total += values[i] }
    fmt.Println(total)
}
