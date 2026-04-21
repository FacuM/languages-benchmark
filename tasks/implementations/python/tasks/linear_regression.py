import csv
from pathlib import Path

def run(size: str, fixtures_root: str) -> None:
    path = Path(fixtures_root) / "generated" / "linear_regression" / f"{size}.csv"
    n = 0.0
    sum_x = sum_y = sum_xy = sum_x2 = 0.0
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            x = float(row["x"])
            y = float(row["y"])
            n += 1.0
            sum_x += x
            sum_y += y
            sum_xy += x * y
            sum_x2 += x * x
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    intercept = (sum_y - slope * sum_x) / n
    checksum = round(slope * 1_000_000) + round(intercept * 1_000_000)
    print(checksum)
