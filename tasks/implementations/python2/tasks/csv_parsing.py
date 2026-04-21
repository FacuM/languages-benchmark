import csv

from tasks.compat import emit, join_path, open_text


def run(size, fixtures_root):
    path = join_path(fixtures_root, 'generated', 'csv', '%s.csv' % size)
    total = 0
    handle = open_text(path)
    try:
        reader = csv.DictReader(handle)
        for row in reader:
            total += int(row['value_a']) + int(row['value_b'])
    finally:
        handle.close()
    emit(total)
