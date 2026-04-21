package main

import (
    "fmt"
    "os"
    "path/filepath"
    "regexp"
    "strconv"
)

func RunApiClient(size string, fixturesRoot string) {
    data, _ := os.ReadFile(filepath.Join(fixturesRoot, "mocks", "public_api_"+size+".json"))
    re := regexp.MustCompile(`"id":\s*(\d+),\s*"name":\s*"([^"]+)",\s*"value":\s*(\d+)`)
    total := 0
    for _, match := range re.FindAllStringSubmatch(string(data), -1) {
        id, _ := strconv.Atoi(match[1])
        value, _ := strconv.Atoi(match[3])
        total += id + value + len(match[2])
    }
    fmt.Println(total)
}
