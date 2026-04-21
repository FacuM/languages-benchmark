from pathlib import Path
import re


def run(size: str, fixtures_root: str) -> None:
    text = (Path(fixtures_root) / "mocks" / f"twitter_like_{size}.json").read_text(encoding="utf-8")
    total = 0
    for post_id, body, likes in re.findall(r'"id":\s*"([^"]+)",\s*"text":\s*"([^"]+)",\s*"likes":\s*(\d+)', text):
        total += len(post_id) + len(body) + int(likes)
    print(total)
