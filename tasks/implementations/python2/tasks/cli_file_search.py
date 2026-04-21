from tasks.compat import emit, open_text, join_path, walk_text_files

KEYWORD = 'needle'


def run(size, fixtures_root):
    root = join_path(fixtures_root, 'generated', 'search', size)
    total = 0
    for path in walk_text_files(root):
        handle = open_text(path)
        try:
            for line in handle:
                if KEYWORD in line:
                    total += 1
        finally:
            handle.close()
    emit(total)
