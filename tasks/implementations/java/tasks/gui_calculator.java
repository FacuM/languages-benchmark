class GuiCalculator {
    public static void start(String size, int port, String fixturesRoot) throws Exception {
        ServiceSupport.startHttpService("gui_calculator", port);
    }
}
