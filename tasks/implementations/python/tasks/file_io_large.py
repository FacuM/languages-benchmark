from pathlib import Path

def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "file_io" / f"{size}.txt"
    total = 0
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            total += int(line.strip())
    print(total)
