from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import math
import shutil
from statistics import pstdev

from runner.config import ROOT, load_app_config, load_catalog, load_rubrics, load_weights
from runner.scoring import score_results, split_aggregate_scores, aggregate_for_task_ids
from runner.utils import ensure_dir, read_json, write_json

MARKER_BEGIN = "<!-- benchmark:begin -->"
MARKER_END = "<!-- benchmark:end -->"
PLOT_FILES = [
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
]
LANGUAGE_LABELS = {
    "php": "PHP",
    "python": "Python",
    "java": "Java",
    "cpp": "C++",
    "node": "JavaScript (Node.js)",
    "go": "Go",
    "rust": "Rust",
}
TASK_EXPLANATIONS = {
    "sort_integers": {
        "how": "Each implementation reads a deterministic fixture of integers, parses them into an in-memory array/vector/list, sorts ascending, and prints the sum of the first 100 values as a correctness checksum.",
        "tests": "This stresses file parsing, allocation behavior, the language's standard-library sort implementation, and raw single-process CPU throughput on a simple but realistic data-processing workload.",
    },
    "matrix_multiplication": {
        "how": "Each implementation reads two dense square matrices from the fixture, performs naive O(n^3) multiplication with a triple nested loop, and prints the sum of all output cells so the work cannot be optimized away.",
        "tests": "This emphasizes arithmetic throughput, tight-loop overhead, array indexing costs, cache locality, and how well the runtime handles hot numeric code without relying on specialized libraries.",
    },
    "csv_parsing": {
        "how": "Each implementation opens the same generated CSV file, skips the header, parses numeric columns from every row, and accumulates a deterministic total that is printed at the end.",
        "tests": "This measures text parsing overhead, per-row iteration cost, string-to-number conversion, streaming/file I/O behavior, and the standard library's ergonomics for simple data ingestion.",
    },
    "prime_sieve": {
        "how": "Each implementation runs a Sieve of Eratosthenes up to a fixed limit for size S, M, or L, then counts and prints the number of primes found.",
        "tests": "This isolates tight loops, repeated memory writes, boolean-array behavior, and branch-heavy compute in a benchmark that is simple to verify and highly repeatable across runtimes.",
    },
    "file_io_large": {
        "how": "Each implementation opens the same large deterministic text file, reads it sequentially, parses one integer per line, and accumulates a total checksum that is printed at the end.",
        "tests": "This focuses on streaming file I/O, text parsing overhead, buffered reading behavior, and the runtime cost of turning a large raw file into usable numeric values.",
    },
    "binary_search_tree": {
        "how": "Each implementation reads a deterministic sequence of insert values and query values, builds an in-memory binary search tree from the inserts, then searches every query and sums the values that are found.",
        "tests": "This measures pointer-heavy data structure work, heap allocation patterns, branch behavior, and the ergonomics of implementing a classic mutable tree without external libraries.",
    },
    "linear_regression": {
        "how": "Each implementation reads the same synthetic regression dataset, computes the least-squares slope and intercept for a single-feature linear model, and prints a rounded checksum of the fitted parameters.",
        "tests": "This exercises numeric iteration over a realistic machine-learning style dataset, repeated floating-point accumulation, and the cost of basic statistical computation without specialized ML libraries.",
    },
    "cli_file_search": {
        "how": "Each implementation recursively walks a deterministic directory tree of text files, scans file contents line by line, and counts how many lines contain the target token `needle`.",
        "tests": "This benchmarks directory traversal, path handling, repeated file opening, line scanning, and the amount of glue code each language needs for a basic command-line search utility.",
    },
    "tic_tac_toe": {
        "how": "Each implementation replays a deterministic set of tic-tac-toe move sequences, applies the rules of the game, detects wins or draws, and accumulates a checksum from the final board state and game outcome.",
        "tests": "This stresses branch-heavy control flow, small-state mutation, repeated rule checking, and the ergonomics of implementing a tiny game engine in each language.",
    },
    "basic_blockchain": {
        "how": "Each implementation reads deterministic blocks of synthetic transactions, links them through a rolling previous-hash value, computes a simple chain hash for every block, and accumulates a final checksum for the whole chain.",
        "tests": "This measures integer-heavy stateful iteration, repeated hashing/mixing work, and the overhead of maintaining a minimal blockchain-style data pipeline without relying on external cryptography libraries.",
    },
    "image_resizing": {
        "how": "Each implementation loads the same deterministic PPM image fixture, downsamples it by a fixed factor using nearest-neighbor sampling, and prints a checksum over the resized pixels instead of writing an output file.",
        "tests": "This exercises structured file parsing, array indexing, pixel-wise numeric loops, and a simple but realistic image-processing workload using only standard library tools.",
    },
    "sentiment_analysis": {
        "how": "Each implementation scans the same deterministic corpus of text lines, applies a tiny lexicon-based sentiment model with positive and negative word lists, and prints the aggregate sentiment score.",
        "tests": "This benchmarks tokenization, repeated dictionary/set lookups, string processing, and a minimal natural-language processing workload that stays fully reproducible offline.",
    },
    "decision_tree": {
        "how": "Each implementation trains the same small deterministic decision tree on a synthetic labeled dataset using fixed split candidates, then evaluates the model across the dataset and prints a checksum based on accuracy and predictions.",
        "tests": "This measures structured CSV parsing, repeated impurity calculations, recursive model construction, and a basic but realistic machine-learning training workload that stays comparable across languages.",
    },
    "producer_consumer": {
        "how": "Each implementation reads the same sequence of produced values, feeds them through a bounded circular buffer that simulates producer and consumer coordination, and prints a checksum over the consumed stream.",
        "tests": "This benchmarks queue bookkeeping, bounded-buffer logic, stateful iteration, and the implementation overhead of a classic producer-consumer style workload in each language.",
    },
    "simple_web_server": {
        "how": "Each implementation starts a minimal local HTTP server, exposes a `/health` route plus a root route returning a fixed response body, and the neutral runner measures repeated local GET requests against that service.",
        "tests": "This measures HTTP server startup, request parsing, response generation, socket handling, and the baseline cost of serving a tiny deterministic web workload in each language.",
    },
    "rest_api": {
        "how": "Each implementation starts a deterministic local HTTP API with `/item?id=...` returning a small JSON payload, and the benchmark driver issues repeated GET requests while validating the aggregated numeric response values.",
        "tests": "This benchmarks lightweight routing, query parsing, JSON serialization, per-request object construction, and service-style runtime overhead beyond pure compute loops.",
    },
    "chat_application": {
        "how": "Each implementation starts a minimal TCP chat-style server, accepts short line-oriented client messages, prepends a deterministic marker to each payload, and the benchmark driver measures repeated round trips over loopback networking.",
        "tests": "This focuses on TCP socket setup, connection handling, message framing, short-lived request-response behavior, and the language runtime’s overhead for small network services.",
    },
    "sqlite_crud": {
        "how": "Each implementation starts a local HTTP service backed by SQLite, exposes deterministic create/read/update/delete endpoints, and the benchmark driver executes the full CRUD cycle repeatedly with fixed IDs and values.",
        "tests": "This measures service routing plus subprocess or database interaction overhead, request parsing, JSON encoding, and the end-to-end cost of a tiny stateful CRUD API.",
    },
    "socket_programming": {
        "how": "Each implementation starts a minimal TCP echo server and the neutral driver performs repeated loopback connect-send-receive cycles with deterministic payloads of increasing count by input size.",
        "tests": "This isolates low-level networking overhead, socket read/write behavior, connection lifecycle cost, and the ergonomics of implementing a bare-bones network service in each language.",
    },
    "gui_calculator": {
        "how": "Each implementation starts a local HTTP UI that exposes a browser-based calculator contract, and the neutral headless browser driver performs deterministic add/multiply interactions while collecting a checksum from the rendered result state.",
        "tests": "This measures HTTP UI serving overhead plus real browser-side event handling, DOM updates, and the cost of driving a tiny interactive calculator contract through a consistent headless-browser workflow.",
    },
    "data_visualization": {
        "how": "Each implementation starts a local HTTP UI that serves a deterministic visualization page, and the neutral browser driver renders a fixed bar-chart dataset in the DOM and computes a checksum from the resulting bars.",
        "tests": "This benchmarks UI-serving overhead together with browser rendering, DOM construction, layout/style work, and the cost of a simple deterministic data-visualization workflow.",
    },
    "basic_web_application": {
        "how": "Each implementation starts a local HTTP to-do style web application, and the neutral browser driver adds and toggles deterministic tasks before computing a checksum from the rendered list state.",
        "tests": "This measures web-application serving overhead plus browser-side state updates, list rendering, event handling, and the general cost of a small interactive CRUD-style UI contract.",
    },
    "web_scraper": {
        "how": "Each implementation opens a deterministic local fixture site, extracts linked page paths from the index HTML, loads each linked page, and computes a checksum from the scraped titles and paragraph text.",
        "tests": "This measures file/HTML parsing, lightweight extraction logic, repeated document loading, and the overhead of a tiny offline scraping workflow without depending on live websites.",
    },
    "api_client": {
        "how": "Each implementation reads a deterministic mock public-API JSON payload from the fixtures, parses the returned item records, and computes a checksum from IDs, names, and numeric values.",
        "tests": "This benchmarks client-side payload parsing, string extraction, numeric conversion, and the general overhead of consuming a simple third-party style API response.",
    },
    "third_party_api": {
        "how": "Each implementation reads a deterministic Twitter-like mock response from fixtures, extracts post IDs, text bodies, and like counts, and aggregates them into a checksum.",
        "tests": "This stresses semi-structured payload parsing, string-heavy extraction, and the glue code needed to consume a typical social-media style third-party API response.",
    },
    "ai_service_integration": {
        "how": "Each implementation reads a deterministic mock AI-service response set, extracts prompts, outputs, token counts, and the model name, and computes a checksum over the full interaction set.",
        "tests": "This measures integration-style response handling for AI outputs, repeated string processing, token-count extraction, and the runtime overhead of consuming structured mock LLM results offline.",
    },
}

