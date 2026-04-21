# 2026-04-22 Second benchmark quality improvements plan

## Goal
Push the benchmark from “auditable and well documented” to “easier to compare over time, easier to interpret for service workloads, and clearer about runtime-vs-family behavior”.

## Live TODO
- [x] Add confidence-interval reporting and error bars for measured raw-unit metrics
- [x] Add startup-vs-steady-state plots for service/UI workloads
- [x] Expand fixture publication into a clearer task-contract appendix
- [x] Add baseline-relative comparison views using a configured baseline runtime
- [x] Add historical publish-trend reporting from archived publish manifests
- [x] Add per-task correctness digests/fingerprints
- [x] Split rubric handling so runtime variants can override family-level rubric scores
- [x] Make the HTML report interactive (sortable tables and lightweight filtering)
- [x] Record and display publish-profile metadata (preset, iterations, warmups, jobs)
- [x] Document the parallel-run caveat clearly for canonical published runs
- [x] Update tests and regenerate README/report artifacts

## Implementation notes
1. Confidence intervals should use the repeated measured samples already captured per task/size and be labeled clearly as approximate 95% CIs around the measured medians/aggregates.
2. Startup-vs-workload views should focus on service/UI task medians and stay in raw units rather than normalized scores.
3. Baseline-relative comparisons should default to a configurable runtime (initially Python 3.12) but remain data-driven from the scored artifact.
4. Historical trend reporting should archive publish manifests into `docs/publish-history/` and derive trend lines from canonical published snapshots.
5. Correctness digests should summarize deterministic output fingerprints per task/size so readers can audit expected outputs without reading raw JSON.
6. Runtime-level rubric overrides should be optional: variants may override family defaults while untouched variants continue inheriting family-level values.
7. Interactive HTML should remain dependency-free: small inline JavaScript is enough for sorting and filtering.
8. Canonical published runs remain sequential by default even though `--jobs` is available.

## Completion notes
- Added approximate 95% CI fields to scored medians and aggregate raw-unit summaries, then rendered them as error bars on raw-unit plots.
- Added startup/workload timing plots and CI-aware tables for service/UI workloads.
- Added baseline-relative comparison plots/tables using `benchmark.yaml`'s configured `baseline_runtime` (default `python-3.12`).
- Added archived publish-history snapshots under `docs/publish-history/` plus a historical trend plot/table.
- Added correctness digest tables for task/size output fingerprints.
- Added optional runtime-specific rubric overrides via `runtime_rubrics.yaml`; family defaults still apply when no variant override exists.
- Added publish-profile metadata to artifacts plus README/report sections, and documented the sequential-publication caveat for `--jobs`.
- Added lightweight HTML interactivity (sortable tables and leaderboard filtering).
- Validation: `.venv/bin/pytest tests` → `10 passed`.
