package main

import (
    "fmt"
    "os"
    "path/filepath"
    "regexp"
    "strconv"
)

func RunAiServiceIntegration(size string, fixturesRoot string) {
    data, _ := os.ReadFile(filepath.Join(fixturesRoot, "mocks", "ai_service_"+size+".json"))
    modelRe := regexp.MustCompile(`"model":\s*"([^"]+)"`)
    rowRe := regexp.MustCompile(`"prompt":\s*"([^"]+)",\s*"output":\s*"([^"]+)",\s*"tokens":\s*(\d+)`)
    total := len(modelRe.FindStringSubmatch(string(data))[1])
    for _, match := range rowRe.FindAllStringSubmatch(string(data), -1) {
        tokens, _ := strconv.Atoi(match[3])
        total += len(match[1]) + len(match[2]) + tokens
    }
    fmt.Println(total)
}
