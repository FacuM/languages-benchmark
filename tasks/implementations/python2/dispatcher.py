import importlib
import os
import sys

DISPATCH = {
    "sort_integers": ("tasks.sort_integers", "run"),
    "matrix_multiplication": ("tasks.matrix_multiplication", "run"),
    "csv_parsing": ("tasks.csv_parsing", "run"),
    "prime_sieve": ("tasks.prime_sieve", "run"),
    "file_io_large": ("tasks.file_io_large", "run"),
    "binary_search_tree": ("tasks.binary_search_tree", "run"),
    "linear_regression": ("tasks.linear_regression", "run"),
    "cli_file_search": ("tasks.cli_file_search", "run"),
    "tic_tac_toe": ("tasks.tic_tac_toe", "run"),
    "basic_blockchain": ("tasks.basic_blockchain", "run"),
    "image_resizing": ("tasks.image_resizing", "run"),
    "sentiment_analysis": ("tasks.sentiment_analysis", "run"),
    "decision_tree": ("tasks.decision_tree", "run"),
    "producer_consumer": ("tasks.producer_consumer", "run"),
    "web_scraper": ("tasks.web_scraper", "run"),
    "api_client": ("tasks.api_client", "run"),
    "third_party_api": ("tasks.third_party_api", "run"),
    "ai_service_integration": ("tasks.ai_service_integration", "run"),
}

SERVICE_DISPATCH = {
    "simple_web_server": ("tasks.simple_web_server", "start"),
    "rest_api": ("tasks.rest_api", "start"),
    "sqlite_crud": ("tasks.sqlite_crud", "start"),
    "chat_application": ("tasks.chat_application", "start"),
    "socket_programming": ("tasks.socket_programming", "start"),
    "gui_calculator": ("tasks.gui_calculator", "start"),
    "data_visualization": ("tasks.data_visualization", "start"),
    "basic_web_application": ("tasks.basic_web_application", "start"),
}


def _resolve(mapping, task_id):
    module_name, attr_name = mapping[task_id]
    module = importlib.import_module(module_name)
    return getattr(module, attr_name)


if __name__ == '__main__':
    if sys.argv[1] == 'start':
        task_id, size = sys.argv[2], sys.argv[3]
        if task_id not in SERVICE_DISPATCH:
            raise SystemExit('unsupported service task: {0}'.format(task_id))
        _resolve(SERVICE_DISPATCH, task_id)(size, int(os.environ.get('PORT', '8000')), '/fixtures')
        raise SystemExit(0)

    task_id, size = sys.argv[1], sys.argv[2]
    if task_id not in DISPATCH:
        raise SystemExit('unsupported task: {0}'.format(task_id))
    _resolve(DISPATCH, task_id)(size, '/fixtures')
