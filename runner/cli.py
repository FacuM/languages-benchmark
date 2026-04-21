from __future__ import annotations

import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import math
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import time
import zipfile

from runner.config import ROOT, load_app_config, load_catalog, load_weights, load_rubrics, load_runtime_rubrics, load_community
from runner.engine import ContainerEngine
from runner.fixtures import prepare_fixtures, fixture_manifest
from runner.loc import count_loc
from runner.reporting import generate_report
from runner.service_workloads import run_service_workload, service_port, wait_for_service
from runner.ui_workloads import run_ui_workload, ui_port
from runner.readme_sync import sync_readme
from runner.scoring import score_results
from runner.utils import collect_host_metadata, ensure_dir, utc_stamp, write_json, write_csv, read_json, git_metadata

LANGUAGES = ["php", "python", "java", "cpp", "node", "go", "rust"]


def _log(message: str) -> None:
    print(message, flush=True)


def _format_seconds_short(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value < 1.0:
        return f"{value * 1000:.1f} ms"
    return f"{value:.2f} s"


def _describe_case(case: dict) -> str:
    task = case["task"]
    spec = case["spec"]
    return f"{task.id} | {spec.get('label', case['variant_id'])} | size {str(case['size']).upper()}"


def _summarize_case_rows(rows: list[dict]) -> str:
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[str(row.get("status"))] += 1
    measured = [row for row in rows if row.get("status") == "ok"]
    failures = counts.get("failed", 0)
    skips = counts.get("skipped", 0)
    warmups = counts.get("warmup", 0)
    if measured:
        wall = sum(float(row.get("wall_seconds") or 0.0) for row in measured) / len(measured)
        cpu = sum(float(row.get("cpu_seconds") or 0.0) for row in measured) / len(measured)
        rss = sum(float(row.get("max_rss_mb") or 0.0) for row in measured) / len(measured)
        return (
            f"measured={len(measured)}, warmups={warmups}, failed={failures}, skipped={skips}, "
            f"avg wall={_format_seconds_short(wall)}, avg cpu={_format_seconds_short(cpu)}, avg rss={rss:.1f} MB"
        )
    if skips:
        return f"skipped={skips}"
    if failures:
        return f"failed={failures}"
    return ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="bench")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("setup")

    run_p = sub.add_parser("run")
    run_p.add_argument("--tasks")
    run_p.add_argument("--langs")
    run_p.add_argument("--sizes")
    run_p.add_argument("--iterations", type=int)
    run_p.add_argument("--warmups", type=int)
    run_p.add_argument("--engine")
    run_p.add_argument("--preset")
    run_p.add_argument("--dry-run", action="store_true")
    run_p.add_argument("--jobs", type=int, default=None)
    run_p.add_argument("--execution-mode", choices=["container", "native-host"], default="container")

    score_p = sub.add_parser("score")
    score_p.add_argument("--results", required=True)
    score_p.add_argument("--weights")

    report_p = sub.add_parser("report")
    report_p.add_argument("--results", required=True)
    report_p.add_argument("--update-readme", action="store_true")

    readme_p = sub.add_parser("readme")
    readme_p.add_argument("--results", required=True)

    all_p = sub.add_parser("all")
    all_p.add_argument("--tasks")
    all_p.add_argument("--langs")
    all_p.add_argument("--sizes")
    all_p.add_argument("--iterations", type=int)
    all_p.add_argument("--warmups", type=int)
    all_p.add_argument("--engine")
    all_p.add_argument("--preset")
    all_p.add_argument("--dry-run", action="store_true")
    all_p.add_argument("--update-readme", action="store_true")
    all_p.add_argument("--jobs", type=int, default=None)
    all_p.add_argument("--execution-mode", choices=["container", "native-host"], default="container")

    bundle_p = sub.add_parser("publish-bundle")
    bundle_p.add_argument("--tasks")
    bundle_p.add_argument("--langs")
    bundle_p.add_argument("--sizes")
    bundle_p.add_argument("--iterations", type=int)
    bundle_p.add_argument("--warmups", type=int)
    bundle_p.add_argument("--engine")
    bundle_p.add_argument("--preset", default="publish")
    bundle_p.add_argument("--dry-run", action="store_true")
    bundle_p.add_argument("--jobs", type=int, default=None)
    bundle_p.add_argument("--reruns", type=int, default=3)
    bundle_p.add_argument("--update-readme", action="store_true")
    bundle_p.add_argument("--execution-mode", choices=["container", "native-host"], default="container")

    args = parser.parse_args(argv)
    if args.command == "setup":
        return cmd_setup()
    if args.command == "run":
        return cmd_run(args)
    if args.command == "score":
        return cmd_score(args)
    if args.command == "report":
        return cmd_report(args)
    if args.command == "readme":
        return cmd_readme(args)
    if args.command == "all":
        cmd_setup()
        cmd_run(args)
        results = ROOT / "results" / "latest" / "raw_results.json"
        cmd_score(argparse.Namespace(results=str(results), weights=None))
        scored = ROOT / "results" / "latest" / "scored_results.json"
        cmd_report(argparse.Namespace(results=str(scored), update_readme=args.update_readme))
        return 0
    if args.command == "publish-bundle":
        return cmd_publish_bundle(args)
    return 1


