from tasks.compat import emit, join_path, read_lines

POSITIVE = set(['good', 'great', 'happy', 'clean', 'fast', 'love'])
NEGATIVE = set(['bad', 'sad', 'dirty', 'slow', 'hate', 'poor'])


def run(size, fixtures_root):
    path = join_path(fixtures_root, 'generated', 'sentiment', '%s.txt' % size)
    total = 0
    for line in read_lines(path):
        for token in line.split():
            if token in POSITIVE:
                total += 1
            elif token in NEGATIVE:
                total -= 1
    emit(total)
