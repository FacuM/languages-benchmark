class SimpleWebServer {
    public static void start(String size, int port, String fixturesRoot) throws Exception {
        ServiceSupport.startHttpService("simple_web_server", port);
    }
}