def cmd_setup() -> int:
    config = load_app_config()
    _log(f"[setup] Preparing fixtures under {ROOT / 'fixtures'}")
    prepare_fixtures(ROOT)
    engine = ContainerEngine(config.engine)
    _log(f"[setup] Validating container engine: {config.engine}")
    engine.validate()
    for variant_id, spec in _variant_entries(config):
        _log(f"[setup] Building runtime image {variant_id} from {spec['dockerfile']}")
        engine.build(_image_tag(variant_id), ROOT / spec["dockerfile"], ROOT, build_args=_build_args(spec))
    _log(f"[setup] Building UI driver image {config.ui_driver_image}")
    engine.build(config.ui_driver_image, ROOT / "runner" / "ui-driver.Dockerfile", ROOT)
    _log("[setup] Setup complete")
    return 0


def cmd_run(args) -> int:
    config = load_app_config()
    catalog = load_catalog()
    preset = _resolve_preset(config, getattr(args, "preset", None))
    task_selector = args.tasks if args.tasks is not None else preset.get("tasks", config.default_tasks)
    lang_selector = args.langs if args.langs is not None else preset.get("langs", "all")
    sizes_selector = args.sizes if args.sizes is not None else preset.get("sizes", config.sizes)
    iterations = args.iterations if args.iterations is not None else int(preset.get("iterations", config.iterations))
    warmups = args.warmups if args.warmups is not None else int(preset.get("warmups", config.warmups))
    selected_tasks = _select_tasks(catalog, task_selector, config.smoke_tasks)
    variants = _select_variants(config, lang_selector)
    sizes = _select_sizes(sizes_selector, config.sizes)
    jobs = max(1, int(args.jobs if args.jobs is not None else int(preset.get("jobs", 1))))
    run_id = utc_stamp()
    output_dir = ensure_dir(ROOT / config.results_dir / run_id)
    latest = ROOT / config.results_dir / "latest"
    if latest.exists() or latest.is_symlink():
        latest.unlink() if latest.is_symlink() else shutil.rmtree(latest)
    latest.symlink_to(output_dir, target_is_directory=True)
    rubrics = load_rubrics()
    runtime_rubrics = load_runtime_rubrics()
    community = load_community()
    engine = ContainerEngine(args.engine or config.engine)
    host = collect_host_metadata(engine.binary)
    git = git_metadata(ROOT)
    runtimes = _collect_runtime_matrix(engine, variants, dry_run=args.dry_run)
    _log(
        "[run] Starting benchmark run "
        f"{run_id} | tasks={len(selected_tasks)} | runtimes={len(variants)} | sizes={len(sizes)} | "
        f"iterations={iterations} | warmups={warmups} | jobs={jobs} | "
        f"mode={args.execution_mode} | dry_run={'yes' if args.dry_run else 'no'}"
    )
    _log("[run] Selected runtimes: " + ", ".join(spec.get("label", variant_id) for variant_id, spec in variants))
    variant_index = {variant_id: index for index, (variant_id, _spec) in enumerate(_variant_entries(config))}
    cases = []
    for task_index, task in enumerate(selected_tasks):
        for variant_index_order, (variant_id, spec) in enumerate(variants):
            family = spec["family"]
            implementation = spec.get("implementation", family)
            rubric = runtime_rubrics.get(variant_id, rubrics[family])
            community_score = round((community[family]["active_contributors"] + community[family]["update_cadence"]) / 2.0, 2)
            supported_tasks = set(spec.get("supported_tasks", []))
            for size_index, size in enumerate(sizes):
                cases.append({
                    "sort_key": (task_index, variant_index_order, size_index),
                    "task": task,
                    "variant_id": variant_id,
                    "spec": spec,
                    "size": size,
                    "implementation": implementation,
                    "rubric": rubric,
                    "community_score": community_score,
                    "supported_tasks": supported_tasks,
                    "execution_mode": args.execution_mode,
                })

    rows = []
    total_cases = len(cases)
    if jobs == 1 or args.dry_run:
        for index, case in enumerate(cases, start=1):
            _log(f"[run] [{index}/{total_cases}] START { _describe_case(case) }")
            started = time.perf_counter()
            bucket = _run_case(
                case=case,
                run_id=run_id,
                iterations=iterations,
                warmups=warmups,
                variant_order=variant_index,
                engine=engine,
                config=config,
                dry_run=args.dry_run,
            )
            rows.extend(bucket)
            _log(
                f"[run] [{index}/{total_cases}] DONE  {_describe_case(case)} | "
                f"{_summarize_case_rows(bucket)} | elapsed={_format_seconds_short(time.perf_counter() - started)}"
            )
    else:
        max_workers = min(jobs, len(cases)) if cases else 1
        _log(f"[run] Executing {total_cases} cases with {max_workers} worker(s)")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_map = {
                executor.submit(
                    _run_case,
                    case=case,
                    run_id=run_id,
                    iterations=iterations,
                    warmups=warmups,
                    variant_order=variant_index,
                    engine=ContainerEngine(args.engine or config.engine),
                    config=config,
                    dry_run=args.dry_run,
                ): case["sort_key"]
                for case in cases
            }
            case_rows = []
            completed = 0
            for future in as_completed(future_map):
                sort_key = future_map[future]
                completed += 1
                case = next(case for case in cases if case["sort_key"] == sort_key)
                bucket = future.result()
                case_rows.append((sort_key, bucket))
                _log(f"[run] [{completed}/{total_cases}] DONE  {_describe_case(case)} | {_summarize_case_rows(bucket)}")
            for _sort_key, bucket in sorted(case_rows, key=lambda item: item[0]):
                rows.extend(bucket)
    profile = {
        "preset": getattr(args, "preset", None),
        "tasks": task_selector,
        "langs": lang_selector,
        "sizes": sizes,
        "iterations": iterations,
        "warmups": warmups,
        "jobs": jobs,
        "engine": args.engine or config.engine,
        "baseline_runtime": config.baseline_runtime,
        "execution_mode": args.execution_mode,
    }
    write_json(output_dir / "raw_results.json", {"run_id": run_id, "host": host, "git": git, "runtimes": runtimes, "fixture_manifest": fixture_manifest(ROOT), "profile": profile, "rows": rows})
    write_csv(output_dir / "raw_results.csv", rows)
    status_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        status_counts[str(row.get("status"))] += 1
    _log(
        "[run] Completed "
        f"{run_id} | ok={status_counts.get('ok', 0)} | warmup={status_counts.get('warmup', 0)} | "
        f"failed={status_counts.get('failed', 0)} | skipped={status_counts.get('skipped', 0)}"
    )
    print(output_dir / "raw_results.json")
    return 0


