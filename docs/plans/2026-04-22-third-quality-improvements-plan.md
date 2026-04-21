# 2026-04-22 Third benchmark quality improvements plan

## Goal
Make the benchmark easier to trust, slice, and publish repeatedly by adding expected-output verification, richer category views, stronger publication workflows, and clearer provenance/trend reporting.

## Live TODO
- [x] Add true publish reruns and aggregate rerun stability reporting
- [x] Add per-task baseline comparison views
- [x] Add a checked-in expected-output manifest and compare current results against it
- [x] Add task tags and category-level leaderboards/filters
- [x] Promote cold-start vs hot-path service timing into first-class benchmark views
- [x] Add version-history trend charts per language/runtime
- [x] Add more explicit artifact/source provenance in README/report
- [x] Add a single publish-bundle command/export flow
- [x] Add task difficulty / workload-relevance notes
- [x] Add optional native-host run support as an experimental mode
- [x] Update tests and regenerate README/report artifacts

## Completed
1. Added `docs/expected-outputs.json` and surfaced current-vs-expected checks in the report and README.
2. Tagged every task in `tasks/catalog.yaml`, then used those tags to build category leaderboards from the same scored rows.
3. Added per-task baseline delta plots, startup-vs-steady-state charts, version-history trend plots, and provenance sections.
4. Added `publish-bundle` with rerun stability summaries and a bundled manifest/export flow.
5. Added task relevance notes, experimental native-host execution scaffolding, and supporting regression tests.

## Implementation notes
1. Publish reruns should re-run the chosen preset multiple times and emit a small bundle artifact that includes rerun summaries.
2. Expected-output verification should prefer a checked-in manifest of deterministic output digests per task/size and report current-vs-expected status.
3. Task tags should be lightweight and checked into task metadata so category leaderboards can be recomputed without hardcoding in the report layer.
4. Cold-start vs hot-path reporting should build on the existing startup/workload split and elevate both into visible category comparisons.
5. Version-history plots should show runtime-specific trend lines when archived publish-history snapshots exist.
6. Provenance sections should explicitly identify which artifact and source notes powered each published view.
7. Native-host mode should be clearly marked experimental and only run when a variant declares a local command template; unsupported variants should skip cleanly.
