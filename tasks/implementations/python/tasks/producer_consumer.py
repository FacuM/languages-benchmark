from pathlib import Path

MOD = 4_294_967_291
CAPACITY = 64


def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "producer_consumer" / f"{size}.txt"
    values = [int(x) for x in path.read_text(encoding="utf-8").split()]
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
    print(checksum)
