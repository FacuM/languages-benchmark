import re

from tasks.compat import emit, join_path, read_text


def run(size, fixtures_root):
    text = read_text(join_path(fixtures_root, 'mocks', 'ai_service_%s.json' % size))
    model = re.search(r'"model":\s*"([^"]+)"', text).group(1)
    total = len(model)
    for prompt, output, tokens in re.findall(r'"prompt":\s*"([^"]+)",\s*"output":\s*"([^"]+)",\s*"tokens":\s*(\d+)', text):
        total += len(prompt) + len(output) + int(tokens)
    emit(total)
