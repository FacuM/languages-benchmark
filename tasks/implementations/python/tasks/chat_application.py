from tasks.service_support import start_tcp_service

def start(size: str, port: int, fixtures_root: str) -> None:
    start_tcp_service("chat_application", port)
