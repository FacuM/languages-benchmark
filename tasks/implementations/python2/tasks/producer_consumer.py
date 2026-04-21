from tasks.compat import emit, join_path, read_text

MOD = 4294967291
CAPACITY = 64


def run(size, fixtures_root):
    path = join_path(fixtures_root, 'generated', 'producer_consumer', '%s.txt' % size)
    values = [int(x) for x in read_text(path).split()]
    buffer = [0] * CAPACITY
    head = tail = count = produced = consumed = 0
    checksum = 0
    total = len(values)
    while produced < total or count > 0:
        while produced < total and count < CAPACITY:
            buffer[tail] = values[produced]
            tail = (tail + 1) % CAPACITY
            produced += 1
            count += 1
        if count > 0:
            value = buffer[head]
            head = (head + 1) % CAPACITY
            count -= 1
            checksum = (checksum + value * (consumed + 1)) % MOD
            consumed += 1
    emit(checksum)
