from pathlib import Path

MOD = 4_294_967_291
MULT = 16_777_619

def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "blockchain" / f"{size}.txt"
    prev_hash = 2_166_136_261
    total = 0
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if not line.strip():
            continue
        hash_value = prev_hash
        for token in line.split():
            hash_value = (hash_value * MULT + int(token) + index + 1) % MOD
        total = (total + hash_value) % MOD
        prev_hash = hash_value
    print(total)
