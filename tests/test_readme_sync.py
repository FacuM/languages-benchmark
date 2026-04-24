import json

from runner.readme_sync import _architecture_publish_payload, sync_readme
from runner.utils import write_json


def _architecture_payload(run_id: str, runtime: str, architecture: str, cpu_seconds: float) -> dict:
    language = f"{runtime}@{architecture}"
    return {
        "run_id": run_id,
        "host": {"hostname": f"{architecture}-host", "architecture": architecture},
        "profile": {"architectures": [architecture]},
        "runtimes": [{
            "language": language,
            "runtime_id": runtime,
            "architecture": architecture,
            "language_label": f"{runtime} [{architecture}]",
            "language_family": runtime.split("-", 1)[0],
        }],
        "rows": [{
            "task_id": "sort_integers",
            "language": language,
            "runtime_id": runtime,
            "architecture": architecture,
            "language_label": f"{runtime} [{architecture}]",
            "language_family": runtime.split("-", 1)[0],
            "size": "s",
            "status": "ok",
            "cpu_seconds": cpu_seconds,
            "wall_seconds": cpu_seconds + 0.1,
            "max_rss_mb": 10.0,
            "loc": 10,
            "ease_score": 9,
            "community_score": 9,
            "debugging_score": 9,
            "docs_score": 9,
            "libraries_score": 9,
            "concurrency_score": 9,
            "stdout": "ok",
        }],
        "weights": {
            "cpu": 0.14,
            "wall": 0.14,
            "memory": 0.10,
            "loc": 0.06,
            "ease": 0.08,
            "community": 0.08,
            "scalability": 0.12,
            "debugging": 0.06,
            "docs": 0.06,
            "libraries": 0.06,
            "concurrency": 0.10,
        },
    }


def test_architecture_publish_payload_merges_missing_architectures_and_replaces_current(tmp_path):
    docs_dir = tmp_path / "docs"
    x86_path = tmp_path / "results" / "x86" / "scored_results.json"
    arm_path = tmp_path / "results" / "arm" / "scored_results.json"
    x86_path.parent.mkdir(parents=True)
    arm_path.parent.mkdir(parents=True)
    x86_payload = _architecture_payload("x86-run", "python-3.12", "x86_64", 0.2)
    arm_payload = _architecture_payload("arm-run", "python-3.12", "aarch64", 0.1)
    write_json(x86_path, x86_payload)
    write_json(arm_path, arm_payload)
    previous_manifest = {
        "generated_run_id": "x86-run",
        "architecture_results": {"x86_64": str(x86_path)},
        "canonical_results": str(x86_path),
    }

    merged, merged_path = _architecture_publish_payload(arm_payload, arm_path, docs_dir, previous_manifest)

    assert merged_path.name == "architecture_merged_scored_results.json"
    assert merged["architecture_results"] == {"aarch64": str(arm_path), "x86_64": str(x86_path)}
    assert {row["architecture"] for row in merged["rows"]} == {"x86_64", "aarch64"}
    assert {row["language"] for row in merged["aggregate"]} == {"python-3.12@x86_64", "python-3.12@aarch64"}
    assert merged["profile"]["architectures"] == ["aarch64", "x86_64"]


