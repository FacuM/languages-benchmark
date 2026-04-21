from pathlib import Path

def run(size: str, fixtures_root: str) -> None:
    tokens = Path(fixtures_root, "generated", "image", f"{size}.ppm").read_text(encoding="utf-8").split()
    width = int(tokens[1])
    height = int(tokens[2])
    data = list(map(int, tokens[4:]))
    checksum = 0
    for y in range(height // 2):
        for x in range(width // 2):
            idx = ((y * 2) * width + (x * 2)) * 3
            checksum += data[idx] + data[idx + 1] + data[idx + 2]
    print(checksum)
