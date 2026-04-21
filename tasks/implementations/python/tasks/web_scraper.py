from pathlib import Path
import re


def _extract(pattern: str, text: str):
    return re.findall(pattern, text, flags=re.IGNORECASE)


def run(size: str, fixtures_root: str) -> None:
    base = Path(fixtures_root) / "mock_site" / size
    index = (base / "index.html").read_text(encoding="utf-8")
    links = _extract(r'href="([^"]+)"', index)
    total = 0
    for idx, link in enumerate(links):
        text = (base / link).read_text(encoding="utf-8")
        title = _extract(r"<h2>(.*?)</h2>", text)[0]
        body = _extract(r"<p>(.*?)</p>", text)[0]
        total += (idx + 1) * (len(title) + len(body))
    print(total)
