import re

from tasks.compat import emit, join_path, read_text


def run(size, fixtures_root):
    text = read_text(join_path(fixtures_root, 'mocks', 'public_api_%s.json' % size))
    total = 0
    for item_id, name, value in re.findall(r'"id":\s*(\d+),\s*"name":\s*"([^"]+)",\s*"value":\s*(\d+)', text):
        total += int(item_id) + int(value) + len(name)
    emit(total)
