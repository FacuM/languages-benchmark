from runner.scoring import score_results


def test_score_results_produces_leaderboard():
    rows = []
    for language, cpu, wall, mem, loc in [
        ("python", 1.0, 1.2, 50.0, 30),
        ("go", 0.8, 1.0, 40.0, 35),
    ]:
        for size in ["s", "m", "l"]:
            rows.append({
                "run_id": "r1",
                "task_id": "sort_integers",
                "language": language,
                "size": size,
                "iteration": 1,
                "status": "ok",
                "cpu_seconds": cpu * (1 if size == 's' else 2 if size == 'm' else 4),
                "wall_seconds": wall * (1 if size == 's' else 2 if size == 'm' else 4),
                "max_rss_mb": mem * (1 if size == 's' else 2 if size == 'm' else 3),
                "loc": loc,
                "community_score": 90,
                "ease_score": 9,
                "debugging_score": 8,
                "docs_score": 9,
                "libraries_score": 9,
                "concurrency_score": 8,
                "scalability_score": None,
                "overall_score": None,
            })
    medians, aggregate = score_results(rows, {
        "cpu": 0.14, "wall": 0.14, "memory": 0.10, "loc": 0.06, "ease": 0.08,
        "community": 0.08, "scalability": 0.12, "debugging": 0.06, "docs": 0.06,
        "libraries": 0.06, "concurrency": 0.10,
    })
    assert medians
    assert aggregate[0]["language"] == "go"


def test_score_results_keeps_architecture_rows_separate():
    rows = []
    for architecture, cpu in [("x86_64", 1.0), ("aarch64", 2.0)]:
        for size in ["s", "m", "l"]:
            rows.append({
                "run_id": "r1",
                "task_id": "sort_integers",
                "language": f"python-3.12@{architecture}",
                "runtime_id": "python-3.12",
                "architecture": architecture,
                "language_label": f"Python 3.12 [{architecture}]",
                "size": size,
                "iteration": 1,
                "status": "ok",
                "cpu_seconds": cpu * (1 if size == 's' else 2 if size == 'm' else 4),
                "wall_seconds": cpu * (1 if size == 's' else 2 if size == 'm' else 4),
                "max_rss_mb": 50.0,
                "loc": 30,
                "community_score": 90,
                "ease_score": 9,
                "debugging_score": 8,
                "docs_score": 9,
                "libraries_score": 9,
                "concurrency_score": 8,
                "scalability_score": None,
                "overall_score": None,
            })
    _medians, aggregate = score_results(rows, {
        "cpu": 0.14, "wall": 0.14, "memory": 0.10, "loc": 0.06, "ease": 0.08,
        "community": 0.08, "scalability": 0.12, "debugging": 0.06, "docs": 0.06,
        "libraries": 0.06, "concurrency": 0.10,
    })
    assert {row["architecture"] for row in aggregate} == {"x86_64", "aarch64"}
    assert {row["language"] for row in aggregate} == {"python-3.12@x86_64", "python-3.12@aarch64"}
