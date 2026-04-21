from pathlib import Path
import re


def run(size: str, fixtures_root: str) -> None:
    text = (Path(fixtures_root) / "mocks" / f"ai_service_{size}.json").read_text(encoding="utf-8")
    model = re.search(r'"model":\s*"([^"]+)"', text).group(1)
    total = len(model)
    for prompt, output, tokens in re.findall(r'"prompt":\s*"([^"]+)",\s*"output":\s*"([^"]+)",\s*"tokens":\s*(\d+)', text):
        total += len(prompt) + len(output) + int(tokens)
    print(total)
