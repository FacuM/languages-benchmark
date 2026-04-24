from __future__ import annotations

from collections import defaultdict
from math import exp, log
from statistics import median, pstdev

from runner.models import ScoredLanguage

EPSILON = 1e-9

OBJECTIVE_METRICS = [
    ("cpu_score", "cpu"),
    ("wall_score", "wall"),
    ("memory_score", "memory"),
    ("loc_score", "loc"),
]

OPINIONATED_METRICS = [
    ("scalability_score", "scalability"),
    ("ease_score", "ease"),
    ("community_score", "community"),
    ("debugging_score", "debugging"),
    ("docs_score", "docs"),
    ("libraries_score", "libraries"),
    ("concurrency_score", "concurrency"),
]


def score_results(rows: list[dict], weights: dict[str, float]) -> tuple[list[dict], list[dict]]:
    completed = [r for r in rows if r.get("status") == "ok"]
    by_lang_task_size: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for row in completed:
        by_lang_task_size[(row["language"], row["task_id"], row["size"])].append(row)

    medians = []
    for (language, task_id, size), bucket in sorted(by_lang_task_size.items()):
        cpu_values = [x["cpu_seconds"] for x in bucket if x["cpu_seconds"] is not None]
        wall_values = [x["wall_seconds"] for x in bucket if x["wall_seconds"] is not None]
        startup_values = [x["startup_wall_seconds"] for x in bucket if x.get("startup_wall_seconds") is not None]
        workload_values = [x["workload_wall_seconds"] for x in bucket if x.get("workload_wall_seconds") is not None]
        memory_values = [x["max_rss_mb"] for x in bucket if x["max_rss_mb"] is not None]
        medians.append({
            "language": language,
            "runtime_id": bucket[0].get("runtime_id", language),
            "architecture": bucket[0].get("architecture", "unknown"),
            "language_family": bucket[0].get("language_family", language),
            "language_label": bucket[0].get("language_label", language),
            "language_version": bucket[0].get("language_version"),
            "task_id": task_id,
            "size": size,
            "sample_count": len(bucket),
            "cpu_seconds": median(cpu_values),
            "cpu_min_seconds": min(cpu_values),
            "cpu_max_seconds": max(cpu_values),
            "cpu_stddev_seconds": _stddev(cpu_values),
            "cpu_ci95_seconds": _ci95(cpu_values),
            "wall_seconds": median(wall_values),
            "wall_min_seconds": min(wall_values),
            "wall_max_seconds": max(wall_values),
            "wall_stddev_seconds": _stddev(wall_values),
            "wall_ci95_seconds": _ci95(wall_values),
            "startup_wall_seconds": median(startup_values) if startup_values else None,
            "workload_wall_seconds": median(workload_values) if workload_values else None,
            "max_rss_mb": median(memory_values),
            "memory_min_mb": min(memory_values),
            "memory_max_mb": max(memory_values),
            "memory_stddev_mb": _stddev(memory_values),
            "memory_ci95_mb": _ci95(memory_values),
            "loc": median(x["loc"] for x in bucket if x["loc"] is not None),
            "ease_score": bucket[0]["ease_score"],
            "community_score": bucket[0]["community_score"],
            "debugging_score": bucket[0]["debugging_score"],
            "docs_score": bucket[0]["docs_score"],
            "libraries_score": bucket[0]["libraries_score"],
            "concurrency_score": bucket[0]["concurrency_score"],
        })

    scalability = _compute_scalability(medians)
    for row in medians:
        row["scalability_score"] = scalability.get((row["language"], row["task_id"]), 0.0)

    aggregate = _aggregate_language_scores(medians, rows, weights)
    return medians, aggregate


def aggregate_for_task_ids(rows: list[dict], weights: dict[str, float], task_ids: set[str]) -> tuple[list[dict], list[dict]]:
    filtered_rows = [row for row in rows if row.get("task_id") in task_ids]
    if not filtered_rows:
        return [], []
    return score_results(filtered_rows, weights)


