#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>

static const std::string DB_PATH = "/tmp/bench.sqlite";

static std::string trim(std::string value) {
    while (!value.empty() && (value.back() == '\n' || value.back() == '\r' || value.back() == ' ')) value.pop_back();
    return value;
}

static std::string sqlite_query(const std::string& query) {
    std::string command = "sqlite3 '" + DB_PATH + "' '" + query + "'";
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) throw std::runtime_error("failed to execute sqlite3");
    char buffer[256];
    std::string output;
    while (fgets(buffer, sizeof(buffer), pipe)) output += buffer;
    int status = pclose(pipe);
    if (status != 0) throw std::runtime_error("sqlite3 command failed");
    return trim(output);
}

static std::map<std::string, std::string> parse_query(const std::string& target) {
    std::map<std::string, std::string> values;
    auto pos = target.find('?');
    if (pos == std::string::npos) return values;
    std::stringstream ss(target.substr(pos + 1));
    std::string item;
    while (std::getline(ss, item, '&')) {
        auto eq = item.find('=');
        if (eq == std::string::npos) values[item] = "";
        else values[item.substr(0, eq)] = item.substr(eq + 1);
    }
    return values;
}

static std::string path_only(const std::string& target) {
    auto pos = target.find('?');
    return pos == std::string::npos ? target : target.substr(0, pos);
}

static std::string json_pair(const std::string& key, const std::string& value, bool quoted = false) {
    return "\"" + key + "\":" + (quoted ? ("\"" + value + "\"") : value);
}

static std::string read_file_text(const std::string& path) {
    std::ifstream file(path);
    std::ostringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

static void send_response(int client, const std::string& status, const std::string& type, const std::string& body) {
    std::ostringstream out;
    out << "HTTP/1.1 " << status << "\r\n"
        << "Content-Type: " << type << "\r\n"
        << "Content-Length: " << body.size() << "\r\n"
        << "Connection: close\r\n\r\n"
        << body;
    std::string payload = out.str();
    send(client, payload.c_str(), payload.size(), 0);
}

void start_http_service(const std::string& task, int port) {
    if (task == "sqlite_crud") {
        sqlite_query("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value INTEGER);");
    }
    int server = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(server, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(port);
    bind(server, reinterpret_cast<sockaddr*>(&addr), sizeof(addr));
    listen(server, 128);

    while (true) {
        int client = accept(server, nullptr, nullptr);
        if (client < 0) continue;
        std::string request;
        char buffer[4096];
        while (request.find("\r\n\r\n") == std::string::npos) {
            ssize_t n = recv(client, buffer, sizeof(buffer), 0);
            if (n <= 0) break;
            request.append(buffer, buffer + n);
            if (request.size() > 65535) break;
        }
        std::istringstream line_stream(request);
        std::string method, target, version;
        line_stream >> method >> target >> version;
        std::string path = path_only(target.empty() ? "/" : target);
        auto query = parse_query(target);

        try {
            if (path == "/health") {
                send_response(client, "200 OK", "text/plain", "ok");
            } else if (task == "simple_web_server" && path == "/") {
                send_response(client, "200 OK", "text/plain", "hello-benchmark");
            } else if (task == "rest_api" && path == "/item") {
                int id = std::stoi(query.count("id") ? query["id"] : "0");
                send_response(client, "200 OK", "application/json", "{" + json_pair("id", std::to_string(id)) + "," + json_pair("value", std::to_string(id * 2)) + "}");
            } else if ((task == "gui_calculator" || task == "data_visualization" || task == "basic_web_application") && path == "/") {
                send_response(client, "200 OK", "text/html; charset=utf-8", read_file_text("/fixtures/ui/" + task + ".html"));
            } else if (task == "sqlite_crud") {
                int id = std::stoi(query.count("id") ? query["id"] : "0");
                if (path == "/create") {
                    int value = std::stoi(query.count("value") ? query["value"] : "0");
                    sqlite_query("INSERT OR REPLACE INTO items(id, value) VALUES(" + std::to_string(id) + ", " + std::to_string(value) + ");");
                    send_response(client, "200 OK", "application/json", "{" + json_pair("status", "created", true) + "," + json_pair("id", std::to_string(id)) + "}");
                } else if (path == "/read") {
                    std::string value = sqlite_query("SELECT value FROM items WHERE id=" + std::to_string(id) + " LIMIT 1;");
                    send_response(client, "200 OK", "application/json", value.empty() ? ("{" + json_pair("id", std::to_string(id)) + ",\"value\":null}") : ("{" + json_pair("id", std::to_string(id)) + "," + json_pair("value", value) + "}"));
                } else if (path == "/update") {
                    int value = std::stoi(query.count("value") ? query["value"] : "0");
                    sqlite_query("UPDATE items SET value=" + std::to_string(value) + " WHERE id=" + std::to_string(id) + ";");
                    send_response(client, "200 OK", "application/json", "{" + json_pair("status", "updated", true) + "," + json_pair("id", std::to_string(id)) + "}");
                } else if (path == "/delete") {
                    sqlite_query("DELETE FROM items WHERE id=" + std::to_string(id) + ";");
                    send_response(client, "200 OK", "application/json", "{" + json_pair("status", "deleted", true) + "," + json_pair("id", std::to_string(id)) + "}");
                } else {
                    send_response(client, "404 Not Found", "text/plain", "not-found");
                }
            } else {
                send_response(client, "404 Not Found", "text/plain", "not-found");
            }
        } catch (const std::exception& exc) {
            send_response(client, "500 Internal Server Error", "text/plain", exc.what());
        }
        close(client);
    }
}

void start_tcp_service(const std::string& task, int port) {
    int server = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(server, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(port);
    bind(server, reinterpret_cast<sockaddr*>(&addr), sizeof(addr));
    listen(server, 128);

    while (true) {
        int client = accept(server, nullptr, nullptr);
        if (client < 0) continue;
        std::string payload;
        char buffer[4096];
        while (true) {
            ssize_t n = recv(client, buffer, sizeof(buffer), 0);
            if (n <= 0) break;
            payload.append(buffer, buffer + n);
        }
        if (!payload.empty()) {
            std::string response = task == "chat_application" ? "chat:" + payload : payload;
            send(client, response.c_str(), response.size(), 0);
        }
        close(client);
    }
}
