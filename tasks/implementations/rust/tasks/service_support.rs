use std::fs;
use std::collections::HashMap;
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::process::Command;

const DB_PATH: &str = "/tmp/bench.sqlite";

fn sqlite(query: &str) -> String {
    let output = Command::new("sqlite3").arg(DB_PATH).arg(query).output().unwrap();
    if !output.status.success() {
        panic!("sqlite3 failed: {}", String::from_utf8_lossy(&output.stderr));
    }
    String::from_utf8(output.stdout).unwrap().trim().to_string()
}

pub fn start_http_service(task: &str, port: u16) {
    if task == "sqlite_crud" {
        sqlite("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value INTEGER);");
    }
    let listener = TcpListener::bind(("0.0.0.0", port)).unwrap();
    for stream in listener.incoming() {
        if let Ok(mut stream) = stream {
            handle_http_connection(task, &mut stream);
        }
    }
}

fn handle_http_connection(task: &str, stream: &mut TcpStream) {
    let mut request = Vec::new();
    let mut buffer = [0u8; 4096];
    loop {
        match stream.read(&mut buffer) {
            Ok(0) => break,
            Ok(n) => {
                request.extend_from_slice(&buffer[..n]);
                if request.windows(4).any(|w| w == b"\r\n\r\n") || request.len() > 65535 {
                    break;
                }
            }
            Err(_) => return,
        }
    }
    let request_text = String::from_utf8_lossy(&request);
    let first_line = request_text.lines().next().unwrap_or("GET / HTTP/1.1");
    let mut parts = first_line.split_whitespace();
    let _method = parts.next().unwrap_or("GET");
    let target = parts.next().unwrap_or("/");
    let (path, query) = parse_target(target);

    let (status, content_type, body) = if path == "/health" {
        ("200 OK", "text/plain", "ok".to_string())
    } else if task == "simple_web_server" && path == "/" {
        ("200 OK", "text/plain", "hello-benchmark".to_string())
    } else if task == "rest_api" && path == "/item" {
        let id: i64 = query.get("id").and_then(|x| x.parse().ok()).unwrap_or(0);
        ("200 OK", "application/json", format!("{{\"id\":{},\"value\":{}}}", id, id * 2))
    } else if ["gui_calculator", "data_visualization", "basic_web_application"].contains(&task) && path == "/" {
        ("200 OK", "text/html; charset=utf-8", fs::read_to_string(format!("/fixtures/ui/{}.html", task)).unwrap())
    } else if task == "sqlite_crud" {
        let id: i64 = query.get("id").and_then(|x| x.parse().ok()).unwrap_or(0);
        match path.as_str() {
            "/create" => {
                let value: i64 = query.get("value").and_then(|x| x.parse().ok()).unwrap_or(0);
                sqlite(&format!("INSERT OR REPLACE INTO items(id, value) VALUES({}, {});", id, value));
                ("200 OK", "application/json", format!("{{\"status\":\"created\",\"id\":{}}}", id))
            }
            "/read" => {
                let value = sqlite(&format!("SELECT value FROM items WHERE id={} LIMIT 1;", id));
                let body = if value.is_empty() {
                    format!("{{\"id\":{},\"value\":null}}", id)
                } else {
                    format!("{{\"id\":{},\"value\":{}}}", id, value)
                };
                ("200 OK", "application/json", body)
            }
            "/update" => {
                let value: i64 = query.get("value").and_then(|x| x.parse().ok()).unwrap_or(0);
                sqlite(&format!("UPDATE items SET value={} WHERE id={};", value, id));
                ("200 OK", "application/json", format!("{{\"status\":\"updated\",\"id\":{}}}", id))
            }
            "/delete" => {
                sqlite(&format!("DELETE FROM items WHERE id={};", id));
                ("200 OK", "application/json", format!("{{\"status\":\"deleted\",\"id\":{}}}", id))
            }
            _ => ("404 Not Found", "text/plain", "not-found".to_string()),
        }
    } else {
        ("404 Not Found", "text/plain", "not-found".to_string())
    };

    let response = format!(
        "HTTP/1.1 {}\r\nContent-Type: {}\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
        status,
        content_type,
        body.len(),
        body
    );
    let _ = stream.write_all(response.as_bytes());
}

fn parse_target(target: &str) -> (String, HashMap<String, String>) {
    let mut parts = target.splitn(2, '?');
    let path = parts.next().unwrap_or("/").to_string();
    let mut query = HashMap::new();
    if let Some(rest) = parts.next() {
        for pair in rest.split('&') {
            let mut kv = pair.splitn(2, '=');
            let key = kv.next().unwrap_or("").to_string();
            let value = kv.next().unwrap_or("").to_string();
            query.insert(key, value);
        }
    }
    (path, query)
}

pub fn start_tcp_service(task: &str, port: u16) {
    let listener = TcpListener::bind(("0.0.0.0", port)).unwrap();
    for stream in listener.incoming() {
        if let Ok(mut stream) = stream {
            let mut payload = Vec::new();
            let _ = stream.read_to_end(&mut payload);
            if payload.is_empty() {
                continue;
            }
            let input = String::from_utf8_lossy(&payload);
            let output = if task == "chat_application" {
                format!("chat:{}", input)
            } else {
                input.to_string()
            };
            let _ = stream.write_all(output.as_bytes());
        }
    }
}
