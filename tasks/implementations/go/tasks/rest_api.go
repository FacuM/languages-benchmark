package main

func StartRestApi(size string, port int, fixturesRoot string) {
    startHTTPService("rest_api", port)
}
