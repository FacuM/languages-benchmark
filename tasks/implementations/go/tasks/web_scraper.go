package main

import (
    "fmt"
    "os"
    "path/filepath"
    "regexp"
)

func RunWebScraper(size string, fixturesRoot string) {
    base := filepath.Join(fixturesRoot, "mock_site", size)
    indexBytes, _ := os.ReadFile(filepath.Join(base, "index.html"))
    linkRe := regexp.MustCompile(`href="([^"]+)"`)
    titleRe := regexp.MustCompile(`<h2>(.*?)</h2>`)
    bodyRe := regexp.MustCompile(`<p>(.*?)</p>`)
    links := linkRe.FindAllStringSubmatch(string(indexBytes), -1)
    total := 0
    for idx, match := range links {
        pageBytes, _ := os.ReadFile(filepath.Join(base, match[1]))
        title := titleRe.FindStringSubmatch(string(pageBytes))[1]
        body := bodyRe.FindStringSubmatch(string(pageBytes))[1]
        total += (idx + 1) * (len(title) + len(body))
    }
    fmt.Println(total)
}
