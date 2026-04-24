from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from html import escape
from pathlib import Path
from statistics import pstdev
import hashlib
import textwrap

from runner.config import ROOT, load_app_config, load_catalog, load_weights
from runner.scoring import normalize_medians, split_aggregate_scores, aggregate_for_task_ids
from runner.utils import ensure_dir, read_json

BAR_PLOT_META = {
    "overall": {
        "metric": "overall_score",
        "title": "Overall benchmark score (0-100, higher is better)",
        "subtitle": "Weighted composite of runtime, memory, LOC, scalability, and rubric/community inputs.",
        "description": "Weighted composite score; higher is better.",
    },
    "cpu": {
        "metric": "cpu_score",
        "title": "CPU efficiency score (0-100, higher is better)",
        "subtitle": "Normalized from CPU time; lower raw CPU time becomes a higher score.",
        "description": "Lower raw CPU time becomes a higher score.",
    },
    "wall": {
        "metric": "wall_score",
        "title": "Wall-clock efficiency score (0-100, higher is better)",
        "subtitle": "Normalized from elapsed runtime; lower raw runtime becomes a higher score.",
        "description": "Lower raw elapsed runtime becomes a higher score.",
    },
    "memory": {
        "metric": "memory_score",
        "title": "Memory efficiency score (0-100, higher is better)",
        "subtitle": "Normalized from max RSS memory; lower raw memory usage becomes a higher score.",
        "description": "Lower raw max RSS memory becomes a higher score.",
    },
    "loc": {
        "metric": "loc_score",
        "title": "LOC efficiency score (0-100, higher is better)",
        "subtitle": "Normalized from lines of code; fewer lines become a higher score.",
        "description": "Lower raw lines of code become a higher score.",
    },
    "scalability": {
        "metric": "scalability_score",
        "title": "Scalability score (0-100, higher is better)",
        "subtitle": "Aggregate scalability score derived from how gracefully runtime and memory grow from S to M to L.",
        "description": "Higher means runtime and memory degrade more gracefully as input size increases.",
    },
}

RAW_UNIT_PLOT_META = {
    "cpu_units": {
        "metric": "cpu_seconds_total",
        "title": "Total CPU time across the full suite",
        "subtitle": "Sum of per-task/per-size median CPU times for each language. Lower is better.",
        "footer": "Raw CPU time uses real units, not normalized benchmark scores.",
        "better": "lower",
        "unit_kind": "seconds",
    },
    "wall_units": {
        "metric": "wall_seconds_total",
        "title": "Total wall-clock time across the full suite",
        "subtitle": "Sum of per-task/per-size median elapsed times for each language. Lower is better.",
        "footer": "Raw wall time uses real units, not normalized benchmark scores.",
        "better": "lower",
        "unit_kind": "seconds",
    },
    "memory_units": {
        "metric": "memory_mb_avg",
        "title": "Average peak memory across the full suite",
        "subtitle": "Average of per-task/per-size median peak RSS values for each language. Lower is better.",
        "footer": "Raw memory uses real units, not normalized benchmark scores.",
        "better": "lower",
        "unit_kind": "memory",
    },
    "loc_units": {
        "metric": "loc_avg",
        "title": "Average lines of code per task",
        "subtitle": "Average LOC across the implemented tasks for each language. Lower is better if less code is preferred.",
        "footer": "LOC uses a raw line-count unit, not normalized benchmark scores.",
        "better": "lower",
        "unit_kind": "lines",
    },
}

GEOMEAN_PLOT_META = {
    "cpu_geomean": {
        "metric": "cpu_geomean_score",
        "title": "CPU geometric-mean efficiency score (0-100, higher is better)",
        "subtitle": "Geometric mean of normalized per-task/per-size CPU efficiency ratios.",
        "description": "Higher means better typical CPU efficiency across the suite while reducing the impact of extreme outliers.",
    },
    "wall_geomean": {
        "metric": "wall_geomean_score",
        "title": "Wall-time geometric-mean efficiency score (0-100, higher is better)",
        "subtitle": "Geometric mean of normalized per-task/per-size wall-time efficiency ratios.",
        "description": "Higher means better typical wall-clock efficiency across the suite while reducing the impact of extreme outliers.",
    },
}

VARIANCE_PLOT_META = {
    "variance_cpu": {
        "metric": "cpu_cv_percent",
        "title": "CPU variance summary",
        "subtitle": "Average coefficient of variation across measured CPU medians. Lower is better.",
        "footer": "Average CPU stddev / median across per-task/per-size measurements.",
    },
    "variance_wall": {
        "metric": "wall_cv_percent",
        "title": "Wall-time variance summary",
        "subtitle": "Average coefficient of variation across measured wall-time medians. Lower is better.",
        "footer": "Average wall-time stddev / median across per-task/per-size measurements.",
    },
    "variance_memory": {
        "metric": "memory_cv_percent",
        "title": "Memory variance summary",
        "subtitle": "Average coefficient of variation across measured peak-memory medians. Lower is better.",
        "footer": "Average memory stddev / median across per-task/per-size measurements.",
    },
}

BASELINE_PLOT_META = {
    "baseline_cpu_ratio": {
        "metric": "cpu_ratio_vs_baseline",
        "title": "CPU time relative to baseline runtime",
        "subtitle": "Runtime total CPU time divided by the configured baseline runtime. Lower is better; baseline = 1.0x.",
        "unit_kind": "ratio",
    },
    "baseline_wall_ratio": {
        "metric": "wall_ratio_vs_baseline",
        "title": "Wall time relative to baseline runtime",
        "subtitle": "Runtime total wall-clock time divided by the configured baseline runtime. Lower is better; baseline = 1.0x.",
        "unit_kind": "ratio",
    },
    "baseline_memory_ratio": {
        "metric": "memory_ratio_vs_baseline",
        "title": "Memory use relative to baseline runtime",
        "subtitle": "Runtime average peak RSS divided by the configured baseline runtime. Lower is better; baseline = 1.0x.",
        "unit_kind": "ratio",
    },
    "baseline_overall_delta": {
        "metric": "overall_delta_vs_baseline",
        "title": "Overall score delta relative to baseline runtime",
        "subtitle": "Overall composite score minus the configured baseline runtime score. Higher is better; baseline = 0.",
        "unit_kind": "delta",
    },
}


@lru_cache(maxsize=1)
def _canonical_language_order() -> list[str]:
    return list(load_app_config().languages)


@lru_cache(maxsize=1)
def _canonical_variant_order() -> list[str]:
    config = load_app_config()
    if config.language_variants:
        return list(config.language_variants.keys())
    return list(config.languages)


@lru_cache(maxsize=1)
def _task_names() -> dict[str, str]:
    return {task.id: task.name for task in load_catalog()}