def test_sync_readme_embeds_dual_plot_sets_table_explanations_and_code(tmp_path):
    results_dir = tmp_path / "results"
    report_dir = results_dir / "report"
    report_dir.mkdir(parents=True)
    for name in [
        "cpu_units.svg",
        "wall_units.svg",
        "memory_units.svg",
        "loc_units.svg",
        "best_case_cpu_units.svg",
        "best_case_wall_units.svg",
        "best_case_memory_units.svg",
        "best_case_loc_units.svg",
        "cpu_units_ranked.svg",
        "wall_units_ranked.svg",
        "memory_units_ranked.svg",
        "loc_units_ranked.svg",
        "best_case_cpu_units_ranked.svg",
        "best_case_wall_units_ranked.svg",
        "best_case_memory_units_ranked.svg",
        "best_case_loc_units_ranked.svg",
        "objective.svg",
        "objective_ranked.svg",
        "best_case_objective.svg",
        "best_case_objective_ranked.svg",
        "opinionated.svg",
        "opinionated_ranked.svg",
        "best_case_opinionated.svg",
        "best_case_opinionated_ranked.svg",
        "overall.svg",
        "cpu.svg",
        "wall.svg",
        "memory.svg",
        "loc.svg",
        "scalability.svg",
        "best_case_overall.svg",
        "best_case_cpu.svg",
        "best_case_wall.svg",
        "best_case_memory.svg",
        "best_case_loc.svg",
        "best_case_scalability.svg",
        "overall_ranked.svg",
        "cpu_ranked.svg",
        "wall_ranked.svg",
        "memory_ranked.svg",
        "loc_ranked.svg",
        "scalability_ranked.svg",
        "best_case_overall_ranked.svg",
        "best_case_cpu_ranked.svg",
        "best_case_wall_ranked.svg",
        "best_case_memory_ranked.svg",
        "best_case_loc_ranked.svg",
        "best_case_scalability_ranked.svg",
        "scalability_curve.svg",
        "scalability_curve_ranked.svg",
        "scalability_memory_curve.svg",
        "scalability_memory_curve_ranked.svg",
        "scalability_growth_ratios.svg",
        "scalability_growth_ratios_ranked.svg",
        "cpu_geomean.svg",
        "cpu_geomean_ranked.svg",
        "wall_geomean.svg",
        "wall_geomean_ranked.svg",
        "variance_cpu.svg",
        "variance_cpu_ranked.svg",
        "variance_wall.svg",
        "variance_wall_ranked.svg",
        "variance_memory.svg",
        "variance_memory_ranked.svg",
        "startup_units.svg",
        "startup_units_ranked.svg",
        "workload_units.svg",
        "workload_units_ranked.svg",
        "baseline_cpu_ratio.svg",
        "baseline_cpu_ratio_ranked.svg",
        "baseline_wall_ratio.svg",
        "baseline_wall_ratio_ranked.svg",
        "baseline_memory_ratio.svg",
        "baseline_memory_ratio_ranked.svg",
            "baseline_overall_delta.svg",
            "baseline_overall_delta_ranked.svg",
            "history_overall.svg",
            "history_version_matrix_overall.svg",
            "task_sort_integers.svg",
            "task_sort_integers_ranked.svg",
            "task_baseline_sort_integers_ranked.svg",
            "best_case_task_sort_integers.svg",
            "best_case_task_sort_integers_ranked.svg",
            "task_csv_parsing.svg",
            "task_csv_parsing_ranked.svg",
            "task_baseline_csv_parsing_ranked.svg",
            "best_case_task_csv_parsing.svg",
            "best_case_task_csv_parsing_ranked.svg",
        ]:
        (report_dir / name).write_text("<svg></svg>", encoding="utf-8")
    results_path = results_dir / "scored_results.json"
    write_json(results_path, {
        "run_id": "run-1",
        "host": {"hostname": "bench-host"},
        "runtimes": [{"language": "python-3.12", "language_label": "Python 3.12", "language_family": "python", "configured_version": "3.12", "reported_version": "Python 3.12.0", "image": "languages-benchmark:python-3.12"}],
        "medians": [
            {"task_id": "sort_integers", "language": "python-3.12", "language_label": "Python 3.12", "size": "s", "sample_count": 1, "cpu_seconds": 0.1, "cpu_stddev_seconds": 0.0, "cpu_min_seconds": 0.1, "cpu_max_seconds": 0.1, "wall_seconds": 0.2, "wall_stddev_seconds": 0.0, "wall_min_seconds": 0.2, "wall_max_seconds": 0.2, "max_rss_mb": 10.0, "memory_stddev_mb": 0.0, "memory_min_mb": 10.0, "memory_max_mb": 10.0, "loc": 10},
            {"task_id": "csv_parsing", "language": "python-3.12", "language_label": "Python 3.12", "size": "s", "sample_count": 1, "cpu_seconds": 0.1, "cpu_stddev_seconds": 0.0, "cpu_min_seconds": 0.1, "cpu_max_seconds": 0.1, "wall_seconds": 0.2, "wall_stddev_seconds": 0.0, "wall_min_seconds": 0.2, "wall_max_seconds": 0.2, "max_rss_mb": 10.0, "memory_stddev_mb": 0.0, "memory_min_mb": 10.0, "memory_max_mb": 10.0, "loc": 10},
        ],
        "rows": [
            {"task_id": "sort_integers", "language": "python-3.12", "language_label": "Python 3.12", "size": "s", "status": "ok", "cpu_seconds": 0.1, "wall_seconds": 0.2, "max_rss_mb": 10.0, "loc": 10, "ease_score": 92.0, "community_score": 90.0, "debugging_score": 91.0, "docs_score": 93.0, "libraries_score": 94.0, "concurrency_score": 87.0, "stdout": "123"},
            {"task_id": "sort_integers", "language": "python-3.12", "language_label": "Python 3.12", "size": "m", "status": "ok", "cpu_seconds": 0.2, "wall_seconds": 0.3, "max_rss_mb": 11.0, "loc": 10, "ease_score": 92.0, "community_score": 90.0, "debugging_score": 91.0, "docs_score": 93.0, "libraries_score": 94.0, "concurrency_score": 87.0, "stdout": "234"},
            {"task_id": "sort_integers", "language": "python-3.12", "language_label": "Python 3.12", "size": "l", "status": "ok", "cpu_seconds": 0.3, "wall_seconds": 0.4, "max_rss_mb": 12.0, "loc": 10, "ease_score": 92.0, "community_score": 90.0, "debugging_score": 91.0, "docs_score": 93.0, "libraries_score": 94.0, "concurrency_score": 87.0, "stdout": "345"},
            {"task_id": "csv_parsing", "language": "python-3.12", "language_label": "Python 3.12", "size": "s", "status": "ok", "cpu_seconds": 0.1, "wall_seconds": 0.2, "max_rss_mb": 10.0, "loc": 10, "ease_score": 92.0, "community_score": 90.0, "debugging_score": 91.0, "docs_score": 93.0, "libraries_score": 94.0, "concurrency_score": 87.0, "stdout": "456"},
            {"task_id": "csv_parsing", "language": "python-3.12", "language_label": "Python 3.12", "size": "m", "status": "ok", "cpu_seconds": 0.2, "wall_seconds": 0.3, "max_rss_mb": 11.0, "loc": 10, "ease_score": 92.0, "community_score": 90.0, "debugging_score": 91.0, "docs_score": 93.0, "libraries_score": 94.0, "concurrency_score": 87.0, "stdout": "567"},
            {"task_id": "csv_parsing", "language": "python-3.12", "language_label": "Python 3.12", "size": "l", "status": "ok", "cpu_seconds": 0.3, "wall_seconds": 0.4, "max_rss_mb": 12.0, "loc": 10, "ease_score": 92.0, "community_score": 90.0, "debugging_score": 91.0, "docs_score": 93.0, "libraries_score": 94.0, "concurrency_score": 87.0, "stdout": "678"},
        ],
        "aggregate": [{
            "language": "python",
            "language_label": "Python 3.12",
            "overall_score": 90.5,
            "cpu_score": 91.0,
            "wall_score": 89.0,
            "memory_score": 80.0,
            "loc_score": 88.0,
            "ease_score": 92.0,
            "community_score": 90.0,
            "debugging_score": 91.0,
            "docs_score": 93.0,
            "libraries_score": 94.0,
            "concurrency_score": 87.0,
            "scalability_score": 95.0,
            "tasks_covered": 2,
        }],
    })
    readme = tmp_path / "README.md"
    readme.write_text(
        "# Demo\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)\n\n<!-- benchmark:begin -->\nold\n<!-- benchmark:end -->\n",
        encoding="utf-8",
    )
    sync_readme(results_path, readme, tmp_path / "docs")
    content = readme.read_text(encoding="utf-8")
    assert "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)" in content
    assert "Latest benchmark snapshot" in content
    assert "Snapshot summary" in content
    assert "Machine-readable publish manifest" in content
    assert "Publish profile" in content
    assert "Size legend" in content
    assert "`S` = **Small** input" in content
    assert "Methodology for non-objective and derived criteria" in content
    assert "`scalability_score = 100 * best_raw_scalability / candidate_raw_scalability`" in content
    assert "Rubric evidence and sources" in content
    assert "<summary><strong>Python</strong> — reviewed 2026-04-22</summary>" in content
    assert "https://docs.python.org/3/" in content
    assert "https://pypi.org/" in content
    assert "Blended overview for this 2-task published snapshot" in content
    assert "Objective / unopinionated family summary for this 2-task published snapshot" in content
    assert "Opinionated / interpretive family summary for this 2-task published snapshot" in content
    assert "Canonical full-suite" not in content
    assert "| Language family | Primary runtime | Overall | Objective | Opinionated | Tasks |" in content
    assert "| Language family | Primary runtime | Objective | CPU | Wall | Memory | LOC | Tasks |" in content
    assert "| Language family | Primary runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |" in content
    assert "What the current executable tests do" in content
    assert "Code examples from the current implementations" not in content
    assert "- **Implementations:**" in content
    assert "### Category leaderboards" in content
    assert "| Runtime | Overall | Objective | Opinionated | Tasks |" in content
    assert "| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |" in content
    assert "| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |" in content
    assert "canonical-order" in content
    assert "Global raw-unit plots for this 2-task published snapshot" in content
    assert "Runtime versions present in this published snapshot" in content
    assert "Objective / unopinionated score plots" in content
    assert "Opinionated / interpretive score plots" in content
    assert "Blended composite plots sorted best to worst" in content
    assert "docs/plots/cpu_units_ranked.svg" in content
    assert "docs/plots/memory_units.svg" in content
    assert "docs/plots/best_case_cpu_units_ranked.svg" in content
    assert "docs/plots/objective_ranked.svg" in content
    assert "Geometric-mean runtime views" in content
    assert "Variance / confidence summary" in content
    assert "Correctness digests" in content
    assert "Baseline-relative comparisons" in content
    assert "Historical publish trends" in content
    assert "docs/plots/cpu_geomean_ranked.svg" in content
    assert "docs/plots/variance_cpu_ranked.svg" in content
    assert "docs/plots/startup_units_ranked.svg" in content
    assert "docs/plots/baseline_cpu_ratio_ranked.svg" in content
    assert "docs/plots/opinionated_ranked.svg" in content
    assert content.index("Blended composite plots sorted best to worst") < content.index("Blended composite plots in canonical language order")
    assert "docs/plots/overall.svg" in content
    assert "docs/plots/overall_ranked.svg" in content
    assert "docs/plots/scalability_curve_ranked.svg" in content
    assert "docs/plots/scalability_memory_curve.svg" in content
    assert "docs/plots/scalability_growth_ratios_ranked.svg" in content
    assert "Per-task score plots" in content
    assert "Scalability growth charts" in content
    assert "docs/plots/task_sort_integers_ranked.svg" in content
    assert "docs/plots/task_sort_integers.svg" in content
    assert "docs/plots/best_case_task_sort_integers_ranked.svg" in content
    assert "#### `sort_integers`" in content
    assert "**Implementations:**" in content
    assert "| Python | Python 3.12 | 90.50 | 87.45 | 91.68 | 2 |" in content
    assert "| Python | Python 3.12 | 87.45 | 91.00 | 89.00 | 80.00 | 88.00 | 2 |" in content
    assert "| Python | Python 3.12 | 91.68 | 95.00 | 92.00 | 90.00 | 91.00 | 93.00 | 94.00 | 87.00 | 2 |" in content
    assert "What this benchmark is not" in content
    assert "Per-version methodology notes" not in content
    assert "Per-version score tables" not in content
    assert "docs/plots/history_version_matrix_overall.svg" not in content
    assert "Tasks: `csv_parsing`" in content
    assert "decision_tree" not in content


