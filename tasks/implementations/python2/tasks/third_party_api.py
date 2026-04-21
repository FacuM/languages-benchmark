import re

from tasks.compat import emit, join_path, read_text


def run(size, fixtures_root):
    text = read_text(join_path(fixtures_root, 'mocks', 'twitter_like_%s.json' % size))
    total = 0
    for post_id, body, likes in re.findall(r'"id":\s*"([^"]+)",\s*"text":\s*"([^"]+)",\s*"likes":\s*(\d+)', text):
        total += len(post_id) + len(body) + int(likes)
    emit(total)
