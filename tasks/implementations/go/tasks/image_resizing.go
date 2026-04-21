package main

import (
    "fmt"
    "os"
    "path/filepath"
    "strconv"
    "strings"
)

func RunImageResizing(size string, fixturesRoot string) {
    text, _ := os.ReadFile(filepath.Join(fixturesRoot, "generated", "image", size+".ppm"))
    tokens := strings.Fields(string(text))
    width, _ := strconv.Atoi(tokens[1])
    height, _ := strconv.Atoi(tokens[2])
    checksum := 0
    for y := 0; y < height/2; y++ {
        for x := 0; x < width/2; x++ {
            idx := 4 + (((y*2)*width + (x*2)) * 3)
            r, _ := strconv.Atoi(tokens[idx])
            g, _ := strconv.Atoi(tokens[idx+1])
            b, _ := strconv.Atoi(tokens[idx+2])
            checksum += r + g + b
        }
    }
    fmt.Println(checksum)
}
