from tasks.compat import emit, join_path, read_lines

MOD = 4294967291
MULT = 16777619


def run(size, fixtures_root):
    path = join_path(fixtures_root, 'generated', 'blockchain', '%s.txt' % size)
    prev_hash = 2166136261
    total = 0
    for index, line in enumerate(read_lines(path)):
        if not line.strip():
            continue
        hash_value = prev_hash
        for token in line.split():
            hash_value = (hash_value * MULT + int(token) + index + 1) % MOD
        total = (total + hash_value) % MOD
        prev_hash = hash_value
    emit(total)