def generate_report(results_path: Path, output_dir: Path) -> Path:
    payload = read_json(results_path)
    config = load_app_config()
    ensure_dir(output_dir)
    aggregate = payload.get("aggregate", [])
    medians = payload.get("medians", [])
    rows = payload.get("rows", [])
    host = payload.get("host") or {}
    git = payload.get("git") or {}
    runtimes = payload.get("runtimes") or []
    fixture_sizes = payload.get("fixture_manifest") or {}
    weights = payload.get("weights", {})
    profile = payload.get("profile") or {}
    source_notes = payload.get("source_notes") or {}
    canonical_rows = _ordered_rows(aggregate)
    raw_unit_rows = _raw_unit_rows(medians)
    best_case_rows = _best_case_rows(aggregate, "overall_score")
    best_case_raw_unit_rows = {
        stem: _best_case_rows(raw_unit_rows, meta["metric"], higher_is_better=False)
        for stem, meta in RAW_UNIT_PLOT_META.items()
    }
    category_rows = split_aggregate_scores(aggregate, weights) if aggregate and weights else {"objective": [], "opinionated": []}
    for stem, meta in RAW_UNIT_PLOT_META.items():
        metric = meta["metric"]
        error_metric = _error_metric_for_raw(stem)
        _write_svg_raw_bar(
            output_dir / f"{stem}.svg",
            _ordered_rows(raw_unit_rows),
            metric,
            meta["title"],
            meta["subtitle"],
            footer="Canonical language order from benchmark.yaml. " + meta["footer"],
            better=meta["better"],
            unit_kind=meta["unit_kind"],
            error_metric=error_metric,
        )
        _write_svg_raw_bar(
            output_dir / f"{stem}_ranked.svg",
            _ordered_rows(raw_unit_rows, metric=metric, ranked=True, reverse_for_ranking=False),
            metric,
            f"{meta['title']} — ranked best to worst",
            meta["subtitle"],
            footer="Languages sorted by this raw measurement from best to worst. " + meta["footer"],
            better=meta["better"],
            unit_kind=meta["unit_kind"],
            error_metric=error_metric,
        )
        _write_svg_raw_bar(
            output_dir / f"best_case_{stem}.svg",
            _ordered_rows(best_case_raw_unit_rows[stem], best_case=True),
            metric,
            f"{meta['title']} — language best-case",
            meta["subtitle"],
            footer="One bar per language family, keeping only the best tested version for this raw measurement.",
            better=meta["better"],
            unit_kind=meta["unit_kind"],
            error_metric=error_metric,
        )
        _write_svg_raw_bar(
            output_dir / f"best_case_{stem}_ranked.svg",
            _ordered_rows(best_case_raw_unit_rows[stem], metric=metric, ranked=True, reverse_for_ranking=False, best_case=True),
            metric,
            f"{meta['title']} — language best-case ranked",
            meta["subtitle"],
            footer="One bar per language family, sorted by the best tested version for this raw measurement.",
            better=meta["better"],
            unit_kind=meta["unit_kind"],
            error_metric=error_metric,
        )
    for stem, meta in GEOMEAN_PLOT_META.items():
        metric = meta["metric"]
        _write_svg_bar(
            output_dir / f"{stem}.svg",
            canonical_rows,
            metric,
            meta["title"],
            meta["subtitle"],
            footer="Canonical language order from benchmark.yaml.",
        )
        _write_svg_bar(
            output_dir / f"{stem}_ranked.svg",
            _ordered_rows(aggregate, metric=metric, ranked=True),
            metric,
            f"{meta['title']} — ranked best to worst",
            meta["subtitle"],
            footer="Languages sorted by geometric mean score from best to worst.",
        )
    for stem, meta in VARIANCE_PLOT_META.items():
        metric = meta["metric"]
        _write_svg_raw_bar(
            output_dir / f"{stem}.svg",
            canonical_rows,
            metric,
            meta["title"],
            meta["subtitle"],
            footer="Canonical language order from benchmark.yaml. " + meta["footer"],
            better="lower",
            unit_kind="percent",
        )
        _write_svg_raw_bar(
            output_dir / f"{stem}_ranked.svg",
            _ordered_rows(aggregate, metric=metric, ranked=True, reverse_for_ranking=False),
            metric,
            f"{meta['title']} — ranked best to worst",
            meta["subtitle"],
            footer="Languages sorted by stability from best to worst. " + meta["footer"],
            better="lower",
            unit_kind="percent",
        )
    if category_rows["objective"]:
        _write_svg_bar(
            output_dir / "objective.svg",
            _ordered_rows(category_rows["objective"]),
            "objective_score",
            "Objective benchmark score (0-100, higher is better)",
            "Recomputed only from CPU, wall time, memory, and LOC, with weights renormalized within the objective subset.",
            footer="Canonical language order from benchmark.yaml.",
        )
        _write_svg_bar(
            output_dir / "objective_ranked.svg",
            _ordered_rows(category_rows["objective"], metric="objective_score", ranked=True),
            "objective_score",
            "Objective benchmark score (0-100, higher is better) — ranked best to worst",
            "Recomputed only from CPU, wall time, memory, and LOC, with weights renormalized within the objective subset.",
            footer="Languages sorted by objective-only score from best to worst.",
        )
        objective_best_case = _best_case_rows(category_rows["objective"], "objective_score")
        _write_svg_bar(
            output_dir / "best_case_objective.svg",
            _ordered_rows(objective_best_case, best_case=True),
            "objective_score",
            "Objective benchmark score (0-100, higher is better) — language best-case",
            "One bar per language family, keeping only the best tested version for the objective-only score.",
            footer="Canonical language-family order from benchmark.yaml.",
        )
        _write_svg_bar(
            output_dir / "best_case_objective_ranked.svg",
            _ordered_rows(objective_best_case, metric="objective_score", ranked=True, best_case=True),
            "objective_score",
            "Objective benchmark score (0-100, higher is better) — language best-case ranked",
            "One bar per language family, keeping only the best tested version for the objective-only score.",
            footer="Language families sorted by their best tested objective-only score.",
        )
    if category_rows["opinionated"]:
        _write_svg_bar(
            output_dir / "opinionated.svg",
            _ordered_rows(category_rows["opinionated"]),
            "opinionated_score",
            "Opinionated benchmark score (0-100, higher is better)",
            "Recomputed only from scalability and rubric/community-style metrics, with weights renormalized within that subset.",
            footer="Canonical language order from benchmark.yaml.",
        )
        _write_svg_bar(
            output_dir / "opinionated_ranked.svg",
            _ordered_rows(category_rows["opinionated"], metric="opinionated_score", ranked=True),
            "opinionated_score",
            "Opinionated benchmark score (0-100, higher is better) — ranked best to worst",
            "Recomputed only from scalability and rubric/community-style metrics, with weights renormalized within that subset.",
            footer="Languages sorted by opinionated-only score from best to worst.",
        )
        opinionated_best_case = _best_case_rows(category_rows["opinionated"], "opinionated_score")
        _write_svg_bar(
            output_dir / "best_case_opinionated.svg",
            _ordered_rows(opinionated_best_case, best_case=True),
            "opinionated_score",
            "Opinionated benchmark score (0-100, higher is better) — language best-case",
            "One bar per language family, keeping only the best tested version for the opinionated-only score.",
            footer="Canonical language-family order from benchmark.yaml.",
        )
        _write_svg_bar(
            output_dir / "best_case_opinionated_ranked.svg",
            _ordered_rows(opinionated_best_case, metric="opinionated_score", ranked=True, best_case=True),
            "opinionated_score",
            "Opinionated benchmark score (0-100, higher is better) — language best-case ranked",
            "One bar per language family, keeping only the best tested version for the opinionated-only score.",
            footer="Language families sorted by their best tested opinionated-only score.",
        )
    for stem, meta in BAR_PLOT_META.items():
        metric = meta["metric"]
        _write_svg_bar(
            output_dir / f"{stem}.svg",
            canonical_rows,
            metric,
            meta["title"],
            meta["subtitle"],
            footer="Canonical language order from benchmark.yaml.",
        )
        _write_svg_bar(
            output_dir / f"{stem}_ranked.svg",
            _ordered_rows(aggregate, metric=metric, ranked=True),
            metric,
            f"{meta['title']} — ranked best to worst",
            meta["subtitle"],
            footer="Languages sorted by this metric from best to worst for easier comparison.",
        )
        best_case_metric_rows = _best_case_rows(aggregate, metric)
        _write_svg_bar(
            output_dir / f"best_case_{stem}.svg",
            _ordered_rows(best_case_metric_rows, best_case=True),
            metric,
            f"{meta['title']} — language best-case",
            meta["subtitle"],
            footer="One bar per language family, keeping only the best tested version for this metric.",
        )
        _write_svg_bar(
            output_dir / f"best_case_{stem}_ranked.svg",
            _ordered_rows(best_case_metric_rows, metric=metric, ranked=True, best_case=True),
            metric,
            f"{meta['title']} — language best-case ranked",
            meta["subtitle"],
            footer="Language families sorted by the best tested version for this metric.",
        )
    task_rows = _task_score_rows(medians, weights or load_weights())
    for task_id, task_score_rows in sorted(task_rows.items()):
        task_name = _task_names().get(task_id, task_id)
        _write_svg_bar(
            output_dir / f"task_{task_id}.svg",
            _ordered_rows(task_score_rows),
            "overall_score",
            f"{task_name} — per-task overall score (0-100, higher is better)",
            "This score is normalized within this task only, then averaged across S, M, and L for each language.",
            footer="Canonical language order from benchmark.yaml for this task.",
        )
        _write_svg_bar(
            output_dir / f"task_{task_id}_ranked.svg",
            _ordered_rows(task_score_rows, metric="overall_score", ranked=True),
            "overall_score",
            f"{task_name} — per-task overall score (0-100, higher is better) — ranked best to worst",
            "Same per-task score, but languages are sorted by their score for this benchmark only.",
            footer="Languages sorted by per-task overall score from best to worst.",
        )
        best_case_task_rows = _best_case_rows(task_score_rows, "overall_score")
        _write_svg_bar(
            output_dir / f"best_case_task_{task_id}.svg",
            _ordered_rows(best_case_task_rows, best_case=True),
            "overall_score",
            f"{task_name} — per-task overall score (0-100, higher is better) — language best-case",
            "One bar per language family, keeping only the best tested version for this task.",
            footer="Canonical language-family order from benchmark.yaml for this task.",
        )
        _write_svg_bar(
            output_dir / f"best_case_task_{task_id}_ranked.svg",
            _ordered_rows(best_case_task_rows, metric="overall_score", ranked=True, best_case=True),
            "overall_score",
            f"{task_name} — per-task overall score (0-100, higher is better) — language best-case ranked",
            "One bar per language family, keeping only the best tested version for this task.",
            footer="Language families sorted by their best tested per-task score.",
        )
        task_baseline = _task_baseline_rows(rows, config.baseline_runtime)
        if task_baseline:
            _write_svg_raw_bar(
                output_dir / f"task_baseline_{task_id}_ranked.svg",
                _ordered_rows(task_baseline, metric="baseline_delta", ranked=True),
                "baseline_delta",
                f"{task_name} — overall score delta vs baseline",
                f"Per-task overall score minus baseline runtime {config.baseline_runtime}. Higher is better; baseline = 0.",
                footer=f"Baseline runtime: {config.baseline_runtime}.",
                better="higher",
                unit_kind="delta",
            )
    _write_scalability_curve(
        output_dir / "scalability_curve.svg",
        medians,
        _canonical_language_order(),
        "Wall-time growth by input size (S baseline = 1.0x, lower is better)",
        "Each point shows the average per-task wall-time growth ratio for that language relative to its own S input time.",
        footer="Legend keeps the canonical language order from benchmark.yaml.",
        metric_key="wall_seconds",
        ranked=False,
    )
    _write_scalability_curve(
        output_dir / "scalability_curve_ranked.svg",
        medians,
        _growth_ranked_languages(medians, "wall_seconds"),
        "Wall-time growth by input size (S baseline = 1.0x, lower is better) — ranked legend",
        "Same wall-time growth curves, but the legend is ordered from best to worst L/S wall-time growth.",
        footer="Legend sorted by wall-time growth from best to worst.",
        metric_key="wall_seconds",
        ranked=True,
    )
    _write_scalability_curve(
        output_dir / "scalability_memory_curve.svg",
        medians,
        _canonical_language_order(),
        "Memory growth by input size (S baseline = 1.0x, lower is better)",
        "Each point shows the average per-task peak-memory growth ratio for that language relative to its own S input memory.",
        footer="Legend keeps the canonical language order from benchmark.yaml.",
        metric_key="max_rss_mb",
        ranked=False,
    )
    _write_scalability_curve(
        output_dir / "scalability_memory_curve_ranked.svg",
        medians,
        _growth_ranked_languages(medians, "max_rss_mb"),
        "Memory growth by input size (S baseline = 1.0x, lower is better) — ranked legend",
        "Same memory growth curves, but the legend is ordered from best to worst L/S memory growth.",
        footer="Legend sorted by memory growth from best to worst.",
        metric_key="max_rss_mb",
        ranked=True,
    )
    _write_growth_ratio_bar(
        output_dir / "scalability_growth_ratios.svg",
        medians,
        _canonical_language_order(),
        "L/S growth ratio summary (lower is better)",
        "Side-by-side bars compare each language's average L/S wall-time and memory growth ratios across tasks.",
        footer="Canonical language order from benchmark.yaml.",
    )
    _write_growth_ratio_bar(
        output_dir / "scalability_growth_ratios_ranked.svg",
        medians,
        _growth_ranked_languages(medians, "combined"),
        "L/S growth ratio summary (lower is better) — ranked best to worst",
        "Same L/S growth-ratio bars, but languages are ordered by the average of wall-time and memory L/S growth.",
        footer="Languages sorted by combined L/S growth from best to worst.",
    )
    service_split_rows = _service_split_rows(medians)
    for stem, metric, title in [
        ("startup_units", "startup_wall_avg", "Average startup time across service/UI workloads"),
        ("workload_units", "workload_wall_avg", "Average steady-state workload time across service/UI workloads"),
    ]:
        if service_split_rows:
            _write_svg_raw_bar(
                output_dir / f"{stem}.svg",
                _ordered_rows(service_split_rows),
                metric,
                title,
                "Average across service/UI task-size medians. Lower is better.",
                footer="Canonical runtime order from benchmark.yaml.",
                better="lower",
                unit_kind="seconds",
                error_metric=f"{metric}_ci95",
            )
            _write_svg_raw_bar(
                output_dir / f"{stem}_ranked.svg",
                _ordered_rows(service_split_rows, metric=metric, ranked=True, reverse_for_ranking=False),
                metric,
                f"{title} — ranked best to worst",
                "Average across service/UI task-size medians. Lower is better.",
                footer="Runtimes sorted by the corresponding average service/UI timing from best to worst.",
                better="lower",
                unit_kind="seconds",
                error_metric=f"{metric}_ci95",
            )
        else:
            message = f"{title} is unavailable for this artifact because no startup/workload split timings were recorded."
            _write_placeholder_svg(output_dir / f"{stem}.svg", title, message)
            _write_placeholder_svg(output_dir / f"{stem}_ranked.svg", f"{title} — ranked best to worst", message)
    _write_architecture_plot_sets(output_dir, aggregate, medians, raw_unit_rows, category_rows, service_split_rows)
    config = load_app_config()
    baseline_runtime = str(profile.get("baseline_runtime") or config.baseline_runtime)
    effective_profile = {
        "preset": profile.get("preset") or "manual / inherited",
        "iterations": profile.get("iterations") or config.iterations,
        "warmups": profile.get("warmups") or config.warmups,
        "jobs": profile.get("jobs") or 1,
        "architectures": profile.get("architectures") or config.architectures,
        "baseline_runtime": baseline_runtime,
    }
    baseline_rows = _baseline_rows(aggregate, raw_unit_rows, baseline_runtime)
    for stem, meta in BASELINE_PLOT_META.items():
        if baseline_rows:
            reverse = False if stem != "baseline_overall_delta" else True
            better = "lower" if stem != "baseline_overall_delta" else "higher"
            _write_svg_raw_bar(
                output_dir / f"{stem}.svg",
                _ordered_rows(baseline_rows),
                meta["metric"],
                meta["title"],
                meta["subtitle"],
                footer=f"Baseline runtime: {baseline_runtime}.",
                better=better,
                unit_kind=meta["unit_kind"],
            )
            _write_svg_raw_bar(
                output_dir / f"{stem}_ranked.svg",
                _ordered_rows(baseline_rows, metric=meta["metric"], ranked=True, reverse_for_ranking=reverse),
                meta["metric"],
                f"{meta['title']} — ranked",
                meta["subtitle"],
                footer=f"Baseline runtime: {baseline_runtime}.",
                better=better,
                unit_kind=meta["unit_kind"],
            )
        else:
            _write_placeholder_svg(output_dir / f"{stem}.svg", meta["title"], f"Configured baseline runtime {baseline_runtime} was not present in this artifact.")
            _write_placeholder_svg(output_dir / f"{stem}_ranked.svg", f"{meta['title']} — ranked", f"Configured baseline runtime {baseline_runtime} was not present in this artifact.")
    history_rows = _load_publish_history()
    version_history_rows = _load_version_matrix_history()
    if history_rows:
        _write_history_line(
            output_dir / "history_overall.svg",
            history_rows,
            "Historical overall-score trend across published snapshots",
            "One point per archived publish manifest / canonical published artifact.",
        )
    else:
        _write_placeholder_svg(output_dir / "history_overall.svg", "Historical overall-score trend across published snapshots", "No archived publish-history snapshots were available yet.")
    if len(version_history_rows) >= 2:
        _write_history_line(
            output_dir / "history_version_matrix_overall.svg",
            version_history_rows,
            "Version-matrix overall-score trend across published snapshots",
            "One point per archived publish manifest using the supplemental version-matrix artifact.",
        )
    else:
        _write_placeholder_svg(output_dir / "history_version_matrix_overall.svg", "Version-matrix overall-score trend across published snapshots", "At least two archived version-matrix history snapshots are required before a trend chart is shown.")
    html = _html_page(
        canonical_rows,
        raw_unit_rows,
        task_rows,
        category_rows,
        medians,
        rows,
        host,
        git,
        runtimes,
        fixture_sizes,
        weights,
        profile,
        baseline_rows,
        history_rows,
        version_history_rows,
        source_notes,
        _load_previous_publish_manifest(),
    )
    report_path = output_dir / "report.html"
    report_path.write_text(html, encoding="utf-8")
    return report_path


def _ordered_rows(
    rows: list[dict],
    metric: str | None = None,
    ranked: bool = False,
    reverse_for_ranking: bool = True,
    best_case: bool = False,
) -> list[dict]:
    if not rows:
        return []
    canonical = _canonical_language_order() if best_case else _canonical_variant_order()
    order_index = {language: index for index, language in enumerate(canonical)}
    def order_key(row: dict) -> str:
        return str(row.get("runtime_id") or row.get("language", "")).split("@", 1)[0]

    enriched = list(rows)
    if ranked and metric:
        return sorted(
            enriched,
            key=lambda row: (
                (-1 if reverse_for_ranking else 1) * float(row.get(metric, 0) or 0),
                order_index.get(order_key(row), len(order_index)),
                row.get("language", ""),
            ),
        )
    return sorted(
        enriched,
        key=lambda row: (
            order_index.get(order_key(row), len(order_index)),
            row.get("language", ""),
        ),
    )


