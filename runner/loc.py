from __future__ import annotations

from pathlib import Path

COMMENT_PREFIXES = {
    ".py": ["#"],
    ".js": ["//"],
    ".php": ["//", "#"],
    ".java": ["//"],
    ".go": ["//"],
    ".rs": ["//"],
    ".cpp": ["//"],
    ".hpp": ["//"],
}

EXT_MAP = {
    "python": ".py",
    "python2": ".py",
    "node": ".js",
    "php": ".php",
    "php56": ".php",
    "java": ".java",
    "go": ".go",
    "rust": ".rs",
    "cpp": ".cpp",
}


def count_loc(root: Path, language: str, task_id: str) -> int:
    ext = EXT_MAP[language]
    file_path = root / "tasks" / "implementations" / language / "tasks" / f"{task_id}{ext}"
    if not file_path.exists():
        return 0
    count = 0
    prefixes = COMMENT_PREFIXES.get(ext, ["//", "#"])
    for raw in file_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if any(line.startswith(prefix) for prefix in prefixes):
            continue
        count += 1
    return count
