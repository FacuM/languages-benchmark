from tasks.compat import emit, join_path, read_text


def run(size, fixtures_root):
    tokens = read_text(join_path(fixtures_root, 'generated', 'matrix', '%s.txt' % size)).split()
    n = int(tokens[0])
    nums = map(int, tokens[1:])
    split = n * n
    a = nums[:split]
    b = nums[split:]
    total = 0
    for i in xrange(n):
        for j in xrange(n):
            cell = 0
            for k in xrange(n):
                cell += a[i * n + k] * b[k * n + j]
            total += cell
    emit(total)