def _architecture_groups(rows: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        architecture = row.get("architecture")
        if architecture and architecture != "unknown":
            grouped[str(architecture)].append(row)
    return dict(sorted(grouped.items()))


def _architecture_plot_stem(architecture: str, stem: str) -> str:
    safe_architecture = "".join(ch if ch.isalnum() else "_" for ch in architecture).strip("_") or "unknown"
    return f"arch_{safe_architecture}_{stem}"


def _write_architecture_plot_sets(
    output_dir: Path,
    aggregate: list[dict],
    medians: list[dict],
    raw_unit_rows: list[dict],
    category_rows: dict[str, list[dict]],
    service_split_rows: list[dict],
) -> None:
    aggregate_by_architecture = _architecture_groups(aggregate)
    if not aggregate_by_architecture:
        return
    medians_by_architecture = _architecture_groups(medians)
    raw_by_architecture = _architecture_groups(raw_unit_rows)
    service_by_architecture = _architecture_groups(service_split_rows)
    objective_by_architecture = _architecture_groups(category_rows.get("objective", []))
    opinionated_by_architecture = _architecture_groups(category_rows.get("opinionated", []))
    for architecture, arch_aggregate in aggregate_by_architecture.items():
        arch_medians = medians_by_architecture.get(architecture, [])
        arch_raw = raw_by_architecture.get(architecture, [])
        arch_objective = objective_by_architecture.get(architecture, [])
        arch_opinionated = opinionated_by_architecture.get(architecture, [])
        arch_service = service_by_architecture.get(architecture, [])
        title_suffix = f"on {architecture}"
        for stem, meta in RAW_UNIT_PLOT_META.items():
            metric = meta["metric"]
            error_metric = _error_metric_for_raw(stem)
            arch_stem = _architecture_plot_stem(architecture, stem)
            _write_svg_raw_bar(
                output_dir / f"{arch_stem}.svg",
                _ordered_rows(arch_raw),
                metric,
                f"{meta['title']} — {title_suffix}",
                meta["subtitle"],
                footer=f"Per-architecture canonical runtime order for {architecture}. " + meta["footer"],
                better=meta["better"],
                unit_kind=meta["unit_kind"],
                error_metric=error_metric,
            )
            _write_svg_raw_bar(
                output_dir / f"{arch_stem}_ranked.svg",
                _ordered_rows(arch_raw, metric=metric, ranked=True, reverse_for_ranking=False),
                metric,
                f"{meta['title']} — {title_suffix} — ranked best to worst",
                meta["subtitle"],
                footer=f"Only {architecture} runtime rows are included; sorted by this raw measurement.",
                better=meta["better"],
                unit_kind=meta["unit_kind"],
                error_metric=error_metric,
            )
        for stem, meta in BAR_PLOT_META.items():
            metric = meta["metric"]
            arch_stem = _architecture_plot_stem(architecture, stem)
            _write_svg_bar(
                output_dir / f"{arch_stem}.svg",
                _ordered_rows(arch_aggregate),
                metric,
                f"{meta['title']} — {title_suffix}",
                meta["subtitle"],
                footer=f"Only {architecture} runtime rows are included; canonical runtime order is preserved.",
            )
            _write_svg_bar(
                output_dir / f"{arch_stem}_ranked.svg",
                _ordered_rows(arch_aggregate, metric=metric, ranked=True),
                metric,
                f"{meta['title']} — {title_suffix} — ranked best to worst",
                meta["subtitle"],
                footer=f"Only {architecture} runtime rows are included; sorted best to worst for this metric.",
            )
        if arch_objective:
            arch_stem = _architecture_plot_stem(architecture, "objective")
            _write_svg_bar(
                output_dir / f"{arch_stem}.svg",
                _ordered_rows(arch_objective),
                "objective_score",
                f"Objective benchmark score (0-100, higher is better) — {title_suffix}",
                "Recomputed only from CPU, wall time, memory, and LOC for this architecture.",
                footer=f"Only {architecture} runtime rows are included; canonical runtime order is preserved.",
            )
            _write_svg_bar(
                output_dir / f"{arch_stem}_ranked.svg",
                _ordered_rows(arch_objective, metric="objective_score", ranked=True),
                "objective_score",
                f"Objective benchmark score — {title_suffix} — ranked best to worst",
                "Recomputed only from CPU, wall time, memory, and LOC for this architecture.",
                footer=f"Only {architecture} runtime rows are included; sorted by objective-only score.",
            )
        if arch_opinionated:
            arch_stem = _architecture_plot_stem(architecture, "opinionated")
            _write_svg_bar(
                output_dir / f"{arch_stem}.svg",
                _ordered_rows(arch_opinionated),
                "opinionated_score",
                f"Opinionated benchmark score (0-100, higher is better) — {title_suffix}",
                "Recomputed only from scalability and rubric/community-style metrics for this architecture.",
                footer=f"Only {architecture} runtime rows are included; canonical runtime order is preserved.",
            )
            _write_svg_bar(
                output_dir / f"{arch_stem}_ranked.svg",
                _ordered_rows(arch_opinionated, metric="opinionated_score", ranked=True),
                "opinionated_score",
                f"Opinionated benchmark score — {title_suffix} — ranked best to worst",
                "Recomputed only from scalability and rubric/community-style metrics for this architecture.",
                footer=f"Only {architecture} runtime rows are included; sorted by opinionated-only score.",
            )
        if arch_medians:
            order = _ordered_rows(arch_aggregate)
            language_order = [str(row.get("language")) for row in order]
            _write_scalability_curve(
                output_dir / f"{_architecture_plot_stem(architecture, 'scalability_curve')}.svg",
                arch_medians,
                language_order,
                f"Wall-time growth by input size — {title_suffix}",
                "S baseline = 1.0x. Lower M/L growth means better scaling within this architecture.",
                footer=f"Only {architecture} runtime rows are included.",
                metric_key="wall_seconds",
                ranked=False,
            )
            _write_scalability_curve(
                output_dir / f"{_architecture_plot_stem(architecture, 'scalability_curve')}_ranked.svg",
                arch_medians,
                _growth_ranked_languages(arch_medians, "wall_seconds"),
                f"Wall-time growth by input size — {title_suffix} — ranked legend",
                "S baseline = 1.0x. Legend is ordered from best to worst L/S wall-time growth within this architecture.",
                footer=f"Only {architecture} runtime rows are included.",
                metric_key="wall_seconds",
                ranked=True,
            )
            _write_growth_ratio_bar(
                output_dir / f"{_architecture_plot_stem(architecture, 'scalability_growth_ratios')}_ranked.svg",
                arch_medians,
                _growth_ranked_languages(arch_medians, "combined"),
                f"L/S growth ratio summary — {title_suffix} — ranked best to worst",
                "Side-by-side bars compare each runtime's average L/S wall-time and memory growth ratios within this architecture.",
                footer=f"Only {architecture} runtime rows are included.",
            )
        for stem, metric, title in [
            ("startup_units", "startup_wall_avg", "Average startup time across service/UI workloads"),
            ("workload_units", "workload_wall_avg", "Average steady-state workload time across service/UI workloads"),
        ]:
            if not arch_service:
                continue
            arch_stem = _architecture_plot_stem(architecture, stem)
            _write_svg_raw_bar(
                output_dir / f"{arch_stem}.svg",
                _ordered_rows(arch_service),
                metric,
                f"{title} — {title_suffix}",
                "Average across service/UI task-size medians. Lower is better.",
                footer=f"Only {architecture} runtime rows are included; canonical runtime order is preserved.",
                better="lower",
                unit_kind="seconds",
                error_metric=f"{metric}_ci95",
            )
            _write_svg_raw_bar(
                output_dir / f"{arch_stem}_ranked.svg",
                _ordered_rows(arch_service, metric=metric, ranked=True, reverse_for_ranking=False),
                metric,
                f"{title} — {title_suffix} — ranked best to worst",
                "Average across service/UI task-size medians. Lower is better.",
                footer=f"Only {architecture} runtime rows are included; sorted by the corresponding average service/UI timing.",
                better="lower",
                unit_kind="seconds",
                error_metric=f"{metric}_ci95",
            )


def _bar_chart_width(base_width: int, count: int, margin_left: int, margin_right: int, gap: int, min_bar_width: int = 34) -> int:
    if count <= 0:
        return base_width
    minimum_needed = margin_left + margin_right + count * min_bar_width + max(count - 1, 0) * gap
    return max(base_width, minimum_needed + 24)


def _bar_x_positions(count: int, width: int, margin_left: int, margin_right: int, gap: int) -> tuple[int, int]:
    usable_width = width - margin_left - margin_right
    if count <= 0:
        return margin_left, usable_width
    bar_width = max(34, min(88, (usable_width - gap * max(count - 1, 0)) // count))
    total_width = count * bar_width + max(count - 1, 0) * gap
    start_x = margin_left + max(0, (usable_width - total_width) // 2)
    return start_x, bar_width


def _wrap_svg_lines(text: str, width: int) -> list[str]:
    wrapped = textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)
    return wrapped or [text]


def _svg_text_block(
    parts: list[str],
    *,
    x: float,
    y: float,
    lines: list[str],
    font_size: int,
    line_height: int,
    fill: str = "#000",
    anchor: str = "middle",
    font_weight: str | None = None,
) -> None:
    weight_attr = f" font-weight='{font_weight}'" if font_weight else ""
    parts.append(
        f"<text x='{x}' y='{y}' text-anchor='{anchor}' font-size='{font_size}' fill='{fill}'{weight_attr}>"
    )
    for index, line in enumerate(lines):
        dy = "0" if index == 0 else str(line_height)
        parts.append(f"<tspan x='{x}' dy='{dy}'>{escape(line)}</tspan>")
    parts.append("</text>")


def _svg_rotated_label(parts: list[str], *, x: float, y: float, text: str, angle: int = -32, font_size: int = 11, fill: str = "#111") -> None:
    parts.append(
        f"<text x='{x}' y='{y}' transform='rotate({angle} {x} {y})' text-anchor='end' "
        f"font-size='{font_size}' fill='{fill}'>{escape(text)}</text>"
    )


def _bar_labels_are_crowded(rows: list[dict]) -> bool:
    if len(rows) >= 8:
        return True
    return any(len(_display_label(row)) > 12 for row in rows)


def _render_bar_label(parts: list[str], *, x: float, y: float, row: dict, crowded: bool) -> None:
    label = _display_label(row)
    if crowded:
        _svg_rotated_label(parts, x=x + 8, y=y + 18, text=label, angle=-30, font_size=11, fill="#222")
        return
    parts.append(f"<text x='{x}' y='{y}' text-anchor='middle' font-size='12'>{escape(label)}</text>")


def _footer_block_y(height: int, lines: list[str], line_height: int = 14, bottom_padding: int = 12) -> int:
    return height - bottom_padding - ((max(1, len(lines)) - 1) * line_height)


def _write_placeholder_svg(path: Path, title: str, message: str) -> None:
    title_lines = _wrap_svg_lines(title, 58)
    message_lines = _wrap_svg_lines(message, 78)
    height = 220
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='860' height='{height}' viewBox='0 0 860 {height}'>"]
    parts.append("<rect x='0' y='0' width='860' height='{0}' fill='#ffffff'/>".format(height))
    parts.append("<rect x='0.5' y='0.5' width='859' height='{0}' fill='none' stroke='#d1d5db'/>".format(height - 1))
    _svg_text_block(parts, x=430, y=34, lines=title_lines, font_size=20, line_height=22)
    _svg_text_block(parts, x=430, y=100, lines=message_lines, font_size=13, line_height=18, fill="#555")
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def _error_metric_for_raw(stem: str) -> str | None:
    return {
        "cpu_units": "cpu_ci95_total_seconds",
        "wall_units": "wall_ci95_total_seconds",
        "memory_units": "memory_ci95_avg_mb",
    }.get(stem)


def _write_svg_bar(path: Path, rows: list[dict], metric: str, title: str, subtitle: str, footer: str) -> None:
    width, height = 860, 520
    title_lines = _wrap_svg_lines(title, 58)
    subtitle_lines = _wrap_svg_lines(subtitle, 92)
    footer_lines = _wrap_svg_lines(f"{footer} All bars are normalized scores from 0 to 100, so higher bars are better.", 118)
    crowded_labels = _bar_labels_are_crowded(rows)
    margin_left, margin_right = 64, 48
    width = _bar_chart_width(width, len(rows), margin_left, margin_right, 18)
    margin_top = 24 + len(title_lines) * 22 + len(subtitle_lines) * 16 + 18
    label_space = 88 if crowded_labels else 40
    margin_bottom = label_space + 28 + len(footer_lines) * 14
    plot_height = height - margin_top - margin_bottom
    gap = 18
    start_x, bar_width = _bar_x_positions(len(rows), width, margin_left, margin_right, gap)
    max_value = 100.0
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' viewBox='0 0 {width} {height}'>"]
    parts.append(f"<rect x='0' y='0' width='{width}' height='{height}' fill='#ffffff'/>")
    parts.append(f"<rect x='0.5' y='0.5' width='{width - 1}' height='{height - 1}' fill='none' stroke='#d1d5db'/>")
    _svg_text_block(parts, x=width / 2, y=28, lines=title_lines, font_size=20, line_height=22)
    _svg_text_block(parts, x=width / 2, y=28 + len(title_lines) * 22, lines=subtitle_lines, font_size=12, line_height=16, fill="#555")
    for tick in [0, 25, 50, 75, 100]:
        y = margin_top + plot_height - int((tick / max_value) * plot_height)
        parts.append(f"<line x1='{margin_left}' y1='{y}' x2='{width - margin_right}' y2='{y}' stroke='#e5e7eb' stroke-width='1'/>")
        parts.append(f"<text x='{margin_left - 10}' y='{y + 4}' text-anchor='end' font-size='11' fill='#555'>{tick}</text>")
    parts.append(f"<line x1='{margin_left}' y1='{margin_top + plot_height}' x2='{width - margin_right}' y2='{margin_top + plot_height}' stroke='black'/>")
    for idx, row in enumerate(rows):
        value = float(row.get(metric, 0) or 0)
        x = start_x + idx * (bar_width + gap)
        bar_height = int((value / max_value) * plot_height)
        y = margin_top + plot_height - bar_height
        parts.append(f"<rect x='{x}' y='{y}' width='{bar_width}' height='{bar_height}' rx='4' fill='#4f46e5'/>")
        _render_bar_label(parts, x=x + bar_width / 2, y=margin_top + plot_height + 22, row=row, crowded=crowded_labels)
        parts.append(f"<text x='{x + bar_width / 2}' y='{max(margin_top + 14, y - 8)}' text-anchor='middle' font-size='12'>{value:.1f}</text>")
    _svg_text_block(parts, x=width / 2, y=_footer_block_y(height, footer_lines), lines=footer_lines, font_size=11, line_height=14, fill="#555")
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def _write_svg_raw_bar(path: Path, rows: list[dict], metric: str, title: str, subtitle: str, footer: str, better: str, unit_kind: str, error_metric: str | None = None) -> None:
    width, height = 860, 520
    raw_values = [float(row.get(metric, 0) or 0) for row in rows]
    error_values = [float(row.get(error_metric, 0) or 0) for row in rows] if error_metric else [0.0 for _ in rows]
    scaled_values, unit_label = _scaled_values(raw_values, unit_kind)
    scaled_errors, _ = _scaled_values(error_values, unit_kind)
    title_lines = _wrap_svg_lines(f"{title} ({unit_label}, {better} is better)", 58)
    subtitle_lines = _wrap_svg_lines(subtitle, 92)
    footer_lines = _wrap_svg_lines(footer, 118)
    crowded_labels = _bar_labels_are_crowded(rows)
    margin_left, margin_right = 72, 48
    width = _bar_chart_width(width, len(rows), margin_left, margin_right, 18)
    margin_top = 24 + len(title_lines) * 22 + len(subtitle_lines) * 16 + 18
    label_space = 88 if crowded_labels else 40
    margin_bottom = label_space + 28 + len(footer_lines) * 14
    plot_height = height - margin_top - margin_bottom
    gap = 18
    start_x, bar_width = _bar_x_positions(len(rows), width, margin_left, margin_right, gap)
    min_scaled = min(scaled_values, default=0.0)
    max_scaled = max(scaled_values, default=0.0)
    axis_min = _nice_floor(min_scaled) if min_scaled < 0 else 0.0
    axis_max = _nice_ceiling(max_scaled) if max_scaled > 0 else 0.0
    if axis_min == axis_max:
        axis_max = 1.0
    axis_span = max(axis_max - axis_min, 1e-9)
    zero_y = margin_top + plot_height - int(((0.0 - axis_min) / axis_span) * plot_height)
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' viewBox='0 0 {width} {height}'>"]
    parts.append(f"<rect x='0' y='0' width='{width}' height='{height}' fill='#ffffff'/>")
    parts.append(f"<rect x='0.5' y='0.5' width='{width - 1}' height='{height - 1}' fill='none' stroke='#d1d5db'/>")
    _svg_text_block(parts, x=width / 2, y=28, lines=title_lines, font_size=20, line_height=22)
    _svg_text_block(parts, x=width / 2, y=28 + len(title_lines) * 22, lines=subtitle_lines, font_size=12, line_height=16, fill="#555")
    tick_values = [axis_min + axis_span * fraction for fraction in [0, 0.25, 0.5, 0.75, 1.0]]
    for tick in tick_values:
        y = margin_top + plot_height - int(((tick - axis_min) / axis_span) * plot_height)
        parts.append(f"<line x1='{margin_left}' y1='{y}' x2='{width - margin_right}' y2='{y}' stroke='#e5e7eb' stroke-width='1'/>")
        parts.append(f"<text x='{margin_left - 10}' y='{y + 4}' text-anchor='end' font-size='11' fill='#555'>{_format_tick(tick, unit_kind)}</text>")
    parts.append(f"<line x1='{margin_left}' y1='{zero_y}' x2='{width - margin_right}' y2='{zero_y}' stroke='black'/>")
    for idx, row in enumerate(rows):
        scaled = scaled_values[idx]
        raw = raw_values[idx]
        error_scaled = scaled_errors[idx] if idx < len(scaled_errors) else 0.0
        x = start_x + idx * (bar_width + gap)
        value_y = margin_top + plot_height - int(((scaled - axis_min) / axis_span) * plot_height)
        rect_y = min(zero_y, value_y)
        bar_height = max(1 if scaled != 0 else 0, abs(zero_y - value_y))
        parts.append(f"<rect x='{x}' y='{rect_y}' width='{bar_width}' height='{bar_height}' rx='4' fill='#0f766e'/>")
        if error_scaled > 0:
            center_x = x + bar_width / 2
            top_value = min(scaled + error_scaled, axis_max)
            bottom_value = max(scaled - error_scaled, axis_min)
            top_y = margin_top + plot_height - int(((top_value - axis_min) / axis_span) * plot_height)
            bottom_y = margin_top + plot_height - int(((bottom_value - axis_min) / axis_span) * plot_height)
            parts.append(f"<line x1='{center_x}' y1='{top_y}' x2='{center_x}' y2='{bottom_y}' stroke='#111827' stroke-width='2'/>")
            parts.append(f"<line x1='{center_x - 6}' y1='{top_y}' x2='{center_x + 6}' y2='{top_y}' stroke='#111827' stroke-width='2'/>")
            parts.append(f"<line x1='{center_x - 6}' y1='{bottom_y}' x2='{center_x + 6}' y2='{bottom_y}' stroke='#111827' stroke-width='2'/>")
        _render_bar_label(parts, x=x + bar_width / 2, y=margin_top + plot_height + 22, row=row, crowded=crowded_labels)
        label_y = max(margin_top + 14, rect_y - 8) if scaled >= 0 else min(margin_top + plot_height - 6, rect_y + bar_height + 16)
        parts.append(f"<text x='{x + bar_width / 2}' y='{label_y}' text-anchor='middle' font-size='12'>{_format_value(raw, unit_kind)}</text>")
    _svg_text_block(parts, x=width / 2, y=_footer_block_y(height, footer_lines), lines=footer_lines, font_size=11, line_height=14, fill="#555")
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def _write_scalability_curve(path: Path, medians: list[dict], language_order: list[str], title: str, subtitle: str, footer: str, metric_key: str, ranked: bool) -> None:
    base_width, base_height = 980, 460
    title_lines = _wrap_svg_lines(title, 72)
    subtitle_lines = _wrap_svg_lines(subtitle, 110)
    footer_lines = _wrap_svg_lines(f"{footer} Lower lines indicate better scaling behavior.", 134)
    margin_left = 72
    margin_top = 24 + len(title_lines) * 22 + len(subtitle_lines) * 16 + 18
    margin_bottom = 28 + len(footer_lines) * 14
    curve_data = _growth_curve_rows(medians, metric_key)
    label_map = _label_map(medians)
    colors = _language_colors(curve_data.keys())
    ordered_languages = [language for language in language_order if language in curve_data]
    ordered_languages.extend(sorted(language for language in curve_data if language not in ordered_languages))
    max_value = max((max(points.values()) for points in curve_data.values()), default=1.0)
    max_tick = _nice_ceiling(max_value)
    legend_title = "Ranked legend" if ranked else "Legend order"
    legend_font_size = 12
    legend_title_size = 13
    legend_line_height = 22
    legend_text_width = max([len(legend_title) * 8] + [len(label_map.get(language, language)) * 7 for language in ordered_languages] or [140])
    legend_width = max(210, legend_text_width + 56)
    legend_height = 18 + len(ordered_languages) * legend_line_height + 16
    margin_right = legend_width + 48
    width = max(base_width, margin_left + 560 + margin_right)
    height = max(base_height, margin_top + legend_height + margin_bottom + 20)
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom
    xs = {
        "s": margin_left + int(plot_width * 0.15),
        "m": margin_left + int(plot_width * 0.5),
        "l": margin_left + int(plot_width * 0.85),
    }

    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' viewBox='0 0 {width} {height}'>"]
    parts.append(f"<rect x='0' y='0' width='{width}' height='{height}' fill='#ffffff'/>")
    parts.append(f"<rect x='0.5' y='0.5' width='{width - 1}' height='{height - 1}' fill='none' stroke='#d1d5db'/>")
    _svg_text_block(parts, x=width / 2, y=28, lines=title_lines, font_size=20, line_height=22)
    _svg_text_block(parts, x=width / 2, y=28 + len(title_lines) * 22, lines=subtitle_lines, font_size=12, line_height=16, fill="#555")
    for fraction in [0, 0.25, 0.5, 0.75, 1.0]:
        tick = max_tick * fraction
        y = margin_top + plot_height - int((tick / max_tick) * plot_height) if max_tick else margin_top + plot_height
        parts.append(f"<line x1='{margin_left}' y1='{y}' x2='{margin_left + plot_width}' y2='{y}' stroke='#e5e7eb' stroke-width='1'/>")
        parts.append(f"<text x='{margin_left - 10}' y='{y + 4}' text-anchor='end' font-size='11' fill='#555'>{tick:.1f}x</text>")
    for size, x in xs.items():
        parts.append(f"<line x1='{x}' y1='{margin_top}' x2='{x}' y2='{margin_top + plot_height}' stroke='#f1f5f9' stroke-width='1'/>")
        parts.append(f"<text x='{x}' y='{margin_top + plot_height + 22}' text-anchor='middle' font-size='12'>{size.upper()}</text>")
    for language in ordered_languages:
        coords = []
        for size in ["s", "m", "l"]:
            value = curve_data[language].get(size, 1.0)
            y = margin_top + plot_height - int((value / max_tick) * plot_height) if max_tick else margin_top + plot_height
            coords.append((xs[size], y, value))
        parts.append(
            f"<polyline points='{' '.join(f'{x},{y}' for x, y, _ in coords)}' fill='none' stroke='{colors[language]}' stroke-width='3' stroke-linecap='round'/>"
        )
        for x, y, value in coords:
            parts.append(f"<circle cx='{x}' cy='{y}' r='4' fill='{colors[language]}'/>")
            parts.append(f"<title>{escape(label_map.get(language, language))} {value:.2f}x</title>")
    legend_x = margin_left + plot_width + 24
    parts.append(f"<rect x='{legend_x - 12}' y='{margin_top}' width='{legend_width}' height='{legend_height}' rx='8' fill='#f8fafc' stroke='#e5e7eb'/>")
    parts.append(f"<text x='{legend_x}' y='{margin_top + 18}' font-size='{legend_title_size}' font-weight='bold'>{legend_title}</text>")
    for idx, language in enumerate(ordered_languages):
        y = margin_top + 40 + idx * legend_line_height
        parts.append(f"<line x1='{legend_x}' y1='{y - 4}' x2='{legend_x + 18}' y2='{y - 4}' stroke='{colors[language]}' stroke-width='4' stroke-linecap='round'/>")
        parts.append(f"<text x='{legend_x + 28}' y='{y}' font-size='{legend_font_size}'>{escape(label_map.get(language, language))}</text>")
    _svg_text_block(parts, x=width / 2, y=_footer_block_y(height, footer_lines), lines=footer_lines, font_size=11, line_height=14, fill="#555")
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def _growth_curve_rows(medians: list[dict], metric_key: str) -> dict[str, dict[str, float]]:
    grouped: dict[tuple[str, str], dict[str, dict]] = defaultdict(dict)
    for row in medians:
        grouped[(row["language"], row["task_id"])][row["size"]] = row
    by_language: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for (language, _task_id), sizes in grouped.items():
        if not {"s", "m", "l"}.issubset(sizes):
            continue
        s_value = max(float(sizes["s"].get(metric_key, 0) or 0), 1e-9)
        by_language[language]["s"].append(1.0)
        by_language[language]["m"].append(float(sizes["m"].get(metric_key, 0) or 0) / s_value)
        by_language[language]["l"].append(float(sizes["l"].get(metric_key, 0) or 0) / s_value)
    averaged: dict[str, dict[str, float]] = {}
    for language, size_map in by_language.items():
        averaged[language] = {
            size: round(sum(values) / len(values), 3)
            for size, values in size_map.items()
            if values
        }
    return averaged


def _language_colors(languages) -> dict[str, str]:
    palette = ["#4f46e5", "#0891b2", "#16a34a", "#dc2626", "#9333ea", "#ea580c", "#475569", "#0f766e", "#ca8a04"]
    canonical = _canonical_language_order()
    all_languages = [language for language in canonical if language in languages]
    all_languages.extend(sorted(language for language in languages if language not in all_languages))
    return {language: palette[idx % len(palette)] for idx, language in enumerate(all_languages)}


def _display_label(row: dict) -> str:
    if row.get("best_variant_label"):
        family = str(row.get("language_label") or row.get("language_family") or row.get("language") or "")
        return f"{family} ({row['best_variant_label']})"
    return str(row.get("language_label") or row.get("language") or "")


def _label_map(rows: list[dict]) -> dict[str, str]:
    labels: dict[str, str] = {}
    for row in rows:
        language = row.get("language")
        label = row.get("language_label")
        if language and label:
            labels[str(language)] = str(label)
    return labels


def _family_label(family: str) -> str:
    labels = {
        "php": "PHP",
        "python": "Python",
        "java": "Java",
        "cpp": "C++",
        "node": "Node.js",
        "go": "Go",
        "rust": "Rust",
    }
    return labels.get(family, family)


def _best_case_rows(rows: list[dict], metric: str, higher_is_better: bool = True) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("language_family") or row.get("language"))].append(row)
    output = []
    for family, bucket in grouped.items():
        best = max(bucket, key=lambda row: float(row.get(metric, 0) or 0)) if higher_is_better else min(bucket, key=lambda row: float(row.get(metric, 0) or 0))
        collapsed = dict(best)
        collapsed["language"] = family
        collapsed["language_family"] = family
        collapsed["language_label"] = _family_label(family)
        collapsed["best_variant"] = best.get("language")
        collapsed["best_variant_label"] = best.get("language_label", best.get("language"))
        collapsed["best_variant_version"] = best.get("language_version")
        output.append(collapsed)
    return output


def _raw_unit_rows(medians: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in medians:
        grouped[row["language"]].append(row)
    rows = []
    for language, bucket in grouped.items():
        rows.append({
            "language": language,
            "runtime_id": bucket[0].get("runtime_id", language),
            "architecture": bucket[0].get("architecture", "unknown"),
            "language_family": bucket[0].get("language_family", language),
            "language_label": bucket[0].get("language_label", language),
            "language_version": bucket[0].get("language_version"),
            "cpu_seconds_total": round(sum(float(row.get("cpu_seconds", 0) or 0) for row in bucket), 6),
            "wall_seconds_total": round(sum(float(row.get("wall_seconds", 0) or 0) for row in bucket), 6),
            "memory_mb_avg": round(sum(float(row.get("max_rss_mb", 0) or 0) for row in bucket) / max(len(bucket), 1), 6),
            "loc_avg": round(sum(float(row.get("loc", 0) or 0) for row in bucket) / max(len(bucket), 1), 2),
            "cpu_ci95_total_seconds": round(sum(float(row.get("cpu_ci95_seconds", 0) or 0) ** 2 for row in bucket) ** 0.5, 6),
            "wall_ci95_total_seconds": round(sum(float(row.get("wall_ci95_seconds", 0) or 0) ** 2 for row in bucket) ** 0.5, 6),
            "memory_ci95_avg_mb": round((sum(float(row.get("memory_ci95_mb", 0) or 0) ** 2 for row in bucket) ** 0.5) / max(len(bucket), 1), 6),
        })
    return rows


def _scaled_values(values: list[float], unit_kind: str) -> tuple[list[float], str]:
    if unit_kind == "seconds":
        if max(values or [0.0]) < 1.0:
            return [value * 1000.0 for value in values], "ms"
        return values, "s"
    if unit_kind == "memory":
        if max(values or [0.0]) >= 1024.0:
            return [value / 1024.0 for value in values], "GB"
        return values, "MB"
    if unit_kind == "percent":
        return values, "%"
    if unit_kind == "ratio":
        return values, "x"
    if unit_kind == "delta":
        return values, "pts"
    return values, "lines"


def _format_value(value: float, unit_kind: str) -> str:
    if unit_kind == "seconds":
        return f"{value * 1000:.1f} ms" if value < 1.0 else f"{value:.2f} s"
    if unit_kind == "memory":
        return f"{value / 1024:.2f} GB" if value >= 1024.0 else f"{value:.1f} MB"
    if unit_kind == "percent":
        return f"{value:.2f}%"
    if unit_kind == "ratio":
        return f"{value:.2f}x"
    if unit_kind == "delta":
        return f"{value:+.2f}"
    return f"{value:.1f}"


def _format_tick(value: float, unit_kind: str) -> str:
    if unit_kind in {"seconds", "memory"}:
        return f"{value:.1f}"
    if unit_kind == "percent":
        return f"{value:.1f}%"
    if unit_kind == "ratio":
        return f"{value:.1f}x"
    if unit_kind == "delta":
        return f"{value:+.1f}"
    return f"{value:.0f}"


def _nice_ceiling(value: float) -> float:
    if value <= 0:
        return 1.0
    magnitude = 10 ** (len(str(int(value))) - 1)
    for factor in [1, 2, 5, 10]:
        candidate = factor * magnitude
        if candidate >= value:
            return float(candidate)
    return float(10 * magnitude)


def _nice_floor(value: float) -> float:
    if value >= 0:
        return 0.0
    return -_nice_ceiling(abs(value))


def _stddev_list(values: list[float]) -> float:
    if len(values) <= 1:
        return 0.0
    return float(pstdev(values))


def _growth_ranked_languages(medians: list[dict], metric_key: str) -> list[str]:
    if metric_key == "combined":
        wall = _growth_curve_rows(medians, "wall_seconds")
        mem = _growth_curve_rows(medians, "max_rss_mb")
        languages = sorted(set(wall) | set(mem))
        scored = []
        for language in languages:
            wall_l = wall.get(language, {}).get("l", 1e9)
            mem_l = mem.get(language, {}).get("l", 1e9)
            scored.append((language, (wall_l + mem_l) / 2.0))
        return [language for language, _ in sorted(scored, key=lambda item: item[1])]
    growth = _growth_curve_rows(medians, metric_key)
    return [language for language, _ in sorted(growth.items(), key=lambda item: item[1].get("l", 1e9))]


def _write_growth_ratio_bar(path: Path, medians: list[dict], language_order: list[str], title: str, subtitle: str, footer: str) -> None:
    width, height = 980, 540
    title_lines = _wrap_svg_lines(title, 72)
    subtitle_lines = _wrap_svg_lines(subtitle, 110)
    footer_lines = _wrap_svg_lines(f"{footer} Lower bars are better.", 134)
    margin_left, margin_right = 72, 48
    width = _bar_chart_width(width, len(language_order), margin_left, margin_right, 16)
    margin_top = 24 + len(title_lines) * 22 + len(subtitle_lines) * 16 + 18
    gap = 16
    rows = []
    wall = _growth_curve_rows(medians, "wall_seconds")
    mem = _growth_curve_rows(medians, "max_rss_mb")
    label_map = _label_map(medians)
    for language in language_order:
        if language not in wall and language not in mem:
            continue
        rows.append({
            "language": language,
            "language_label": label_map.get(language, language),
            "wall_l": wall.get(language, {}).get("l", 0.0),
            "memory_l": mem.get(language, {}).get("l", 0.0),
        })
    crowded_labels = _bar_labels_are_crowded(rows)
    label_space = 96 if crowded_labels else 48
    margin_bottom = label_space + 40 + len(footer_lines) * 14
    plot_height = height - margin_top - margin_bottom
    max_value = max([max(row["wall_l"], row["memory_l"]) for row in rows] or [1.0])
    max_tick = _nice_ceiling(max_value)
    start_x, bar_width = _bar_x_positions(len(rows), width, margin_left, margin_right, gap)
    inner_gap = 6
    pair_width = max(18, (bar_width - inner_gap) // 2)
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' viewBox='0 0 {width} {height}'>"]
    parts.append(f"<rect x='0' y='0' width='{width}' height='{height}' fill='#ffffff'/>")
    parts.append(f"<rect x='0.5' y='0.5' width='{width - 1}' height='{height - 1}' fill='none' stroke='#d1d5db'/>")
    _svg_text_block(parts, x=width / 2, y=28, lines=title_lines, font_size=20, line_height=22)
    _svg_text_block(parts, x=width / 2, y=28 + len(title_lines) * 22, lines=subtitle_lines, font_size=12, line_height=16, fill="#555")
    for fraction in [0, 0.25, 0.5, 0.75, 1.0]:
        tick = max_tick * fraction
        y = margin_top + plot_height - int((tick / max_tick) * plot_height)
        parts.append(f"<line x1='{margin_left}' y1='{y}' x2='{width - margin_right}' y2='{y}' stroke='#e5e7eb' stroke-width='1'/>")
        parts.append(f"<text x='{margin_left - 10}' y='{y + 4}' text-anchor='end' font-size='11' fill='#555'>{tick:.1f}x</text>")
    parts.append(f"<line x1='{margin_left}' y1='{margin_top + plot_height}' x2='{width - margin_right}' y2='{margin_top + plot_height}' stroke='black'/>")
    for idx, row in enumerate(rows):
        x = start_x + idx * (bar_width + gap)
        for offset, field, color in [(0, "wall_l", "#4f46e5"), (pair_width + inner_gap, "memory_l", "#0f766e")]:
            value = row[field]
            bar_height = int((value / max_tick) * plot_height) if max_tick else 0
            y = margin_top + plot_height - bar_height
            parts.append(f"<rect x='{x + offset}' y='{y}' width='{pair_width}' height='{bar_height}' rx='3' fill='{color}'/>")
        _render_bar_label(parts, x=x + bar_width / 2, y=margin_top + plot_height + 22, row=row, crowded=crowded_labels)
        parts.append(f"<text x='{x + pair_width / 2}' y='{max(margin_top + 14, margin_top + plot_height - int((row['wall_l'] / max_tick) * plot_height) - 8)}' text-anchor='middle' font-size='11'>{row['wall_l']:.2f}x</text>")
        parts.append(f"<text x='{x + pair_width + inner_gap + pair_width / 2}' y='{max(margin_top + 14, margin_top + plot_height - int((row['memory_l'] / max_tick) * plot_height) - 8)}' text-anchor='middle' font-size='11'>{row['memory_l']:.2f}x</text>")
    legend_x = width - margin_right - 180
    legend_y = height - margin_bottom - 34
    parts.append(f"<rect x='{legend_x}' y='{legend_y}' width='180' height='30' rx='8' fill='#f8fafc' stroke='#e5e7eb'/>")
    parts.append(f"<rect x='{legend_x + 12}' y='{legend_y + 9}' width='14' height='14' rx='3' fill='#4f46e5'/>")
    parts.append(f"<text x='{legend_x + 34}' y='{legend_y + 20}' font-size='12'>Wall L/S</text>")
    parts.append(f"<rect x='{legend_x + 92}' y='{legend_y + 9}' width='14' height='14' rx='3' fill='#0f766e'/>")
    parts.append(f"<text x='{legend_x + 114}' y='{legend_y + 20}' font-size='12'>Memory L/S</text>")
    _svg_text_block(parts, x=width / 2, y=_footer_block_y(height, footer_lines), lines=footer_lines, font_size=11, line_height=14, fill="#555")
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def _write_history_line(path: Path, history_rows: list[dict], title: str, subtitle: str) -> None:
    if not history_rows:
        return
    languages = []
    label_map: dict[str, str] = {}
    for item in history_rows:
        for row in item.get("aggregate", []):
            language = row.get("language")
            if language and language not in languages:
                languages.append(language)
            if language and row.get("language_label"):
                label_map[str(language)] = str(row.get("language_label"))
    colors = _language_colors(languages)
    width, height = 980, max(460, 380 + len(languages) * 4)
    title_lines = _wrap_svg_lines(title, 72)
    subtitle_lines = _wrap_svg_lines(subtitle, 108)
    margin_left, margin_right, margin_top, margin_bottom = 72, 180, 24 + len(title_lines) * 22 + len(subtitle_lines) * 16 + 18, 56
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom
    max_value = max((float(row.get("overall_score", 0) or 0) for item in history_rows for row in item.get("aggregate", [])), default=100.0)
    max_tick = _nice_ceiling(max_value)
    steps = max(len(history_rows) - 1, 1)
    xs = [margin_left + int(plot_width * (idx / steps)) for idx in range(len(history_rows))]
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' viewBox='0 0 {width} {height}'>"]
    parts.append(f"<rect x='0' y='0' width='{width}' height='{height}' fill='#ffffff'/>")
    parts.append(f"<rect x='0.5' y='0.5' width='{width - 1}' height='{height - 1}' fill='none' stroke='#d1d5db'/>")
    _svg_text_block(parts, x=width / 2, y=28, lines=title_lines, font_size=20, line_height=22)
    _svg_text_block(parts, x=width / 2, y=28 + len(title_lines) * 22, lines=subtitle_lines, font_size=12, line_height=16, fill="#555")
    for fraction in [0, 0.25, 0.5, 0.75, 1.0]:
        tick = max_tick * fraction
        y = margin_top + plot_height - int((tick / max_tick) * plot_height) if max_tick else margin_top + plot_height
        parts.append(f"<line x1='{margin_left}' y1='{y}' x2='{margin_left + plot_width}' y2='{y}' stroke='#e5e7eb' stroke-width='1'/>")
        parts.append(f"<text x='{margin_left - 10}' y='{y + 4}' text-anchor='end' font-size='11' fill='#555'>{tick:.0f}</text>")
    for idx, item in enumerate(history_rows):
        x = xs[idx]
        parts.append(f"<line x1='{x}' y1='{margin_top}' x2='{x}' y2='{margin_top + plot_height}' stroke='#f1f5f9' stroke-width='1'/>")
        parts.append(f"<text x='{x}' y='{margin_top + plot_height + 22}' text-anchor='middle' font-size='11'>{escape(str(item.get('run_id'))[-6:])}</text>")
    for language in languages:
        coords = []
        for idx, item in enumerate(history_rows):
            matching = next((row for row in item.get("aggregate", []) if row.get("language") == language), None)
            if not matching:
                continue
            value = float(matching.get("overall_score", 0) or 0)
            y = margin_top + plot_height - int((value / max_tick) * plot_height) if max_tick else margin_top + plot_height
            coords.append((xs[idx], y, value))
        if len(coords) >= 2:
            parts.append(f"<polyline points='{' '.join(f'{x},{y}' for x, y, _ in coords)}' fill='none' stroke='{colors[language]}' stroke-width='3' stroke-linecap='round'/>")
        for x, y, value in coords:
            parts.append(f"<circle cx='{x}' cy='{y}' r='4' fill='{colors[language]}'/>")
            parts.append(f"<title>{escape(label_map.get(language, language))} {value:.2f}</title>")
    legend_x = margin_left + plot_width + 24
    parts.append(f"<rect x='{legend_x - 12}' y='{margin_top}' width='168' height='{max(40, 24 + len(languages) * 18)}' rx='8' fill='#f8fafc' stroke='#e5e7eb'/>")
    for idx, language in enumerate(languages):
        y = margin_top + 20 + idx * 18
        parts.append(f"<line x1='{legend_x}' y1='{y}' x2='{legend_x + 18}' y2='{y}' stroke='{colors[language]}' stroke-width='4' stroke-linecap='round'/>")
        label = label_map.get(language) or (_family_label(language) if "-" not in language and "@" not in language else language)
        parts.append(f"<text x='{legend_x + 28}' y='{y + 4}' font-size='11'>{escape(label)}</text>")
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def _task_score_rows(medians: list[dict], weights: dict[str, float]) -> dict[str, list[dict]]:
    if not medians:
        return {}
    effective_weights = weights or load_weights()
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in medians:
        enriched = dict(row)
        for field in (
            "ease_score",
            "community_score",
            "scalability_score",
            "debugging_score",
            "docs_score",
            "libraries_score",
            "concurrency_score",
        ):
            enriched.setdefault(field, 0.0)
        grouped[enriched["task_id"]].append(enriched)
    output: dict[str, list[dict]] = {}
    for task_id, rows in grouped.items():
        normalized = normalize_medians(rows)
        per_language: dict[str, list[dict]] = defaultdict(list)
        for row in normalized:
            per_language[row["language"]].append(row)
        task_scores = []
        for language, bucket in per_language.items():
            averaged = {metric: sum(r[metric] for r in bucket) / len(bucket) for metric in bucket[0] if metric.endswith("_score") or metric == "loc_score"}
            overall = (
                averaged["cpu_score"] * effective_weights["cpu"] +
                averaged["wall_score"] * effective_weights["wall"] +
                averaged["memory_score"] * effective_weights["memory"] +
                averaged["loc_score"] * effective_weights["loc"] +
                averaged["ease_score"] * effective_weights["ease"] +
                averaged["community_score"] * effective_weights["community"] +
                averaged["scalability_score"] * effective_weights["scalability"] +
                averaged["debugging_score"] * effective_weights["debugging"] +
                averaged["docs_score"] * effective_weights["docs"] +
                averaged["libraries_score"] * effective_weights["libraries"] +
                averaged["concurrency_score"] * effective_weights["concurrency"]
            )
            task_scores.append({
                "language": language,
                "language_family": bucket[0].get("language_family", language),
                "language_label": bucket[0].get("language_label", language),
                "language_version": bucket[0].get("language_version"),
                "overall_score": round(overall, 2),
                "cpu_score": round(averaged["cpu_score"], 2),
                "wall_score": round(averaged["wall_score"], 2),
                "memory_score": round(averaged["memory_score"], 2),
                "loc_score": round(averaged["loc_score"], 2),
                "scalability_score": round(averaged["scalability_score"], 2),
            })
        output[task_id] = sorted(task_scores, key=lambda row: row["overall_score"], reverse=True)
    return output


def _task_baseline_rows(task_rows: list[dict], baseline_runtime: str) -> list[dict]:
    config = load_app_config()
    baseline_family = config.language_variants.get(baseline_runtime, {}).get("family", baseline_runtime)
    baseline = next((row for row in task_rows if row.get("language") == baseline_runtime or row.get("runtime_id") == baseline_runtime), None)
    if baseline is None:
        baseline = next((row for row in task_rows if row.get("language") == baseline_family or row.get("language_family") == baseline_family), None)
    if baseline is None:
        return []
    return [
        {
            "language": row["language"],
            "language_family": row.get("language_family", row["language"]),
            "language_label": row.get("language_label", row["language"]),
            "baseline_delta": float(row.get("overall_score", 0) or 0) - float(baseline.get("overall_score", 0) or 0),
        }
        for row in task_rows
    ]


def _task_raw_rows(medians: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in medians:
        grouped[row["task_id"]].append(row)
    output: dict[str, list[dict]] = {}
    for task_id, rows in grouped.items():
        output[task_id] = sorted(
            rows,
            key=lambda row: (
                _canonical_variant_order().index(row["language"]) if row["language"] in _canonical_variant_order() else 999,
                {"s": 0, "m": 1, "l": 2}.get(row["size"], 999),
            ),
        )
    return output


def _format_seconds(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 1000:.3f} ms" if value < 1.0 else f"{value:.4f} s"


def _format_memory(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value / 1024:.3f} GB" if value >= 1024.0 else f"{value:.3f} MB"


def _format_lines(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{int(value)}"


def _task_raw_table_html(rows: list[dict]) -> str:
    body = []
    for row in rows:
        body.append(
            "<tr>"
            f"<td>{escape(_display_label(row))}</td>"
            f"<td>{escape(row['size'].upper())}</td>"
            f"<td>{int(row.get('sample_count', 0) or 0)}</td>"
            f"<td>{escape(_format_seconds(row.get('cpu_seconds')))}</td>"
            f"<td>{escape(_format_seconds(row.get('cpu_stddev_seconds')))}</td>"
            f"<td>{escape(_format_seconds(row.get('cpu_ci95_seconds')))}</td>"
            f"<td>{escape(_format_seconds(row.get('cpu_min_seconds')))} → {escape(_format_seconds(row.get('cpu_max_seconds')))}</td>"
            f"<td>{escape(_format_seconds(row.get('wall_seconds')))}</td>"
            f"<td>{escape(_format_seconds(row.get('wall_stddev_seconds')))}</td>"
            f"<td>{escape(_format_seconds(row.get('wall_ci95_seconds')))}</td>"
            f"<td>{escape(_format_seconds(row.get('wall_min_seconds')))} → {escape(_format_seconds(row.get('wall_max_seconds')))}</td>"
            f"<td>{escape(_format_memory(row.get('max_rss_mb')))}</td>"
            f"<td>{escape(_format_memory(row.get('memory_stddev_mb')))}</td>"
            f"<td>{escape(_format_memory(row.get('memory_ci95_mb')))}</td>"
            f"<td>{escape(_format_memory(row.get('memory_min_mb')))} → {escape(_format_memory(row.get('memory_max_mb')))}</td>"
            f"<td>{escape(_format_lines(row.get('loc')))}</td>"
            "</tr>"
        )
    return (
        "<table>"
        "<thead><tr>"
        "<th>Language</th><th>Size</th><th>Samples</th>"
        "<th>CPU median</th><th>CPU σ</th><th>CPU ±95% CI</th><th>CPU range</th>"
        "<th>Wall median</th><th>Wall σ</th><th>Wall ±95% CI</th><th>Wall range</th>"
        "<th>Memory median</th><th>Memory σ</th><th>Memory ±95% CI</th><th>Memory range</th>"
        "<th>LOC</th>"
        "</tr></thead>"
        f"<tbody>{''.join(body)}</tbody>"
        "</table>"
    )


def _host_metadata_html(host: dict) -> str:
    if not host:
        return "<p>Host metadata was not available in this results file.</p>"
    rows = []
    labels = [
        ("hostname", "Hostname"),
        ("system", "System"),
        ("release", "Kernel / release"),
        ("platform", "Platform"),
        ("machine", "Machine"),
        ("architecture", "Normalized architecture"),
        ("cpu_model", "CPU model"),
        ("cpu_count", "CPU count"),
        ("python_version", "Python"),
        ("engine_binary", "Container engine"),
        ("engine_version", "Engine version"),
    ]
    for key, label in labels:
        value = host.get(key)
        if value in {None, ""}:
            continue
        rows.append(f"<tr><th>{escape(label)}</th><td>{escape(str(value))}</td></tr>")
    return f"<table><tbody>{''.join(rows)}</tbody></table>" if rows else "<p>Host metadata was not available in this results file.</p>"


def _runtime_matrix_html(runtimes: list[dict]) -> str:
    if not runtimes:
        return "<p>Runtime version metadata was not available in this results file.</p>"
    rows = []
    for row in runtimes:
        rows.append(
            "<tr>"
            f"<td>{escape(str(row.get('language_label') or row.get('language') or ''))}</td>"
            f"<td>{escape(str(row.get('language_family') or ''))}</td>"
            f"<td>{escape(str(row.get('architecture') or ''))}</td>"
            f"<td>{escape(str(row.get('configured_version') or ''))}</td>"
            f"<td>{escape(str(row.get('reported_version') or ''))}</td>"
            f"<td>{escape(_normalized_image_label(row.get('image') or ''))}</td>"
            "</tr>"
        )
    return (
        "<table><thead><tr>"
        "<th>Runtime</th><th>Family</th><th>Architecture</th><th>Configured version</th><th>Reported version</th><th>Image</th>"
        "</tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def _git_metadata_html(git: dict) -> str:
    if not git:
        return "<p>Git metadata was not available in this results file.</p>"
    rows = []
    for key, label in [("branch", "Branch"), ("commit", "Commit"), ("commit_short", "Short commit"), ("dirty", "Dirty working tree")]:
        value = git.get(key)
        if value in {None, ""}:
            continue
        rows.append(f"<tr><th>{escape(label)}</th><td>{escape(str(value))}</td></tr>")
    return f"<table><tbody>{''.join(rows)}</tbody></table>" if rows else "<p>Git metadata was not available in this results file.</p>"


def _metric_provenance_html() -> str:
    rows = [
        ("CPU / Wall / Memory / LOC", "Measured", "Directly measured from benchmark execution or LOC counting."),
        ("Scalability", "Derived", "Computed from S→M→L wall-time and memory growth ratios."),
        ("Community", "Derived", "Computed from checked-in contributor/update-cadence inputs."),
        ("Ease / Debugging / Docs / Libraries / Concurrency", "Rubric", "Checked-in rubric values with evidence and sources."),
        ("Objective / Opinionated / Overall", "Derived", "Recomputed aggregate scores built from the inputs above."),
    ]
    body = "".join(
        f"<tr><td>{escape(a)}</td><td><strong>{escape(b)}</strong></td><td>{escape(c)}</td></tr>"
        for a, b, c in rows
    )
    return "<table><thead><tr><th>Metric group</th><th>Type</th><th>Meaning</th></tr></thead><tbody>" + body + "</tbody></table>"


def _fixture_manifest_html(manifest: dict[str, dict[str, str]]) -> str:
    if not manifest:
        return "<p>Fixture-size metadata was not available in this results file.</p>"
    rows = []
    for task_id in sorted(manifest):
        rows.append(
            "<tr>"
            f"<td><code>{escape(task_id)}</code></td>"
            f"<td>{escape(manifest[task_id].get('s', 'n/a'))}</td>"
            f"<td>{escape(manifest[task_id].get('m', 'n/a'))}</td>"
            f"<td>{escape(manifest[task_id].get('l', 'n/a'))}</td>"
            "</tr>"
        )
    return "<table><thead><tr><th>Task</th><th>S</th><th>M</th><th>L</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>"


def _correctness_summary(rows_payload: list[dict]) -> dict:
    grouped: dict[tuple[str, str], set[str]] = defaultdict(set)
    languages: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in rows_payload:
        if row.get("status") != "ok":
            continue
        key = (row["task_id"], row["size"])
        grouped[key].add(str(row.get("stdout", "")))
        languages[key].add(str(row["language"]))
    mismatches = []
    for key, outputs in grouped.items():
        if len(outputs) > 1:
            mismatches.append({"task_id": key[0], "size": key[1], "output_count": len(outputs), "languages": len(languages[key])})
    return {"groups_checked": len(grouped), "mismatch_count": len(mismatches), "mismatches": mismatches}


def _correctness_digest_rows(rows_payload: list[dict]) -> list[dict]:
    grouped: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in rows_payload:
        if row.get("status") != "ok":
            continue
        grouped[(str(row.get("task_id")), str(row.get("size")))].add(str(row.get("stdout", "")))
    rows = []
    for (task_id, size), outputs in sorted(grouped.items()):
        canonical = sorted(outputs)[0] if outputs else ""
        digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:12] if canonical else ""
        preview = canonical.strip().replace("\n", "\\n")
        rows.append({
            "task_id": task_id,
            "size": size,
            "digest": digest,
            "distinct_outputs": len(outputs),
            "preview": preview[:64] + ("…" if len(preview) > 64 else ""),
        })
    return rows


def _correctness_summary_html(summary: dict) -> str:
    if summary.get("mismatch_count", 0) == 0:
        return f"<p><strong>0 mismatches</strong> across {summary.get('groups_checked', 0)} task/size groups.</p>"
    body = "".join(
        f"<tr><td><code>{escape(row['task_id'])}</code></td><td>{escape(str(row['size']).upper())}</td><td>{row['output_count']}</td><td>{row['languages']}</td></tr>"
        for row in summary.get("mismatches", [])
    )
    return "<table><thead><tr><th>Task</th><th>Size</th><th>Distinct outputs</th><th>Languages checked</th></tr></thead><tbody>" + body + "</tbody></table>"


def _correctness_digest_html(rows_payload: list[dict]) -> str:
    rows = _correctness_digest_rows(rows_payload)
    if not rows:
        return "<p>No successful outputs were available to build correctness digests.</p>"
    body = "".join(
        "<tr>"
        f"<td><code>{escape(row['task_id'])}</code></td>"
        f"<td>{escape(str(row['size']).upper())}</td>"
        f"<td><code>{escape(row['digest'])}</code></td>"
        f"<td>{row['distinct_outputs']}</td>"
        f"<td><code>{escape(row['preview'])}</code></td>"
        "</tr>"
        for row in rows
    )
    return "<table><thead><tr><th>Task</th><th>Size</th><th>Digest</th><th>Distinct outputs</th><th>Canonical output preview</th></tr></thead><tbody>" + body + "</tbody></table>"


def _expected_outputs_path() -> Path:
    return ROOT / "docs" / "expected-outputs.json"


def _expected_output_check_html(rows_payload: list[dict]) -> str:
    path = _expected_outputs_path()
    if not path.exists():
        return "<p>No checked-in expected-output manifest was available yet.</p>"
    manifest = read_json(path)
    expected = manifest.get("expected_outputs", {})
    current = {f"{row['task_id']}:{str(row['size']).lower()}": row for row in _correctness_digest_rows(rows_payload)}
    mismatches = []
    for key, row in current.items():
        want = expected.get(key)
        if not want:
            mismatches.append((key, row["digest"], "missing"))
        elif want.get("digest") != row["digest"]:
            mismatches.append((key, row["digest"], want.get("digest")))
    if not mismatches:
        return f"<p>All {len(current)} current task/size output digests matched the checked-in expected-output manifest.</p>"
    body = "".join(
        f"<tr><td><code>{escape(key)}</code></td><td><code>{escape(got)}</code></td><td><code>{escape(want)}</code></td></tr>"
        for key, got, want in mismatches
    )
    return "<table><thead><tr><th>Task/size</th><th>Current digest</th><th>Expected digest</th></tr></thead><tbody>" + body + "</tbody></table>"


def _source_provenance_html(source_notes: dict) -> str:
    rows = ["<table><thead><tr><th>Published view</th><th>Source artifact</th></tr></thead><tbody>"]
    rows.append("<tr><td>Canonical README/report snapshot</td><td>Current scored artifact</td></tr>")
    for label, key in [
        ("Version-matrix supplemental view", "version_matrix_source"),
        ("Runtime metadata source", "runtime_metadata_source"),
        ("JavaScript runtime comparison source", "javascript_runtime_source"),
    ]:
        if source_notes.get(key):
            rows.append(f"<tr><td>{label}</td><td><code>{escape(str(source_notes[key]))}</code></td></tr>")
    rows.append("</tbody></table>")
    return "".join(rows)


def _service_split_rows(medians: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in medians:
        if row.get("startup_wall_seconds") is not None or row.get("workload_wall_seconds") is not None:
            grouped[row["language"]].append(row)
    rows = []
    for language, bucket in grouped.items():
        startup = [float(row.get("startup_wall_seconds") or 0) for row in bucket if row.get("startup_wall_seconds") is not None]
        workload = [float(row.get("workload_wall_seconds") or 0) for row in bucket if row.get("workload_wall_seconds") is not None]
        rows.append({
            "language": language,
            "runtime_id": bucket[0].get("runtime_id", language),
            "architecture": bucket[0].get("architecture", "unknown"),
            "language_label": bucket[0].get("language_label", language),
            "service_task_count": len(bucket),
            "startup_wall_avg": sum(startup) / len(startup) if startup else 0.0,
            "startup_wall_avg_ci95": (1.96 * _stddev_list(startup) / (len(startup) ** 0.5)) if len(startup) > 1 else 0.0,
            "workload_wall_avg": sum(workload) / len(workload) if workload else 0.0,
            "workload_wall_avg_ci95": (1.96 * _stddev_list(workload) / (len(workload) ** 0.5)) if len(workload) > 1 else 0.0,
        })
    return _ordered_rows(rows)


def _service_split_table_html(rows: list[dict]) -> str:
    if not rows:
        return "<p>No startup/workload split timings were available in this results file.</p>"
    body = "".join(
        "<tr>"
        f"<td>{escape(_display_label(row))}</td>"
        f"<td>{int(row['service_task_count'])}</td>"
        f"<td>{escape(_format_seconds(row['startup_wall_avg']))}</td>"
        f"<td>{escape(_format_seconds(row['workload_wall_avg']))}</td>"
        f"<td>{escape(_format_seconds(row['startup_wall_avg'] + row['workload_wall_avg']))}</td>"
        "</tr>"
        for row in rows
    )
    return "<table><thead><tr><th>Runtime</th><th>Task/size medians used</th><th>Avg startup</th><th>Avg steady-state workload</th><th>Avg total</th></tr></thead><tbody>" + body + "</tbody></table>"


def _baseline_rows(aggregate: list[dict], raw_unit_rows: list[dict], baseline_runtime: str) -> list[dict]:
    aggregate_by_language = {row["language"]: row for row in aggregate}
    raw_by_language = {row["language"]: row for row in raw_unit_rows}
    config = load_app_config()
    baseline_family = config.language_variants.get(baseline_runtime, {}).get("family", baseline_runtime)
    baseline_agg = (
        aggregate_by_language.get(baseline_runtime)
        or next((row for row in aggregate if row.get("runtime_id") == baseline_runtime), None)
        or aggregate_by_language.get(baseline_family)
        or next((row for row in aggregate if row.get("language_family") == baseline_family), None)
    )
    baseline_raw = (
        raw_by_language.get(baseline_runtime)
        or next((row for row in raw_unit_rows if row.get("runtime_id") == baseline_runtime), None)
        or raw_by_language.get(baseline_family)
        or next((row for row in raw_unit_rows if row.get("language_family") == baseline_family), None)
    )
    if not baseline_agg or not baseline_raw:
        return []
    rows = []
    for language, row in aggregate_by_language.items():
        raw = raw_by_language.get(language)
        if not raw:
            continue
        rows.append({
            "language": language,
            "language_label": row.get("language_label", language),
            "cpu_ratio_vs_baseline": float(raw.get("cpu_seconds_total", 0) or 0) / max(float(baseline_raw.get("cpu_seconds_total", 0) or 0), 1e-9),
            "wall_ratio_vs_baseline": float(raw.get("wall_seconds_total", 0) or 0) / max(float(baseline_raw.get("wall_seconds_total", 0) or 0), 1e-9),
            "memory_ratio_vs_baseline": float(raw.get("memory_mb_avg", 0) or 0) / max(float(baseline_raw.get("memory_mb_avg", 0) or 0), 1e-9),
            "overall_delta_vs_baseline": float(row.get("overall_score", 0) or 0) - float(baseline_agg.get("overall_score", 0) or 0),
        })
    return rows


def _baseline_table_html(rows: list[dict], baseline_runtime: str) -> str:
    if not rows:
        return f"<p>Configured baseline runtime <code>{escape(baseline_runtime)}</code> was not present in this artifact.</p>"
    body = "".join(
        "<tr>"
        f"<td>{escape(_display_label(row))}</td>"
        f"<td>{row['cpu_ratio_vs_baseline']:.2f}x</td>"
        f"<td>{row['wall_ratio_vs_baseline']:.2f}x</td>"
        f"<td>{row['memory_ratio_vs_baseline']:.2f}x</td>"
        f"<td>{row['overall_delta_vs_baseline']:+.2f}</td>"
        "</tr>"
        for row in rows
    )
    return "<table><thead><tr><th>Runtime</th><th>CPU vs baseline</th><th>Wall vs baseline</th><th>Memory vs baseline</th><th>Overall Δ vs baseline</th></tr></thead><tbody>" + body + "</tbody></table>"


def _load_publish_history() -> list[dict]:
    history_dir = ROOT / "docs" / "publish-history"
    if not history_dir.exists():
        return []
    rows_by_run_id: dict[str, dict] = {}
    for path in sorted(history_dir.glob("*.json")):
        manifest = read_json(path)
        canonical = manifest.get("canonical_results")
        if not canonical:
            continue
        results_path = ROOT / str(canonical)
        if not results_path.exists():
            continue
        payload = read_json(results_path)
        run_id = str(payload.get("run_id") or manifest.get("generated_run_id") or path.stem)
        if run_id in rows_by_run_id:
            continue
        rows_by_run_id[run_id] = {
            "run_id": run_id,
            "aggregate": payload.get("aggregate", []),
        }
    return [rows_by_run_id[key] for key in sorted(rows_by_run_id)]


def _history_table_html(history_rows: list[dict]) -> str:
    if not history_rows:
        return "<p>No archived publish-history snapshots were available yet.</p>"
    body = []
    for item in history_rows:
        aggregate = item.get("aggregate", [])
        top = max(aggregate, key=lambda row: float(row.get("overall_score", 0) or 0), default=None)
        top_label = escape(_display_label(top)) if top else "n/a"
        top_score = f"{float(top.get('overall_score', 0) or 0):.2f}" if top else "n/a"
        body.append(
            "<tr>"
            f"<td><code>{escape(str(item.get('run_id')))}</code></td>"
            f"<td>{top_label}</td>"
            f"<td>{top_score}</td>"
            f"<td>{len(aggregate)}</td>"
            "</tr>"
        )
    return "<table><thead><tr><th>Run ID</th><th>Top overall runtime</th><th>Top score</th><th>Runtime rows</th></tr></thead><tbody>" + "".join(body) + "</tbody></table>"


def _load_version_matrix_history() -> list[dict]:
    history_dir = ROOT / "docs" / "publish-history"
    if not history_dir.exists():
        return []
    rows_by_run_id: dict[str, dict] = {}
    for path in sorted(history_dir.glob("*.json")):
        manifest = read_json(path)
        version_matrix = manifest.get("version_matrix_results")
        if not version_matrix:
            continue
        results_path = ROOT / str(version_matrix)
        if not results_path.exists():
            continue
        payload = read_json(results_path)
        run_id = str(payload.get("run_id") or path.stem)
        if run_id in rows_by_run_id:
            continue
        rows_by_run_id[run_id] = {
            "run_id": run_id,
            "aggregate": payload.get("aggregate", []),
        }
    return [rows_by_run_id[key] for key in sorted(rows_by_run_id)]


def _category_sections(rows_payload: list[dict], weights: dict[str, float]) -> list[dict]:
    catalog = {task.id: task for task in load_catalog()}
    snapshot_task_ids = {str(row.get("task_id")) for row in rows_payload if row.get("task_id")}
    sections = []
    seen = set()
    for tag in ["compute", "service", "ui", "integration", "io", "ml", "networking"]:
        task_ids = {
            task_id for task_id, task in catalog.items()
            if tag in set((getattr(task, "tags", []) or []) + [task.kind])
        } & snapshot_task_ids
        if not task_ids or tag in seen:
            continue
        _medians, aggregate = aggregate_for_task_ids(rows_payload, weights, task_ids)
        if aggregate:
            sections.append({"tag": tag, "task_ids": sorted(task_ids), "aggregate": aggregate})
            seen.add(tag)
    return sections


def _blended_category_rows(aggregate: list[dict], category_rows: dict[str, list[dict]]) -> list[dict]:
    objective_by_language = {str(row["language"]): row for row in category_rows.get("objective", [])}
    opinionated_by_language = {str(row["language"]): row for row in category_rows.get("opinionated", [])}
    rows = []
    for row in aggregate:
        language = str(row.get("language"))
        objective = objective_by_language.get(language, {})
        opinionated = opinionated_by_language.get(language, {})
        rows.append({
            "language": language,
            "language_label": row.get("language_label", language),
            "overall_score": float(row.get("overall_score", 0) or 0),
            "objective_score": float(objective.get("objective_score", 0) or 0),
            "opinionated_score": float(opinionated.get("opinionated_score", 0) or 0),
            "tasks_covered": row.get("tasks_covered", 0),
        })
    return sorted(rows, key=lambda item: item["overall_score"], reverse=True)


def _category_sections_html(rows_payload: list[dict], weights: dict[str, float]) -> str:
    sections = _category_sections(rows_payload, weights)
    if not sections:
        return "<p>No category leaderboards were available.</p>"
    parts = []
    for section in sections:
        category_rows = split_aggregate_scores(section["aggregate"], weights)
        blended_body = "".join(
            f"<tr><td>{escape(_display_label(row))}</td><td>{row['overall_score']:.2f}</td><td>{row['objective_score']:.2f}</td><td>{row['opinionated_score']:.2f}</td><td>{row['tasks_covered']}</td></tr>"
            for row in _blended_category_rows(section["aggregate"], category_rows)
        )
        objective_body = "".join(
            f"<tr><td>{escape(_display_label(row))}</td><td>{row['objective_score']:.2f}</td><td>{row['cpu_score']:.2f}</td><td>{row['wall_score']:.2f}</td><td>{row['memory_score']:.2f}</td><td>{row['loc_score']:.2f}</td><td>{row['tasks_covered']}</td></tr>"
            for row in category_rows["objective"]
        )
        opinionated_body = "".join(
            f"<tr><td>{escape(_display_label(row))}</td><td>{row['opinionated_score']:.2f}</td><td>{row['scalability_score']:.2f}</td><td>{row['ease_score']:.2f}</td><td>{row['community_score']:.2f}</td><td>{row['debugging_score']:.2f}</td><td>{row['docs_score']:.2f}</td><td>{row['libraries_score']:.2f}</td><td>{row['concurrency_score']:.2f}</td><td>{row['tasks_covered']}</td></tr>"
            for row in category_rows["opinionated"]
        )
        parts.append(
            f"<h3><code>{escape(section['tag'])}</code></h3>"
            f"<p>Tasks: {' '.join(f'<code>{escape(task_id)}</code>' for task_id in section['task_ids'])}</p>"
            "<table><thead><tr><th>Runtime</th><th>Overall</th><th>Objective</th><th>Opinionated</th><th>Tasks</th></tr></thead><tbody>"
            + blended_body +
            "</tbody></table>"
            "<table><thead><tr><th>Runtime</th><th>Objective</th><th>CPU</th><th>Wall</th><th>Memory</th><th>LOC</th><th>Tasks</th></tr></thead><tbody>"
            + objective_body +
            "</tbody></table>"
            "<table><thead><tr><th>Runtime</th><th>Opinionated</th><th>Scalability</th><th>Ease</th><th>Community</th><th>Debugging</th><th>Docs</th><th>Libraries</th><th>Concurrency</th><th>Tasks</th></tr></thead><tbody>"
            + opinionated_body +
            "</tbody></table>"
        )
    return "".join(parts)


def _normalized_image_label(image: object) -> str:
    return str(image or "").replace("multi-benchmark:", "languages-benchmark:")


def _publish_manifest_path() -> Path:
    return ROOT / "docs" / "publish-manifest.json"


def _load_previous_publish_manifest() -> dict | None:
    path = _publish_manifest_path()
    if not path.exists():
        return None
    return read_json(path)


def _regression_summary_rows(aggregate: list[dict], current_weights: dict[str, float], previous_manifest: dict | None) -> list[dict]:
    if not previous_manifest:
        return []
    previous_path = previous_manifest.get("canonical_results")
    if not previous_path:
        return []
    previous_file = (ROOT / str(previous_path)).resolve()
    if not previous_file.exists():
        return []
    previous_payload = read_json(previous_file)
    if previous_payload.get("aggregate") == aggregate:
        return []
    current_by_language = {row["language"]: row for row in aggregate}
    previous_by_language = {row["language"]: row for row in previous_payload.get("aggregate", [])}
    if not current_by_language or not previous_by_language:
        return []
    current_split = split_aggregate_scores(aggregate, current_weights) if current_weights else {"objective": [], "opinionated": []}
    previous_split = split_aggregate_scores(previous_payload.get("aggregate", []), previous_payload.get("weights") or current_weights) if previous_payload.get("aggregate") else {"objective": [], "opinionated": []}
    current_objective = {row["language"]: row for row in current_split["objective"]}
    current_opinionated = {row["language"]: row for row in current_split["opinionated"]}
    previous_objective = {row["language"]: row for row in previous_split["objective"]}
    previous_opinionated = {row["language"]: row for row in previous_split["opinionated"]}
    rows = []
    for language in sorted(set(current_by_language) & set(previous_by_language)):
        if language not in current_objective or language not in previous_objective or language not in current_opinionated or language not in previous_opinionated:
            continue
        rows.append({
            "language": language,
            "language_label": current_by_language[language].get("language_label", language),
            "overall_delta": float(current_by_language[language].get("overall_score", 0) or 0) - float(previous_by_language[language].get("overall_score", 0) or 0),
            "objective_delta": float(current_objective[language].get("objective_score", 0) or 0) - float(previous_objective[language].get("objective_score", 0) or 0),
            "opinionated_delta": float(current_opinionated[language].get("opinionated_score", 0) or 0) - float(previous_opinionated[language].get("opinionated_score", 0) or 0),
        })
    return rows


def _regression_summary_html(aggregate: list[dict], current_weights: dict[str, float], previous_manifest: dict | None) -> str:
    rows = _regression_summary_rows(aggregate, current_weights, previous_manifest)
    if not previous_manifest:
        return "<p>No previous publish manifest was available, so no regression baseline could be computed yet.</p>"
    if not rows:
        return "<p>No earlier comparable published snapshot was available for regression comparison.</p>"
    body = "".join(
        "<tr>"
        f"<td>{escape(_display_label(row))}</td>"
        f"<td>{row['overall_delta']:+.2f}</td>"
        f"<td>{row['objective_delta']:+.2f}</td>"
        f"<td>{row['opinionated_delta']:+.2f}</td>"
        "</tr>"
        for row in rows
    )
    return "<table><thead><tr><th>Runtime</th><th>Overall Δ</th><th>Objective Δ</th><th>Opinionated Δ</th></tr></thead><tbody>" + body + "</tbody></table>"


def _html_page(
    aggregate: list[dict],
    raw_unit_rows: list[dict],
    task_rows: dict[str, list[dict]],
    category_rows: dict[str, list[dict]],
    medians: list[dict],
    rows_payload: list[dict],
    host: dict,
    git: dict,
    runtimes: list[dict],
    fixture_sizes: dict[str, dict[str, str]],
    weights: dict[str, float],
    profile: dict,
    baseline_rows: list[dict],
    history_rows: list[dict],
    version_history_rows: list[dict],
    source_notes: dict,
    previous_manifest: dict | None,
) -> str:
    rows = "\n".join(
        f"<tr><td>{escape(_display_label(row))}</td><td>{row['overall_score']}</td><td>{row['cpu_score']}</td><td>{row['wall_score']}</td><td>{row['memory_score']}</td><td>{row['tasks_covered']}</td><td>{row['skipped_tasks']}</td></tr>"
        for row in aggregate
    )
    task_raw_rows = _task_raw_rows(medians)
    task_sections = []
    for task_id in sorted(task_rows):
        task_name = _task_names().get(task_id, task_id)
        task_meta = next((task for task in load_catalog() if task.id == task_id), None)
        task_tags = ", ".join(getattr(task_meta, "tags", []) or [])
        task_sections.append(
            f"""
  <details>
    <summary><strong>{escape(task_id)}</strong> — {escape(task_name)}</summary>
    <p>First: every tested runtime variant ranked best-to-worst for this task. Second: the same plot in canonical runtime order. Third and fourth: the language best-case view for this task. Fifth: per-task delta against the configured baseline runtime.</p>
    <p><strong>Tags:</strong> {escape(task_tags or 'n/a')}</p>
    <div class='charts'>
      <iframe src='task_{escape(task_id)}_ranked.svg'></iframe>
      <iframe src='task_{escape(task_id)}.svg'></iframe>
      <iframe src='best_case_task_{escape(task_id)}_ranked.svg'></iframe>
      <iframe src='best_case_task_{escape(task_id)}.svg'></iframe>
      <iframe src='task_baseline_{escape(task_id)}_ranked.svg'></iframe>
    </div>
    <p><strong>Raw numeric table:</strong> per-language, per-size medians with variance and range from the measured iterations.</p>
    {_task_raw_table_html(task_raw_rows.get(task_id, []))}
  </details>
""".rstrip()
        )
    canonical_order = ", ".join(_canonical_language_order())
    canonical_variant_order = ", ".join(_canonical_variant_order())
    config = load_app_config()
    baseline_runtime = str(profile.get("baseline_runtime") or config.baseline_runtime)
    effective_profile = {
        "preset": profile.get("preset") or "manual / inherited",
        "iterations": profile.get("iterations") or config.iterations,
        "warmups": profile.get("warmups") or config.warmups,
        "jobs": profile.get("jobs") or 1,
        "architectures": profile.get("architectures") or config.architectures,
        "baseline_runtime": baseline_runtime,
    }
    version_history_iframe = "<iframe src='history_version_matrix_overall.svg'></iframe>" if len(version_history_rows) >= 2 else ""
    per_version_methodology_html = ""
    if source_notes.get("version_matrix_source") or source_notes.get("runtime_metadata_source"):
        per_version_methodology_html = """
  <h2>Per-version methodology notes</h2>
  <ul class='caption-list'>
    <li><strong>Measured at runtime-version level:</strong> CPU, wall time, memory, LOC, startup split, workload split, correctness outputs, and scalability growth inputs.</li>
    <li><strong>Rubric handling:</strong> runtime variants can now override family-level rubric values for ease/debugging/docs/libraries/concurrency; untouched variants still inherit the family default.</li>
    <li><strong>Community handling:</strong> community inputs still attach to the language family, so variants inside one family still share that part of the interpretive model.</li>
    <li><strong>Best comparison for runtime variants:</strong> objective raw-unit plots, objective score plots, startup/workload split tables, and correctness summaries.</li>
  </ul>
""".rstrip()
    baseline_section = f"""
  <h2>Baseline-relative comparison</h2>
  <p>These views compare every runtime to the configured baseline runtime <code>{escape(baseline_runtime)}</code>.</p>
  {_baseline_table_html(baseline_rows, baseline_runtime)}
  <div class='charts'>
    <iframe src='baseline_cpu_ratio_ranked.svg'></iframe>
    <iframe src='baseline_wall_ratio_ranked.svg'></iframe>
    <iframe src='baseline_memory_ratio_ranked.svg'></iframe>
    <iframe src='baseline_overall_delta_ranked.svg'></iframe>
  </div>
""".rstrip()
    history_section = (
        f"""
  <h2>Historical publish trends</h2>
  {_history_table_html(history_rows)}
  <div class='charts'>
    <iframe src='history_overall.svg'></iframe>
    {version_history_iframe}
  </div>
""".rstrip()
        if history_rows or len(version_history_rows) >= 2 else
        """
  <h2>Historical publish trends</h2>
  <p>No archived publish-history snapshots were available yet.</p>
""".rstrip()
    )
    return f"""
<!doctype html>
<html>
<head>
  <meta charset='utf-8'/>
  <title>languages-benchmark report</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 2rem; line-height: 1.5; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
    th {{ background: #f3f4f6; }}
    .charts {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem; }}
    iframe {{ width: 100%; height: 560px; border: none; background: #fff; }}
    .note {{ background: #f8fafc; border-left: 4px solid #4f46e5; padding: 0.75rem 1rem; margin: 1rem 0 1.5rem; }}
    .caption-list li {{ margin-bottom: 0.35rem; }}
    code {{ background: #f3f4f6; padding: 0.15rem 0.35rem; border-radius: 4px; }}
    details {{ margin: 1rem 0 1.25rem; padding: 0.5rem 0; }}
    summary {{ cursor: pointer; font-size: 1.05rem; }}
    input[type='search'] {{ padding: 0.4rem 0.6rem; min-width: 280px; margin: 0.5rem 0 1rem; }}
  </style>
</head>
<body>
  <h1>languages-benchmark report</h1>
  <div class='note'>
    <strong>How to read these plots:</strong><br/>
    This report now separates <strong>per-version charts</strong> from <strong>language best-case charts</strong>, and also separates <strong>raw-unit charts</strong> from <strong>normalized score charts</strong>. When a real unit exists, the report uses it directly: CPU and wall time are shown in seconds or milliseconds, memory is shown in MB or GB, and LOC is shown as raw line counts. Normalized 0-to-100 scoring is still used for dimensions without a clean real-world unit, such as overall composite score or scalability behavior.
  </div>
  <h2>Size legend</h2>
  <ul class='caption-list'>
    <li><strong>S</strong> = small input</li>
    <li><strong>M</strong> = medium input</li>
    <li><strong>L</strong> = large input</li>
    <li>These are deterministic fixture sizes defined per task, so they do not represent one universal row-count or byte-size across the entire suite.</li>
  </ul>
  <h2>Host / environment</h2>
  <p>This benchmark captures host metadata with each run so raw results can be interpreted in context.</p>
  {_host_metadata_html(host)}
  <h2>Git / publish identity</h2>
  {_git_metadata_html(git)}
  <h2>Publish profile</h2>
  <p>Canonical published runs should stay sequential by default even though the runner supports <code>--jobs N</code> for faster local experimentation.</p>
  <table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody>
    <tr><td>Preset</td><td>{escape(str(effective_profile.get("preset")))}</td></tr>
    <tr><td>Iterations</td><td>{escape(str(effective_profile.get("iterations")))}</td></tr>
    <tr><td>Warmups</td><td>{escape(str(effective_profile.get("warmups")))}</td></tr>
    <tr><td>Jobs</td><td>{escape(str(effective_profile.get("jobs")))}</td></tr>
    <tr><td>Architectures</td><td>{escape(', '.join(effective_profile.get("architectures") or []))}</td></tr>
    <tr><td>Baseline runtime</td><td>{escape(str(effective_profile.get("baseline_runtime")))}</td></tr>
  </tbody></table>
  <h2>Regression vs previous published snapshot</h2>
  {_regression_summary_html(aggregate, weights, previous_manifest)}
  <h2>Tested runtime versions</h2>
  <p>Each benchmark run records the configured/reported runtime version and CPU architecture for every tested runtime variant. Runtime identity is architecture-aware, so future ARM, RISC-V, or other host runs can be added without collapsing them into the current architecture's results.</p>
  {_runtime_matrix_html(runtimes)}
  <ul class='caption-list'>
    <li><strong>Per-version charts:</strong> one bar per tested runtime variant, such as PHP 5.6 vs PHP 8.4.</li>
    <li><strong>Language best-case charts:</strong> collapse all tested versions of a language down to the best-performing version for that metric.</li>
    <li><strong>Raw-unit charts:</strong> lower is better for CPU time, wall time, memory, and LOC.</li>
    <li><strong>Objective score:</strong> recomputed only from directly measured CPU, wall, memory, and LOC metrics.</li>
    <li><strong>Opinionated score:</strong> recomputed only from scalability and rubric/community-style metrics.</li>
    <li><strong>Overall:</strong> weighted composite score; higher is better.</li>
    <li><strong>CPU:</strong> lower raw CPU time becomes a higher score.</li>
    <li><strong>Wall:</strong> lower raw elapsed time becomes a higher score.</li>
    <li><strong>Memory:</strong> lower raw max RSS becomes a higher score.</li>
    <li><strong>Scalability:</strong> higher means the language degrades more gracefully as input size increases.</li>
  </ul>
  <h2>Metric provenance</h2>
  {_metric_provenance_html()}
  <h2>Methodology for non-objective and derived criteria</h2>
  <p>This benchmark separates objective/measured inputs from derived and interpretive inputs.</p>
  <ul class='caption-list'>
    <li><strong>Objective inputs:</strong> CPU time, wall time, memory, and LOC are measured directly. Lower-is-better metrics are normalized as <code>100 * best / candidate</code>.</li>
    <li><strong>Scalability:</strong> derived per language/task from size growth, not taken from one direct measurement.</li>
  </ul>
  <p>For each language/task pair with S, M, and L:</p>
  <ul class='caption-list'>
    <li><code>wall_growth = ((M_wall / S_wall) + (L_wall / M_wall)) / 2</code></li>
    <li><code>memory_growth = ((M_mem / S_mem) + (L_mem / M_mem)) / 2</code></li>
    <li><code>raw_scalability = (wall_growth + memory_growth) / 2</code></li>
    <li><code>scalability_score = 100 * best_raw_scalability / candidate_raw_scalability</code></li>
  </ul>
  <p>So a higher scalability score means lower growth after inversion and normalization.</p>
  <ul class='caption-list'>
    <li><strong>Ease, debugging, docs, libraries, concurrency:</strong> audited rubric scores from <code>rubrics.yaml</code>.</li>
    <li><strong>Community:</strong> derived from <code>community.yaml</code> as the average of <code>active_contributors</code> and <code>update_cadence</code>.</li>
    <li><strong>Higher-is-better interpretive metrics:</strong> normalized as <code>100 * candidate / best</code>.</li>
    <li><strong>Objective score:</strong> recomputed using only CPU, wall, memory, and LOC, with weights renormalized inside that subset.</li>
    <li><strong>Opinionated score:</strong> recomputed using scalability, ease, community, debugging, docs, libraries, and concurrency, with weights renormalized inside that subset.</li>
    <li><strong>Overall score:</strong> blended from both groups with the weights in <code>weights.default.yaml</code>.</li>
  </ul>
  {per_version_methodology_html}
  <h2>Fixture sizes by task</h2>
  {_fixture_manifest_html(fixture_sizes)}
  <h2>Correctness verification summary</h2>
  {_correctness_summary_html(_correctness_summary(rows_payload))}
  <h2>Expected-output manifest check</h2>
  {_expected_output_check_html(rows_payload)}
  <h2>Correctness digests</h2>
  <p>These short hashes let readers compare the canonical successful output fingerprint for each task/size without opening the raw JSON artifact.</p>
  {_correctness_digest_html(rows_payload)}
  <h2>Service and UI startup vs steady-state</h2>
  {_service_split_table_html(_service_split_rows(medians))}
  <div class='charts'>
    <iframe src='startup_units_ranked.svg'></iframe>
    <iframe src='workload_units_ranked.svg'></iframe>
  </div>
  <h2>Machine-readable publish manifest</h2>
  <p>The README publication flow writes a machine-readable manifest to <code>docs/publish-manifest.json</code> so the published snapshot can be audited later.</p>
  <h2>Artifact/source provenance</h2>
  {_source_provenance_html(source_notes)}
  {baseline_section}
  {history_section}
  <h2>Category leaderboards</h2>
  <p>These recompute the benchmark across tagged subsets of tasks so you can inspect category-specific leaders instead of only the global aggregate.</p>
  {_category_sections_html(rows_payload, weights)}
  <h2>Raw-unit plots for this published snapshot</h2>
  <p>These charts use real units wherever possible and show exactly the runtimes present in this published artifact. CPU and wall time are shown as total median time across the snapshot, memory is shown as average median peak RSS, and LOC is shown as average lines per task.</p>
  <div class='charts'>
    <iframe src='cpu_units_ranked.svg'></iframe>
    <iframe src='wall_units_ranked.svg'></iframe>
    <iframe src='memory_units_ranked.svg'></iframe>
    <iframe src='loc_units_ranked.svg'></iframe>
    <iframe src='cpu_units.svg'></iframe>
    <iframe src='wall_units.svg'></iframe>
    <iframe src='memory_units.svg'></iframe>
    <iframe src='loc_units.svg'></iframe>
  </div>
  <h2>Language best-case raw-unit plots</h2>
  <p>These charts collapse the runtime variants and keep only the best measured version for each language family for the metric being plotted.</p>
  <div class='charts'>
    <iframe src='best_case_cpu_units_ranked.svg'></iframe>
    <iframe src='best_case_wall_units_ranked.svg'></iframe>
    <iframe src='best_case_memory_units_ranked.svg'></iframe>
    <iframe src='best_case_loc_units_ranked.svg'></iframe>
    <iframe src='best_case_cpu_units.svg'></iframe>
    <iframe src='best_case_wall_units.svg'></iframe>
    <iframe src='best_case_memory_units.svg'></iframe>
    <iframe src='best_case_loc_units.svg'></iframe>
  </div>
  <h2>Objective / unopinionated score plots</h2>
  <p>These recomputed metrics keep only directly measurable benchmark dimensions: CPU time, wall time, memory, and LOC. This removes scalability and rubric/community-driven components.</p>
  <div class='charts'>
    <iframe src='objective_ranked.svg'></iframe>
    <iframe src='objective.svg'></iframe>
    <iframe src='cpu_ranked.svg'></iframe>
    <iframe src='wall_ranked.svg'></iframe>
    <iframe src='memory_ranked.svg'></iframe>
    <iframe src='loc_ranked.svg'></iframe>
  </div>
  <h2>Language best-case objective plots</h2>
  <div class='charts'>
    <iframe src='best_case_objective_ranked.svg'></iframe>
    <iframe src='best_case_objective.svg'></iframe>
    <iframe src='best_case_cpu_ranked.svg'></iframe>
    <iframe src='best_case_wall_ranked.svg'></iframe>
    <iframe src='best_case_memory_ranked.svg'></iframe>
    <iframe src='best_case_loc_ranked.svg'></iframe>
  </div>
  <h2>Geometric-mean runtime views</h2>
  <p>These reduce the influence of extreme outliers by taking the geometric mean of normalized per-task/per-size runtime efficiency ratios.</p>
  <div class='charts'>
    <iframe src='cpu_geomean_ranked.svg'></iframe>
    <iframe src='wall_geomean_ranked.svg'></iframe>
    <iframe src='cpu_geomean.svg'></iframe>
    <iframe src='wall_geomean.svg'></iframe>
  </div>
  <h2>Variance / confidence summary</h2>
  <p>Lower values are better here: they indicate less relative run-to-run variation across the measured benchmark medians.</p>
  <div class='charts'>
    <iframe src='variance_cpu_ranked.svg'></iframe>
    <iframe src='variance_wall_ranked.svg'></iframe>
    <iframe src='variance_memory_ranked.svg'></iframe>
    <iframe src='variance_cpu.svg'></iframe>
    <iframe src='variance_wall.svg'></iframe>
    <iframe src='variance_memory.svg'></iframe>
  </div>
  <h2>Opinionated score plots</h2>
  <p>These recomputed metrics keep only interpretive or hybrid dimensions: scalability, ease, community support, debugging, docs, libraries, and concurrency support.</p>
  <div class='charts'>
    <iframe src='opinionated_ranked.svg'></iframe>
    <iframe src='opinionated.svg'></iframe>
    <iframe src='scalability_ranked.svg'></iframe>
    <iframe src='scalability.svg'></iframe>
  </div>
  <h2>Language best-case opinionated plots</h2>
  <div class='charts'>
    <iframe src='best_case_opinionated_ranked.svg'></iframe>
    <iframe src='best_case_opinionated.svg'></iframe>
    <iframe src='best_case_scalability_ranked.svg'></iframe>
    <iframe src='best_case_scalability.svg'></iframe>
  </div>
  <h2>Ranked plots</h2>
  <p>These use the same metrics, but each chart sorts languages from best to worst for that specific metric.</p>
  <div class='charts'>
    <iframe src='overall_ranked.svg'></iframe>
    <iframe src='cpu_ranked.svg'></iframe>
    <iframe src='wall_ranked.svg'></iframe>
    <iframe src='memory_ranked.svg'></iframe>
    <iframe src='scalability_ranked.svg'></iframe>
  </div>
  <h2>Canonical-order plots</h2>
  <p>These preserve the benchmark's fixed runtime-variant order from <code>benchmark.yaml</code>: {escape(canonical_variant_order)}.</p>
  <div class='charts'>
    <iframe src='overall.svg'></iframe>
    <iframe src='cpu.svg'></iframe>
    <iframe src='wall.svg'></iframe>
    <iframe src='memory.svg'></iframe>
    <iframe src='scalability.svg'></iframe>
  </div>
  <h2>Scalability growth curves</h2>
  <p>The old flat “scalability curves” were not very informative because they were based on a per-task score that did not change across S/M/L. These updated charts now plot the actual average size-growth ratios derived from median wall time and memory. In all of these charts, lower is better.</p>
  <div class='charts'>
    <iframe src='scalability_curve.svg'></iframe>
    <iframe src='scalability_curve_ranked.svg'></iframe>
    <iframe src='scalability_memory_curve.svg'></iframe>
    <iframe src='scalability_memory_curve_ranked.svg'></iframe>
    <iframe src='scalability_growth_ratios.svg'></iframe>
    <iframe src='scalability_growth_ratios_ranked.svg'></iframe>
  </div>
  <h2>Per-task score plots</h2>
  <p>These task sections avoid hiding the benchmark behind only one global aggregate. Each task is plotted on its own for every tested runtime variant, then again as a language best-case view, followed by a raw numeric table with medians, variance, and ranges.</p>
  {"".join(task_sections)}
  <h2>Leaderboard</h2>
  <input id='leaderboard-filter' type='search' placeholder='Filter leaderboard rows...'/>
  <table id='leaderboard-table' data-sortable='true' data-filterable='true'>
    <thead><tr><th>Language</th><th>Overall</th><th>CPU</th><th>Wall</th><th>Memory</th><th>Covered tasks</th><th>Skipped</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <h2>What this benchmark is not</h2>
  <ul class='caption-list'>
    <li>It is not a universal truth about a language; it is a comparison across this repository's fixed workload mix.</li>
    <li>It is not using every ecosystem's most highly optimized specialist library for every task.</li>
    <li>It is not a substitute for benchmarking your own production workload on your own hardware.</li>
  </ul>
  <script>
    (() => {{
      const parseValue = (text) => {{
        const cleaned = text.replace(/,/g, '').trim();
        const n = Number(cleaned.replace(/[^0-9+\\-.]/g, ''));
        return Number.isFinite(n) ? n : cleaned.toLowerCase();
      }};
      document.querySelectorAll('table').forEach((table) => {{
        const headers = table.querySelectorAll('thead th');
        headers.forEach((th, index) => {{
          th.style.cursor = 'pointer';
          th.addEventListener('click', () => {{
            const tbody = table.querySelector('tbody');
            if (!tbody) return;
            const rows = Array.from(tbody.querySelectorAll('tr'));
            const current = th.dataset.sortDir === 'asc' ? 'desc' : 'asc';
            headers.forEach((h) => delete h.dataset.sortDir);
            th.dataset.sortDir = current;
            rows.sort((a, b) => {{
              const av = parseValue(a.children[index]?.textContent || '');
              const bv = parseValue(b.children[index]?.textContent || '');
              if (av < bv) return current === 'asc' ? -1 : 1;
              if (av > bv) return current === 'asc' ? 1 : -1;
              return 0;
            }});
            rows.forEach((row) => tbody.appendChild(row));
          }});
        }});
      }});
      const filter = document.getElementById('leaderboard-filter');
      const table = document.getElementById('leaderboard-table');
      if (filter && table) {{
        filter.addEventListener('input', () => {{
          const term = filter.value.trim().toLowerCase();
          table.querySelectorAll('tbody tr').forEach((row) => {{
            row.style.display = row.textContent.toLowerCase().includes(term) ? '' : 'none';
          }});
        }});
      }}
    }})();
  </script>
</body>
</html>
""".strip()
