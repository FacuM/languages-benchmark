from pathlib import Path

KEYWORD = "needle"

def run(size: str, fixtures_root: str) -> None:
    root = Path(fixtures_root) / "generated" / "search" / size
    total = 0
    for path in root.rglob("*.txt"):
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if KEYWORD in line:
                    total += 1
    print(total)
