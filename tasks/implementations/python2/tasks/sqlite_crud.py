from tasks.service_support import start_http_service


def start(size, port, fixtures_root):
    start_http_service('sqlite_crud', port)
