import csv
from pathlib import Path

def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "csv" / f"{size}.csv"
    total = 0
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            total += int(row["value_a"]) + int(row["value_b"])
    print(total)
