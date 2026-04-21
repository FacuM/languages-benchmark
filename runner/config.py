from __future__ import annotations

from pathlib import Path
import yaml

from runner.models import AppConfig, TaskSpec

ROOT = Path(__file__).resolve().parent.parent


def _load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def load_app_config(root: Path = ROOT) -> AppConfig:
    data = _load_yaml(root / "benchmark.yaml")
    return AppConfig(**data)


def load_catalog(root: Path = ROOT) -> list[TaskSpec]:
    data = _load_yaml(root / "tasks" / "catalog.yaml")
    tasks = []
    for row in data.get("tasks", []):
        tasks.append(TaskSpec(**row))
    return tasks


def load_weights(root: Path = ROOT, path: Path | None = None) -> dict[str, float]:
    data = _load_yaml(path or (root / "weights.default.yaml"))
    return {k: float(v) for k, v in data["weights"].items()}


def load_rubrics(root: Path = ROOT) -> dict:
    return _load_yaml(root / "rubrics.yaml")["ratings"]


def load_runtime_rubrics(root: Path = ROOT) -> dict:
    path = root / "runtime_rubrics.yaml"
    if not path.exists():
        return {}
    return _load_yaml(path).get("ratings", {})


def load_community(root: Path = ROOT) -> dict:
    return _load_yaml(root / "community.yaml")["community"]
