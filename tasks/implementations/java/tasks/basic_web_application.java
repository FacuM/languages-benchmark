class BasicWebApplication {
    public static void start(String size, int port, String fixturesRoot) throws Exception {
        ServiceSupport.startHttpService("basic_web_application", port);
    }
}