def _compute_scalability(rows: list[dict]) -> dict[tuple[str, str], float]:
    grouped: dict[tuple[str, str], dict[str, dict]] = defaultdict(dict)
    for row in rows:
        grouped[(row["language"], row["task_id"])][row["size"]] = row
    raw = {}
    for key, sizes in grouped.items():
        if not {"s", "m", "l"}.issubset(sizes):
            raw[key] = 0.0
            continue
        s, m, l = sizes["s"], sizes["m"], sizes["l"]
        wall_growth = (_safe_div(m["wall_seconds"], s["wall_seconds"]) + _safe_div(l["wall_seconds"], m["wall_seconds"])) / 2.0
        mem_growth = (_safe_div(m["max_rss_mb"], s["max_rss_mb"]) + _safe_div(l["max_rss_mb"], m["max_rss_mb"])) / 2.0
        raw[key] = (wall_growth + mem_growth) / 2.0
    non_zero = [value for value in raw.values() if value > 0]
    if not non_zero:
        return {k: 0.0 for k in raw}
    best = min(non_zero)
    return {k: round(100.0 * best / v, 2) if v else 0.0 for k, v in raw.items()}


def _aggregate_language_scores(medians: list[dict], all_rows: list[dict], weights: dict[str, float]) -> list[dict]:
    if not medians:
        return []
    languages = sorted({row["language"] for row in all_rows})
    skipped = defaultdict(int)
    for row in all_rows:
        if row.get("status") in {"skipped", "failed"}:
            skipped[row["language"]] += 1
    score_inputs = normalize_medians(medians)
    per_lang: dict[str, list[dict]] = defaultdict(list)
    for row in score_inputs:
        per_lang[row["language"]].append(row)
    output = []
    for language in languages:
        bucket = per_lang.get(language, [])
        if not bucket:
            continue
        averaged = {metric: sum(r[metric] for r in bucket) / len(bucket) for metric in bucket[0] if metric.endswith("_score") or metric == "loc_score"}
        overall = (
            averaged["cpu_score"] * weights["cpu"] +
            averaged["wall_score"] * weights["wall"] +
            averaged["memory_score"] * weights["memory"] +
            averaged["loc_score"] * weights["loc"] +
            averaged["ease_score"] * weights["ease"] +
            averaged["community_score"] * weights["community"] +
            averaged["scalability_score"] * weights["scalability"] +
            averaged["debugging_score"] * weights["debugging"] +
            averaged["docs_score"] * weights["docs"] +
            averaged["libraries_score"] * weights["libraries"] +
            averaged["concurrency_score"] * weights["concurrency"]
        )
        output.append(ScoredLanguage(
            language=language,
            cpu_score=round(averaged["cpu_score"], 2),
            wall_score=round(averaged["wall_score"], 2),
            memory_score=round(averaged["memory_score"], 2),
            loc_score=round(averaged["loc_score"], 2),
            ease_score=round(averaged["ease_score"], 2),
            community_score=round(averaged["community_score"], 2),
            scalability_score=round(averaged["scalability_score"], 2),
            debugging_score=round(averaged["debugging_score"], 2),
            docs_score=round(averaged["docs_score"], 2),
            libraries_score=round(averaged["libraries_score"], 2),
            concurrency_score=round(averaged["concurrency_score"], 2),
            overall_score=round(overall, 2),
            tasks_covered=len({r["task_id"] for r in bucket}),
            skipped_tasks=skipped[language],
        ).to_dict())
        output[-1]["language_family"] = bucket[0].get("language_family", language)
        output[-1]["language_label"] = bucket[0].get("language_label", language)
        output[-1]["language_version"] = bucket[0].get("language_version")
        output[-1]["runtime_id"] = bucket[0].get("runtime_id", language)
        output[-1]["architecture"] = bucket[0].get("architecture", "unknown")
        output[-1]["cpu_geomean_score"] = round(_geomean([r["cpu_score"] for r in bucket]), 2)
        output[-1]["wall_geomean_score"] = round(_geomean([r["wall_score"] for r in bucket]), 2)
        output[-1]["cpu_cv_percent"] = round(_avg_cv(bucket, "cpu_stddev_seconds", "cpu_seconds"), 2)
        output[-1]["wall_cv_percent"] = round(_avg_cv(bucket, "wall_stddev_seconds", "wall_seconds"), 2)
        output[-1]["memory_cv_percent"] = round(_avg_cv(bucket, "memory_stddev_mb", "max_rss_mb"), 2)
        output[-1]["cpu_ci95_total_seconds"] = round(_aggregate_ci95(bucket, "cpu_ci95_seconds", average=False), 6)
        output[-1]["wall_ci95_total_seconds"] = round(_aggregate_ci95(bucket, "wall_ci95_seconds", average=False), 6)
        output[-1]["memory_ci95_avg_mb"] = round(_aggregate_ci95(bucket, "memory_ci95_mb", average=True), 6)
    output.sort(key=lambda row: row["overall_score"], reverse=True)
    return output


