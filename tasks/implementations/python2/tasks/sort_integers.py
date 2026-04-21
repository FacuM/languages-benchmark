from tasks.compat import emit, join_path, read_text


def run(size, fixtures_root):
    path = join_path(fixtures_root, 'generated', 'sort', '%s.txt' % size)
    values = [int(x) for x in read_text(path).split()]
    values.sort()
    emit(sum(values[:100]))
