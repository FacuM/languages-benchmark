package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strconv"
)

func RunProducerConsumer(size string, fixturesRoot string) {
    const mod uint64 = 4294967291
    const capacity = 64
    file, _ := os.Open(filepath.Join(fixturesRoot, "generated", "producer_consumer", size+".txt"))
    defer file.Close()
    scanner := bufio.NewScanner(file)
    values := make([]int, 0)
    for scanner.Scan() {
        value, _ := strconv.Atoi(scanner.Text())
        values = append(values, value)
    }
    buffer := make([]int, capacity)
    head, tail, count := 0, 0, 0
    produced := 0
    consumed := uint64(0)
    checksum := uint64(0)
    for produced < len(values) || count > 0 {
        for produced < len(values) && count < capacity {
            buffer[tail] = values[produced]
            tail = (tail + 1) % capacity
            produced++
            count++
        }
        if count > 0 {
            value := buffer[head]
            head = (head + 1) % capacity
            count--
            checksum = (checksum + uint64(value)*(consumed+1)) % mod
            consumed++
        }
    }
    fmt.Println(checksum)
}
