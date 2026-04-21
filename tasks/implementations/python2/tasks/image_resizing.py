from tasks.compat import emit, join_path, read_text


def run(size, fixtures_root):
    tokens = read_text(join_path(fixtures_root, 'generated', 'image', '%s.ppm' % size)).split()
    width = int(tokens[1])
    height = int(tokens[2])
    data = [int(x) for x in tokens[4:]]
    checksum = 0
    for y in xrange(height // 2):
        for x in xrange(width // 2):
            idx = ((y * 2) * width + (x * 2)) * 3
            checksum += data[idx] + data[idx + 1] + data[idx + 2]
    emit(checksum)
