from pathlib import Path
import re


def run(size: str, fixtures_root: str) -> None:
    text = (Path(fixtures_root) / "mocks" / f"public_api_{size}.json").read_text(encoding="utf-8")
    total = 0
    for item_id, name, value in re.findall(r'"id":\s*(\d+),\s*"name":\s*"([^"]+)",\s*"value":\s*(\d+)', text):
        total += int(item_id) + int(value) + len(name)
    print(total)
