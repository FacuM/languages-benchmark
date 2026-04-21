class RestApi {
    public static void start(String size, int port, String fixturesRoot) throws Exception {
        ServiceSupport.startHttpService("rest_api", port);
    }
}
