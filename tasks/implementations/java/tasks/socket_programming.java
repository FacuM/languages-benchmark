class SocketProgramming {
    public static void start(String size, int port, String fixturesRoot) throws Exception {
        ServiceSupport.startTcpService("socket_programming", port);
    }
}
