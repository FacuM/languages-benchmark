from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class AppConfig:
    engine: str
    iterations: int
    warmups: int
    cpu_limit: str
    memory_limit: str
    network_disabled: bool
    target_wall_seconds: float
    max_repeat_factor: int
    sizes: list[str]
    languages: list[str]
    default_tasks: str | list[str]
    smoke_tasks: list[str]
    results_dir: str
    architectures: list[str] = field(default_factory=lambda: ["host"])
    ui_driver_image: str = "languages-benchmark:ui-driver"
    baseline_runtime: str = "python-3.12"
    presets: dict[str, dict[str, Any]] = field(default_factory=dict)
    language_variants: dict[str, dict[str, Any]] = field(default_factory=dict)


@dataclass(slots=True)
class TaskSpec:
    id: str
    name: str
    kind: str
    executable: bool
    smoke: bool
    sizes: list[str]
    tags: list[str] = field(default_factory=list)
    contract: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ResultRow:
    run_id: str
    task_id: str
    language: str
    runtime_id: str
    architecture: str
    size: str
    iteration: int
    repeat_count: int
    status: str
    cpu_seconds: float | None
    wall_seconds: float | None
    max_rss_mb: float | None
    loc: int | None
    community_score: float | None
    ease_score: float | None
    debugging_score: float | None
    docs_score: float | None
    libraries_score: float | None
    concurrency_score: float | None
    scalability_score: float | None
    overall_score: float | None
    stdout: str = ""
    stderr: str = ""
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ScoredLanguage:
    language: str
    cpu_score: float
    wall_score: float
    memory_score: float
    loc_score: float
    ease_score: float
    community_score: float
    scalability_score: float
    debugging_score: float
    docs_score: float
    libraries_score: float
    concurrency_score: float
    overall_score: float
    tasks_covered: int
    skipped_tasks: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
