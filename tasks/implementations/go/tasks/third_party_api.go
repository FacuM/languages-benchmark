package main

import (
    "fmt"
    "os"
    "path/filepath"
    "regexp"
    "strconv"
)

func RunThirdPartyApi(size string, fixturesRoot string) {
    data, _ := os.ReadFile(filepath.Join(fixturesRoot, "mocks", "twitter_like_"+size+".json"))
    re := regexp.MustCompile(`"id":\s*"([^"]+)",\s*"text":\s*"([^"]+)",\s*"likes":\s*(\d+)`)
    total := 0
    for _, match := range re.FindAllStringSubmatch(string(data), -1) {
        likes, _ := strconv.Atoi(match[3])
        total += len(match[1]) + len(match[2]) + likes
    }
    fmt.Println(total)
}
