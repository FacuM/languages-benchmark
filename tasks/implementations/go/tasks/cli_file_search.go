package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strings"
)

func RunCliFileSearch(size string, fixturesRoot string) {
    root := filepath.Join(fixturesRoot, "generated", "search", size)
    total := 0
    filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
        if err != nil || info == nil || info.IsDir() || !strings.HasSuffix(path, ".txt") {
            return nil
        }
        file, _ := os.Open(path)
        defer file.Close()
        scanner := bufio.NewScanner(file)
        for scanner.Scan() {
            if strings.Contains(scanner.Text(), "needle") { total++ }
        }
        return nil
    })
    fmt.Println(total)
}
