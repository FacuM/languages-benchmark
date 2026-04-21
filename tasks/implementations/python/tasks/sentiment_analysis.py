from pathlib import Path

POSITIVE = {"good", "great", "happy", "clean", "fast", "love"}
NEGATIVE = {"bad", "sad", "dirty", "slow", "hate", "poor"}

def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "sentiment" / f"{size}.txt"
    total = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        for token in line.split():
            if token in POSITIVE:
                total += 1
            elif token in NEGATIVE:
                total -= 1
    print(total)
