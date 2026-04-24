from runner.reporting import generate_report
from runner.utils import write_json



def test_generate_report_writes_canonical_and_ranked_plot_variants(tmp_path):
    results_path = tmp_path / "scored_results.json"
    write_json(results_path, {
        "run_id": "run-1",
        "host": {"hostname": "bench-host", "cpu_model": "Test CPU"},
        "runtimes": [
            {"language": "php-8.4@x86_64", "runtime_id": "php-8.4", "architecture": "x86_64", "language_label": "PHP 8.4 [x86_64]", "language_family": "php", "configured_version": "8.4", "reported_version": "PHP 8.4.0", "image": "languages-benchmark:php-8.4"},
            {"language": "rust-1.82@x86_64", "runtime_id": "rust-1.82", "architecture": "x86_64", "language_label": "Rust 1.82 [x86_64]", "language_family": "rust", "configured_version": "1.82", "reported_version": "Rust 1.82", "image": "languages-benchmark:rust-1.82"},
        ],
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
        "aggregate": [
            {
                "language": "rust-1.82@x86_64",
                "runtime_id": "rust-1.82",
                "architecture": "x86_64",
                "language_label": "Rust 1.82 [x86_64]",
                "language_family": "rust",
                "overall_score": 95.0,
                "cpu_score": 93.0,
                "wall_score": 94.0,
                "memory_score": 91.0,
                "scalability_score": 92.0,
                "tasks_covered": 4,
                "skipped_tasks": 0,
            },
            {
                "language": "php-8.4@x86_64",
                "runtime_id": "php-8.4",
                "architecture": "x86_64",
                "language_label": "PHP 8.4 [x86_64]",
                "language_family": "php",
                "overall_score": 40.0,
                "cpu_score": 35.0,
                "wall_score": 36.0,
                "memory_score": 45.0,
                "scalability_score": 41.0,
                "tasks_covered": 4,
                "skipped_tasks": 0,
            },
        ],
        "medians": [
            {"language": "php-8.4@x86_64", "runtime_id": "php-8.4", "architecture": "x86_64", "language_label": "PHP 8.4 [x86_64]", "language_family": "php", "task_id": "sort_integers", "size": "s", "cpu_seconds": 2.0, "wall_seconds": 2.1, "max_rss_mb": 30.0, "loc": 20, "ease_score": 7, "community_score": 70, "debugging_score": 7, "docs_score": 7, "libraries_score": 7, "concurrency_score": 6, "scalability_score": 40.0},
            {"language": "php-8.4@x86_64", "runtime_id": "php-8.4", "architecture": "x86_64", "language_label": "PHP 8.4 [x86_64]", "language_family": "php", "task_id": "sort_integers", "size": "m", "cpu_seconds": 3.0, "wall_seconds": 3.2, "max_rss_mb": 32.0, "loc": 20, "ease_score": 7, "community_score": 70, "debugging_score": 7, "docs_score": 7, "libraries_score": 7, "concurrency_score": 6, "scalability_score": 38.0},
            {"language": "php-8.4@x86_64", "runtime_id": "php-8.4", "architecture": "x86_64", "language_label": "PHP 8.4 [x86_64]", "language_family": "php", "task_id": "sort_integers", "size": "l", "cpu_seconds": 4.0, "wall_seconds": 4.4, "max_rss_mb": 35.0, "loc": 20, "ease_score": 7, "community_score": 70, "debugging_score": 7, "docs_score": 7, "libraries_score": 7, "concurrency_score": 6, "scalability_score": 35.0},
            {"language": "rust-1.82@x86_64", "runtime_id": "rust-1.82", "architecture": "x86_64", "language_label": "Rust 1.82 [x86_64]", "language_family": "rust", "task_id": "sort_integers", "size": "s", "cpu_seconds": 1.0, "wall_seconds": 1.1, "max_rss_mb": 20.0, "loc": 16, "ease_score": 8, "community_score": 80, "debugging_score": 8, "docs_score": 8, "libraries_score": 8, "concurrency_score": 7, "scalability_score": 95.0},
            {"language": "rust-1.82@x86_64", "runtime_id": "rust-1.82", "architecture": "x86_64", "language_label": "Rust 1.82 [x86_64]", "language_family": "rust", "task_id": "sort_integers", "size": "m", "cpu_seconds": 1.4, "wall_seconds": 1.5, "max_rss_mb": 21.0, "loc": 16, "ease_score": 8, "community_score": 80, "debugging_score": 8, "docs_score": 8, "libraries_score": 8, "concurrency_score": 7, "scalability_score": 93.0},
            {"language": "rust-1.82@x86_64", "runtime_id": "rust-1.82", "architecture": "x86_64", "language_label": "Rust 1.82 [x86_64]", "language_family": "rust", "task_id": "sort_integers", "size": "l", "cpu_seconds": 1.9, "wall_seconds": 2.0, "max_rss_mb": 22.0, "loc": 16, "ease_score": 8, "community_score": 80, "debugging_score": 8, "docs_score": 8, "libraries_score": 8, "concurrency_score": 7, "scalability_score": 90.0},
        ],
        "rows": [
            {"language": "php-8.4@x86_64", "runtime_id": "php-8.4", "architecture": "x86_64", "language_label": "PHP 8.4 [x86_64]", "language_family": "php", "task_id": "sort_integers", "size": "s", "status": "ok", "cpu_seconds": 2.0, "wall_seconds": 2.1, "max_rss_mb": 30.0, "loc": 20, "ease_score": 7, "community_score": 70, "debugging_score": 7, "docs_score": 7, "libraries_score": 7, "concurrency_score": 6, "stdout": "1"},
            {"language": "php-8.4@x86_64", "runtime_id": "php-8.4", "architecture": "x86_64", "language_label": "PHP 8.4 [x86_64]", "language_family": "php", "task_id": "sort_integers", "size": "m", "status": "ok", "cpu_seconds": 3.0, "wall_seconds": 3.2, "max_rss_mb": 32.0, "loc": 20, "ease_score": 7, "community_score": 70, "debugging_score": 7, "docs_score": 7, "libraries_score": 7, "concurrency_score": 6, "stdout": "2"},
            {"language": "php-8.4@x86_64", "runtime_id": "php-8.4", "architecture": "x86_64", "language_label": "PHP 8.4 [x86_64]", "language_family": "php", "task_id": "sort_integers", "size": "l", "status": "ok", "cpu_seconds": 4.0, "wall_seconds": 4.4, "max_rss_mb": 35.0, "loc": 20, "ease_score": 7, "community_score": 70, "debugging_score": 7, "docs_score": 7, "libraries_score": 7, "concurrency_score": 6, "stdout": "3"},
            {"language": "rust-1.82@x86_64", "runtime_id": "rust-1.82", "architecture": "x86_64", "language_label": "Rust 1.82 [x86_64]", "language_family": "rust", "task_id": "sort_integers", "size": "s", "status": "ok", "cpu_seconds": 1.0, "wall_seconds": 1.1, "max_rss_mb": 20.0, "loc": 16, "ease_score": 8, "community_score": 80, "debugging_score": 8, "docs_score": 8, "libraries_score": 8, "concurrency_score": 7, "stdout": "4"},
            {"language": "rust-1.82@x86_64", "runtime_id": "rust-1.82", "architecture": "x86_64", "language_label": "Rust 1.82 [x86_64]", "language_family": "rust", "task_id": "sort_integers", "size": "m", "status": "ok", "cpu_seconds": 1.4, "wall_seconds": 1.5, "max_rss_mb": 21.0, "loc": 16, "ease_score": 8, "community_score": 80, "debugging_score": 8, "docs_score": 8, "libraries_score": 8, "concurrency_score": 7, "stdout": "5"},
            {"language": "rust-1.82@x86_64", "runtime_id": "rust-1.82", "architecture": "x86_64", "language_label": "Rust 1.82 [x86_64]", "language_family": "rust", "task_id": "sort_integers", "size": "l", "status": "ok", "cpu_seconds": 1.9, "wall_seconds": 2.0, "max_rss_mb": 22.0, "loc": 16, "ease_score": 8, "community_score": 80, "debugging_score": 8, "docs_score": 8, "libraries_score": 8, "concurrency_score": 7, "stdout": "6"},
        ],
    })
    report_dir = tmp_path / "report"
    report_path = generate_report(results_path, report_dir)
    assert report_path.exists()
    canonical = (report_dir / "overall.svg").read_text(encoding="utf-8")
    ranked = (report_dir / "overall_ranked.svg").read_text(encoding="utf-8")
    html = report_path.read_text(encoding="utf-8")
    assert canonical.index("PHP 8.4 [x86_64]") < canonical.index("Rust 1.82 [x86_64]")
    assert ranked.index("Rust 1.82 [x86_64]") < ranked.index("PHP 8.4 [x86_64]")
    assert "fill='#ffffff'" in canonical
    assert (report_dir / "cpu_units.svg").exists()
    assert (report_dir / "cpu_units_ranked.svg").exists()
    assert (report_dir / "best_case_cpu_units_ranked.svg").exists()
    assert (report_dir / "objective.svg").exists()
    assert (report_dir / "objective_ranked.svg").exists()
    assert (report_dir / "arch_x86_64_overall_ranked.svg").exists()
    assert (report_dir / "arch_x86_64_cpu_units_ranked.svg").exists()
    assert (report_dir / "arch_x86_64_scalability_growth_ratios_ranked.svg").exists()
    assert (report_dir / "best_case_objective_ranked.svg").exists()
    assert (report_dir / "cpu_geomean.svg").exists()
    assert (report_dir / "cpu_geomean_ranked.svg").exists()
    assert (report_dir / "variance_cpu.svg").exists()
    assert (report_dir / "variance_cpu_ranked.svg").exists()
    assert (report_dir / "startup_units_ranked.svg").exists()
    assert (report_dir / "workload_units_ranked.svg").exists()
    assert (report_dir / "baseline_cpu_ratio_ranked.svg").exists()
    assert (report_dir / "history_overall.svg").exists()
    assert (report_dir / "opinionated.svg").exists()
    assert (report_dir / "opinionated_ranked.svg").exists()
    assert (report_dir / "loc.svg").exists()
    assert (report_dir / "loc_ranked.svg").exists()
    assert (report_dir / "task_sort_integers.svg").exists()
    assert (report_dir / "task_sort_integers_ranked.svg").exists()
    assert (report_dir / "best_case_task_sort_integers.svg").exists()
    assert (report_dir / "best_case_task_sort_integers_ranked.svg").exists()
    assert (report_dir / "scalability_curve.svg").exists()
    assert (report_dir / "scalability_curve_ranked.svg").exists()
    assert (report_dir / "scalability_memory_curve.svg").exists()
    assert (report_dir / "scalability_memory_curve_ranked.svg").exists()
    assert (report_dir / "scalability_growth_ratios.svg").exists()
    assert (report_dir / "scalability_growth_ratios_ranked.svg").exists()
    assert "Per-task score plots" in html
    assert "Size legend" in html
    assert "<strong>S</strong> = small input" in html
    assert "Methodology for non-objective and derived criteria" in html
    assert "Regression vs previous published snapshot" in html
    assert "Publish profile" in html
    assert "Correctness digests" in html
    assert "Baseline-relative comparison" in html
    assert "Historical publish trends" in html
    assert "Machine-readable publish manifest" in html
    assert "Geometric-mean runtime views" in html
    assert "Variance / confidence summary" in html
    assert "<h2>Category leaderboards</h2>" in html
    assert "<th>Runtime</th><th>Overall</th><th>Objective</th><th>Opinionated</th><th>Tasks</th>" in html
    assert "<th>Runtime</th><th>Objective</th><th>CPU</th><th>Wall</th><th>Memory</th><th>LOC</th><th>Tasks</th>" in html
    assert "<th>Runtime</th><th>Opinionated</th><th>Scalability</th><th>Ease</th><th>Community</th><th>Debugging</th><th>Docs</th><th>Libraries</th><th>Concurrency</th><th>Tasks</th>" in html
    assert "scalability_score = 100 * best_raw_scalability / candidate_raw_scalability" in html
    assert "Raw-unit plots for this published snapshot" in html
    assert "Tested runtime versions" in html
    assert "Language best-case raw-unit plots" in html
    assert "Objective / unopinionated score plots" in html
    assert "Opinionated score plots" in html
    assert "Scalability growth curves" in html
    assert html.index("Raw-unit plots for this published snapshot") < html.index("Ranked plots")
    assert html.index("Ranked plots") < html.index("Canonical-order plots")
