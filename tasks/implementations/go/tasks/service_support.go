package main

import (
    "encoding/json"
    "fmt"
    "net"
    "net/http"
    "os"
    "os/exec"
    "strconv"
)

const dbPath = "/tmp/bench.sqlite"

func sqlite(query string) string {
    out, err := exec.Command("sqlite3", dbPath, query).CombinedOutput()
    if err != nil { panic(string(out)) }
    return string(bytesTrim(out))
}

func bytesTrim(value []byte) []byte {
    for len(value) > 0 && (value[len(value)-1] == '\n' || value[len(value)-1] == '\r' || value[len(value)-1] == ' ') {
        value = value[:len(value)-1]
    }
    return value
}

func startHTTPService(task string, port int) {
    if task == "sqlite_crud" {
        sqlite("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value INTEGER);")
    }
    mux := http.NewServeMux()
    mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) { fmt.Fprint(w, "ok") })
    mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        switch task {
        case "simple_web_server":
            fmt.Fprint(w, "hello-benchmark")
        case "rest_api":
            if r.URL.Path != "/item" { http.NotFound(w, r); return }
            id, _ := strconv.Atoi(r.URL.Query().Get("id"))
            json.NewEncoder(w).Encode(map[string]int{"id": id, "value": id * 2})
        case "gui_calculator", "data_visualization", "basic_web_application":
            if r.URL.Path != "/" { http.NotFound(w, r); return }
            body, _ := os.ReadFile("/fixtures/ui/" + task + ".html")
            w.Header().Set("Content-Type", "text/html; charset=utf-8")
            fmt.Fprint(w, string(body))
        case "sqlite_crud":
            id, _ := strconv.Atoi(r.URL.Query().Get("id"))
            switch r.URL.Path {
            case "/create":
                value, _ := strconv.Atoi(r.URL.Query().Get("value"))
                sqlite(fmt.Sprintf("INSERT OR REPLACE INTO items(id, value) VALUES(%d, %d);", id, value))
                json.NewEncoder(w).Encode(map[string]any{"status": "created", "id": id})
            case "/read":
                value := sqlite(fmt.Sprintf("SELECT value FROM items WHERE id=%d LIMIT 1;", id))
                if value == "" { json.NewEncoder(w).Encode(map[string]any{"id": id, "value": nil}) } else { parsed, _ := strconv.Atoi(value); json.NewEncoder(w).Encode(map[string]any{"id": id, "value": parsed}) }
            case "/update":
                value, _ := strconv.Atoi(r.URL.Query().Get("value"))
                sqlite(fmt.Sprintf("UPDATE items SET value=%d WHERE id=%d;", value, id))
                json.NewEncoder(w).Encode(map[string]any{"status": "updated", "id": id})
            case "/delete":
                sqlite(fmt.Sprintf("DELETE FROM items WHERE id=%d;", id))
                json.NewEncoder(w).Encode(map[string]any{"status": "deleted", "id": id})
            default:
                http.NotFound(w, r)
            }
        default:
            http.NotFound(w, r)
        }
    })
    http.ListenAndServe(fmt.Sprintf(":%d", port), mux)
}

func startTCPService(task string, port int) {
    listener, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
    if err != nil { panic(err) }
    for {
        conn, err := listener.Accept()
        if err != nil { continue }
        go func(c net.Conn) {
            defer c.Close()
            buf := make([]byte, 4096)
            n, _ := c.Read(buf)
            if n <= 0 { return }
            payload := string(buf[:n])
            if task == "chat_application" { c.Write([]byte("chat:" + payload)) } else { c.Write([]byte(payload)) }
        }(conn)
    }
}
