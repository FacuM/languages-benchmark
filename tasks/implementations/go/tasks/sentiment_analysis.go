package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strings"
)

func RunSentimentAnalysis(size string, fixturesRoot string) {
    positive := map[string]bool{"good": true, "great": true, "happy": true, "clean": true, "fast": true, "love": true}
    negative := map[string]bool{"bad": true, "sad": true, "dirty": true, "slow": true, "hate": true, "poor": true}
    file, _ := os.Open(filepath.Join(fixturesRoot, "generated", "sentiment", size+".txt"))
    defer file.Close()
    scanner := bufio.NewScanner(file)
    total := 0
    for scanner.Scan() {
        for _, token := range strings.Fields(scanner.Text()) {
            if positive[token] { total++ } else if negative[token] { total-- }
        }
    }
    fmt.Println(total)
}