def cmd_score(args) -> int:
    path = Path(args.results)
    _log(f"[score] Loading raw results from {path}")
    payload = read_json(path)
    weights = load_weights(path=Path(args.weights)) if args.weights else load_weights()
    medians, aggregate = score_results(payload["rows"], weights)
    scored = {
        "run_id": payload.get("run_id"),
        "host": payload.get("host"),
        "git": payload.get("git"),
        "runtimes": payload.get("runtimes", []),
        "fixture_manifest": payload.get("fixture_manifest", {}),
        "profile": payload.get("profile", {}),
        "rows": payload["rows"],
        "medians": medians,
        "aggregate": aggregate,
        "weights": weights,
    }
    target = path.with_name("scored_results.json")
    write_json(target, scored)
    write_csv(target.with_suffix(".csv"), aggregate)
    _log(f"[score] Wrote scored JSON and CSV for {len(aggregate)} runtime rows")
    print(target)
    return 0


def cmd_report(args) -> int:
    results_path = Path(args.results)
    report_dir = results_path.parent / "report"
    _log(f"[report] Generating report from {results_path}")
    report_path = generate_report(results_path, report_dir)
    if getattr(args, "update_readme", False):
        _log("[report] Updating README and docs/plots from this report")
        sync_readme(results_path, ROOT / "README.md", ROOT / "docs")
    _log(f"[report] Report ready at {report_path}")
    print(report_path)
    return 0


