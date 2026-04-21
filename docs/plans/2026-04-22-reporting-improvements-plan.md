# Benchmark Reporting Improvements Plan — 2026-04-22

## Summary
Implement a concrete subset of the previously suggested improvements:

1. Capture and publish host/environment metadata with each run
2. Add benchmark presets for publishable runs
3. Compute and surface iteration variance summaries
4. Add per-task raw numeric tables to the report and README
5. Capture and publish the tested runtime version for each language variant
6. Add version-aware plots plus language best-case plots

## Live TODO
- [x] Add host metadata capture to benchmark artifacts and surface it in report/README
- [x] Add `--preset` support for `run`/`all` with at least `dev` and `release`
- [x] Extend scored medians with variance/range fields for CPU, wall, and memory
- [x] Add per-task raw numeric tables to HTML report
- [x] Add per-task raw numeric tables to README snapshot
- [x] Capture and publish tested runtime versions for every configured language variant
- [x] Add version-aware plots for all tested runtime variants
- [x] Add language best-case plots that collapse each family to its best tested version per metric
- [x] Update tests for new payload/report/README behavior
- [x] Regenerate the report/README from the latest scored run

## Notes
- Published snapshot regenerated from `results/20260422T125222Z/scored_results.json`.
- This publish run uses the real compute subset (`sort_integers`, `matrix_multiplication`, `csv_parsing`, `prime_sieve`) across all configured runtime variants.
- Legacy runtimes now use per-variant task support where needed:
  - `Python 2.7` runs the validated compute subset via `tasks/implementations/python2`
  - `PHP 5.6` runs the validated compute subset via `tasks/implementations/php56`
  - `PHP 7.2` is included in the version matrix and currently limited to the validated compute subset for clean publish runs
- A full mixed smoke run previously exposed a version-specific UI startup problem for `gui_calculator`; that remains separate from the reporting/versioning work completed here.

## Follow-up TODO
- [x] Add `PHP 7.2` as an additional tested runtime variant
- [x] Add `Python 2.7` as an additional tested runtime variant
- [x] Add a Python 2.7-compatible implementation for the validated compute subset
- [x] Allow per-variant supported-task subsets so legacy runtimes can be skipped cleanly on unsupported tasks
- [x] Rebuild versioned images and regenerate the published version-aware snapshot
