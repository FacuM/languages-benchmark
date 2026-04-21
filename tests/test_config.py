from runner.config import ROOT, load_app_config, load_catalog, load_weights, load_rubrics, load_community
from runner.utils import read_json


def test_config_loads():
    cfg = load_app_config()
    assert cfg.engine == "docker"
    assert "python" in cfg.languages


def test_catalog_has_full_list():
    catalog = load_catalog()
    assert len(catalog) == 26
    assert any(task.id == "sort_integers" and task.executable for task in catalog)
    assert all(task.tags for task in catalog)


def test_support_data_complete():
    weights = load_weights()
    rubrics = load_rubrics()
    community = load_community()
    assert round(sum(weights.values()), 2) == 1.0
    assert set(rubrics) == set(community)


def test_rubrics_have_structured_evidence():
    rubrics = load_rubrics()
    required_numeric = {"ease", "debugging", "docs", "libraries", "concurrency"}
    for language, row in rubrics.items():
        assert required_numeric.issubset(row)
        assert row["reviewed_at"]
        evidence = row["evidence"]
        assert evidence["summary"]
        assert required_numeric.issubset(evidence["rationale"])
        assert evidence["sources"]
        for source in evidence["sources"]:
            assert source["label"]
            assert source["url"]
            assert source["kind"]


def test_expected_outputs_manifest_exists_for_all_task_sizes():
    manifest = read_json(ROOT / "docs" / "expected-outputs.json")
    assert manifest["source_run_id"]
    expected = manifest["expected_outputs"]
    catalog = load_catalog()
    assert len(expected) == sum(len(task.sizes) for task in catalog)
    assert "sort_integers:s" in expected