def test_sync_readme_uses_stable_manifest_paths_and_dedupes_history(tmp_path):
    real_results_dir = tmp_path / "results" / "run-1"
    report_dir = real_results_dir / "report"
    report_dir.mkdir(parents=True)
    for name in [
        "cpu_units.svg", "wall_units.svg", "memory_units.svg", "loc_units.svg",
        "best_case_cpu_units.svg", "best_case_wall_units.svg", "best_case_memory_units.svg", "best_case_loc_units.svg",
        "cpu_units_ranked.svg", "wall_units_ranked.svg", "memory_units_ranked.svg", "loc_units_ranked.svg",
        "best_case_cpu_units_ranked.svg", "best_case_wall_units_ranked.svg", "best_case_memory_units_ranked.svg", "best_case_loc_units_ranked.svg",
        "objective.svg", "objective_ranked.svg", "best_case_objective.svg", "best_case_objective_ranked.svg",
        "opinionated.svg", "opinionated_ranked.svg", "best_case_opinionated.svg", "best_case_opinionated_ranked.svg",
        "overall.svg", "cpu.svg", "wall.svg", "memory.svg", "loc.svg", "scalability.svg",
        "best_case_overall.svg", "best_case_cpu.svg", "best_case_wall.svg", "best_case_memory.svg", "best_case_loc.svg", "best_case_scalability.svg",
        "overall_ranked.svg", "cpu_ranked.svg", "wall_ranked.svg", "memory_ranked.svg", "loc_ranked.svg", "scalability_ranked.svg",
        "best_case_overall_ranked.svg", "best_case_cpu_ranked.svg", "best_case_wall_ranked.svg", "best_case_memory_ranked.svg", "best_case_loc_ranked.svg", "best_case_scalability_ranked.svg",
        "scalability_curve.svg", "scalability_curve_ranked.svg", "scalability_memory_curve.svg", "scalability_memory_curve_ranked.svg",
        "scalability_growth_ratios.svg", "scalability_growth_ratios_ranked.svg", "cpu_geomean.svg", "cpu_geomean_ranked.svg",
        "wall_geomean.svg", "wall_geomean_ranked.svg", "variance_cpu.svg", "variance_cpu_ranked.svg", "variance_wall.svg", "variance_wall_ranked.svg",
        "variance_memory.svg", "variance_memory_ranked.svg", "startup_units.svg", "startup_units_ranked.svg", "workload_units.svg", "workload_units_ranked.svg",
        "baseline_cpu_ratio.svg", "baseline_cpu_ratio_ranked.svg", "baseline_wall_ratio.svg", "baseline_wall_ratio_ranked.svg",
        "baseline_memory_ratio.svg", "baseline_memory_ratio_ranked.svg", "baseline_overall_delta.svg", "baseline_overall_delta_ranked.svg",
        "history_overall.svg", "history_version_matrix_overall.svg", "task_sort_integers.svg", "task_sort_integers_ranked.svg",
        "best_case_task_sort_integers.svg", "best_case_task_sort_integers_ranked.svg", "task_baseline_sort_integers_ranked.svg",
    ]:
        (report_dir / name).write_text("<svg></svg>", encoding="utf-8")
    payload = {
        "run_id": "run-1",
        "host": {"hostname": "bench-host"},
        "runtimes": [{"language": "python-3.12", "language_label": "Python 3.12", "language_family": "python", "configured_version": "3.12", "reported_version": "Python 3.12.0", "image": "languages-benchmark:python-3.12"}],
        "medians": [{"task_id": "sort_integers", "language": "python-3.12", "language_label": "Python 3.12", "size": "s", "sample_count": 1, "cpu_seconds": 0.1, "wall_seconds": 0.2, "max_rss_mb": 10.0, "loc": 10}],
        "rows": [{"task_id": "sort_integers", "language": "python-3.12", "language_label": "Python 3.12", "size": "s", "status": "ok", "cpu_seconds": 0.1, "wall_seconds": 0.2, "max_rss_mb": 10.0, "loc": 10, "ease_score": 9, "community_score": 9, "debugging_score": 9, "docs_score": 9, "libraries_score": 9, "concurrency_score": 9, "stdout": "ok"}],
        "aggregate": [{"language": "python", "language_label": "Python 3.12", "overall_score": 90.0, "cpu_score": 90.0, "wall_score": 90.0, "memory_score": 90.0, "loc_score": 90.0, "ease_score": 90.0, "community_score": 90.0, "debugging_score": 90.0, "docs_score": 90.0, "libraries_score": 90.0, "concurrency_score": 90.0, "scalability_score": 90.0, "tasks_covered": 1}],
    }
    real_results_path = real_results_dir / "scored_results.json"
    write_json(real_results_path, payload)
    latest_dir = tmp_path / "results" / "latest"
    latest_dir.parent.mkdir(parents=True, exist_ok=True)
    latest_dir.symlink_to(real_results_dir, target_is_directory=True)
    docs_dir = tmp_path / "docs"
    history_dir = docs_dir / "publish-history"
    history_dir.mkdir(parents=True)
    dup_manifest = {
        "generated_run_id": "older-alias",
        "canonical_results": str(real_results_path),
        "version_matrix_results": None,
    }
    write_json(history_dir / "dup-a.json", dup_manifest)
    write_json(history_dir / "dup-b.json", dup_manifest)
    readme = tmp_path / "README.md"
    readme.write_text("# Demo\n\n<!-- benchmark:begin -->\nold\n<!-- benchmark:end -->\n", encoding="utf-8")
    sync_readme(latest_dir / "scored_results.json", readme, docs_dir)
    manifest = json.loads((docs_dir / "publish-manifest.json").read_text(encoding="utf-8"))
    assert "results/latest/scored_results.json" not in manifest["canonical_results"]
    assert manifest["generated_run_id"] == "run-1"
    content = readme.read_text(encoding="utf-8")
    assert content.count("| `run-1` | Python 3.12 | 90.00 | 1 |") == 1
    assert "older-alias" not in content
