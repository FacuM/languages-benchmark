package main

import (
    "encoding/csv"
    "fmt"
    "math"
    "os"
    "path/filepath"
    "strconv"
)

func RunLinearRegression(size string, fixturesRoot string) {
    file, _ := os.Open(filepath.Join(fixturesRoot, "generated", "linear_regression", size+".csv"))
    defer file.Close()
    rows, _ := csv.NewReader(file).ReadAll()
    n := 0.0
    sumX, sumY, sumXY, sumX2 := 0.0, 0.0, 0.0, 0.0
    for _, row := range rows[1:] {
        x, _ := strconv.ParseFloat(row[0], 64)
        y, _ := strconv.ParseFloat(row[1], 64)
        n += 1.0
        sumX += x; sumY += y; sumXY += x * y; sumX2 += x * x
    }
    slope := (n*sumXY - sumX*sumY) / (n*sumX2 - sumX*sumX)
    intercept := (sumY - slope*sumX) / n
    checksum := math.Round(slope*1000000) + math.Round(intercept*1000000)
    fmt.Println(int64(checksum))
}
