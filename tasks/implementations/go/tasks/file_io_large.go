package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strconv"
)

func RunFileIOLarge(size string, fixturesRoot string) {
    file, _ := os.Open(filepath.Join(fixturesRoot, "generated", "file_io", size+".txt"))
    defer file.Close()
    scanner := bufio.NewScanner(file)
    var total int64 = 0
    for scanner.Scan() {
        value, _ := strconv.ParseInt(scanner.Text(), 10, 64)
        total += value
    }
    fmt.Println(total)
}
