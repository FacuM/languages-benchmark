from pathlib import Path

def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "sort" / f"{size}.txt"
    values = [int(x) for x in path.read_text(encoding="utf-8").split()]
    values.sort()
    print(sum(values[:100]))
