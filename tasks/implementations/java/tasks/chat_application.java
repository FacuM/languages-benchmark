class ChatApplication {
    public static void start(String size, int port, String fixturesRoot) throws Exception {
        ServiceSupport.startTcpService("chat_application", port);
    }
}
