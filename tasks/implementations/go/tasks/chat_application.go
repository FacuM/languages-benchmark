package main

func StartChatApplication(size string, port int, fixturesRoot string) {
    startTCPService("chat_application", port)
}
