from pathlib import Path
from runner.cli import main
from runner.config import ROOT


def test_dry_run_creates_results(tmp_path, monkeypatch):
    monkeypatch.chdir(ROOT)
    latest_link = ROOT / "results" / "latest"
    previous_latest = latest_link.resolve() if latest_link.exists() else None
    assert main(["run", "--tasks", "smoke", "--langs", "python,go", "--sizes", "s,m,l", "--iterations", "1", "--warmups", "1", "--dry-run"]) == 0
    latest = ROOT / "results" / "latest" / "raw_results.json"
    assert latest.exists()
    created_run_dir = latest.parent.resolve()
    assert main(["score", "--results", str(latest)]) == 0
    scored = ROOT / "results" / "latest" / "scored_results.json"
    assert scored.exists()
    assert main(["report", "--results", str(scored)]) == 0
    assert (ROOT / "results" / "latest" / "report" / "report.html").exists()
    if latest_link.is_symlink():
        latest_link.unlink()
    if created_run_dir.exists():
        import shutil
        shutil.rmtree(created_run_dir)
    if previous_latest is not None and previous_latest.exists():
        latest_link.symlink_to(previous_latest, target_is_directory=True)


def test_dry_run_respects_zero_warmups(monkeypatch):
    monkeypatch.chdir(ROOT)
    latest_link = ROOT / "results" / "latest"
    previous_latest = latest_link.resolve() if latest_link.exists() else None
    assert main(["run", "--tasks", "sort_integers", "--langs", "python-3.12", "--sizes", "s", "--iterations", "1", "--warmups", "0", "--dry-run"]) == 0
    latest = ROOT / "results" / "latest" / "raw_results.json"
    created_run_dir = latest.parent.resolve()
    payload = __import__("json").load(latest.open())
    statuses = [row["status"] for row in payload["rows"]]
    assert statuses == ["ok"]
    assert payload["runtimes"][0]["runtime_id"] == "python-3.12"
    assert payload["runtimes"][0]["architecture"]
    assert payload["rows"][0]["architecture"] == payload["runtimes"][0]["architecture"]
    if latest_link.is_symlink():
        latest_link.unlink()
    if created_run_dir.exists():
        import shutil
        shutil.rmtree(created_run_dir)
    if previous_latest is not None and previous_latest.exists():
        latest_link.symlink_to(previous_latest, target_is_directory=True)


def test_publish_bundle_dry_run_writes_unique_run_artifacts(monkeypatch):
    monkeypatch.chdir(ROOT)
    bundles_dir = ROOT / "results" / "bundles"
    before = {path.name for path in bundles_dir.iterdir()} if bundles_dir.exists() else set()
    assert main([
        "publish-bundle",
        "--tasks", "sort_integers",
        "--langs", "python-3.12",
        "--sizes", "s",
        "--dry-run",
        "--reruns", "2",
    ]) == 0
    after = {path.name for path in bundles_dir.iterdir()} if bundles_dir.exists() else set()
    created = sorted(after - before)
    assert created
    bundle_dir = bundles_dir / created[-1]
    manifest = __import__("json").load((bundle_dir / "bundle_manifest.json").open())
    assert manifest["reruns"] == 2
    scored_paths = [run["scored_results"] for run in manifest["runs"]]
    assert len(scored_paths) == len(set(scored_paths))
    import shutil
    shutil.rmtree(bundle_dir)