TASK_RELEVANCE = {
    "sort_integers": "Mostly raw CPU throughput and standard-library algorithm efficiency.",
    "matrix_multiplication": "Numeric hot loops and memory locality.",
    "simple_web_server": "Cold-start plus tiny steady-state HTTP service behavior.",
    "csv_parsing": "I/O plus text parsing overhead.",
    "linear_regression": "Numeric/data-processing throughput with light ML-style computation.",
    "rest_api": "Cold-start, request routing, and small JSON API overhead.",
    "file_io_large": "Filesystem streaming and parsing overhead.",
    "binary_search_tree": "Pointer-heavy data structure work and allocation behavior.",
    "prime_sieve": "Algorithmic CPU throughput on tight loops.",
    "tic_tac_toe": "Branch-heavy control flow rather than raw numeric throughput.",
    "chat_application": "TCP startup and tiny message round trips.",
    "basic_blockchain": "Stateful hashing-style computation with sequential dependencies.",
    "web_scraper": "HTML parsing and offline integration glue.",
    "image_resizing": "Pixel-oriented compute with structured file parsing.",
    "sentiment_analysis": "String/token processing and repeated dictionary lookups.",
    "sqlite_crud": "Cold-start plus service/database CRUD overhead.",
    "producer_consumer": "Concurrency-style bookkeeping and queue simulation.",
    "socket_programming": "Low-level networking and echo-style hot path.",
    "gui_calculator": "UI serving plus browser-side interaction overhead.",
    "cli_file_search": "Filesystem traversal and text scanning.",
    "data_visualization": "UI serving plus browser render/layout work.",
    "basic_web_application": "Interactive web CRUD behavior in a browser contract.",
    "api_client": "JSON/API client parsing and glue code.",
    "decision_tree": "Control flow plus ML-style model-building workload.",
    "third_party_api": "Third-party style JSON/integration handling.",
    "ai_service_integration": "Structured AI-style response parsing and integration glue.",
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
def _catalog_by_id() -> dict[str, object]:
    return {task.id: task for task in load_catalog()}


@lru_cache(maxsize=1)
def _tag_to_task_ids() -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for task in load_catalog():
        tags = set(getattr(task, "tags", []) or [])
        tags.add(task.kind)
        for tag in sorted(tags):
            mapping.setdefault(tag, []).append(task.id)
    return mapping


def _featured_tags() -> list[str]:
    return ["compute", "service", "ui", "integration", "io", "ml", "networking"]


def _publish_manifest_path(docs_dir: Path) -> Path:
    return docs_dir / "publish-manifest.json"


def _publish_history_dir(docs_dir: Path) -> Path:
    return docs_dir / "publish-history"


def _stable_results_path(path: Path | str | None) -> str | None:
    if not path:
        return None
    raw = Path(path)
    resolved = raw.resolve()
    try:
        return resolved.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return resolved.as_posix()


def _results_path_from_stable(path: str | Path | None) -> Path | None:
    if not path:
        return None
    raw = Path(path)
    return raw if raw.is_absolute() else ROOT / raw


def _architecture_publish_payload(payload: dict, results_path: Path, docs_dir: Path, previous_manifest: dict | None) -> tuple[dict, Path]:
    """Return the architecture-union payload used for README/report publication.

    Each architecture has one authoritative source artifact. A fresh x86_64 run
    replaces the x86_64 slice; a later aarch64 run replaces only the aarch64
    slice and keeps the latest known x86_64 slice in the published tables.
    """

    current_architectures = _payload_architectures(payload)
    if not current_architectures:
        return payload, results_path

    current_source = _stable_results_path(results_path)
    architecture_results = _previous_architecture_results(previous_manifest)
    for architecture in current_architectures:
        architecture_results[architecture] = current_source
    architecture_results = {
        architecture: source
        for architecture, source in sorted(architecture_results.items())
        if source and _results_path_from_stable(source) and _results_path_from_stable(source).exists()
    }

    if len(architecture_results) <= 1:
        payload["architecture_results"] = architecture_results
        payload["architecture_source_runs"] = _architecture_source_runs(architecture_results, payload, current_source)
        source_notes = dict(payload.get("source_notes") or {})
        source_notes["architecture_sources"] = architecture_results
        payload["source_notes"] = source_notes
        return payload, results_path

    merged = _merge_architecture_sources(architecture_results, payload, current_source)
    target = results_path.parent / "architecture_merged_scored_results.json"
    write_json(target, merged)
    return merged, target


def _previous_architecture_results(previous_manifest: dict | None) -> dict[str, str]:
    if not previous_manifest:
        return {}
    explicit = previous_manifest.get("architecture_results")
    if isinstance(explicit, dict):
        return {
            str(architecture): str(source)
            for architecture, source in explicit.items()
            if architecture and source
        }
    canonical = previous_manifest.get("canonical_results")
    canonical_path = _results_path_from_stable(canonical)
    if not canonical_path or not canonical_path.exists():
        return {}
    try:
        payload = read_json(canonical_path)
    except Exception:
        return {}
    source = _stable_results_path(canonical_path)
    return {architecture: source for architecture in _payload_architectures(payload)}


def _payload_architectures(payload: dict) -> list[str]:
    architectures: set[str] = set()
    for collection_name in ("rows", "medians", "aggregate", "runtimes"):
        for row in payload.get(collection_name) or []:
            architecture = row.get("architecture")
            if architecture:
                architectures.add(str(architecture))
    profile_architectures = (payload.get("profile") or {}).get("architectures") or []
    if isinstance(profile_architectures, str):
        profile_architectures = [profile_architectures]
    for architecture in profile_architectures:
        if architecture and architecture != "host":
            architectures.add(str(architecture))
    host_architecture = (payload.get("host") or {}).get("architecture")
    if host_architecture:
        architectures.add(str(host_architecture))
    return sorted(architectures)


def _architecture_source_runs(architecture_results: dict[str, str], current_payload: dict, current_source: str | None) -> dict[str, dict]:
    runs: dict[str, dict] = {}
    for architecture, source in architecture_results.items():
        if source == current_source:
            source_payload = current_payload
        else:
            source_path = _results_path_from_stable(source)
            if not source_path or not source_path.exists():
                continue
            source_payload = read_json(source_path)
        runs[architecture] = {
            "run_id": source_payload.get("run_id"),
            "results": source,
            "host": (source_payload.get("host") or {}).get("hostname"),
            "architecture": architecture,
        }
    return runs


def _merge_architecture_sources(architecture_results: dict[str, str], current_payload: dict, current_source: str | None) -> dict:
    combined_rows: list[dict] = []
    combined_runtimes: dict[str, dict] = {}
    source_runs = _architecture_source_runs(architecture_results, current_payload, current_source)
    source_payloads: dict[str, dict] = {}
    for source in sorted(set(architecture_results.values())):
        if source == current_source:
            source_payloads[source] = current_payload
            continue
        source_path = _results_path_from_stable(source)
        if source_path and source_path.exists():
            source_payloads[source] = read_json(source_path)

    for architecture, source in architecture_results.items():
        source_payload = source_payloads.get(source)
        if not source_payload:
            continue
        for row in source_payload.get("rows") or []:
            if row.get("architecture") == architecture:
                combined_rows.append(dict(row))
        for runtime in source_payload.get("runtimes") or []:
            if runtime.get("architecture") != architecture:
                continue
            key = str(runtime.get("language") or f"{runtime.get('runtime_id')}@{architecture}")
            combined_runtimes[key] = dict(runtime)

    weights = current_payload.get("weights") or load_weights()
    medians, aggregate = score_results(combined_rows, weights)
    source_notes = dict(current_payload.get("source_notes") or {})
    source_notes["architecture_sources"] = architecture_results
    profile = dict(current_payload.get("profile") or {})
    profile["architectures"] = sorted(architecture_results)
    profile["architecture_sources"] = architecture_results
    merged = {
        **current_payload,
        "host": current_payload.get("host"),
        "profile": profile,
        "runtimes": sorted(combined_runtimes.values(), key=lambda row: str(row.get("language") or "")),
        "rows": combined_rows,
        "medians": medians,
        "aggregate": aggregate,
        "weights": weights,
        "architecture_results": architecture_results,
        "architecture_source_runs": source_runs,
        "source_notes": source_notes,
    }
    return merged


def _current_snapshot_task_ids(payload: dict) -> list[str]:
    return sorted({str(row.get("task_id")) for row in payload.get("medians", []) if row.get("task_id")})


@lru_cache(maxsize=1)
def _catalog_executable_task_ids() -> list[str]:
    return sorted(task.id for task in load_catalog() if getattr(task, "executable", False))


def _snapshot_scope(tasks: list[str]) -> tuple[bool, str, str]:
    full_suite = tasks == _catalog_executable_task_ids()
    if full_suite:
        return True, "full-suite", f"full runnable {len(tasks)}-task suite"
    return False, "published snapshot", f"{len(tasks)}-task published snapshot"


def _history_entries(docs_dir: Path, include_version_matrix: bool = False) -> list[dict]:
    history_dir = _publish_history_dir(docs_dir)
    if not history_dir.exists():
        return []
    rows_by_run_id: dict[str, dict] = {}
    for path in sorted(history_dir.glob("*.json")):
        manifest = read_json(path)
        artifact = manifest.get("version_matrix_results") if include_version_matrix else manifest.get("canonical_results")
        stable_artifact = _stable_results_path(artifact)
        if not stable_artifact:
            continue
        results_path = ROOT / stable_artifact
        if not results_path.exists():
            continue
        payload = read_json(results_path)
        run_id = str(payload.get("run_id") or manifest.get("generated_run_id") or path.stem)
        if run_id in rows_by_run_id:
            continue
        rows_by_run_id[run_id] = {
            "run_id": run_id,
            "results_path": stable_artifact,
            "aggregate": payload.get("aggregate", []),
        }
    return [rows_by_run_id[key] for key in sorted(rows_by_run_id)]


def _latest_version_matrix_history_path(docs_dir: Path) -> str | None:
    rows = _history_entries(docs_dir, include_version_matrix=True)
    if not rows:
        return None
    return rows[-1].get("results_path")


def _load_previous_publish_manifest(docs_dir: Path) -> dict | None:
    path = _publish_manifest_path(docs_dir)
    if not path.exists():
        return None
    return read_json(path)


def _effective_previous_manifest(docs_dir: Path, current_run_id: str, previous_manifest: dict | None) -> dict | None:
    if previous_manifest and previous_manifest.get("generated_run_id") != current_run_id:
        return previous_manifest
    history_rows = _history_entries(docs_dir)
    prior_rows = [row for row in history_rows if row.get("run_id") != current_run_id]
    if not prior_rows:
        return None
    latest = prior_rows[-1]
    return {
        "generated_run_id": latest.get("run_id"),
        "canonical_results": latest.get("results_path"),
    }


def sync_readme(results_path: Path, readme_path: Path, docs_dir: Path) -> Path:
    payload = read_json(results_path)
    previous_manifest = _load_previous_publish_manifest(docs_dir)
    payload, results_path = _architecture_publish_payload(payload, results_path, docs_dir, previous_manifest)
    _archive_publish_history(payload, results_path, docs_dir, previous_manifest)
    report_dir = results_path.parent / "report"
    plot_dir = ensure_dir(docs_dir / "plots")
    _copy_report_plots(results_path, plot_dir)
    versioned = _supplemental_version_payload(payload, docs_dir)
    if versioned:
        version_path = _supplemental_version_path(payload, docs_dir)
        if version_path:
            _copy_report_plots(version_path, plot_dir, prefix="version_")
    section = _build_section(payload, plot_dir.relative_to(readme_path.parent), docs_dir, previous_manifest)
    _write_publish_manifest(payload, results_path, docs_dir, previous_manifest)
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
    else:
        content = "# languages-benchmark\n"
    if MARKER_BEGIN in content and MARKER_END in content:
        before = content.split(MARKER_BEGIN, 1)[0].rstrip()
        after = content.split(MARKER_END, 1)[1].lstrip()
        new_content = f"{before}\n\n{MARKER_BEGIN}\n{section}\n{MARKER_END}\n\n{after}".rstrip() + "\n"
    else:
        new_content = content.rstrip() + f"\n\n{MARKER_BEGIN}\n{section}\n{MARKER_END}\n"
    readme_path.write_text(new_content, encoding="utf-8")
    return readme_path


def _copy_report_plots(results_path: Path, plot_dir: Path, prefix: str = "") -> None:
    report_dir = results_path.parent / "report"
    expected = [report_dir / name for name in PLOT_FILES]
    needs_architecture_plots = False
    if report_dir.exists() and not any(report_dir.glob("arch_*.svg")):
        try:
            needs_architecture_plots = bool(_payload_architectures(read_json(results_path)))
        except Exception:
            needs_architecture_plots = False
    if not report_dir.exists() or not any(report_dir.glob("*.svg")) or any(not path.exists() for path in expected) or needs_architecture_plots:
        from runner.reporting import generate_report

        generate_report(results_path, report_dir)
    for name in PLOT_FILES:
        src = report_dir / name
        if src.exists():
            shutil.copyfile(src, plot_dir / f"{prefix}{name}")
    dynamic_plots = (
        list(report_dir.glob("task_*.svg"))
        + list(report_dir.glob("best_case_task_*.svg"))
        + list(report_dir.glob("task_baseline_*.svg"))
        + list(report_dir.glob("arch_*.svg"))
    )
    for src in sorted(dynamic_plots):
        shutil.copyfile(src, plot_dir / f"{prefix}{src.name}")


def _build_section(payload: dict, plot_rel_dir: Path, docs_dir: Path, previous_manifest: dict | None = None) -> str:
    aggregate = payload.get("aggregate", [])
    medians = payload.get("medians", [])
    host = payload.get("host") or {}
    git = payload.get("git") or {}
    profile = payload.get("profile") or {}
    runtimes = payload.get("runtimes") or []
    fixture_sizes = payload.get("fixture_manifest") or {}
    all_runtimes = _published_runtimes(payload, docs_dir)
    runtime_label_map = _runtime_family_label_map(runtimes)
    _apply_runtime_labels(aggregate, runtime_label_map)
    _apply_runtime_labels(medians, runtime_label_map)
    rubrics = _validated_rubrics()
    weights = payload.get("weights") or load_weights()
    category_rows = split_aggregate_scores(aggregate, weights) if aggregate else {"objective": [], "opinionated": []}
    for rows in category_rows.values():
        _apply_runtime_labels(rows, runtime_label_map)
    run_id = payload.get("run_id", "unknown")
    previous_manifest = _effective_previous_manifest(docs_dir, str(run_id), previous_manifest)
    tasks = _current_snapshot_task_ids(payload)
    full_suite, snapshot_scope_short, snapshot_scope_long = _snapshot_scope(tasks)
    versioned = _supplemental_version_payload(payload, docs_dir)
    comparison_payload = versioned or payload
    comparison_aggregate = comparison_payload.get("aggregate") or []
    comparison_weights = comparison_payload.get("weights") or weights
    comparison_category_rows = split_aggregate_scores(comparison_aggregate, comparison_weights) if comparison_aggregate else {"objective": [], "opinionated": []}
    for rows in comparison_category_rows.values():
        _apply_runtime_labels(rows, runtime_label_map)
    comparison_medians = comparison_payload.get("medians") or []
    _apply_runtime_labels(comparison_aggregate, runtime_label_map)
    _apply_runtime_labels(comparison_medians, runtime_label_map)
    comparison_prefix = "version_" if versioned else ""
    comparison_label = (
        f"the supplemental per-version runtime comparison (`{comparison_payload.get('run_id', 'unknown')}`)"
        if versioned
        else f"this {snapshot_scope_long}"
    )
    plot = lambda name: f"{plot_rel_dir.as_posix()}/{comparison_prefix}{name}"
    service_split_payload = comparison_payload if _has_service_split_data(comparison_medians) else payload
    service_split_medians = service_split_payload.get("medians") or []
    service_split_prefix = "version_" if service_split_payload is comparison_payload and versioned else ""
    service_split_label = (
        f"the supplemental per-version runtime comparison (`{service_split_payload.get('run_id', 'unknown')}`)"
        if service_split_payload is comparison_payload and versioned
        else f"this {snapshot_scope_long}"
    )
    service_plot = lambda name: f"{plot_rel_dir.as_posix()}/{service_split_prefix}{name}"
    has_version_history = len(_history_entries(docs_dir, include_version_matrix=True)) >= 2
    snapshot_scope_line = (
        f"- This snapshot covers the **{snapshot_scope_long}** currently tracked in the benchmark catalog."
        if full_suite
        else f"- This snapshot covers **{len(tasks)} task(s)** from the benchmark catalog; supplemental runs may cover other subsets such as version-matrix comparisons."
    )
    canonical_order = ", ".join(f"`{language}`" for language in _canonical_language_order())
    snapshot_variant_order = ", ".join(
        f"`{row.get('language_label') or row.get('language')}`"
        for row in all_runtimes
    ) if all_runtimes else "n/a"
    lines = [
        "## Latest benchmark snapshot",
        "",
        f"Run ID: `{run_id}`",
        "",
        "### Host / environment",
        "",
    ]
    lines.extend(_host_lines(host))
    lines.extend([
        "",
        "### Git / publish identity",
        "",
    ])
    lines.extend(_git_lines(git))
    lines.extend([
        "",
        "### Publish profile",
        "",
    ])
    lines.extend(_profile_lines(profile))
    lines.extend([
        "",
        "### Runtime versions present in this published snapshot",
        "",
        "Runtime identity is architecture-aware: each row represents a specific language/runtime version on a specific CPU architecture so future ARM, RISC-V, or other host runs can be added without collapsing them into the current x86_64 results.",
        "",
    ])
    lines.extend(_runtime_lines(all_runtimes))
    lines.extend([
        "",
        f"Tasks in this snapshot: {', '.join(f'`{task}`' for task in tasks) if tasks else 'n/a'}",
        "",
        "### Snapshot summary",
        "",
    ])
    lines.extend(_summary_lines(aggregate, category_rows))
    lines.extend([
        "",
        "### Regression vs previous published snapshot",
        "",
    ])
    lines.extend(_regression_summary_lines(payload, previous_manifest))
    lines.extend([
        "",
        "### Machine-readable publish manifest",
        "",
        "- The README publication flow also writes a machine-readable manifest to `docs/publish-manifest.json` so the published snapshot can be audited later.",
        "- Canonical published runs should remain sequential by default even though `./bench run --jobs N` is supported for faster local experimentation.",
        "",
    ])
    lines.extend([
        "",
        "### Artifact/source provenance",
        "",
    ])
    lines.extend(_provenance_lines(payload))
    lines.extend([
        "",
        "### Size legend",
        "",
        "- `S` = **Small** input",
        "- `M` = **Medium** input",
        "- `L` = **Large** input",
        "- These are deterministic fixture sizes defined per task. They do **not** mean the same absolute number of rows/items/bytes for every benchmark; each task has its own `S/M/L` workload specification.",
        "",
        "### How to read these plots",
        "",
        "- The README now contains both **snapshot-scoped plots** and **language best-case plots**.",
        "- **Global comparison plots** rank every runtime/version/architecture row in the active comparison artifact against every other row.",
        "- **Per-architecture plots** filter to one CPU architecture at a time so `x86_64`, `aarch64`, and future architectures can each have their own native truth set.",
        "- The README now contains both **raw-unit plots** and **normalized score plots**.",
        "- **Snapshot-scoped** plots show exactly the runtimes present in the published artifact used to generate this README.",
        "- **Language best-case** plots collapse each language family down to whichever tested version performed best for that specific metric.",
        "- The new **raw-unit** section uses real units wherever possible: CPU and wall time in **ms/s**, memory in **MB/GB**, and implementation size in **lines of code**.",
        "- For those raw-unit plots, **lower is better** and there is no internal inversion.",
        "- For **CPU**, **wall time**, and **memory**, the raw measurements are **lower is better**, but the plotted scores are inverted so **higher is better**.",
        "- **Overall** is a weighted composite score, so **higher is better**.",
        "- **Scalability** is also **higher is better** and reflects how gracefully runtime and memory grow from small to large inputs.",
        f"- The **canonical-order snapshot** plots keep the runtime order actually present in this published artifact: {snapshot_variant_order}.",
        f"- The **canonical-order best-case** plots keep the language-family order from `benchmark.yaml`: {canonical_order}.",
        "- The **ranked** plots reorder languages from best to worst for the specific metric shown in that chart.",
        snapshot_scope_line,
        "",
        "### Metric provenance",
        "",
    ])
    lines.extend(_metric_provenance_lines())
    if versioned:
        lines.extend([
            "",
            "### Per-version methodology notes",
            "",
            "- **Measured at runtime-version level:** CPU, wall time, memory, LOC, startup split, workload split, correctness outputs, and scalability growth inputs.",
            "- **Rubric handling:** runtime variants can now override family-level rubric values for ease/debugging/docs/libraries/concurrency; variants without an override continue inheriting the family default.",
            "- **Community handling:** community inputs still attach to the language family rather than each runtime variant.",
            "- **Best pure runtime comparison:** the per-version raw-unit and objective sections are the cleanest apples-to-apples runtime comparison.",
            "",
        ])
    lines.extend([
        "### Methodology for non-objective and derived criteria",
        "",
        "This benchmark separates **objective/measured** inputs from **derived** and **interpretive** inputs.",
        "",
        "**Measured / objective inputs**",
        "",
        "- **CPU time**: median measured CPU seconds.",
        "- **Wall time**: median measured elapsed seconds.",
        "- **Memory**: median measured peak RSS in MB.",
        "- **LOC**: counted lines of code.",
        "",
        "For lower-is-better objective metrics, the normalized score is:",
        "",
        "- `score = 100 * best / candidate`",
        "",
        "**Scalability**",
        "",
        "Scalability is derived from growth across `S`, `M`, and `L` for each language/task pair rather than taken from one direct measurement.",
        "",
        "For each language/task:",
        "",
        "- `wall_growth = ((M_wall / S_wall) + (L_wall / M_wall)) / 2`",
        "- `memory_growth = ((M_mem / S_mem) + (L_mem / M_mem)) / 2`",
        "- `raw_scalability = (wall_growth + memory_growth) / 2`",
        "",
        "Then it is normalized relative to the best observed raw growth:",
        "",
        "- `scalability_score = 100 * best_raw_scalability / candidate_raw_scalability`",
        "",
        "So **higher scalability score is better** only because lower growth is inverted into a higher score.",
        "",
        "**Other non-objective / interpretive inputs**",
        "",
        "- **Ease**: audited rubric score from `rubrics.yaml` for readability, maintainability, and implementation ergonomics.",
        "- **Debugging**: audited rubric score from `rubrics.yaml` for debugging tools and workflow quality.",
        "- **Docs**: audited rubric score from `rubrics.yaml` for official documentation and learning resources.",
        "- **Libraries**: audited rubric score from `rubrics.yaml` for third-party ecosystem breadth and quality.",
        "- **Concurrency**: audited rubric score from `rubrics.yaml` for support for concurrent/parallel programming.",
        "- **Community**: derived from `community.yaml` as the average of `active_contributors` and `update_cadence`.",
        "- Variants can override family-level rubric inputs, but community is still **language-family-level** today.",
        "",
        "For higher-is-better interpretive metrics, the normalized score is:",
        "",
        "- `score = 100 * candidate / best`",
        "",
        "**Recomputed category scores**",
        "",
        "- **Objective score** uses only CPU, wall, memory, and LOC, with weights renormalized inside that subset.",
        "- **Opinionated score** uses scalability, ease, community, debugging, docs, libraries, and concurrency, with weights renormalized inside that subset.",
        "- **Overall score** blends both groups with the weights from `weights.default.yaml`.",
        "",
        "### Fixture sizes by task",
        "",
    ])
    lines.extend(_fixture_manifest_lines(fixture_sizes))
    lines.extend([
        "",
        "### Correctness verification summary",
        "",
    ])
    lines.extend(_correctness_summary_lines(_correctness_summary(payload.get("rows", []))))
    lines.extend([
        "",
        "### Expected-output manifest check",
        "",
    ])
    lines.extend(_expected_output_lines(payload.get("rows", []), docs_dir))
    lines.extend([
        "",
        "### Correctness digests",
        "",
        "These short hashes summarize the canonical successful output fingerprint for each task/size group.",
        "",
    ])
    lines.extend(_correctness_digest_lines(payload.get("rows", [])))
    lines.extend([
        "",
        "### Service and UI startup vs steady-state",
        "",
        "The benchmark now records startup wait separately from steady-state workload time for service/UI tasks. The table below shows average startup vs average steady-state workload time across service/UI task-size medians for each runtime.",
        f"These startup/workload views use **{service_split_label}**.",
        "",
    ])
    if service_split_payload is payload and versioned:
        lines.extend([
            "The supplemental per-version artifact does not currently include startup/workload split timings, so this section falls back to the canonical published snapshot for now.",
            "",
        ])
    lines.extend(_service_split_lines(service_split_medians))
    lines.extend([
        "",
        f"![Startup-time ranked chart]({service_plot('startup_units_ranked.svg')})",
        "",
        f"![Steady-state workload-time ranked chart]({service_plot('workload_units_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order startup/workload plots</strong></summary>",
        "",
        f"![Startup-time chart]({service_plot('startup_units.svg')})",
        "",
        f"![Steady-state workload-time chart]({service_plot('workload_units.svg')})",
        "",
        "</details>",
        "",
        "### Baseline-relative comparisons",
        "",
    ])
    lines.extend(_baseline_lines(comparison_payload))
    lines.extend([
        "",
        f"![CPU vs baseline ranked chart]({plot('baseline_cpu_ratio_ranked.svg')})",
        "",
        f"![Wall vs baseline ranked chart]({plot('baseline_wall_ratio_ranked.svg')})",
        "",
        f"![Memory vs baseline ranked chart]({plot('baseline_memory_ratio_ranked.svg')})",
        "",
        f"![Overall delta vs baseline ranked chart]({plot('baseline_overall_delta_ranked.svg')})",
        "",
        "### Historical publish trends",
        "",
    ])
    lines.extend(_publish_history_lines(docs_dir))
    lines.extend([
        "",
        f"![Historical overall trend chart]({plot_rel_dir.as_posix()}/history_overall.svg)",
        "",
    ])
    if has_version_history:
        lines.extend([
            f"![Historical version-matrix trend chart]({plot_rel_dir.as_posix()}/history_version_matrix_overall.svg)",
            "",
        ])
    lines.extend([
        "### Category leaderboards",
        "",
        "These recompute the benchmark across tagged subsets of tasks so you can inspect category-specific leaders instead of only the global aggregate.",
        "",
    ])
    lines.extend(_category_score_lines(comparison_payload))
    lines.extend([
        "",
        "### Fixture/workload contract appendix",
        "",
        "This appendix publishes the exact `S/M/L` contract for every runnable task so readers can audit what each benchmark size means.",
        "",
    ])
    lines.extend(_fixture_manifest_lines(fixture_sizes))
    lines.extend(_version_matrix_plot_lines(payload, plot_rel_dir, docs_dir))
    lines.extend(_version_matrix_table_lines(payload, docs_dir))
    family_summary_heading = f"### Language-family summary for this {snapshot_scope_long}" if versioned else f"### Blended overview for this {snapshot_scope_long}"
    if versioned:
        lines.extend([
            "",
            "<details>",
            f"<summary><strong>Show language-family summary for this {snapshot_scope_long}</strong></summary>",
            "",
        ])
    lines.extend([
        "",
        family_summary_heading,
        "",
        f"This family-collapsed summary keeps one **primary runtime** per language family from this **{snapshot_scope_long}** so you can compare the published artifact at the language-family level.",
        "",
        "| Language family | Primary runtime | Overall | Objective | Opinionated | Tasks |",
        "|---|---|---:|---:|---:|---:|",
    ])
    for row in _blended_rows(aggregate, category_rows):
        lines.append(
            f"| {_family_display_name(row)} | {_display_name(row)} | {row['overall_score']:.2f} | {row['objective_score']:.2f} | {row['opinionated_score']:.2f} | {row['tasks_covered']} |"
        )
    lines.extend([
        "",
        f"#### Objective / unopinionated family summary for this {snapshot_scope_long}",
        "",
        "| Language family | Primary runtime | Objective | CPU | Wall | Memory | LOC | Tasks |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ])
    for row in category_rows["objective"]:
        lines.append(
            f"| {_family_display_name(row)} | {_display_name(row)} | {row['objective_score']:.2f} | {row['cpu_score']:.2f} | {row['wall_score']:.2f} | {row['memory_score']:.2f} | {row['loc_score']:.2f} | {row['tasks_covered']} |"
        )
    lines.extend([
        "",
        f"#### Opinionated / interpretive family summary for this {snapshot_scope_long}",
        "",
        "| Language family | Primary runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for row in category_rows["opinionated"]:
        lines.append(
            f"| {_family_display_name(row)} | {_display_name(row)} | {row['opinionated_score']:.2f} | {row['scalability_score']:.2f} | {row['ease_score']:.2f} | {row['community_score']:.2f} | {row['debugging_score']:.2f} | {row['docs_score']:.2f} | {row['libraries_score']:.2f} | {row['concurrency_score']:.2f} | {row['tasks_covered']} |"
        )
    if versioned:
        lines.extend([
            "",
            "</details>",
        ])
    lines.extend([
        "",
        "### Rubric evidence and sources",
        "",
        "These rubric values are language-family level judgments sourced from official or canonical references and used by the opinionated portion of the benchmark. They are reviewed separately from any single benchmark run.",
        "",
    ])
    lines.extend(_rubric_evidence_lines(rubrics))
    lines.extend(_architecture_plot_lines(comparison_payload, plot_rel_dir, docs_dir, comparison_prefix, comparison_label))
    lines.extend([
        "",
        f"### Global raw-unit plots for {comparison_label}",
        "",
        "These global plots use real units rather than internal normalized scores and compare every runtime/version/architecture row in the active comparison view against every other row. CPU and wall time are shown as total median time, memory is shown as average median peak RSS, and LOC is shown as average lines per task.",
        "",
        "**CPU time (ranked):** raw total CPU time across the suite; **lower is better**.",
        "",
        f"![CPU raw-unit ranked chart]({plot('cpu_units_ranked.svg')})",
        "",
        "**Wall time (ranked):** raw total elapsed time across the suite; **lower is better**.",
        "",
        f"![Wall raw-unit ranked chart]({plot('wall_units_ranked.svg')})",
        "",
        "**Memory (ranked):** average median peak RSS; **lower is better**.",
        "",
        f"![Memory raw-unit ranked chart]({plot('memory_units_ranked.svg')})",
        "",
        "**LOC (ranked):** average lines of code per task; **lower is better**.",
        "",
        f"![LOC raw-unit ranked chart]({plot('loc_units_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order raw-unit plots for this snapshot</strong></summary>",
        "",
        "These plots keep the fixed configured runtime-variant order instead of sorting by performance.",
        "",
        f"![CPU raw-unit chart]({plot('cpu_units.svg')})",
        "",
        f"![Wall raw-unit chart]({plot('wall_units.svg')})",
        "",
        f"![Memory raw-unit chart]({plot('memory_units.svg')})",
        "",
        f"![LOC raw-unit chart]({plot('loc_units.svg')})",
        "",
        "</details>",
        "",
        "### Language best-case raw-unit plots",
        "",
        "These charts collapse the runtime variants and keep only the best measured version for each language family for the metric being plotted.",
        "",
        f"![Best-case CPU raw-unit ranked chart]({plot('best_case_cpu_units_ranked.svg')})",
        "",
        f"![Best-case Wall raw-unit ranked chart]({plot('best_case_wall_units_ranked.svg')})",
        "",
        f"![Best-case Memory raw-unit ranked chart]({plot('best_case_memory_units_ranked.svg')})",
        "",
        f"![Best-case LOC raw-unit ranked chart]({plot('best_case_loc_units_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order best-case raw-unit plots</strong></summary>",
        "",
        "These plots keep the fixed canonical language-family order instead of sorting by performance.",
        "",
        f"![Best-case CPU raw-unit chart]({plot('best_case_cpu_units.svg')})",
        "",
        f"![Best-case Wall raw-unit chart]({plot('best_case_wall_units.svg')})",
        "",
        f"![Best-case Memory raw-unit chart]({plot('best_case_memory_units.svg')})",
        "",
        f"![Best-case LOC raw-unit chart]({plot('best_case_loc_units.svg')})",
        "",
        "</details>",
        "",
        "### Objective / unopinionated score plots",
        "",
        "These recomputed score plots keep only directly measurable benchmark dimensions. They intentionally exclude scalability and all rubric/community-driven scores.",
        "",
        "**Objective score (ranked):** recomputed from CPU, wall, memory, and LOC only; **higher is better**.",
        "",
        f"![Objective ranked score chart]({plot('objective_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order objective plots</strong></summary>",
        "",
        "**Objective score (canonical):** same metric in fixed benchmark language order.",
        "",
        f"![Objective score chart]({plot('objective.svg')})",
        "",
        "**Objective component score plots:** normalized objective-only views of CPU, wall, memory, and LOC.",
        "",
        f"![CPU score chart]({plot('cpu.svg')})",
        "",
        f"![Wall score chart]({plot('wall.svg')})",
        "",
        f"![Memory score chart]({plot('memory.svg')})",
        "",
        f"![LOC score chart]({plot('loc.svg')})",
        "",
        "</details>",
        "",
        "**Objective component score plots (ranked):** normalized objective-only views of CPU, wall, memory, and LOC sorted best to worst.",
        "",
        f"![CPU ranked score chart]({plot('cpu_ranked.svg')})",
        "",
        f"![Wall ranked score chart]({plot('wall_ranked.svg')})",
        "",
        f"![Memory ranked score chart]({plot('memory_ranked.svg')})",
        "",
        f"![LOC ranked score chart]({plot('loc_ranked.svg')})",
        "",
        "### Language best-case objective / unopinionated score plots",
        "",
        f"![Best-case objective ranked score chart]({plot('best_case_objective_ranked.svg')})",
        "",
        f"![Best-case CPU ranked score chart]({plot('best_case_cpu_ranked.svg')})",
        "",
        f"![Best-case Wall ranked score chart]({plot('best_case_wall_ranked.svg')})",
        "",
        f"![Best-case Memory ranked score chart]({plot('best_case_memory_ranked.svg')})",
        "",
        f"![Best-case LOC ranked score chart]({plot('best_case_loc_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order best-case objective plots</strong></summary>",
        "",
        f"![Best-case objective score chart]({plot('best_case_objective.svg')})",
        "",
        f"![Best-case CPU score chart]({plot('best_case_cpu.svg')})",
        "",
        f"![Best-case Wall score chart]({plot('best_case_wall.svg')})",
        "",
        f"![Best-case Memory score chart]({plot('best_case_memory.svg')})",
        "",
        f"![Best-case LOC score chart]({plot('best_case_loc.svg')})",
        "",
        "</details>",
        "",
        "### Geometric-mean runtime views",
        "",
        "These views reduce the influence of extreme outliers by taking the geometric mean of normalized per-task/per-size runtime efficiency ratios.",
        "",
        f"![CPU geometric-mean ranked chart]({plot('cpu_geomean_ranked.svg')})",
        "",
        f"![Wall-time geometric-mean ranked chart]({plot('wall_geomean_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order geometric-mean plots</strong></summary>",
        "",
        f"![CPU geometric-mean chart]({plot('cpu_geomean.svg')})",
        "",
        f"![Wall-time geometric-mean chart]({plot('wall_geomean.svg')})",
        "",
        "</details>",
        "",
        "### Variance / confidence summary",
        "",
        "These plots summarize average coefficient of variation across the measured medians. Lower values mean less relative run-to-run variation.",
        "",
        f"![CPU variance ranked chart]({plot('variance_cpu_ranked.svg')})",
        "",
        f"![Wall variance ranked chart]({plot('variance_wall_ranked.svg')})",
        "",
        f"![Memory variance ranked chart]({plot('variance_memory_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order variance plots</strong></summary>",
        "",
        f"![CPU variance chart]({plot('variance_cpu.svg')})",
        "",
        f"![Wall variance chart]({plot('variance_wall.svg')})",
        "",
        f"![Memory variance chart]({plot('variance_memory.svg')})",
        "",
        "</details>",
        "",
        "### Opinionated / interpretive score plots",
        "",
        "These recomputed score plots keep only interpretive or hybrid dimensions, including scalability and rubric/community-style scores.",
        "",
        "**Opinionated score (ranked):** recomputed from scalability, ease, community, debugging, docs, libraries, and concurrency; **higher is better**.",
        "",
        f"![Opinionated ranked score chart]({plot('opinionated_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order opinionated plots</strong></summary>",
        "",
        "**Opinionated score (canonical):** same metric in fixed benchmark language order.",
        "",
        f"![Opinionated score chart]({plot('opinionated.svg')})",
        "",
        "**Scalability remains visible here because it belongs to the interpretive/hybrid category in this split.**",
        "",
        f"![Scalability chart]({plot('scalability.svg')})",
        "",
        "</details>",
        "",
        f"![Scalability ranked chart]({plot('scalability_ranked.svg')})",
        "",
        "### Language best-case opinionated / interpretive score plots",
        "",
        f"![Best-case opinionated ranked score chart]({plot('best_case_opinionated_ranked.svg')})",
        "",
        f"![Best-case scalability ranked chart]({plot('best_case_scalability_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order best-case opinionated plots</strong></summary>",
        "",
        f"![Best-case opinionated score chart]({plot('best_case_opinionated.svg')})",
        "",
        f"![Best-case scalability chart]({plot('best_case_scalability.svg')})",
        "",
        "</details>",
        "",
        "### Blended composite plots sorted best to worst",
        "",
        "These are the legacy blended plots that combine both objective and opinionated inputs into one composite view. They are kept for reference, but the split sections above are the primary interpretation.",
        "",
        "**Overall score (ranked):** best weighted composite score appears first; **higher is better**.",
        "",
        f"![Overall ranked score chart]({plot('overall_ranked.svg')})",
        "",
        "**CPU efficiency score (ranked):** best CPU efficiency appears first; **lower raw CPU time = higher plotted score**.",
        "",
        f"![CPU ranked score chart]({plot('cpu_ranked.svg')})",
        "",
        "**Wall-clock efficiency score (ranked):** best elapsed-time efficiency appears first; **lower raw runtime = higher plotted score**.",
        "",
        f"![Wall ranked score chart]({plot('wall_ranked.svg')})",
        "",
        "**Memory efficiency score (ranked):** best memory efficiency appears first; **lower raw memory usage = higher plotted score**.",
        "",
        f"![Memory ranked score chart]({plot('memory_ranked.svg')})",
        "",
        "**Scalability score (ranked):** best aggregate scalability score appears first; **higher is better**.",
        "",
        f"![Scalability ranked chart]({plot('scalability_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order blended composite plots</strong></summary>",
        "",
        "### Blended composite plots in canonical language order",
        "",
        f"These plots keep the same left-to-right language order every time: {canonical_order}.",
        "",
        "**Overall score:** weighted composite benchmark score; **higher is better**.",
        "",
        f"![Overall score chart]({plot('overall.svg')})",
        "",
        "**CPU efficiency score:** derived from raw CPU time; **lower raw CPU time = higher plotted score**.",
        "",
        f"![CPU score chart]({plot('cpu.svg')})",
        "",
        "**Wall-clock efficiency score:** derived from elapsed runtime; **lower raw runtime = higher plotted score**.",
        "",
        f"![Wall score chart]({plot('wall.svg')})",
        "",
        "**Memory efficiency score:** derived from max RSS memory; **lower raw memory usage = higher plotted score**.",
        "",
        f"![Memory score chart]({plot('memory.svg')})",
        "",
        "**Scalability score:** aggregate score derived from S → M → L growth; **higher is better**.",
        "",
        f"![Scalability chart]({plot('scalability.svg')})",
        "",
        "</details>",
        "",
        "### Blended composite plots as language best-case scenarios",
        "",
        "These charts keep only the best-performing tested version of each language for the metric being plotted.",
        "",
        f"![Best-case overall ranked score chart]({plot('best_case_overall_ranked.svg')})",
        "",
        f"![Best-case CPU ranked score chart]({plot('best_case_cpu_ranked.svg')})",
        "",
        f"![Best-case Wall ranked score chart]({plot('best_case_wall_ranked.svg')})",
        "",
        f"![Best-case Memory ranked score chart]({plot('best_case_memory_ranked.svg')})",
        "",
        f"![Best-case Scalability ranked chart]({plot('best_case_scalability_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order best-case blended plots</strong></summary>",
        "",
        f"![Best-case overall score chart]({plot('best_case_overall.svg')})",
        "",
        f"![Best-case CPU score chart]({plot('best_case_cpu.svg')})",
        "",
        f"![Best-case Wall score chart]({plot('best_case_wall.svg')})",
        "",
        f"![Best-case Memory score chart]({plot('best_case_memory.svg')})",
        "",
        f"![Best-case Scalability chart]({plot('best_case_scalability.svg')})",
        "",
        "</details>",
        "",
        "### Scalability growth charts",
        "",
        "The old scalability curves were too abstract and often looked flat because they were based on a score that did not vary by size. These updated charts now use actual growth ratios derived from measured medians, so they are easier to read. In every chart below, **lower is better**.",
        "",
        "**Wall-time growth curves (ranked legend):** S is fixed at **1.0x** and M/L show average wall-time growth relative to S.",
        "",
        f"![Wall-time growth curve ranked legend]({plot('scalability_curve_ranked.svg')})",
        "",
        "**Memory growth curves (ranked legend):** S is fixed at **1.0x** and M/L show average memory growth relative to S.",
        "",
        f"![Memory growth curve ranked legend]({plot('scalability_memory_curve_ranked.svg')})",
        "",
        "**L/S ratio summary bars (ranked):** side-by-side bars compare final large-vs-small growth for wall time and memory.",
        "",
        f"![L/S growth ratio summary ranked]({plot('scalability_growth_ratios_ranked.svg')})",
        "",
        "<details>",
        "<summary><strong>Show canonical-order scalability growth charts</strong></summary>",
        "",
        f"![Wall-time growth curve]({plot('scalability_curve.svg')})",
        "",
        f"![Memory growth curve]({plot('scalability_memory_curve.svg')})",
        "",
        f"![L/S growth ratio summary]({plot('scalability_growth_ratios.svg')})",
        "",
        "</details>",
        "",
        "### Per-task score plots",
        "",
        "The sections below avoid reducing the suite to one global aggregate. Each task gets its own score plot for all tested runtime variants and then a language best-case view.",
        "",
    ])
    lines.extend(_task_plot_lines(tasks, plot_rel_dir, versioned))
    lines.extend([
        "",
        "### Per-task raw numeric tables",
        "",
        "Each task also includes the measured medians, standard deviation, and min→max range for CPU time, wall time, and memory.",
        f"These per-task tables use the supplemental version-matrix medians when they are available, so runtime variants such as multiple Python, PHP, or JavaScript runtimes are listed individually instead of being collapsed to one primary runtime per family.",
        "",
    ])
    lines.extend(_task_raw_table_lines(versioned.get("medians", medians) if versioned else medians, tasks, versioned=bool(versioned)))
    lines.extend([
        "",
        "### What the current executable tests do",
        "",
        "This published snapshot uses deterministic local fixtures and a checksum-style output for each task so every language performs the same work and produces a comparable, verifiable result.",
        "",
    ])
    lines.extend(_task_explanation_lines(tasks))
    lines.extend([
        "",
        "### What this benchmark is not",
        "",
        "- It is **not** a universal truth about a language; it is a comparison across this repository's fixed workload mix.",
        "- It is **not** using every ecosystem's most highly optimized specialist library for every task.",
        "- It is **not** a substitute for benchmarking your own production workload on your own hardware.",
        "",
        "> Generated from the latest scored benchmark run via `./bench report --results ... --update-readme`.",
    ])
    return "\n".join(lines)


def _summary_lines(aggregate: list[dict], category_rows: dict[str, list[dict]]) -> list[str]:
    if not aggregate:
        return ["No aggregate results were available for this snapshot."]
    lines = []
    if category_rows.get("objective"):
        top = category_rows["objective"][0]
        runner_up = category_rows["objective"][1] if len(category_rows["objective"]) > 1 else None
        suffix = f"; next is **{_display_name(runner_up)}** at **{runner_up['objective_score']:.2f}**" if runner_up else ""
        lines.append(f"- **Objective leader:** **{_display_name(top)}** at **{top['objective_score']:.2f}**{suffix}.")
    if category_rows.get("opinionated"):
        top = category_rows["opinionated"][0]
        runner_up = category_rows["opinionated"][1] if len(category_rows["opinionated"]) > 1 else None
        suffix = f"; next is **{_display_name(runner_up)}** at **{runner_up['opinionated_score']:.2f}**" if runner_up else ""
        lines.append(f"- **Opinionated leader:** **{_display_name(top)}** at **{top['opinionated_score']:.2f}**{suffix}.")
    metric_defs = [
        ("cpu_score", "Best CPU efficiency"),
        ("wall_score", "Best wall-clock efficiency"),
        ("memory_score", "Best memory efficiency"),
        ("scalability_score", "Best scalability"),
    ]
    for metric, label in metric_defs:
        ranked = sorted(aggregate, key=lambda row: float(row.get(metric, 0) or 0), reverse=True)
        top = ranked[0]
        runner_up = ranked[1] if len(ranked) > 1 else None
        suffix = f"; next is **{_display_name(runner_up)}** at **{runner_up[metric]:.2f}**" if runner_up else ""
        lines.append(f"- **{label}:** **{_display_name(top)}** at **{top[metric]:.2f}**{suffix}.")
    return lines


def _display_name(row: dict) -> str:
    language = str(row.get("language") or "")
    return str(row.get("language_label") or LANGUAGE_LABELS.get(language, language))


def _family_display_name(row: dict) -> str:
    family = row.get("language_family")
    if family:
        return LANGUAGE_LABELS.get(str(family), str(family))
    language = str(row.get("language") or "")
    if language in LANGUAGE_LABELS:
        return LANGUAGE_LABELS[language]
    for candidate, label in LANGUAGE_LABELS.items():
        if language.startswith(f"{candidate}-"):
            return label
    return language


def _validated_rubrics() -> dict:
    rubrics = load_rubrics()
    required_numeric = ["ease", "debugging", "docs", "libraries", "concurrency"]
    for language in _canonical_language_order():
        if language not in rubrics:
            raise ValueError(f"Missing rubric entry for {language}")
        row = rubrics[language]
        for key in required_numeric:
            if key not in row:
                raise ValueError(f"Missing rubric score '{key}' for {language}")
        if not row.get("reviewed_at"):
            raise ValueError(f"Missing reviewed_at for {language}")
        evidence = row.get("evidence")
        if not isinstance(evidence, dict):
            raise ValueError(f"Expected structured evidence object for {language}")
        if not evidence.get("summary"):
            raise ValueError(f"Missing evidence.summary for {language}")
        rationale = evidence.get("rationale")
        if not isinstance(rationale, dict):
            raise ValueError(f"Missing evidence.rationale mapping for {language}")
        for key in required_numeric:
            if not rationale.get(key):
                raise ValueError(f"Missing evidence.rationale.{key} for {language}")
        sources = evidence.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValueError(f"Missing evidence.sources for {language}")
        for idx, source in enumerate(sources):
            if not isinstance(source, dict):
                raise ValueError(f"Invalid source entry {idx} for {language}")
            for field in ["label", "url", "kind"]:
                if not source.get(field):
                    raise ValueError(f"Missing source field '{field}' in rubric for {language}")
    return rubrics


def _rubric_evidence_lines(rubrics: dict) -> list[str]:
    lines: list[str] = []
    for language in _canonical_language_order():
        row = rubrics[language]
        evidence = row["evidence"]
        label = LANGUAGE_LABELS.get(language, language)
        lines.extend([
            "<details>",
            f"<summary><strong>{label}</strong> — reviewed {row['reviewed_at']}</summary>",
            "",
            f"- **Scores:** ease {row['ease']}/10, debugging {row['debugging']}/10, docs {row['docs']}/10, libraries {row['libraries']}/10, concurrency {row['concurrency']}/10",
            f"- **Summary:** {evidence['summary']}",
            "",
            "Category rationale:",
            "",
            f"- **Ease:** {evidence['rationale']['ease']}",
            f"- **Debugging:** {evidence['rationale']['debugging']}",
            f"- **Docs:** {evidence['rationale']['docs']}",
            f"- **Libraries:** {evidence['rationale']['libraries']}",
            f"- **Concurrency:** {evidence['rationale']['concurrency']}",
            "",
            "Sources:",
            "",
        ])
        for source in evidence["sources"]:
            lines.append(f"- [{source['label']}]({source['url']}) — {source['kind']}")
        lines.extend(["", "</details>", ""])
    return lines


def _version_matrix_table_lines(payload: dict, docs_dir: Path) -> list[str]:
    versioned = _supplemental_version_payload(payload, docs_dir)
    if not versioned:
        return []
    aggregate = versioned.get("aggregate") or []
    if not aggregate:
        return []
    runtimes = versioned.get("runtimes") or []
    weights = versioned.get("weights") or payload.get("weights") or load_weights()
    runtime_label_map = _runtime_family_label_map(runtimes)
    _apply_runtime_labels(aggregate, runtime_label_map)
    category_rows = split_aggregate_scores(aggregate, weights)
    for rows in category_rows.values():
        _apply_runtime_labels(rows, runtime_label_map)
    tasks = sorted({row.get("task_id") for row in versioned.get("medians", []) if row.get("task_id")})
    catalog_tasks = sorted(task_id for task_id, task in _catalog_by_id().items() if getattr(task, "executable", False))
    full_suite = tasks == catalog_tasks
    coverage_label = "full 26-task suite" if full_suite else f"{len(tasks)}-task subset"
    lines = [
        "",
        "### Per-version score tables",
        "",
        f"These tables show the **version-matrix comparison snapshot** from `{versioned.get('run_id', 'unknown')}`. This is a supplemental view so that all benchmarked runtime versions appear in README tables too.",
        (
            f"**Important:** this per-version comparison now covers the **full 26-task suite**. "
            if full_suite
            else f"**Important:** this per-version comparison currently covers only a **{len(tasks)}-task subset**, not the full 26-task suite. "
        )
        + f"Tasks in this supplemental run: {', '.join(f'`{task}`' for task in tasks) if tasks else 'n/a'}.",
        "These tables are rescored from one combined raw-row comparison pool, so the normalization is consistent across all listed runtime versions.",
        "Interpretive inputs such as rubric/community are still shared at the language-family level today, so the **objective** per-version table is the cleanest pure runtime comparison.",
        "",
        f"#### Per-version blended overview ({coverage_label})",
        "",
        "| Runtime | Overall | Objective | Opinionated | Tasks |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in _blended_rows(aggregate, category_rows):
        lines.append(
            f"| {_display_name(row)} | {row['overall_score']:.2f} | {row['objective_score']:.2f} | {row['opinionated_score']:.2f} | {row['tasks_covered']} |"
        )
    lines.extend([
        "",
        f"#### Per-version objective results ({coverage_label})",
        "",
        "| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ])
    for row in category_rows["objective"]:
        lines.append(
            f"| {_display_name(row)} | {row['objective_score']:.2f} | {row['cpu_score']:.2f} | {row['wall_score']:.2f} | {row['memory_score']:.2f} | {row['loc_score']:.2f} | {row['tasks_covered']} |"
        )
    lines.extend([
        "",
        f"#### Per-version opinionated results ({coverage_label})",
        "",
        "| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for row in category_rows["opinionated"]:
        lines.append(
            f"| {_display_name(row)} | {row['opinionated_score']:.2f} | {row['scalability_score']:.2f} | {row['ease_score']:.2f} | {row['community_score']:.2f} | {row['debugging_score']:.2f} | {row['docs_score']:.2f} | {row['libraries_score']:.2f} | {row['concurrency_score']:.2f} | {row['tasks_covered']} |"
        )
    return lines


def _version_matrix_plot_lines(payload: dict, plot_rel_dir: Path, docs_dir: Path) -> list[str]:
    versioned = _supplemental_version_payload(payload, docs_dir)
    if not versioned:
        return []
    tasks = sorted({row.get("task_id") for row in versioned.get("medians", []) if row.get("task_id")})
    catalog_tasks = sorted(task_id for task_id, task in _catalog_by_id().items() if getattr(task, "executable", False))
    full_suite = tasks == catalog_tasks
    coverage_label = "full 26-task suite" if full_suite else f"{len(tasks)}-task subset"
    return [
        "",
        "### Per-version plots",
        "",
        f"These plots come from the **version-matrix comparison snapshot** `{versioned.get('run_id', 'unknown')}` and show every benchmarked runtime variant separately.",
        (
            f"**Important:** this per-version snapshot now covers the **full 26-task suite**. "
            if full_suite
            else f"**Important:** this per-version snapshot currently covers only a **{len(tasks)}-task subset**, not the full 26-task suite. "
        )
        + f"Tasks in this supplemental run: {', '.join(f'`{task}`' for task in tasks) if tasks else 'n/a'}.",
        "The **objective** per-version plots are the fairest runtime-vs-runtime view. The **opinionated** per-version plots still include shared family-level rubric/community inputs, so variants from the same language family can remain artificially close on those dimensions.",
        "",
        f"#### Per-version raw-unit plots ({coverage_label})",
        "",
        f"![Per-version CPU raw-unit ranked chart]({plot_rel_dir.as_posix()}/version_cpu_units_ranked.svg)",
        "",
        f"![Per-version wall raw-unit ranked chart]({plot_rel_dir.as_posix()}/version_wall_units_ranked.svg)",
        "",
        f"![Per-version memory raw-unit ranked chart]({plot_rel_dir.as_posix()}/version_memory_units_ranked.svg)",
        "",
        f"![Per-version LOC raw-unit ranked chart]({plot_rel_dir.as_posix()}/version_loc_units_ranked.svg)",
        "",
        "<details>",
        "<summary><strong>Show canonical-order per-version raw-unit plots</strong></summary>",
        "",
        f"![Per-version CPU raw-unit chart]({plot_rel_dir.as_posix()}/version_cpu_units.svg)",
        "",
        f"![Per-version wall raw-unit chart]({plot_rel_dir.as_posix()}/version_wall_units.svg)",
        "",
        f"![Per-version memory raw-unit chart]({plot_rel_dir.as_posix()}/version_memory_units.svg)",
        "",
        f"![Per-version LOC raw-unit chart]({plot_rel_dir.as_posix()}/version_loc_units.svg)",
        "",
        "</details>",
        "",
        f"#### Per-version normalized score plots ({coverage_label})",
        "",
        f"![Per-version objective ranked score chart]({plot_rel_dir.as_posix()}/version_objective_ranked.svg)",
        "",
        f"![Per-version opinionated ranked score chart]({plot_rel_dir.as_posix()}/version_opinionated_ranked.svg)",
        "",
        f"![Per-version overall ranked score chart]({plot_rel_dir.as_posix()}/version_overall_ranked.svg)",
        "",
        f"![Per-version scalability ranked score chart]({plot_rel_dir.as_posix()}/version_scalability_ranked.svg)",
        "",
        "<details>",
        "<summary><strong>Show canonical-order per-version normalized score plots</strong></summary>",
        "",
        f"![Per-version objective score chart]({plot_rel_dir.as_posix()}/version_objective.svg)",
        "",
        f"![Per-version opinionated score chart]({plot_rel_dir.as_posix()}/version_opinionated.svg)",
        "",
        f"![Per-version overall score chart]({plot_rel_dir.as_posix()}/version_overall.svg)",
        "",
        f"![Per-version scalability score chart]({plot_rel_dir.as_posix()}/version_scalability.svg)",
        "",
        "</details>",
        "",
        f"#### Per-version scalability growth plots ({coverage_label})",
        "",
        f"![Per-version wall-time growth curve ranked legend]({plot_rel_dir.as_posix()}/version_scalability_curve_ranked.svg)",
        "",
        f"![Per-version memory growth curve ranked legend]({plot_rel_dir.as_posix()}/version_scalability_memory_curve_ranked.svg)",
        "",
        f"![Per-version L/S growth ratio summary ranked]({plot_rel_dir.as_posix()}/version_scalability_growth_ratios_ranked.svg)",
        "",
        "<details>",
        "<summary><strong>Show canonical-order per-version scalability growth plots</strong></summary>",
        "",
        f"![Per-version wall-time growth curve]({plot_rel_dir.as_posix()}/version_scalability_curve.svg)",
        "",
        f"![Per-version memory growth curve]({plot_rel_dir.as_posix()}/version_scalability_memory_curve.svg)",
        "",
        f"![Per-version L/S growth ratio summary]({plot_rel_dir.as_posix()}/version_scalability_growth_ratios.svg)",
        "",
        "</details>",
        "",
    ]


def _safe_architecture_stem(architecture: str, stem: str) -> str:
    safe_architecture = "".join(ch if ch.isalnum() else "_" for ch in architecture).strip("_") or "unknown"
    return f"arch_{safe_architecture}_{stem}"


def _architecture_plot_lines(payload: dict, plot_rel_dir: Path, docs_dir: Path, prefix: str, comparison_label: str) -> list[str]:
    architectures = sorted({
        str(row.get("architecture"))
        for row in payload.get("aggregate", [])
        if row.get("architecture") and row.get("architecture") != "unknown"
    })
    if not architectures:
        return []
    plot_dir = docs_dir / "plots"
    sections: list[str] = [
        "",
        f"### Per-architecture plots for {comparison_label}",
        "",
        "These plots filter the active comparison artifact to one CPU architecture at a time. Use them when you want the native truth for a specific architecture without mixing it with other machines. The global sections below still compare every runtime/version/architecture row together.",
        "",
    ]
    rendered_any = False
    for architecture in architectures:
        def plot_name(stem: str) -> str:
            return f"{prefix}{_safe_architecture_stem(architecture, stem)}"

        required = plot_dir / f"{plot_name('overall')}_ranked.svg"
        if not required.exists():
            continue
        rendered_any = True
        sections.extend([
            "<details>",
            f"<summary><strong>{architecture}</strong> native-only plots</summary>",
            "",
            f"These charts include only runtime rows whose normalized architecture is `{architecture}`.",
            "",
            f"![{architecture} overall ranked score chart]({plot_rel_dir.as_posix()}/{plot_name('overall')}_ranked.svg)",
            "",
            f"![{architecture} objective ranked score chart]({plot_rel_dir.as_posix()}/{plot_name('objective')}_ranked.svg)",
            "",
            f"![{architecture} opinionated ranked score chart]({plot_rel_dir.as_posix()}/{plot_name('opinionated')}_ranked.svg)",
            "",
            f"![{architecture} CPU raw-unit ranked chart]({plot_rel_dir.as_posix()}/{plot_name('cpu_units')}_ranked.svg)",
            "",
            f"![{architecture} wall raw-unit ranked chart]({plot_rel_dir.as_posix()}/{plot_name('wall_units')}_ranked.svg)",
            "",
            f"![{architecture} memory raw-unit ranked chart]({plot_rel_dir.as_posix()}/{plot_name('memory_units')}_ranked.svg)",
            "",
            f"![{architecture} scalability growth ranked chart]({plot_rel_dir.as_posix()}/{plot_name('scalability_growth_ratios')}_ranked.svg)",
            "",
            "<details>",
            f"<summary><strong>Show canonical-order {architecture} plots</strong></summary>",
            "",
            f"![{architecture} overall canonical score chart]({plot_rel_dir.as_posix()}/{plot_name('overall')}.svg)",
            "",
            f"![{architecture} objective canonical score chart]({plot_rel_dir.as_posix()}/{plot_name('objective')}.svg)",
            "",
            f"![{architecture} opinionated canonical score chart]({plot_rel_dir.as_posix()}/{plot_name('opinionated')}.svg)",
            "",
            f"![{architecture} CPU raw-unit canonical chart]({plot_rel_dir.as_posix()}/{plot_name('cpu_units')}.svg)",
            "",
            f"![{architecture} wall raw-unit canonical chart]({plot_rel_dir.as_posix()}/{plot_name('wall_units')}.svg)",
            "",
            f"![{architecture} memory raw-unit canonical chart]({plot_rel_dir.as_posix()}/{plot_name('memory_units')}.svg)",
            "",
            f"![{architecture} wall-time growth curve]({plot_rel_dir.as_posix()}/{plot_name('scalability_curve')}.svg)",
            "",
            "</details>",
            "",
            "</details>",
            "",
        ])
    return sections if rendered_any else []


def _supplemental_version_payload(payload: dict, docs_dir: Path | None = None) -> dict | None:
    path = _supplemental_version_path(payload, docs_dir)
    if not path:
        return None
    return read_json(path)


def _supplemental_version_path(payload: dict, docs_dir: Path | None = None) -> Path | None:
    source_notes = payload.get("source_notes") or {}
    source_path = _stable_results_path(source_notes.get("version_matrix_source") or source_notes.get("runtime_metadata_source"))
    if not source_path and docs_dir is not None:
        source_path = _latest_version_matrix_history_path(docs_dir)
    if not source_path:
        return None
    path = ROOT / str(source_path)
    if not path.exists():
        return None
    return path


def _published_runtimes(payload: dict, docs_dir: Path | None = None) -> list[dict]:
    canonical = payload.get("runtimes") or []
    supplemental = (_supplemental_version_payload(payload, docs_dir) or {}).get("runtimes") or []
    merged: dict[str, dict] = {}
    for row in [*canonical, *supplemental]:
        language = row.get("language")
        if not language:
            continue
        merged[str(language)] = row
    ordered = []
    variant_order = _canonical_variant_order()
    def runtime_order_id(row: dict) -> str:
        return str(row.get("runtime_id") or row.get("language") or "").split("@", 1)[0]

    for variant in variant_order:
        for language, row in merged.items():
            if runtime_order_id(row) == variant and row not in ordered:
                ordered.append(row)
    for language, row in merged.items():
        if row not in ordered:
            ordered.append(row)
    return ordered


def _runtime_family_label_map(runtimes: list[dict]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for row in runtimes:
        label = row.get("language_label") or row.get("language")
        if not label:
            continue
        family = row.get("language_family")
        language = row.get("language")
        if family:
            mapping[str(family)] = str(label)
        if language:
            mapping[str(language)] = str(label)
    return mapping


def _apply_runtime_labels(rows: list[dict], runtime_label_map: dict[str, str]) -> None:
    for row in rows:
        if row.get("language_label"):
            continue
        language = row.get("language")
        if language in runtime_label_map:
            row["language_label"] = runtime_label_map[str(language)]


def _host_lines(host: dict) -> list[str]:
    if not host:
        return ["Host metadata was not available in this results file."]
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
    lines = ["| Field | Value |", "|---|---|"]
    for key, label in labels:
        value = host.get(key)
        if value in {None, ""}:
            continue
        escaped = str(value).replace("|", "\\|")
        lines.append(f"| {label} | {escaped} |")
    return lines if len(lines) > 2 else ["Host metadata was not available in this results file."]


def _git_lines(git: dict) -> list[str]:
    if not git:
        return ["Git metadata was not available in this results file."]
    labels = [
        ("branch", "Branch"),
        ("commit", "Commit"),
        ("commit_short", "Short commit"),
        ("dirty", "Dirty working tree"),
    ]
    lines = ["| Field | Value |", "|---|---|"]
    for key, label in labels:
        value = git.get(key)
        if value in {None, ""}:
            continue
        lines.append(f"| {label} | {str(value).replace('|', '\\|')} |")
    return lines if len(lines) > 2 else ["Git metadata was not available in this results file."]


def _runtime_lines(runtimes: list[dict]) -> list[str]:
    if not runtimes:
        return ["Runtime version metadata was not available in this results file."]
    lines = [
        "| Runtime | Family | Architecture | Configured version | Reported version | Image |",
        "|---|---|---|---|---|---|",
    ]
    for row in runtimes:
        lines.append(
            f"| {_display_name(row)} | {row.get('language_family', '')} | {row.get('architecture', '')} | {row.get('configured_version', '')} | {row.get('reported_version', '')} | {_normalized_image_label(row.get('image', ''))} |"
        )
    return lines


def _normalized_image_label(image: object) -> str:
    text = str(image or "")
    text = text.replace("multi-benchmark:", "languages-benchmark:")
    return text.replace("|", "\\|")


def _write_publish_manifest(payload: dict, results_path: Path, docs_dir: Path, previous_manifest: dict | None = None) -> Path:
    source_notes = payload.get("source_notes") or {}
    config = load_app_config()
    profile = payload.get("profile") or {"preset": None, "iterations": config.iterations, "warmups": config.warmups, "jobs": 1, "baseline_runtime": config.baseline_runtime, "engine": config.engine}
    generated_from = _stable_results_path(results_path)
    version_matrix_source = _stable_results_path(source_notes.get("version_matrix_source"))
    runtime_metadata_source = _stable_results_path(source_notes.get("runtime_metadata_source"))
    javascript_runtime_source = _stable_results_path(source_notes.get("javascript_runtime_source"))
    previous_reference = None
    if previous_manifest and previous_manifest.get("generated_run_id") != payload.get("run_id"):
        previous_reference = _stable_results_path(previous_manifest.get("canonical_results"))
    manifest = {
        "generated_from": generated_from,
        "generated_run_id": payload.get("run_id"),
        "canonical_results": generated_from,
        "version_matrix_results": version_matrix_source,
        "runtime_metadata_source": runtime_metadata_source,
        "javascript_runtime_source": javascript_runtime_source,
        "architecture_results": payload.get("architecture_results") or {},
        "architecture_source_runs": payload.get("architecture_source_runs") or {},
        "host": payload.get("host"),
        "git": payload.get("git"),
        "profile": profile,
        "previous_manifest": previous_reference,
    }
    path = _publish_manifest_path(docs_dir)
    write_json(path, manifest)
    return path


def _archive_publish_history(payload: dict, results_path: Path, docs_dir: Path, previous_manifest: dict | None = None) -> None:
    source_notes = payload.get("source_notes") or {}
    config = load_app_config()
    profile = payload.get("profile") or {"preset": None, "iterations": config.iterations, "warmups": config.warmups, "jobs": 1, "baseline_runtime": config.baseline_runtime, "engine": config.engine}
    generated_from = _stable_results_path(results_path)
    version_matrix_source = _stable_results_path(source_notes.get("version_matrix_source"))
    runtime_metadata_source = _stable_results_path(source_notes.get("runtime_metadata_source"))
    javascript_runtime_source = _stable_results_path(source_notes.get("javascript_runtime_source"))
    previous_reference = None
    if previous_manifest and previous_manifest.get("generated_run_id") != payload.get("run_id"):
        previous_reference = _stable_results_path(previous_manifest.get("canonical_results"))
    manifest = {
        "generated_from": generated_from,
        "generated_run_id": payload.get("run_id"),
        "canonical_results": generated_from,
        "version_matrix_results": version_matrix_source,
        "runtime_metadata_source": runtime_metadata_source,
        "javascript_runtime_source": javascript_runtime_source,
        "architecture_results": payload.get("architecture_results") or {},
        "architecture_source_runs": payload.get("architecture_source_runs") or {},
        "host": payload.get("host"),
        "git": payload.get("git"),
        "profile": profile,
        "previous_manifest": previous_reference,
    }
    history_dir = ensure_dir(_publish_history_dir(docs_dir))
    if manifest.get("generated_run_id"):
        write_json(history_dir / f"{manifest['generated_run_id']}.json", manifest)


def _format_seconds(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 1000:.3f} ms" if value < 1.0 else f"{value:.4f} s"


def _format_memory(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value / 1024:.3f} GB" if value >= 1024.0 else f"{value:.3f} MB"


def _format_percent(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.2f}%"


def _metric_provenance_lines() -> list[str]:
    rows = [
        ("CPU / Wall / Memory / LOC", "Measured", "Directly measured from benchmark execution or LOC counting."),
        ("Scalability", "Derived", "Computed from S→M→L wall-time and memory growth ratios."),
        ("Community", "Derived", "Computed from checked-in contributor/update-cadence inputs."),
        ("Ease / Debugging / Docs / Libraries / Concurrency", "Rubric", "Checked-in rubric values with evidence and sources."),
        ("Objective / Opinionated / Overall", "Derived", "Recomputed aggregate scores built from the inputs above."),
    ]
    lines = ["| Metric group | Type | Meaning |", "|---|---|---|"]
    for a, b, c in rows:
        lines.append(f"| {a} | **{b}** | {c} |")
    return lines


def _fixture_manifest_lines(manifest: dict[str, dict[str, str]]) -> list[str]:
    if not manifest:
        return ["Fixture-size metadata was not available in this results file."]
    lines = ["| Task | S | M | L |", "|---|---|---|---|"]
    for task_id in sorted(manifest):
        sizes = manifest[task_id]
        lines.append(f"| `{task_id}` | {sizes.get('s', 'n/a')} | {sizes.get('m', 'n/a')} | {sizes.get('l', 'n/a')} |")
    return lines


def _correctness_summary(rows: list[dict]) -> dict:
    grouped: dict[tuple[str, str], set[str]] = {}
    for row in rows:
        if row.get("status") != "ok":
            continue
        key = (str(row.get("task_id")), str(row.get("size")))
        grouped.setdefault(key, set()).add(str(row.get("stdout", "")))
    mismatches = [{"task_id": task_id, "size": size, "distinct_outputs": len(outputs)} for (task_id, size), outputs in sorted(grouped.items()) if len(outputs) > 1]
    return {"groups_checked": len(grouped), "mismatch_count": len(mismatches), "mismatches": mismatches}


def _correctness_summary_lines(summary: dict) -> list[str]:
    if summary["mismatch_count"] == 0:
        return [f"**0 mismatches** across {summary['groups_checked']} task/size groups in this artifact."]
    lines = [f"**{summary['mismatch_count']} mismatches** across {summary['groups_checked']} task/size groups.", "", "| Task | Size | Distinct outputs |", "|---|---|---:|"]
    for row in summary["mismatches"]:
        lines.append(f"| `{row['task_id']}` | `{str(row['size']).upper()}` | {row['distinct_outputs']} |")
    return lines


def _correctness_digest_rows(rows: list[dict]) -> list[dict]:
    import hashlib

    grouped: dict[tuple[str, str], set[str]] = {}
    for row in rows:
        if row.get("status") != "ok":
            continue
        key = (str(row.get("task_id")), str(row.get("size")))
        grouped.setdefault(key, set()).add(str(row.get("stdout", "")))
    output = []
    for (task_id, size), outputs in sorted(grouped.items()):
        canonical = sorted(outputs)[0] if outputs else ""
        digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:12] if canonical else ""
        preview = canonical.strip().replace("\n", "\\n")
        output.append({
            "task_id": task_id,
            "size": size,
            "digest": digest,
            "distinct_outputs": len(outputs),
            "preview": preview[:64] + ("…" if len(preview) > 64 else ""),
        })
    return output


def _correctness_digest_lines(rows: list[dict]) -> list[str]:
    digest_rows = _correctness_digest_rows(rows)
    if not digest_rows:
        return ["No successful outputs were available to build correctness digests."]
    lines = [
        "| Task | Size | Digest | Distinct outputs | Canonical output preview |",
        "|---|---|---|---:|---|",
    ]
    for row in digest_rows:
        lines.append(
            f"| `{row['task_id']}` | `{str(row['size']).upper()}` | `{row['digest']}` | {row['distinct_outputs']} | `{row['preview']}` |"
        )
    return lines


def _service_split_rows(medians: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = {}
    for row in medians:
        if row.get("startup_wall_seconds") is not None or row.get("workload_wall_seconds") is not None:
            grouped.setdefault(str(row["language"]), []).append(row)
    rows = []
    for language, bucket in grouped.items():
        startup = [float(row.get("startup_wall_seconds") or 0) for row in bucket if row.get("startup_wall_seconds") is not None]
        workload = [float(row.get("workload_wall_seconds") or 0) for row in bucket if row.get("workload_wall_seconds") is not None]
        rows.append({
            "language": language,
            "runtime_id": bucket[0].get("runtime_id", language),
            "architecture": bucket[0].get("architecture", "unknown"),
            "language_label": bucket[0].get("language_label", language),
            "samples": len(bucket),
            "startup_wall_avg": sum(startup) / len(startup) if startup else 0.0,
            "startup_wall_avg_ci95": (1.96 * pstdev(startup) / (len(startup) ** 0.5)) if len(startup) > 1 else 0.0,
            "workload_wall_avg": sum(workload) / len(workload) if workload else 0.0,
            "workload_wall_avg_ci95": (1.96 * pstdev(workload) / (len(workload) ** 0.5)) if len(workload) > 1 else 0.0,
        })
    canonical = _canonical_variant_order()
    return sorted(rows, key=lambda row: canonical.index(str(row.get("runtime_id") or row["language"]).split("@", 1)[0]) if str(row.get("runtime_id") or row["language"]).split("@", 1)[0] in canonical else 999)


def _has_service_split_data(medians: list[dict]) -> bool:
    return any(row.get("startup_wall_seconds") is not None or row.get("workload_wall_seconds") is not None for row in medians)


def _service_split_lines(medians: list[dict]) -> list[str]:
    rows = _service_split_rows(medians)
    if not rows:
        return ["No startup/workload split timings were available in this results file."]
    lines = [
        "| Runtime | Task/size medians used | Avg startup | Avg steady-state workload | Avg total |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        total = row["startup_wall_avg"] + row["workload_wall_avg"]
        lines.append(
            f"| {_display_name(row)} | {row['samples']} | {_format_seconds(row['startup_wall_avg'])} ± {_format_seconds(row.get('startup_wall_avg_ci95'))} | {_format_seconds(row['workload_wall_avg'])} ± {_format_seconds(row.get('workload_wall_avg_ci95'))} | {_format_seconds(total)} |"
        )
    return lines


def _profile_lines(profile: dict) -> list[str]:
    config = load_app_config()
    effective = {
        "preset": profile.get("preset") if profile else None,
        "iterations": profile.get("iterations") if profile else config.iterations,
        "warmups": profile.get("warmups") if profile else config.warmups,
        "jobs": profile.get("jobs") if profile else 1,
        "architectures": profile.get("architectures") if profile else config.architectures,
        "baseline_runtime": profile.get("baseline_runtime") if profile else config.baseline_runtime,
        "engine": profile.get("engine") if profile else config.engine,
    }
    rows = [
        ("Preset", effective.get("preset") or "manual / inherited"),
        ("Iterations", effective.get("iterations")),
        ("Warmups", effective.get("warmups")),
        ("Jobs", effective.get("jobs")),
        ("Architectures", ", ".join(effective.get("architectures") or [])),
        ("Baseline runtime", effective.get("baseline_runtime")),
        ("Engine", effective.get("engine")),
    ]
    lines = ["| Field | Value |", "|---|---|"]
    for label, value in rows:
        if value in {None, ""}:
            continue
        lines.append(f"| {label} | {str(value).replace('|', '\\|')} |")
    return lines


def _regression_summary_lines(payload: dict, previous_manifest: dict | None) -> list[str]:
    if not previous_manifest:
        return ["No previous publish manifest was available, so no regression baseline could be computed yet."]
    previous_path = _stable_results_path(previous_manifest.get("canonical_results"))
    current_run_id = payload.get("run_id")
    if not previous_path:
        return ["The previous publish manifest did not record a canonical results artifact."]
    previous_file = ROOT / str(previous_path)
    if not previous_file.exists():
        return [f"Previous canonical artifact `{previous_path}` is not available locally."]
    previous_payload = read_json(previous_file)
    if previous_payload.get("run_id") == current_run_id:
        return ["The previous publish manifest points to the same canonical artifact, so there is no earlier baseline to compare against."]
    prev = {row["language"]: row for row in previous_payload.get("aggregate", [])}
    curr = {row["language"]: row for row in payload.get("aggregate", [])}
    lines = ["| Runtime | Overall Δ | Objective Δ | Opinionated Δ |", "|---|---:|---:|---:|"]
    changed = False
    current_weights = payload.get("weights") or load_weights()
    current_split = split_aggregate_scores(payload.get("aggregate", []), current_weights)
    prev_split = split_aggregate_scores(previous_payload.get("aggregate", []), previous_payload.get("weights") or current_weights)
    curr_objective = {row["language"]: row for row in current_split["objective"]}
    curr_opinionated = {row["language"]: row for row in current_split["opinionated"]}
    prev_objective = {row["language"]: row for row in prev_split["objective"]}
    prev_opinionated = {row["language"]: row for row in prev_split["opinionated"]}
    for language in sorted(set(prev) & set(curr)):
        changed = True
        overall_delta = float(curr[language]["overall_score"]) - float(prev[language]["overall_score"])
        objective_delta = float(curr_objective[language]["objective_score"]) - float(prev_objective[language]["objective_score"])
        opinionated_delta = float(curr_opinionated[language]["opinionated_score"]) - float(prev_opinionated[language]["opinionated_score"])
        lines.append(f"| {_display_name(curr[language])} | {overall_delta:+.2f} | {objective_delta:+.2f} | {opinionated_delta:+.2f} |")
    return lines if changed else ["No overlapping runtime rows were available for regression comparison."]


def _baseline_rows(payload: dict) -> tuple[str, list[dict]]:
    profile = payload.get("profile") or {}
    baseline_runtime = str(profile.get("baseline_runtime") or load_app_config().baseline_runtime)
    config = load_app_config()
    baseline_family = config.language_variants.get(baseline_runtime, {}).get("family", baseline_runtime)
    aggregate = payload.get("aggregate") or []
    medians = payload.get("medians") or []
    raw_grouped: dict[str, list[dict]] = {}
    for row in medians:
        raw_grouped.setdefault(str(row.get("language")), []).append(row)
    raw_rows = {}
    for language, bucket in raw_grouped.items():
        raw_rows[language] = {
            "cpu_seconds_total": sum(float(row.get("cpu_seconds", 0) or 0) for row in bucket),
            "wall_seconds_total": sum(float(row.get("wall_seconds", 0) or 0) for row in bucket),
            "memory_mb_avg": sum(float(row.get("max_rss_mb", 0) or 0) for row in bucket) / max(len(bucket), 1),
        }
    aggregate_by_language = {row["language"]: row for row in aggregate}
    baseline_agg = (
        aggregate_by_language.get(baseline_runtime)
        or next((row for row in aggregate if row.get("runtime_id") == baseline_runtime), None)
        or aggregate_by_language.get(baseline_family)
        or next((row for row in aggregate if row.get("language_family") == baseline_family), None)
    )
    baseline_raw = (
        raw_rows.get(baseline_runtime)
        or next((raw_rows.get(str(row.get("language"))) for row in medians if row.get("runtime_id") == baseline_runtime and raw_rows.get(str(row.get("language")))), None)
        or raw_rows.get(baseline_family)
        or next((raw_rows.get(str(row.get("language"))) for row in medians if row.get("language_family") == baseline_family and raw_rows.get(str(row.get("language")))), None)
    )
    if not baseline_agg or not baseline_raw:
        return baseline_runtime, []
    rows = []
    for row in aggregate:
        language = row["language"]
        raw = raw_rows.get(language)
        if not raw:
            continue
        rows.append({
            "language": language,
            "language_label": row.get("language_label", language),
            "cpu_ratio_vs_baseline": raw["cpu_seconds_total"] / max(baseline_raw["cpu_seconds_total"], 1e-9),
            "wall_ratio_vs_baseline": raw["wall_seconds_total"] / max(baseline_raw["wall_seconds_total"], 1e-9),
            "memory_ratio_vs_baseline": raw["memory_mb_avg"] / max(baseline_raw["memory_mb_avg"], 1e-9),
            "overall_delta_vs_baseline": float(row.get("overall_score", 0) or 0) - float(baseline_agg.get("overall_score", 0) or 0),
        })
    return baseline_runtime, rows


def _baseline_lines(payload: dict) -> list[str]:
    baseline_runtime, rows = _baseline_rows(payload)
    if not rows:
        return [f"Configured baseline runtime `{baseline_runtime}` was not present in this artifact."]
    lines = [
        f"Baseline runtime: `{baseline_runtime}`",
        "",
        "| Runtime | CPU vs baseline | Wall vs baseline | Memory vs baseline | Overall Δ vs baseline |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {_display_name(row)} | {row['cpu_ratio_vs_baseline']:.2f}x | {row['wall_ratio_vs_baseline']:.2f}x | {row['memory_ratio_vs_baseline']:.2f}x | {row['overall_delta_vs_baseline']:+.2f} |"
        )
    return lines


def _publish_history_lines(docs_dir: Path) -> list[str]:
    history_rows = _history_entries(docs_dir)
    if not history_rows:
        return ["No archived publish-history snapshots were available yet."]
    lines = ["| Run ID | Top overall runtime | Top score | Runtime rows |", "|---|---|---:|---:|"]
    for item in history_rows:
        aggregate = item.get("aggregate", [])
        top = max(aggregate, key=lambda row: float(row.get("overall_score", 0) or 0), default=None)
        top_runtime = _display_name(top) if top else "n/a"
        top_score = f"{float(top.get('overall_score', 0) or 0):.2f}" if top else "n/a"
        lines.append(f"| `{item['run_id']}` | {top_runtime} | {top_score} | {len(aggregate)} |")
    return lines


def _expected_outputs_path(docs_dir: Path) -> Path:
    return docs_dir / "expected-outputs.json"


def _expected_output_lines(rows: list[dict], docs_dir: Path) -> list[str]:
    path = _expected_outputs_path(docs_dir)
    if not path.exists():
        return ["No checked-in expected-output manifest was available yet."]
    manifest = read_json(path)
    expected = manifest.get("expected_outputs", {})
    current = {f"{row['task_id']}:{str(row['size']).lower()}": row for row in _correctness_digest_rows(rows)}
    mismatches = []
    for key, row in current.items():
        want = expected.get(key)
        if not want:
            mismatches.append((key, row["digest"], "missing"))
        elif want.get("digest") != row["digest"]:
            mismatches.append((key, row["digest"], want.get("digest")))
    if not mismatches:
        return [f"All {len(current)} current task/size output digests matched the checked-in expected-output manifest."]
    lines = ["| Task/size | Current digest | Expected digest |", "|---|---|---|"]
    for key, got, want in mismatches:
        lines.append(f"| `{key}` | `{got}` | `{want}` |")
    return lines


def _provenance_lines(payload: dict) -> list[str]:
    source_notes = payload.get("source_notes") or {}
    lines = ["| Published view | Source artifact |", "|---|---|"]
    lines.append(f"| Canonical README/report snapshot | `{payload.get('run_id', 'unknown')}` |")
    architecture_sources = source_notes.get("architecture_sources") or payload.get("architecture_results") or {}
    if isinstance(architecture_sources, dict) and architecture_sources:
        for architecture, source in sorted(architecture_sources.items()):
            lines.append(f"| Architecture truth: `{architecture}` | `{_stable_results_path(source)}` |")
    for label, key in [
        ("Version-matrix supplemental view", "version_matrix_source"),
        ("Runtime metadata source", "runtime_metadata_source"),
        ("JavaScript runtime comparison source", "javascript_runtime_source"),
    ]:
        if source_notes.get(key):
            lines.append(f"| {label} | `{_stable_results_path(source_notes[key])}` |")
    return lines


def _category_score_lines(payload: dict) -> list[str]:
    weights = payload.get("weights") or load_weights()
    rows = payload.get("rows") or []
    snapshot_task_ids = {str(row.get("task_id")) for row in rows if row.get("task_id")}
    lines: list[str] = []
    for tag in _featured_tags():
        task_ids = set(_tag_to_task_ids().get(tag, [])) & snapshot_task_ids
        if not task_ids:
            continue
        _medians, aggregate = aggregate_for_task_ids(rows, weights, task_ids)
        if not aggregate:
            continue
        category_rows = split_aggregate_scores(aggregate, weights)
        lines.extend([
            f"#### `{tag}`",
            "",
            f"Tasks: {', '.join(f'`{task_id}`' for task_id in sorted(task_ids))}",
            "",
            "| Runtime | Overall | Objective | Opinionated | Tasks |",
            "|---|---:|---:|---:|---:|",
        ])
        for row in _blended_rows(aggregate, category_rows):
            lines.append(
                f"| {_display_name(row)} | {row['overall_score']:.2f} | {row['objective_score']:.2f} | {row['opinionated_score']:.2f} | {row['tasks_covered']} |"
            )
        lines.extend([
            "",
            "| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ])
        for row in category_rows["objective"]:
            lines.append(
                f"| {_display_name(row)} | {row['objective_score']:.2f} | {row['cpu_score']:.2f} | {row['wall_score']:.2f} | {row['memory_score']:.2f} | {row['loc_score']:.2f} | {row['tasks_covered']} |"
            )
        lines.extend([
            "",
            "| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ])
        for row in category_rows["opinionated"]:
            lines.append(
                f"| {_display_name(row)} | {row['opinionated_score']:.2f} | {row['scalability_score']:.2f} | {row['ease_score']:.2f} | {row['community_score']:.2f} | {row['debugging_score']:.2f} | {row['docs_score']:.2f} | {row['libraries_score']:.2f} | {row['concurrency_score']:.2f} | {row['tasks_covered']} |"
            )
        lines.extend(["", ""])
    return lines or ["No category leaderboards were available."]


def _task_implementation_links(task_id: str) -> str:
    links = []
    for language in _canonical_language_order():
        path = _task_source_path(language, task_id)
        if path.exists():
            rel = path.relative_to(ROOT)
            links.append(f"[{LANGUAGE_LABELS.get(language, language)}]({rel.as_posix()})")
    return " · ".join(links)


def _blended_rows(aggregate: list[dict], category_rows: dict[str, list[dict]]) -> list[dict]:
    objective_by_language = {row["language"]: row for row in category_rows.get("objective", [])}
    opinionated_by_language = {row["language"]: row for row in category_rows.get("opinionated", [])}
    rows = []
    for row in aggregate:
        objective = objective_by_language.get(row["language"], {})
        opinionated = opinionated_by_language.get(row["language"], {})
        rows.append({
            "language": row["language"],
            "language_label": row.get("language_label", row["language"]),
            "overall_score": float(row.get("overall_score", 0) or 0),
            "objective_score": float(objective.get("objective_score", 0) or 0),
            "opinionated_score": float(opinionated.get("opinionated_score", 0) or 0),
            "tasks_covered": row.get("tasks_covered", 0),
        })
    return sorted(rows, key=lambda row: row["overall_score"], reverse=True)


def _task_explanation_lines(task_ids: list[str]) -> list[str]:
    lines: list[str] = []
    catalog = _catalog_by_id()
    for task_id in task_ids:
        task = catalog.get(task_id)
        meta = TASK_EXPLANATIONS.get(task_id)
        if task is None or meta is None:
            continue
        lines.extend([
            f"#### `{task_id}` — {task.name}",
            "",
            f"- **How it works:** {meta['how']}",
            f"- **What it tests:** {meta['tests']}",
            f"- **Why this task matters:** {TASK_RELEVANCE.get(task_id, 'Representative benchmark workload.')}",
            f"- **Tags:** {', '.join(f'`{tag}`' for tag in (getattr(task, 'tags', []) or [task.kind]))}",
            f"- **Input sizes:** `{', '.join(task.sizes)}`",
            f"- **Implementations:** {_task_implementation_links(task_id) or 'n/a'}",
            "",
        ])
    return lines


def _task_plot_lines(task_ids: list[str], plot_rel_dir: Path, versioned: dict | None = None) -> list[str]:
    lines: list[str] = []
    catalog = _catalog_by_id()
    prefix = "version_" if versioned else ""
    scope = "Per-version" if versioned else "Snapshot-scoped"
    for task_id in task_ids:
        task = catalog.get(task_id)
        if task is None:
            continue
        lines.extend([
            "<details>",
            f"<summary><strong>{task_id}</strong> — {task.name}</summary>",
            "",
            f"{scope} ranked plot first, then {scope.lower()} canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:",
            "",
            f"![{task_id} ranked score chart]({plot_rel_dir.as_posix()}/{prefix}task_{task_id}_ranked.svg)",
            "",
            f"![{task_id} canonical score chart]({plot_rel_dir.as_posix()}/{prefix}task_{task_id}.svg)",
            "",
            f"![{task_id} best-case ranked score chart]({plot_rel_dir.as_posix()}/{prefix}best_case_task_{task_id}_ranked.svg)",
            "",
            f"![{task_id} best-case canonical score chart]({plot_rel_dir.as_posix()}/{prefix}best_case_task_{task_id}.svg)",
            "",
            f"![{task_id} baseline delta ranked chart]({plot_rel_dir.as_posix()}/{prefix}task_baseline_{task_id}_ranked.svg)",
            "",
            "</details>",
            "",
        ])
    return lines


def _task_raw_table_lines(medians: list[dict], task_ids: list[str], versioned: bool = False) -> list[str]:
    lines: list[str] = []
    grouped: dict[str, list[dict]] = {}
    for row in medians:
        grouped.setdefault(row["task_id"], []).append(row)
    canonical = _canonical_variant_order()
    size_order = {"s": 0, "m": 1, "l": 2}
    catalog = _catalog_by_id()
    for task_id in task_ids:
        task = catalog.get(task_id)
        if task is None:
            continue
        rows = sorted(
            grouped.get(task_id, []),
            key=lambda row: (
                canonical.index(str(row.get("runtime_id") or row.get("language", "")).split("@", 1)[0]) if str(row.get("runtime_id") or row.get("language", "")).split("@", 1)[0] in canonical else 999,
                size_order.get(row.get("size"), 999),
            ),
        )
        if versioned:
            header = "| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |"
            sep = "|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|"
        else:
            header = "| Language family | Primary runtime | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |"
            sep = "|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|"
        lines.extend([
            "<details>",
            f"<summary><strong>{task_id}</strong> — {task.name}</summary>",
            "",
            header,
            sep,
        ])
        for row in rows:
            left = _display_name(row) if versioned else _family_display_name(row)
            right = _family_display_name(row) if versioned else _display_name(row)
            lines.append(
                f"| {left} | {right} | {str(row.get('size', '')).upper()} | {int(row.get('sample_count', 0) or 0)} | "
                f"{_format_seconds(row.get('cpu_seconds'))} | {_format_seconds(row.get('cpu_stddev_seconds'))} | {_format_seconds(row.get('cpu_ci95_seconds'))} | {_format_seconds(row.get('cpu_min_seconds'))} → {_format_seconds(row.get('cpu_max_seconds'))} | "
                f"{_format_seconds(row.get('wall_seconds'))} | {_format_seconds(row.get('wall_stddev_seconds'))} | {_format_seconds(row.get('wall_ci95_seconds'))} | {_format_seconds(row.get('wall_min_seconds'))} → {_format_seconds(row.get('wall_max_seconds'))} | "
                f"{_format_memory(row.get('max_rss_mb'))} | {_format_memory(row.get('memory_stddev_mb'))} | {_format_memory(row.get('memory_ci95_mb'))} | {_format_memory(row.get('memory_min_mb'))} → {_format_memory(row.get('memory_max_mb'))} | "
                f"{int(row.get('loc', 0) or 0)} |"
            )
        lines.extend(["", "</details>", ""])
    return lines


def _task_source_path(language: str, task_id: str) -> Path:
    base = ROOT / "tasks" / "implementations" / language
    if language == "rust":
        return base / "tasks" / f"{task_id}.rs"
    extension = {
        "php": "php",
        "python": "py",
        "java": "java",
        "cpp": "cpp",
        "node": "js",
        "go": "go",
    }[language]
    return base / "tasks" / f"{task_id}.{extension}"
