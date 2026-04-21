from tasks.service_support import start_tcp_service


def start(size, port, fixtures_root):
    start_tcp_service('socket_programming', port)
