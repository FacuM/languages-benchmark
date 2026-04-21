class SqliteCrud {
    public static void start(String size, int port, String fixturesRoot) throws Exception {
        ServiceSupport.startHttpService("sqlite_crud", port);
    }
}