def normalize_medians(medians: list[dict]) -> list[dict]:
    best = {
        "cpu": min(_nonnull(row["cpu_seconds"]) for row in medians),
        "wall": min(_nonnull(row["wall_seconds"]) for row in medians),
        "memory": min(_nonnull(row["max_rss_mb"]) for row in medians),
        "loc": min(max(int(row["loc"]), 1) for row in medians),
        "ease": max(_nonnull(row["ease_score"]) for row in medians),
        "community": max(_nonnull(row["community_score"]) for row in medians),
        "scalability": max(_nonnull(row["scalability_score"]) for row in medians),
        "debugging": max(_nonnull(row["debugging_score"]) for row in medians),
        "docs": max(_nonnull(row["docs_score"]) for row in medians),
        "libraries": max(_nonnull(row["libraries_score"]) for row in medians),
        "concurrency": max(_nonnull(row["concurrency_score"]) for row in medians),
    }
    normalized = []
    for row in medians:
        normalized.append({
            **row,
            "cpu_score": round(100 * best["cpu"] / _nonnull(row["cpu_seconds"]), 2),
            "wall_score": round(100 * best["wall"] / _nonnull(row["wall_seconds"]), 2),
            "memory_score": round(100 * best["memory"] / _nonnull(row["max_rss_mb"]), 2),
            "loc_score": round(100 * best["loc"] / max(int(row["loc"]), 1), 2),
            "ease_score": round(100 * _nonnull(row["ease_score"]) / best["ease"], 2),
            "community_score": round(100 * _nonnull(row["community_score"]) / best["community"], 2),
            "scalability_score": round(100 * _nonnull(row["scalability_score"]) / best["scalability"], 2) if best["scalability"] else 0.0,
            "debugging_score": round(100 * _nonnull(row["debugging_score"]) / best["debugging"], 2),
            "docs_score": round(100 * _nonnull(row["docs_score"]) / best["docs"], 2),
            "libraries_score": round(100 * _nonnull(row["libraries_score"]) / best["libraries"], 2),
            "concurrency_score": round(100 * _nonnull(row["concurrency_score"]) / best["concurrency"], 2),
        })
    return normalized


def split_aggregate_scores(aggregate: list[dict], weights: dict[str, float]) -> dict[str, list[dict]]:
    return {
        "objective": _category_rows(aggregate, weights, OBJECTIVE_METRICS, "objective_score"),
        "opinionated": _category_rows(aggregate, weights, OPINIONATED_METRICS, "opinionated_score"),
    }


def _category_rows(aggregate: list[dict], weights: dict[str, float], metric_defs: list[tuple[str, str]], score_key: str) -> list[dict]:
    total_weight = sum(weights[weight_key] for _, weight_key in metric_defs)
    rows = []
    for row in aggregate:
        category_score = 0.0
        for field_name, weight_key in metric_defs:
            category_score += float(row.get(field_name, 0) or 0) * weights[weight_key]
        category_score = category_score / total_weight if total_weight else 0.0
        rows.append({
            **row,
            score_key: round(category_score, 2),
        })
    return sorted(rows, key=lambda row: row[score_key], reverse=True)


def _nonnull(value: float | int | None) -> float:
    if value is None:
        return EPSILON
    if isinstance(value, int):
        return float(max(value, 1))
    return max(float(value), EPSILON)


def _safe_div(num: float | None, den: float | None) -> float:
    return _nonnull(num) / _nonnull(den)


def _stddev(values: list[float]) -> float:
    if len(values) <= 1:
        return 0.0
    return round(pstdev(values), 6)


def _geomean(values: list[float]) -> float:
    cleaned = [max(float(v), EPSILON) for v in values if v is not None]
    if not cleaned:
        return 0.0
    return exp(sum(log(v) for v in cleaned) / len(cleaned))


def _avg_cv(rows: list[dict], std_field: str, value_field: str) -> float:
    values = []
    for row in rows:
        base = float(row.get(value_field) or 0)
        std = float(row.get(std_field) or 0)
        if base <= 0:
            continue
        values.append((std / base) * 100.0)
    return sum(values) / len(values) if values else 0.0


def _ci95(values: list[float]) -> float:
    if len(values) <= 1:
        return 0.0
    std = pstdev(values)
    return round(1.96 * std / (len(values) ** 0.5), 6)


def _aggregate_ci95(rows: list[dict], field: str, average: bool) -> float:
    components = [float(row.get(field) or 0.0) for row in rows]
    if not components:
        return 0.0
    combined = sum(value * value for value in components) ** 0.5
    if average:
        combined /= len(components)
    return combined
