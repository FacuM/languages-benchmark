package main

import (
    "encoding/csv"
    "fmt"
    "os"
    "path/filepath"
    "strconv"
)

func RunCSVParsing(size string, fixturesRoot string) {
    file, _ := os.Open(filepath.Join(fixturesRoot, "generated", "csv", size+".csv"))
    defer file.Close()
    reader := csv.NewReader(file)
    rows, _ := reader.ReadAll()
    total := 0
    for _, row := range rows[1:] {
        a, _ := strconv.Atoi(row[1])
        b, _ := strconv.Atoi(row[2])
        total += a + b
    }
    fmt.Println(total)
}