def cmd_publish_bundle(args) -> int:
    reruns = max(1, int(getattr(args, "reruns", 1) or 1))
    bundle_id = utc_stamp()
    bundle_dir = ensure_dir(ROOT / "results" / "bundles" / bundle_id)
    _log(f"[bundle] Starting publish bundle {bundle_id} with {reruns} rerun(s)")
    runs = []
    for index in range(reruns):
        _log(f"[bundle] Rerun {index + 1}/{reruns}: benchmark")
        run_args = argparse.Namespace(
            tasks=args.tasks,
            langs=args.langs,
            sizes=args.sizes,
            iterations=args.iterations,
            warmups=args.warmups,
            engine=args.engine,
            preset=args.preset,
            dry_run=args.dry_run,
            jobs=args.jobs,
            execution_mode=args.execution_mode,
        )
        cmd_run(run_args)
        raw_path = ROOT / "results" / "latest" / "raw_results.json"
        _log(f"[bundle] Rerun {index + 1}/{reruns}: scoring")
        cmd_score(argparse.Namespace(results=str(raw_path), weights=None))
        scored_path = ROOT / "results" / "latest" / "scored_results.json"
        _log(f"[bundle] Rerun {index + 1}/{reruns}: reporting")
        cmd_report(argparse.Namespace(results=str(scored_path), update_readme=(index == reruns - 1 and args.update_readme)))
        scored_payload = read_json(scored_path)
        run_id = str(scored_payload.get("run_id") or f"run-{index + 1}")
        bundle_scored = bundle_dir / f"{index + 1:02d}-{run_id}-scored_results.json"
        shutil.copyfile(scored_path.resolve(), bundle_scored)
        try:
            scored_rel = bundle_scored.relative_to(ROOT)
        except ValueError:
            scored_rel = bundle_scored
        runs.append({
            "run_id": run_id,
            "scored_results": str(scored_rel),
            "overall_scores": {row["language"]: row["overall_score"] for row in scored_payload.get("aggregate", [])},
        })
        _log(f"[bundle] Rerun {index + 1}/{reruns}: archived {bundle_scored.name}")
    stability = _rerun_stability(runs)
    manifest = {
        "bundle_id": bundle_id,
        "preset": args.preset,
        "reruns": reruns,
        "execution_mode": args.execution_mode,
        "runs": runs,
        "stability": stability,
    }
    write_json(bundle_dir / "bundle_manifest.json", manifest)
    zip_path = bundle_dir / "bundle.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(bundle_dir / "bundle_manifest.json", arcname="bundle_manifest.json")
        for run in runs:
            scored_rel = Path(run["scored_results"])
            if (ROOT / scored_rel).exists():
                archive.write(ROOT / scored_rel, arcname=str(scored_rel))
    _log(f"[bundle] Bundle ready at {bundle_dir}")
    print(bundle_dir / "bundle_manifest.json")
    return 0


