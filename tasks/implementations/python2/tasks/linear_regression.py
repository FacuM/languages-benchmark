import csv

from tasks.compat import emit, join_path, open_text


def run(size, fixtures_root):
    path = join_path(fixtures_root, 'generated', 'linear_regression', '%s.csv' % size)
    count = 0.0
    sum_x = sum_y = sum_xy = sum_x2 = 0.0
    handle = open_text(path)
    try:
        reader = csv.DictReader(handle)
        for row in reader:
            x = float(row['x'])
            y = float(row['y'])
            count += 1.0
            sum_x += x
            sum_y += y
            sum_xy += x * y
            sum_x2 += x * x
    finally:
        handle.close()
    slope = (count * sum_xy - sum_x * sum_y) / (count * sum_x2 - sum_x * sum_x)
    intercept = (sum_y - slope * sum_x) / count
    checksum = int(round(slope * 1000000)) + int(round(intercept * 1000000))
    emit(checksum)
