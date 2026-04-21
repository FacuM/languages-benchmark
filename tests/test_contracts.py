from pathlib import Path
from runner.config import ROOT, load_catalog

LANGS = ["php", "python", "java", "cpp", "node", "go", "rust"]
EXT = {"php": ".php", "python": ".py", "java": ".java", "cpp": ".cpp", "node": ".js", "go": ".go", "rust": ".rs"}


def test_executable_tasks_have_all_language_files():
    catalog = load_catalog()
    executable = [task for task in catalog if task.executable]
    for task in executable:
        for language in LANGS:
            path = ROOT / "tasks" / "implementations" / language / "tasks" / f"{task.id}{EXT[language]}"
            assert path.exists(), f"missing {path}"