def cmd_readme(args) -> int:
    results_path = Path(args.results)
    _log(f"[readme] Syncing README from {results_path}")
    readme_path = sync_readme(results_path, ROOT / "README.md", ROOT / "docs")
    _log(f"[readme] README updated at {readme_path}")
    print(readme_path)
    return 0


def _select_tasks(catalog, selector: str, smoke_tasks: list[str]):
    if selector == "all":
        return catalog
    if selector == "smoke":
        wanted = set(smoke_tasks)
        return [task for task in catalog if task.id in wanted]
    if isinstance(selector, str):
        wanted = {x.strip() for x in selector.split(",") if x.strip()}
    else:
        wanted = {str(x).strip() for x in selector if str(x).strip()}
    return [task for task in catalog if task.id in wanted]


def _resolve_preset(config, preset_name: str | None) -> dict:
    if not preset_name:
        return {}
    preset = config.presets.get(preset_name)
    if preset is None:
        available = ", ".join(sorted(config.presets)) or "none"
        raise SystemExit(f"Unknown preset '{preset_name}'. Available presets: {available}")
    return preset


def _variant_entries(config) -> list[tuple[str, dict]]:
    if config.language_variants:
        return list(config.language_variants.items())
    return [(language, {"family": language, "label": language, "version": "", "dockerfile": f"tasks/implementations/{language}/Dockerfile"}) for language in LANGUAGES]


def _select_variants(config, selector) -> list[tuple[str, dict]]:
    entries = _variant_entries(config)
    variants_by_id = {variant_id: spec for variant_id, spec in entries}
    families = defaultdict(list)
    for variant_id, spec in entries:
        families[spec["family"]].append((variant_id, spec))
    if selector == "all":
        return entries
    tokens = [x.strip() for x in selector.split(",")] if isinstance(selector, str) else [str(x).strip() for x in selector]
    selected: list[tuple[str, dict]] = []
    seen: set[str] = set()
    for token in tokens:
        if not token:
            continue
        if token in variants_by_id:
            if token not in seen:
                selected.append((token, variants_by_id[token]))
                seen.add(token)
            continue
        if token in families:
            for variant_id, spec in families[token]:
                if variant_id not in seen:
                    selected.append((variant_id, spec))
                    seen.add(variant_id)
            continue
        raise SystemExit(f"Unknown language selector '{token}'. Use a family like 'python' or variant like 'python-3.12'.")
    return selected


def _build_args(spec: dict) -> dict[str, str]:
    mapping = {
        "base_image": "BASE_IMAGE",
        "build_image": "BUILD_IMAGE",
        "runtime_image": "RUNTIME_IMAGE",
    }
    return {arg_name: str(spec[key]) for key, arg_name in mapping.items() if spec.get(key)}


def _image_tag(variant_id: str) -> str:
    return f"languages-benchmark:{variant_id}"


def _collect_runtime_matrix(engine: ContainerEngine, variants: list[tuple[str, dict]], dry_run: bool) -> list[dict]:
    runtimes = []
    for variant_id, spec in variants:
        reported = spec.get("version")
        command = spec.get("runtime_version_command")
        if not dry_run and command:
            reported = engine.inspect_runtime(_image_tag(variant_id), command) or reported
        runtimes.append({
            "language": variant_id,
            "language_family": spec["family"],
            "language_label": spec.get("label", variant_id),
            "configured_version": spec.get("version"),
            "reported_version": reported,
            "image": _image_tag(variant_id),
        })
    return runtimes


def _select_sizes(selector, default_sizes: list[str]) -> list[str]:
    if selector is None or selector == "all":
        return list(default_sizes)
    if isinstance(selector, str):
        return [x.strip() for x in selector.split(",") if x.strip()]
    return [str(x).strip() for x in selector if str(x).strip()]


def _rerun_stability(runs: list[dict]) -> list[dict]:
    buckets: dict[str, list[float]] = defaultdict(list)
    for run in runs:
        for language, score in run.get("overall_scores", {}).items():
            buckets[str(language)].append(float(score))
    output = []
    for language, values in sorted(buckets.items()):
        avg = sum(values) / len(values)
        variance = sum((value - avg) ** 2 for value in values) / len(values) if values else 0.0
        std = variance ** 0.5
        output.append({
            "language": language,
            "reruns": len(values),
            "overall_avg": round(avg, 2),
            "overall_stddev": round(std, 4),
            "overall_range": [round(min(values), 2), round(max(values), 2)] if values else [],
        })
    return output


