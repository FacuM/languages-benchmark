package main

func StartSqliteCrud(size string, port int, fixturesRoot string) {
    startHTTPService("sqlite_crud", port)
}
