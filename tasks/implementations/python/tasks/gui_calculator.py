from tasks.service_support import start_http_service

def start(size: str, port: int, fixtures_root: str) -> None:
    start_http_service("gui_calculator", port)