def _run_service_benchmark(*, engine, image, task_id, size, fixtures_dir, cpu_limit, memory_limit):
    boot_started = time.perf_counter()
    handle = engine.start_service(
        image=image,
        task_id=task_id,
        size=size,
        fixtures_dir=fixtures_dir,
        cpu_limit=cpu_limit,
        memory_limit=memory_limit,
        container_port=service_port(task_id),
    )
    try:
        wait_for_service(task_id, "127.0.0.1", handle.host_port)
        startup_wall_seconds = time.perf_counter() - boot_started
        cpu_before = engine.container_cpu_seconds(handle.container_id) or 0.0
        workload_started = time.perf_counter()
        workload_output = run_service_workload(task_id, size, "127.0.0.1", handle.host_port)
        workload_wall_seconds = time.perf_counter() - workload_started
        cpu_after = engine.container_cpu_seconds(handle.container_id) or cpu_before
        stdout, stderr = engine.container_logs(handle.container_id)
        return type("ServiceMetrics", (), {
            "cpu_seconds": max(0.0, cpu_after - cpu_before),
            "wall_seconds": startup_wall_seconds + workload_wall_seconds,
            "startup_wall_seconds": startup_wall_seconds,
            "workload_wall_seconds": workload_wall_seconds,
            "max_rss_mb": engine.container_memory_peak_mb(handle.container_id),
            "stdout": workload_output + "\n",
            "stderr": stdout + stderr,
            "returncode": 0,
            "host_wall_seconds": startup_wall_seconds + workload_wall_seconds,
            "repeat_count": 1,
        })()
    except Exception as exc:  # noqa: BLE001
        stdout, stderr = engine.container_logs(handle.container_id)
        return type("ServiceMetrics", (), {
            "cpu_seconds": None,
            "wall_seconds": None,
            "startup_wall_seconds": None,
            "workload_wall_seconds": None,
            "max_rss_mb": engine.container_memory_peak_mb(handle.container_id),
            "stdout": stdout,
            "stderr": stderr + f"\nSERVICE_ERROR: {exc}\n",
            "returncode": 1,
            "host_wall_seconds": 0.0,
            "repeat_count": 1,
        })()
    finally:
        engine.stop_service(handle.container_id)


def _run_ui_benchmark(*, engine, image, task_id, size, fixtures_dir, cpu_limit, memory_limit):
    container_port = ui_port(task_id)
    boot_started = time.perf_counter()
    handle = engine.start_service(
        image=image,
        task_id=task_id,
        size=size,
        fixtures_dir=fixtures_dir,
        cpu_limit=cpu_limit,
        memory_limit=memory_limit,
        container_port=container_port,
    )
    try:
        wait_for_service(task_id, "127.0.0.1", handle.host_port)
        startup_wall_seconds = time.perf_counter() - boot_started
        cpu_before = engine.container_cpu_seconds(handle.container_id) or 0.0
        workload = run_ui_workload(engine.binary, task_id, size, handle.container_id, container_port)
        cpu_after = engine.container_cpu_seconds(handle.container_id) or cpu_before
        stdout, stderr = engine.container_logs(handle.container_id)
        return type("UIMetrics", (), {
            "cpu_seconds": max(0.0, cpu_after - cpu_before),
            "wall_seconds": startup_wall_seconds + workload.wall_seconds,
            "startup_wall_seconds": startup_wall_seconds,
            "workload_wall_seconds": workload.wall_seconds,
            "max_rss_mb": engine.container_memory_peak_mb(handle.container_id),
            "stdout": workload.stdout,
            "stderr": workload.stderr + stdout + stderr,
            "returncode": workload.returncode,
            "host_wall_seconds": startup_wall_seconds + workload.wall_seconds,
            "repeat_count": 1,
        })()
    finally:
        engine.stop_service(handle.container_id)


