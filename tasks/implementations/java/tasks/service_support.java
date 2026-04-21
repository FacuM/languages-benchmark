import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

class ServiceSupport {
    static final String DB_PATH = "/tmp/bench.sqlite";

    static String sqlite(String query) throws Exception {
        Process proc = new ProcessBuilder("sqlite3", DB_PATH, query).start();
        byte[] out = proc.getInputStream().readAllBytes();
        byte[] err = proc.getErrorStream().readAllBytes();
        int code = proc.waitFor();
        if (code != 0) throw new RuntimeException(new String(err, StandardCharsets.UTF_8));
        return new String(out, StandardCharsets.UTF_8).trim();
    }

    static void startHttpService(String task, int port) throws Exception {
        if (task.equals("sqlite_crud")) {
            sqlite("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, value INTEGER);");
        }
        HttpServer server = HttpServer.create(new InetSocketAddress("0.0.0.0", port), 0);
        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                try {
                    String path = exchange.getRequestURI().getPath();
                    Map<String, String> query = parseQuery(exchange.getRequestURI().getRawQuery());
                    if (path.equals("/health")) {
                        send(exchange, 200, "text/plain", "ok");
                        return;
                    }
                    if (task.equals("simple_web_server") && path.equals("/")) {
                        send(exchange, 200, "text/plain", "hello-benchmark");
                        return;
                    }
                    if (task.equals("rest_api") && path.equals("/item")) {
                        int id = Integer.parseInt(query.getOrDefault("id", "0"));
                        send(exchange, 200, "application/json", String.format("{\"id\":%d,\"value\":%d}", id, id * 2));
                        return;
                    }
                    if ((task.equals("gui_calculator") || task.equals("data_visualization") || task.equals("basic_web_application")) && path.equals("/")) {
                        send(exchange, 200, "text/html; charset=utf-8", Files.readString(Path.of("/fixtures", "ui", task + ".html")));
                        return;
                    }
                    if (task.equals("sqlite_crud")) {
                        int id = Integer.parseInt(query.getOrDefault("id", "0"));
                        if (path.equals("/create")) {
                            int value = Integer.parseInt(query.getOrDefault("value", "0"));
                            sqlite("INSERT OR REPLACE INTO items(id, value) VALUES(" + id + ", " + value + ");");
                            send(exchange, 200, "application/json", String.format("{\"status\":\"created\",\"id\":%d}", id));
                            return;
                        }
                        if (path.equals("/read")) {
                            String value = sqlite("SELECT value FROM items WHERE id=" + id + " LIMIT 1;");
                            String body = value.isEmpty() ? String.format("{\"id\":%d,\"value\":null}", id) : String.format("{\"id\":%d,\"value\":%d}", id, Integer.parseInt(value));
                            send(exchange, 200, "application/json", body);
                            return;
                        }
                        if (path.equals("/update")) {
                            int value = Integer.parseInt(query.getOrDefault("value", "0"));
                            sqlite("UPDATE items SET value=" + value + " WHERE id=" + id + ";");
                            send(exchange, 200, "application/json", String.format("{\"status\":\"updated\",\"id\":%d}", id));
                            return;
                        }
                        if (path.equals("/delete")) {
                            sqlite("DELETE FROM items WHERE id=" + id + ";");
                            send(exchange, 200, "application/json", String.format("{\"status\":\"deleted\",\"id\":%d}", id));
                            return;
                        }
                    }
                    send(exchange, 404, "text/plain", "not-found");
                } catch (Exception exc) {
                    send(exchange, 500, "text/plain", exc.toString());
                }
            }
        });
        server.start();
        Thread.currentThread().join();
    }

    static void startTcpService(String task, int port) throws Exception {
        try (ServerSocket server = new ServerSocket(port)) {
            while (true) {
                Socket socket = server.accept();
                try (socket; InputStream in = socket.getInputStream(); OutputStream out = socket.getOutputStream()) {
                    ByteArrayOutputStream buffer = new ByteArrayOutputStream();
                    while (true) {
                        int value = in.read();
                        if (value < 0) break;
                        buffer.write(value);
                        if (value == '\n') break;
                    }
                    String payload = buffer.toString(StandardCharsets.UTF_8);
                    if (!payload.isEmpty()) {
                        String response = task.equals("chat_application") ? "chat:" + payload : payload;
                        out.write(response.getBytes(StandardCharsets.UTF_8));
                        out.flush();
                    }
                }
            }
        }
    }

    static void send(HttpExchange exchange, int status, String type, String body) throws IOException {
        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", type);
        exchange.sendResponseHeaders(status, bytes.length);
        try (OutputStream out = exchange.getResponseBody()) {
            out.write(bytes);
        }
    }

    static Map<String, String> parseQuery(String rawQuery) {
        Map<String, String> result = new HashMap<>();
        if (rawQuery == null || rawQuery.isBlank()) return result;
        for (String pair : rawQuery.split("&")) {
            String[] parts = pair.split("=", 2);
            String key = URLDecoder.decode(parts[0], StandardCharsets.UTF_8);
            String value = parts.length > 1 ? URLDecoder.decode(parts[1], StandardCharsets.UTF_8) : "";
            result.put(key, value);
        }
        return result;
    }
}
