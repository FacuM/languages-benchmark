from pathlib import Path

def run(size: str, fixtures_root: str) -> None:
    tokens = Path(fixtures_root, "generated", "matrix", f"{size}.txt").read_text(encoding="utf-8").split()
    n = int(tokens[0])
    nums = list(map(int, tokens[1:]))
    split = n*n
    a = nums[:split]
    b = nums[split:]
    total = 0
    for i in range(n):
        for j in range(n):
            cell = 0
            for k in range(n):
                cell += a[i*n+k] * b[k*n+j]
            total += cell
    print(total)