def _estimate_repeat_count(*, engine, image, task_id, size, fixtures_dir, cpu_limit, memory_limit, network_disabled, target_wall_seconds: float, max_repeat_factor: int) -> int:
    pilot = engine.run_single(
        image=image,
        args=[task_id, size],
        fixtures_dir=fixtures_dir,
        cpu_limit=cpu_limit,
        memory_limit=memory_limit,
        network_disabled=network_disabled,
        repeat_count=1,
    )
    baseline = max(pilot.cpu_seconds or 0.0, pilot.wall_seconds or 0.0, 0.001)
    estimated = math.ceil(target_wall_seconds / baseline)
    return max(1, min(max_repeat_factor, estimated))


def _run_native_single(*, command_template: str, task_id: str, size: str, fixtures_dir: Path, repeat_count: int = 1):
    command = command_template.format(task_id=task_id, size=size, fixtures_dir=str(fixtures_dir))
    loop = (
        "i=0; "
        f"while [ \"$i\" -lt {repeat_count} ]; do {command} > /tmp/bench.stdout 2> /tmp/bench.stderr || exit $?; "
        "i=$((i+1)); "
        "done"
    )
    time_format = "\\n".join(
        [
            "__CPU_USER=%U",
            "__CPU_SYS=%S",
            "__WALL=%e",
            "__RSS_KB=%M",
        ]
    )
    timed = f"/usr/bin/time -f {shlex.quote(time_format)} -o /tmp/bench.time sh -lc {shlex.quote(loop)}; status=$?; cat /tmp/bench.stdout; cat /tmp/bench.stderr >&2; cat /tmp/bench.time >&2; exit $status"
    started = time.perf_counter()
    proc = subprocess.run(["bash", "-lc", timed], text=True, capture_output=True)
    host_wall_seconds = time.perf_counter() - started
    from runner.engine import _parse_cpu_seconds, _parse_wall_seconds, _parse_rss_mb

    divisor = max(repeat_count, 1)
    return type("NativeMetrics", (), {
        "cpu_seconds": (_parse_cpu_seconds(proc.stderr) / divisor) if _parse_cpu_seconds(proc.stderr) is not None else None,
        "wall_seconds": (_parse_wall_seconds(proc.stderr) / divisor) if _parse_wall_seconds(proc.stderr) is not None else host_wall_seconds / divisor,
        "startup_wall_seconds": None,
        "workload_wall_seconds": None,
        "max_rss_mb": _parse_rss_mb(proc.stderr),
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "returncode": proc.returncode,
        "host_wall_seconds": host_wall_seconds / divisor,
        "repeat_count": repeat_count,
    })()


def _base_row(run_id, task_id, language, spec, size, iteration, status, loc, community_score, rubric, stdout="", stderr="", repeat_count=1, notes=""):
    return {
        "run_id": run_id,
        "task_id": task_id,
        "language": language,
        "language_family": spec["family"],
        "language_label": spec.get("label", language),
        "language_version": spec.get("version"),
        "size": size,
        "iteration": iteration,
        "repeat_count": repeat_count,
        "status": status,
        "cpu_seconds": None,
        "wall_seconds": None,
        "startup_wall_seconds": None,
        "workload_wall_seconds": None,
        "max_rss_mb": None,
        "loc": loc,
        "community_score": community_score,
        "ease_score": rubric["ease"],
        "debugging_score": rubric["debugging"],
        "docs_score": rubric["docs"],
        "libraries_score": rubric["libraries"],
        "concurrency_score": rubric["concurrency"],
        "scalability_score": None,
        "overall_score": None,
        "stdout": stdout,
        "stderr": stderr,
        "notes": notes,
    }


