package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strconv"
    "strings"
)

func RunBasicBlockchain(size string, fixturesRoot string) {
    const mod uint64 = 4294967291
    const mult uint64 = 16777619
    file, _ := os.Open(filepath.Join(fixturesRoot, "generated", "blockchain", size+".txt"))
    defer file.Close()
    scanner := bufio.NewScanner(file)
    var prevHash uint64 = 2166136261
    var total uint64 = 0
    index := uint64(0)
    for scanner.Scan() {
        line := strings.TrimSpace(scanner.Text())
        if line == "" { continue }
        hashValue := prevHash
        for _, token := range strings.Fields(line) {
            tx, _ := strconv.ParseUint(token, 10, 64)
            hashValue = (hashValue*mult + tx + index + 1) % mod
        }
        total = (total + hashValue) % mod
        prevHash = hashValue
        index++
    }
    fmt.Println(total)
}
