import re

from tasks.compat import emit, join_path, read_text


def _extract(pattern, text):
    return re.findall(pattern, text, flags=re.IGNORECASE)


def run(size, fixtures_root):
    base = join_path(fixtures_root, 'mock_site', size)
    index = read_text(join_path(base, 'index.html'))
    links = _extract(r'href="([^"]+)"', index)
    total = 0
    for idx, link in enumerate(links):
        text = read_text(join_path(base, link))
        title = _extract(r'<h2>(.*?)</h2>', text)[0]
        body = _extract(r'<p>(.*?)</p>', text)[0]
        total += (idx + 1) * (len(title) + len(body))
    emit(total)