def _run_case(*, case, run_id, iterations, warmups, variant_order, engine, config, dry_run):
    task = case["task"]
    variant_id = case["variant_id"]
    spec = case["spec"]
    size = case["size"]
    implementation = case["implementation"]
    rubric = case["rubric"]
    community_score = case["community_score"]
    supported_tasks = case["supported_tasks"]
    execution_mode = case.get("execution_mode", "container")
    if not task.executable or (supported_tasks and task.id not in supported_tasks):
        skip_note = "Catalog scaffold only" if not task.executable else "Variant does not support this task"
        return [_base_row(run_id, task.id, variant_id, spec, size, 0, "skipped", count_loc(ROOT, implementation, task.id), community_score, rubric, notes=skip_note)]
    native_template = spec.get("native_command_template")
    if execution_mode == "native-host" and not native_template:
        return [_base_row(run_id, task.id, variant_id, spec, size, 0, "skipped", count_loc(ROOT, implementation, task.id), community_score, rubric, notes="Experimental native-host mode is not configured for this variant")]

    rows = []
    repeat_count = 1
    if task.kind not in {"service", "ui"} and not dry_run and execution_mode == "container":
        repeat_count = _estimate_repeat_count(
            engine=engine,
            image=_image_tag(variant_id),
            task_id=task.id,
            size=size,
            fixtures_dir=ROOT / "fixtures",
            cpu_limit=config.cpu_limit,
            memory_limit=config.memory_limit,
            network_disabled=config.network_disabled,
            target_wall_seconds=config.target_wall_seconds,
            max_repeat_factor=config.max_repeat_factor,
        )
    for iteration in range(0, warmups + iterations):
        status = "warmup" if iteration < warmups else "ok"
        if dry_run:
            row = _base_row(run_id, task.id, variant_id, spec, size, iteration, status, count_loc(ROOT, implementation, task.id), community_score, rubric, repeat_count=repeat_count)
            multiplier = {"s": 1.0, "m": 2.0, "l": 4.0}[size]
            lang_factor = (variant_order.get(variant_id, 0) + 1) / 10.0
            row.update({
                "cpu_seconds": round(0.02 * multiplier + lang_factor, 4),
                "wall_seconds": round(0.03 * multiplier + lang_factor, 4),
                "max_rss_mb": round(10 * multiplier + 20 + lang_factor, 3),
            })
            rows.append(row)
            continue
        if task.kind == "service":
            metrics = _run_service_benchmark(
                engine=engine,
                image=_image_tag(variant_id),
                task_id=task.id,
                size=size,
                fixtures_dir=ROOT / "fixtures",
                cpu_limit=config.cpu_limit,
                memory_limit=config.memory_limit,
            )
        elif task.kind == "ui":
            metrics = _run_ui_benchmark(
                engine=engine,
                image=_image_tag(variant_id),
                task_id=task.id,
                size=size,
                fixtures_dir=ROOT / "fixtures",
                cpu_limit=config.cpu_limit,
                memory_limit=config.memory_limit,
            )
        elif execution_mode == "native-host":
            metrics = _run_native_single(
                command_template=str(native_template),
                task_id=task.id,
                size=size,
                fixtures_dir=ROOT / "fixtures",
                repeat_count=repeat_count,
            )
        else:
            metrics = engine.run_single(
                image=_image_tag(variant_id),
                args=[task.id, size],
                fixtures_dir=ROOT / "fixtures",
                cpu_limit=config.cpu_limit,
                memory_limit=config.memory_limit,
                network_disabled=config.network_disabled,
                repeat_count=repeat_count,
            )
        row = _base_row(
            run_id,
            task.id,
            variant_id,
            spec,
            size,
            iteration,
            status if metrics.returncode == 0 else "failed",
            count_loc(ROOT, implementation, task.id),
            community_score,
            rubric,
            stdout=metrics.stdout,
            stderr=metrics.stderr,
            repeat_count=repeat_count,
            notes=f"repeat_count={metrics.repeat_count}; host_wall_seconds={metrics.host_wall_seconds:.6f}",
        )
        row.update({
            "cpu_seconds": metrics.cpu_seconds,
            "wall_seconds": metrics.wall_seconds,
            "startup_wall_seconds": getattr(metrics, "startup_wall_seconds", None),
            "workload_wall_seconds": getattr(metrics, "workload_wall_seconds", None),
            "max_rss_mb": metrics.max_rss_mb,
        })
        rows.append(row)
    return rows


if __name__ == "__main__":
    raise SystemExit(main())
