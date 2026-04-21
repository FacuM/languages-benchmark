# 2026-04-22 Benchmark quality improvements plan

## Goal
Raise the benchmark from “works and documents results” to “more rigorous, auditable, and publication-friendly”.

## Live TODO
- [x] Add statistical confidence reporting (variance tables, summary, and variance plots)
- [x] Add stronger benchmark presets for publishable runs
- [x] Publish exact fixture sizes per task in README/report
- [x] Separate service/UI startup cost from steady-state workload cost
- [x] Make per-version methodology more explicit
- [x] Generate a machine-readable publish manifest
- [x] Add correctness verification summary to README/report
- [x] Add regression tracking against the previous canonical publish artifact
- [x] Add geometric-mean runtime views
- [x] Add optional parallel runner mode via `--jobs N`
- [x] Add a “What this benchmark is not” section
- [x] Add visible metric provenance labels: measured / derived / rubric
- [x] Add README links from each task to its actual implementations
- [x] Update tests and regenerate README/report artifacts

## Completion notes
- Added `publish` and `full-release` presets in `benchmark.yaml`, while keeping sequential publication defaults.
- Added fixture-manifest capture, git metadata capture, and startup/workload split timing to raw/scored artifacts.
- Added opt-in parallel case execution via `./bench run --jobs N` while preserving deterministic output ordering.
- Added geometric-mean runtime plots, variance plots, provenance tables, fixture-size tables, correctness summaries, regression tables, and “what this benchmark is not” sections to the README/report.
- Added machine-readable publication metadata at `docs/publish-manifest.json`.
- Added README task-level implementation links and regenerated the canonical README/report artifacts.
- Validation: `.venv/bin/pytest tests` → `10 passed`.

## Implementation notes
1. Confidence reporting should use existing min/max/stddev data from medians and add a lightweight plot plus README/report summaries.
2. Publish presets should remain conservative defaults; canonical runs remain sequential unless `--jobs` is explicitly set.
3. Fixture-size reporting should describe the real contract for each task and each `S/M/L` tier.
4. Service/UI split timing should record startup wait separately from workload execution while keeping current total metrics available.
5. Per-version methodology must clearly state which fields are runtime-specific versus family-shared rubric/community inputs.
6. The publish manifest should capture canonical artifact paths, supplemental version-matrix artifact paths, commit identity when available, and source provenance.
7. Regression tracking should compare against the previous canonical publish artifact if available.
8. Geometric means should focus on runtime-style objective metrics where that aggregation is meaningful.
9. `--jobs` should be opt-in and should preserve deterministic result writing.
10. Provenance labels and task implementation links should appear in both README/report methodology/task sections where practical.
