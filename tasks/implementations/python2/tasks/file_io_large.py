from tasks.compat import emit, join_path, open_text


def run(size, fixtures_root):
    path = join_path(fixtures_root, 'generated', 'file_io', '%s.txt' % size)
    total = 0
    handle = open_text(path)
    try:
        for line in handle:
            total += int(line.strip())
    finally:
        handle.close()
    emit(total)
