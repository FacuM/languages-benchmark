# languages-benchmark

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Docker-first, Python-orchestrated multi-language benchmark framework for PHP, Python, Java, C++, Node.js, Go, and Rust.

## Features
- Single CLI entrypoint: `./bench`
- Deterministic fixture generation
- Docker-first engine adapter with Podman-compatible command surface
- Raw JSON + CSV + static HTML/SVG reporting
- Weighted scoring with overrideable weights and rubric/community inputs
- Full benchmark catalog metadata with executable smoke tasks implemented across all seven languages
- README sync that embeds the latest benchmark plots directly into repository documentation

## Implemented benchmark tasks
Executable today:
- `sort_integers`
- `matrix_multiplication`
- `simple_web_server`
- `csv_parsing`
- `linear_regression`
- `rest_api`
- `file_io_large`
- `binary_search_tree`
- `prime_sieve`
- `tic_tac_toe`
- `chat_application`
- `basic_blockchain`
- `image_resizing`
- `sentiment_analysis`
- `sqlite_crud`
- `producer_consumer`
- `socket_programming`
- `gui_calculator`
- `cli_file_search`
- `data_visualization`
- `basic_web_application`
- `api_client`
- `decision_tree`
- `third_party_api`
- `ai_service_integration`
- `web_scraper`

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
./bench setup
./bench run --tasks smoke --langs all --sizes s,m,l --iterations 2
./bench score --results results/latest/raw_results.json
./bench report --results results/latest/scored_results.json --update-readme
```

You can also refresh only the README benchmark section from any scored run:

```bash
./bench readme --results results/latest/scored_results.json
```

## Layout
- `runner/` — CLI, config, fixtures, engine adapter, scoring, reporting, README sync
- `tasks/` — catalog plus per-language executable implementations
- `fixtures/` — deterministic inputs and local mock assets
- `tests/` — config, scoring, contract, and dry-run CLI tests
- `docs/plots/` — stable chart assets embedded from the latest scored benchmark run

<!-- benchmark:begin -->
## Latest benchmark snapshot

Run ID: `20260423T042840Z`

### Host / environment

| Field | Value |
|---|---|
| Hostname | cachyos-x8664-hp16la |
| System | Linux |
| Kernel / release | 6.19.11-1-cachyos |
| Platform | Linux-6.19.11-1-cachyos-x86_64-with-glibc2.43 |
| Machine | x86_64 |
| Normalized architecture | x86_64 |
| CPU model | Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz |
| CPU count | 8 |
| Python | 3.14.4 |
| Container engine | docker |
| Engine version | Docker version 29.4.0, build 9d7ad9ff18 |

### Git / publish identity

| Field | Value |
|---|---|
| Branch | master |
| Commit | 61cb41f4fd1703931ef034db67bf05ad97ba45f3 |
| Short commit | 61cb41f |
| Dirty working tree | True |

### Publish profile

| Field | Value |
|---|---|
| Preset | manual / inherited |
| Iterations | 1 |
| Warmups | 0 |
| Jobs | 1 |
| Architectures | x86_64 |
| Baseline runtime | python-3.12 |
| Engine | docker |

### Runtime versions present in this published snapshot

Runtime identity is architecture-aware: each row represents a specific language/runtime version on a specific CPU architecture so future ARM, RISC-V, or other host runs can be added without collapsing them into the current x86_64 results.

| Runtime | Family | Architecture | Configured version | Reported version | Image |
|---|---|---|---|---|---|
| PHP 5.6 [x86_64] | php | x86_64 | 5.6 | PHP 5.6.40 (cli) (built: Jan 23 2019 00:04:26) | languages-benchmark:php-5.6 |
| PHP 7.4 [x86_64] | php | x86_64 | 7.4 | PHP 7.4.33 (cli) (built: Nov 15 2022 06:01:17) ( NTS ) | languages-benchmark:php-7.4 |
| PHP 7.2 [x86_64] | php | x86_64 | 7.2 | PHP 7.2.34 (cli) (built: Dec 11 2020 10:44:02) ( NTS ) | languages-benchmark:php-7.2 |
| PHP 8.4 [x86_64] | php | x86_64 | 8.4 | PHP 8.4.20 (cli) (built: Apr 22 2026 01:24:37) (NTS) | languages-benchmark:php-8.4 |
| Python 2.7 [x86_64] | python | x86_64 | 2.7 | Python 2.7.18 | languages-benchmark:python-2.7 |
| Python 3.8 [x86_64] | python | x86_64 | 3.8 | Python 3.8.20 | languages-benchmark:python-3.8 |
| Python 3.11 [x86_64] | python | x86_64 | 3.11 | Python 3.11.15 | languages-benchmark:python-3.11 |
| Python 3.12 [x86_64] | python | x86_64 | 3.12 | Python 3.12.13 | languages-benchmark:python-3.12 |
| Java 21 [x86_64] | java | x86_64 | 21 | openjdk version "21.0.10" 2026-01-20 LTS | languages-benchmark:java-21 |
| C++ (GCC 14) [x86_64] | cpp | x86_64 | 14 | g++ (GCC) 14.3.0 | languages-benchmark:cpp-14 |
| Node.js 22 [x86_64] | node | x86_64 | 22 | v22.22.2 | languages-benchmark:node-22 |
| Bun 1.3.12 [x86_64] | node | x86_64 | 1.3.12 | 1.3.12 | languages-benchmark:bun-1.3.12 |
| Deno 2.7.6 [x86_64] | node | x86_64 | 2.7.6 | deno 2.7.6 (stable, release, x86_64-unknown-linux-gnu) | languages-benchmark:deno-2.7.6 |
| Go 1.23 [x86_64] | go | x86_64 | 1.23 | Go 1.23 (built from golang:1.23-bookworm) | languages-benchmark:go-1.23 |
| Rust 1.82 [x86_64] | rust | x86_64 | 1.82 | Rust 1.82 (built from rust:1.82-slim-bookworm) | languages-benchmark:rust-1.82 |

Tasks in this snapshot: `ai_service_integration`, `api_client`, `basic_blockchain`, `basic_web_application`, `binary_search_tree`, `chat_application`, `cli_file_search`, `csv_parsing`, `data_visualization`, `decision_tree`, `file_io_large`, `gui_calculator`, `image_resizing`, `linear_regression`, `matrix_multiplication`, `prime_sieve`, `producer_consumer`, `rest_api`, `sentiment_analysis`, `simple_web_server`, `socket_programming`, `sort_integers`, `sqlite_crud`, `third_party_api`, `tic_tac_toe`, `web_scraper`

### Snapshot summary

- **Objective leader:** **Rust 1.82 [x86_64]** at **47.49**; next is **C++ (GCC 14) [x86_64]** at **34.07**.
- **Opinionated leader:** **Java 21 [x86_64]** at **90.34**; next is **Python 3.12 [x86_64]** at **89.19**.
- **Best CPU efficiency:** **Rust 1.82 [x86_64]** at **40.00**; next is **C++ (GCC 14) [x86_64]** at **25.93**.
- **Best wall-clock efficiency:** **Rust 1.82 [x86_64]** at **38.94**; next is **C++ (GCC 14) [x86_64]** at **24.67**.
- **Best memory efficiency:** **Rust 1.82 [x86_64]** at **73.37**; next is **C++ (GCC 14) [x86_64]** at **63.32**.
- **Best scalability:** **Node.js 22 [x86_64]** at **83.60**; next is **Python 3.12 [x86_64]** at **81.16**.

### Regression vs previous published snapshot

No previous publish manifest was available, so no regression baseline could be computed yet.

### Machine-readable publish manifest

- The README publication flow also writes a machine-readable manifest to `docs/publish-manifest.json` so the published snapshot can be audited later.
- Canonical published runs should remain sequential by default even though `./bench run --jobs N` is supported for faster local experimentation.


### Artifact/source provenance

| Published view | Source artifact |
|---|---|
| Canonical README/report snapshot | `20260423T042840Z` |
| Architecture truth: `x86_64` | `results/20260423T042840Z/scored_results.json` |
| Version-matrix supplemental view | `results/20260423T043938Z/scored_results.json` |
| Runtime metadata source | `results/20260423T043938Z/scored_results.json` |
| JavaScript runtime comparison source | `results/20260423T043938Z/scored_results.json` |

### Size legend

- `S` = **Small** input
- `M` = **Medium** input
- `L` = **Large** input
- These are deterministic fixture sizes defined per task. They do **not** mean the same absolute number of rows/items/bytes for every benchmark; each task has its own `S/M/L` workload specification.

### How to read these plots

- The README now contains both **snapshot-scoped plots** and **language best-case plots**.
- The README now contains both **raw-unit plots** and **normalized score plots**.
- **Snapshot-scoped** plots show exactly the runtimes present in the published artifact used to generate this README.
- **Language best-case** plots collapse each language family down to whichever tested version performed best for that specific metric.
- The new **raw-unit** section uses real units wherever possible: CPU and wall time in **ms/s**, memory in **MB/GB**, and implementation size in **lines of code**.
- For those raw-unit plots, **lower is better** and there is no internal inversion.
- For **CPU**, **wall time**, and **memory**, the raw measurements are **lower is better**, but the plotted scores are inverted so **higher is better**.
- **Overall** is a weighted composite score, so **higher is better**.
- **Scalability** is also **higher is better** and reflects how gracefully runtime and memory grow from small to large inputs.
- The **canonical-order snapshot** plots keep the runtime order actually present in this published artifact: `PHP 5.6 [x86_64]`, `PHP 7.4 [x86_64]`, `PHP 7.2 [x86_64]`, `PHP 8.4 [x86_64]`, `Python 2.7 [x86_64]`, `Python 3.8 [x86_64]`, `Python 3.11 [x86_64]`, `Python 3.12 [x86_64]`, `Java 21 [x86_64]`, `C++ (GCC 14) [x86_64]`, `Node.js 22 [x86_64]`, `Bun 1.3.12 [x86_64]`, `Deno 2.7.6 [x86_64]`, `Go 1.23 [x86_64]`, `Rust 1.82 [x86_64]`.
- The **canonical-order best-case** plots keep the language-family order from `benchmark.yaml`: `php`, `python`, `java`, `cpp`, `node`, `go`, `rust`.
- The **ranked** plots reorder languages from best to worst for the specific metric shown in that chart.
- This snapshot covers the **full runnable 26-task suite** currently tracked in the benchmark catalog.

### Metric provenance

| Metric group | Type | Meaning |
|---|---|---|
| CPU / Wall / Memory / LOC | **Measured** | Directly measured from benchmark execution or LOC counting. |
| Scalability | **Derived** | Computed from S→M→L wall-time and memory growth ratios. |
| Community | **Derived** | Computed from checked-in contributor/update-cadence inputs. |
| Ease / Debugging / Docs / Libraries / Concurrency | **Rubric** | Checked-in rubric values with evidence and sources. |
| Objective / Opinionated / Overall | **Derived** | Recomputed aggregate scores built from the inputs above. |

### Per-version methodology notes

- **Measured at runtime-version level:** CPU, wall time, memory, LOC, startup split, workload split, correctness outputs, and scalability growth inputs.
- **Rubric handling:** runtime variants can now override family-level rubric values for ease/debugging/docs/libraries/concurrency; variants without an override continue inheriting the family default.
- **Community handling:** community inputs still attach to the language family rather than each runtime variant.
- **Best pure runtime comparison:** the per-version raw-unit and objective sections are the cleanest apples-to-apples runtime comparison.

### Methodology for non-objective and derived criteria

This benchmark separates **objective/measured** inputs from **derived** and **interpretive** inputs.

**Measured / objective inputs**

- **CPU time**: median measured CPU seconds.
- **Wall time**: median measured elapsed seconds.
- **Memory**: median measured peak RSS in MB.
- **LOC**: counted lines of code.

For lower-is-better objective metrics, the normalized score is:

- `score = 100 * best / candidate`

**Scalability**

Scalability is derived from growth across `S`, `M`, and `L` for each language/task pair rather than taken from one direct measurement.

For each language/task:

- `wall_growth = ((M_wall / S_wall) + (L_wall / M_wall)) / 2`
- `memory_growth = ((M_mem / S_mem) + (L_mem / M_mem)) / 2`
- `raw_scalability = (wall_growth + memory_growth) / 2`

Then it is normalized relative to the best observed raw growth:

- `scalability_score = 100 * best_raw_scalability / candidate_raw_scalability`

So **higher scalability score is better** only because lower growth is inverted into a higher score.

**Other non-objective / interpretive inputs**

- **Ease**: audited rubric score from `rubrics.yaml` for readability, maintainability, and implementation ergonomics.
- **Debugging**: audited rubric score from `rubrics.yaml` for debugging tools and workflow quality.
- **Docs**: audited rubric score from `rubrics.yaml` for official documentation and learning resources.
- **Libraries**: audited rubric score from `rubrics.yaml` for third-party ecosystem breadth and quality.
- **Concurrency**: audited rubric score from `rubrics.yaml` for support for concurrent/parallel programming.
- **Community**: derived from `community.yaml` as the average of `active_contributors` and `update_cadence`.
- Variants can override family-level rubric inputs, but community is still **language-family-level** today.

For higher-is-better interpretive metrics, the normalized score is:

- `score = 100 * candidate / best`

**Recomputed category scores**

- **Objective score** uses only CPU, wall, memory, and LOC, with weights renormalized inside that subset.
- **Opinionated score** uses scalability, ease, community, debugging, docs, libraries, and concurrency, with weights renormalized inside that subset.
- **Overall score** blends both groups with the weights from `weights.default.yaml`.

### Fixture sizes by task

| Task | S | M | L |
|---|---|---|---|
| `ai_service_integration` | 80 mock AI responses from mocks/ai_service_s.json | 300 mock AI responses from mocks/ai_service_m.json | 700 mock AI responses from mocks/ai_service_l.json |
| `api_client` | 120 mock API items from mocks/public_api_s.json | 500 mock API items from mocks/public_api_m.json | 1,000 mock API items from mocks/public_api_l.json |
| `basic_blockchain` | 1,000 blocks × 6 synthetic transactions/block from generated/blockchain/s.txt | 5,000 blocks × 6 synthetic transactions/block from generated/blockchain/m.txt | 10,000 blocks × 6 synthetic transactions/block from generated/blockchain/l.txt |
| `basic_web_application` | 120 browser-side to-do operations against fixtures/ui/basic_web_application.html | 480 browser-side to-do operations against fixtures/ui/basic_web_application.html | 1,200 browser-side to-do operations against fixtures/ui/basic_web_application.html |
| `binary_search_tree` | 5,000 inserts + 2,000 queries from generated/bst/s.txt | 20,000 inserts + 8,000 queries from generated/bst/m.txt | 50,000 inserts + 20,000 queries from generated/bst/l.txt |
| `chat_application` | 40 TCP chat round-trips | 160 TCP chat round-trips | 400 TCP chat round-trips |
| `cli_file_search` | 3 dirs × 6 files/dir × 24 lines/file under generated/search/s | 5 dirs × 8 files/dir × 40 lines/file under generated/search/m | 7 dirs × 10 files/dir × 60 lines/file under generated/search/l |
| `csv_parsing` | 10,000 CSV data rows from generated/csv/s.csv | 50,000 CSV data rows from generated/csv/m.csv | 100,000 CSV data rows from generated/csv/l.csv |
| `data_visualization` | 120 browser-side chart bars rendered against fixtures/ui/data_visualization.html | 480 browser-side chart bars rendered against fixtures/ui/data_visualization.html | 1,200 browser-side chart bars rendered against fixtures/ui/data_visualization.html |
| `decision_tree` | 2,000 labeled rows from generated/decision_tree/s.csv | 10,000 labeled rows from generated/decision_tree/m.csv | 20,000 labeled rows from generated/decision_tree/l.csv |
| `file_io_large` | 10,000 newline-delimited integers from generated/file_io/s.txt | 50,000 newline-delimited integers from generated/file_io/m.txt | 100,000 newline-delimited integers from generated/file_io/l.txt |
| `gui_calculator` | 120 browser-side calculator updates against fixtures/ui/gui_calculator.html | 480 browser-side calculator updates against fixtures/ui/gui_calculator.html | 1,200 browser-side calculator updates against fixtures/ui/gui_calculator.html |
| `image_resizing` | 64×64 PPM image from generated/image/s.ppm | 128×128 PPM image from generated/image/m.ppm | 192×192 PPM image from generated/image/l.ppm |
| `linear_regression` | 10,000 training rows from generated/linear_regression/s.csv | 50,000 training rows from generated/linear_regression/m.csv | 100,000 training rows from generated/linear_regression/l.csv |
| `matrix_multiplication` | 2 dense 32×32 matrices from generated/matrix/s.txt | 2 dense 64×64 matrices from generated/matrix/m.txt | 2 dense 96×96 matrices from generated/matrix/l.txt |
| `prime_sieve` | sieve limit 50,000 | sieve limit 125,000 | sieve limit 250,000 |
| `producer_consumer` | 10,000 queued values from generated/producer_consumer/s.txt | 50,000 queued values from generated/producer_consumer/m.txt | 100,000 queued values from generated/producer_consumer/l.txt |
| `rest_api` | 60 local GET /item requests | 240 local GET /item requests | 600 local GET /item requests |
| `sentiment_analysis` | 5,000 text lines from generated/sentiment/s.txt | 20,000 text lines from generated/sentiment/m.txt | 50,000 text lines from generated/sentiment/l.txt |
| `simple_web_server` | 60 local GET / requests | 240 local GET / requests | 600 local GET / requests |
| `socket_programming` | 40 TCP echo round-trips | 160 TCP echo round-trips | 400 TCP echo round-trips |
| `sort_integers` | 10,000 integers from generated/sort/s.txt | 50,000 integers from generated/sort/m.txt | 100,000 integers from generated/sort/l.txt |
| `sqlite_crud` | 20 CRUD cycles (create/read/update/read/delete) | 80 CRUD cycles (create/read/update/read/delete) | 200 CRUD cycles (create/read/update/read/delete) |
| `third_party_api` | 120 mock social posts from mocks/twitter_like_s.json | 500 mock social posts from mocks/twitter_like_m.json | 1,000 mock social posts from mocks/twitter_like_l.json |
| `tic_tac_toe` | 1,000 deterministic games from generated/tic_tac_toe/s.txt | 5,000 deterministic games from generated/tic_tac_toe/m.txt | 10,000 deterministic games from generated/tic_tac_toe/l.txt |
| `web_scraper` | 8 local HTML pages (+ index) under mock_site/s | 24 local HTML pages (+ index) under mock_site/m | 60 local HTML pages (+ index) under mock_site/l |

### Correctness verification summary

**0 mismatches** across 78 task/size groups in this artifact.

### Expected-output manifest check

All 78 current task/size output digests matched the checked-in expected-output manifest.

### Correctness digests

These short hashes summarize the canonical successful output fingerprint for each task/size group.

| Task | Size | Digest | Distinct outputs | Canonical output preview |
|---|---|---|---:|---|
| `ai_service_integration` | `L` | `17fd386a64d8` | 1 | `47365` |
| `ai_service_integration` | `M` | `bba3be97a8a8` | 1 | `20153` |
| `ai_service_integration` | `S` | `bb7ccf341f26` | 1 | `5236` |
| `api_client` | `L` | `a4b361990443` | 1 | `1006917` |
| `api_client` | `M` | `3dbf56f9ca2b` | 1 | `361322` |
| `api_client` | `S` | `a61ac4de221f` | 1 | `58330` |
| `basic_blockchain` | `L` | `4f669965c328` | 1 | `1349894952` |
| `basic_blockchain` | `M` | `76596d42c0a6` | 1 | `2019723500` |
| `basic_blockchain` | `S` | `2f6418a43a43` | 1 | `2772269579` |
| `basic_web_application` | `L` | `b0e7e28de522` | 1 | `1439895` |
| `basic_web_application` | `M` | `bb3fa0b450a3` | 1 | `227295` |
| `basic_web_application` | `S` | `2098fc01f406` | 1 | `13015` |
| `binary_search_tree` | `L` | `edbc0a20c7ce` | 1 | `5007255743` |
| `binary_search_tree` | `M` | `48db771f2616` | 1 | `806728510` |
| `binary_search_tree` | `S` | `4fda16c4115f` | 1 | `50062169` |
| `chat_application` | `L` | `c5b33d04f844` | 1 | `8580` |
| `chat_application` | `M` | `8473d094d884` | 1 | `3300` |
| `chat_application` | `S` | `e18b971fb266` | 1 | `780` |
| `cli_file_search` | `L` | `ab8e9a58c47a` | 1 | `600` |
| `cli_file_search` | `M` | `c942bc47f4c9` | 1 | `228` |
| `cli_file_search` | `S` | `2a62cf402cd3` | 1 | `61` |
| `csv_parsing` | `L` | `3731d73bf8d3` | 1 | `100112691` |
| `csv_parsing` | `M` | `cad73ad4bffd` | 1 | `50033678` |
| `csv_parsing` | `S` | `ac1024e30ac3` | 1 | `9964974` |
| `data_visualization` | `L` | `273dc79a708b` | 1 | `3526369` |
| `data_visualization` | `M` | `28270a0112a0` | 1 | `2156572` |
| `data_visualization` | `S` | `debe935fc864` | 1 | `139234` |
| `decision_tree` | `L` | `07b93b5234aa` | 1 | `2026280554` |
| `decision_tree` | `M` | `8fdb4e675688` | 1 | `990549112` |
| `decision_tree` | `S` | `09449ab6ee1e` | 1 | `194400561` |
| `file_io_large` | `L` | `d2ed0bbe2c21` | 1 | `501738729308` |
| `file_io_large` | `M` | `ae2b279922d2` | 1 | `250594893028` |
| `file_io_large` | `S` | `1e31a2c51808` | 1 | `50207724265` |
| `gui_calculator` | `L` | `54673e600034` | 1 | `84181` |
| `gui_calculator` | `M` | `173b1dc7697d` | 1 | `915282` |
| `gui_calculator` | `S` | `8212ba5ccbab` | 1 | `367300` |
| `image_resizing` | `L` | `073e693a30a9` | 1 | `3494416` |
| `image_resizing` | `M` | `664a1376f609` | 1 | `1570381` |
| `image_resizing` | `S` | `674ca46abc1e` | 1 | `392833` |
| `linear_regression` | `L` | `ff862d747945` | 1 | `9998560` |
| `linear_regression` | `M` | `9c21331ae173` | 1 | `9996280` |
| `linear_regression` | `S` | `421f5d383444` | 1 | `9983806` |
| `matrix_multiplication` | `L` | `a669cc74fc5d` | 1 | `17784056` |
| `matrix_multiplication` | `M` | `89d09b2675ff` | 1 | `5179849` |
| `matrix_multiplication` | `S` | `de89d1beb6ae` | 1 | `653345` |
| `prime_sieve` | `L` | `9342debf6bd5` | 1 | `22044` |
| `prime_sieve` | `M` | `7d3cce2b0e1f` | 1 | `11734` |
| `prime_sieve` | `S` | `a44bb4d076ad` | 1 | `5133` |
| `producer_consumer` | `L` | `3fa3d2f544ba` | 1 | `3920525990` |
| `producer_consumer` | `M` | `d5227b55eb03` | 1 | `1607111531` |
| `producer_consumer` | `S` | `15fadc455991` | 1 | `2389872086` |
| `rest_api` | `L` | `4a07ca68244e` | 1 | `539100` |
| `rest_api` | `M` | `f746ae300261` | 1 | `86040` |
| `rest_api` | `S` | `0ff7e2487118` | 1 | `5310` |
| `sentiment_analysis` | `L` | `66944880e34f` | 1 | `74999` |
| `sentiment_analysis` | `M` | `148744f24146` | 1 | `29999` |
| `sentiment_analysis` | `S` | `f1bbaed6eebd` | 1 | `7499` |
| `simple_web_server` | `L` | `8cf005daf293` | 1 | `9000` |
| `simple_web_server` | `M` | `997f68b79ee0` | 1 | `3600` |
| `simple_web_server` | `S` | `22f1a6d92267` | 1 | `900` |
| `socket_programming` | `L` | `2580435e03bb` | 1 | `3490` |
| `socket_programming` | `M` | `3e2d84595920` | 1 | `1330` |
| `socket_programming` | `S` | `bfa9b234f734` | 1 | `310` |
| `sort_integers` | `L` | `ddb1f009e7a8` | 1 | `61722` |
| `sort_integers` | `M` | `72b8a61fe15d` | 1 | `127671` |
| `sort_integers` | `S` | `2d4dae131242` | 1 | `566598` |
| `sqlite_crud` | `L` | `0b30c339ebb5` | 1 | `124400` |
| `sqlite_crud` | `M` | `483f093a5680` | 1 | `20960` |
| `sqlite_crud` | `S` | `1ca032e4df02` | 1 | `1640` |
| `third_party_api` | `L` | `c1a40227a213` | 1 | `531858` |
| `third_party_api` | `M` | `73dd9a060f02` | 1 | `269036` |
| `third_party_api` | `S` | `b186c59140cc` | 1 | `62783` |
| `tic_tac_toe` | `L` | `ca7521aaaa23` | 1 | `2489992` |
| `tic_tac_toe` | `M` | `3046fcfe73f6` | 1 | `1240628` |
| `tic_tac_toe` | `S` | `b3bd0d4ccfcc` | 1 | `249684` |
| `web_scraper` | `L` | `0dac4b6549df` | 1 | `104200` |
| `web_scraper` | `M` | `1a7200d4113b` | 1 | `16990` |
| `web_scraper` | `S` | `a350f43a181d` | 1 | `1980` |

### Service and UI startup vs steady-state

The benchmark now records startup wait separately from steady-state workload time for service/UI tasks. The table below shows average startup vs average steady-state workload time across service/UI task-size medians for each runtime.
These startup/workload views use **the supplemental per-version runtime comparison (`20260423T043938Z`)**.

| Runtime | Task/size medians used | Avg startup | Avg steady-state workload | Avg total |
|---|---:|---:|---:|---:|
| PHP 5.6 [x86_64] | 24 | 268.018 ms ± 21.208 ms | 629.619 ms ± 400.099 ms | 897.638 ms |
| PHP 7.4 [x86_64] | 24 | 237.978 ms ± 16.825 ms | 579.068 ms ± 334.799 ms | 817.046 ms |
| PHP 7.2 [x86_64] | 24 | 293.314 ms ± 21.726 ms | 635.146 ms ± 404.770 ms | 928.459 ms |
| PHP 8.4 [x86_64] | 24 | 294.611 ms ± 20.412 ms | 602.285 ms ± 349.965 ms | 896.897 ms |
| Python 2.7 [x86_64] | 24 | 319.719 ms ± 30.346 ms | 644.307 ms ± 398.050 ms | 964.026 ms |
| Python 3.8 [x86_64] | 24 | 452.399 ms ± 52.179 ms | 676.522 ms ± 430.945 ms | 1.1289 s |
| Python 3.11 [x86_64] | 24 | 453.951 ms ± 54.985 ms | 620.954 ms ± 348.422 ms | 1.0749 s |
| Python 3.12 [x86_64] | 24 | 468.440 ms ± 58.790 ms | 612.866 ms ± 346.548 ms | 1.0813 s |
| Java 21 [x86_64] | 24 | 459.083 ms ± 63.123 ms | 693.717 ms ± 384.453 ms | 1.1528 s |
| C++ (GCC 14) [x86_64] | 24 | 250.267 ms ± 23.065 ms | 587.172 ms ± 342.348 ms | 837.439 ms |
| Node.js 22 [x86_64] | 24 | 320.817 ms ± 21.270 ms | 646.887 ms ± 384.816 ms | 967.704 ms |
| Bun 1.3.12 [x86_64] | 24 | 314.248 ms ± 21.986 ms | 600.246 ms ± 341.069 ms | 914.494 ms |
| Deno 2.7.6 [x86_64] | 24 | 328.376 ms ± 26.123 ms | 650.109 ms ± 361.789 ms | 978.485 ms |
| Go 1.23 [x86_64] | 24 | 240.032 ms ± 24.370 ms | 596.055 ms ± 327.865 ms | 836.086 ms |
| Rust 1.82 [x86_64] | 24 | 237.363 ms ± 24.746 ms | 556.225 ms ± 311.124 ms | 793.588 ms |

![Startup-time ranked chart](docs/plots/version_startup_units_ranked.svg)

![Steady-state workload-time ranked chart](docs/plots/version_workload_units_ranked.svg)

<details>
<summary><strong>Show canonical-order startup/workload plots</strong></summary>

![Startup-time chart](docs/plots/version_startup_units.svg)

![Steady-state workload-time chart](docs/plots/version_workload_units.svg)

</details>

### Baseline-relative comparisons

Baseline runtime: `python-3.12`

| Runtime | CPU vs baseline | Wall vs baseline | Memory vs baseline | Overall Δ vs baseline |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 0.37x | 0.63x | 0.29x | +12.67 |
| Go 1.23 [x86_64] | 0.53x | 0.69x | 0.62x | +3.11 |
| C++ (GCC 14) [x86_64] | 0.47x | 0.67x | 0.31x | +1.55 |
| Python 3.11 [x86_64] | 0.90x | 0.97x | 0.97x | +0.04 |
| Python 3.12 [x86_64] | 1.00x | 1.00x | 1.00x | +0.00 |
| Python 3.8 [x86_64] | 1.24x | 1.04x | 0.81x | -0.40 |
| Node.js 22 [x86_64] | 0.96x | 0.86x | 2.39x | -1.45 |
| Java 21 [x86_64] | 2.43x | 1.34x | 2.52x | -1.70 |
| Deno 2.7.6 [x86_64] | 1.03x | 0.88x | 3.54x | -3.89 |
| Bun 1.3.12 [x86_64] | 0.83x | 0.81x | 2.37x | -3.91 |
| Python 2.7 [x86_64] | 0.97x | 0.86x | 0.68x | -5.86 |
| PHP 7.4 [x86_64] | 0.57x | 0.69x | 1.22x | -8.50 |
| PHP 8.4 [x86_64] | 0.61x | 0.75x | 1.32x | -8.54 |
| PHP 7.2 [x86_64] | 0.73x | 0.79x | 1.28x | -12.43 |
| PHP 5.6 [x86_64] | 1.03x | 0.85x | 1.25x | -16.40 |

![CPU vs baseline ranked chart](docs/plots/version_baseline_cpu_ratio_ranked.svg)

![Wall vs baseline ranked chart](docs/plots/version_baseline_wall_ratio_ranked.svg)

![Memory vs baseline ranked chart](docs/plots/version_baseline_memory_ratio_ranked.svg)

![Overall delta vs baseline ranked chart](docs/plots/version_baseline_overall_delta_ranked.svg)

### Historical publish trends

| Run ID | Top overall runtime | Top score | Runtime rows |
|---|---|---:|---:|
| `20260423T042840Z` | Rust 1.82 [x86_64] | 67.31 | 7 |

![Historical overall trend chart](docs/plots/history_overall.svg)

### Category leaderboards

These recompute the benchmark across tagged subsets of tasks so you can inspect category-specific leaders instead of only the global aggregate.

#### `compute`

Tasks: `basic_blockchain`, `binary_search_tree`, `cli_file_search`, `csv_parsing`, `decision_tree`, `file_io_large`, `image_resizing`, `linear_regression`, `matrix_multiplication`, `prime_sieve`, `producer_consumer`, `sentiment_analysis`, `sort_integers`, `tic_tac_toe`

| Runtime | Overall | Objective | Opinionated | Tasks |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 71.42 | 58.58 | 81.52 | 14 |
| C++ (GCC 14) [x86_64] | 59.32 | 42.80 | 72.30 | 14 |
| Go 1.23 [x86_64] | 58.94 | 27.56 | 83.60 | 14 |
| Python 3.11 [x86_64] | 54.70 | 12.28 | 88.03 | 14 |
| Python 3.12 [x86_64] | 54.54 | 11.71 | 88.18 | 14 |
| Python 3.8 [x86_64] | 54.01 | 13.18 | 86.08 | 14 |
| Node.js 22 [x86_64] | 53.32 | 8.12 | 88.84 | 14 |
| Java 21 [x86_64] | 53.11 | 6.16 | 90.00 | 14 |
| Deno 2.7.6 [x86_64] | 51.22 | 7.53 | 85.56 | 14 |
| Bun 1.3.12 [x86_64] | 50.77 | 8.36 | 84.08 | 14 |
| Python 2.7 [x86_64] | 47.80 | 15.22 | 73.40 | 14 |
| PHP 8.4 [x86_64] | 46.13 | 11.28 | 73.51 | 14 |
| PHP 7.4 [x86_64] | 46.03 | 11.69 | 73.01 | 14 |
| PHP 7.2 [x86_64] | 41.95 | 11.00 | 66.27 | 14 |
| PHP 5.6 [x86_64] | 36.75 | 9.67 | 58.03 | 14 |

| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---:|---:|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 58.58 | 52.57 | 51.36 | 91.25 | 34.99 | 14 |
| C++ (GCC 14) [x86_64] | 42.80 | 33.76 | 32.97 | 78.31 | 27.64 | 14 |
| Go 1.23 [x86_64] | 27.56 | 27.90 | 27.75 | 30.18 | 21.96 | 14 |
| Python 2.7 [x86_64] | 15.22 | 3.69 | 3.53 | 33.00 | 39.78 | 14 |
| Python 3.8 [x86_64] | 13.18 | 2.01 | 1.93 | 26.12 | 43.92 | 14 |
| Python 3.11 [x86_64] | 12.28 | 2.38 | 2.28 | 21.14 | 43.92 | 14 |
| Python 3.12 [x86_64] | 11.71 | 2.00 | 1.93 | 19.68 | 43.92 | 14 |
| PHP 7.4 [x86_64] | 11.69 | 6.10 | 5.92 | 12.10 | 37.54 | 14 |
| PHP 8.4 [x86_64] | 11.28 | 5.75 | 5.60 | 11.20 | 37.54 | 14 |
| PHP 7.2 [x86_64] | 11.00 | 5.24 | 5.05 | 11.46 | 37.54 | 14 |
| PHP 5.6 [x86_64] | 9.67 | 3.59 | 3.51 | 12.00 | 34.36 | 14 |
| Bun 1.3.12 [x86_64] | 8.36 | 2.67 | 2.71 | 5.77 | 39.16 | 14 |
| Node.js 22 [x86_64] | 8.12 | 2.43 | 2.44 | 5.41 | 39.16 | 14 |
| Deno 2.7.6 [x86_64] | 7.53 | 2.01 | 2.11 | 3.85 | 39.16 | 14 |
| Java 21 [x86_64] | 6.16 | 0.64 | 0.70 | 6.15 | 31.78 | 14 |

| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java 21 [x86_64] | 90.00 | 77.96 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 14 |
| Node.js 22 [x86_64] | 88.84 | 82.56 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 14 |
| Python 3.12 [x86_64] | 88.18 | 76.44 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 14 |
| Python 3.11 [x86_64] | 88.03 | 75.75 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 14 |
| Python 3.8 [x86_64] | 86.08 | 71.65 | 100.00 | 98.45 | 88.89 | 90.00 | 100.00 | 70.00 | 14 |
| Deno 2.7.6 [x86_64] | 85.56 | 82.79 | 88.89 | 100.00 | 77.78 | 90.00 | 80.00 | 80.00 | 14 |
| Bun 1.3.12 [x86_64] | 84.08 | 80.91 | 88.89 | 100.00 | 77.78 | 80.00 | 80.00 | 80.00 | 14 |
| Go 1.23 [x86_64] | 83.60 | 64.53 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 14 |
| Rust 1.82 [x86_64] | 81.52 | 69.54 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 14 |
| PHP 8.4 [x86_64] | 73.51 | 74.11 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 14 |
| Python 2.7 [x86_64] | 73.40 | 61.18 | 77.78 | 98.45 | 77.78 | 70.00 | 80.00 | 60.00 | 14 |
| PHP 7.4 [x86_64] | 73.01 | 71.75 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 14 |
| C++ (GCC 14) [x86_64] | 72.30 | 67.36 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 14 |
| PHP 7.2 [x86_64] | 66.27 | 71.60 | 66.67 | 77.32 | 66.67 | 70.00 | 80.00 | 40.00 | 14 |
| PHP 5.6 [x86_64] | 58.03 | 55.54 | 55.56 | 77.32 | 66.67 | 60.00 | 60.00 | 40.00 | 14 |


#### `service`

Tasks: `chat_application`, `rest_api`, `simple_web_server`, `socket_programming`, `sqlite_crud`

| Runtime | Overall | Objective | Opinionated | Tasks |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 79.64 | 72.97 | 84.87 | 5 |
| Go 1.23 [x86_64] | 74.66 | 58.11 | 87.66 | 5 |
| C++ (GCC 14) [x86_64] | 71.36 | 64.87 | 76.46 | 5 |
| Python 3.12 [x86_64] | 71.01 | 45.88 | 90.76 | 5 |
| Python 3.11 [x86_64] | 70.94 | 46.18 | 90.38 | 5 |
| Python 3.8 [x86_64] | 70.22 | 45.46 | 89.68 | 5 |
| PHP 7.4 [x86_64] | 68.81 | 60.13 | 75.63 | 5 |
| Node.js 22 [x86_64] | 68.73 | 43.07 | 88.90 | 5 |
| PHP 8.4 [x86_64] | 67.51 | 56.71 | 76.00 | 5 |
| Bun 1.3.12 [x86_64] | 66.42 | 42.60 | 85.13 | 5 |
| Python 2.7 [x86_64] | 66.13 | 49.87 | 78.91 | 5 |
| Java 21 [x86_64] | 64.82 | 31.80 | 90.77 | 5 |
| PHP 7.2 [x86_64] | 64.06 | 57.16 | 69.48 | 5 |
| Deno 2.7.6 [x86_64] | 63.47 | 37.26 | 84.06 | 5 |
| PHP 5.6 [x86_64] | 62.10 | 59.56 | 64.10 | 5 |

| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---:|---:|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 72.97 | 71.36 | 57.83 | 80.21 | 100.00 | 5 |
| C++ (GCC 14) [x86_64] | 64.87 | 69.99 | 54.04 | 81.80 | 50.00 | 5 |
| PHP 7.4 [x86_64] | 60.13 | 67.62 | 60.12 | 49.73 | 60.00 | 5 |
| PHP 5.6 [x86_64] | 59.56 | 64.75 | 57.89 | 54.37 | 60.00 | 5 |
| Go 1.23 [x86_64] | 58.11 | 53.77 | 56.73 | 55.98 | 75.00 | 5 |
| PHP 7.2 [x86_64] | 57.16 | 66.67 | 52.88 | 48.12 | 60.00 | 5 |
| PHP 8.4 [x86_64] | 56.71 | 66.67 | 53.65 | 45.07 | 60.00 | 5 |
| Python 2.7 [x86_64] | 49.87 | 33.33 | 50.56 | 41.97 | 100.00 | 5 |
| Python 3.11 [x86_64] | 46.18 | 32.65 | 46.51 | 32.38 | 100.00 | 5 |
| Python 3.12 [x86_64] | 45.88 | 31.23 | 45.64 | 34.24 | 100.00 | 5 |
| Python 3.8 [x86_64] | 45.46 | 28.23 | 45.07 | 37.40 | 100.00 | 5 |
| Node.js 22 [x86_64] | 43.07 | 30.39 | 45.56 | 38.18 | 75.00 | 5 |
| Bun 1.3.12 [x86_64] | 42.60 | 31.92 | 46.44 | 32.75 | 75.00 | 5 |
| Deno 2.7.6 [x86_64] | 37.26 | 28.27 | 42.36 | 20.08 | 75.00 | 5 |
| Java 21 [x86_64] | 31.80 | 20.94 | 39.11 | 19.86 | 60.00 | 5 |

| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java 21 [x86_64] | 90.77 | 81.55 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 5 |
| Python 3.12 [x86_64] | 90.76 | 88.47 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 5 |
| Python 3.11 [x86_64] | 90.38 | 86.71 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 5 |
| Python 3.8 [x86_64] | 89.68 | 88.42 | 100.00 | 98.45 | 88.89 | 90.00 | 100.00 | 70.00 | 5 |
| Node.js 22 [x86_64] | 88.90 | 82.82 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 5 |
| Go 1.23 [x86_64] | 87.66 | 83.50 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 5 |
| Bun 1.3.12 [x86_64] | 85.13 | 85.80 | 88.89 | 100.00 | 77.78 | 80.00 | 80.00 | 80.00 | 5 |
| Rust 1.82 [x86_64] | 84.87 | 85.20 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 5 |
| Deno 2.7.6 [x86_64] | 84.06 | 75.78 | 88.89 | 100.00 | 77.78 | 90.00 | 80.00 | 80.00 | 5 |
| Python 2.7 [x86_64] | 78.91 | 86.88 | 77.78 | 98.45 | 77.78 | 70.00 | 80.00 | 60.00 | 5 |
| C++ (GCC 14) [x86_64] | 76.46 | 86.76 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 5 |
| PHP 8.4 [x86_64] | 76.00 | 85.70 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 5 |
| PHP 7.4 [x86_64] | 75.63 | 83.99 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 5 |
| PHP 7.2 [x86_64] | 69.48 | 86.59 | 66.67 | 77.32 | 66.67 | 70.00 | 80.00 | 40.00 | 5 |
| PHP 5.6 [x86_64] | 64.10 | 83.87 | 55.56 | 77.32 | 66.67 | 60.00 | 60.00 | 40.00 | 5 |


#### `ui`

Tasks: `basic_web_application`, `data_visualization`, `gui_calculator`

| Runtime | Overall | Objective | Opinionated | Tasks |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 90.91 | 96.04 | 86.88 | 3 |
| Go 1.23 [x86_64] | 88.36 | 86.00 | 90.22 | 3 |
| Node.js 22 [x86_64] | 84.68 | 76.11 | 91.41 | 3 |
| Python 3.8 [x86_64] | 83.70 | 74.64 | 90.81 | 3 |
| Python 3.12 [x86_64] | 83.55 | 72.83 | 91.98 | 3 |
| Python 3.11 [x86_64] | 83.27 | 72.96 | 91.36 | 3 |
| C++ (GCC 14) [x86_64] | 83.12 | 89.41 | 78.18 | 3 |
| Bun 1.3.12 [x86_64] | 81.23 | 73.62 | 87.21 | 3 |
| Python 2.7 [x86_64] | 80.72 | 80.56 | 80.84 | 3 |
| PHP 7.4 [x86_64] | 79.22 | 81.00 | 77.81 | 3 |
| Java 21 [x86_64] | 77.54 | 57.77 | 93.06 | 3 |
| PHP 8.4 [x86_64] | 77.14 | 76.45 | 77.67 | 3 |
| PHP 7.2 [x86_64] | 74.49 | 78.30 | 71.50 | 3 |
| Deno 2.7.6 [x86_64] | 73.33 | 55.20 | 87.56 | 3 |
| PHP 5.6 [x86_64] | 72.49 | 80.75 | 66.00 | 3 |

| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---:|---:|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 96.04 | 97.49 | 96.45 | 91.07 | 100.00 | 3 |
| C++ (GCC 14) [x86_64] | 89.41 | 95.92 | 94.19 | 91.27 | 60.00 | 3 |
| Go 1.23 [x86_64] | 86.00 | 92.38 | 90.61 | 77.22 | 75.00 | 3 |
| PHP 7.4 [x86_64] | 81.00 | 94.25 | 93.12 | 58.09 | 60.00 | 3 |
| PHP 5.6 [x86_64] | 80.75 | 94.94 | 87.36 | 64.10 | 60.00 | 3 |
| Python 2.7 [x86_64] | 80.56 | 91.82 | 82.71 | 50.13 | 100.00 | 3 |
| PHP 7.2 [x86_64] | 78.30 | 94.74 | 85.49 | 56.18 | 60.00 | 3 |
| PHP 8.4 [x86_64] | 76.45 | 93.04 | 83.35 | 53.45 | 60.00 | 3 |
| Node.js 22 [x86_64] | 76.11 | 89.48 | 82.80 | 48.68 | 75.00 | 3 |
| Python 3.8 [x86_64] | 74.64 | 92.25 | 70.32 | 40.84 | 100.00 | 3 |
| Bun 1.3.12 [x86_64] | 73.62 | 81.99 | 85.80 | 44.02 | 75.00 | 3 |
| Python 3.11 [x86_64] | 72.96 | 92.49 | 68.62 | 35.48 | 100.00 | 3 |
| Python 3.12 [x86_64] | 72.83 | 91.47 | 69.58 | 34.96 | 100.00 | 3 |
| Java 21 [x86_64] | 57.77 | 67.84 | 71.88 | 22.60 | 60.00 | 3 |
| Deno 2.7.6 [x86_64] | 55.20 | 37.22 | 82.77 | 29.91 | 75.00 | 3 |

| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java 21 [x86_64] | 93.06 | 92.24 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 3 |
| Python 3.12 [x86_64] | 91.98 | 94.15 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 3 |
| Node.js 22 [x86_64] | 91.41 | 94.55 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 3 |
| Python 3.11 [x86_64] | 91.36 | 91.28 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 3 |
| Python 3.8 [x86_64] | 90.81 | 93.71 | 100.00 | 98.45 | 88.89 | 90.00 | 100.00 | 70.00 | 3 |
| Go 1.23 [x86_64] | 90.22 | 95.43 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 3 |
| Deno 2.7.6 [x86_64] | 87.56 | 92.15 | 88.89 | 100.00 | 77.78 | 90.00 | 80.00 | 80.00 | 3 |
| Bun 1.3.12 [x86_64] | 87.21 | 95.51 | 88.89 | 100.00 | 77.78 | 80.00 | 80.00 | 80.00 | 3 |
| Rust 1.82 [x86_64] | 86.88 | 94.58 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 3 |
| Python 2.7 [x86_64] | 80.84 | 95.90 | 77.78 | 98.45 | 77.78 | 70.00 | 80.00 | 60.00 | 3 |
| C++ (GCC 14) [x86_64] | 78.18 | 94.80 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 3 |
| PHP 7.4 [x86_64] | 77.81 | 94.17 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 3 |
| PHP 8.4 [x86_64] | 77.67 | 93.52 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 3 |
| PHP 7.2 [x86_64] | 71.50 | 96.00 | 66.67 | 77.32 | 66.67 | 70.00 | 80.00 | 40.00 | 3 |
| PHP 5.6 [x86_64] | 66.00 | 92.73 | 55.56 | 77.32 | 66.67 | 60.00 | 60.00 | 40.00 | 3 |


#### `integration`

Tasks: `ai_service_integration`, `api_client`, `third_party_api`, `web_scraper`

| Runtime | Overall | Objective | Opinionated | Tasks |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 83.90 | 81.47 | 85.81 | 4 |
| C++ (GCC 14) [x86_64] | 67.80 | 57.59 | 75.82 | 4 |
| Go 1.23 [x86_64] | 64.60 | 36.82 | 86.42 | 4 |
| Python 3.11 [x86_64] | 59.56 | 18.64 | 91.70 | 4 |
| Python 3.8 [x86_64] | 59.44 | 19.88 | 90.52 | 4 |
| Python 3.12 [x86_64] | 59.31 | 17.92 | 91.83 | 4 |
| Node.js 22 [x86_64] | 57.39 | 14.43 | 91.14 | 4 |
| Java 21 [x86_64] | 56.42 | 10.45 | 92.54 | 4 |
| Python 2.7 [x86_64] | 56.37 | 26.24 | 80.05 | 4 |
| Deno 2.7.6 [x86_64] | 55.40 | 13.53 | 88.30 | 4 |
| Bun 1.3.12 [x86_64] | 55.17 | 14.53 | 87.09 | 4 |
| PHP 7.4 [x86_64] | 52.91 | 21.29 | 77.75 | 4 |
| PHP 8.4 [x86_64] | 52.50 | 20.28 | 77.81 | 4 |
| PHP 7.2 [x86_64] | 48.67 | 20.17 | 71.06 | 4 |
| PHP 5.6 [x86_64] | 45.68 | 19.95 | 65.90 | 4 |

| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---:|---:|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 81.47 | 87.16 | 87.00 | 98.21 | 27.36 | 4 |
| C++ (GCC 14) [x86_64] | 57.59 | 54.33 | 54.77 | 77.05 | 39.36 | 4 |
| Go 1.23 [x86_64] | 36.82 | 36.20 | 37.04 | 34.97 | 40.86 | 4 |
| Python 2.7 [x86_64] | 26.24 | 9.32 | 8.95 | 38.54 | 85.56 | 4 |
| PHP 7.4 [x86_64] | 21.29 | 10.21 | 10.21 | 13.18 | 86.51 | 4 |
| PHP 8.4 [x86_64] | 20.28 | 9.08 | 9.15 | 11.82 | 86.51 | 4 |
| PHP 7.2 [x86_64] | 20.17 | 8.67 | 8.69 | 12.52 | 86.51 | 4 |
| PHP 5.6 [x86_64] | 19.95 | 9.51 | 9.57 | 14.41 | 77.78 | 4 |
| Python 3.8 [x86_64] | 19.88 | 2.89 | 2.89 | 28.04 | 85.56 | 4 |
| Python 3.11 [x86_64] | 18.64 | 3.01 | 2.94 | 22.36 | 85.56 | 4 |
| Python 3.12 [x86_64] | 17.92 | 2.54 | 2.50 | 20.44 | 85.56 | 4 |
| Bun 1.3.12 [x86_64] | 14.53 | 3.43 | 3.55 | 6.94 | 78.73 | 4 |
| Node.js 22 [x86_64] | 14.43 | 3.46 | 3.48 | 6.55 | 78.73 | 4 |
| Deno 2.7.6 [x86_64] | 13.53 | 2.73 | 2.93 | 4.35 | 78.73 | 4 |
| Java 21 [x86_64] | 10.45 | 0.93 | 1.05 | 6.72 | 60.84 | 4 |

| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java 21 [x86_64] | 92.54 | 89.82 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 4 |
| Python 3.12 [x86_64] | 91.83 | 93.48 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 4 |
| Python 3.11 [x86_64] | 91.70 | 92.87 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 4 |
| Node.js 22 [x86_64] | 91.14 | 93.29 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 4 |
| Python 3.8 [x86_64] | 90.52 | 92.34 | 100.00 | 98.45 | 88.89 | 90.00 | 100.00 | 70.00 | 4 |
| Deno 2.7.6 [x86_64] | 88.30 | 95.57 | 88.89 | 100.00 | 77.78 | 90.00 | 80.00 | 80.00 | 4 |
| Bun 1.3.12 [x86_64] | 87.09 | 94.95 | 88.89 | 100.00 | 77.78 | 80.00 | 80.00 | 80.00 | 4 |
| Go 1.23 [x86_64] | 86.42 | 77.71 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 4 |
| Rust 1.82 [x86_64] | 85.81 | 89.55 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 4 |
| Python 2.7 [x86_64] | 80.05 | 92.20 | 77.78 | 98.45 | 77.78 | 70.00 | 80.00 | 60.00 | 4 |
| PHP 8.4 [x86_64] | 77.81 | 94.14 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 4 |
| PHP 7.4 [x86_64] | 77.75 | 93.88 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 4 |
| C++ (GCC 14) [x86_64] | 75.82 | 83.81 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 4 |
| PHP 7.2 [x86_64] | 71.06 | 93.97 | 66.67 | 77.32 | 66.67 | 70.00 | 80.00 | 40.00 | 4 |
| PHP 5.6 [x86_64] | 65.90 | 92.27 | 55.56 | 77.32 | 66.67 | 60.00 | 60.00 | 40.00 | 4 |


#### `io`

Tasks: `cli_file_search`, `csv_parsing`, `file_io_large`, `web_scraper`

| Runtime | Overall | Objective | Opinionated | Tasks |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 76.66 | 67.76 | 83.65 | 4 |
| C++ (GCC 14) [x86_64] | 65.58 | 53.77 | 74.87 | 4 |
| Go 1.23 [x86_64] | 62.77 | 34.04 | 85.34 | 4 |
| Python 3.11 [x86_64] | 58.26 | 16.90 | 90.75 | 4 |
| Python 3.12 [x86_64] | 57.99 | 16.31 | 90.74 | 4 |
| Python 3.8 [x86_64] | 57.94 | 18.26 | 89.12 | 4 |
| Node.js 22 [x86_64] | 55.74 | 12.23 | 89.92 | 4 |
| Java 21 [x86_64] | 55.44 | 9.60 | 91.45 | 4 |
| Deno 2.7.6 [x86_64] | 53.87 | 11.64 | 87.06 | 4 |
| Bun 1.3.12 [x86_64] | 53.39 | 12.53 | 85.50 | 4 |
| Python 2.7 [x86_64] | 52.34 | 20.75 | 77.16 | 4 |
| PHP 7.4 [x86_64] | 49.75 | 16.40 | 75.96 | 4 |
| PHP 8.4 [x86_64] | 49.42 | 15.59 | 76.00 | 4 |
| PHP 7.2 [x86_64] | 45.73 | 15.57 | 69.43 | 4 |
| PHP 5.6 [x86_64] | 42.35 | 15.46 | 63.49 | 4 |

| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---:|---:|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 67.76 | 60.93 | 61.01 | 94.72 | 54.52 | 4 |
| C++ (GCC 14) [x86_64] | 53.77 | 45.43 | 45.71 | 80.05 | 48.25 | 4 |
| Go 1.23 [x86_64] | 34.04 | 33.10 | 34.03 | 33.74 | 36.75 | 4 |
| Python 2.7 [x86_64] | 20.75 | 5.82 | 5.71 | 38.45 | 61.19 | 4 |
| Python 3.8 [x86_64] | 18.26 | 2.27 | 2.25 | 28.11 | 76.52 | 4 |
| Python 3.11 [x86_64] | 16.90 | 2.29 | 2.22 | 22.15 | 76.52 | 4 |
| PHP 7.4 [x86_64] | 16.40 | 7.49 | 7.51 | 13.28 | 63.15 | 4 |
| Python 3.12 [x86_64] | 16.31 | 1.98 | 1.98 | 20.31 | 76.52 | 4 |
| PHP 8.4 [x86_64] | 15.59 | 6.72 | 6.73 | 11.89 | 63.15 | 4 |
| PHP 7.2 [x86_64] | 15.57 | 6.43 | 6.44 | 12.59 | 63.15 | 4 |
| PHP 5.6 [x86_64] | 15.46 | 6.58 | 6.58 | 14.53 | 58.43 | 4 |
| Bun 1.3.12 [x86_64] | 12.53 | 2.95 | 3.03 | 6.18 | 67.62 | 4 |
| Node.js 22 [x86_64] | 12.23 | 2.66 | 2.74 | 5.70 | 67.62 | 4 |
| Deno 2.7.6 [x86_64] | 11.64 | 2.26 | 2.48 | 3.99 | 67.62 | 4 |
| Java 21 [x86_64] | 9.60 | 0.73 | 0.84 | 6.29 | 56.24 | 4 |

| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java 21 [x86_64] | 91.45 | 84.73 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 4 |
| Python 3.11 [x86_64] | 90.75 | 88.43 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 4 |
| Python 3.12 [x86_64] | 90.74 | 88.39 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 4 |
| Node.js 22 [x86_64] | 89.92 | 87.59 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 4 |
| Python 3.8 [x86_64] | 89.12 | 85.83 | 100.00 | 98.45 | 88.89 | 90.00 | 100.00 | 70.00 | 4 |
| Deno 2.7.6 [x86_64] | 87.06 | 89.81 | 88.89 | 100.00 | 77.78 | 90.00 | 80.00 | 80.00 | 4 |
| Bun 1.3.12 [x86_64] | 85.50 | 87.52 | 88.89 | 100.00 | 77.78 | 80.00 | 80.00 | 80.00 | 4 |
| Go 1.23 [x86_64] | 85.34 | 72.66 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 4 |
| Rust 1.82 [x86_64] | 83.65 | 79.47 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 4 |
| Python 2.7 [x86_64] | 77.16 | 78.71 | 77.78 | 98.45 | 77.78 | 70.00 | 80.00 | 60.00 | 4 |
| PHP 8.4 [x86_64] | 76.00 | 85.73 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 4 |
| PHP 7.4 [x86_64] | 75.96 | 85.52 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 4 |
| C++ (GCC 14) [x86_64] | 74.87 | 79.35 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 4 |
| PHP 7.2 [x86_64] | 69.43 | 86.35 | 66.67 | 77.32 | 66.67 | 70.00 | 80.00 | 40.00 | 4 |
| PHP 5.6 [x86_64] | 63.49 | 81.02 | 55.56 | 77.32 | 66.67 | 60.00 | 60.00 | 40.00 | 4 |


#### `ml`

Tasks: `decision_tree`, `linear_regression`

| Runtime | Overall | Objective | Opinionated | Tasks |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 67.10 | 49.79 | 80.70 | 2 |
| Python 3.11 [x86_64] | 56.40 | 13.66 | 89.99 | 2 |
| Python 3.12 [x86_64] | 56.31 | 13.02 | 90.33 | 2 |
| Python 3.8 [x86_64] | 55.75 | 14.67 | 88.03 | 2 |
| Node.js 22 [x86_64] | 55.72 | 11.37 | 90.57 | 2 |
| Java 21 [x86_64] | 55.37 | 8.74 | 92.01 | 2 |
| Bun 1.3.12 [x86_64] | 53.66 | 12.01 | 86.39 | 2 |
| C++ (GCC 14) [x86_64] | 53.16 | 29.67 | 71.62 | 2 |
| Deno 2.7.6 [x86_64] | 52.80 | 10.87 | 85.75 | 2 |
| Go 1.23 [x86_64] | 50.85 | 16.99 | 77.45 | 2 |
| Python 2.7 [x86_64] | 48.98 | 16.37 | 74.61 | 2 |
| PHP 8.4 [x86_64] | 47.91 | 14.11 | 74.46 | 2 |
| PHP 7.4 [x86_64] | 47.69 | 14.45 | 73.82 | 2 |
| PHP 7.2 [x86_64] | 42.88 | 13.74 | 65.77 | 2 |
| PHP 5.6 [x86_64] | 37.42 | 12.39 | 57.08 | 2 |

| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---:|---:|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 49.79 | 39.09 | 39.42 | 81.34 | 46.38 | 2 |
| C++ (GCC 14) [x86_64] | 29.67 | 13.06 | 13.52 | 68.28 | 41.76 | 2 |
| Go 1.23 [x86_64] | 16.99 | 10.42 | 11.14 | 20.67 | 39.86 | 2 |
| Python 2.7 [x86_64] | 16.37 | 2.63 | 2.63 | 36.30 | 47.28 | 2 |
| Python 3.8 [x86_64] | 14.67 | 1.66 | 1.65 | 27.21 | 54.54 | 2 |
| PHP 7.4 [x86_64] | 14.45 | 5.52 | 5.63 | 12.45 | 59.18 | 2 |
| PHP 8.4 [x86_64] | 14.11 | 5.32 | 5.44 | 11.52 | 59.18 | 2 |
| PHP 7.2 [x86_64] | 13.74 | 4.68 | 4.73 | 11.78 | 59.18 | 2 |
| Python 3.11 [x86_64] | 13.66 | 2.10 | 2.12 | 21.46 | 54.54 | 2 |
| Python 3.12 [x86_64] | 13.02 | 1.71 | 1.71 | 19.79 | 54.54 | 2 |
| PHP 5.6 [x86_64] | 12.39 | 3.01 | 3.06 | 12.51 | 55.88 | 2 |
| Bun 1.3.12 [x86_64] | 12.01 | 3.18 | 3.40 | 5.34 | 63.79 | 2 |
| Node.js 22 [x86_64] | 11.37 | 2.36 | 2.51 | 4.93 | 63.79 | 2 |
| Deno 2.7.6 [x86_64] | 10.87 | 2.02 | 2.23 | 3.60 | 63.79 | 2 |
| Java 21 [x86_64] | 8.74 | 0.57 | 0.62 | 5.83 | 51.63 | 2 |

| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java 21 [x86_64] | 92.01 | 87.33 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 2 |
| Node.js 22 [x86_64] | 90.57 | 90.61 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 2 |
| Python 3.12 [x86_64] | 90.33 | 86.44 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 2 |
| Python 3.11 [x86_64] | 89.99 | 84.87 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 2 |
| Python 3.8 [x86_64] | 88.03 | 80.71 | 100.00 | 98.45 | 88.89 | 90.00 | 100.00 | 70.00 | 2 |
| Bun 1.3.12 [x86_64] | 86.39 | 91.69 | 88.89 | 100.00 | 77.78 | 80.00 | 80.00 | 80.00 | 2 |
| Deno 2.7.6 [x86_64] | 85.75 | 83.69 | 88.89 | 100.00 | 77.78 | 90.00 | 80.00 | 80.00 | 2 |
| Rust 1.82 [x86_64] | 80.70 | 65.73 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 2 |
| Go 1.23 [x86_64] | 77.45 | 35.84 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 2 |
| Python 2.7 [x86_64] | 74.61 | 66.80 | 77.78 | 98.45 | 77.78 | 70.00 | 80.00 | 60.00 | 2 |
| PHP 8.4 [x86_64] | 74.46 | 78.52 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 2 |
| PHP 7.4 [x86_64] | 73.82 | 75.53 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 2 |
| C++ (GCC 14) [x86_64] | 71.62 | 64.20 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 2 |
| PHP 7.2 [x86_64] | 65.77 | 69.26 | 66.67 | 77.32 | 66.67 | 70.00 | 80.00 | 40.00 | 2 |
| PHP 5.6 [x86_64] | 57.08 | 51.12 | 55.56 | 77.32 | 66.67 | 60.00 | 60.00 | 40.00 | 2 |


#### `networking`

Tasks: `chat_application`, `simple_web_server`, `socket_programming`

| Runtime | Overall | Objective | Opinionated | Tasks |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 86.11 | 85.60 | 86.51 | 3 |
| Go 1.23 [x86_64] | 80.94 | 70.11 | 89.45 | 3 |
| C++ (GCC 14) [x86_64] | 77.49 | 76.37 | 78.37 | 3 |
| Python 3.12 [x86_64] | 75.68 | 54.61 | 92.24 | 3 |
| Python 3.11 [x86_64] | 75.49 | 54.75 | 91.78 | 3 |
| Python 3.8 [x86_64] | 75.00 | 54.29 | 91.27 | 3 |
| PHP 7.4 [x86_64] | 74.89 | 72.09 | 77.09 | 3 |
| PHP 8.4 [x86_64] | 73.72 | 68.72 | 77.65 | 3 |
| Node.js 22 [x86_64] | 73.15 | 51.40 | 90.25 | 3 |
| Python 2.7 [x86_64] | 71.01 | 58.64 | 80.72 | 3 |
| Bun 1.3.12 [x86_64] | 70.72 | 50.69 | 86.46 | 3 |
| PHP 7.2 [x86_64] | 70.44 | 69.81 | 70.93 | 3 |
| Java 21 [x86_64] | 69.53 | 40.40 | 92.41 | 3 |
| PHP 5.6 [x86_64] | 68.12 | 71.19 | 65.71 | 3 |
| Deno 2.7.6 [x86_64] | 66.78 | 43.60 | 85.00 | 3 |

| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---:|---:|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 85.60 | 87.52 | 70.73 | 95.11 | 100.00 | 3 |
| C++ (GCC 14) [x86_64] | 76.37 | 87.30 | 64.82 | 93.05 | 50.00 | 3 |
| PHP 7.4 [x86_64] | 72.09 | 83.93 | 75.81 | 57.56 | 60.00 | 3 |
| PHP 5.6 [x86_64] | 71.19 | 81.56 | 71.30 | 63.25 | 60.00 | 3 |
| Go 1.23 [x86_64] | 70.11 | 69.42 | 70.01 | 68.26 | 75.00 | 3 |
| PHP 7.2 [x86_64] | 69.81 | 84.14 | 69.96 | 55.44 | 60.00 | 3 |
| PHP 8.4 [x86_64] | 68.72 | 83.35 | 70.08 | 51.56 | 60.00 | 3 |
| Python 2.7 [x86_64] | 58.64 | 40.31 | 66.16 | 48.98 | 100.00 | 3 |
| Python 3.11 [x86_64] | 54.75 | 37.35 | 63.94 | 39.08 | 100.00 | 3 |
| Python 3.12 [x86_64] | 54.61 | 35.76 | 62.84 | 42.23 | 100.00 | 3 |
| Python 3.8 [x86_64] | 54.29 | 32.55 | 62.47 | 45.86 | 100.00 | 3 |
| Node.js 22 [x86_64] | 51.40 | 39.46 | 57.78 | 45.01 | 75.00 | 3 |
| Bun 1.3.12 [x86_64] | 50.69 | 39.91 | 59.30 | 39.13 | 75.00 | 3 |
| Deno 2.7.6 [x86_64] | 43.60 | 35.32 | 53.06 | 23.10 | 75.00 | 3 |
| Java 21 [x86_64] | 40.40 | 29.92 | 53.73 | 24.66 | 60.00 | 3 |

| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java 21 [x86_64] | 92.41 | 89.19 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 3 |
| Python 3.12 [x86_64] | 92.24 | 95.37 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 3 |
| Python 3.11 [x86_64] | 91.78 | 93.25 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 3 |
| Python 3.8 [x86_64] | 91.27 | 95.87 | 100.00 | 98.45 | 88.89 | 90.00 | 100.00 | 70.00 | 3 |
| Node.js 22 [x86_64] | 90.25 | 89.14 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 3 |
| Go 1.23 [x86_64] | 89.45 | 91.86 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 3 |
| Rust 1.82 [x86_64] | 86.51 | 92.85 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 3 |
| Bun 1.3.12 [x86_64] | 86.46 | 91.98 | 88.89 | 100.00 | 77.78 | 80.00 | 80.00 | 80.00 | 3 |
| Deno 2.7.6 [x86_64] | 85.00 | 80.17 | 88.89 | 100.00 | 77.78 | 90.00 | 80.00 | 80.00 | 3 |
| Python 2.7 [x86_64] | 80.72 | 95.33 | 77.78 | 98.45 | 77.78 | 70.00 | 80.00 | 60.00 | 3 |
| C++ (GCC 14) [x86_64] | 78.37 | 95.68 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 3 |
| PHP 8.4 [x86_64] | 77.65 | 93.41 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 3 |
| PHP 7.4 [x86_64] | 77.09 | 90.82 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 3 |
| PHP 7.2 [x86_64] | 70.93 | 93.35 | 66.67 | 77.32 | 66.67 | 70.00 | 80.00 | 40.00 | 3 |
| PHP 5.6 [x86_64] | 65.71 | 91.38 | 55.56 | 77.32 | 66.67 | 60.00 | 60.00 | 40.00 | 3 |



### Fixture/workload contract appendix

This appendix publishes the exact `S/M/L` contract for every runnable task so readers can audit what each benchmark size means.

| Task | S | M | L |
|---|---|---|---|
| `ai_service_integration` | 80 mock AI responses from mocks/ai_service_s.json | 300 mock AI responses from mocks/ai_service_m.json | 700 mock AI responses from mocks/ai_service_l.json |
| `api_client` | 120 mock API items from mocks/public_api_s.json | 500 mock API items from mocks/public_api_m.json | 1,000 mock API items from mocks/public_api_l.json |
| `basic_blockchain` | 1,000 blocks × 6 synthetic transactions/block from generated/blockchain/s.txt | 5,000 blocks × 6 synthetic transactions/block from generated/blockchain/m.txt | 10,000 blocks × 6 synthetic transactions/block from generated/blockchain/l.txt |
| `basic_web_application` | 120 browser-side to-do operations against fixtures/ui/basic_web_application.html | 480 browser-side to-do operations against fixtures/ui/basic_web_application.html | 1,200 browser-side to-do operations against fixtures/ui/basic_web_application.html |
| `binary_search_tree` | 5,000 inserts + 2,000 queries from generated/bst/s.txt | 20,000 inserts + 8,000 queries from generated/bst/m.txt | 50,000 inserts + 20,000 queries from generated/bst/l.txt |
| `chat_application` | 40 TCP chat round-trips | 160 TCP chat round-trips | 400 TCP chat round-trips |
| `cli_file_search` | 3 dirs × 6 files/dir × 24 lines/file under generated/search/s | 5 dirs × 8 files/dir × 40 lines/file under generated/search/m | 7 dirs × 10 files/dir × 60 lines/file under generated/search/l |
| `csv_parsing` | 10,000 CSV data rows from generated/csv/s.csv | 50,000 CSV data rows from generated/csv/m.csv | 100,000 CSV data rows from generated/csv/l.csv |
| `data_visualization` | 120 browser-side chart bars rendered against fixtures/ui/data_visualization.html | 480 browser-side chart bars rendered against fixtures/ui/data_visualization.html | 1,200 browser-side chart bars rendered against fixtures/ui/data_visualization.html |
| `decision_tree` | 2,000 labeled rows from generated/decision_tree/s.csv | 10,000 labeled rows from generated/decision_tree/m.csv | 20,000 labeled rows from generated/decision_tree/l.csv |
| `file_io_large` | 10,000 newline-delimited integers from generated/file_io/s.txt | 50,000 newline-delimited integers from generated/file_io/m.txt | 100,000 newline-delimited integers from generated/file_io/l.txt |
| `gui_calculator` | 120 browser-side calculator updates against fixtures/ui/gui_calculator.html | 480 browser-side calculator updates against fixtures/ui/gui_calculator.html | 1,200 browser-side calculator updates against fixtures/ui/gui_calculator.html |
| `image_resizing` | 64×64 PPM image from generated/image/s.ppm | 128×128 PPM image from generated/image/m.ppm | 192×192 PPM image from generated/image/l.ppm |
| `linear_regression` | 10,000 training rows from generated/linear_regression/s.csv | 50,000 training rows from generated/linear_regression/m.csv | 100,000 training rows from generated/linear_regression/l.csv |
| `matrix_multiplication` | 2 dense 32×32 matrices from generated/matrix/s.txt | 2 dense 64×64 matrices from generated/matrix/m.txt | 2 dense 96×96 matrices from generated/matrix/l.txt |
| `prime_sieve` | sieve limit 50,000 | sieve limit 125,000 | sieve limit 250,000 |
| `producer_consumer` | 10,000 queued values from generated/producer_consumer/s.txt | 50,000 queued values from generated/producer_consumer/m.txt | 100,000 queued values from generated/producer_consumer/l.txt |
| `rest_api` | 60 local GET /item requests | 240 local GET /item requests | 600 local GET /item requests |
| `sentiment_analysis` | 5,000 text lines from generated/sentiment/s.txt | 20,000 text lines from generated/sentiment/m.txt | 50,000 text lines from generated/sentiment/l.txt |
| `simple_web_server` | 60 local GET / requests | 240 local GET / requests | 600 local GET / requests |
| `socket_programming` | 40 TCP echo round-trips | 160 TCP echo round-trips | 400 TCP echo round-trips |
| `sort_integers` | 10,000 integers from generated/sort/s.txt | 50,000 integers from generated/sort/m.txt | 100,000 integers from generated/sort/l.txt |
| `sqlite_crud` | 20 CRUD cycles (create/read/update/read/delete) | 80 CRUD cycles (create/read/update/read/delete) | 200 CRUD cycles (create/read/update/read/delete) |
| `third_party_api` | 120 mock social posts from mocks/twitter_like_s.json | 500 mock social posts from mocks/twitter_like_m.json | 1,000 mock social posts from mocks/twitter_like_l.json |
| `tic_tac_toe` | 1,000 deterministic games from generated/tic_tac_toe/s.txt | 5,000 deterministic games from generated/tic_tac_toe/m.txt | 10,000 deterministic games from generated/tic_tac_toe/l.txt |
| `web_scraper` | 8 local HTML pages (+ index) under mock_site/s | 24 local HTML pages (+ index) under mock_site/m | 60 local HTML pages (+ index) under mock_site/l |

### Per-version plots

These plots come from the **version-matrix comparison snapshot** `20260423T043938Z` and show every benchmarked runtime variant separately.
**Important:** this per-version snapshot now covers the **full 26-task suite**. Tasks in this supplemental run: `ai_service_integration`, `api_client`, `basic_blockchain`, `basic_web_application`, `binary_search_tree`, `chat_application`, `cli_file_search`, `csv_parsing`, `data_visualization`, `decision_tree`, `file_io_large`, `gui_calculator`, `image_resizing`, `linear_regression`, `matrix_multiplication`, `prime_sieve`, `producer_consumer`, `rest_api`, `sentiment_analysis`, `simple_web_server`, `socket_programming`, `sort_integers`, `sqlite_crud`, `third_party_api`, `tic_tac_toe`, `web_scraper`.
The **objective** per-version plots are the fairest runtime-vs-runtime view. The **opinionated** per-version plots still include shared family-level rubric/community inputs, so variants from the same language family can remain artificially close on those dimensions.

#### Per-version raw-unit plots (full 26-task suite)

![Per-version CPU raw-unit ranked chart](docs/plots/version_cpu_units_ranked.svg)

![Per-version wall raw-unit ranked chart](docs/plots/version_wall_units_ranked.svg)

![Per-version memory raw-unit ranked chart](docs/plots/version_memory_units_ranked.svg)

![Per-version LOC raw-unit ranked chart](docs/plots/version_loc_units_ranked.svg)

<details>
<summary><strong>Show canonical-order per-version raw-unit plots</strong></summary>

![Per-version CPU raw-unit chart](docs/plots/version_cpu_units.svg)

![Per-version wall raw-unit chart](docs/plots/version_wall_units.svg)

![Per-version memory raw-unit chart](docs/plots/version_memory_units.svg)

![Per-version LOC raw-unit chart](docs/plots/version_loc_units.svg)

</details>

#### Per-version normalized score plots (full 26-task suite)

![Per-version objective ranked score chart](docs/plots/version_objective_ranked.svg)

![Per-version opinionated ranked score chart](docs/plots/version_opinionated_ranked.svg)

![Per-version overall ranked score chart](docs/plots/version_overall_ranked.svg)

![Per-version scalability ranked score chart](docs/plots/version_scalability_ranked.svg)

<details>
<summary><strong>Show canonical-order per-version normalized score plots</strong></summary>

![Per-version objective score chart](docs/plots/version_objective.svg)

![Per-version opinionated score chart](docs/plots/version_opinionated.svg)

![Per-version overall score chart](docs/plots/version_overall.svg)

![Per-version scalability score chart](docs/plots/version_scalability.svg)

</details>

#### Per-version scalability growth plots (full 26-task suite)

![Per-version wall-time growth curve ranked legend](docs/plots/version_scalability_curve_ranked.svg)

![Per-version memory growth curve ranked legend](docs/plots/version_scalability_memory_curve_ranked.svg)

![Per-version L/S growth ratio summary ranked](docs/plots/version_scalability_growth_ratios_ranked.svg)

<details>
<summary><strong>Show canonical-order per-version scalability growth plots</strong></summary>

![Per-version wall-time growth curve](docs/plots/version_scalability_curve.svg)

![Per-version memory growth curve](docs/plots/version_scalability_memory_curve.svg)

![Per-version L/S growth ratio summary](docs/plots/version_scalability_growth_ratios.svg)

</details>


### Per-version score tables

These tables show the **version-matrix comparison snapshot** from `20260423T043938Z`. This is a supplemental view so that all benchmarked runtime versions appear in README tables too.
**Important:** this per-version comparison now covers the **full 26-task suite**. Tasks in this supplemental run: `ai_service_integration`, `api_client`, `basic_blockchain`, `basic_web_application`, `binary_search_tree`, `chat_application`, `cli_file_search`, `csv_parsing`, `data_visualization`, `decision_tree`, `file_io_large`, `gui_calculator`, `image_resizing`, `linear_regression`, `matrix_multiplication`, `prime_sieve`, `producer_consumer`, `rest_api`, `sentiment_analysis`, `simple_web_server`, `socket_programming`, `sort_integers`, `sqlite_crud`, `third_party_api`, `tic_tac_toe`, `web_scraper`.
These tables are rescored from one combined raw-row comparison pool, so the normalization is consistent across all listed runtime versions.
Interpretive inputs such as rubric/community are still shared at the language-family level today, so the **objective** per-version table is the cleanest pure runtime comparison.

#### Per-version blended overview (full 26-task suite)

| Runtime | Overall | Objective | Opinionated | Tasks |
|---|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 67.69 | 48.32 | 82.91 | 26 |
| Go 1.23 [x86_64] | 58.13 | 23.84 | 85.08 | 26 |
| C++ (GCC 14) [x86_64] | 56.57 | 34.63 | 73.80 | 26 |
| Python 3.11 [x86_64] | 55.06 | 12.03 | 88.88 | 26 |
| Python 3.12 [x86_64] | 55.02 | 11.64 | 89.11 | 26 |
| Python 3.8 [x86_64] | 54.62 | 12.82 | 87.46 | 26 |
| Node.js 22 [x86_64] | 53.57 | 8.57 | 88.93 | 26 |
| Java 21 [x86_64] | 53.32 | 6.20 | 90.34 | 26 |
| Deno 2.7.6 [x86_64] | 51.13 | 7.55 | 85.36 | 26 |
| Bun 1.3.12 [x86_64] | 51.11 | 8.58 | 84.53 | 26 |
| Python 2.7 [x86_64] | 49.16 | 15.20 | 75.85 | 26 |
| PHP 7.4 [x86_64] | 46.52 | 11.22 | 74.26 | 26 |
| PHP 8.4 [x86_64] | 46.48 | 10.72 | 74.58 | 26 |
| PHP 7.2 [x86_64] | 42.59 | 10.64 | 67.69 | 26 |
| PHP 5.6 [x86_64] | 38.62 | 10.32 | 60.86 | 26 |

#### Per-version objective results (full 26-task suite)

| Runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---:|---:|---:|---:|---:|---:|
| Rust 1.82 [x86_64] | 48.32 | 41.28 | 40.32 | 73.31 | 41.77 | 26 |
| C++ (GCC 14) [x86_64] | 34.63 | 26.67 | 25.74 | 63.26 | 26.25 | 26 |
| Go 1.23 [x86_64] | 23.84 | 20.74 | 20.29 | 28.63 | 31.35 | 26 |
| Python 2.7 [x86_64] | 15.20 | 4.14 | 3.30 | 28.60 | 46.41 | 26 |
| Python 3.8 [x86_64] | 12.82 | 2.26 | 1.52 | 22.61 | 47.53 | 26 |
| Python 3.11 [x86_64] | 12.03 | 2.50 | 1.72 | 18.50 | 47.53 | 26 |
| Python 3.12 [x86_64] | 11.64 | 2.22 | 1.46 | 17.54 | 47.53 | 26 |
| PHP 7.4 [x86_64] | 11.22 | 5.83 | 4.76 | 14.41 | 33.56 | 26 |
| PHP 8.4 [x86_64] | 10.72 | 5.47 | 4.42 | 13.20 | 33.56 | 26 |
| PHP 7.2 [x86_64] | 10.64 | 5.15 | 4.06 | 13.77 | 33.56 | 26 |
| PHP 5.6 [x86_64] | 10.32 | 4.43 | 3.39 | 15.12 | 32.20 | 26 |
| Bun 1.3.12 [x86_64] | 8.58 | 2.65 | 2.04 | 8.27 | 38.16 | 26 |
| Node.js 22 [x86_64] | 8.57 | 2.56 | 1.89 | 8.60 | 38.16 | 26 |
| Deno 2.7.6 [x86_64] | 7.55 | 1.92 | 1.62 | 5.37 | 38.16 | 26 |
| Java 21 [x86_64] | 6.20 | 1.05 | 0.59 | 6.66 | 30.53 | 26 |

#### Per-version opinionated results (full 26-task suite)

| Runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java 21 [x86_64] | 90.34 | 79.55 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 26 |
| Python 3.12 [x86_64] | 89.11 | 80.78 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 26 |
| Node.js 22 [x86_64] | 88.93 | 82.96 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 26 |
| Python 3.11 [x86_64] | 88.88 | 79.68 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 26 |
| Python 3.8 [x86_64] | 87.46 | 78.06 | 100.00 | 98.45 | 88.89 | 90.00 | 100.00 | 70.00 | 26 |
| Deno 2.7.6 [x86_64] | 85.36 | 81.88 | 88.89 | 100.00 | 77.78 | 90.00 | 80.00 | 80.00 | 26 |
| Go 1.23 [x86_64] | 85.08 | 71.44 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 26 |
| Bun 1.3.12 [x86_64] | 84.53 | 83.01 | 88.89 | 100.00 | 77.78 | 80.00 | 80.00 | 80.00 | 26 |
| Rust 1.82 [x86_64] | 82.91 | 76.06 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 26 |
| Python 2.7 [x86_64] | 75.85 | 72.58 | 77.78 | 98.45 | 77.78 | 70.00 | 80.00 | 60.00 | 26 |
| PHP 8.4 [x86_64] | 74.58 | 79.10 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 26 |
| PHP 7.4 [x86_64] | 74.26 | 77.60 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 26 |
| C++ (GCC 14) [x86_64] | 73.80 | 74.36 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 26 |
| PHP 7.2 [x86_64] | 67.69 | 78.22 | 66.67 | 77.32 | 66.67 | 70.00 | 80.00 | 40.00 | 26 |
| PHP 5.6 [x86_64] | 60.86 | 68.76 | 55.56 | 77.32 | 66.67 | 60.00 | 60.00 | 40.00 | 26 |

<details>
<summary><strong>Show language-family summary for this full runnable 26-task suite</strong></summary>


### Language-family summary for this full runnable 26-task suite

This family-collapsed summary keeps one **primary runtime** per language family from this **full runnable 26-task suite** so you can compare the published artifact at the language-family level.

| Language family | Primary runtime | Overall | Objective | Opinionated | Tasks |
|---|---|---:|---:|---:|---:|
| Rust | Rust 1.82 [x86_64] | 67.31 | 47.49 | 82.89 | 26 |
| Go | Go 1.23 [x86_64] | 58.05 | 23.45 | 85.24 | 26 |
| C++ | C++ (GCC 14) [x86_64] | 56.26 | 34.07 | 73.69 | 26 |
| Python | Python 3.12 [x86_64] | 55.05 | 11.60 | 89.19 | 26 |
| JavaScript (Node.js) | Node.js 22 [x86_64] | 53.64 | 8.54 | 89.07 | 26 |
| Java | Java 21 [x86_64] | 53.33 | 6.23 | 90.34 | 26 |
| PHP | PHP 8.4 [x86_64] | 46.53 | 10.75 | 74.65 | 26 |

#### Objective / unopinionated family summary for this full runnable 26-task suite

| Language family | Primary runtime | Objective | CPU | Wall | Memory | LOC | Tasks |
|---|---|---:|---:|---:|---:|---:|---:|
| Rust | Rust 1.82 [x86_64] | 47.49 | 40.00 | 38.94 | 73.37 | 41.77 | 26 |
| C++ | C++ (GCC 14) [x86_64] | 34.07 | 25.93 | 24.67 | 63.32 | 26.25 | 26 |
| Go | Go 1.23 [x86_64] | 23.45 | 20.32 | 19.79 | 28.22 | 31.35 | 26 |
| Python | Python 3.12 [x86_64] | 11.60 | 2.16 | 1.40 | 17.56 | 47.53 | 26 |
| PHP | PHP 8.4 [x86_64] | 10.75 | 5.55 | 4.45 | 13.16 | 33.56 | 26 |
| JavaScript (Node.js) | Node.js 22 [x86_64] | 8.54 | 2.53 | 1.88 | 8.51 | 38.16 | 26 |
| Java | Java 21 [x86_64] | 6.23 | 1.10 | 0.66 | 6.63 | 30.53 | 26 |

#### Opinionated / interpretive family summary for this full runnable 26-task suite

| Language family | Primary runtime | Opinionated | Scalability | Ease | Community | Debugging | Docs | Libraries | Concurrency | Tasks |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Java | Java 21 [x86_64] | 90.34 | 79.57 | 77.78 | 92.78 | 100.00 | 90.00 | 100.00 | 100.00 | 26 |
| Python | Python 3.12 [x86_64] | 89.19 | 81.16 | 100.00 | 98.45 | 88.89 | 100.00 | 100.00 | 70.00 | 26 |
| JavaScript (Node.js) | Node.js 22 [x86_64] | 89.07 | 83.60 | 88.89 | 100.00 | 88.89 | 90.00 | 100.00 | 80.00 | 26 |
| Go | Go 1.23 [x86_64] | 85.24 | 72.21 | 88.89 | 88.66 | 77.78 | 90.00 | 80.00 | 100.00 | 26 |
| Rust | Rust 1.82 [x86_64] | 82.89 | 75.93 | 66.67 | 93.81 | 77.78 | 90.00 | 90.00 | 90.00 | 26 |
| PHP | PHP 8.4 [x86_64] | 74.65 | 79.41 | 77.78 | 77.32 | 77.78 | 80.00 | 90.00 | 50.00 | 26 |
| C++ | C++ (GCC 14) [x86_64] | 73.69 | 73.86 | 44.44 | 81.44 | 88.89 | 70.00 | 80.00 | 80.00 | 26 |

</details>

### Rubric evidence and sources

These rubric values are language-family level judgments sourced from official or canonical references and used by the opinionated portion of the benchmark. They are reviewed separately from any single benchmark run.

<details>
<summary><strong>PHP</strong> — reviewed 2026-04-22</summary>

- **Scores:** ease 7/10, debugging 7/10, docs 8/10, libraries 9/10, concurrency 5/10
- **Summary:** PHP remains easy to ship for everyday web work, has strong official/manual coverage and a massive package ecosystem, but its built-in concurrency story is still much weaker and less central than in runtimes designed around threads, workers, or goroutines.

Category rationale:

- **Ease:** PHP keeps a relatively small surface area for standard application code and has a familiar request-response programming model, but long-term maintainability can vary more across codebases because the ecosystem spans multiple major styles and framework conventions.
- **Debugging:** The core language plus Xdebug give PHP a mature enough debugging workflow, but the debugging/tooling story is less uniformly strong than in Java or Python-heavy environments.
- **Docs:** The official manual is broad, stable, and still one of PHP's strongest assets, though documentation quality outside the core manual varies by framework and package.
- **Libraries:** Packagist and Composer provide a very large and production-proven package ecosystem, especially for web/backend development.
- **Concurrency:** Modern PHP has Fibers and event-driven libraries, but concurrency is still less idiomatic and less built into the mainstream development model than in Go, Java, or Rust.

Sources:

- [PHP Documentation](https://www.php.net/docs.php) — official
- [PHP Fibers manual](https://www.php.net/manual/en/language.fibers.php) — official
- [Xdebug documentation](https://xdebug.org/docs/) — official
- [Packagist](https://packagist.org/) — official

</details>

<details>
<summary><strong>Python</strong> — reviewed 2026-04-22</summary>

- **Scores:** ease 9/10, debugging 8/10, docs 10/10, libraries 10/10, concurrency 7/10
- **Summary:** Python remains one of the easiest languages to read and teach, has outstanding official documentation and the largest general-purpose package ecosystem in the set, but its mainstream concurrency story is still shaped by tradeoffs such as the GIL and the need to choose among threads, processes, and async.

Category rationale:

- **Ease:** Python's syntax and standard library conventions strongly favor readability and low ceremony, which makes simple implementations and maintenance comparatively easy.
- **Debugging:** Python has solid built-in debugging support and excellent IDE/tool support, though the runtime model is not as debugger-centric as Java.
- **Docs:** The official Python docs are deep, broad, and well organized across the language reference, standard library, tutorials, and HOWTO material.
- **Libraries:** PyPI is the dominant ecosystem for general-purpose scripting, data tooling, ML, web, and automation libraries.
- **Concurrency:** Python supports threads, processes, asyncio, and futures well enough for most workloads, but the model is split across multiple approaches and CPU-bound parallelism still carries more caveats than in Go or Java.

Sources:

- [Python documentation](https://docs.python.org/3/) — official
- [pdb](https://docs.python.org/3/library/pdb.html) — official
- [PyPI](https://pypi.org/) — official
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) — official

</details>

<details>
<summary><strong>Java</strong> — reviewed 2026-04-22</summary>

- **Scores:** ease 7/10, debugging 9/10, docs 9/10, libraries 10/10, concurrency 10/10
- **Summary:** Java remains more verbose than scripting-oriented languages, but it has first-class debugger architecture, very mature official documentation, the deepest enterprise library story in the set, and one of the strongest concurrency platforms available.

Category rationale:

- **Ease:** Java still carries more ceremony than Python, Go, or Node.js for small tasks, even though modern Java has improved significantly.
- **Debugging:** The platform ships with a formal debugger architecture and standard debugger tooling, which makes the debugging story exceptionally mature.
- **Docs:** Oracle's platform docs and API references are extensive and highly structured.
- **Libraries:** The JVM ecosystem and Maven Central make Java one of the broadest and most mature library ecosystems in software.
- **Concurrency:** Java's standard concurrency stack is exceptionally strong and explicit, with mature threading, executors, futures, structured primitives, and long-standing tooling support.

Sources:

- [Java SE 21 documentation](https://docs.oracle.com/en/java/javase/21/) — official
- [The jdb Command](https://docs.oracle.com/en/java/javase/21/docs/specs/man/jdb.html) — official
- [Java concurrency](https://docs.oracle.com/en/java/javase/21/core/concurrency.html) — official
- [Maven Central](https://search.maven.org/) — official

</details>

<details>
<summary><strong>C++</strong> — reviewed 2026-04-22</summary>

- **Scores:** ease 4/10, debugging 8/10, docs 7/10, libraries 8/10, concurrency 8/10
- **Summary:** C++ offers huge performance and control, plus strong native tooling and a rich library landscape, but its language complexity and the lack of one single official learning/documentation hub make it harder to learn and maintain than the others.

Category rationale:

- **Ease:** C++ remains the hardest language in the benchmark set for everyday readability and maintainability because of its language complexity, value-category rules, templates, memory model, and broad feature surface.
- **Debugging:** Native debugging with GDB and IDE integrations is strong, even if optimized C++ can still be difficult to inspect.
- **Docs:** C++ lacks a single official, centralized documentation experience comparable to Python or Java; cppreference is excellent, but it is a canonical community resource rather than an official language publisher.
- **Libraries:** C++ has deep standard-library and third-party ecosystems, and package-manager support has improved materially with tools like vcpkg.
- **Concurrency:** The standard library includes mature threading and synchronization primitives, though writing correct concurrent C++ remains more expert-heavy than in Go or Java.

Sources:

- [cppreference](https://en.cppreference.com/) — canonical
- [C++ concurrency support library](https://en.cppreference.com/w/cpp/thread) — canonical
- [Debugging with GDB](https://sourceware.org/gdb/current/onlinedocs/gdb) — official
- [vcpkg packages](https://vcpkg.io/en/packages.html) — official

</details>

<details>
<summary><strong>JavaScript (Node.js)</strong> — reviewed 2026-04-22</summary>

- **Scores:** ease 8/10, debugging 8/10, docs 9/10, libraries 10/10, concurrency 8/10
- **Summary:** Node.js stays highly productive for small-to-medium services and tooling, has excellent official docs, and sits on top of npm's enormous package registry, while offering practical concurrency via the event loop, worker threads, and the broader async ecosystem.

Category rationale:

- **Ease:** Node.js keeps implementation friction low for web, tooling, and API-style work, though async-heavy code can still become harder to reason about at scale.
- **Debugging:** Node ships documented debugger support and is well supported by mainstream tooling and IDE workflows.
- **Docs:** The official Node.js API documentation is extensive and consistently maintained.
- **Libraries:** npm remains one of the largest and most accessible package ecosystems in software.
- **Concurrency:** Node's concurrency story is good in practice through async I/O and worker threads, but it is still less direct for CPU-bound parallel work than Go or Java.

Sources:

- [Node.js API documentation](https://nodejs.org/api/) — official
- [Node.js debugger](https://nodejs.org/api/debugger.html) — official
- [Worker threads](https://nodejs.org/api/worker_threads.html) — official
- [npm About](https://www.npmjs.com/about) — official

</details>

<details>
<summary><strong>Go</strong> — reviewed 2026-04-22</summary>

- **Scores:** ease 8/10, debugging 7/10, docs 9/10, libraries 8/10, concurrency 10/10
- **Summary:** Go keeps the language small and readable, documents the language and ecosystem clearly, and has arguably the most direct built-in concurrency ergonomics in the set; its library ecosystem is broad, though not as vast as Python, Node, or Java.

Category rationale:

- **Ease:** Go is intentionally small, readable, and convention-heavy, which lowers implementation and maintenance overhead for many backend and systems tasks.
- **Debugging:** Go's debugging story is solid but not best-in-class; the project documentation itself points out caveats around GDB and recommends purpose-built tooling like Delve.
- **Docs:** Go's official documentation hub and package discovery experience are clear, opinionated, and unusually approachable.
- **Libraries:** Go has a strong standard library and a healthy module ecosystem, but the overall breadth is still smaller than the largest ecosystems in this benchmark.
- **Concurrency:** Goroutines and channels remain one of Go's defining strengths, making concurrency unusually central, ergonomic, and well documented.

Sources:

- [Go documentation](https://go.dev/doc) — official
- [Go Packages](https://pkg.go.dev/about) — official
- [Debugging Go Code with GDB](https://go.dev/doc/gdb) — official
- [Share Memory By Communicating](https://go.dev/doc/codewalk/sharemem/) — official

</details>

<details>
<summary><strong>Rust</strong> — reviewed 2026-04-22</summary>

- **Scores:** ease 6/10, debugging 7/10, docs 9/10, libraries 9/10, concurrency 9/10
- **Summary:** Rust has a steeper learning curve than the other non-C++ languages here, but compensates with excellent official documentation, a fast-growing crates ecosystem, and a strong native-threading/concurrency story built around memory safety.

Category rationale:

- **Ease:** Rust is harder to learn and maintain than Python, Go, Node.js, or Java because ownership, borrowing, and lifetime constraints demand more upfront precision.
- **Debugging:** Rust has good native-debugging support and dedicated debugger-visualizer features, but the debugging workflow is still less turnkey than Java's and can be more demanding than Python's.
- **Docs:** Rust's official docs ecosystem is unusually rich, spanning the Book, Reference, std docs, rustdoc output, and other first-party books.
- **Libraries:** crates.io provides a broad and fast-moving ecosystem that is now strong across systems, CLI, async, web, and serialization workloads.
- **Concurrency:** Rust's standard library and language guarantees make concurrent code comparatively powerful and safe, even if the learning curve is higher than in Go.

Sources:

- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/ch00-00-introduction.html) — official
- [Rust documentation overview](https://doc.rust-lang.org/) — official
- [std::thread](https://doc.rust-lang.org/std/thread/index.html) — official
- [crates.io](https://crates.io/) — official

</details>


### Raw-unit plots for the supplemental per-version runtime comparison (`20260423T043938Z`)

These plots use real units rather than internal normalized scores. CPU and wall time are shown as total median time across the active comparison view, memory is shown as average median peak RSS, and LOC is shown as average lines per task.

**CPU time (ranked):** raw total CPU time across the suite; **lower is better**.

![CPU raw-unit ranked chart](docs/plots/version_cpu_units_ranked.svg)

**Wall time (ranked):** raw total elapsed time across the suite; **lower is better**.

![Wall raw-unit ranked chart](docs/plots/version_wall_units_ranked.svg)

**Memory (ranked):** average median peak RSS; **lower is better**.

![Memory raw-unit ranked chart](docs/plots/version_memory_units_ranked.svg)

**LOC (ranked):** average lines of code per task; **lower is better**.

![LOC raw-unit ranked chart](docs/plots/version_loc_units_ranked.svg)

<details>
<summary><strong>Show canonical-order raw-unit plots for this snapshot</strong></summary>

These plots keep the fixed configured runtime-variant order instead of sorting by performance.

![CPU raw-unit chart](docs/plots/version_cpu_units.svg)

![Wall raw-unit chart](docs/plots/version_wall_units.svg)

![Memory raw-unit chart](docs/plots/version_memory_units.svg)

![LOC raw-unit chart](docs/plots/version_loc_units.svg)

</details>

### Language best-case raw-unit plots

These charts collapse the runtime variants and keep only the best measured version for each language family for the metric being plotted.

![Best-case CPU raw-unit ranked chart](docs/plots/version_best_case_cpu_units_ranked.svg)

![Best-case Wall raw-unit ranked chart](docs/plots/version_best_case_wall_units_ranked.svg)

![Best-case Memory raw-unit ranked chart](docs/plots/version_best_case_memory_units_ranked.svg)

![Best-case LOC raw-unit ranked chart](docs/plots/version_best_case_loc_units_ranked.svg)

<details>
<summary><strong>Show canonical-order best-case raw-unit plots</strong></summary>

These plots keep the fixed canonical language-family order instead of sorting by performance.

![Best-case CPU raw-unit chart](docs/plots/version_best_case_cpu_units.svg)

![Best-case Wall raw-unit chart](docs/plots/version_best_case_wall_units.svg)

![Best-case Memory raw-unit chart](docs/plots/version_best_case_memory_units.svg)

![Best-case LOC raw-unit chart](docs/plots/version_best_case_loc_units.svg)

</details>

### Objective / unopinionated score plots

These recomputed score plots keep only directly measurable benchmark dimensions. They intentionally exclude scalability and all rubric/community-driven scores.

**Objective score (ranked):** recomputed from CPU, wall, memory, and LOC only; **higher is better**.

![Objective ranked score chart](docs/plots/version_objective_ranked.svg)

<details>
<summary><strong>Show canonical-order objective plots</strong></summary>

**Objective score (canonical):** same metric in fixed benchmark language order.

![Objective score chart](docs/plots/version_objective.svg)

**Objective component score plots:** normalized objective-only views of CPU, wall, memory, and LOC.

![CPU score chart](docs/plots/version_cpu.svg)

![Wall score chart](docs/plots/version_wall.svg)

![Memory score chart](docs/plots/version_memory.svg)

![LOC score chart](docs/plots/version_loc.svg)

</details>

**Objective component score plots (ranked):** normalized objective-only views of CPU, wall, memory, and LOC sorted best to worst.

![CPU ranked score chart](docs/plots/version_cpu_ranked.svg)

![Wall ranked score chart](docs/plots/version_wall_ranked.svg)

![Memory ranked score chart](docs/plots/version_memory_ranked.svg)

![LOC ranked score chart](docs/plots/version_loc_ranked.svg)

### Language best-case objective / unopinionated score plots

![Best-case objective ranked score chart](docs/plots/version_best_case_objective_ranked.svg)

![Best-case CPU ranked score chart](docs/plots/version_best_case_cpu_ranked.svg)

![Best-case Wall ranked score chart](docs/plots/version_best_case_wall_ranked.svg)

![Best-case Memory ranked score chart](docs/plots/version_best_case_memory_ranked.svg)

![Best-case LOC ranked score chart](docs/plots/version_best_case_loc_ranked.svg)

<details>
<summary><strong>Show canonical-order best-case objective plots</strong></summary>

![Best-case objective score chart](docs/plots/version_best_case_objective.svg)

![Best-case CPU score chart](docs/plots/version_best_case_cpu.svg)

![Best-case Wall score chart](docs/plots/version_best_case_wall.svg)

![Best-case Memory score chart](docs/plots/version_best_case_memory.svg)

![Best-case LOC score chart](docs/plots/version_best_case_loc.svg)

</details>

### Geometric-mean runtime views

These views reduce the influence of extreme outliers by taking the geometric mean of normalized per-task/per-size runtime efficiency ratios.

![CPU geometric-mean ranked chart](docs/plots/version_cpu_geomean_ranked.svg)

![Wall-time geometric-mean ranked chart](docs/plots/version_wall_geomean_ranked.svg)

<details>
<summary><strong>Show canonical-order geometric-mean plots</strong></summary>

![CPU geometric-mean chart](docs/plots/version_cpu_geomean.svg)

![Wall-time geometric-mean chart](docs/plots/version_wall_geomean.svg)

</details>

### Variance / confidence summary

These plots summarize average coefficient of variation across the measured medians. Lower values mean less relative run-to-run variation.

![CPU variance ranked chart](docs/plots/version_variance_cpu_ranked.svg)

![Wall variance ranked chart](docs/plots/version_variance_wall_ranked.svg)

![Memory variance ranked chart](docs/plots/version_variance_memory_ranked.svg)

<details>
<summary><strong>Show canonical-order variance plots</strong></summary>

![CPU variance chart](docs/plots/version_variance_cpu.svg)

![Wall variance chart](docs/plots/version_variance_wall.svg)

![Memory variance chart](docs/plots/version_variance_memory.svg)

</details>

### Opinionated / interpretive score plots

These recomputed score plots keep only interpretive or hybrid dimensions, including scalability and rubric/community-style scores.

**Opinionated score (ranked):** recomputed from scalability, ease, community, debugging, docs, libraries, and concurrency; **higher is better**.

![Opinionated ranked score chart](docs/plots/version_opinionated_ranked.svg)

<details>
<summary><strong>Show canonical-order opinionated plots</strong></summary>

**Opinionated score (canonical):** same metric in fixed benchmark language order.

![Opinionated score chart](docs/plots/version_opinionated.svg)

**Scalability remains visible here because it belongs to the interpretive/hybrid category in this split.**

![Scalability chart](docs/plots/version_scalability.svg)

</details>

![Scalability ranked chart](docs/plots/version_scalability_ranked.svg)

### Language best-case opinionated / interpretive score plots

![Best-case opinionated ranked score chart](docs/plots/version_best_case_opinionated_ranked.svg)

![Best-case scalability ranked chart](docs/plots/version_best_case_scalability_ranked.svg)

<details>
<summary><strong>Show canonical-order best-case opinionated plots</strong></summary>

![Best-case opinionated score chart](docs/plots/version_best_case_opinionated.svg)

![Best-case scalability chart](docs/plots/version_best_case_scalability.svg)

</details>

### Blended composite plots sorted best to worst

These are the legacy blended plots that combine both objective and opinionated inputs into one composite view. They are kept for reference, but the split sections above are the primary interpretation.

**Overall score (ranked):** best weighted composite score appears first; **higher is better**.

![Overall ranked score chart](docs/plots/version_overall_ranked.svg)

**CPU efficiency score (ranked):** best CPU efficiency appears first; **lower raw CPU time = higher plotted score**.

![CPU ranked score chart](docs/plots/version_cpu_ranked.svg)

**Wall-clock efficiency score (ranked):** best elapsed-time efficiency appears first; **lower raw runtime = higher plotted score**.

![Wall ranked score chart](docs/plots/version_wall_ranked.svg)

**Memory efficiency score (ranked):** best memory efficiency appears first; **lower raw memory usage = higher plotted score**.

![Memory ranked score chart](docs/plots/version_memory_ranked.svg)

**Scalability score (ranked):** best aggregate scalability score appears first; **higher is better**.

![Scalability ranked chart](docs/plots/version_scalability_ranked.svg)

<details>
<summary><strong>Show canonical-order blended composite plots</strong></summary>

### Blended composite plots in canonical language order

These plots keep the same left-to-right language order every time: `php`, `python`, `java`, `cpp`, `node`, `go`, `rust`.

**Overall score:** weighted composite benchmark score; **higher is better**.

![Overall score chart](docs/plots/version_overall.svg)

**CPU efficiency score:** derived from raw CPU time; **lower raw CPU time = higher plotted score**.

![CPU score chart](docs/plots/version_cpu.svg)

**Wall-clock efficiency score:** derived from elapsed runtime; **lower raw runtime = higher plotted score**.

![Wall score chart](docs/plots/version_wall.svg)

**Memory efficiency score:** derived from max RSS memory; **lower raw memory usage = higher plotted score**.

![Memory score chart](docs/plots/version_memory.svg)

**Scalability score:** aggregate score derived from S → M → L growth; **higher is better**.

![Scalability chart](docs/plots/version_scalability.svg)

</details>

### Blended composite plots as language best-case scenarios

These charts keep only the best-performing tested version of each language for the metric being plotted.

![Best-case overall ranked score chart](docs/plots/version_best_case_overall_ranked.svg)

![Best-case CPU ranked score chart](docs/plots/version_best_case_cpu_ranked.svg)

![Best-case Wall ranked score chart](docs/plots/version_best_case_wall_ranked.svg)

![Best-case Memory ranked score chart](docs/plots/version_best_case_memory_ranked.svg)

![Best-case Scalability ranked chart](docs/plots/version_best_case_scalability_ranked.svg)

<details>
<summary><strong>Show canonical-order best-case blended plots</strong></summary>

![Best-case overall score chart](docs/plots/version_best_case_overall.svg)

![Best-case CPU score chart](docs/plots/version_best_case_cpu.svg)

![Best-case Wall score chart](docs/plots/version_best_case_wall.svg)

![Best-case Memory score chart](docs/plots/version_best_case_memory.svg)

![Best-case Scalability chart](docs/plots/version_best_case_scalability.svg)

</details>

### Scalability growth charts

The old scalability curves were too abstract and often looked flat because they were based on a score that did not vary by size. These updated charts now use actual growth ratios derived from measured medians, so they are easier to read. In every chart below, **lower is better**.

**Wall-time growth curves (ranked legend):** S is fixed at **1.0x** and M/L show average wall-time growth relative to S.

![Wall-time growth curve ranked legend](docs/plots/version_scalability_curve_ranked.svg)

**Memory growth curves (ranked legend):** S is fixed at **1.0x** and M/L show average memory growth relative to S.

![Memory growth curve ranked legend](docs/plots/version_scalability_memory_curve_ranked.svg)

**L/S ratio summary bars (ranked):** side-by-side bars compare final large-vs-small growth for wall time and memory.

![L/S growth ratio summary ranked](docs/plots/version_scalability_growth_ratios_ranked.svg)

<details>
<summary><strong>Show canonical-order scalability growth charts</strong></summary>

![Wall-time growth curve](docs/plots/version_scalability_curve.svg)

![Memory growth curve](docs/plots/version_scalability_memory_curve.svg)

![L/S growth ratio summary](docs/plots/version_scalability_growth_ratios.svg)

</details>

### Per-task score plots

The sections below avoid reducing the suite to one global aggregate. Each task gets its own score plot for all tested runtime variants and then a language best-case view.

<details>
<summary><strong>ai_service_integration</strong> — Integrating with AI services (e.g., OpenAI API or MCP services)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![ai_service_integration ranked score chart](docs/plots/version_task_ai_service_integration_ranked.svg)

![ai_service_integration canonical score chart](docs/plots/version_task_ai_service_integration.svg)

![ai_service_integration best-case ranked score chart](docs/plots/version_best_case_task_ai_service_integration_ranked.svg)

![ai_service_integration best-case canonical score chart](docs/plots/version_best_case_task_ai_service_integration.svg)

![ai_service_integration baseline delta ranked chart](docs/plots/version_task_baseline_ai_service_integration_ranked.svg)

</details>

<details>
<summary><strong>api_client</strong> — Implementing a simple API client (fetching data from a public API)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![api_client ranked score chart](docs/plots/version_task_api_client_ranked.svg)

![api_client canonical score chart](docs/plots/version_task_api_client.svg)

![api_client best-case ranked score chart](docs/plots/version_best_case_task_api_client_ranked.svg)

![api_client best-case canonical score chart](docs/plots/version_best_case_task_api_client.svg)

![api_client baseline delta ranked chart](docs/plots/version_task_baseline_api_client_ranked.svg)

</details>

<details>
<summary><strong>basic_blockchain</strong> — Implementing a basic blockchain</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![basic_blockchain ranked score chart](docs/plots/version_task_basic_blockchain_ranked.svg)

![basic_blockchain canonical score chart](docs/plots/version_task_basic_blockchain.svg)

![basic_blockchain best-case ranked score chart](docs/plots/version_best_case_task_basic_blockchain_ranked.svg)

![basic_blockchain best-case canonical score chart](docs/plots/version_best_case_task_basic_blockchain.svg)

![basic_blockchain baseline delta ranked chart](docs/plots/version_task_baseline_basic_blockchain_ranked.svg)

</details>

<details>
<summary><strong>basic_web_application</strong> — Implementing a basic web application (a to-do list)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![basic_web_application ranked score chart](docs/plots/version_task_basic_web_application_ranked.svg)

![basic_web_application canonical score chart](docs/plots/version_task_basic_web_application.svg)

![basic_web_application best-case ranked score chart](docs/plots/version_best_case_task_basic_web_application_ranked.svg)

![basic_web_application best-case canonical score chart](docs/plots/version_best_case_task_basic_web_application.svg)

![basic_web_application baseline delta ranked chart](docs/plots/version_task_baseline_basic_web_application_ranked.svg)

</details>

<details>
<summary><strong>binary_search_tree</strong> — Implementing a basic data structure (binary search tree)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![binary_search_tree ranked score chart](docs/plots/version_task_binary_search_tree_ranked.svg)

![binary_search_tree canonical score chart](docs/plots/version_task_binary_search_tree.svg)

![binary_search_tree best-case ranked score chart](docs/plots/version_best_case_task_binary_search_tree_ranked.svg)

![binary_search_tree best-case canonical score chart](docs/plots/version_best_case_task_binary_search_tree.svg)

![binary_search_tree baseline delta ranked chart](docs/plots/version_task_baseline_binary_search_tree_ranked.svg)

</details>

<details>
<summary><strong>chat_application</strong> — Implementing a simple chat application</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![chat_application ranked score chart](docs/plots/version_task_chat_application_ranked.svg)

![chat_application canonical score chart](docs/plots/version_task_chat_application.svg)

![chat_application best-case ranked score chart](docs/plots/version_best_case_task_chat_application_ranked.svg)

![chat_application best-case canonical score chart](docs/plots/version_best_case_task_chat_application.svg)

![chat_application baseline delta ranked chart](docs/plots/version_task_baseline_chat_application_ranked.svg)

</details>

<details>
<summary><strong>cli_file_search</strong> — Implementing a basic command-line tool (a file search utility)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![cli_file_search ranked score chart](docs/plots/version_task_cli_file_search_ranked.svg)

![cli_file_search canonical score chart](docs/plots/version_task_cli_file_search.svg)

![cli_file_search best-case ranked score chart](docs/plots/version_best_case_task_cli_file_search_ranked.svg)

![cli_file_search best-case canonical score chart](docs/plots/version_best_case_task_cli_file_search.svg)

![cli_file_search baseline delta ranked chart](docs/plots/version_task_baseline_cli_file_search_ranked.svg)

</details>

<details>
<summary><strong>csv_parsing</strong> — Processing a large dataset (CSV file parsing)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![csv_parsing ranked score chart](docs/plots/version_task_csv_parsing_ranked.svg)

![csv_parsing canonical score chart](docs/plots/version_task_csv_parsing.svg)

![csv_parsing best-case ranked score chart](docs/plots/version_best_case_task_csv_parsing_ranked.svg)

![csv_parsing best-case canonical score chart](docs/plots/version_best_case_task_csv_parsing.svg)

![csv_parsing baseline delta ranked chart](docs/plots/version_task_baseline_csv_parsing_ranked.svg)

</details>

<details>
<summary><strong>data_visualization</strong> — Implementing a simple data visualization task (plotting a graph)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![data_visualization ranked score chart](docs/plots/version_task_data_visualization_ranked.svg)

![data_visualization canonical score chart](docs/plots/version_task_data_visualization.svg)

![data_visualization best-case ranked score chart](docs/plots/version_best_case_task_data_visualization_ranked.svg)

![data_visualization best-case canonical score chart](docs/plots/version_best_case_task_data_visualization.svg)

![data_visualization baseline delta ranked chart](docs/plots/version_task_baseline_data_visualization_ranked.svg)

</details>

<details>
<summary><strong>decision_tree</strong> — Implementing a basic machine learning model (decision tree)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![decision_tree ranked score chart](docs/plots/version_task_decision_tree_ranked.svg)

![decision_tree canonical score chart](docs/plots/version_task_decision_tree.svg)

![decision_tree best-case ranked score chart](docs/plots/version_best_case_task_decision_tree_ranked.svg)

![decision_tree best-case canonical score chart](docs/plots/version_best_case_task_decision_tree.svg)

![decision_tree baseline delta ranked chart](docs/plots/version_task_baseline_decision_tree_ranked.svg)

</details>

<details>
<summary><strong>file_io_large</strong> — Performing file I/O operations on a large file</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![file_io_large ranked score chart](docs/plots/version_task_file_io_large_ranked.svg)

![file_io_large canonical score chart](docs/plots/version_task_file_io_large.svg)

![file_io_large best-case ranked score chart](docs/plots/version_best_case_task_file_io_large_ranked.svg)

![file_io_large best-case canonical score chart](docs/plots/version_best_case_task_file_io_large.svg)

![file_io_large baseline delta ranked chart](docs/plots/version_task_baseline_file_io_large_ranked.svg)

</details>

<details>
<summary><strong>gui_calculator</strong> — Implementing a simple GUI application (a calculator)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![gui_calculator ranked score chart](docs/plots/version_task_gui_calculator_ranked.svg)

![gui_calculator canonical score chart](docs/plots/version_task_gui_calculator.svg)

![gui_calculator best-case ranked score chart](docs/plots/version_best_case_task_gui_calculator_ranked.svg)

![gui_calculator best-case canonical score chart](docs/plots/version_best_case_task_gui_calculator.svg)

![gui_calculator baseline delta ranked chart](docs/plots/version_task_baseline_gui_calculator_ranked.svg)

</details>

<details>
<summary><strong>image_resizing</strong> — Implementing a basic image processing task (resizing an image)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![image_resizing ranked score chart](docs/plots/version_task_image_resizing_ranked.svg)

![image_resizing canonical score chart](docs/plots/version_task_image_resizing.svg)

![image_resizing best-case ranked score chart](docs/plots/version_best_case_task_image_resizing_ranked.svg)

![image_resizing best-case canonical score chart](docs/plots/version_best_case_task_image_resizing.svg)

![image_resizing baseline delta ranked chart](docs/plots/version_task_baseline_image_resizing_ranked.svg)

</details>

<details>
<summary><strong>linear_regression</strong> — Implementing a basic machine learning algorithm (linear regression)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![linear_regression ranked score chart](docs/plots/version_task_linear_regression_ranked.svg)

![linear_regression canonical score chart](docs/plots/version_task_linear_regression.svg)

![linear_regression best-case ranked score chart](docs/plots/version_best_case_task_linear_regression_ranked.svg)

![linear_regression best-case canonical score chart](docs/plots/version_best_case_task_linear_regression.svg)

![linear_regression baseline delta ranked chart](docs/plots/version_task_baseline_linear_regression_ranked.svg)

</details>

<details>
<summary><strong>matrix_multiplication</strong> — Performing matrix multiplication</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![matrix_multiplication ranked score chart](docs/plots/version_task_matrix_multiplication_ranked.svg)

![matrix_multiplication canonical score chart](docs/plots/version_task_matrix_multiplication.svg)

![matrix_multiplication best-case ranked score chart](docs/plots/version_best_case_task_matrix_multiplication_ranked.svg)

![matrix_multiplication best-case canonical score chart](docs/plots/version_best_case_task_matrix_multiplication.svg)

![matrix_multiplication baseline delta ranked chart](docs/plots/version_task_baseline_matrix_multiplication_ranked.svg)

</details>

<details>
<summary><strong>prime_sieve</strong> — Implementing a simple algorithm (prime number generation)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![prime_sieve ranked score chart](docs/plots/version_task_prime_sieve_ranked.svg)

![prime_sieve canonical score chart](docs/plots/version_task_prime_sieve.svg)

![prime_sieve best-case ranked score chart](docs/plots/version_best_case_task_prime_sieve_ranked.svg)

![prime_sieve best-case canonical score chart](docs/plots/version_best_case_task_prime_sieve.svg)

![prime_sieve baseline delta ranked chart](docs/plots/version_task_baseline_prime_sieve_ranked.svg)

</details>

<details>
<summary><strong>producer_consumer</strong> — Implementing a simple multithreading task (producer-consumer problem)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![producer_consumer ranked score chart](docs/plots/version_task_producer_consumer_ranked.svg)

![producer_consumer canonical score chart](docs/plots/version_task_producer_consumer.svg)

![producer_consumer best-case ranked score chart](docs/plots/version_best_case_task_producer_consumer_ranked.svg)

![producer_consumer best-case canonical score chart](docs/plots/version_best_case_task_producer_consumer.svg)

![producer_consumer baseline delta ranked chart](docs/plots/version_task_baseline_producer_consumer_ranked.svg)

</details>

<details>
<summary><strong>rest_api</strong> — Implementing a simple REST API</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![rest_api ranked score chart](docs/plots/version_task_rest_api_ranked.svg)

![rest_api canonical score chart](docs/plots/version_task_rest_api.svg)

![rest_api best-case ranked score chart](docs/plots/version_best_case_task_rest_api_ranked.svg)

![rest_api best-case canonical score chart](docs/plots/version_best_case_task_rest_api.svg)

![rest_api baseline delta ranked chart](docs/plots/version_task_baseline_rest_api_ranked.svg)

</details>

<details>
<summary><strong>sentiment_analysis</strong> — Implementing a simple natural language processing task (sentiment analysis)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![sentiment_analysis ranked score chart](docs/plots/version_task_sentiment_analysis_ranked.svg)

![sentiment_analysis canonical score chart](docs/plots/version_task_sentiment_analysis.svg)

![sentiment_analysis best-case ranked score chart](docs/plots/version_best_case_task_sentiment_analysis_ranked.svg)

![sentiment_analysis best-case canonical score chart](docs/plots/version_best_case_task_sentiment_analysis.svg)

![sentiment_analysis baseline delta ranked chart](docs/plots/version_task_baseline_sentiment_analysis_ranked.svg)

</details>

<details>
<summary><strong>simple_web_server</strong> — Implementing a simple web server</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![simple_web_server ranked score chart](docs/plots/version_task_simple_web_server_ranked.svg)

![simple_web_server canonical score chart](docs/plots/version_task_simple_web_server.svg)

![simple_web_server best-case ranked score chart](docs/plots/version_best_case_task_simple_web_server_ranked.svg)

![simple_web_server best-case canonical score chart](docs/plots/version_best_case_task_simple_web_server.svg)

![simple_web_server baseline delta ranked chart](docs/plots/version_task_baseline_simple_web_server_ranked.svg)

</details>

<details>
<summary><strong>socket_programming</strong> — Implementing a basic networking task (socket programming)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![socket_programming ranked score chart](docs/plots/version_task_socket_programming_ranked.svg)

![socket_programming canonical score chart](docs/plots/version_task_socket_programming.svg)

![socket_programming best-case ranked score chart](docs/plots/version_best_case_task_socket_programming_ranked.svg)

![socket_programming best-case canonical score chart](docs/plots/version_best_case_task_socket_programming.svg)

![socket_programming baseline delta ranked chart](docs/plots/version_task_baseline_socket_programming_ranked.svg)

</details>

<details>
<summary><strong>sort_integers</strong> — Sorting a large array of integers</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![sort_integers ranked score chart](docs/plots/version_task_sort_integers_ranked.svg)

![sort_integers canonical score chart](docs/plots/version_task_sort_integers.svg)

![sort_integers best-case ranked score chart](docs/plots/version_best_case_task_sort_integers_ranked.svg)

![sort_integers best-case canonical score chart](docs/plots/version_best_case_task_sort_integers.svg)

![sort_integers baseline delta ranked chart](docs/plots/version_task_baseline_sort_integers_ranked.svg)

</details>

<details>
<summary><strong>sqlite_crud</strong> — Implementing a basic database interaction (CRUD operations)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![sqlite_crud ranked score chart](docs/plots/version_task_sqlite_crud_ranked.svg)

![sqlite_crud canonical score chart](docs/plots/version_task_sqlite_crud.svg)

![sqlite_crud best-case ranked score chart](docs/plots/version_best_case_task_sqlite_crud_ranked.svg)

![sqlite_crud best-case canonical score chart](docs/plots/version_best_case_task_sqlite_crud.svg)

![sqlite_crud baseline delta ranked chart](docs/plots/version_task_baseline_sqlite_crud_ranked.svg)

</details>

<details>
<summary><strong>third_party_api</strong> — Integrating with a third-party API (e.g., Twitter API)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![third_party_api ranked score chart](docs/plots/version_task_third_party_api_ranked.svg)

![third_party_api canonical score chart](docs/plots/version_task_third_party_api.svg)

![third_party_api best-case ranked score chart](docs/plots/version_best_case_task_third_party_api_ranked.svg)

![third_party_api best-case canonical score chart](docs/plots/version_best_case_task_third_party_api.svg)

![third_party_api baseline delta ranked chart](docs/plots/version_task_baseline_third_party_api_ranked.svg)

</details>

<details>
<summary><strong>tic_tac_toe</strong> — Implementing a basic game (tic-tac-toe)</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![tic_tac_toe ranked score chart](docs/plots/version_task_tic_tac_toe_ranked.svg)

![tic_tac_toe canonical score chart](docs/plots/version_task_tic_tac_toe.svg)

![tic_tac_toe best-case ranked score chart](docs/plots/version_best_case_task_tic_tac_toe_ranked.svg)

![tic_tac_toe best-case canonical score chart](docs/plots/version_best_case_task_tic_tac_toe.svg)

![tic_tac_toe baseline delta ranked chart](docs/plots/version_task_baseline_tic_tac_toe_ranked.svg)

</details>

<details>
<summary><strong>web_scraper</strong> — Implementing a simple web scraper</summary>

Per-version ranked plot first, then per-version canonical order, then language best-case ranked, then language best-case canonical order, then per-task delta against the configured baseline runtime:

![web_scraper ranked score chart](docs/plots/version_task_web_scraper_ranked.svg)

![web_scraper canonical score chart](docs/plots/version_task_web_scraper.svg)

![web_scraper best-case ranked score chart](docs/plots/version_best_case_task_web_scraper_ranked.svg)

![web_scraper best-case canonical score chart](docs/plots/version_best_case_task_web_scraper.svg)

![web_scraper baseline delta ranked chart](docs/plots/version_task_baseline_web_scraper_ranked.svg)

</details>


### Per-task raw numeric tables

Each task also includes the measured medians, standard deviation, and min→max range for CPU time, wall time, and memory.
These per-task tables use the supplemental version-matrix medians when they are available, so runtime variants such as multiple Python, PHP, or JavaScript runtimes are listed individually instead of being collapsed to one primary runtime per family.

<details>
<summary><strong>ai_service_integration</strong> — Integrating with AI services (e.g., OpenAI API or MCP services)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 20.938 MB | 0.000 MB | 0.000 MB | 20.938 MB → 20.938 MB | 10 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 21.086 MB | 0.000 MB | 0.000 MB | 21.086 MB → 21.086 MB | 10 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 13.846 ms | 0.000 ms | 0.000 ms | 13.846 ms → 13.846 ms | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 20.832 MB | 0.000 MB | 0.000 MB | 20.832 MB → 20.832 MB | 10 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 22.969 MB | 0.000 MB | 0.000 MB | 22.969 MB → 22.969 MB | 9 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 22.988 MB | 0.000 MB | 0.000 MB | 22.988 MB → 22.988 MB | 9 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 22.973 MB | 0.000 MB | 0.000 MB | 22.973 MB → 22.973 MB | 9 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 24.113 MB | 0.000 MB | 0.000 MB | 24.113 MB → 24.113 MB | 9 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 24.164 MB | 0.000 MB | 0.000 MB | 24.164 MB → 24.164 MB | 9 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 24.113 MB | 0.000 MB | 0.000 MB | 24.113 MB → 24.113 MB | 9 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 25.648 MB | 0.000 MB | 0.000 MB | 25.648 MB → 25.648 MB | 9 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 25.641 MB | 0.000 MB | 0.000 MB | 25.641 MB → 25.641 MB | 9 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 25.590 MB | 0.000 MB | 0.000 MB | 25.590 MB → 25.590 MB | 9 |
| Python 2.7 [x86_64] | Python | S | 1 | 12.857 ms | 0.000 ms | 0.000 ms | 12.857 ms → 12.857 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 7.742 MB | 0.000 MB | 0.000 MB | 7.742 MB → 7.742 MB | 9 |
| Python 2.7 [x86_64] | Python | M | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 16.000 ms | 0.000 ms | 0.000 ms | 16.000 ms → 16.000 ms | 7.859 MB | 0.000 MB | 0.000 MB | 7.859 MB → 7.859 MB | 9 |
| Python 2.7 [x86_64] | Python | L | 1 | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 8.078 MB | 0.000 MB | 0.000 MB | 8.078 MB → 8.078 MB | 9 |
| Python 3.8 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 10.918 MB | 0.000 MB | 0.000 MB | 10.918 MB → 10.918 MB | 9 |
| Python 3.8 [x86_64] | Python | M | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 10.844 MB | 0.000 MB | 0.000 MB | 10.844 MB → 10.844 MB | 9 |
| Python 3.8 [x86_64] | Python | L | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 11.008 MB | 0.000 MB | 0.000 MB | 11.008 MB → 11.008 MB | 9 |
| Python 3.11 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 13.594 MB | 0.000 MB | 0.000 MB | 13.594 MB → 13.594 MB | 9 |
| Python 3.11 [x86_64] | Python | M | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 13.449 MB | 0.000 MB | 0.000 MB | 13.449 MB → 13.449 MB | 9 |
| Python 3.11 [x86_64] | Python | L | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.625 MB | 0.000 MB | 0.000 MB | 13.625 MB → 13.625 MB | 9 |
| Python 3.12 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 14.922 MB | 0.000 MB | 0.000 MB | 14.922 MB → 14.922 MB | 9 |
| Python 3.12 [x86_64] | Python | M | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.922 MB | 0.000 MB | 0.000 MB | 14.922 MB → 14.922 MB | 9 |
| Python 3.12 [x86_64] | Python | L | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.965 MB | 0.000 MB | 0.000 MB | 14.965 MB → 14.965 MB | 9 |
| Java 21 [x86_64] | Java | S | 1 | 130.000 ms | 0.000 ms | 0.000 ms | 130.000 ms → 130.000 ms | 113.333 ms | 0.000 ms | 0.000 ms | 113.333 ms → 113.333 ms | 45.070 MB | 0.000 MB | 0.000 MB | 45.070 MB → 45.070 MB | 13 |
| Java 21 [x86_64] | Java | M | 1 | 143.333 ms | 0.000 ms | 0.000 ms | 143.333 ms → 143.333 ms | 143.333 ms | 0.000 ms | 0.000 ms | 143.333 ms → 143.333 ms | 45.125 MB | 0.000 MB | 0.000 MB | 45.125 MB → 45.125 MB | 13 |
| Java 21 [x86_64] | Java | L | 1 | 166.667 ms | 0.000 ms | 0.000 ms | 166.667 ms → 166.667 ms | 160.000 ms | 0.000 ms | 0.000 ms | 160.000 ms → 160.000 ms | 45.172 MB | 0.000 MB | 0.000 MB | 45.172 MB → 45.172 MB | 13 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 2.040 ms | 0.000 ms | 0.000 ms | 2.040 ms → 2.040 ms | 2.120 ms | 0.000 ms | 0.000 ms | 2.120 ms → 2.120 ms | 3.883 MB | 0.000 MB | 0.000 MB | 3.883 MB → 3.883 MB | 20 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 2.520 ms | 0.000 ms | 0.000 ms | 2.520 ms → 2.520 ms | 2.560 ms | 0.000 ms | 0.000 ms | 2.560 ms → 2.560 ms | 4.008 MB | 0.000 MB | 0.000 MB | 4.008 MB → 4.008 MB | 20 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 3.560 ms | 0.000 ms | 0.000 ms | 3.560 ms → 3.560 ms | 3.640 ms | 0.000 ms | 0.000 ms | 3.640 ms → 3.640 ms | 3.973 MB | 0.000 MB | 0.000 MB | 3.973 MB → 3.973 MB | 20 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 46.098 MB | 0.000 MB | 0.000 MB | 46.098 MB → 46.098 MB | 10 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 46.223 MB | 0.000 MB | 0.000 MB | 46.223 MB → 46.223 MB | 10 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 46.348 MB | 0.000 MB | 0.000 MB | 46.348 MB → 46.348 MB | 10 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 45.556 ms | 0.000 ms | 0.000 ms | 45.556 ms → 45.556 ms | 45.556 ms | 0.000 ms | 0.000 ms | 45.556 ms → 45.556 ms | 43.438 MB | 0.000 MB | 0.000 MB | 43.438 MB → 43.438 MB | 10 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 38.000 ms | 0.000 ms | 0.000 ms | 38.000 ms → 38.000 ms | 38.000 ms | 0.000 ms | 0.000 ms | 38.000 ms → 38.000 ms | 43.547 MB | 0.000 MB | 0.000 MB | 43.547 MB → 43.547 MB | 10 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 43.922 MB | 0.000 MB | 0.000 MB | 43.922 MB → 43.922 MB | 10 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 69.348 MB | 0.000 MB | 0.000 MB | 69.348 MB → 69.348 MB | 10 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 69.480 MB | 0.000 MB | 0.000 MB | 69.480 MB → 69.480 MB | 10 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 69.582 MB | 0.000 MB | 0.000 MB | 69.582 MB → 69.582 MB | 10 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.840 ms | 0.000 ms | 0.000 ms | 2.840 ms → 2.840 ms | 2.880 ms | 0.000 ms | 0.000 ms | 2.880 ms → 2.880 ms | 7.676 MB | 0.000 MB | 0.000 MB | 7.676 MB → 7.676 MB | 19 |
| Go 1.23 [x86_64] | Go | M | 1 | 3.960 ms | 0.000 ms | 0.000 ms | 3.960 ms → 3.960 ms | 4.000 ms | 0.000 ms | 0.000 ms | 4.000 ms → 4.000 ms | 9.469 MB | 0.000 MB | 0.000 MB | 9.469 MB → 9.469 MB | 19 |
| Go 1.23 [x86_64] | Go | L | 1 | 5.800 ms | 0.000 ms | 0.000 ms | 5.800 ms → 5.800 ms | 5.800 ms | 0.000 ms | 0.000 ms | 5.800 ms → 5.800 ms | 9.680 MB | 0.000 MB | 0.000 MB | 9.680 MB → 9.680 MB | 19 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.320 ms | 0.000 ms | 0.000 ms | 1.320 ms → 1.320 ms | 1.360 ms | 0.000 ms | 0.000 ms | 1.360 ms → 1.360 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 31 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 1.520 ms | 0.000 ms | 0.000 ms | 1.520 ms → 1.520 ms | 1.560 ms | 0.000 ms | 0.000 ms | 1.560 ms → 1.560 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 31 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 1.640 ms | 0.000 ms | 0.000 ms | 1.640 ms → 1.640 ms | 1.720 ms | 0.000 ms | 0.000 ms | 1.720 ms → 1.720 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 31 |

</details>

<details>
<summary><strong>api_client</strong> — Implementing a simple API client (fetching data from a public API)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 21.062 MB | 0.000 MB | 0.000 MB | 21.062 MB → 21.062 MB | 9 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 20.910 MB | 0.000 MB | 0.000 MB | 20.910 MB → 20.910 MB | 9 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 21.086 MB | 0.000 MB | 0.000 MB | 21.086 MB → 21.086 MB | 9 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 22.969 MB | 0.000 MB | 0.000 MB | 22.969 MB → 22.969 MB | 8 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 22.957 MB | 0.000 MB | 0.000 MB | 22.957 MB → 22.957 MB | 8 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 22.977 MB | 0.000 MB | 0.000 MB | 22.977 MB → 22.977 MB | 8 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 24.152 MB | 0.000 MB | 0.000 MB | 24.152 MB → 24.152 MB | 8 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 24.172 MB | 0.000 MB | 0.000 MB | 24.172 MB → 24.172 MB | 8 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 24.191 MB | 0.000 MB | 0.000 MB | 24.191 MB → 24.191 MB | 8 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 25.617 MB | 0.000 MB | 0.000 MB | 25.617 MB → 25.617 MB | 8 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 25.641 MB | 0.000 MB | 0.000 MB | 25.641 MB → 25.641 MB | 8 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 25.605 MB | 0.000 MB | 0.000 MB | 25.605 MB → 25.605 MB | 8 |
| Python 2.7 [x86_64] | Python | S | 1 | 12.857 ms | 0.000 ms | 0.000 ms | 12.857 ms → 12.857 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 7.801 MB | 0.000 MB | 0.000 MB | 7.801 MB → 7.801 MB | 8 |
| Python 2.7 [x86_64] | Python | M | 1 | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 7.832 MB | 0.000 MB | 0.000 MB | 7.832 MB → 7.832 MB | 8 |
| Python 2.7 [x86_64] | Python | L | 1 | 15.714 ms | 0.000 ms | 0.000 ms | 15.714 ms → 15.714 ms | 15.714 ms | 0.000 ms | 0.000 ms | 15.714 ms → 15.714 ms | 7.836 MB | 0.000 MB | 0.000 MB | 7.836 MB → 7.836 MB | 8 |
| Python 3.8 [x86_64] | Python | S | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 10.766 MB | 0.000 MB | 0.000 MB | 10.766 MB → 10.766 MB | 8 |
| Python 3.8 [x86_64] | Python | M | 1 | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 10.832 MB | 0.000 MB | 0.000 MB | 10.832 MB → 10.832 MB | 8 |
| Python 3.8 [x86_64] | Python | L | 1 | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 10.812 MB | 0.000 MB | 0.000 MB | 10.812 MB → 10.812 MB | 8 |
| Python 3.11 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 13.586 MB | 0.000 MB | 0.000 MB | 13.586 MB → 13.586 MB | 8 |
| Python 3.11 [x86_64] | Python | M | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 13.348 MB | 0.000 MB | 0.000 MB | 13.348 MB → 13.348 MB | 8 |
| Python 3.11 [x86_64] | Python | L | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.609 MB | 0.000 MB | 0.000 MB | 13.609 MB → 13.609 MB | 8 |
| Python 3.12 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 14.766 MB | 0.000 MB | 0.000 MB | 14.766 MB → 14.766 MB | 8 |
| Python 3.12 [x86_64] | Python | M | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 14.902 MB | 0.000 MB | 0.000 MB | 14.902 MB → 14.902 MB | 8 |
| Python 3.12 [x86_64] | Python | L | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.902 MB | 0.000 MB | 0.000 MB | 14.902 MB → 14.902 MB | 8 |
| Java 21 [x86_64] | Java | S | 1 | 136.667 ms | 0.000 ms | 0.000 ms | 136.667 ms → 136.667 ms | 130.000 ms | 0.000 ms | 0.000 ms | 130.000 ms → 130.000 ms | 44.922 MB | 0.000 MB | 0.000 MB | 44.922 MB → 44.922 MB | 11 |
| Java 21 [x86_64] | Java | M | 1 | 143.333 ms | 0.000 ms | 0.000 ms | 143.333 ms → 143.333 ms | 133.333 ms | 0.000 ms | 0.000 ms | 133.333 ms → 133.333 ms | 45.156 MB | 0.000 MB | 0.000 MB | 45.156 MB → 45.156 MB | 11 |
| Java 21 [x86_64] | Java | L | 1 | 180.000 ms | 0.000 ms | 0.000 ms | 180.000 ms → 180.000 ms | 176.667 ms | 0.000 ms | 0.000 ms | 176.667 ms → 176.667 ms | 44.836 MB | 0.000 MB | 0.000 MB | 44.836 MB → 44.836 MB | 11 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 1.920 ms | 0.000 ms | 0.000 ms | 1.920 ms → 1.920 ms | 1.960 ms | 0.000 ms | 0.000 ms | 1.960 ms → 1.960 ms | 3.848 MB | 0.000 MB | 0.000 MB | 3.848 MB → 3.848 MB | 18 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 2.480 ms | 0.000 ms | 0.000 ms | 2.480 ms → 2.480 ms | 2.560 ms | 0.000 ms | 0.000 ms | 2.560 ms → 2.560 ms | 3.977 MB | 0.000 MB | 0.000 MB | 3.977 MB → 3.977 MB | 18 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 3.160 ms | 0.000 ms | 0.000 ms | 3.160 ms → 3.160 ms | 3.240 ms | 0.000 ms | 0.000 ms | 3.240 ms → 3.240 ms | 3.973 MB | 0.000 MB | 0.000 MB | 3.973 MB → 3.973 MB | 18 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 46.047 MB | 0.000 MB | 0.000 MB | 46.047 MB → 46.047 MB | 9 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 37.778 ms | 0.000 ms | 0.000 ms | 37.778 ms → 37.778 ms | 38.889 ms | 0.000 ms | 0.000 ms | 38.889 ms → 38.889 ms | 46.223 MB | 0.000 MB | 0.000 MB | 46.223 MB → 46.223 MB | 9 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 46.367 MB | 0.000 MB | 0.000 MB | 46.367 MB → 46.367 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 36.667 ms | 0.000 ms | 0.000 ms | 36.667 ms → 36.667 ms | 36.667 ms | 0.000 ms | 0.000 ms | 36.667 ms → 36.667 ms | 43.469 MB | 0.000 MB | 0.000 MB | 43.469 MB → 43.469 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 34.286 ms | 0.000 ms | 0.000 ms | 34.286 ms → 34.286 ms | 43.629 MB | 0.000 MB | 0.000 MB | 43.629 MB → 43.629 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 44.172 MB | 0.000 MB | 0.000 MB | 44.172 MB → 44.172 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 69.414 MB | 0.000 MB | 0.000 MB | 69.414 MB → 69.414 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 69.422 MB | 0.000 MB | 0.000 MB | 69.422 MB → 69.422 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 69.434 MB | 0.000 MB | 0.000 MB | 69.434 MB → 69.434 MB | 9 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.840 ms | 0.000 ms | 0.000 ms | 2.840 ms → 2.840 ms | 2.880 ms | 0.000 ms | 0.000 ms | 2.880 ms → 2.880 ms | 7.676 MB | 0.000 MB | 0.000 MB | 7.676 MB → 7.676 MB | 19 |
| Go 1.23 [x86_64] | Go | M | 1 | 4.040 ms | 0.000 ms | 0.000 ms | 4.040 ms → 4.040 ms | 4.040 ms | 0.000 ms | 0.000 ms | 4.040 ms → 4.040 ms | 9.688 MB | 0.000 MB | 0.000 MB | 9.688 MB → 9.688 MB | 19 |
| Go 1.23 [x86_64] | Go | L | 1 | 5.200 ms | 0.000 ms | 0.000 ms | 5.200 ms → 5.200 ms | 5.240 ms | 0.000 ms | 0.000 ms | 5.240 ms → 5.240 ms | 9.695 MB | 0.000 MB | 0.000 MB | 9.695 MB → 9.695 MB | 19 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.320 ms | 0.000 ms | 0.000 ms | 1.320 ms → 1.320 ms | 1.360 ms | 0.000 ms | 0.000 ms | 1.360 ms → 1.360 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 31 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 1.480 ms | 0.000 ms | 0.000 ms | 1.480 ms → 1.480 ms | 1.520 ms | 0.000 ms | 0.000 ms | 1.520 ms → 1.520 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 31 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 1.720 ms | 0.000 ms | 0.000 ms | 1.720 ms → 1.720 ms | 1.760 ms | 0.000 ms | 0.000 ms | 1.760 ms → 1.760 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 31 |

</details>

<details>
<summary><strong>basic_blockchain</strong> — Implementing a basic blockchain</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 21.074 MB | 0.000 MB | 0.000 MB | 21.074 MB → 21.074 MB | 18 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 21.070 MB | 0.000 MB | 0.000 MB | 21.070 MB → 21.070 MB | 18 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 22.359 MB | 0.000 MB | 0.000 MB | 22.359 MB → 22.359 MB | 18 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 22.973 MB | 0.000 MB | 0.000 MB | 22.973 MB → 22.973 MB | 17 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 23.027 MB | 0.000 MB | 0.000 MB | 23.027 MB → 23.027 MB | 17 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 19.231 ms | 0.000 ms | 0.000 ms | 19.231 ms → 19.231 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 25.016 MB | 0.000 MB | 0.000 MB | 25.016 MB → 25.016 MB | 17 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 24.152 MB | 0.000 MB | 0.000 MB | 24.152 MB → 24.152 MB | 17 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 19.231 ms | 0.000 ms | 0.000 ms | 19.231 ms → 19.231 ms | 24.160 MB | 0.000 MB | 0.000 MB | 24.160 MB → 24.160 MB | 17 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 23.077 ms | 0.000 ms | 0.000 ms | 23.077 ms → 23.077 ms | 23.846 ms | 0.000 ms | 0.000 ms | 23.846 ms → 23.846 ms | 26.184 MB | 0.000 MB | 0.000 MB | 26.184 MB → 26.184 MB | 17 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 25.520 MB | 0.000 MB | 0.000 MB | 25.520 MB → 25.520 MB | 17 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 25.535 MB | 0.000 MB | 0.000 MB | 25.535 MB → 25.535 MB | 17 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 25.527 MB | 0.000 MB | 0.000 MB | 25.527 MB → 25.527 MB | 17 |
| Python 2.7 [x86_64] | Python | S | 1 | 17.500 ms | 0.000 ms | 0.000 ms | 17.500 ms → 17.500 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 7.840 MB | 0.000 MB | 0.000 MB | 7.840 MB → 7.840 MB | 16 |
| Python 2.7 [x86_64] | Python | M | 1 | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 32.000 ms | 0.000 ms | 0.000 ms | 32.000 ms → 32.000 ms | 8.934 MB | 0.000 MB | 0.000 MB | 8.934 MB → 8.934 MB | 16 |
| Python 2.7 [x86_64] | Python | L | 1 | 47.500 ms | 0.000 ms | 0.000 ms | 47.500 ms → 47.500 ms | 47.500 ms | 0.000 ms | 0.000 ms | 47.500 ms → 47.500 ms | 10.500 MB | 0.000 MB | 0.000 MB | 10.500 MB → 10.500 MB | 16 |
| Python 3.8 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 11.051 MB | 0.000 MB | 0.000 MB | 11.051 MB → 11.051 MB | 16 |
| Python 3.8 [x86_64] | Python | M | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 11.148 MB | 0.000 MB | 0.000 MB | 11.148 MB → 11.148 MB | 16 |
| Python 3.8 [x86_64] | Python | L | 1 | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 11.320 MB | 0.000 MB | 0.000 MB | 11.320 MB → 11.320 MB | 16 |
| Python 3.11 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.809 MB | 0.000 MB | 0.000 MB | 13.809 MB → 13.809 MB | 16 |
| Python 3.11 [x86_64] | Python | M | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 13.547 MB | 0.000 MB | 0.000 MB | 13.547 MB → 13.547 MB | 16 |
| Python 3.11 [x86_64] | Python | L | 1 | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 14.270 MB | 0.000 MB | 0.000 MB | 14.270 MB → 14.270 MB | 16 |
| Python 3.12 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.812 MB | 0.000 MB | 0.000 MB | 14.812 MB → 14.812 MB | 16 |
| Python 3.12 [x86_64] | Python | M | 1 | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 14.766 MB | 0.000 MB | 0.000 MB | 14.766 MB → 14.766 MB | 16 |
| Python 3.12 [x86_64] | Python | L | 1 | 95.000 ms | 0.000 ms | 0.000 ms | 95.000 ms → 95.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 15.188 MB | 0.000 MB | 0.000 MB | 15.188 MB → 15.188 MB | 16 |
| Java 21 [x86_64] | Java | S | 1 | 215.000 ms | 0.000 ms | 0.000 ms | 215.000 ms → 215.000 ms | 220.000 ms | 0.000 ms | 0.000 ms | 220.000 ms → 220.000 ms | 48.586 MB | 0.000 MB | 0.000 MB | 48.586 MB → 48.586 MB | 22 |
| Java 21 [x86_64] | Java | M | 1 | 270.000 ms | 0.000 ms | 0.000 ms | 270.000 ms → 270.000 ms | 230.000 ms | 0.000 ms | 0.000 ms | 230.000 ms → 230.000 ms | 49.695 MB | 0.000 MB | 0.000 MB | 49.695 MB → 49.695 MB | 22 |
| Java 21 [x86_64] | Java | L | 1 | 390.000 ms | 0.000 ms | 0.000 ms | 390.000 ms → 390.000 ms | 340.000 ms | 0.000 ms | 0.000 ms | 340.000 ms → 340.000 ms | 49.668 MB | 0.000 MB | 0.000 MB | 49.668 MB → 49.668 MB | 22 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 2.080 ms | 0.000 ms | 0.000 ms | 2.080 ms → 2.080 ms | 2.120 ms | 0.000 ms | 0.000 ms | 2.120 ms → 2.120 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 25 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 4.000 ms | 0.000 ms | 0.000 ms | 4.000 ms → 4.000 ms | 4.080 ms | 0.000 ms | 0.000 ms | 4.080 ms → 4.080 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 25 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 6.280 ms | 0.000 ms | 0.000 ms | 6.280 ms → 6.280 ms | 6.360 ms | 0.000 ms | 0.000 ms | 6.360 ms → 6.360 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 25 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 47.250 MB | 0.000 MB | 0.000 MB | 47.250 MB → 47.250 MB | 17 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 56.004 MB | 0.000 MB | 0.000 MB | 56.004 MB → 56.004 MB | 17 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 56.621 MB | 0.000 MB | 0.000 MB | 56.621 MB → 56.621 MB | 17 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 42.857 ms | 0.000 ms | 0.000 ms | 42.857 ms → 42.857 ms | 42.857 ms | 0.000 ms | 0.000 ms | 42.857 ms → 42.857 ms | 46.855 MB | 0.000 MB | 0.000 MB | 46.855 MB → 46.855 MB | 17 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 53.395 MB | 0.000 MB | 0.000 MB | 53.395 MB → 53.395 MB | 17 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 64.309 MB | 0.000 MB | 0.000 MB | 64.309 MB → 64.309 MB | 17 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 74.828 MB | 0.000 MB | 0.000 MB | 74.828 MB → 74.828 MB | 17 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 77.496 MB | 0.000 MB | 0.000 MB | 77.496 MB → 77.496 MB | 17 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 72.500 ms | 0.000 ms | 0.000 ms | 72.500 ms → 72.500 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 79.516 MB | 0.000 MB | 0.000 MB | 79.516 MB → 79.516 MB | 17 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.760 ms | 0.000 ms | 0.000 ms | 2.760 ms → 2.760 ms | 2.800 ms | 0.000 ms | 0.000 ms | 2.800 ms → 2.800 ms | 7.547 MB | 0.000 MB | 0.000 MB | 7.547 MB → 7.547 MB | 32 |
| Go 1.23 [x86_64] | Go | M | 1 | 4.240 ms | 0.000 ms | 0.000 ms | 4.240 ms → 4.240 ms | 4.320 ms | 0.000 ms | 0.000 ms | 4.320 ms → 4.320 ms | 9.613 MB | 0.000 MB | 0.000 MB | 9.613 MB → 9.613 MB | 32 |
| Go 1.23 [x86_64] | Go | L | 1 | 5.840 ms | 0.000 ms | 0.000 ms | 5.840 ms → 5.840 ms | 5.880 ms | 0.000 ms | 0.000 ms | 5.880 ms → 5.880 ms | 9.582 MB | 0.000 MB | 0.000 MB | 9.582 MB → 9.582 MB | 32 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.440 ms | 0.000 ms | 0.000 ms | 1.440 ms → 1.440 ms | 1.480 ms | 0.000 ms | 0.000 ms | 1.480 ms → 1.480 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 19 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 2.040 ms | 0.000 ms | 0.000 ms | 2.040 ms → 2.040 ms | 2.080 ms | 0.000 ms | 0.000 ms | 2.080 ms → 2.080 ms | 3.051 MB | 0.000 MB | 0.000 MB | 3.051 MB → 3.051 MB | 19 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 2.920 ms | 0.000 ms | 0.000 ms | 2.920 ms → 2.920 ms | 2.960 ms | 0.000 ms | 0.000 ms | 2.960 ms → 2.960 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 19 |

</details>

<details>
<summary><strong>basic_web_application</strong> — Implementing a basic web application (a to-do list)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 27.454 ms | 0.000 ms | 0.000 ms | 27.454 ms → 27.454 ms | 959.483 ms | 0.000 ms | 0.000 ms | 959.483 ms → 959.483 ms | 14.230 MB | 0.000 MB | 0.000 MB | 14.230 MB → 14.230 MB | 5 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 27.591 ms | 0.000 ms | 0.000 ms | 27.591 ms → 27.591 ms | 1.1103 s | 0.000 ms | 0.000 ms | 1.1103 s → 1.1103 s | 13.914 MB | 0.000 MB | 0.000 MB | 13.914 MB → 13.914 MB | 5 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 26.888 ms | 0.000 ms | 0.000 ms | 26.888 ms → 26.888 ms | 1.0632 s | 0.000 ms | 0.000 ms | 1.0632 s → 1.0632 s | 15.645 MB | 0.000 MB | 0.000 MB | 15.645 MB → 15.645 MB | 5 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 27.236 ms | 0.000 ms | 0.000 ms | 27.236 ms → 27.236 ms | 1.0166 s | 0.000 ms | 0.000 ms | 1.0166 s → 1.0166 s | 15.773 MB | 0.000 MB | 0.000 MB | 15.773 MB → 15.773 MB | 5 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 26.974 ms | 0.000 ms | 0.000 ms | 26.974 ms → 26.974 ms | 1.0004 s | 0.000 ms | 0.000 ms | 1.0004 s → 1.0004 s | 15.453 MB | 0.000 MB | 0.000 MB | 15.453 MB → 15.453 MB | 5 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 26.962 ms | 0.000 ms | 0.000 ms | 26.962 ms → 26.962 ms | 979.091 ms | 0.000 ms | 0.000 ms | 979.091 ms → 979.091 ms | 15.461 MB | 0.000 MB | 0.000 MB | 15.461 MB → 15.461 MB | 5 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 27.111 ms | 0.000 ms | 0.000 ms | 27.111 ms → 27.111 ms | 1.0978 s | 0.000 ms | 0.000 ms | 1.0978 s → 1.0978 s | 17.281 MB | 0.000 MB | 0.000 MB | 17.281 MB → 17.281 MB | 5 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 29.384 ms | 0.000 ms | 0.000 ms | 29.384 ms → 29.384 ms | 1.1195 s | 0.000 ms | 0.000 ms | 1.1195 s → 1.1195 s | 15.367 MB | 0.000 MB | 0.000 MB | 15.367 MB → 15.367 MB | 5 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 27.088 ms | 0.000 ms | 0.000 ms | 27.088 ms → 27.088 ms | 1.0666 s | 0.000 ms | 0.000 ms | 1.0666 s → 1.0666 s | 16.059 MB | 0.000 MB | 0.000 MB | 16.059 MB → 16.059 MB | 5 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 28.019 ms | 0.000 ms | 0.000 ms | 28.019 ms → 28.019 ms | 1.1138 s | 0.000 ms | 0.000 ms | 1.1138 s → 1.1138 s | 16.832 MB | 0.000 MB | 0.000 MB | 16.832 MB → 16.832 MB | 5 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 1.1178 s | 0.000 ms | 0.000 ms | 1.1178 s → 1.1178 s | 16.922 MB | 0.000 MB | 0.000 MB | 16.922 MB → 16.922 MB | 5 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 28.615 ms | 0.000 ms | 0.000 ms | 28.615 ms → 28.615 ms | 1.1445 s | 0.000 ms | 0.000 ms | 1.1445 s → 1.1445 s | 16.398 MB | 0.000 MB | 0.000 MB | 16.398 MB → 16.398 MB | 5 |
| Python 2.7 [x86_64] | Python | S | 1 | 28.701 ms | 0.000 ms | 0.000 ms | 28.701 ms → 28.701 ms | 1.1879 s | 0.000 ms | 0.000 ms | 1.1879 s → 1.1879 s | 17.137 MB | 0.000 MB | 0.000 MB | 17.137 MB → 17.137 MB | 3 |
| Python 2.7 [x86_64] | Python | M | 1 | 27.686 ms | 0.000 ms | 0.000 ms | 27.686 ms → 27.686 ms | 1.1145 s | 0.000 ms | 0.000 ms | 1.1145 s → 1.1145 s | 19.234 MB | 0.000 MB | 0.000 MB | 19.234 MB → 19.234 MB | 3 |
| Python 2.7 [x86_64] | Python | L | 1 | 28.048 ms | 0.000 ms | 0.000 ms | 28.048 ms → 28.048 ms | 1.0795 s | 0.000 ms | 0.000 ms | 1.0795 s → 1.0795 s | 17.613 MB | 0.000 MB | 0.000 MB | 17.613 MB → 17.613 MB | 3 |
| Python 3.8 [x86_64] | Python | S | 1 | 28.236 ms | 0.000 ms | 0.000 ms | 28.236 ms → 28.236 ms | 1.2952 s | 0.000 ms | 0.000 ms | 1.2952 s → 1.2952 s | 22.539 MB | 0.000 MB | 0.000 MB | 22.539 MB → 22.539 MB | 3 |
| Python 3.8 [x86_64] | Python | M | 1 | 28.504 ms | 0.000 ms | 0.000 ms | 28.504 ms → 28.504 ms | 1.2847 s | 0.000 ms | 0.000 ms | 1.2847 s → 1.2847 s | 23.551 MB | 0.000 MB | 0.000 MB | 23.551 MB → 23.551 MB | 3 |
| Python 3.8 [x86_64] | Python | L | 1 | 26.955 ms | 0.000 ms | 0.000 ms | 26.955 ms → 26.955 ms | 1.3694 s | 0.000 ms | 0.000 ms | 1.3694 s → 1.3694 s | 21.688 MB | 0.000 MB | 0.000 MB | 21.688 MB → 21.688 MB | 3 |
| Python 3.11 [x86_64] | Python | S | 1 | 27.921 ms | 0.000 ms | 0.000 ms | 27.921 ms → 27.921 ms | 1.3321 s | 0.000 ms | 0.000 ms | 1.3321 s → 1.3321 s | 25.379 MB | 0.000 MB | 0.000 MB | 25.379 MB → 25.379 MB | 3 |
| Python 3.11 [x86_64] | Python | M | 1 | 27.445 ms | 0.000 ms | 0.000 ms | 27.445 ms → 27.445 ms | 1.2922 s | 0.000 ms | 0.000 ms | 1.2922 s → 1.2922 s | 24.895 MB | 0.000 MB | 0.000 MB | 24.895 MB → 24.895 MB | 3 |
| Python 3.11 [x86_64] | Python | L | 1 | 26.907 ms | 0.000 ms | 0.000 ms | 26.907 ms → 26.907 ms | 1.3306 s | 0.000 ms | 0.000 ms | 1.3306 s → 1.3306 s | 25.418 MB | 0.000 MB | 0.000 MB | 25.418 MB → 25.418 MB | 3 |
| Python 3.12 [x86_64] | Python | S | 1 | 28.427 ms | 0.000 ms | 0.000 ms | 28.427 ms → 28.427 ms | 1.3625 s | 0.000 ms | 0.000 ms | 1.3625 s → 1.3625 s | 25.184 MB | 0.000 MB | 0.000 MB | 25.184 MB → 25.184 MB | 3 |
| Python 3.12 [x86_64] | Python | M | 1 | 27.387 ms | 0.000 ms | 0.000 ms | 27.387 ms → 27.387 ms | 1.3587 s | 0.000 ms | 0.000 ms | 1.3587 s → 1.3587 s | 25.305 MB | 0.000 MB | 0.000 MB | 25.305 MB → 25.305 MB | 3 |
| Python 3.12 [x86_64] | Python | L | 1 | 27.466 ms | 0.000 ms | 0.000 ms | 27.466 ms → 27.466 ms | 1.3426 s | 0.000 ms | 0.000 ms | 1.3426 s → 1.3426 s | 25.727 MB | 0.000 MB | 0.000 MB | 25.727 MB → 25.727 MB | 3 |
| Java 21 [x86_64] | Java | S | 1 | 35.424 ms | 0.000 ms | 0.000 ms | 35.424 ms → 35.424 ms | 1.1487 s | 0.000 ms | 0.000 ms | 1.1487 s → 1.1487 s | 40.152 MB | 0.000 MB | 0.000 MB | 40.152 MB → 40.152 MB | 5 |
| Java 21 [x86_64] | Java | M | 1 | 37.779 ms | 0.000 ms | 0.000 ms | 37.779 ms → 37.779 ms | 1.5685 s | 0.000 ms | 0.000 ms | 1.5685 s → 1.5685 s | 41.094 MB | 0.000 MB | 0.000 MB | 41.094 MB → 41.094 MB | 5 |
| Java 21 [x86_64] | Java | L | 1 | 38.355 ms | 0.000 ms | 0.000 ms | 38.355 ms → 38.355 ms | 1.2364 s | 0.000 ms | 0.000 ms | 1.2364 s → 1.2364 s | 39.523 MB | 0.000 MB | 0.000 MB | 39.523 MB → 39.523 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 26.766 ms | 0.000 ms | 0.000 ms | 26.766 ms → 26.766 ms | 1.0671 s | 0.000 ms | 0.000 ms | 1.0671 s → 1.0671 s | 9.438 MB | 0.000 MB | 0.000 MB | 9.438 MB → 9.438 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 26.402 ms | 0.000 ms | 0.000 ms | 26.402 ms → 26.402 ms | 961.903 ms | 0.000 ms | 0.000 ms | 961.903 ms → 961.903 ms | 9.789 MB | 0.000 MB | 0.000 MB | 9.789 MB → 9.789 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 26.523 ms | 0.000 ms | 0.000 ms | 26.523 ms → 26.523 ms | 945.356 ms | 0.000 ms | 0.000 ms | 945.356 ms → 945.356 ms | 11.203 MB | 0.000 MB | 0.000 MB | 11.203 MB → 11.203 MB | 5 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 28.900 ms | 0.000 ms | 0.000 ms | 28.900 ms → 28.900 ms | 1.0755 s | 0.000 ms | 0.000 ms | 1.0755 s → 1.0755 s | 18.719 MB | 0.000 MB | 0.000 MB | 18.719 MB → 18.719 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 28.545 ms | 0.000 ms | 0.000 ms | 28.545 ms → 28.545 ms | 1.0991 s | 0.000 ms | 0.000 ms | 1.0991 s → 1.0991 s | 18.734 MB | 0.000 MB | 0.000 MB | 18.734 MB → 18.734 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 27.918 ms | 0.000 ms | 0.000 ms | 27.918 ms → 27.918 ms | 1.1200 s | 0.000 ms | 0.000 ms | 1.1200 s → 1.1200 s | 18.301 MB | 0.000 MB | 0.000 MB | 18.301 MB → 18.301 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 32.955 ms | 0.000 ms | 0.000 ms | 32.955 ms → 32.955 ms | 1.0630 s | 0.000 ms | 0.000 ms | 1.0630 s → 1.0630 s | 20.590 MB | 0.000 MB | 0.000 MB | 20.590 MB → 20.590 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 31.780 ms | 0.000 ms | 0.000 ms | 31.780 ms → 31.780 ms | 1.0846 s | 0.000 ms | 0.000 ms | 1.0846 s → 1.0846 s | 19.938 MB | 0.000 MB | 0.000 MB | 19.938 MB → 19.938 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 30.507 ms | 0.000 ms | 0.000 ms | 30.507 ms → 30.507 ms | 1.0961 s | 0.000 ms | 0.000 ms | 1.0961 s → 1.0961 s | 20.328 MB | 0.000 MB | 0.000 MB | 20.328 MB → 20.328 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 67.115 ms | 0.000 ms | 0.000 ms | 67.115 ms → 67.115 ms | 1.0756 s | 0.000 ms | 0.000 ms | 1.0756 s → 1.0756 s | 30.840 MB | 0.000 MB | 0.000 MB | 30.840 MB → 30.840 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 67.030 ms | 0.000 ms | 0.000 ms | 67.030 ms → 67.030 ms | 1.2208 s | 0.000 ms | 0.000 ms | 1.2208 s → 1.2208 s | 29.867 MB | 0.000 MB | 0.000 MB | 29.867 MB → 29.867 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 68.518 ms | 0.000 ms | 0.000 ms | 68.518 ms → 68.518 ms | 1.3386 s | 0.000 ms | 0.000 ms | 1.3386 s → 1.3386 s | 29.863 MB | 0.000 MB | 0.000 MB | 29.863 MB → 29.863 MB | 4 |
| Go 1.23 [x86_64] | Go | S | 1 | 28.336 ms | 0.000 ms | 0.000 ms | 28.336 ms → 28.336 ms | 979.054 ms | 0.000 ms | 0.000 ms | 979.054 ms → 979.054 ms | 11.824 MB | 0.000 MB | 0.000 MB | 11.824 MB → 11.824 MB | 4 |
| Go 1.23 [x86_64] | Go | M | 1 | 27.071 ms | 0.000 ms | 0.000 ms | 27.071 ms → 27.071 ms | 953.023 ms | 0.000 ms | 0.000 ms | 953.023 ms → 953.023 ms | 11.074 MB | 0.000 MB | 0.000 MB | 11.074 MB → 11.074 MB | 4 |
| Go 1.23 [x86_64] | Go | L | 1 | 26.895 ms | 0.000 ms | 0.000 ms | 26.895 ms → 26.895 ms | 959.621 ms | 0.000 ms | 0.000 ms | 959.621 ms → 959.621 ms | 12.164 MB | 0.000 MB | 0.000 MB | 12.164 MB → 12.164 MB | 4 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 27.302 ms | 0.000 ms | 0.000 ms | 27.302 ms → 27.302 ms | 977.380 ms | 0.000 ms | 0.000 ms | 977.380 ms → 977.380 ms | 9.527 MB | 0.000 MB | 0.000 MB | 9.527 MB → 9.527 MB | 3 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 27.364 ms | 0.000 ms | 0.000 ms | 27.364 ms → 27.364 ms | 980.740 ms | 0.000 ms | 0.000 ms | 980.740 ms → 980.740 ms | 9.770 MB | 0.000 MB | 0.000 MB | 9.770 MB → 9.770 MB | 3 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 26.493 ms | 0.000 ms | 0.000 ms | 26.493 ms → 26.493 ms | 994.284 ms | 0.000 ms | 0.000 ms | 994.284 ms → 994.284 ms | 9.488 MB | 0.000 MB | 0.000 MB | 9.488 MB → 9.488 MB | 3 |

</details>

<details>
<summary><strong>binary_search_tree</strong> — Implementing a basic data structure (binary search tree)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 22.672 MB | 0.000 MB | 0.000 MB | 22.672 MB → 22.672 MB | 45 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 30.652 MB | 0.000 MB | 0.000 MB | 30.652 MB → 30.652 MB | 45 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 640.000 ms | 0.000 ms | 0.000 ms | 640.000 ms → 640.000 ms | 640.000 ms | 0.000 ms | 0.000 ms | 640.000 ms → 640.000 ms | 47.277 MB | 0.000 MB | 0.000 MB | 47.277 MB → 47.277 MB | 45 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 23.113 MB | 0.000 MB | 0.000 MB | 23.113 MB → 23.113 MB | 44 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 27.230 MB | 0.000 MB | 0.000 MB | 27.230 MB → 27.230 MB | 44 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 37.316 MB | 0.000 MB | 0.000 MB | 37.316 MB → 37.316 MB | 44 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 19.231 ms | 0.000 ms | 0.000 ms | 19.231 ms → 19.231 ms | 24.281 MB | 0.000 MB | 0.000 MB | 24.281 MB → 24.281 MB | 44 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 28.402 MB | 0.000 MB | 0.000 MB | 28.402 MB → 28.402 MB | 44 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 125.000 ms | 0.000 ms | 0.000 ms | 125.000 ms → 125.000 ms | 38.309 MB | 0.000 MB | 0.000 MB | 38.309 MB → 38.309 MB | 44 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 25.789 MB | 0.000 MB | 0.000 MB | 25.789 MB → 25.789 MB | 44 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 31.111 ms | 0.000 ms | 0.000 ms | 31.111 ms → 31.111 ms | 32.222 ms | 0.000 ms | 0.000 ms | 32.222 ms → 32.222 ms | 29.777 MB | 0.000 MB | 0.000 MB | 29.777 MB → 29.777 MB | 44 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 35.926 MB | 0.000 MB | 0.000 MB | 35.926 MB → 35.926 MB | 44 |
| Python 2.7 [x86_64] | Python | S | 1 | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 8.066 MB | 0.000 MB | 0.000 MB | 8.066 MB → 8.066 MB | 49 |
| Python 2.7 [x86_64] | Python | M | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 9.902 MB | 0.000 MB | 0.000 MB | 9.902 MB → 9.902 MB | 49 |
| Python 2.7 [x86_64] | Python | L | 1 | 260.000 ms | 0.000 ms | 0.000 ms | 260.000 ms → 260.000 ms | 260.000 ms | 0.000 ms | 0.000 ms | 260.000 ms → 260.000 ms | 15.129 MB | 0.000 MB | 0.000 MB | 15.129 MB → 15.129 MB | 49 |
| Python 3.8 [x86_64] | Python | S | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 11.062 MB | 0.000 MB | 0.000 MB | 11.062 MB → 11.062 MB | 49 |
| Python 3.8 [x86_64] | Python | M | 1 | 110.000 ms | 0.000 ms | 0.000 ms | 110.000 ms → 110.000 ms | 110.000 ms | 0.000 ms | 0.000 ms | 110.000 ms → 110.000 ms | 12.066 MB | 0.000 MB | 0.000 MB | 12.066 MB → 12.066 MB | 49 |
| Python 3.8 [x86_64] | Python | L | 1 | 250.000 ms | 0.000 ms | 0.000 ms | 250.000 ms → 250.000 ms | 260.000 ms | 0.000 ms | 0.000 ms | 260.000 ms → 260.000 ms | 16.473 MB | 0.000 MB | 0.000 MB | 16.473 MB → 16.473 MB | 49 |
| Python 3.11 [x86_64] | Python | S | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 13.512 MB | 0.000 MB | 0.000 MB | 13.512 MB → 13.512 MB | 49 |
| Python 3.11 [x86_64] | Python | M | 1 | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 16.211 MB | 0.000 MB | 0.000 MB | 16.211 MB → 16.211 MB | 49 |
| Python 3.11 [x86_64] | Python | L | 1 | 125.000 ms | 0.000 ms | 0.000 ms | 125.000 ms → 125.000 ms | 130.000 ms | 0.000 ms | 0.000 ms | 130.000 ms → 130.000 ms | 20.402 MB | 0.000 MB | 0.000 MB | 20.402 MB → 20.402 MB | 49 |
| Python 3.12 [x86_64] | Python | S | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 14.922 MB | 0.000 MB | 0.000 MB | 14.922 MB → 14.922 MB | 49 |
| Python 3.12 [x86_64] | Python | M | 1 | 95.000 ms | 0.000 ms | 0.000 ms | 95.000 ms → 95.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 16.031 MB | 0.000 MB | 0.000 MB | 16.031 MB → 16.031 MB | 49 |
| Python 3.12 [x86_64] | Python | L | 1 | 150.000 ms | 0.000 ms | 0.000 ms | 150.000 ms → 150.000 ms | 155.000 ms | 0.000 ms | 0.000 ms | 155.000 ms → 155.000 ms | 19.953 MB | 0.000 MB | 0.000 MB | 19.953 MB → 19.953 MB | 49 |
| Java 21 [x86_64] | Java | S | 1 | 116.667 ms | 0.000 ms | 0.000 ms | 116.667 ms → 116.667 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 45.152 MB | 0.000 MB | 0.000 MB | 45.152 MB → 45.152 MB | 45 |
| Java 21 [x86_64] | Java | M | 1 | 195.000 ms | 0.000 ms | 0.000 ms | 195.000 ms → 195.000 ms | 175.000 ms | 0.000 ms | 0.000 ms | 175.000 ms → 175.000 ms | 47.457 MB | 0.000 MB | 0.000 MB | 47.457 MB → 47.457 MB | 45 |
| Java 21 [x86_64] | Java | L | 1 | 260.000 ms | 0.000 ms | 0.000 ms | 260.000 ms → 260.000 ms | 200.000 ms | 0.000 ms | 0.000 ms | 200.000 ms → 200.000 ms | 50.766 MB | 0.000 MB | 0.000 MB | 50.766 MB → 50.766 MB | 45 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 3.000 ms | 0.000 ms | 0.000 ms | 3.000 ms → 3.000 ms | 3.040 ms | 0.000 ms | 0.000 ms | 3.040 ms → 3.040 ms | 3.824 MB | 0.000 MB | 0.000 MB | 3.824 MB → 3.824 MB | 58 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 7.200 ms | 0.000 ms | 0.000 ms | 7.200 ms → 7.200 ms | 7.600 ms | 0.000 ms | 0.000 ms | 7.600 ms → 7.600 ms | 4.281 MB | 0.000 MB | 0.000 MB | 4.281 MB → 4.281 MB | 58 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 5.156 MB | 0.000 MB | 0.000 MB | 5.156 MB → 5.156 MB | 58 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 53.598 MB | 0.000 MB | 0.000 MB | 53.598 MB → 53.598 MB | 41 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 58.000 ms | 0.000 ms | 0.000 ms | 58.000 ms → 58.000 ms | 58.000 ms | 0.000 ms | 0.000 ms | 58.000 ms → 58.000 ms | 55.895 MB | 0.000 MB | 0.000 MB | 55.895 MB → 55.895 MB | 41 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 82.500 ms | 0.000 ms | 0.000 ms | 82.500 ms → 82.500 ms | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 63.219 MB | 0.000 MB | 0.000 MB | 63.219 MB → 63.219 MB | 41 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 44.863 MB | 0.000 MB | 0.000 MB | 44.863 MB → 44.863 MB | 41 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 47.500 ms | 0.000 ms | 0.000 ms | 47.500 ms → 47.500 ms | 51.102 MB | 0.000 MB | 0.000 MB | 51.102 MB → 51.102 MB | 41 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 68.000 ms | 0.000 ms | 0.000 ms | 68.000 ms → 68.000 ms | 57.301 MB | 0.000 MB | 0.000 MB | 57.301 MB → 57.301 MB | 41 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 73.645 MB | 0.000 MB | 0.000 MB | 73.645 MB → 73.645 MB | 41 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 79.859 MB | 0.000 MB | 0.000 MB | 79.859 MB → 79.859 MB | 41 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 93.333 ms | 0.000 ms | 0.000 ms | 93.333 ms → 93.333 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 86.672 MB | 0.000 MB | 0.000 MB | 86.672 MB → 86.672 MB | 41 |
| Go 1.23 [x86_64] | Go | S | 1 | 3.280 ms | 0.000 ms | 0.000 ms | 3.280 ms → 3.280 ms | 3.320 ms | 0.000 ms | 0.000 ms | 3.320 ms → 3.320 ms | 9.562 MB | 0.000 MB | 0.000 MB | 9.562 MB → 9.562 MB | 53 |
| Go 1.23 [x86_64] | Go | M | 1 | 6.160 ms | 0.000 ms | 0.000 ms | 6.160 ms → 6.160 ms | 6.200 ms | 0.000 ms | 0.000 ms | 6.200 ms → 6.200 ms | 9.574 MB | 0.000 MB | 0.000 MB | 9.574 MB → 9.574 MB | 53 |
| Go 1.23 [x86_64] | Go | L | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 13.832 MB | 0.000 MB | 0.000 MB | 13.832 MB → 13.832 MB | 53 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 2.160 ms | 0.000 ms | 0.000 ms | 2.160 ms → 2.160 ms | 2.200 ms | 0.000 ms | 0.000 ms | 2.200 ms → 2.200 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 57 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 5.520 ms | 0.000 ms | 0.000 ms | 5.520 ms → 5.520 ms | 5.560 ms | 0.000 ms | 0.000 ms | 5.560 ms → 5.560 ms | 3.344 MB | 0.000 MB | 0.000 MB | 3.344 MB → 3.344 MB | 57 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 4.828 MB | 0.000 MB | 0.000 MB | 4.828 MB → 4.828 MB | 57 |

</details>

<details>
<summary><strong>chat_application</strong> — Implementing a simple chat application</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 29.905 ms | 0.000 ms | 0.000 ms | 29.905 ms → 29.905 ms | 205.085 ms | 0.000 ms | 0.000 ms | 205.085 ms → 205.085 ms | 13.703 MB | 0.000 MB | 0.000 MB | 13.703 MB → 13.703 MB | 5 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 32.157 ms | 0.000 ms | 0.000 ms | 32.157 ms → 32.157 ms | 212.032 ms | 0.000 ms | 0.000 ms | 212.032 ms → 212.032 ms | 16.074 MB | 0.000 MB | 0.000 MB | 16.074 MB → 16.074 MB | 5 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 36.612 ms | 0.000 ms | 0.000 ms | 36.612 ms → 36.612 ms | 243.141 ms | 0.000 ms | 0.000 ms | 243.141 ms → 243.141 ms | 13.836 MB | 0.000 MB | 0.000 MB | 13.836 MB → 13.836 MB | 5 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 27.931 ms | 0.000 ms | 0.000 ms | 27.931 ms → 27.931 ms | 194.771 ms | 0.000 ms | 0.000 ms | 194.771 ms → 194.771 ms | 15.926 MB | 0.000 MB | 0.000 MB | 15.926 MB → 15.926 MB | 5 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 30.550 ms | 0.000 ms | 0.000 ms | 30.550 ms → 30.550 ms | 211.609 ms | 0.000 ms | 0.000 ms | 211.609 ms → 211.609 ms | 15.531 MB | 0.000 MB | 0.000 MB | 15.531 MB → 15.531 MB | 5 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 35.670 ms | 0.000 ms | 0.000 ms | 35.670 ms → 35.670 ms | 246.436 ms | 0.000 ms | 0.000 ms | 246.436 ms → 246.436 ms | 15.711 MB | 0.000 MB | 0.000 MB | 15.711 MB → 15.711 MB | 5 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 27.188 ms | 0.000 ms | 0.000 ms | 27.188 ms → 27.188 ms | 200.605 ms | 0.000 ms | 0.000 ms | 200.605 ms → 200.605 ms | 17.098 MB | 0.000 MB | 0.000 MB | 17.098 MB → 17.098 MB | 5 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 29.843 ms | 0.000 ms | 0.000 ms | 29.843 ms → 29.843 ms | 209.831 ms | 0.000 ms | 0.000 ms | 209.831 ms → 209.831 ms | 15.262 MB | 0.000 MB | 0.000 MB | 15.262 MB → 15.262 MB | 5 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 36.136 ms | 0.000 ms | 0.000 ms | 36.136 ms → 36.136 ms | 251.356 ms | 0.000 ms | 0.000 ms | 251.356 ms → 251.356 ms | 15.438 MB | 0.000 MB | 0.000 MB | 15.438 MB → 15.438 MB | 5 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 27.680 ms | 0.000 ms | 0.000 ms | 27.680 ms → 27.680 ms | 194.318 ms | 0.000 ms | 0.000 ms | 194.318 ms → 194.318 ms | 18.324 MB | 0.000 MB | 0.000 MB | 18.324 MB → 18.324 MB | 5 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 30.919 ms | 0.000 ms | 0.000 ms | 30.919 ms → 30.919 ms | 221.060 ms | 0.000 ms | 0.000 ms | 221.060 ms → 221.060 ms | 16.930 MB | 0.000 MB | 0.000 MB | 16.930 MB → 16.930 MB | 5 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 35.485 ms | 0.000 ms | 0.000 ms | 35.485 ms → 35.485 ms | 247.784 ms | 0.000 ms | 0.000 ms | 247.784 ms → 247.784 ms | 17.473 MB | 0.000 MB | 0.000 MB | 17.473 MB → 17.473 MB | 5 |
| Python 2.7 [x86_64] | Python | S | 1 | 73.711 ms | 0.000 ms | 0.000 ms | 73.711 ms → 73.711 ms | 242.870 ms | 0.000 ms | 0.000 ms | 242.870 ms → 242.870 ms | 17.406 MB | 0.000 MB | 0.000 MB | 17.406 MB → 17.406 MB | 3 |
| Python 2.7 [x86_64] | Python | M | 1 | 68.983 ms | 0.000 ms | 0.000 ms | 68.983 ms → 68.983 ms | 210.132 ms | 0.000 ms | 0.000 ms | 210.132 ms → 210.132 ms | 19.266 MB | 0.000 MB | 0.000 MB | 19.266 MB → 19.266 MB | 3 |
| Python 2.7 [x86_64] | Python | L | 1 | 76.884 ms | 0.000 ms | 0.000 ms | 76.884 ms → 76.884 ms | 241.409 ms | 0.000 ms | 0.000 ms | 241.409 ms → 241.409 ms | 19.688 MB | 0.000 MB | 0.000 MB | 19.688 MB → 19.688 MB | 3 |
| Python 3.8 [x86_64] | Python | S | 1 | 115.293 ms | 0.000 ms | 0.000 ms | 115.293 ms → 115.293 ms | 194.149 ms | 0.000 ms | 0.000 ms | 194.149 ms → 194.149 ms | 18.793 MB | 0.000 MB | 0.000 MB | 18.793 MB → 18.793 MB | 3 |
| Python 3.8 [x86_64] | Python | M | 1 | 101.300 ms | 0.000 ms | 0.000 ms | 101.300 ms → 101.300 ms | 272.034 ms | 0.000 ms | 0.000 ms | 272.034 ms → 272.034 ms | 20.008 MB | 0.000 MB | 0.000 MB | 20.008 MB → 20.008 MB | 3 |
| Python 3.8 [x86_64] | Python | L | 1 | 80.746 ms | 0.000 ms | 0.000 ms | 80.746 ms → 80.746 ms | 238.779 ms | 0.000 ms | 0.000 ms | 238.779 ms → 238.779 ms | 18.344 MB | 0.000 MB | 0.000 MB | 18.344 MB → 18.344 MB | 3 |
| Python 3.11 [x86_64] | Python | S | 1 | 75.879 ms | 0.000 ms | 0.000 ms | 75.879 ms → 75.879 ms | 210.504 ms | 0.000 ms | 0.000 ms | 210.504 ms → 210.504 ms | 19.562 MB | 0.000 MB | 0.000 MB | 19.562 MB → 19.562 MB | 3 |
| Python 3.11 [x86_64] | Python | M | 1 | 77.206 ms | 0.000 ms | 0.000 ms | 77.206 ms → 77.206 ms | 215.333 ms | 0.000 ms | 0.000 ms | 215.333 ms → 215.333 ms | 21.176 MB | 0.000 MB | 0.000 MB | 21.176 MB → 21.176 MB | 3 |
| Python 3.11 [x86_64] | Python | L | 1 | 84.505 ms | 0.000 ms | 0.000 ms | 84.505 ms → 84.505 ms | 249.365 ms | 0.000 ms | 0.000 ms | 249.365 ms → 249.365 ms | 21.621 MB | 0.000 MB | 0.000 MB | 21.621 MB → 21.621 MB | 3 |
| Python 3.12 [x86_64] | Python | S | 1 | 76.046 ms | 0.000 ms | 0.000 ms | 76.046 ms → 76.046 ms | 206.978 ms | 0.000 ms | 0.000 ms | 206.978 ms → 206.978 ms | 19.359 MB | 0.000 MB | 0.000 MB | 19.359 MB → 19.359 MB | 3 |
| Python 3.12 [x86_64] | Python | M | 1 | 85.810 ms | 0.000 ms | 0.000 ms | 85.810 ms → 85.810 ms | 210.866 ms | 0.000 ms | 0.000 ms | 210.866 ms → 210.866 ms | 19.660 MB | 0.000 MB | 0.000 MB | 19.660 MB → 19.660 MB | 3 |
| Python 3.12 [x86_64] | Python | L | 1 | 112.684 ms | 0.000 ms | 0.000 ms | 112.684 ms → 112.684 ms | 247.395 ms | 0.000 ms | 0.000 ms | 247.395 ms → 247.395 ms | 20.434 MB | 0.000 MB | 0.000 MB | 20.434 MB → 20.434 MB | 3 |
| Java 21 [x86_64] | Java | S | 1 | 45.939 ms | 0.000 ms | 0.000 ms | 45.939 ms → 45.939 ms | 224.247 ms | 0.000 ms | 0.000 ms | 224.247 ms → 224.247 ms | 33.637 MB | 0.000 MB | 0.000 MB | 33.637 MB → 33.637 MB | 5 |
| Java 21 [x86_64] | Java | M | 1 | 87.285 ms | 0.000 ms | 0.000 ms | 87.285 ms → 87.285 ms | 316.222 ms | 0.000 ms | 0.000 ms | 316.222 ms → 316.222 ms | 33.957 MB | 0.000 MB | 0.000 MB | 33.957 MB → 33.957 MB | 5 |
| Java 21 [x86_64] | Java | L | 1 | 130.246 ms | 0.000 ms | 0.000 ms | 130.246 ms → 130.246 ms | 328.771 ms | 0.000 ms | 0.000 ms | 328.771 ms → 328.771 ms | 34.078 MB | 0.000 MB | 0.000 MB | 34.078 MB → 34.078 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 27.518 ms | 0.000 ms | 0.000 ms | 27.518 ms → 27.518 ms | 284.662 ms | 0.000 ms | 0.000 ms | 284.662 ms → 284.662 ms | 9.492 MB | 0.000 MB | 0.000 MB | 9.492 MB → 9.492 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 28.435 ms | 0.000 ms | 0.000 ms | 28.435 ms → 28.435 ms | 253.332 ms | 0.000 ms | 0.000 ms | 253.332 ms → 253.332 ms | 10.520 MB | 0.000 MB | 0.000 MB | 10.520 MB → 10.520 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 34.191 ms | 0.000 ms | 0.000 ms | 34.191 ms → 34.191 ms | 280.861 ms | 0.000 ms | 0.000 ms | 280.861 ms → 280.861 ms | 9.797 MB | 0.000 MB | 0.000 MB | 9.797 MB → 9.797 MB | 6 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 40.641 ms | 0.000 ms | 0.000 ms | 40.641 ms → 40.641 ms | 249.738 ms | 0.000 ms | 0.000 ms | 249.738 ms → 249.738 ms | 18.652 MB | 0.000 MB | 0.000 MB | 18.652 MB → 18.652 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 60.018 ms | 0.000 ms | 0.000 ms | 60.018 ms → 60.018 ms | 260.585 ms | 0.000 ms | 0.000 ms | 260.585 ms → 260.585 ms | 22.176 MB | 0.000 MB | 0.000 MB | 22.176 MB → 22.176 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 100.344 ms | 0.000 ms | 0.000 ms | 100.344 ms → 100.344 ms | 308.930 ms | 0.000 ms | 0.000 ms | 308.930 ms → 308.930 ms | 21.137 MB | 0.000 MB | 0.000 MB | 21.137 MB → 21.137 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 50.941 ms | 0.000 ms | 0.000 ms | 50.941 ms → 50.941 ms | 249.021 ms | 0.000 ms | 0.000 ms | 249.021 ms → 249.021 ms | 26.887 MB | 0.000 MB | 0.000 MB | 26.887 MB → 26.887 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 66.502 ms | 0.000 ms | 0.000 ms | 66.502 ms → 66.502 ms | 269.786 ms | 0.000 ms | 0.000 ms | 269.786 ms → 269.786 ms | 21.715 MB | 0.000 MB | 0.000 MB | 21.715 MB → 21.715 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 97.241 ms | 0.000 ms | 0.000 ms | 97.241 ms → 97.241 ms | 313.667 ms | 0.000 ms | 0.000 ms | 313.667 ms → 313.667 ms | 23.539 MB | 0.000 MB | 0.000 MB | 23.539 MB → 23.539 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 42.730 ms | 0.000 ms | 0.000 ms | 42.730 ms → 42.730 ms | 247.599 ms | 0.000 ms | 0.000 ms | 247.599 ms → 247.599 ms | 37.484 MB | 0.000 MB | 0.000 MB | 37.484 MB → 37.484 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 74.504 ms | 0.000 ms | 0.000 ms | 74.504 ms → 74.504 ms | 286.948 ms | 0.000 ms | 0.000 ms | 286.948 ms → 286.948 ms | 43.355 MB | 0.000 MB | 0.000 MB | 43.355 MB → 43.355 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 179.187 ms | 0.000 ms | 0.000 ms | 179.187 ms → 179.187 ms | 679.135 ms | 0.000 ms | 0.000 ms | 679.135 ms → 679.135 ms | 42.141 MB | 0.000 MB | 0.000 MB | 42.141 MB → 42.141 MB | 4 |
| Go 1.23 [x86_64] | Go | S | 1 | 29.955 ms | 0.000 ms | 0.000 ms | 29.955 ms → 29.955 ms | 224.915 ms | 0.000 ms | 0.000 ms | 224.915 ms → 224.915 ms | 11.820 MB | 0.000 MB | 0.000 MB | 11.820 MB → 11.820 MB | 4 |
| Go 1.23 [x86_64] | Go | M | 1 | 33.984 ms | 0.000 ms | 0.000 ms | 33.984 ms → 33.984 ms | 246.965 ms | 0.000 ms | 0.000 ms | 246.965 ms → 246.965 ms | 14.609 MB | 0.000 MB | 0.000 MB | 14.609 MB → 14.609 MB | 4 |
| Go 1.23 [x86_64] | Go | L | 1 | 45.900 ms | 0.000 ms | 0.000 ms | 45.900 ms → 45.900 ms | 265.586 ms | 0.000 ms | 0.000 ms | 265.586 ms → 265.586 ms | 11.988 MB | 0.000 MB | 0.000 MB | 11.988 MB → 11.988 MB | 4 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 28.405 ms | 0.000 ms | 0.000 ms | 28.405 ms → 28.405 ms | 225.433 ms | 0.000 ms | 0.000 ms | 225.433 ms → 225.433 ms | 9.164 MB | 0.000 MB | 0.000 MB | 9.164 MB → 9.164 MB | 3 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 30.166 ms | 0.000 ms | 0.000 ms | 30.166 ms → 30.166 ms | 234.288 ms | 0.000 ms | 0.000 ms | 234.288 ms → 234.288 ms | 9.277 MB | 0.000 MB | 0.000 MB | 9.277 MB → 9.277 MB | 3 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 32.195 ms | 0.000 ms | 0.000 ms | 32.195 ms → 32.195 ms | 262.252 ms | 0.000 ms | 0.000 ms | 262.252 ms → 262.252 ms | 11.172 MB | 0.000 MB | 0.000 MB | 11.172 MB → 11.172 MB | 3 |

</details>

<details>
<summary><strong>cli_file_search</strong> — Implementing a basic command-line tool (a file search utility)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 12.308 ms | 0.000 ms | 0.000 ms | 12.308 ms → 12.308 ms | 13.077 ms | 0.000 ms | 0.000 ms | 13.077 ms → 13.077 ms | 20.875 MB | 0.000 MB | 0.000 MB | 20.875 MB → 20.875 MB | 17 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 20.652 MB | 0.000 MB | 0.000 MB | 20.652 MB → 20.652 MB | 17 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 20.887 MB | 0.000 MB | 0.000 MB | 20.887 MB → 20.887 MB | 17 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 13.077 ms | 0.000 ms | 0.000 ms | 13.077 ms → 13.077 ms | 13.077 ms | 0.000 ms | 0.000 ms | 13.077 ms → 13.077 ms | 22.781 MB | 0.000 MB | 0.000 MB | 22.781 MB → 22.781 MB | 16 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 22.844 MB | 0.000 MB | 0.000 MB | 22.844 MB → 22.844 MB | 16 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 22.836 MB | 0.000 MB | 0.000 MB | 22.836 MB → 22.836 MB | 16 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 23.988 MB | 0.000 MB | 0.000 MB | 23.988 MB → 23.988 MB | 16 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 15.600 ms | 0.000 ms | 0.000 ms | 15.600 ms → 15.600 ms | 15.600 ms | 0.000 ms | 0.000 ms | 15.600 ms → 15.600 ms | 24.047 MB | 0.000 MB | 0.000 MB | 24.047 MB → 24.047 MB | 16 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 24.035 MB | 0.000 MB | 0.000 MB | 24.035 MB → 24.035 MB | 16 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 13.077 ms | 0.000 ms | 0.000 ms | 13.077 ms → 13.077 ms | 13.846 ms | 0.000 ms | 0.000 ms | 13.846 ms → 13.846 ms | 25.367 MB | 0.000 MB | 0.000 MB | 25.367 MB → 25.367 MB | 16 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 25.426 MB | 0.000 MB | 0.000 MB | 25.426 MB → 25.426 MB | 16 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 25.410 MB | 0.000 MB | 0.000 MB | 25.410 MB → 25.410 MB | 16 |
| Python 2.7 [x86_64] | Python | S | 1 | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 7.848 MB | 0.000 MB | 0.000 MB | 7.848 MB → 7.848 MB | 14 |
| Python 2.7 [x86_64] | Python | M | 1 | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 15.714 ms | 0.000 ms | 0.000 ms | 15.714 ms → 15.714 ms | 7.934 MB | 0.000 MB | 0.000 MB | 7.934 MB → 7.934 MB | 14 |
| Python 2.7 [x86_64] | Python | L | 1 | 17.143 ms | 0.000 ms | 0.000 ms | 17.143 ms → 17.143 ms | 17.143 ms | 0.000 ms | 0.000 ms | 17.143 ms → 17.143 ms | 7.816 MB | 0.000 MB | 0.000 MB | 7.816 MB → 7.816 MB | 14 |
| Python 3.8 [x86_64] | Python | S | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 10.836 MB | 0.000 MB | 0.000 MB | 10.836 MB → 10.836 MB | 11 |
| Python 3.8 [x86_64] | Python | M | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 10.641 MB | 0.000 MB | 0.000 MB | 10.641 MB → 10.641 MB | 11 |
| Python 3.8 [x86_64] | Python | L | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 10.656 MB | 0.000 MB | 0.000 MB | 10.656 MB → 10.656 MB | 11 |
| Python 3.11 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 13.742 MB | 0.000 MB | 0.000 MB | 13.742 MB → 13.742 MB | 11 |
| Python 3.11 [x86_64] | Python | M | 1 | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 13.695 MB | 0.000 MB | 0.000 MB | 13.695 MB → 13.695 MB | 11 |
| Python 3.11 [x86_64] | Python | L | 1 | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 13.762 MB | 0.000 MB | 0.000 MB | 13.762 MB → 13.762 MB | 11 |
| Python 3.12 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 14.836 MB | 0.000 MB | 0.000 MB | 14.836 MB → 14.836 MB | 11 |
| Python 3.12 [x86_64] | Python | M | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.953 MB | 0.000 MB | 0.000 MB | 14.953 MB → 14.953 MB | 11 |
| Python 3.12 [x86_64] | Python | L | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.848 MB | 0.000 MB | 0.000 MB | 14.848 MB → 14.848 MB | 11 |
| Java 21 [x86_64] | Java | S | 1 | 160.000 ms | 0.000 ms | 0.000 ms | 160.000 ms → 160.000 ms | 150.000 ms | 0.000 ms | 0.000 ms | 150.000 ms → 150.000 ms | 45.398 MB | 0.000 MB | 0.000 MB | 45.398 MB → 45.398 MB | 17 |
| Java 21 [x86_64] | Java | M | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 47.180 MB | 0.000 MB | 0.000 MB | 47.180 MB → 47.180 MB | 17 |
| Java 21 [x86_64] | Java | L | 1 | 226.667 ms | 0.000 ms | 0.000 ms | 226.667 ms → 226.667 ms | 220.000 ms | 0.000 ms | 0.000 ms | 220.000 ms → 220.000 ms | 47.629 MB | 0.000 MB | 0.000 MB | 47.629 MB → 47.629 MB | 17 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 1.840 ms | 0.000 ms | 0.000 ms | 1.840 ms → 1.840 ms | 1.920 ms | 0.000 ms | 0.000 ms | 1.920 ms → 1.920 ms | 3.887 MB | 0.000 MB | 0.000 MB | 3.887 MB → 3.887 MB | 18 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 2.000 ms | 0.000 ms | 0.000 ms | 2.000 ms → 2.000 ms | 2.040 ms | 0.000 ms | 0.000 ms | 2.040 ms → 2.040 ms | 3.887 MB | 0.000 MB | 0.000 MB | 3.887 MB → 3.887 MB | 18 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 2.160 ms | 0.000 ms | 0.000 ms | 2.160 ms → 2.160 ms | 2.240 ms | 0.000 ms | 0.000 ms | 2.240 ms → 2.240 ms | 3.887 MB | 0.000 MB | 0.000 MB | 3.887 MB → 3.887 MB | 18 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 41.429 ms | 0.000 ms | 0.000 ms | 41.429 ms → 41.429 ms | 41.429 ms | 0.000 ms | 0.000 ms | 41.429 ms → 41.429 ms | 52.422 MB | 0.000 MB | 0.000 MB | 52.422 MB → 52.422 MB | 18 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 45.714 ms | 0.000 ms | 0.000 ms | 45.714 ms → 45.714 ms | 45.714 ms | 0.000 ms | 0.000 ms | 45.714 ms → 45.714 ms | 52.598 MB | 0.000 MB | 0.000 MB | 52.598 MB → 52.598 MB | 18 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 53.234 MB | 0.000 MB | 0.000 MB | 53.234 MB → 53.234 MB | 18 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 43.797 MB | 0.000 MB | 0.000 MB | 43.797 MB → 43.797 MB | 18 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 36.000 ms | 0.000 ms | 0.000 ms | 36.000 ms → 36.000 ms | 36.000 ms | 0.000 ms | 0.000 ms | 36.000 ms → 36.000 ms | 43.895 MB | 0.000 MB | 0.000 MB | 43.895 MB → 43.895 MB | 18 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 44.789 MB | 0.000 MB | 0.000 MB | 44.789 MB → 44.789 MB | 18 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 69.906 MB | 0.000 MB | 0.000 MB | 69.906 MB → 69.906 MB | 18 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 70.125 MB | 0.000 MB | 0.000 MB | 70.125 MB → 70.125 MB | 18 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 69.879 MB | 0.000 MB | 0.000 MB | 69.879 MB → 69.879 MB | 18 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.680 ms | 0.000 ms | 0.000 ms | 2.680 ms → 2.680 ms | 2.640 ms | 0.000 ms | 0.000 ms | 2.640 ms → 2.640 ms | 7.547 MB | 0.000 MB | 0.000 MB | 7.547 MB → 7.547 MB | 25 |
| Go 1.23 [x86_64] | Go | M | 1 | 2.880 ms | 0.000 ms | 0.000 ms | 2.880 ms → 2.880 ms | 2.920 ms | 0.000 ms | 0.000 ms | 2.920 ms → 2.920 ms | 7.551 MB | 0.000 MB | 0.000 MB | 7.551 MB → 7.551 MB | 25 |
| Go 1.23 [x86_64] | Go | L | 1 | 3.360 ms | 0.000 ms | 0.000 ms | 3.360 ms → 3.360 ms | 3.360 ms | 0.000 ms | 0.000 ms | 3.360 ms → 3.360 ms | 9.555 MB | 0.000 MB | 0.000 MB | 9.555 MB → 9.555 MB | 25 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.440 ms | 0.000 ms | 0.000 ms | 1.440 ms → 1.440 ms | 1.480 ms | 0.000 ms | 0.000 ms | 1.480 ms → 1.480 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 24 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 1.600 ms | 0.000 ms | 0.000 ms | 1.600 ms → 1.600 ms | 1.640 ms | 0.000 ms | 0.000 ms | 1.640 ms → 1.640 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 24 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 1.720 ms | 0.000 ms | 0.000 ms | 1.720 ms → 1.720 ms | 1.760 ms | 0.000 ms | 0.000 ms | 1.760 ms → 1.760 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 24 |

</details>

<details>
<summary><strong>csv_parsing</strong> — Processing a large dataset (CSV file parsing)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 31.429 ms | 0.000 ms | 0.000 ms | 31.429 ms → 31.429 ms | 32.857 ms | 0.000 ms | 0.000 ms | 32.857 ms → 32.857 ms | 20.703 MB | 0.000 MB | 0.000 MB | 20.703 MB → 20.703 MB | 12 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 113.333 ms | 0.000 ms | 0.000 ms | 113.333 ms → 113.333 ms | 116.667 ms | 0.000 ms | 0.000 ms | 116.667 ms → 116.667 ms | 20.820 MB | 0.000 MB | 0.000 MB | 20.820 MB → 20.820 MB | 12 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 220.000 ms | 0.000 ms | 0.000 ms | 220.000 ms → 220.000 ms | 225.000 ms | 0.000 ms | 0.000 ms | 225.000 ms → 225.000 ms | 20.691 MB | 0.000 MB | 0.000 MB | 20.691 MB → 20.691 MB | 12 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 26.667 ms | 0.000 ms | 0.000 ms | 26.667 ms → 26.667 ms | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 22.719 MB | 0.000 MB | 0.000 MB | 22.719 MB → 22.719 MB | 11 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 86.667 ms | 0.000 ms | 0.000 ms | 86.667 ms → 86.667 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 22.738 MB | 0.000 MB | 0.000 MB | 22.738 MB → 22.738 MB | 11 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 22.648 MB | 0.000 MB | 0.000 MB | 22.648 MB → 22.648 MB | 11 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 24.043 MB | 0.000 MB | 0.000 MB | 24.043 MB → 24.043 MB | 11 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 86.667 ms | 0.000 ms | 0.000 ms | 86.667 ms → 86.667 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 23.840 MB | 0.000 MB | 0.000 MB | 23.840 MB → 23.840 MB | 11 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 160.000 ms | 0.000 ms | 0.000 ms | 160.000 ms → 160.000 ms | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 23.664 MB | 0.000 MB | 0.000 MB | 23.664 MB → 23.664 MB | 11 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 25.414 MB | 0.000 MB | 0.000 MB | 25.414 MB → 25.414 MB | 11 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 86.667 ms | 0.000 ms | 0.000 ms | 86.667 ms → 86.667 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 25.414 MB | 0.000 MB | 0.000 MB | 25.414 MB → 25.414 MB | 11 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 25.309 MB | 0.000 MB | 0.000 MB | 25.309 MB → 25.309 MB | 11 |
| Python 2.7 [x86_64] | Python | S | 1 | 47.500 ms | 0.000 ms | 0.000 ms | 47.500 ms → 47.500 ms | 47.500 ms | 0.000 ms | 0.000 ms | 47.500 ms → 47.500 ms | 7.902 MB | 0.000 MB | 0.000 MB | 7.902 MB → 7.902 MB | 13 |
| Python 2.7 [x86_64] | Python | M | 1 | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 7.906 MB | 0.000 MB | 0.000 MB | 7.906 MB → 7.906 MB | 13 |
| Python 2.7 [x86_64] | Python | L | 1 | 320.000 ms | 0.000 ms | 0.000 ms | 320.000 ms → 320.000 ms | 320.000 ms | 0.000 ms | 0.000 ms | 320.000 ms → 320.000 ms | 7.930 MB | 0.000 MB | 0.000 MB | 7.930 MB → 7.930 MB | 13 |
| Python 3.8 [x86_64] | Python | S | 1 | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 11.059 MB | 0.000 MB | 0.000 MB | 11.059 MB → 11.059 MB | 10 |
| Python 3.8 [x86_64] | Python | M | 1 | 175.000 ms | 0.000 ms | 0.000 ms | 175.000 ms → 175.000 ms | 180.000 ms | 0.000 ms | 0.000 ms | 180.000 ms → 180.000 ms | 10.922 MB | 0.000 MB | 0.000 MB | 10.922 MB → 10.922 MB | 10 |
| Python 3.8 [x86_64] | Python | L | 1 | 340.000 ms | 0.000 ms | 0.000 ms | 340.000 ms → 340.000 ms | 340.000 ms | 0.000 ms | 0.000 ms | 340.000 ms → 340.000 ms | 11.141 MB | 0.000 MB | 0.000 MB | 11.141 MB → 11.141 MB | 10 |
| Python 3.11 [x86_64] | Python | S | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 13.789 MB | 0.000 MB | 0.000 MB | 13.789 MB → 13.789 MB | 10 |
| Python 3.11 [x86_64] | Python | M | 1 | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 13.754 MB | 0.000 MB | 0.000 MB | 13.754 MB → 13.754 MB | 10 |
| Python 3.11 [x86_64] | Python | L | 1 | 250.000 ms | 0.000 ms | 0.000 ms | 250.000 ms → 250.000 ms | 250.000 ms | 0.000 ms | 0.000 ms | 250.000 ms → 250.000 ms | 13.711 MB | 0.000 MB | 0.000 MB | 13.711 MB → 13.711 MB | 10 |
| Python 3.12 [x86_64] | Python | S | 1 | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 15.176 MB | 0.000 MB | 0.000 MB | 15.176 MB → 15.176 MB | 10 |
| Python 3.12 [x86_64] | Python | M | 1 | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 15.191 MB | 0.000 MB | 0.000 MB | 15.191 MB → 15.191 MB | 10 |
| Python 3.12 [x86_64] | Python | L | 1 | 300.000 ms | 0.000 ms | 0.000 ms | 300.000 ms → 300.000 ms | 310.000 ms | 0.000 ms | 0.000 ms | 310.000 ms → 310.000 ms | 15.250 MB | 0.000 MB | 0.000 MB | 15.250 MB → 15.250 MB | 10 |
| Java 21 [x86_64] | Java | S | 1 | 245.000 ms | 0.000 ms | 0.000 ms | 245.000 ms → 245.000 ms | 245.000 ms | 0.000 ms | 0.000 ms | 245.000 ms → 245.000 ms | 48.309 MB | 0.000 MB | 0.000 MB | 48.309 MB → 48.309 MB | 13 |
| Java 21 [x86_64] | Java | M | 1 | 450.000 ms | 0.000 ms | 0.000 ms | 450.000 ms → 450.000 ms | 440.000 ms | 0.000 ms | 0.000 ms | 440.000 ms → 440.000 ms | 54.895 MB | 0.000 MB | 0.000 MB | 54.895 MB → 54.895 MB | 13 |
| Java 21 [x86_64] | Java | L | 1 | 630.000 ms | 0.000 ms | 0.000 ms | 630.000 ms → 630.000 ms | 610.000 ms | 0.000 ms | 0.000 ms | 610.000 ms → 610.000 ms | 57.211 MB | 0.000 MB | 0.000 MB | 57.211 MB → 57.211 MB | 13 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 4.560 ms | 0.000 ms | 0.000 ms | 4.560 ms → 4.560 ms | 4.640 ms | 0.000 ms | 0.000 ms | 4.640 ms → 4.640 ms | 3.746 MB | 0.000 MB | 0.000 MB | 3.746 MB → 3.746 MB | 20 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 20 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 3.676 MB | 0.000 MB | 0.000 MB | 3.676 MB → 3.676 MB | 20 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 47.143 ms | 0.000 ms | 0.000 ms | 47.143 ms → 47.143 ms | 47.143 ms | 0.000 ms | 0.000 ms | 47.143 ms → 47.143 ms | 53.895 MB | 0.000 MB | 0.000 MB | 53.895 MB → 53.895 MB | 10 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 62.426 MB | 0.000 MB | 0.000 MB | 62.426 MB → 62.426 MB | 10 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 96.667 ms | 0.000 ms | 0.000 ms | 96.667 ms → 96.667 ms | 96.667 ms | 0.000 ms | 0.000 ms | 96.667 ms → 96.667 ms | 67.809 MB | 0.000 MB | 0.000 MB | 67.809 MB → 67.809 MB | 10 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 47.143 ms | 0.000 ms | 0.000 ms | 47.143 ms → 47.143 ms | 45.714 ms | 0.000 ms | 0.000 ms | 45.714 ms → 45.714 ms | 49.094 MB | 0.000 MB | 0.000 MB | 49.094 MB → 49.094 MB | 10 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 68.742 MB | 0.000 MB | 0.000 MB | 68.742 MB → 68.742 MB | 10 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 116.667 ms | 0.000 ms | 0.000 ms | 116.667 ms → 116.667 ms | 116.667 ms | 0.000 ms | 0.000 ms | 116.667 ms → 116.667 ms | 92.238 MB | 0.000 MB | 0.000 MB | 92.238 MB → 92.238 MB | 10 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 76.578 MB | 0.000 MB | 0.000 MB | 76.578 MB → 76.578 MB | 10 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 83.333 ms | 0.000 ms | 0.000 ms | 83.333 ms → 83.333 ms | 87.758 MB | 0.000 MB | 0.000 MB | 87.758 MB → 87.758 MB | 10 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 105.000 ms | 0.000 ms | 0.000 ms | 105.000 ms → 105.000 ms | 96.891 MB | 0.000 MB | 0.000 MB | 96.891 MB → 96.891 MB | 10 |
| Go 1.23 [x86_64] | Go | S | 1 | 4.840 ms | 0.000 ms | 0.000 ms | 4.840 ms → 4.840 ms | 4.880 ms | 0.000 ms | 0.000 ms | 4.880 ms → 4.880 ms | 9.586 MB | 0.000 MB | 0.000 MB | 9.586 MB → 9.586 MB | 21 |
| Go 1.23 [x86_64] | Go | M | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 37.778 ms | 0.000 ms | 0.000 ms | 37.778 ms → 37.778 ms | 18.359 MB | 0.000 MB | 0.000 MB | 18.359 MB → 18.359 MB | 21 |
| Go 1.23 [x86_64] | Go | L | 1 | 122.000 ms | 0.000 ms | 0.000 ms | 122.000 ms → 122.000 ms | 116.000 ms | 0.000 ms | 0.000 ms | 116.000 ms → 116.000 ms | 24.793 MB | 0.000 MB | 0.000 MB | 24.793 MB → 24.793 MB | 21 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 2.360 ms | 0.000 ms | 0.000 ms | 2.360 ms → 2.360 ms | 2.440 ms | 0.000 ms | 0.000 ms | 2.440 ms → 2.440 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 10 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 6.920 ms | 0.000 ms | 0.000 ms | 6.920 ms → 6.920 ms | 7.000 ms | 0.000 ms | 0.000 ms | 7.000 ms → 7.000 ms | 3.465 MB | 0.000 MB | 0.000 MB | 3.465 MB → 3.465 MB | 10 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 12.000 ms | 0.000 ms | 0.000 ms | 12.000 ms → 12.000 ms | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 4.594 MB | 0.000 MB | 0.000 MB | 4.594 MB → 4.594 MB | 10 |

</details>

<details>
<summary><strong>data_visualization</strong> — Implementing a simple data visualization task (plotting a graph)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 26.956 ms | 0.000 ms | 0.000 ms | 26.956 ms → 26.956 ms | 1.1053 s | 0.000 ms | 0.000 ms | 1.1053 s → 1.1053 s | 14.152 MB | 0.000 MB | 0.000 MB | 14.152 MB → 14.152 MB | 5 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 26.705 ms | 0.000 ms | 0.000 ms | 26.705 ms → 26.705 ms | 1.0745 s | 0.000 ms | 0.000 ms | 1.0745 s → 1.0745 s | 13.750 MB | 0.000 MB | 0.000 MB | 13.750 MB → 13.750 MB | 5 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 26.623 ms | 0.000 ms | 0.000 ms | 26.623 ms → 26.623 ms | 1.1246 s | 0.000 ms | 0.000 ms | 1.1246 s → 1.1246 s | 13.902 MB | 0.000 MB | 0.000 MB | 13.902 MB → 13.902 MB | 5 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 27.171 ms | 0.000 ms | 0.000 ms | 27.171 ms → 27.171 ms | 1.0480 s | 0.000 ms | 0.000 ms | 1.0480 s → 1.0480 s | 15.012 MB | 0.000 MB | 0.000 MB | 15.012 MB → 15.012 MB | 5 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 28.370 ms | 0.000 ms | 0.000 ms | 28.370 ms → 28.370 ms | 1.0214 s | 0.000 ms | 0.000 ms | 1.0214 s → 1.0214 s | 15.211 MB | 0.000 MB | 0.000 MB | 15.211 MB → 15.211 MB | 5 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 27.208 ms | 0.000 ms | 0.000 ms | 27.208 ms → 27.208 ms | 1.0042 s | 0.000 ms | 0.000 ms | 1.0042 s → 1.0042 s | 15.648 MB | 0.000 MB | 0.000 MB | 15.648 MB → 15.648 MB | 5 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 26.578 ms | 0.000 ms | 0.000 ms | 26.578 ms → 26.578 ms | 1.0697 s | 0.000 ms | 0.000 ms | 1.0697 s → 1.0697 s | 17.203 MB | 0.000 MB | 0.000 MB | 17.203 MB → 17.203 MB | 5 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 26.934 ms | 0.000 ms | 0.000 ms | 26.934 ms → 26.934 ms | 1.0793 s | 0.000 ms | 0.000 ms | 1.0793 s → 1.0793 s | 15.543 MB | 0.000 MB | 0.000 MB | 15.543 MB → 15.543 MB | 5 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 26.807 ms | 0.000 ms | 0.000 ms | 26.807 ms → 26.807 ms | 1.1033 s | 0.000 ms | 0.000 ms | 1.1033 s → 1.1033 s | 15.648 MB | 0.000 MB | 0.000 MB | 15.648 MB → 15.648 MB | 5 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 27.058 ms | 0.000 ms | 0.000 ms | 27.058 ms → 27.058 ms | 1.1431 s | 0.000 ms | 0.000 ms | 1.1431 s → 1.1431 s | 16.754 MB | 0.000 MB | 0.000 MB | 16.754 MB → 16.754 MB | 5 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 27.530 ms | 0.000 ms | 0.000 ms | 27.530 ms → 27.530 ms | 1.1881 s | 0.000 ms | 0.000 ms | 1.1881 s → 1.1881 s | 16.918 MB | 0.000 MB | 0.000 MB | 16.918 MB → 16.918 MB | 5 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 28.701 ms | 0.000 ms | 0.000 ms | 28.701 ms → 28.701 ms | 1.1543 s | 0.000 ms | 0.000 ms | 1.1543 s → 1.1543 s | 16.477 MB | 0.000 MB | 0.000 MB | 16.477 MB → 16.477 MB | 5 |
| Python 2.7 [x86_64] | Python | S | 1 | 27.448 ms | 0.000 ms | 0.000 ms | 27.448 ms → 27.448 ms | 1.3450 s | 0.000 ms | 0.000 ms | 1.3450 s → 1.3450 s | 18.094 MB | 0.000 MB | 0.000 MB | 18.094 MB → 18.094 MB | 3 |
| Python 2.7 [x86_64] | Python | M | 1 | 29.422 ms | 0.000 ms | 0.000 ms | 29.422 ms → 29.422 ms | 1.0872 s | 0.000 ms | 0.000 ms | 1.0872 s → 1.0872 s | 17.848 MB | 0.000 MB | 0.000 MB | 17.848 MB → 17.848 MB | 3 |
| Python 2.7 [x86_64] | Python | L | 1 | 27.431 ms | 0.000 ms | 0.000 ms | 27.431 ms → 27.431 ms | 1.0800 s | 0.000 ms | 0.000 ms | 1.0800 s → 1.0800 s | 17.883 MB | 0.000 MB | 0.000 MB | 17.883 MB → 17.883 MB | 3 |
| Python 3.8 [x86_64] | Python | S | 1 | 27.753 ms | 0.000 ms | 0.000 ms | 27.753 ms → 27.753 ms | 1.3255 s | 0.000 ms | 0.000 ms | 1.3255 s → 1.3255 s | 22.230 MB | 0.000 MB | 0.000 MB | 22.230 MB → 22.230 MB | 3 |
| Python 3.8 [x86_64] | Python | M | 1 | 27.678 ms | 0.000 ms | 0.000 ms | 27.678 ms → 27.678 ms | 1.3995 s | 0.000 ms | 0.000 ms | 1.3995 s → 1.3995 s | 21.852 MB | 0.000 MB | 0.000 MB | 21.852 MB → 21.852 MB | 3 |
| Python 3.8 [x86_64] | Python | L | 1 | 27.028 ms | 0.000 ms | 0.000 ms | 27.028 ms → 27.028 ms | 1.3281 s | 0.000 ms | 0.000 ms | 1.3281 s → 1.3281 s | 22.031 MB | 0.000 MB | 0.000 MB | 22.031 MB → 22.031 MB | 3 |
| Python 3.11 [x86_64] | Python | S | 1 | 28.632 ms | 0.000 ms | 0.000 ms | 28.632 ms → 28.632 ms | 1.2885 s | 0.000 ms | 0.000 ms | 1.2885 s → 1.2885 s | 25.473 MB | 0.000 MB | 0.000 MB | 25.473 MB → 25.473 MB | 3 |
| Python 3.11 [x86_64] | Python | M | 1 | 26.907 ms | 0.000 ms | 0.000 ms | 26.907 ms → 26.907 ms | 1.3150 s | 0.000 ms | 0.000 ms | 1.3150 s → 1.3150 s | 25.555 MB | 0.000 MB | 0.000 MB | 25.555 MB → 25.555 MB | 3 |
| Python 3.11 [x86_64] | Python | L | 1 | 28.688 ms | 0.000 ms | 0.000 ms | 28.688 ms → 28.688 ms | 1.4640 s | 0.000 ms | 0.000 ms | 1.4640 s → 1.4640 s | 27.254 MB | 0.000 MB | 0.000 MB | 27.254 MB → 27.254 MB | 3 |
| Python 3.12 [x86_64] | Python | S | 1 | 28.080 ms | 0.000 ms | 0.000 ms | 28.080 ms → 28.080 ms | 1.3801 s | 0.000 ms | 0.000 ms | 1.3801 s → 1.3801 s | 25.633 MB | 0.000 MB | 0.000 MB | 25.633 MB → 25.633 MB | 3 |
| Python 3.12 [x86_64] | Python | M | 1 | 29.355 ms | 0.000 ms | 0.000 ms | 29.355 ms → 29.355 ms | 1.4334 s | 0.000 ms | 0.000 ms | 1.4334 s → 1.4334 s | 26.664 MB | 0.000 MB | 0.000 MB | 26.664 MB → 26.664 MB | 3 |
| Python 3.12 [x86_64] | Python | L | 1 | 28.944 ms | 0.000 ms | 0.000 ms | 28.944 ms → 28.944 ms | 1.2913 s | 0.000 ms | 0.000 ms | 1.2913 s → 1.2913 s | 27.508 MB | 0.000 MB | 0.000 MB | 27.508 MB → 27.508 MB | 3 |
| Java 21 [x86_64] | Java | S | 1 | 39.388 ms | 0.000 ms | 0.000 ms | 39.388 ms → 39.388 ms | 1.3203 s | 0.000 ms | 0.000 ms | 1.3203 s → 1.3203 s | 39.285 MB | 0.000 MB | 0.000 MB | 39.285 MB → 39.285 MB | 5 |
| Java 21 [x86_64] | Java | M | 1 | 39.145 ms | 0.000 ms | 0.000 ms | 39.145 ms → 39.145 ms | 1.2723 s | 0.000 ms | 0.000 ms | 1.2723 s → 1.2723 s | 41.113 MB | 0.000 MB | 0.000 MB | 41.113 MB → 41.113 MB | 5 |
| Java 21 [x86_64] | Java | L | 1 | 37.152 ms | 0.000 ms | 0.000 ms | 37.152 ms → 37.152 ms | 1.3134 s | 0.000 ms | 0.000 ms | 1.3134 s → 1.3134 s | 40.852 MB | 0.000 MB | 0.000 MB | 40.852 MB → 40.852 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 26.905 ms | 0.000 ms | 0.000 ms | 26.905 ms → 26.905 ms | 957.638 ms | 0.000 ms | 0.000 ms | 957.638 ms → 957.638 ms | 11.098 MB | 0.000 MB | 0.000 MB | 11.098 MB → 11.098 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 26.385 ms | 0.000 ms | 0.000 ms | 26.385 ms → 26.385 ms | 979.564 ms | 0.000 ms | 0.000 ms | 979.564 ms → 979.564 ms | 9.625 MB | 0.000 MB | 0.000 MB | 9.625 MB → 9.625 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 28.208 ms | 0.000 ms | 0.000 ms | 28.208 ms → 28.208 ms | 1.0335 s | 0.000 ms | 0.000 ms | 1.0335 s → 1.0335 s | 9.566 MB | 0.000 MB | 0.000 MB | 9.566 MB → 9.566 MB | 5 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 29.425 ms | 0.000 ms | 0.000 ms | 29.425 ms → 29.425 ms | 1.2012 s | 0.000 ms | 0.000 ms | 1.2012 s → 1.2012 s | 18.457 MB | 0.000 MB | 0.000 MB | 18.457 MB → 18.457 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 28.551 ms | 0.000 ms | 0.000 ms | 28.551 ms → 28.551 ms | 1.1869 s | 0.000 ms | 0.000 ms | 1.1869 s → 1.1869 s | 18.070 MB | 0.000 MB | 0.000 MB | 18.070 MB → 18.070 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 29.589 ms | 0.000 ms | 0.000 ms | 29.589 ms → 29.589 ms | 1.1564 s | 0.000 ms | 0.000 ms | 1.1564 s → 1.1564 s | 18.414 MB | 0.000 MB | 0.000 MB | 18.414 MB → 18.414 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 30.566 ms | 0.000 ms | 0.000 ms | 30.566 ms → 30.566 ms | 1.0932 s | 0.000 ms | 0.000 ms | 1.0932 s → 1.0932 s | 22.418 MB | 0.000 MB | 0.000 MB | 22.418 MB → 22.418 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 30.708 ms | 0.000 ms | 0.000 ms | 30.708 ms → 30.708 ms | 1.0719 s | 0.000 ms | 0.000 ms | 1.0719 s → 1.0719 s | 20.023 MB | 0.000 MB | 0.000 MB | 20.023 MB → 20.023 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 31.068 ms | 0.000 ms | 0.000 ms | 31.068 ms → 31.068 ms | 1.1303 s | 0.000 ms | 0.000 ms | 1.1303 s → 1.1303 s | 19.699 MB | 0.000 MB | 0.000 MB | 19.699 MB → 19.699 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 68.658 ms | 0.000 ms | 0.000 ms | 68.658 ms → 68.658 ms | 1.0797 s | 0.000 ms | 0.000 ms | 1.0797 s → 1.0797 s | 30.598 MB | 0.000 MB | 0.000 MB | 30.598 MB → 30.598 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 75.502 ms | 0.000 ms | 0.000 ms | 75.502 ms → 75.502 ms | 1.0818 s | 0.000 ms | 0.000 ms | 1.0818 s → 1.0818 s | 28.340 MB | 0.000 MB | 0.000 MB | 28.340 MB → 28.340 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 67.370 ms | 0.000 ms | 0.000 ms | 67.370 ms → 67.370 ms | 1.0705 s | 0.000 ms | 0.000 ms | 1.0705 s → 1.0705 s | 31.754 MB | 0.000 MB | 0.000 MB | 31.754 MB → 31.754 MB | 4 |
| Go 1.23 [x86_64] | Go | S | 1 | 28.602 ms | 0.000 ms | 0.000 ms | 28.602 ms → 28.602 ms | 1.1228 s | 0.000 ms | 0.000 ms | 1.1228 s → 1.1228 s | 11.844 MB | 0.000 MB | 0.000 MB | 11.844 MB → 11.844 MB | 4 |
| Go 1.23 [x86_64] | Go | M | 1 | 27.763 ms | 0.000 ms | 0.000 ms | 27.763 ms → 27.763 ms | 996.642 ms | 0.000 ms | 0.000 ms | 996.642 ms → 996.642 ms | 12.363 MB | 0.000 MB | 0.000 MB | 12.363 MB → 12.363 MB | 4 |
| Go 1.23 [x86_64] | Go | L | 1 | 31.479 ms | 0.000 ms | 0.000 ms | 31.479 ms → 31.479 ms | 1.1765 s | 0.000 ms | 0.000 ms | 1.1765 s → 1.1765 s | 11.875 MB | 0.000 MB | 0.000 MB | 11.875 MB → 11.875 MB | 4 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 26.033 ms | 0.000 ms | 0.000 ms | 26.033 ms → 26.033 ms | 970.503 ms | 0.000 ms | 0.000 ms | 970.503 ms → 970.503 ms | 11.820 MB | 0.000 MB | 0.000 MB | 11.820 MB → 11.820 MB | 3 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 26.700 ms | 0.000 ms | 0.000 ms | 26.700 ms → 26.700 ms | 974.235 ms | 0.000 ms | 0.000 ms | 974.235 ms → 974.235 ms | 9.543 MB | 0.000 MB | 0.000 MB | 9.543 MB → 9.543 MB | 3 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 25.878 ms | 0.000 ms | 0.000 ms | 25.878 ms → 25.878 ms | 982.894 ms | 0.000 ms | 0.000 ms | 982.894 ms → 982.894 ms | 9.043 MB | 0.000 MB | 0.000 MB | 9.043 MB → 9.043 MB | 3 |

</details>

<details>
<summary><strong>decision_tree</strong> — Implementing a basic machine learning model (decision tree)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 31.111 ms | 0.000 ms | 0.000 ms | 31.111 ms → 31.111 ms | 22.164 MB | 0.000 MB | 0.000 MB | 22.164 MB → 22.164 MB | 70 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 210.000 ms | 0.000 ms | 0.000 ms | 210.000 ms → 210.000 ms | 215.000 ms | 0.000 ms | 0.000 ms | 215.000 ms → 215.000 ms | 31.605 MB | 0.000 MB | 0.000 MB | 31.605 MB → 31.605 MB | 70 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 910.000 ms | 0.000 ms | 0.000 ms | 910.000 ms → 910.000 ms | 930.000 ms | 0.000 ms | 0.000 ms | 930.000 ms → 930.000 ms | 43.242 MB | 0.000 MB | 0.000 MB | 43.242 MB → 43.242 MB | 70 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 22.711 MB | 0.000 MB | 0.000 MB | 22.711 MB → 22.711 MB | 66 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 26.852 MB | 0.000 MB | 0.000 MB | 26.852 MB → 26.852 MB | 66 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 32.832 MB | 0.000 MB | 0.000 MB | 32.832 MB → 32.832 MB | 66 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 20.769 ms | 0.000 ms | 0.000 ms | 20.769 ms → 20.769 ms | 24.191 MB | 0.000 MB | 0.000 MB | 24.191 MB → 24.191 MB | 66 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 28.336 MB | 0.000 MB | 0.000 MB | 28.336 MB → 28.336 MB | 66 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 34.062 MB | 0.000 MB | 0.000 MB | 34.062 MB → 34.062 MB | 66 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 19.231 ms | 0.000 ms | 0.000 ms | 19.231 ms → 19.231 ms | 25.406 MB | 0.000 MB | 0.000 MB | 25.406 MB → 25.406 MB | 66 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 27.555 MB | 0.000 MB | 0.000 MB | 27.555 MB → 27.555 MB | 66 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 31.488 MB | 0.000 MB | 0.000 MB | 31.488 MB → 31.488 MB | 66 |
| Python 2.7 [x86_64] | Python | S | 1 | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 32.000 ms | 0.000 ms | 0.000 ms | 32.000 ms → 32.000 ms | 7.996 MB | 0.000 MB | 0.000 MB | 7.996 MB → 7.996 MB | 64 |
| Python 2.7 [x86_64] | Python | M | 1 | 93.333 ms | 0.000 ms | 0.000 ms | 93.333 ms → 93.333 ms | 93.333 ms | 0.000 ms | 0.000 ms | 93.333 ms → 93.333 ms | 8.828 MB | 0.000 MB | 0.000 MB | 8.828 MB → 8.828 MB | 64 |
| Python 2.7 [x86_64] | Python | L | 1 | 160.000 ms | 0.000 ms | 0.000 ms | 160.000 ms → 160.000 ms | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 10.652 MB | 0.000 MB | 0.000 MB | 10.652 MB → 10.652 MB | 64 |
| Python 3.8 [x86_64] | Python | S | 1 | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 10.957 MB | 0.000 MB | 0.000 MB | 10.957 MB → 10.957 MB | 55 |
| Python 3.8 [x86_64] | Python | M | 1 | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 125.000 ms | 0.000 ms | 0.000 ms | 125.000 ms → 125.000 ms | 11.152 MB | 0.000 MB | 0.000 MB | 11.152 MB → 11.152 MB | 55 |
| Python 3.8 [x86_64] | Python | L | 1 | 190.000 ms | 0.000 ms | 0.000 ms | 190.000 ms → 190.000 ms | 195.000 ms | 0.000 ms | 0.000 ms | 195.000 ms → 195.000 ms | 12.590 MB | 0.000 MB | 0.000 MB | 12.590 MB → 12.590 MB | 55 |
| Python 3.11 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 13.758 MB | 0.000 MB | 0.000 MB | 13.758 MB → 13.758 MB | 55 |
| Python 3.11 [x86_64] | Python | M | 1 | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 105.000 ms | 0.000 ms | 0.000 ms | 105.000 ms → 105.000 ms | 14.766 MB | 0.000 MB | 0.000 MB | 14.766 MB → 14.766 MB | 55 |
| Python 3.11 [x86_64] | Python | L | 1 | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 16.102 MB | 0.000 MB | 0.000 MB | 16.102 MB → 16.102 MB | 55 |
| Python 3.12 [x86_64] | Python | S | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 14.930 MB | 0.000 MB | 0.000 MB | 14.930 MB → 14.930 MB | 55 |
| Python 3.12 [x86_64] | Python | M | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 15.445 MB | 0.000 MB | 0.000 MB | 15.445 MB → 15.445 MB | 55 |
| Python 3.12 [x86_64] | Python | L | 1 | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 17.258 MB | 0.000 MB | 0.000 MB | 17.258 MB → 17.258 MB | 55 |
| Java 21 [x86_64] | Java | S | 1 | 290.000 ms | 0.000 ms | 0.000 ms | 290.000 ms → 290.000 ms | 270.000 ms | 0.000 ms | 0.000 ms | 270.000 ms → 270.000 ms | 48.656 MB | 0.000 MB | 0.000 MB | 48.656 MB → 48.656 MB | 84 |
| Java 21 [x86_64] | Java | M | 1 | 340.000 ms | 0.000 ms | 0.000 ms | 340.000 ms → 340.000 ms | 340.000 ms | 0.000 ms | 0.000 ms | 340.000 ms → 340.000 ms | 51.070 MB | 0.000 MB | 0.000 MB | 51.070 MB → 51.070 MB | 84 |
| Java 21 [x86_64] | Java | L | 1 | 500.000 ms | 0.000 ms | 0.000 ms | 500.000 ms → 500.000 ms | 470.000 ms | 0.000 ms | 0.000 ms | 470.000 ms → 470.000 ms | 54.625 MB | 0.000 MB | 0.000 MB | 54.625 MB → 54.625 MB | 84 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 4.227 MB | 0.000 MB | 0.000 MB | 4.227 MB → 4.227 MB | 82 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 58.000 ms | 0.000 ms | 0.000 ms | 58.000 ms → 58.000 ms | 5.637 MB | 0.000 MB | 0.000 MB | 5.637 MB → 5.637 MB | 82 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 116.667 ms | 0.000 ms | 0.000 ms | 116.667 ms → 116.667 ms | 116.667 ms | 0.000 ms | 0.000 ms | 116.667 ms → 116.667 ms | 7.340 MB | 0.000 MB | 0.000 MB | 7.340 MB → 7.340 MB | 82 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 56.816 MB | 0.000 MB | 0.000 MB | 56.816 MB → 56.816 MB | 58 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 116.667 ms | 0.000 ms | 0.000 ms | 116.667 ms → 116.667 ms | 64.449 MB | 0.000 MB | 0.000 MB | 64.449 MB → 64.449 MB | 58 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 136.667 ms | 0.000 ms | 0.000 ms | 136.667 ms → 136.667 ms | 67.328 MB | 0.000 MB | 0.000 MB | 67.328 MB → 67.328 MB | 58 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 47.143 ms | 0.000 ms | 0.000 ms | 47.143 ms → 47.143 ms | 44.286 ms | 0.000 ms | 0.000 ms | 44.286 ms → 44.286 ms | 47.289 MB | 0.000 MB | 0.000 MB | 47.289 MB → 47.289 MB | 58 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 64.000 ms | 0.000 ms | 0.000 ms | 64.000 ms → 64.000 ms | 64.000 ms | 0.000 ms | 0.000 ms | 64.000 ms → 64.000 ms | 58.086 MB | 0.000 MB | 0.000 MB | 58.086 MB → 58.086 MB | 58 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 86.667 ms | 0.000 ms | 0.000 ms | 86.667 ms → 86.667 ms | 76.667 ms | 0.000 ms | 0.000 ms | 76.667 ms → 76.667 ms | 65.289 MB | 0.000 MB | 0.000 MB | 65.289 MB → 65.289 MB | 58 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 74.332 MB | 0.000 MB | 0.000 MB | 74.332 MB → 74.332 MB | 58 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 136.667 ms | 0.000 ms | 0.000 ms | 136.667 ms → 136.667 ms | 130.000 ms | 0.000 ms | 0.000 ms | 130.000 ms → 130.000 ms | 87.797 MB | 0.000 MB | 0.000 MB | 87.797 MB → 87.797 MB | 58 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 90.488 MB | 0.000 MB | 0.000 MB | 90.488 MB → 90.488 MB | 58 |
| Go 1.23 [x86_64] | Go | S | 1 | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.590 MB | 0.000 MB | 0.000 MB | 14.590 MB → 14.590 MB | 88 |
| Go 1.23 [x86_64] | Go | M | 1 | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 14.242 MB | 0.000 MB | 0.000 MB | 14.242 MB → 14.242 MB | 88 |
| Go 1.23 [x86_64] | Go | L | 1 | 450.000 ms | 0.000 ms | 0.000 ms | 450.000 ms → 450.000 ms | 430.000 ms | 0.000 ms | 0.000 ms | 430.000 ms → 430.000 ms | 15.852 MB | 0.000 MB | 0.000 MB | 15.852 MB → 15.852 MB | 88 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 3.880 ms | 0.000 ms | 0.000 ms | 3.880 ms → 3.880 ms | 3.960 ms | 0.000 ms | 0.000 ms | 3.960 ms → 3.960 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 69 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 5.070 MB | 0.000 MB | 0.000 MB | 5.070 MB → 5.070 MB | 69 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 25.556 ms | 0.000 ms | 0.000 ms | 25.556 ms → 25.556 ms | 26.667 ms | 0.000 ms | 0.000 ms | 26.667 ms → 26.667 ms | 7.730 MB | 0.000 MB | 0.000 MB | 7.730 MB → 7.730 MB | 69 |

</details>

<details>
<summary><strong>file_io_large</strong> — Performing file I/O operations on a large file</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 20.812 MB | 0.000 MB | 0.000 MB | 20.812 MB → 20.812 MB | 12 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 20.820 MB | 0.000 MB | 0.000 MB | 20.820 MB → 20.820 MB | 12 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 20.617 MB | 0.000 MB | 0.000 MB | 20.617 MB → 20.617 MB | 12 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 13.077 ms | 0.000 ms | 0.000 ms | 13.077 ms → 13.077 ms | 13.846 ms | 0.000 ms | 0.000 ms | 13.846 ms → 13.846 ms | 22.734 MB | 0.000 MB | 0.000 MB | 22.734 MB → 22.734 MB | 11 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 22.660 MB | 0.000 MB | 0.000 MB | 22.660 MB → 22.660 MB | 11 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 22.308 ms | 0.000 ms | 0.000 ms | 22.308 ms → 22.308 ms | 22.777 MB | 0.000 MB | 0.000 MB | 22.777 MB → 22.777 MB | 11 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 23.863 MB | 0.000 MB | 0.000 MB | 23.863 MB → 23.863 MB | 11 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 20.769 ms | 0.000 ms | 0.000 ms | 20.769 ms → 20.769 ms | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 24.039 MB | 0.000 MB | 0.000 MB | 24.039 MB → 24.039 MB | 11 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 25.556 ms | 0.000 ms | 0.000 ms | 25.556 ms → 25.556 ms | 25.556 ms | 0.000 ms | 0.000 ms | 25.556 ms → 25.556 ms | 24.102 MB | 0.000 MB | 0.000 MB | 24.102 MB → 24.102 MB | 11 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 15.600 ms | 0.000 ms | 0.000 ms | 15.600 ms → 15.600 ms | 25.430 MB | 0.000 MB | 0.000 MB | 25.430 MB → 25.430 MB | 11 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 19.231 ms | 0.000 ms | 0.000 ms | 19.231 ms → 19.231 ms | 25.434 MB | 0.000 MB | 0.000 MB | 25.434 MB → 25.434 MB | 11 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 23.077 ms | 0.000 ms | 0.000 ms | 23.077 ms → 23.077 ms | 23.846 ms | 0.000 ms | 0.000 ms | 23.846 ms → 23.846 ms | 25.355 MB | 0.000 MB | 0.000 MB | 25.355 MB → 25.355 MB | 11 |
| Python 2.7 [x86_64] | Python | S | 1 | 17.143 ms | 0.000 ms | 0.000 ms | 17.143 ms → 17.143 ms | 18.571 ms | 0.000 ms | 0.000 ms | 18.571 ms → 18.571 ms | 7.832 MB | 0.000 MB | 0.000 MB | 7.832 MB → 7.832 MB | 11 |
| Python 2.7 [x86_64] | Python | M | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 7.941 MB | 0.000 MB | 0.000 MB | 7.941 MB → 7.941 MB | 11 |
| Python 2.7 [x86_64] | Python | L | 1 | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 7.949 MB | 0.000 MB | 0.000 MB | 7.949 MB → 7.949 MB | 11 |
| Python 3.8 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 10.625 MB | 0.000 MB | 0.000 MB | 10.625 MB → 10.625 MB | 8 |
| Python 3.8 [x86_64] | Python | M | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 10.812 MB | 0.000 MB | 0.000 MB | 10.812 MB → 10.812 MB | 8 |
| Python 3.8 [x86_64] | Python | L | 1 | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 11.016 MB | 0.000 MB | 0.000 MB | 11.016 MB → 11.016 MB | 8 |
| Python 3.11 [x86_64] | Python | S | 1 | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 13.539 MB | 0.000 MB | 0.000 MB | 13.539 MB → 13.539 MB | 8 |
| Python 3.11 [x86_64] | Python | M | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 13.605 MB | 0.000 MB | 0.000 MB | 13.605 MB → 13.605 MB | 8 |
| Python 3.11 [x86_64] | Python | L | 1 | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 13.648 MB | 0.000 MB | 0.000 MB | 13.648 MB → 13.648 MB | 8 |
| Python 3.12 [x86_64] | Python | S | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.906 MB | 0.000 MB | 0.000 MB | 14.906 MB → 14.906 MB | 8 |
| Python 3.12 [x86_64] | Python | M | 1 | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 14.934 MB | 0.000 MB | 0.000 MB | 14.934 MB → 14.934 MB | 8 |
| Python 3.12 [x86_64] | Python | L | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 14.879 MB | 0.000 MB | 0.000 MB | 14.879 MB → 14.879 MB | 8 |
| Java 21 [x86_64] | Java | S | 1 | 146.667 ms | 0.000 ms | 0.000 ms | 146.667 ms → 146.667 ms | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 45.441 MB | 0.000 MB | 0.000 MB | 45.441 MB → 45.441 MB | 10 |
| Java 21 [x86_64] | Java | M | 1 | 275.000 ms | 0.000 ms | 0.000 ms | 275.000 ms → 275.000 ms | 265.000 ms | 0.000 ms | 0.000 ms | 265.000 ms → 265.000 ms | 49.719 MB | 0.000 MB | 0.000 MB | 49.719 MB → 49.719 MB | 10 |
| Java 21 [x86_64] | Java | L | 1 | 230.000 ms | 0.000 ms | 0.000 ms | 230.000 ms → 230.000 ms | 200.000 ms | 0.000 ms | 0.000 ms | 200.000 ms → 200.000 ms | 50.742 MB | 0.000 MB | 0.000 MB | 50.742 MB → 50.742 MB | 10 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 2.160 ms | 0.000 ms | 0.000 ms | 2.160 ms → 2.160 ms | 2.200 ms | 0.000 ms | 0.000 ms | 2.200 ms → 2.200 ms | 3.680 MB | 0.000 MB | 0.000 MB | 3.680 MB → 3.680 MB | 10 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 4.320 ms | 0.000 ms | 0.000 ms | 4.320 ms → 4.320 ms | 4.400 ms | 0.000 ms | 0.000 ms | 4.400 ms → 4.400 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 10 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 7.692 ms | 0.000 ms | 0.000 ms | 7.692 ms → 7.692 ms | 7.692 ms | 0.000 ms | 0.000 ms | 7.692 ms → 7.692 ms | 3.645 MB | 0.000 MB | 0.000 MB | 3.645 MB → 3.645 MB | 10 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 47.301 MB | 0.000 MB | 0.000 MB | 47.301 MB → 47.301 MB | 9 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 57.090 MB | 0.000 MB | 0.000 MB | 57.090 MB → 57.090 MB | 9 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 62.199 MB | 0.000 MB | 0.000 MB | 62.199 MB → 62.199 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 44.469 MB | 0.000 MB | 0.000 MB | 44.469 MB → 44.469 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 42.857 ms | 0.000 ms | 0.000 ms | 42.857 ms → 42.857 ms | 42.857 ms | 0.000 ms | 0.000 ms | 42.857 ms → 42.857 ms | 48.219 MB | 0.000 MB | 0.000 MB | 48.219 MB → 48.219 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 53.363 MB | 0.000 MB | 0.000 MB | 53.363 MB → 53.363 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 74.059 MB | 0.000 MB | 0.000 MB | 74.059 MB → 74.059 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 81.305 MB | 0.000 MB | 0.000 MB | 81.305 MB → 81.305 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 87.500 ms | 0.000 ms | 0.000 ms | 87.500 ms → 87.500 ms | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 86.590 MB | 0.000 MB | 0.000 MB | 86.590 MB → 86.590 MB | 9 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.880 ms | 0.000 ms | 0.000 ms | 2.880 ms → 2.880 ms | 2.920 ms | 0.000 ms | 0.000 ms | 2.920 ms → 2.920 ms | 7.547 MB | 0.000 MB | 0.000 MB | 7.547 MB → 7.547 MB | 19 |
| Go 1.23 [x86_64] | Go | M | 1 | 4.440 ms | 0.000 ms | 0.000 ms | 4.440 ms → 4.440 ms | 4.480 ms | 0.000 ms | 0.000 ms | 4.480 ms → 4.480 ms | 7.551 MB | 0.000 MB | 0.000 MB | 7.551 MB → 7.551 MB | 19 |
| Go 1.23 [x86_64] | Go | L | 1 | 6.240 ms | 0.000 ms | 0.000 ms | 6.240 ms → 6.240 ms | 6.280 ms | 0.000 ms | 0.000 ms | 6.280 ms → 6.280 ms | 7.547 MB | 0.000 MB | 0.000 MB | 7.547 MB → 7.547 MB | 19 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.840 ms | 0.000 ms | 0.000 ms | 1.840 ms → 1.840 ms | 1.880 ms | 0.000 ms | 0.000 ms | 1.880 ms → 1.880 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 11 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 3.960 ms | 0.000 ms | 0.000 ms | 3.960 ms → 3.960 ms | 4.040 ms | 0.000 ms | 0.000 ms | 4.040 ms → 4.040 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 11 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 6.560 ms | 0.000 ms | 0.000 ms | 6.560 ms → 6.560 ms | 6.640 ms | 0.000 ms | 0.000 ms | 6.640 ms → 6.640 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 11 |

</details>

<details>
<summary><strong>gui_calculator</strong> — Implementing a simple GUI application (a calculator)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 28.330 ms | 0.000 ms | 0.000 ms | 28.330 ms → 28.330 ms | 1.1582 s | 0.000 ms | 0.000 ms | 1.1582 s → 1.1582 s | 13.859 MB | 0.000 MB | 0.000 MB | 13.859 MB → 13.859 MB | 5 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 26.480 ms | 0.000 ms | 0.000 ms | 26.480 ms → 26.480 ms | 1.0316 s | 0.000 ms | 0.000 ms | 1.0316 s → 1.0316 s | 14.109 MB | 0.000 MB | 0.000 MB | 14.109 MB → 14.109 MB | 5 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 27.073 ms | 0.000 ms | 0.000 ms | 27.073 ms → 27.073 ms | 1.1418 s | 0.000 ms | 0.000 ms | 1.1418 s → 1.1418 s | 13.605 MB | 0.000 MB | 0.000 MB | 13.605 MB → 13.605 MB | 5 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 27.306 ms | 0.000 ms | 0.000 ms | 27.306 ms → 27.306 ms | 1.0317 s | 0.000 ms | 0.000 ms | 1.0317 s → 1.0317 s | 15.570 MB | 0.000 MB | 0.000 MB | 15.570 MB → 15.570 MB | 5 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 26.293 ms | 0.000 ms | 0.000 ms | 26.293 ms → 26.293 ms | 1.0131 s | 0.000 ms | 0.000 ms | 1.0131 s → 1.0131 s | 15.457 MB | 0.000 MB | 0.000 MB | 15.457 MB → 15.457 MB | 5 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 28.425 ms | 0.000 ms | 0.000 ms | 28.425 ms → 28.425 ms | 1.0254 s | 0.000 ms | 0.000 ms | 1.0254 s → 1.0254 s | 16.609 MB | 0.000 MB | 0.000 MB | 16.609 MB → 16.609 MB | 5 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 26.305 ms | 0.000 ms | 0.000 ms | 26.305 ms → 26.305 ms | 1.1208 s | 0.000 ms | 0.000 ms | 1.1208 s → 1.1208 s | 17.285 MB | 0.000 MB | 0.000 MB | 17.285 MB → 17.285 MB | 5 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 27.919 ms | 0.000 ms | 0.000 ms | 27.919 ms → 27.919 ms | 1.1303 s | 0.000 ms | 0.000 ms | 1.1303 s → 1.1303 s | 15.613 MB | 0.000 MB | 0.000 MB | 15.613 MB → 15.613 MB | 5 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 26.661 ms | 0.000 ms | 0.000 ms | 26.661 ms → 26.661 ms | 1.1734 s | 0.000 ms | 0.000 ms | 1.1734 s → 1.1734 s | 15.238 MB | 0.000 MB | 0.000 MB | 15.238 MB → 15.238 MB | 5 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 26.897 ms | 0.000 ms | 0.000 ms | 26.897 ms → 26.897 ms | 1.0654 s | 0.000 ms | 0.000 ms | 1.0654 s → 1.0654 s | 16.641 MB | 0.000 MB | 0.000 MB | 16.641 MB → 16.641 MB | 5 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 27.655 ms | 0.000 ms | 0.000 ms | 27.655 ms → 27.655 ms | 1.1543 s | 0.000 ms | 0.000 ms | 1.1543 s → 1.1543 s | 18.684 MB | 0.000 MB | 0.000 MB | 18.684 MB → 18.684 MB | 5 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 26.893 ms | 0.000 ms | 0.000 ms | 26.893 ms → 26.893 ms | 1.1345 s | 0.000 ms | 0.000 ms | 1.1345 s → 1.1345 s | 16.852 MB | 0.000 MB | 0.000 MB | 16.852 MB → 16.852 MB | 5 |
| Python 2.7 [x86_64] | Python | S | 1 | 27.762 ms | 0.000 ms | 0.000 ms | 27.762 ms → 27.762 ms | 1.1639 s | 0.000 ms | 0.000 ms | 1.1639 s → 1.1639 s | 17.875 MB | 0.000 MB | 0.000 MB | 17.875 MB → 17.875 MB | 3 |
| Python 2.7 [x86_64] | Python | M | 1 | 28.347 ms | 0.000 ms | 0.000 ms | 28.347 ms → 28.347 ms | 1.1342 s | 0.000 ms | 0.000 ms | 1.1342 s → 1.1342 s | 17.586 MB | 0.000 MB | 0.000 MB | 17.586 MB → 17.586 MB | 3 |
| Python 2.7 [x86_64] | Python | L | 1 | 27.576 ms | 0.000 ms | 0.000 ms | 27.576 ms → 27.576 ms | 1.1386 s | 0.000 ms | 0.000 ms | 1.1386 s → 1.1386 s | 19.320 MB | 0.000 MB | 0.000 MB | 19.320 MB → 19.320 MB | 3 |
| Python 3.8 [x86_64] | Python | S | 1 | 29.902 ms | 0.000 ms | 0.000 ms | 29.902 ms → 29.902 ms | 1.3658 s | 0.000 ms | 0.000 ms | 1.3658 s → 1.3658 s | 21.523 MB | 0.000 MB | 0.000 MB | 21.523 MB → 21.523 MB | 3 |
| Python 3.8 [x86_64] | Python | M | 1 | 26.958 ms | 0.000 ms | 0.000 ms | 26.958 ms → 26.958 ms | 1.3480 s | 0.000 ms | 0.000 ms | 1.3480 s → 1.3480 s | 21.961 MB | 0.000 MB | 0.000 MB | 21.961 MB → 21.961 MB | 3 |
| Python 3.8 [x86_64] | Python | L | 1 | 28.372 ms | 0.000 ms | 0.000 ms | 28.372 ms → 28.372 ms | 1.3931 s | 0.000 ms | 0.000 ms | 1.3931 s → 1.3931 s | 22.012 MB | 0.000 MB | 0.000 MB | 22.012 MB → 22.012 MB | 3 |
| Python 3.11 [x86_64] | Python | S | 1 | 27.110 ms | 0.000 ms | 0.000 ms | 27.110 ms → 27.110 ms | 1.3900 s | 0.000 ms | 0.000 ms | 1.3900 s → 1.3900 s | 25.266 MB | 0.000 MB | 0.000 MB | 25.266 MB → 25.266 MB | 3 |
| Python 3.11 [x86_64] | Python | M | 1 | 29.137 ms | 0.000 ms | 0.000 ms | 29.137 ms → 29.137 ms | 1.3938 s | 0.000 ms | 0.000 ms | 1.3938 s → 1.3938 s | 25.395 MB | 0.000 MB | 0.000 MB | 25.395 MB → 25.395 MB | 3 |
| Python 3.11 [x86_64] | Python | L | 1 | 27.920 ms | 0.000 ms | 0.000 ms | 27.920 ms → 27.920 ms | 1.6662 s | 0.000 ms | 0.000 ms | 1.6662 s → 1.6662 s | 24.887 MB | 0.000 MB | 0.000 MB | 24.887 MB → 24.887 MB | 3 |
| Python 3.12 [x86_64] | Python | S | 1 | 28.022 ms | 0.000 ms | 0.000 ms | 28.022 ms → 28.022 ms | 1.3663 s | 0.000 ms | 0.000 ms | 1.3663 s → 1.3663 s | 25.219 MB | 0.000 MB | 0.000 MB | 25.219 MB → 25.219 MB | 3 |
| Python 3.12 [x86_64] | Python | M | 1 | 28.290 ms | 0.000 ms | 0.000 ms | 28.290 ms → 28.290 ms | 1.3611 s | 0.000 ms | 0.000 ms | 1.3611 s → 1.3611 s | 26.422 MB | 0.000 MB | 0.000 MB | 26.422 MB → 26.422 MB | 3 |
| Python 3.12 [x86_64] | Python | L | 1 | 27.440 ms | 0.000 ms | 0.000 ms | 27.440 ms → 27.440 ms | 1.3405 s | 0.000 ms | 0.000 ms | 1.3405 s → 1.3405 s | 25.332 MB | 0.000 MB | 0.000 MB | 25.332 MB → 25.332 MB | 3 |
| Java 21 [x86_64] | Java | S | 1 | 42.098 ms | 0.000 ms | 0.000 ms | 42.098 ms → 42.098 ms | 1.3829 s | 0.000 ms | 0.000 ms | 1.3829 s → 1.3829 s | 39.336 MB | 0.000 MB | 0.000 MB | 39.336 MB → 39.336 MB | 5 |
| Java 21 [x86_64] | Java | M | 1 | 35.592 ms | 0.000 ms | 0.000 ms | 35.592 ms → 35.592 ms | 1.2292 s | 0.000 ms | 0.000 ms | 1.2292 s → 1.2292 s | 39.371 MB | 0.000 MB | 0.000 MB | 39.371 MB → 39.371 MB | 5 |
| Java 21 [x86_64] | Java | L | 1 | 37.432 ms | 0.000 ms | 0.000 ms | 37.432 ms → 37.432 ms | 1.4594 s | 0.000 ms | 0.000 ms | 1.4594 s → 1.4594 s | 39.480 MB | 0.000 MB | 0.000 MB | 39.480 MB → 39.480 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 26.761 ms | 0.000 ms | 0.000 ms | 26.761 ms → 26.761 ms | 1.0918 s | 0.000 ms | 0.000 ms | 1.0918 s → 1.0918 s | 9.367 MB | 0.000 MB | 0.000 MB | 9.367 MB → 9.367 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 26.798 ms | 0.000 ms | 0.000 ms | 26.798 ms → 26.798 ms | 1.0450 s | 0.000 ms | 0.000 ms | 1.0450 s → 1.0450 s | 9.781 MB | 0.000 MB | 0.000 MB | 9.781 MB → 9.781 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 26.862 ms | 0.000 ms | 0.000 ms | 26.862 ms → 26.862 ms | 973.512 ms | 0.000 ms | 0.000 ms | 973.512 ms → 973.512 ms | 9.664 MB | 0.000 MB | 0.000 MB | 9.664 MB → 9.664 MB | 5 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 29.111 ms | 0.000 ms | 0.000 ms | 29.111 ms → 29.111 ms | 1.1211 s | 0.000 ms | 0.000 ms | 1.1211 s → 1.1211 s | 20.164 MB | 0.000 MB | 0.000 MB | 20.164 MB → 20.164 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 27.507 ms | 0.000 ms | 0.000 ms | 27.507 ms → 27.507 ms | 1.1193 s | 0.000 ms | 0.000 ms | 1.1193 s → 1.1193 s | 18.402 MB | 0.000 MB | 0.000 MB | 18.402 MB → 18.402 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 29.503 ms | 0.000 ms | 0.000 ms | 29.503 ms → 29.503 ms | 1.2112 s | 0.000 ms | 0.000 ms | 1.2112 s → 1.2112 s | 18.070 MB | 0.000 MB | 0.000 MB | 18.070 MB → 18.070 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 31.165 ms | 0.000 ms | 0.000 ms | 31.165 ms → 31.165 ms | 1.1356 s | 0.000 ms | 0.000 ms | 1.1356 s → 1.1356 s | 21.555 MB | 0.000 MB | 0.000 MB | 21.555 MB → 21.555 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 32.426 ms | 0.000 ms | 0.000 ms | 32.426 ms → 32.426 ms | 1.1385 s | 0.000 ms | 0.000 ms | 1.1385 s → 1.1385 s | 20.598 MB | 0.000 MB | 0.000 MB | 20.598 MB → 20.598 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 31.554 ms | 0.000 ms | 0.000 ms | 31.554 ms → 31.554 ms | 1.1092 s | 0.000 ms | 0.000 ms | 1.1092 s → 1.1092 s | 20.035 MB | 0.000 MB | 0.000 MB | 20.035 MB → 20.035 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 73.900 ms | 0.000 ms | 0.000 ms | 73.900 ms → 73.900 ms | 1.1607 s | 0.000 ms | 0.000 ms | 1.1607 s → 1.1607 s | 30.352 MB | 0.000 MB | 0.000 MB | 30.352 MB → 30.352 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 67.884 ms | 0.000 ms | 0.000 ms | 67.884 ms → 67.884 ms | 1.1146 s | 0.000 ms | 0.000 ms | 1.1146 s → 1.1146 s | 30.211 MB | 0.000 MB | 0.000 MB | 30.211 MB → 30.211 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 67.486 ms | 0.000 ms | 0.000 ms | 67.486 ms → 67.486 ms | 1.1894 s | 0.000 ms | 0.000 ms | 1.1894 s → 1.1894 s | 30.496 MB | 0.000 MB | 0.000 MB | 30.496 MB → 30.496 MB | 4 |
| Go 1.23 [x86_64] | Go | S | 1 | 27.282 ms | 0.000 ms | 0.000 ms | 27.282 ms → 27.282 ms | 1.2789 s | 0.000 ms | 0.000 ms | 1.2789 s → 1.2789 s | 11.523 MB | 0.000 MB | 0.000 MB | 11.523 MB → 11.523 MB | 4 |
| Go 1.23 [x86_64] | Go | M | 1 | 27.703 ms | 0.000 ms | 0.000 ms | 27.703 ms → 27.703 ms | 1.0220 s | 0.000 ms | 0.000 ms | 1.0220 s → 1.0220 s | 11.312 MB | 0.000 MB | 0.000 MB | 11.312 MB → 11.312 MB | 4 |
| Go 1.23 [x86_64] | Go | L | 1 | 26.273 ms | 0.000 ms | 0.000 ms | 26.273 ms → 26.273 ms | 991.004 ms | 0.000 ms | 0.000 ms | 991.004 ms → 991.004 ms | 11.531 MB | 0.000 MB | 0.000 MB | 11.531 MB → 11.531 MB | 4 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 25.741 ms | 0.000 ms | 0.000 ms | 25.741 ms → 25.741 ms | 971.120 ms | 0.000 ms | 0.000 ms | 971.120 ms → 971.120 ms | 9.805 MB | 0.000 MB | 0.000 MB | 9.805 MB → 9.805 MB | 3 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 26.478 ms | 0.000 ms | 0.000 ms | 26.478 ms → 26.478 ms | 977.929 ms | 0.000 ms | 0.000 ms | 977.929 ms → 977.929 ms | 9.594 MB | 0.000 MB | 0.000 MB | 9.594 MB → 9.594 MB | 3 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 25.758 ms | 0.000 ms | 0.000 ms | 25.758 ms → 25.758 ms | 992.673 ms | 0.000 ms | 0.000 ms | 992.673 ms → 992.673 ms | 11.438 MB | 0.000 MB | 0.000 MB | 11.438 MB → 11.438 MB | 3 |

</details>

<details>
<summary><strong>image_resizing</strong> — Implementing a basic image processing task (resizing an image)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 22.308 ms | 0.000 ms | 0.000 ms | 22.308 ms → 22.308 ms | 22.308 ms | 0.000 ms | 0.000 ms | 22.308 ms → 22.308 ms | 24.898 MB | 0.000 MB | 0.000 MB | 24.898 MB → 24.898 MB | 16 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 40.055 MB | 0.000 MB | 0.000 MB | 40.055 MB → 40.055 MB | 16 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 83.333 ms | 0.000 ms | 0.000 ms | 83.333 ms → 83.333 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 64.020 MB | 0.000 MB | 0.000 MB | 64.020 MB → 64.020 MB | 16 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 24.992 MB | 0.000 MB | 0.000 MB | 24.992 MB → 24.992 MB | 15 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 30.988 MB | 0.000 MB | 0.000 MB | 30.988 MB → 30.988 MB | 15 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 24.615 ms | 0.000 ms | 0.000 ms | 24.615 ms → 24.615 ms | 25.385 ms | 0.000 ms | 0.000 ms | 25.385 ms → 25.385 ms | 39.004 MB | 0.000 MB | 0.000 MB | 39.004 MB → 39.004 MB | 15 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 26.273 MB | 0.000 MB | 0.000 MB | 26.273 MB → 26.273 MB | 15 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 20.769 ms | 0.000 ms | 0.000 ms | 20.769 ms → 20.769 ms | 32.238 MB | 0.000 MB | 0.000 MB | 32.238 MB → 32.238 MB | 15 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 40.188 MB | 0.000 MB | 0.000 MB | 40.188 MB → 40.188 MB | 15 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 25.617 MB | 0.000 MB | 0.000 MB | 25.617 MB → 25.617 MB | 15 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 19.231 ms | 0.000 ms | 0.000 ms | 19.231 ms → 19.231 ms | 31.527 MB | 0.000 MB | 0.000 MB | 31.527 MB → 31.527 MB | 15 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 24.286 ms | 0.000 ms | 0.000 ms | 24.286 ms → 24.286 ms | 25.714 ms | 0.000 ms | 0.000 ms | 25.714 ms → 25.714 ms | 35.496 MB | 0.000 MB | 0.000 MB | 35.496 MB → 35.496 MB | 15 |
| Python 2.7 [x86_64] | Python | S | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 8.000 MB | 0.000 MB | 0.000 MB | 8.000 MB → 8.000 MB | 12 |
| Python 2.7 [x86_64] | Python | M | 1 | 34.000 ms | 0.000 ms | 0.000 ms | 34.000 ms → 34.000 ms | 36.000 ms | 0.000 ms | 0.000 ms | 36.000 ms → 36.000 ms | 10.754 MB | 0.000 MB | 0.000 MB | 10.754 MB → 10.754 MB | 12 |
| Python 2.7 [x86_64] | Python | L | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 16.098 MB | 0.000 MB | 0.000 MB | 16.098 MB → 16.098 MB | 12 |
| Python 3.8 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 11.367 MB | 0.000 MB | 0.000 MB | 11.367 MB → 11.367 MB | 12 |
| Python 3.8 [x86_64] | Python | M | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 13.199 MB | 0.000 MB | 0.000 MB | 13.199 MB → 13.199 MB | 12 |
| Python 3.8 [x86_64] | Python | L | 1 | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 18.402 MB | 0.000 MB | 0.000 MB | 18.402 MB → 18.402 MB | 12 |
| Python 3.11 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.477 MB | 0.000 MB | 0.000 MB | 13.477 MB → 13.477 MB | 12 |
| Python 3.11 [x86_64] | Python | M | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 16.801 MB | 0.000 MB | 0.000 MB | 16.801 MB → 16.801 MB | 12 |
| Python 3.11 [x86_64] | Python | L | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 21.969 MB | 0.000 MB | 0.000 MB | 21.969 MB → 21.969 MB | 12 |
| Python 3.12 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.957 MB | 0.000 MB | 0.000 MB | 14.957 MB → 14.957 MB | 12 |
| Python 3.12 [x86_64] | Python | M | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 17.105 MB | 0.000 MB | 0.000 MB | 17.105 MB → 17.105 MB | 12 |
| Python 3.12 [x86_64] | Python | L | 1 | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 21.621 MB | 0.000 MB | 0.000 MB | 21.621 MB → 21.621 MB | 12 |
| Java 21 [x86_64] | Java | S | 1 | 143.333 ms | 0.000 ms | 0.000 ms | 143.333 ms → 143.333 ms | 133.333 ms | 0.000 ms | 0.000 ms | 133.333 ms → 133.333 ms | 47.520 MB | 0.000 MB | 0.000 MB | 47.520 MB → 47.520 MB | 16 |
| Java 21 [x86_64] | Java | M | 1 | 235.000 ms | 0.000 ms | 0.000 ms | 235.000 ms → 235.000 ms | 230.000 ms | 0.000 ms | 0.000 ms | 230.000 ms → 230.000 ms | 50.652 MB | 0.000 MB | 0.000 MB | 50.652 MB → 50.652 MB | 16 |
| Java 21 [x86_64] | Java | L | 1 | 290.000 ms | 0.000 ms | 0.000 ms | 290.000 ms → 290.000 ms | 280.000 ms | 0.000 ms | 0.000 ms | 280.000 ms → 280.000 ms | 55.449 MB | 0.000 MB | 0.000 MB | 55.449 MB → 55.449 MB | 16 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 2.240 ms | 0.000 ms | 0.000 ms | 2.240 ms → 2.240 ms | 2.280 ms | 0.000 ms | 0.000 ms | 2.280 ms → 2.280 ms | 3.793 MB | 0.000 MB | 0.000 MB | 3.793 MB → 3.793 MB | 20 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 3.960 ms | 0.000 ms | 0.000 ms | 3.960 ms → 3.960 ms | 4.040 ms | 0.000 ms | 0.000 ms | 4.040 ms → 4.040 ms | 3.773 MB | 0.000 MB | 0.000 MB | 3.773 MB → 3.773 MB | 20 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 6.840 ms | 0.000 ms | 0.000 ms | 6.840 ms → 6.840 ms | 6.880 ms | 0.000 ms | 0.000 ms | 6.880 ms → 6.880 ms | 3.852 MB | 0.000 MB | 0.000 MB | 3.852 MB → 3.852 MB | 20 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 47.164 MB | 0.000 MB | 0.000 MB | 47.164 MB → 47.164 MB | 15 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 49.941 MB | 0.000 MB | 0.000 MB | 49.941 MB → 49.941 MB | 15 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 58.000 ms | 0.000 ms | 0.000 ms | 58.000 ms → 58.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 56.438 MB | 0.000 MB | 0.000 MB | 56.438 MB → 56.438 MB | 15 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 44.461 MB | 0.000 MB | 0.000 MB | 44.461 MB → 44.461 MB | 15 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 42.857 ms | 0.000 ms | 0.000 ms | 42.857 ms → 42.857 ms | 42.857 ms | 0.000 ms | 0.000 ms | 42.857 ms → 42.857 ms | 47.895 MB | 0.000 MB | 0.000 MB | 47.895 MB → 47.895 MB | 15 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 55.711 MB | 0.000 MB | 0.000 MB | 55.711 MB → 55.711 MB | 15 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 71.129 MB | 0.000 MB | 0.000 MB | 71.129 MB → 71.129 MB | 15 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 75.316 MB | 0.000 MB | 0.000 MB | 75.316 MB → 75.316 MB | 15 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 82.031 MB | 0.000 MB | 0.000 MB | 82.031 MB → 82.031 MB | 15 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.760 ms | 0.000 ms | 0.000 ms | 2.760 ms → 2.760 ms | 2.760 ms | 0.000 ms | 0.000 ms | 2.760 ms → 2.760 ms | 9.559 MB | 0.000 MB | 0.000 MB | 9.559 MB → 9.559 MB | 25 |
| Go 1.23 [x86_64] | Go | M | 1 | 3.480 ms | 0.000 ms | 0.000 ms | 3.480 ms → 3.480 ms | 3.520 ms | 0.000 ms | 0.000 ms | 3.520 ms → 3.520 ms | 9.574 MB | 0.000 MB | 0.000 MB | 9.574 MB → 9.574 MB | 25 |
| Go 1.23 [x86_64] | Go | L | 1 | 4.600 ms | 0.000 ms | 0.000 ms | 4.600 ms → 4.600 ms | 4.600 ms | 0.000 ms | 0.000 ms | 4.600 ms → 4.600 ms | 11.562 MB | 0.000 MB | 0.000 MB | 11.562 MB → 11.562 MB | 25 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.560 ms | 0.000 ms | 0.000 ms | 1.560 ms → 1.560 ms | 1.640 ms | 0.000 ms | 0.000 ms | 1.640 ms → 1.640 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 16 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 2.560 ms | 0.000 ms | 0.000 ms | 2.560 ms → 2.560 ms | 2.640 ms | 0.000 ms | 0.000 ms | 2.640 ms → 2.640 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 16 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 3.800 ms | 0.000 ms | 0.000 ms | 3.800 ms → 3.800 ms | 3.840 ms | 0.000 ms | 0.000 ms | 3.840 ms → 3.840 ms | 3.594 MB | 0.000 MB | 0.000 MB | 3.594 MB → 3.594 MB | 16 |

</details>

<details>
<summary><strong>linear_regression</strong> — Implementing a basic machine learning algorithm (linear regression)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 26.667 ms | 0.000 ms | 0.000 ms | 26.667 ms → 26.667 ms | 26.667 ms | 0.000 ms | 0.000 ms | 26.667 ms → 26.667 ms | 20.727 MB | 0.000 MB | 0.000 MB | 20.727 MB → 20.727 MB | 18 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 83.333 ms | 0.000 ms | 0.000 ms | 83.333 ms → 83.333 ms | 20.695 MB | 0.000 MB | 0.000 MB | 20.695 MB → 20.695 MB | 18 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 150.000 ms | 0.000 ms | 0.000 ms | 150.000 ms → 150.000 ms | 155.000 ms | 0.000 ms | 0.000 ms | 155.000 ms → 155.000 ms | 20.430 MB | 0.000 MB | 0.000 MB | 20.430 MB → 20.430 MB | 18 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 20.769 ms | 0.000 ms | 0.000 ms | 20.769 ms → 20.769 ms | 20.769 ms | 0.000 ms | 0.000 ms | 20.769 ms → 20.769 ms | 22.742 MB | 0.000 MB | 0.000 MB | 22.742 MB → 22.742 MB | 17 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 22.723 MB | 0.000 MB | 0.000 MB | 22.723 MB → 22.723 MB | 17 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 96.667 ms | 0.000 ms | 0.000 ms | 96.667 ms → 96.667 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 22.512 MB | 0.000 MB | 0.000 MB | 22.512 MB → 22.512 MB | 17 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 23.077 ms | 0.000 ms | 0.000 ms | 23.077 ms → 23.077 ms | 23.846 ms | 0.000 ms | 0.000 ms | 23.846 ms → 23.846 ms | 23.992 MB | 0.000 MB | 0.000 MB | 23.992 MB → 23.992 MB | 17 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 58.000 ms | 0.000 ms | 0.000 ms | 58.000 ms → 58.000 ms | 58.000 ms | 0.000 ms | 0.000 ms | 58.000 ms → 58.000 ms | 23.855 MB | 0.000 MB | 0.000 MB | 23.855 MB → 23.855 MB | 17 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 103.333 ms | 0.000 ms | 0.000 ms | 103.333 ms → 103.333 ms | 106.667 ms | 0.000 ms | 0.000 ms | 106.667 ms → 106.667 ms | 24.047 MB | 0.000 MB | 0.000 MB | 24.047 MB → 24.047 MB | 17 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 22.308 ms | 0.000 ms | 0.000 ms | 22.308 ms → 22.308 ms | 22.308 ms | 0.000 ms | 0.000 ms | 22.308 ms → 22.308 ms | 25.426 MB | 0.000 MB | 0.000 MB | 25.426 MB → 25.426 MB | 17 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 25.227 MB | 0.000 MB | 0.000 MB | 25.227 MB → 25.227 MB | 17 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 25.211 MB | 0.000 MB | 0.000 MB | 25.211 MB → 25.211 MB | 17 |
| Python 2.7 [x86_64] | Python | S | 1 | 42.500 ms | 0.000 ms | 0.000 ms | 42.500 ms → 42.500 ms | 45.000 ms | 0.000 ms | 0.000 ms | 45.000 ms → 45.000 ms | 7.941 MB | 0.000 MB | 0.000 MB | 7.941 MB → 7.941 MB | 23 |
| Python 2.7 [x86_64] | Python | M | 1 | 150.000 ms | 0.000 ms | 0.000 ms | 150.000 ms → 150.000 ms | 150.000 ms | 0.000 ms | 0.000 ms | 150.000 ms → 150.000 ms | 7.832 MB | 0.000 MB | 0.000 MB | 7.832 MB → 7.832 MB | 23 |
| Python 2.7 [x86_64] | Python | L | 1 | 280.000 ms | 0.000 ms | 0.000 ms | 280.000 ms → 280.000 ms | 290.000 ms | 0.000 ms | 0.000 ms | 290.000 ms → 290.000 ms | 7.918 MB | 0.000 MB | 0.000 MB | 7.918 MB → 7.918 MB | 23 |
| Python 3.8 [x86_64] | Python | S | 1 | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 10.949 MB | 0.000 MB | 0.000 MB | 10.949 MB → 10.949 MB | 20 |
| Python 3.8 [x86_64] | Python | M | 1 | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 11.016 MB | 0.000 MB | 0.000 MB | 11.016 MB → 11.016 MB | 20 |
| Python 3.8 [x86_64] | Python | L | 1 | 320.000 ms | 0.000 ms | 0.000 ms | 320.000 ms → 320.000 ms | 330.000 ms | 0.000 ms | 0.000 ms | 330.000 ms → 330.000 ms | 10.949 MB | 0.000 MB | 0.000 MB | 10.949 MB → 10.949 MB | 20 |
| Python 3.11 [x86_64] | Python | S | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 13.750 MB | 0.000 MB | 0.000 MB | 13.750 MB → 13.750 MB | 20 |
| Python 3.11 [x86_64] | Python | M | 1 | 125.000 ms | 0.000 ms | 0.000 ms | 125.000 ms → 125.000 ms | 125.000 ms | 0.000 ms | 0.000 ms | 125.000 ms → 125.000 ms | 13.707 MB | 0.000 MB | 0.000 MB | 13.707 MB → 13.707 MB | 20 |
| Python 3.11 [x86_64] | Python | L | 1 | 205.000 ms | 0.000 ms | 0.000 ms | 205.000 ms → 205.000 ms | 210.000 ms | 0.000 ms | 0.000 ms | 210.000 ms → 210.000 ms | 13.715 MB | 0.000 MB | 0.000 MB | 13.715 MB → 13.715 MB | 20 |
| Python 3.12 [x86_64] | Python | S | 1 | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 15.078 MB | 0.000 MB | 0.000 MB | 15.078 MB → 15.078 MB | 20 |
| Python 3.12 [x86_64] | Python | M | 1 | 145.000 ms | 0.000 ms | 0.000 ms | 145.000 ms → 145.000 ms | 150.000 ms | 0.000 ms | 0.000 ms | 150.000 ms → 150.000 ms | 15.055 MB | 0.000 MB | 0.000 MB | 15.055 MB → 15.055 MB | 20 |
| Python 3.12 [x86_64] | Python | L | 1 | 260.000 ms | 0.000 ms | 0.000 ms | 260.000 ms → 260.000 ms | 270.000 ms | 0.000 ms | 0.000 ms | 270.000 ms → 270.000 ms | 15.172 MB | 0.000 MB | 0.000 MB | 15.172 MB → 15.172 MB | 20 |
| Java 21 [x86_64] | Java | S | 1 | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 160.000 ms | 0.000 ms | 0.000 ms | 160.000 ms → 160.000 ms | 50.609 MB | 0.000 MB | 0.000 MB | 50.609 MB → 50.609 MB | 19 |
| Java 21 [x86_64] | Java | M | 1 | 440.000 ms | 0.000 ms | 0.000 ms | 440.000 ms → 440.000 ms | 440.000 ms | 0.000 ms | 0.000 ms | 440.000 ms → 440.000 ms | 52.504 MB | 0.000 MB | 0.000 MB | 52.504 MB → 52.504 MB | 19 |
| Java 21 [x86_64] | Java | L | 1 | 670.000 ms | 0.000 ms | 0.000 ms | 670.000 ms → 670.000 ms | 650.000 ms | 0.000 ms | 0.000 ms | 650.000 ms → 650.000 ms | 58.332 MB | 0.000 MB | 0.000 MB | 58.332 MB → 58.332 MB | 19 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 4.240 ms | 0.000 ms | 0.000 ms | 4.240 ms → 4.240 ms | 4.280 ms | 0.000 ms | 0.000 ms | 4.280 ms → 4.280 ms | 3.852 MB | 0.000 MB | 0.000 MB | 3.852 MB → 3.852 MB | 25 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 3.801 MB | 0.000 MB | 0.000 MB | 3.801 MB → 3.801 MB | 25 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 3.754 MB | 0.000 MB | 0.000 MB | 3.754 MB → 3.754 MB | 25 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 55.035 MB | 0.000 MB | 0.000 MB | 55.035 MB → 55.035 MB | 16 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 77.500 ms | 0.000 ms | 0.000 ms | 77.500 ms → 77.500 ms | 77.500 ms | 0.000 ms | 0.000 ms | 77.500 ms → 77.500 ms | 63.148 MB | 0.000 MB | 0.000 MB | 63.148 MB → 63.148 MB | 16 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 106.667 ms | 0.000 ms | 0.000 ms | 106.667 ms → 106.667 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 67.566 MB | 0.000 MB | 0.000 MB | 67.566 MB → 67.566 MB | 16 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 41.429 ms | 0.000 ms | 0.000 ms | 41.429 ms → 41.429 ms | 41.429 ms | 0.000 ms | 0.000 ms | 41.429 ms → 41.429 ms | 48.738 MB | 0.000 MB | 0.000 MB | 48.738 MB → 48.738 MB | 16 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 59.488 MB | 0.000 MB | 0.000 MB | 59.488 MB → 59.488 MB | 16 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 73.102 MB | 0.000 MB | 0.000 MB | 73.102 MB → 73.102 MB | 16 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 57.500 ms | 0.000 ms | 0.000 ms | 57.500 ms → 57.500 ms | 57.500 ms | 0.000 ms | 0.000 ms | 57.500 ms → 57.500 ms | 77.348 MB | 0.000 MB | 0.000 MB | 77.348 MB → 77.348 MB | 16 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 83.333 ms | 0.000 ms | 0.000 ms | 83.333 ms → 83.333 ms | 87.336 MB | 0.000 MB | 0.000 MB | 87.336 MB → 87.336 MB | 16 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 166.667 ms | 0.000 ms | 0.000 ms | 166.667 ms → 166.667 ms | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 96.773 MB | 0.000 MB | 0.000 MB | 96.773 MB → 96.773 MB | 16 |
| Go 1.23 [x86_64] | Go | S | 1 | 4.760 ms | 0.000 ms | 0.000 ms | 4.760 ms → 4.760 ms | 4.800 ms | 0.000 ms | 0.000 ms | 4.800 ms → 4.800 ms | 9.582 MB | 0.000 MB | 0.000 MB | 9.582 MB → 9.582 MB | 26 |
| Go 1.23 [x86_64] | Go | M | 1 | 37.692 ms | 0.000 ms | 0.000 ms | 37.692 ms → 37.692 ms | 34.615 ms | 0.000 ms | 0.000 ms | 34.615 ms → 34.615 ms | 18.344 MB | 0.000 MB | 0.000 MB | 18.344 MB → 18.344 MB | 26 |
| Go 1.23 [x86_64] | Go | L | 1 | 92.000 ms | 0.000 ms | 0.000 ms | 92.000 ms → 92.000 ms | 84.000 ms | 0.000 ms | 0.000 ms | 84.000 ms → 84.000 ms | 22.324 MB | 0.000 MB | 0.000 MB | 22.324 MB → 22.324 MB | 26 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.880 ms | 0.000 ms | 0.000 ms | 1.880 ms → 1.880 ms | 1.960 ms | 0.000 ms | 0.000 ms | 1.960 ms → 1.960 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 23 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 4.680 ms | 0.000 ms | 0.000 ms | 4.680 ms → 4.680 ms | 4.760 ms | 0.000 ms | 0.000 ms | 4.760 ms → 4.760 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 23 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 7.600 ms | 0.000 ms | 0.000 ms | 7.600 ms → 7.600 ms | 8.000 ms | 0.000 ms | 0.000 ms | 8.000 ms → 8.000 ms | 3.469 MB | 0.000 MB | 0.000 MB | 3.469 MB → 3.469 MB | 23 |

</details>

<details>
<summary><strong>matrix_multiplication</strong> — Performing matrix multiplication</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 20.938 MB | 0.000 MB | 0.000 MB | 20.938 MB → 20.938 MB | 20 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 38.000 ms | 0.000 ms | 0.000 ms | 38.000 ms → 38.000 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 22.402 MB | 0.000 MB | 0.000 MB | 22.402 MB → 22.402 MB | 20 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 106.667 ms | 0.000 ms | 0.000 ms | 106.667 ms → 106.667 ms | 110.000 ms | 0.000 ms | 0.000 ms | 110.000 ms → 110.000 ms | 25.766 MB | 0.000 MB | 0.000 MB | 25.766 MB → 25.766 MB | 20 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 22.973 MB | 0.000 MB | 0.000 MB | 22.973 MB → 22.973 MB | 19 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 18.889 ms | 0.000 ms | 0.000 ms | 18.889 ms → 18.889 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 23.008 MB | 0.000 MB | 0.000 MB | 23.008 MB → 23.008 MB | 19 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 24.977 MB | 0.000 MB | 0.000 MB | 24.977 MB → 24.977 MB | 19 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 24.258 MB | 0.000 MB | 0.000 MB | 24.258 MB → 24.258 MB | 19 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 24.444 ms | 0.000 ms | 0.000 ms | 24.444 ms → 24.444 ms | 25.556 ms | 0.000 ms | 0.000 ms | 25.556 ms → 25.556 ms | 26.383 MB | 0.000 MB | 0.000 MB | 26.383 MB → 26.383 MB | 19 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 28.242 MB | 0.000 MB | 0.000 MB | 28.242 MB → 28.242 MB | 19 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 25.586 MB | 0.000 MB | 0.000 MB | 25.586 MB → 25.586 MB | 19 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 25.621 MB | 0.000 MB | 0.000 MB | 25.621 MB → 25.621 MB | 19 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 25.566 MB | 0.000 MB | 0.000 MB | 25.566 MB → 25.566 MB | 19 |
| Python 2.7 [x86_64] | Python | S | 1 | 18.000 ms | 0.000 ms | 0.000 ms | 18.000 ms → 18.000 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 7.762 MB | 0.000 MB | 0.000 MB | 7.762 MB → 7.762 MB | 16 |
| Python 2.7 [x86_64] | Python | M | 1 | 45.000 ms | 0.000 ms | 0.000 ms | 45.000 ms → 45.000 ms | 47.500 ms | 0.000 ms | 0.000 ms | 47.500 ms → 47.500 ms | 7.965 MB | 0.000 MB | 0.000 MB | 7.965 MB → 7.965 MB | 16 |
| Python 2.7 [x86_64] | Python | L | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 8.203 MB | 0.000 MB | 0.000 MB | 8.203 MB → 8.203 MB | 16 |
| Python 3.8 [x86_64] | Python | S | 1 | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 10.980 MB | 0.000 MB | 0.000 MB | 10.980 MB → 10.980 MB | 16 |
| Python 3.8 [x86_64] | Python | M | 1 | 110.000 ms | 0.000 ms | 0.000 ms | 110.000 ms → 110.000 ms | 110.000 ms | 0.000 ms | 0.000 ms | 110.000 ms → 110.000 ms | 10.805 MB | 0.000 MB | 0.000 MB | 10.805 MB → 10.805 MB | 16 |
| Python 3.8 [x86_64] | Python | L | 1 | 260.000 ms | 0.000 ms | 0.000 ms | 260.000 ms → 260.000 ms | 260.000 ms | 0.000 ms | 0.000 ms | 260.000 ms → 260.000 ms | 11.203 MB | 0.000 MB | 0.000 MB | 11.203 MB → 11.203 MB | 16 |
| Python 3.11 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.527 MB | 0.000 MB | 0.000 MB | 13.527 MB → 13.527 MB | 16 |
| Python 3.11 [x86_64] | Python | M | 1 | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 13.500 MB | 0.000 MB | 0.000 MB | 13.500 MB → 13.500 MB | 16 |
| Python 3.11 [x86_64] | Python | L | 1 | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 13.582 MB | 0.000 MB | 0.000 MB | 13.582 MB → 13.582 MB | 16 |
| Python 3.12 [x86_64] | Python | S | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 14.953 MB | 0.000 MB | 0.000 MB | 14.953 MB → 14.953 MB | 16 |
| Python 3.12 [x86_64] | Python | M | 1 | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 14.922 MB | 0.000 MB | 0.000 MB | 14.922 MB → 14.922 MB | 16 |
| Python 3.12 [x86_64] | Python | L | 1 | 180.000 ms | 0.000 ms | 0.000 ms | 180.000 ms → 180.000 ms | 180.000 ms | 0.000 ms | 0.000 ms | 180.000 ms → 180.000 ms | 14.953 MB | 0.000 MB | 0.000 MB | 14.953 MB → 14.953 MB | 16 |
| Java 21 [x86_64] | Java | S | 1 | 105.000 ms | 0.000 ms | 0.000 ms | 105.000 ms → 105.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 44.969 MB | 0.000 MB | 0.000 MB | 44.969 MB → 44.969 MB | 23 |
| Java 21 [x86_64] | Java | M | 1 | 160.000 ms | 0.000 ms | 0.000 ms | 160.000 ms → 160.000 ms | 143.333 ms | 0.000 ms | 0.000 ms | 143.333 ms → 143.333 ms | 44.887 MB | 0.000 MB | 0.000 MB | 44.887 MB → 44.887 MB | 23 |
| Java 21 [x86_64] | Java | L | 1 | 185.000 ms | 0.000 ms | 0.000 ms | 185.000 ms → 185.000 ms | 165.000 ms | 0.000 ms | 0.000 ms | 165.000 ms → 165.000 ms | 47.590 MB | 0.000 MB | 0.000 MB | 47.590 MB → 47.590 MB | 23 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 1.760 ms | 0.000 ms | 0.000 ms | 1.760 ms → 1.760 ms | 1.800 ms | 0.000 ms | 0.000 ms | 1.800 ms → 1.800 ms | 3.699 MB | 0.000 MB | 0.000 MB | 3.699 MB → 3.699 MB | 23 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 2.080 ms | 0.000 ms | 0.000 ms | 2.080 ms → 2.080 ms | 2.120 ms | 0.000 ms | 0.000 ms | 2.120 ms → 2.120 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 23 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 2.840 ms | 0.000 ms | 0.000 ms | 2.840 ms → 2.840 ms | 2.920 ms | 0.000 ms | 0.000 ms | 2.920 ms → 2.920 ms | 3.793 MB | 0.000 MB | 0.000 MB | 3.793 MB → 3.793 MB | 23 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 52.039 MB | 0.000 MB | 0.000 MB | 52.039 MB → 52.039 MB | 20 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 44.286 ms | 0.000 ms | 0.000 ms | 44.286 ms → 44.286 ms | 44.286 ms | 0.000 ms | 0.000 ms | 44.286 ms → 44.286 ms | 52.828 MB | 0.000 MB | 0.000 MB | 52.828 MB → 52.828 MB | 20 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 44.286 ms | 0.000 ms | 0.000 ms | 44.286 ms → 44.286 ms | 42.857 ms | 0.000 ms | 0.000 ms | 42.857 ms → 42.857 ms | 53.172 MB | 0.000 MB | 0.000 MB | 53.172 MB → 53.172 MB | 20 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 44.113 MB | 0.000 MB | 0.000 MB | 44.113 MB → 44.113 MB | 20 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 44.891 MB | 0.000 MB | 0.000 MB | 44.891 MB → 44.891 MB | 20 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 47.969 MB | 0.000 MB | 0.000 MB | 47.969 MB → 47.969 MB | 20 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 70.836 MB | 0.000 MB | 0.000 MB | 70.836 MB → 70.836 MB | 20 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 73.906 MB | 0.000 MB | 0.000 MB | 73.906 MB → 73.906 MB | 20 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 74.699 MB | 0.000 MB | 0.000 MB | 74.699 MB → 74.699 MB | 20 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.640 ms | 0.000 ms | 0.000 ms | 2.640 ms → 2.640 ms | 2.640 ms | 0.000 ms | 0.000 ms | 2.640 ms → 2.640 ms | 7.547 MB | 0.000 MB | 0.000 MB | 7.547 MB → 7.547 MB | 29 |
| Go 1.23 [x86_64] | Go | M | 1 | 3.040 ms | 0.000 ms | 0.000 ms | 3.040 ms → 3.040 ms | 3.080 ms | 0.000 ms | 0.000 ms | 3.080 ms → 3.080 ms | 9.555 MB | 0.000 MB | 0.000 MB | 9.555 MB → 9.555 MB | 29 |
| Go 1.23 [x86_64] | Go | L | 1 | 3.880 ms | 0.000 ms | 0.000 ms | 3.880 ms → 3.880 ms | 3.880 ms | 0.000 ms | 0.000 ms | 3.880 ms → 3.880 ms | 9.559 MB | 0.000 MB | 0.000 MB | 9.559 MB → 9.559 MB | 29 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.360 ms | 0.000 ms | 0.000 ms | 1.360 ms → 1.360 ms | 1.400 ms | 0.000 ms | 0.000 ms | 1.400 ms → 1.400 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 21 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 1.680 ms | 0.000 ms | 0.000 ms | 1.680 ms → 1.680 ms | 1.720 ms | 0.000 ms | 0.000 ms | 1.720 ms → 1.720 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 21 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 2.400 ms | 0.000 ms | 0.000 ms | 2.400 ms → 2.400 ms | 2.480 ms | 0.000 ms | 0.000 ms | 2.480 ms → 2.480 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 21 |

</details>

<details>
<summary><strong>prime_sieve</strong> — Implementing a simple algorithm (prime number generation)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 33.333 ms | 0.000 ms | 0.000 ms | 33.333 ms → 33.333 ms | 34.444 ms | 0.000 ms | 0.000 ms | 34.444 ms → 34.444 ms | 26.664 MB | 0.000 MB | 0.000 MB | 26.664 MB → 26.664 MB | 16 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 36.609 MB | 0.000 MB | 0.000 MB | 36.609 MB → 36.609 MB | 16 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 113.333 ms | 0.000 ms | 0.000 ms | 113.333 ms → 113.333 ms | 113.333 ms | 0.000 ms | 0.000 ms | 113.333 ms → 113.333 ms | 53.598 MB | 0.000 MB | 0.000 MB | 53.598 MB → 53.598 MB | 16 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 16.400 ms | 0.000 ms | 0.000 ms | 16.400 ms → 16.400 ms | 24.730 MB | 0.000 MB | 0.000 MB | 24.730 MB → 24.730 MB | 15 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 26.707 MB | 0.000 MB | 0.000 MB | 26.707 MB → 26.707 MB | 15 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 30.613 MB | 0.000 MB | 0.000 MB | 30.613 MB → 30.613 MB | 15 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 26.102 MB | 0.000 MB | 0.000 MB | 26.102 MB → 26.102 MB | 15 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 20.769 ms | 0.000 ms | 0.000 ms | 20.769 ms → 20.769 ms | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 27.895 MB | 0.000 MB | 0.000 MB | 27.895 MB → 27.895 MB | 15 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 32.094 MB | 0.000 MB | 0.000 MB | 32.094 MB → 32.094 MB | 15 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 15.600 ms | 0.000 ms | 0.000 ms | 15.600 ms → 15.600 ms | 16.000 ms | 0.000 ms | 0.000 ms | 16.000 ms → 16.000 ms | 25.418 MB | 0.000 MB | 0.000 MB | 25.418 MB → 25.418 MB | 15 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 27.438 MB | 0.000 MB | 0.000 MB | 27.438 MB → 27.438 MB | 15 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 22.222 ms | 0.000 ms | 0.000 ms | 22.222 ms → 22.222 ms | 23.333 ms | 0.000 ms | 0.000 ms | 23.333 ms → 23.333 ms | 29.336 MB | 0.000 MB | 0.000 MB | 29.336 MB → 29.336 MB | 15 |
| Python 2.7 [x86_64] | Python | S | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 8.203 MB | 0.000 MB | 0.000 MB | 8.203 MB → 8.203 MB | 13 |
| Python 2.7 [x86_64] | Python | M | 1 | 26.000 ms | 0.000 ms | 0.000 ms | 26.000 ms → 26.000 ms | 28.000 ms | 0.000 ms | 0.000 ms | 28.000 ms → 28.000 ms | 8.719 MB | 0.000 MB | 0.000 MB | 8.719 MB → 8.719 MB | 13 |
| Python 2.7 [x86_64] | Python | L | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 42.500 ms | 0.000 ms | 0.000 ms | 42.500 ms → 42.500 ms | 9.727 MB | 0.000 MB | 0.000 MB | 9.727 MB → 9.727 MB | 13 |
| Python 3.8 [x86_64] | Python | S | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 21.429 ms | 0.000 ms | 0.000 ms | 21.429 ms → 21.429 ms | 8.805 MB | 0.000 MB | 0.000 MB | 8.805 MB → 8.805 MB | 12 |
| Python 3.8 [x86_64] | Python | M | 1 | 28.000 ms | 0.000 ms | 0.000 ms | 28.000 ms → 28.000 ms | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 9.324 MB | 0.000 MB | 0.000 MB | 9.324 MB → 9.324 MB | 12 |
| Python 3.8 [x86_64] | Python | L | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 10.348 MB | 0.000 MB | 0.000 MB | 10.348 MB → 10.348 MB | 12 |
| Python 3.11 [x86_64] | Python | S | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 9.656 MB | 0.000 MB | 0.000 MB | 9.656 MB → 9.656 MB | 12 |
| Python 3.11 [x86_64] | Python | M | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 10.305 MB | 0.000 MB | 0.000 MB | 10.305 MB → 10.305 MB | 12 |
| Python 3.11 [x86_64] | Python | L | 1 | 27.143 ms | 0.000 ms | 0.000 ms | 27.143 ms → 27.143 ms | 28.571 ms | 0.000 ms | 0.000 ms | 28.571 ms → 28.571 ms | 11.238 MB | 0.000 MB | 0.000 MB | 11.238 MB → 11.238 MB | 12 |
| Python 3.12 [x86_64] | Python | S | 1 | 16.667 ms | 0.000 ms | 0.000 ms | 16.667 ms → 16.667 ms | 17.778 ms | 0.000 ms | 0.000 ms | 17.778 ms → 17.778 ms | 10.605 MB | 0.000 MB | 0.000 MB | 10.605 MB → 10.605 MB | 12 |
| Python 3.12 [x86_64] | Python | M | 1 | 22.222 ms | 0.000 ms | 0.000 ms | 22.222 ms → 22.222 ms | 23.333 ms | 0.000 ms | 0.000 ms | 23.333 ms → 23.333 ms | 11.242 MB | 0.000 MB | 0.000 MB | 11.242 MB → 11.242 MB | 12 |
| Python 3.12 [x86_64] | Python | L | 1 | 32.857 ms | 0.000 ms | 0.000 ms | 32.857 ms → 32.857 ms | 34.286 ms | 0.000 ms | 0.000 ms | 34.286 ms → 34.286 ms | 12.219 MB | 0.000 MB | 0.000 MB | 12.219 MB → 12.219 MB | 12 |
| Java 21 [x86_64] | Java | S | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 44.062 MB | 0.000 MB | 0.000 MB | 44.062 MB → 44.062 MB | 16 |
| Java 21 [x86_64] | Java | M | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 87.500 ms | 0.000 ms | 0.000 ms | 87.500 ms → 87.500 ms | 43.715 MB | 0.000 MB | 0.000 MB | 43.715 MB → 43.715 MB | 16 |
| Java 21 [x86_64] | Java | L | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 77.500 ms | 0.000 ms | 0.000 ms | 77.500 ms → 77.500 ms | 43.789 MB | 0.000 MB | 0.000 MB | 43.789 MB → 43.789 MB | 16 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 1.760 ms | 0.000 ms | 0.000 ms | 1.760 ms → 1.760 ms | 1.840 ms | 0.000 ms | 0.000 ms | 1.840 ms → 1.840 ms | 3.711 MB | 0.000 MB | 0.000 MB | 3.711 MB → 3.711 MB | 16 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 2.200 ms | 0.000 ms | 0.000 ms | 2.200 ms → 2.200 ms | 2.240 ms | 0.000 ms | 0.000 ms | 2.240 ms → 2.240 ms | 3.711 MB | 0.000 MB | 0.000 MB | 3.711 MB → 3.711 MB | 16 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 2.680 ms | 0.000 ms | 0.000 ms | 2.680 ms → 2.680 ms | 2.760 ms | 0.000 ms | 0.000 ms | 2.760 ms → 2.760 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 16 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 45.714 ms | 0.000 ms | 0.000 ms | 45.714 ms → 45.714 ms | 45.714 ms | 0.000 ms | 0.000 ms | 45.714 ms → 45.714 ms | 53.801 MB | 0.000 MB | 0.000 MB | 53.801 MB → 53.801 MB | 14 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 56.410 MB | 0.000 MB | 0.000 MB | 56.410 MB → 56.410 MB | 14 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 57.449 MB | 0.000 MB | 0.000 MB | 57.449 MB → 57.449 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 43.469 MB | 0.000 MB | 0.000 MB | 43.469 MB → 43.469 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 44.219 MB | 0.000 MB | 0.000 MB | 44.219 MB → 44.219 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 48.613 MB | 0.000 MB | 0.000 MB | 48.613 MB → 48.613 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 76.602 MB | 0.000 MB | 0.000 MB | 76.602 MB → 76.602 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 78.805 MB | 0.000 MB | 0.000 MB | 78.805 MB → 78.805 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 80.023 MB | 0.000 MB | 0.000 MB | 80.023 MB → 80.023 MB | 14 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.520 ms | 0.000 ms | 0.000 ms | 2.520 ms → 2.520 ms | 2.520 ms | 0.000 ms | 0.000 ms | 2.520 ms → 2.520 ms | 7.547 MB | 0.000 MB | 0.000 MB | 7.547 MB → 7.547 MB | 16 |
| Go 1.23 [x86_64] | Go | M | 1 | 2.760 ms | 0.000 ms | 0.000 ms | 2.760 ms → 2.760 ms | 2.800 ms | 0.000 ms | 0.000 ms | 2.800 ms → 2.800 ms | 9.551 MB | 0.000 MB | 0.000 MB | 9.551 MB → 9.551 MB | 16 |
| Go 1.23 [x86_64] | Go | L | 1 | 3.040 ms | 0.000 ms | 0.000 ms | 3.040 ms → 3.040 ms | 3.040 ms | 0.000 ms | 0.000 ms | 3.040 ms → 3.040 ms | 9.555 MB | 0.000 MB | 0.000 MB | 9.555 MB → 9.555 MB | 16 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.360 ms | 0.000 ms | 0.000 ms | 1.360 ms → 1.360 ms | 1.360 ms | 0.000 ms | 0.000 ms | 1.360 ms → 1.360 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 15 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 1.560 ms | 0.000 ms | 0.000 ms | 1.560 ms → 1.560 ms | 1.600 ms | 0.000 ms | 0.000 ms | 1.600 ms → 1.600 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 15 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 1.680 ms | 0.000 ms | 0.000 ms | 1.680 ms → 1.680 ms | 1.720 ms | 0.000 ms | 0.000 ms | 1.720 ms → 1.720 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 15 |

</details>

<details>
<summary><strong>producer_consumer</strong> — Implementing a simple multithreading task (producer-consumer problem)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 22.308 ms | 0.000 ms | 0.000 ms | 22.308 ms → 22.308 ms | 22.308 ms | 0.000 ms | 0.000 ms | 22.308 ms → 22.308 ms | 23.047 MB | 0.000 MB | 0.000 MB | 23.047 MB → 23.047 MB | 26 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 35.441 MB | 0.000 MB | 0.000 MB | 35.441 MB → 35.441 MB | 26 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 95.000 ms | 0.000 ms | 0.000 ms | 95.000 ms → 95.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 50.727 MB | 0.000 MB | 0.000 MB | 50.727 MB → 50.727 MB | 26 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 22.965 MB | 0.000 MB | 0.000 MB | 22.965 MB → 22.965 MB | 25 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 23.846 ms | 0.000 ms | 0.000 ms | 23.846 ms → 23.846 ms | 24.615 ms | 0.000 ms | 0.000 ms | 24.615 ms → 24.615 ms | 28.977 MB | 0.000 MB | 0.000 MB | 28.977 MB → 28.977 MB | 25 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 34.286 ms | 0.000 ms | 0.000 ms | 34.286 ms → 34.286 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 34.957 MB | 0.000 MB | 0.000 MB | 34.957 MB → 34.957 MB | 25 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 18.000 ms | 0.000 ms | 0.000 ms | 18.000 ms → 18.000 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 24.098 MB | 0.000 MB | 0.000 MB | 24.098 MB → 24.098 MB | 25 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 25.556 ms | 0.000 ms | 0.000 ms | 25.556 ms → 25.556 ms | 26.667 ms | 0.000 ms | 0.000 ms | 26.667 ms → 26.667 ms | 30.184 MB | 0.000 MB | 0.000 MB | 30.184 MB → 30.184 MB | 25 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 36.234 MB | 0.000 MB | 0.000 MB | 36.234 MB → 36.234 MB | 25 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 16.154 ms | 0.000 ms | 0.000 ms | 16.154 ms → 16.154 ms | 25.598 MB | 0.000 MB | 0.000 MB | 25.598 MB → 25.598 MB | 25 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 23.846 ms | 0.000 ms | 0.000 ms | 23.846 ms → 23.846 ms | 23.846 ms | 0.000 ms | 0.000 ms | 23.846 ms → 23.846 ms | 29.730 MB | 0.000 MB | 0.000 MB | 29.730 MB → 29.730 MB | 25 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 33.333 ms | 0.000 ms | 0.000 ms | 33.333 ms → 33.333 ms | 34.444 ms | 0.000 ms | 0.000 ms | 34.444 ms → 34.444 ms | 33.652 MB | 0.000 MB | 0.000 MB | 33.652 MB → 33.652 MB | 25 |
| Python 2.7 [x86_64] | Python | S | 1 | 24.000 ms | 0.000 ms | 0.000 ms | 24.000 ms → 24.000 ms | 24.000 ms | 0.000 ms | 0.000 ms | 24.000 ms → 24.000 ms | 7.891 MB | 0.000 MB | 0.000 MB | 7.891 MB → 7.891 MB | 23 |
| Python 2.7 [x86_64] | Python | M | 1 | 52.500 ms | 0.000 ms | 0.000 ms | 52.500 ms → 52.500 ms | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 12.500 MB | 0.000 MB | 0.000 MB | 12.500 MB → 12.500 MB | 23 |
| Python 2.7 [x86_64] | Python | L | 1 | 93.333 ms | 0.000 ms | 0.000 ms | 93.333 ms → 93.333 ms | 93.333 ms | 0.000 ms | 0.000 ms | 93.333 ms → 93.333 ms | 18.383 MB | 0.000 MB | 0.000 MB | 18.383 MB → 18.383 MB | 23 |
| Python 3.8 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 11.105 MB | 0.000 MB | 0.000 MB | 11.105 MB → 11.105 MB | 23 |
| Python 3.8 [x86_64] | Python | M | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 95.000 ms | 0.000 ms | 0.000 ms | 95.000 ms → 95.000 ms | 14.473 MB | 0.000 MB | 0.000 MB | 14.473 MB → 14.473 MB | 23 |
| Python 3.8 [x86_64] | Python | L | 1 | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 19.535 MB | 0.000 MB | 0.000 MB | 19.535 MB → 19.535 MB | 23 |
| Python 3.11 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 14.023 MB | 0.000 MB | 0.000 MB | 14.023 MB → 14.023 MB | 23 |
| Python 3.11 [x86_64] | Python | M | 1 | 73.333 ms | 0.000 ms | 0.000 ms | 73.333 ms → 73.333 ms | 73.333 ms | 0.000 ms | 0.000 ms | 73.333 ms → 73.333 ms | 17.898 MB | 0.000 MB | 0.000 MB | 17.898 MB → 17.898 MB | 23 |
| Python 3.11 [x86_64] | Python | L | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 23.590 MB | 0.000 MB | 0.000 MB | 23.590 MB → 23.590 MB | 23 |
| Python 3.12 [x86_64] | Python | S | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 14.785 MB | 0.000 MB | 0.000 MB | 14.785 MB → 14.785 MB | 23 |
| Python 3.12 [x86_64] | Python | M | 1 | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 18.332 MB | 0.000 MB | 0.000 MB | 18.332 MB → 18.332 MB | 23 |
| Python 3.12 [x86_64] | Python | L | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 23.102 MB | 0.000 MB | 0.000 MB | 23.102 MB → 23.102 MB | 23 |
| Java 21 [x86_64] | Java | S | 1 | 123.333 ms | 0.000 ms | 0.000 ms | 123.333 ms → 123.333 ms | 116.667 ms | 0.000 ms | 0.000 ms | 116.667 ms → 116.667 ms | 47.766 MB | 0.000 MB | 0.000 MB | 47.766 MB → 47.766 MB | 29 |
| Java 21 [x86_64] | Java | M | 1 | 255.000 ms | 0.000 ms | 0.000 ms | 255.000 ms → 255.000 ms | 250.000 ms | 0.000 ms | 0.000 ms | 250.000 ms → 250.000 ms | 50.906 MB | 0.000 MB | 0.000 MB | 50.906 MB → 50.906 MB | 29 |
| Java 21 [x86_64] | Java | L | 1 | 300.000 ms | 0.000 ms | 0.000 ms | 300.000 ms → 300.000 ms | 275.000 ms | 0.000 ms | 0.000 ms | 275.000 ms → 275.000 ms | 53.031 MB | 0.000 MB | 0.000 MB | 53.031 MB → 53.031 MB | 29 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 2.200 ms | 0.000 ms | 0.000 ms | 2.200 ms → 2.200 ms | 2.240 ms | 0.000 ms | 0.000 ms | 2.240 ms → 2.240 ms | 3.852 MB | 0.000 MB | 0.000 MB | 3.852 MB → 3.852 MB | 33 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 4.240 ms | 0.000 ms | 0.000 ms | 4.240 ms → 4.240 ms | 4.320 ms | 0.000 ms | 0.000 ms | 4.320 ms → 4.320 ms | 3.902 MB | 0.000 MB | 0.000 MB | 3.902 MB → 3.902 MB | 33 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 6.800 ms | 0.000 ms | 0.000 ms | 6.800 ms → 6.800 ms | 7.200 ms | 0.000 ms | 0.000 ms | 7.200 ms → 7.200 ms | 3.953 MB | 0.000 MB | 0.000 MB | 3.953 MB → 3.953 MB | 33 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 42.500 ms | 0.000 ms | 0.000 ms | 42.500 ms → 42.500 ms | 42.500 ms | 0.000 ms | 0.000 ms | 42.500 ms → 42.500 ms | 53.672 MB | 0.000 MB | 0.000 MB | 53.672 MB → 53.672 MB | 25 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 58.004 MB | 0.000 MB | 0.000 MB | 58.004 MB → 58.004 MB | 25 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 77.500 ms | 0.000 ms | 0.000 ms | 77.500 ms → 77.500 ms | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 64.914 MB | 0.000 MB | 0.000 MB | 64.914 MB → 64.914 MB | 25 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 46.195 MB | 0.000 MB | 0.000 MB | 46.195 MB → 46.195 MB | 25 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 55.309 MB | 0.000 MB | 0.000 MB | 55.309 MB → 55.309 MB | 25 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 70.945 MB | 0.000 MB | 0.000 MB | 70.945 MB → 70.945 MB | 25 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 75.277 MB | 0.000 MB | 0.000 MB | 75.277 MB → 75.277 MB | 25 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 81.688 MB | 0.000 MB | 0.000 MB | 81.688 MB → 81.688 MB | 25 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 89.055 MB | 0.000 MB | 0.000 MB | 89.055 MB → 89.055 MB | 25 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.920 ms | 0.000 ms | 0.000 ms | 2.920 ms → 2.920 ms | 2.960 ms | 0.000 ms | 0.000 ms | 2.960 ms → 2.960 ms | 9.676 MB | 0.000 MB | 0.000 MB | 9.676 MB → 9.676 MB | 41 |
| Go 1.23 [x86_64] | Go | M | 1 | 4.400 ms | 0.000 ms | 0.000 ms | 4.400 ms → 4.400 ms | 4.480 ms | 0.000 ms | 0.000 ms | 4.480 ms → 4.480 ms | 9.562 MB | 0.000 MB | 0.000 MB | 9.562 MB → 9.562 MB | 41 |
| Go 1.23 [x86_64] | Go | L | 1 | 6.800 ms | 0.000 ms | 0.000 ms | 6.800 ms → 6.800 ms | 6.840 ms | 0.000 ms | 0.000 ms | 6.840 ms → 6.840 ms | 13.844 MB | 0.000 MB | 0.000 MB | 13.844 MB → 13.844 MB | 41 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.520 ms | 0.000 ms | 0.000 ms | 1.520 ms → 1.520 ms | 1.560 ms | 0.000 ms | 0.000 ms | 1.560 ms → 1.560 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 27 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 2.440 ms | 0.000 ms | 0.000 ms | 2.440 ms → 2.440 ms | 2.520 ms | 0.000 ms | 0.000 ms | 2.520 ms → 2.520 ms | 3.090 MB | 0.000 MB | 0.000 MB | 3.090 MB → 3.090 MB | 27 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 3.640 ms | 0.000 ms | 0.000 ms | 3.640 ms → 3.640 ms | 3.680 ms | 0.000 ms | 0.000 ms | 3.680 ms → 3.680 ms | 3.594 MB | 0.000 MB | 0.000 MB | 3.594 MB → 3.594 MB | 27 |

</details>

<details>
<summary><strong>rest_api</strong> — Implementing a simple REST API</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 31.100 ms | 0.000 ms | 0.000 ms | 31.100 ms → 31.100 ms | 248.653 ms | 0.000 ms | 0.000 ms | 248.653 ms → 248.653 ms | 15.492 MB | 0.000 MB | 0.000 MB | 15.492 MB → 15.492 MB | 5 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 33.035 ms | 0.000 ms | 0.000 ms | 33.035 ms → 33.035 ms | 303.957 ms | 0.000 ms | 0.000 ms | 303.957 ms → 303.957 ms | 14.363 MB | 0.000 MB | 0.000 MB | 14.363 MB → 14.363 MB | 5 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 43.981 ms | 0.000 ms | 0.000 ms | 43.981 ms → 43.981 ms | 416.855 ms | 0.000 ms | 0.000 ms | 416.855 ms → 416.855 ms | 14.305 MB | 0.000 MB | 0.000 MB | 14.305 MB → 14.305 MB | 5 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 27.608 ms | 0.000 ms | 0.000 ms | 27.608 ms → 27.608 ms | 258.555 ms | 0.000 ms | 0.000 ms | 258.555 ms → 258.555 ms | 15.195 MB | 0.000 MB | 0.000 MB | 15.195 MB → 15.195 MB | 5 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 32.018 ms | 0.000 ms | 0.000 ms | 32.018 ms → 32.018 ms | 359.174 ms | 0.000 ms | 0.000 ms | 359.174 ms → 359.174 ms | 15.887 MB | 0.000 MB | 0.000 MB | 15.887 MB → 15.887 MB | 5 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 41.283 ms | 0.000 ms | 0.000 ms | 41.283 ms → 41.283 ms | 404.787 ms | 0.000 ms | 0.000 ms | 404.787 ms → 404.787 ms | 15.422 MB | 0.000 MB | 0.000 MB | 15.422 MB → 15.422 MB | 5 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 28.419 ms | 0.000 ms | 0.000 ms | 28.419 ms → 28.419 ms | 463.108 ms | 0.000 ms | 0.000 ms | 463.108 ms → 463.108 ms | 15.852 MB | 0.000 MB | 0.000 MB | 15.852 MB → 15.852 MB | 5 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 35.778 ms | 0.000 ms | 0.000 ms | 35.778 ms → 35.778 ms | 418.422 ms | 0.000 ms | 0.000 ms | 418.422 ms → 418.422 ms | 16.719 MB | 0.000 MB | 0.000 MB | 16.719 MB → 16.719 MB | 5 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 41.907 ms | 0.000 ms | 0.000 ms | 41.907 ms → 41.907 ms | 523.969 ms | 0.000 ms | 0.000 ms | 523.969 ms → 523.969 ms | 15.645 MB | 0.000 MB | 0.000 MB | 15.645 MB → 15.645 MB | 5 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 29.573 ms | 0.000 ms | 0.000 ms | 29.573 ms → 29.573 ms | 377.051 ms | 0.000 ms | 0.000 ms | 377.051 ms → 377.051 ms | 16.832 MB | 0.000 MB | 0.000 MB | 16.832 MB → 16.832 MB | 5 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 32.354 ms | 0.000 ms | 0.000 ms | 32.354 ms → 32.354 ms | 430.103 ms | 0.000 ms | 0.000 ms | 430.103 ms → 430.103 ms | 17.078 MB | 0.000 MB | 0.000 MB | 17.078 MB → 17.078 MB | 5 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 41.664 ms | 0.000 ms | 0.000 ms | 41.664 ms → 41.664 ms | 524.850 ms | 0.000 ms | 0.000 ms | 524.850 ms → 524.850 ms | 17.020 MB | 0.000 MB | 0.000 MB | 17.020 MB → 17.020 MB | 5 |
| Python 2.7 [x86_64] | Python | S | 1 | 41.354 ms | 0.000 ms | 0.000 ms | 41.354 ms → 41.354 ms | 364.705 ms | 0.000 ms | 0.000 ms | 364.705 ms → 364.705 ms | 17.797 MB | 0.000 MB | 0.000 MB | 17.797 MB → 17.797 MB | 3 |
| Python 2.7 [x86_64] | Python | M | 1 | 65.752 ms | 0.000 ms | 0.000 ms | 65.752 ms → 65.752 ms | 430.080 ms | 0.000 ms | 0.000 ms | 430.080 ms → 430.080 ms | 19.488 MB | 0.000 MB | 0.000 MB | 19.488 MB → 19.488 MB | 3 |
| Python 2.7 [x86_64] | Python | L | 1 | 119.689 ms | 0.000 ms | 0.000 ms | 119.689 ms → 119.689 ms | 609.081 ms | 0.000 ms | 0.000 ms | 609.081 ms → 609.081 ms | 18.145 MB | 0.000 MB | 0.000 MB | 18.145 MB → 18.145 MB | 3 |
| Python 3.8 [x86_64] | Python | S | 1 | 40.010 ms | 0.000 ms | 0.000 ms | 40.010 ms → 40.010 ms | 596.503 ms | 0.000 ms | 0.000 ms | 596.503 ms → 596.503 ms | 23.504 MB | 0.000 MB | 0.000 MB | 23.504 MB → 23.504 MB | 3 |
| Python 3.8 [x86_64] | Python | M | 1 | 73.596 ms | 0.000 ms | 0.000 ms | 73.596 ms → 73.596 ms | 696.689 ms | 0.000 ms | 0.000 ms | 696.689 ms → 696.689 ms | 21.918 MB | 0.000 MB | 0.000 MB | 21.918 MB → 21.918 MB | 3 |
| Python 3.8 [x86_64] | Python | L | 1 | 142.991 ms | 0.000 ms | 0.000 ms | 142.991 ms → 142.991 ms | 818.231 ms | 0.000 ms | 0.000 ms | 818.231 ms → 818.231 ms | 21.793 MB | 0.000 MB | 0.000 MB | 21.793 MB → 21.793 MB | 3 |
| Python 3.11 [x86_64] | Python | S | 1 | 36.030 ms | 0.000 ms | 0.000 ms | 36.030 ms → 36.030 ms | 594.369 ms | 0.000 ms | 0.000 ms | 594.369 ms → 594.369 ms | 25.484 MB | 0.000 MB | 0.000 MB | 25.484 MB → 25.484 MB | 3 |
| Python 3.11 [x86_64] | Python | M | 1 | 63.445 ms | 0.000 ms | 0.000 ms | 63.445 ms → 63.445 ms | 630.420 ms | 0.000 ms | 0.000 ms | 630.420 ms → 630.420 ms | 27.117 MB | 0.000 MB | 0.000 MB | 27.117 MB → 27.117 MB | 3 |
| Python 3.11 [x86_64] | Python | L | 1 | 114.256 ms | 0.000 ms | 0.000 ms | 114.256 ms → 114.256 ms | 773.287 ms | 0.000 ms | 0.000 ms | 773.287 ms → 773.287 ms | 27.637 MB | 0.000 MB | 0.000 MB | 27.637 MB → 27.637 MB | 3 |
| Python 3.12 [x86_64] | Python | S | 1 | 36.973 ms | 0.000 ms | 0.000 ms | 36.973 ms → 36.973 ms | 573.456 ms | 0.000 ms | 0.000 ms | 573.456 ms → 573.456 ms | 25.523 MB | 0.000 MB | 0.000 MB | 25.523 MB → 25.523 MB | 3 |
| Python 3.12 [x86_64] | Python | M | 1 | 66.484 ms | 0.000 ms | 0.000 ms | 66.484 ms → 66.484 ms | 631.127 ms | 0.000 ms | 0.000 ms | 631.127 ms → 631.127 ms | 25.348 MB | 0.000 MB | 0.000 MB | 25.348 MB → 25.348 MB | 3 |
| Python 3.12 [x86_64] | Python | L | 1 | 129.698 ms | 0.000 ms | 0.000 ms | 129.698 ms → 129.698 ms | 815.632 ms | 0.000 ms | 0.000 ms | 815.632 ms → 815.632 ms | 25.527 MB | 0.000 MB | 0.000 MB | 25.527 MB → 25.527 MB | 3 |
| Java 21 [x86_64] | Java | S | 1 | 113.171 ms | 0.000 ms | 0.000 ms | 113.171 ms → 113.171 ms | 614.908 ms | 0.000 ms | 0.000 ms | 614.908 ms → 614.908 ms | 41.910 MB | 0.000 MB | 0.000 MB | 41.910 MB → 41.910 MB | 5 |
| Java 21 [x86_64] | Java | M | 1 | 320.529 ms | 0.000 ms | 0.000 ms | 320.529 ms → 320.529 ms | 708.945 ms | 0.000 ms | 0.000 ms | 708.945 ms → 708.945 ms | 40.926 MB | 0.000 MB | 0.000 MB | 40.926 MB → 40.926 MB | 5 |
| Java 21 [x86_64] | Java | L | 1 | 602.364 ms | 0.000 ms | 0.000 ms | 602.364 ms → 602.364 ms | 1.2076 s | 0.000 ms | 0.000 ms | 1.2076 s → 1.2076 s | 52.133 MB | 0.000 MB | 0.000 MB | 52.133 MB → 52.133 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 26.718 ms | 0.000 ms | 0.000 ms | 26.718 ms → 26.718 ms | 245.782 ms | 0.000 ms | 0.000 ms | 245.782 ms → 245.782 ms | 11.152 MB | 0.000 MB | 0.000 MB | 11.152 MB → 11.152 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 29.676 ms | 0.000 ms | 0.000 ms | 29.676 ms → 29.676 ms | 303.084 ms | 0.000 ms | 0.000 ms | 303.084 ms → 303.084 ms | 9.562 MB | 0.000 MB | 0.000 MB | 9.562 MB → 9.562 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 43.908 ms | 0.000 ms | 0.000 ms | 43.908 ms → 43.908 ms | 424.367 ms | 0.000 ms | 0.000 ms | 424.367 ms → 424.367 ms | 9.820 MB | 0.000 MB | 0.000 MB | 9.820 MB → 9.820 MB | 6 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 50.336 ms | 0.000 ms | 0.000 ms | 50.336 ms → 50.336 ms | 373.266 ms | 0.000 ms | 0.000 ms | 373.266 ms → 373.266 ms | 22.074 MB | 0.000 MB | 0.000 MB | 22.074 MB → 22.074 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 116.603 ms | 0.000 ms | 0.000 ms | 116.603 ms → 116.603 ms | 452.888 ms | 0.000 ms | 0.000 ms | 452.888 ms → 452.888 ms | 21.160 MB | 0.000 MB | 0.000 MB | 21.160 MB → 21.160 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 190.371 ms | 0.000 ms | 0.000 ms | 190.371 ms → 190.371 ms | 591.642 ms | 0.000 ms | 0.000 ms | 591.642 ms → 591.642 ms | 21.418 MB | 0.000 MB | 0.000 MB | 21.418 MB → 21.418 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 51.050 ms | 0.000 ms | 0.000 ms | 51.050 ms → 51.050 ms | 407.195 ms | 0.000 ms | 0.000 ms | 407.195 ms → 407.195 ms | 25.844 MB | 0.000 MB | 0.000 MB | 25.844 MB → 25.844 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 80.079 ms | 0.000 ms | 0.000 ms | 80.079 ms → 80.079 ms | 446.761 ms | 0.000 ms | 0.000 ms | 446.761 ms → 446.761 ms | 23.254 MB | 0.000 MB | 0.000 MB | 23.254 MB → 23.254 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 122.484 ms | 0.000 ms | 0.000 ms | 122.484 ms → 122.484 ms | 554.446 ms | 0.000 ms | 0.000 ms | 554.446 ms → 554.446 ms | 26.676 MB | 0.000 MB | 0.000 MB | 26.676 MB → 26.676 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 50.266 ms | 0.000 ms | 0.000 ms | 50.266 ms → 50.266 ms | 372.025 ms | 0.000 ms | 0.000 ms | 372.025 ms → 372.025 ms | 31.656 MB | 0.000 MB | 0.000 MB | 31.656 MB → 31.656 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 92.382 ms | 0.000 ms | 0.000 ms | 92.382 ms → 92.382 ms | 472.020 ms | 0.000 ms | 0.000 ms | 472.020 ms → 472.020 ms | 34.785 MB | 0.000 MB | 0.000 MB | 34.785 MB → 34.785 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 193.953 ms | 0.000 ms | 0.000 ms | 193.953 ms → 193.953 ms | 639.383 ms | 0.000 ms | 0.000 ms | 639.383 ms → 639.383 ms | 45.371 MB | 0.000 MB | 0.000 MB | 45.371 MB → 45.371 MB | 4 |
| Go 1.23 [x86_64] | Go | S | 1 | 32.182 ms | 0.000 ms | 0.000 ms | 32.182 ms → 32.182 ms | 245.549 ms | 0.000 ms | 0.000 ms | 245.549 ms → 245.549 ms | 12.977 MB | 0.000 MB | 0.000 MB | 12.977 MB → 12.977 MB | 4 |
| Go 1.23 [x86_64] | Go | M | 1 | 53.721 ms | 0.000 ms | 0.000 ms | 53.721 ms → 53.721 ms | 343.641 ms | 0.000 ms | 0.000 ms | 343.641 ms → 343.641 ms | 13.613 MB | 0.000 MB | 0.000 MB | 13.613 MB → 13.613 MB | 4 |
| Go 1.23 [x86_64] | Go | L | 1 | 79.423 ms | 0.000 ms | 0.000 ms | 79.423 ms → 79.423 ms | 434.280 ms | 0.000 ms | 0.000 ms | 434.280 ms → 434.280 ms | 14.312 MB | 0.000 MB | 0.000 MB | 14.312 MB → 14.312 MB | 4 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 26.868 ms | 0.000 ms | 0.000 ms | 26.868 ms → 26.868 ms | 252.810 ms | 0.000 ms | 0.000 ms | 252.810 ms → 252.810 ms | 9.301 MB | 0.000 MB | 0.000 MB | 9.301 MB → 9.301 MB | 3 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 29.603 ms | 0.000 ms | 0.000 ms | 29.603 ms → 29.603 ms | 297.726 ms | 0.000 ms | 0.000 ms | 297.726 ms → 297.726 ms | 9.512 MB | 0.000 MB | 0.000 MB | 9.512 MB → 9.512 MB | 3 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 34.941 ms | 0.000 ms | 0.000 ms | 34.941 ms → 34.941 ms | 410.901 ms | 0.000 ms | 0.000 ms | 410.901 ms → 410.901 ms | 9.504 MB | 0.000 MB | 0.000 MB | 9.504 MB → 9.504 MB | 3 |

</details>

<details>
<summary><strong>sentiment_analysis</strong> — Implementing a simple natural language processing task (sentiment analysis)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 31.111 ms | 0.000 ms | 0.000 ms | 31.111 ms → 31.111 ms | 21.141 MB | 0.000 MB | 0.000 MB | 21.141 MB → 21.141 MB | 17 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 83.333 ms | 0.000 ms | 0.000 ms | 83.333 ms → 83.333 ms | 86.667 ms | 0.000 ms | 0.000 ms | 86.667 ms → 86.667 ms | 25.426 MB | 0.000 MB | 0.000 MB | 25.426 MB → 25.426 MB | 17 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 190.000 ms | 0.000 ms | 0.000 ms | 190.000 ms → 190.000 ms | 195.000 ms | 0.000 ms | 0.000 ms | 195.000 ms → 195.000 ms | 33.820 MB | 0.000 MB | 0.000 MB | 33.820 MB → 33.820 MB | 17 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 22.969 MB | 0.000 MB | 0.000 MB | 22.969 MB → 22.969 MB | 14 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 32.222 ms | 0.000 ms | 0.000 ms | 32.222 ms → 32.222 ms | 34.444 ms | 0.000 ms | 0.000 ms | 34.444 ms → 34.444 ms | 26.973 MB | 0.000 MB | 0.000 MB | 26.973 MB → 26.973 MB | 14 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 62.000 ms | 0.000 ms | 0.000 ms | 62.000 ms → 62.000 ms | 31.707 MB | 0.000 MB | 0.000 MB | 31.707 MB → 31.707 MB | 14 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 24.145 MB | 0.000 MB | 0.000 MB | 24.145 MB → 24.145 MB | 14 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 28.188 MB | 0.000 MB | 0.000 MB | 28.188 MB → 28.188 MB | 14 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 72.500 ms | 0.000 ms | 0.000 ms | 72.500 ms → 72.500 ms | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 32.895 MB | 0.000 MB | 0.000 MB | 32.895 MB → 32.895 MB | 14 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 25.609 MB | 0.000 MB | 0.000 MB | 25.609 MB → 25.609 MB | 14 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 34.286 ms | 0.000 ms | 0.000 ms | 34.286 ms → 34.286 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 29.598 MB | 0.000 MB | 0.000 MB | 29.598 MB → 29.598 MB | 14 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 34.340 MB | 0.000 MB | 0.000 MB | 34.340 MB → 34.340 MB | 14 |
| Python 2.7 [x86_64] | Python | S | 1 | 24.000 ms | 0.000 ms | 0.000 ms | 24.000 ms → 24.000 ms | 26.000 ms | 0.000 ms | 0.000 ms | 26.000 ms → 26.000 ms | 9.559 MB | 0.000 MB | 0.000 MB | 9.559 MB → 9.559 MB | 13 |
| Python 2.7 [x86_64] | Python | M | 1 | 55.000 ms | 0.000 ms | 0.000 ms | 55.000 ms → 55.000 ms | 57.500 ms | 0.000 ms | 0.000 ms | 57.500 ms → 57.500 ms | 17.707 MB | 0.000 MB | 0.000 MB | 17.707 MB → 17.707 MB | 13 |
| Python 2.7 [x86_64] | Python | L | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 34.309 MB | 0.000 MB | 0.000 MB | 34.309 MB → 34.309 MB | 13 |
| Python 3.8 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 10.941 MB | 0.000 MB | 0.000 MB | 10.941 MB → 10.941 MB | 13 |
| Python 3.8 [x86_64] | Python | M | 1 | 76.667 ms | 0.000 ms | 0.000 ms | 76.667 ms → 76.667 ms | 76.667 ms | 0.000 ms | 0.000 ms | 76.667 ms → 76.667 ms | 13.027 MB | 0.000 MB | 0.000 MB | 13.027 MB → 13.027 MB | 13 |
| Python 3.8 [x86_64] | Python | L | 1 | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 17.629 MB | 0.000 MB | 0.000 MB | 17.629 MB → 17.629 MB | 13 |
| Python 3.11 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 13.586 MB | 0.000 MB | 0.000 MB | 13.586 MB → 13.586 MB | 13 |
| Python 3.11 [x86_64] | Python | M | 1 | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 16.344 MB | 0.000 MB | 0.000 MB | 16.344 MB → 16.344 MB | 13 |
| Python 3.11 [x86_64] | Python | L | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 21.461 MB | 0.000 MB | 0.000 MB | 21.461 MB → 21.461 MB | 13 |
| Python 3.12 [x86_64] | Python | S | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 15.039 MB | 0.000 MB | 0.000 MB | 15.039 MB → 15.039 MB | 13 |
| Python 3.12 [x86_64] | Python | M | 1 | 95.000 ms | 0.000 ms | 0.000 ms | 95.000 ms → 95.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 17.266 MB | 0.000 MB | 0.000 MB | 17.266 MB → 17.266 MB | 13 |
| Python 3.12 [x86_64] | Python | L | 1 | 130.000 ms | 0.000 ms | 0.000 ms | 130.000 ms → 130.000 ms | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 22.426 MB | 0.000 MB | 0.000 MB | 22.426 MB → 22.426 MB | 13 |
| Java 21 [x86_64] | Java | S | 1 | 315.000 ms | 0.000 ms | 0.000 ms | 315.000 ms → 315.000 ms | 285.000 ms | 0.000 ms | 0.000 ms | 285.000 ms → 285.000 ms | 49.801 MB | 0.000 MB | 0.000 MB | 49.801 MB → 49.801 MB | 16 |
| Java 21 [x86_64] | Java | M | 1 | 850.000 ms | 0.000 ms | 0.000 ms | 850.000 ms → 850.000 ms | 810.000 ms | 0.000 ms | 0.000 ms | 810.000 ms → 810.000 ms | 53.301 MB | 0.000 MB | 0.000 MB | 53.301 MB → 53.301 MB | 16 |
| Java 21 [x86_64] | Java | L | 1 | 1.0900 s | 0.000 ms | 0.000 ms | 1.0900 s → 1.0900 s | 1.0500 s | 0.000 ms | 0.000 ms | 1.0500 s → 1.0500 s | 60.512 MB | 0.000 MB | 0.000 MB | 60.512 MB → 60.512 MB | 16 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 5.120 ms | 0.000 ms | 0.000 ms | 5.120 ms → 5.120 ms | 5.200 ms | 0.000 ms | 0.000 ms | 5.200 ms → 5.200 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 20 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 15.600 ms | 0.000 ms | 0.000 ms | 15.600 ms → 15.600 ms | 15.600 ms | 0.000 ms | 0.000 ms | 15.600 ms → 15.600 ms | 3.727 MB | 0.000 MB | 0.000 MB | 3.727 MB → 3.727 MB | 20 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 3.648 MB | 0.000 MB | 0.000 MB | 3.648 MB → 3.648 MB | 20 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 55.133 MB | 0.000 MB | 0.000 MB | 55.133 MB → 55.133 MB | 14 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 72.500 ms | 0.000 ms | 0.000 ms | 72.500 ms → 72.500 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 57.715 MB | 0.000 MB | 0.000 MB | 57.715 MB → 57.715 MB | 14 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 110.000 ms | 0.000 ms | 0.000 ms | 110.000 ms → 110.000 ms | 110.000 ms | 0.000 ms | 0.000 ms | 110.000 ms → 110.000 ms | 65.098 MB | 0.000 MB | 0.000 MB | 65.098 MB → 65.098 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 52.500 ms | 0.000 ms | 0.000 ms | 52.500 ms → 52.500 ms | 52.500 ms | 0.000 ms | 0.000 ms | 52.500 ms → 52.500 ms | 50.797 MB | 0.000 MB | 0.000 MB | 50.797 MB → 50.797 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 95.000 ms | 0.000 ms | 0.000 ms | 95.000 ms → 95.000 ms | 92.500 ms | 0.000 ms | 0.000 ms | 92.500 ms → 92.500 ms | 73.309 MB | 0.000 MB | 0.000 MB | 73.309 MB → 73.309 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 150.000 ms | 0.000 ms | 0.000 ms | 150.000 ms → 150.000 ms | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 101.402 MB | 0.000 MB | 0.000 MB | 101.402 MB → 101.402 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 77.012 MB | 0.000 MB | 0.000 MB | 77.012 MB → 77.012 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 80.797 MB | 0.000 MB | 0.000 MB | 80.797 MB → 80.797 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 145.000 ms | 0.000 ms | 0.000 ms | 145.000 ms → 145.000 ms | 140.000 ms | 0.000 ms | 0.000 ms | 140.000 ms → 140.000 ms | 89.914 MB | 0.000 MB | 0.000 MB | 89.914 MB → 89.914 MB | 14 |
| Go 1.23 [x86_64] | Go | S | 1 | 6.360 ms | 0.000 ms | 0.000 ms | 6.360 ms → 6.360 ms | 6.400 ms | 0.000 ms | 0.000 ms | 6.400 ms → 6.400 ms | 9.586 MB | 0.000 MB | 0.000 MB | 9.586 MB → 9.586 MB | 22 |
| Go 1.23 [x86_64] | Go | M | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 12.000 MB | 0.000 MB | 0.000 MB | 12.000 MB → 12.000 MB | 22 |
| Go 1.23 [x86_64] | Go | L | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 12.469 MB | 0.000 MB | 0.000 MB | 12.469 MB → 12.469 MB | 22 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 2.360 ms | 0.000 ms | 0.000 ms | 2.360 ms → 2.360 ms | 2.400 ms | 0.000 ms | 0.000 ms | 2.400 ms → 2.400 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 13 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 5.840 ms | 0.000 ms | 0.000 ms | 5.840 ms → 5.840 ms | 5.960 ms | 0.000 ms | 0.000 ms | 5.960 ms → 5.960 ms | 3.477 MB | 0.000 MB | 0.000 MB | 3.477 MB → 3.477 MB | 13 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 11.600 ms | 0.000 ms | 0.000 ms | 11.600 ms → 11.600 ms | 12.000 ms | 0.000 ms | 0.000 ms | 12.000 ms → 12.000 ms | 5.273 MB | 0.000 MB | 0.000 MB | 5.273 MB → 5.273 MB | 13 |

</details>

<details>
<summary><strong>simple_web_server</strong> — Implementing a simple web server</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 30.478 ms | 0.000 ms | 0.000 ms | 30.478 ms → 30.478 ms | 252.853 ms | 0.000 ms | 0.000 ms | 252.853 ms → 252.853 ms | 14.445 MB | 0.000 MB | 0.000 MB | 14.445 MB → 14.445 MB | 5 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 32.079 ms | 0.000 ms | 0.000 ms | 32.079 ms → 32.079 ms | 405.854 ms | 0.000 ms | 0.000 ms | 405.854 ms → 405.854 ms | 14.094 MB | 0.000 MB | 0.000 MB | 14.094 MB → 14.094 MB | 5 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 42.509 ms | 0.000 ms | 0.000 ms | 42.509 ms → 42.509 ms | 516.452 ms | 0.000 ms | 0.000 ms | 516.452 ms → 516.452 ms | 14.289 MB | 0.000 MB | 0.000 MB | 14.289 MB → 14.289 MB | 5 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 28.752 ms | 0.000 ms | 0.000 ms | 28.752 ms → 28.752 ms | 205.742 ms | 0.000 ms | 0.000 ms | 205.742 ms → 205.742 ms | 17.547 MB | 0.000 MB | 0.000 MB | 17.547 MB → 17.547 MB | 5 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 31.214 ms | 0.000 ms | 0.000 ms | 31.214 ms → 31.214 ms | 282.277 ms | 0.000 ms | 0.000 ms | 282.277 ms → 282.277 ms | 15.539 MB | 0.000 MB | 0.000 MB | 15.539 MB → 15.539 MB | 5 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 40.040 ms | 0.000 ms | 0.000 ms | 40.040 ms → 40.040 ms | 475.621 ms | 0.000 ms | 0.000 ms | 475.621 ms → 475.621 ms | 15.340 MB | 0.000 MB | 0.000 MB | 15.340 MB → 15.340 MB | 5 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 28.316 ms | 0.000 ms | 0.000 ms | 28.316 ms → 28.316 ms | 314.442 ms | 0.000 ms | 0.000 ms | 314.442 ms → 314.442 ms | 18.152 MB | 0.000 MB | 0.000 MB | 18.152 MB → 18.152 MB | 5 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 32.941 ms | 0.000 ms | 0.000 ms | 32.941 ms → 32.941 ms | 370.161 ms | 0.000 ms | 0.000 ms | 370.161 ms → 370.161 ms | 15.254 MB | 0.000 MB | 0.000 MB | 15.254 MB → 15.254 MB | 5 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 39.335 ms | 0.000 ms | 0.000 ms | 39.335 ms → 39.335 ms | 474.807 ms | 0.000 ms | 0.000 ms | 474.807 ms → 474.807 ms | 17.520 MB | 0.000 MB | 0.000 MB | 17.520 MB → 17.520 MB | 5 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 28.547 ms | 0.000 ms | 0.000 ms | 28.547 ms → 28.547 ms | 320.280 ms | 0.000 ms | 0.000 ms | 320.280 ms → 320.280 ms | 18.164 MB | 0.000 MB | 0.000 MB | 18.164 MB → 18.164 MB | 5 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 33.721 ms | 0.000 ms | 0.000 ms | 33.721 ms → 33.721 ms | 372.131 ms | 0.000 ms | 0.000 ms | 372.131 ms → 372.131 ms | 18.984 MB | 0.000 MB | 0.000 MB | 18.984 MB → 18.984 MB | 5 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 39.737 ms | 0.000 ms | 0.000 ms | 39.737 ms → 39.737 ms | 471.598 ms | 0.000 ms | 0.000 ms | 471.598 ms → 471.598 ms | 16.738 MB | 0.000 MB | 0.000 MB | 16.738 MB → 16.738 MB | 5 |
| Python 2.7 [x86_64] | Python | S | 1 | 34.341 ms | 0.000 ms | 0.000 ms | 34.341 ms → 34.341 ms | 321.791 ms | 0.000 ms | 0.000 ms | 321.791 ms → 321.791 ms | 22.969 MB | 0.000 MB | 0.000 MB | 22.969 MB → 22.969 MB | 3 |
| Python 2.7 [x86_64] | Python | M | 1 | 59.345 ms | 0.000 ms | 0.000 ms | 59.345 ms → 59.345 ms | 396.785 ms | 0.000 ms | 0.000 ms | 396.785 ms → 396.785 ms | 17.555 MB | 0.000 MB | 0.000 MB | 17.555 MB → 17.555 MB | 3 |
| Python 2.7 [x86_64] | Python | L | 1 | 125.686 ms | 0.000 ms | 0.000 ms | 125.686 ms → 125.686 ms | 575.004 ms | 0.000 ms | 0.000 ms | 575.004 ms → 575.004 ms | 18.961 MB | 0.000 MB | 0.000 MB | 18.961 MB → 18.961 MB | 3 |
| Python 3.8 [x86_64] | Python | S | 1 | 37.821 ms | 0.000 ms | 0.000 ms | 37.821 ms → 37.821 ms | 535.400 ms | 0.000 ms | 0.000 ms | 535.400 ms → 535.400 ms | 28.781 MB | 0.000 MB | 0.000 MB | 28.781 MB → 28.781 MB | 3 |
| Python 3.8 [x86_64] | Python | M | 1 | 84.947 ms | 0.000 ms | 0.000 ms | 84.947 ms → 84.947 ms | 633.496 ms | 0.000 ms | 0.000 ms | 633.496 ms → 633.496 ms | 21.340 MB | 0.000 MB | 0.000 MB | 21.340 MB → 21.340 MB | 3 |
| Python 3.8 [x86_64] | Python | L | 1 | 134.295 ms | 0.000 ms | 0.000 ms | 134.295 ms → 134.295 ms | 754.122 ms | 0.000 ms | 0.000 ms | 754.122 ms → 754.122 ms | 22.285 MB | 0.000 MB | 0.000 MB | 22.285 MB → 22.285 MB | 3 |
| Python 3.11 [x86_64] | Python | S | 1 | 35.956 ms | 0.000 ms | 0.000 ms | 35.956 ms → 35.956 ms | 532.786 ms | 0.000 ms | 0.000 ms | 532.786 ms → 532.786 ms | 28.754 MB | 0.000 MB | 0.000 MB | 28.754 MB → 28.754 MB | 3 |
| Python 3.11 [x86_64] | Python | M | 1 | 58.088 ms | 0.000 ms | 0.000 ms | 58.088 ms → 58.088 ms | 638.605 ms | 0.000 ms | 0.000 ms | 638.605 ms → 638.605 ms | 26.922 MB | 0.000 MB | 0.000 MB | 26.922 MB → 26.922 MB | 3 |
| Python 3.11 [x86_64] | Python | L | 1 | 102.075 ms | 0.000 ms | 0.000 ms | 102.075 ms → 102.075 ms | 742.012 ms | 0.000 ms | 0.000 ms | 742.012 ms → 742.012 ms | 27.543 MB | 0.000 MB | 0.000 MB | 27.543 MB → 27.543 MB | 3 |
| Python 3.12 [x86_64] | Python | S | 1 | 35.961 ms | 0.000 ms | 0.000 ms | 35.961 ms → 35.961 ms | 599.288 ms | 0.000 ms | 0.000 ms | 599.288 ms → 599.288 ms | 25.410 MB | 0.000 MB | 0.000 MB | 25.410 MB → 25.410 MB | 3 |
| Python 3.12 [x86_64] | Python | M | 1 | 64.500 ms | 0.000 ms | 0.000 ms | 64.500 ms → 64.500 ms | 674.096 ms | 0.000 ms | 0.000 ms | 674.096 ms → 674.096 ms | 25.348 MB | 0.000 MB | 0.000 MB | 25.348 MB → 25.348 MB | 3 |
| Python 3.12 [x86_64] | Python | L | 1 | 117.531 ms | 0.000 ms | 0.000 ms | 117.531 ms → 117.531 ms | 813.058 ms | 0.000 ms | 0.000 ms | 813.058 ms → 813.058 ms | 25.539 MB | 0.000 MB | 0.000 MB | 25.539 MB → 25.539 MB | 3 |
| Java 21 [x86_64] | Java | S | 1 | 110.183 ms | 0.000 ms | 0.000 ms | 110.183 ms → 110.183 ms | 626.923 ms | 0.000 ms | 0.000 ms | 626.923 ms → 626.923 ms | 41.062 MB | 0.000 MB | 0.000 MB | 41.062 MB → 41.062 MB | 5 |
| Java 21 [x86_64] | Java | M | 1 | 281.609 ms | 0.000 ms | 0.000 ms | 281.609 ms → 281.609 ms | 867.677 ms | 0.000 ms | 0.000 ms | 867.677 ms → 867.677 ms | 42.508 MB | 0.000 MB | 0.000 MB | 42.508 MB → 42.508 MB | 5 |
| Java 21 [x86_64] | Java | L | 1 | 544.629 ms | 0.000 ms | 0.000 ms | 544.629 ms → 544.629 ms | 1.0281 s | 0.000 ms | 0.000 ms | 1.0281 s → 1.0281 s | 51.680 MB | 0.000 MB | 0.000 MB | 51.680 MB → 51.680 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 29.476 ms | 0.000 ms | 0.000 ms | 29.476 ms → 29.476 ms | 289.582 ms | 0.000 ms | 0.000 ms | 289.582 ms → 289.582 ms | 9.184 MB | 0.000 MB | 0.000 MB | 9.184 MB → 9.184 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 30.415 ms | 0.000 ms | 0.000 ms | 30.415 ms → 30.415 ms | 350.751 ms | 0.000 ms | 0.000 ms | 350.751 ms → 350.751 ms | 11.512 MB | 0.000 MB | 0.000 MB | 11.512 MB → 11.512 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 34.741 ms | 0.000 ms | 0.000 ms | 34.741 ms → 34.741 ms | 449.122 ms | 0.000 ms | 0.000 ms | 449.122 ms → 449.122 ms | 9.699 MB | 0.000 MB | 0.000 MB | 9.699 MB → 9.699 MB | 6 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 52.231 ms | 0.000 ms | 0.000 ms | 52.231 ms → 52.231 ms | 414.981 ms | 0.000 ms | 0.000 ms | 414.981 ms → 414.981 ms | 19.418 MB | 0.000 MB | 0.000 MB | 19.418 MB → 19.418 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 110.227 ms | 0.000 ms | 0.000 ms | 110.227 ms → 110.227 ms | 481.323 ms | 0.000 ms | 0.000 ms | 481.323 ms → 481.323 ms | 21.250 MB | 0.000 MB | 0.000 MB | 21.250 MB → 21.250 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 186.128 ms | 0.000 ms | 0.000 ms | 186.128 ms → 186.128 ms | 642.248 ms | 0.000 ms | 0.000 ms | 642.248 ms → 642.248 ms | 20.984 MB | 0.000 MB | 0.000 MB | 20.984 MB → 20.984 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 47.989 ms | 0.000 ms | 0.000 ms | 47.989 ms → 47.989 ms | 375.924 ms | 0.000 ms | 0.000 ms | 375.924 ms → 375.924 ms | 23.113 MB | 0.000 MB | 0.000 MB | 23.113 MB → 23.113 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 77.788 ms | 0.000 ms | 0.000 ms | 77.788 ms → 77.788 ms | 496.961 ms | 0.000 ms | 0.000 ms | 496.961 ms → 496.961 ms | 23.855 MB | 0.000 MB | 0.000 MB | 23.855 MB → 23.855 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 120.515 ms | 0.000 ms | 0.000 ms | 120.515 ms → 120.515 ms | 569.079 ms | 0.000 ms | 0.000 ms | 569.079 ms → 569.079 ms | 26.492 MB | 0.000 MB | 0.000 MB | 26.492 MB → 26.492 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 45.666 ms | 0.000 ms | 0.000 ms | 45.666 ms → 45.666 ms | 378.105 ms | 0.000 ms | 0.000 ms | 378.105 ms → 378.105 ms | 33.645 MB | 0.000 MB | 0.000 MB | 33.645 MB → 33.645 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 91.989 ms | 0.000 ms | 0.000 ms | 91.989 ms → 91.989 ms | 454.155 ms | 0.000 ms | 0.000 ms | 454.155 ms → 454.155 ms | 35.055 MB | 0.000 MB | 0.000 MB | 35.055 MB → 35.055 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 183.430 ms | 0.000 ms | 0.000 ms | 183.430 ms → 183.430 ms | 608.634 ms | 0.000 ms | 0.000 ms | 608.634 ms → 608.634 ms | 46.660 MB | 0.000 MB | 0.000 MB | 46.660 MB → 46.660 MB | 4 |
| Go 1.23 [x86_64] | Go | S | 1 | 31.473 ms | 0.000 ms | 0.000 ms | 31.473 ms → 31.473 ms | 255.204 ms | 0.000 ms | 0.000 ms | 255.204 ms → 255.204 ms | 11.977 MB | 0.000 MB | 0.000 MB | 11.977 MB → 11.977 MB | 4 |
| Go 1.23 [x86_64] | Go | M | 1 | 45.926 ms | 0.000 ms | 0.000 ms | 45.926 ms → 45.926 ms | 306.816 ms | 0.000 ms | 0.000 ms | 306.816 ms → 306.816 ms | 13.945 MB | 0.000 MB | 0.000 MB | 13.945 MB → 13.945 MB | 4 |
| Go 1.23 [x86_64] | Go | L | 1 | 73.474 ms | 0.000 ms | 0.000 ms | 73.474 ms → 73.474 ms | 423.633 ms | 0.000 ms | 0.000 ms | 423.633 ms → 423.633 ms | 14.059 MB | 0.000 MB | 0.000 MB | 14.059 MB → 14.059 MB | 4 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 26.448 ms | 0.000 ms | 0.000 ms | 26.448 ms → 26.448 ms | 256.447 ms | 0.000 ms | 0.000 ms | 256.447 ms → 256.447 ms | 9.789 MB | 0.000 MB | 0.000 MB | 9.789 MB → 9.789 MB | 3 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 30.072 ms | 0.000 ms | 0.000 ms | 30.072 ms → 30.072 ms | 301.769 ms | 0.000 ms | 0.000 ms | 301.769 ms → 301.769 ms | 9.418 MB | 0.000 MB | 0.000 MB | 9.418 MB → 9.418 MB | 3 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 35.674 ms | 0.000 ms | 0.000 ms | 35.674 ms → 35.674 ms | 409.003 ms | 0.000 ms | 0.000 ms | 409.003 ms → 409.003 ms | 9.453 MB | 0.000 MB | 0.000 MB | 9.453 MB → 9.453 MB | 3 |

</details>

<details>
<summary><strong>socket_programming</strong> — Implementing a basic networking task (socket programming)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 27.560 ms | 0.000 ms | 0.000 ms | 27.560 ms → 27.560 ms | 254.391 ms | 0.000 ms | 0.000 ms | 254.391 ms → 254.391 ms | 14.234 MB | 0.000 MB | 0.000 MB | 14.234 MB → 14.234 MB | 5 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 29.369 ms | 0.000 ms | 0.000 ms | 29.369 ms → 29.369 ms | 266.404 ms | 0.000 ms | 0.000 ms | 266.404 ms → 266.404 ms | 14.949 MB | 0.000 MB | 0.000 MB | 14.949 MB → 14.949 MB | 5 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 35.919 ms | 0.000 ms | 0.000 ms | 35.919 ms → 35.919 ms | 302.601 ms | 0.000 ms | 0.000 ms | 302.601 ms → 302.601 ms | 14.312 MB | 0.000 MB | 0.000 MB | 14.312 MB → 14.312 MB | 5 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 27.968 ms | 0.000 ms | 0.000 ms | 27.968 ms → 27.968 ms | 253.065 ms | 0.000 ms | 0.000 ms | 253.065 ms → 253.065 ms | 16.492 MB | 0.000 MB | 0.000 MB | 16.492 MB → 16.492 MB | 5 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 29.198 ms | 0.000 ms | 0.000 ms | 29.198 ms → 29.198 ms | 274.852 ms | 0.000 ms | 0.000 ms | 274.852 ms → 274.852 ms | 15.094 MB | 0.000 MB | 0.000 MB | 15.094 MB → 15.094 MB | 5 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 36.725 ms | 0.000 ms | 0.000 ms | 36.725 ms → 36.725 ms | 319.427 ms | 0.000 ms | 0.000 ms | 319.427 ms → 319.427 ms | 15.574 MB | 0.000 MB | 0.000 MB | 15.574 MB → 15.574 MB | 5 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 27.967 ms | 0.000 ms | 0.000 ms | 27.967 ms → 27.967 ms | 248.840 ms | 0.000 ms | 0.000 ms | 248.840 ms → 248.840 ms | 15.363 MB | 0.000 MB | 0.000 MB | 15.363 MB → 15.363 MB | 5 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 29.740 ms | 0.000 ms | 0.000 ms | 29.740 ms → 29.740 ms | 289.864 ms | 0.000 ms | 0.000 ms | 289.864 ms → 289.864 ms | 17.383 MB | 0.000 MB | 0.000 MB | 17.383 MB → 17.383 MB | 5 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 35.847 ms | 0.000 ms | 0.000 ms | 35.847 ms → 35.847 ms | 307.999 ms | 0.000 ms | 0.000 ms | 307.999 ms → 307.999 ms | 17.133 MB | 0.000 MB | 0.000 MB | 17.133 MB → 17.133 MB | 5 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 27.787 ms | 0.000 ms | 0.000 ms | 27.787 ms → 27.787 ms | 249.081 ms | 0.000 ms | 0.000 ms | 249.081 ms → 249.081 ms | 17.156 MB | 0.000 MB | 0.000 MB | 17.156 MB → 17.156 MB | 5 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 30.139 ms | 0.000 ms | 0.000 ms | 30.139 ms → 30.139 ms | 271.664 ms | 0.000 ms | 0.000 ms | 271.664 ms → 271.664 ms | 16.863 MB | 0.000 MB | 0.000 MB | 16.863 MB → 16.863 MB | 5 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 35.768 ms | 0.000 ms | 0.000 ms | 35.768 ms → 35.768 ms | 317.134 ms | 0.000 ms | 0.000 ms | 317.134 ms → 317.134 ms | 18.781 MB | 0.000 MB | 0.000 MB | 18.781 MB → 18.781 MB | 5 |
| Python 2.7 [x86_64] | Python | S | 1 | 70.697 ms | 0.000 ms | 0.000 ms | 70.697 ms → 70.697 ms | 287.893 ms | 0.000 ms | 0.000 ms | 287.893 ms → 287.893 ms | 17.523 MB | 0.000 MB | 0.000 MB | 17.523 MB → 17.523 MB | 3 |
| Python 2.7 [x86_64] | Python | M | 1 | 76.410 ms | 0.000 ms | 0.000 ms | 76.410 ms → 76.410 ms | 295.004 ms | 0.000 ms | 0.000 ms | 295.004 ms → 295.004 ms | 17.676 MB | 0.000 MB | 0.000 MB | 17.676 MB → 17.676 MB | 3 |
| Python 2.7 [x86_64] | Python | L | 1 | 66.957 ms | 0.000 ms | 0.000 ms | 66.957 ms → 66.957 ms | 292.386 ms | 0.000 ms | 0.000 ms | 292.386 ms → 292.386 ms | 17.656 MB | 0.000 MB | 0.000 MB | 17.656 MB → 17.656 MB | 3 |
| Python 3.8 [x86_64] | Python | S | 1 | 79.935 ms | 0.000 ms | 0.000 ms | 79.935 ms → 79.935 ms | 258.932 ms | 0.000 ms | 0.000 ms | 258.932 ms → 258.932 ms | 17.684 MB | 0.000 MB | 0.000 MB | 17.684 MB → 17.684 MB | 3 |
| Python 3.8 [x86_64] | Python | M | 1 | 82.012 ms | 0.000 ms | 0.000 ms | 82.012 ms → 82.012 ms | 258.031 ms | 0.000 ms | 0.000 ms | 258.031 ms → 258.031 ms | 17.223 MB | 0.000 MB | 0.000 MB | 17.223 MB → 17.223 MB | 3 |
| Python 3.8 [x86_64] | Python | L | 1 | 105.556 ms | 0.000 ms | 0.000 ms | 105.556 ms → 105.556 ms | 291.123 ms | 0.000 ms | 0.000 ms | 291.123 ms → 291.123 ms | 18.480 MB | 0.000 MB | 0.000 MB | 18.480 MB → 18.480 MB | 3 |
| Python 3.11 [x86_64] | Python | S | 1 | 73.176 ms | 0.000 ms | 0.000 ms | 73.176 ms → 73.176 ms | 245.553 ms | 0.000 ms | 0.000 ms | 245.553 ms → 245.553 ms | 21.012 MB | 0.000 MB | 0.000 MB | 21.012 MB → 21.012 MB | 3 |
| Python 3.11 [x86_64] | Python | M | 1 | 85.394 ms | 0.000 ms | 0.000 ms | 85.394 ms → 85.394 ms | 254.542 ms | 0.000 ms | 0.000 ms | 254.542 ms → 254.542 ms | 22.293 MB | 0.000 MB | 0.000 MB | 22.293 MB → 22.293 MB | 3 |
| Python 3.11 [x86_64] | Python | L | 1 | 112.052 ms | 0.000 ms | 0.000 ms | 112.052 ms → 112.052 ms | 290.399 ms | 0.000 ms | 0.000 ms | 290.399 ms → 290.399 ms | 24.566 MB | 0.000 MB | 0.000 MB | 24.566 MB → 24.566 MB | 3 |
| Python 3.12 [x86_64] | Python | S | 1 | 72.816 ms | 0.000 ms | 0.000 ms | 72.816 ms → 72.816 ms | 252.320 ms | 0.000 ms | 0.000 ms | 252.320 ms → 252.320 ms | 21.578 MB | 0.000 MB | 0.000 MB | 21.578 MB → 21.578 MB | 3 |
| Python 3.12 [x86_64] | Python | M | 1 | 89.429 ms | 0.000 ms | 0.000 ms | 89.429 ms → 89.429 ms | 265.653 ms | 0.000 ms | 0.000 ms | 265.653 ms → 265.653 ms | 19.598 MB | 0.000 MB | 0.000 MB | 19.598 MB → 19.598 MB | 3 |
| Python 3.12 [x86_64] | Python | L | 1 | 88.743 ms | 0.000 ms | 0.000 ms | 88.743 ms → 88.743 ms | 293.689 ms | 0.000 ms | 0.000 ms | 293.689 ms → 293.689 ms | 19.883 MB | 0.000 MB | 0.000 MB | 19.883 MB → 19.883 MB | 3 |
| Java 21 [x86_64] | Java | S | 1 | 42.200 ms | 0.000 ms | 0.000 ms | 42.200 ms → 42.200 ms | 257.722 ms | 0.000 ms | 0.000 ms | 257.722 ms → 257.722 ms | 34.219 MB | 0.000 MB | 0.000 MB | 34.219 MB → 34.219 MB | 5 |
| Java 21 [x86_64] | Java | M | 1 | 85.257 ms | 0.000 ms | 0.000 ms | 85.257 ms → 85.257 ms | 276.708 ms | 0.000 ms | 0.000 ms | 276.708 ms → 276.708 ms | 33.492 MB | 0.000 MB | 0.000 MB | 33.492 MB → 33.492 MB | 5 |
| Java 21 [x86_64] | Java | L | 1 | 90.698 ms | 0.000 ms | 0.000 ms | 90.698 ms → 90.698 ms | 329.958 ms | 0.000 ms | 0.000 ms | 329.958 ms → 329.958 ms | 34.770 MB | 0.000 MB | 0.000 MB | 34.770 MB → 34.770 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 27.516 ms | 0.000 ms | 0.000 ms | 27.516 ms → 27.516 ms | 289.221 ms | 0.000 ms | 0.000 ms | 289.221 ms → 289.221 ms | 9.574 MB | 0.000 MB | 0.000 MB | 9.574 MB → 9.574 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 29.207 ms | 0.000 ms | 0.000 ms | 29.207 ms → 29.207 ms | 267.468 ms | 0.000 ms | 0.000 ms | 267.468 ms → 267.468 ms | 9.406 MB | 0.000 MB | 0.000 MB | 9.406 MB → 9.406 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 33.161 ms | 0.000 ms | 0.000 ms | 33.161 ms → 33.161 ms | 303.018 ms | 0.000 ms | 0.000 ms | 303.018 ms → 303.018 ms | 9.363 MB | 0.000 MB | 0.000 MB | 9.363 MB → 9.363 MB | 6 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 40.048 ms | 0.000 ms | 0.000 ms | 40.048 ms → 40.048 ms | 261.862 ms | 0.000 ms | 0.000 ms | 261.862 ms → 261.862 ms | 19.715 MB | 0.000 MB | 0.000 MB | 19.715 MB → 19.715 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 58.975 ms | 0.000 ms | 0.000 ms | 58.975 ms → 58.975 ms | 284.375 ms | 0.000 ms | 0.000 ms | 284.375 ms → 284.375 ms | 19.648 MB | 0.000 MB | 0.000 MB | 19.648 MB → 19.648 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 133.195 ms | 0.000 ms | 0.000 ms | 133.195 ms → 133.195 ms | 430.225 ms | 0.000 ms | 0.000 ms | 430.225 ms → 430.225 ms | 19.762 MB | 0.000 MB | 0.000 MB | 19.762 MB → 19.762 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 44.406 ms | 0.000 ms | 0.000 ms | 44.406 ms → 44.406 ms | 260.415 ms | 0.000 ms | 0.000 ms | 260.415 ms → 260.415 ms | 20.664 MB | 0.000 MB | 0.000 MB | 20.664 MB → 20.664 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 65.253 ms | 0.000 ms | 0.000 ms | 65.253 ms → 65.253 ms | 290.727 ms | 0.000 ms | 0.000 ms | 290.727 ms → 290.727 ms | 22.270 MB | 0.000 MB | 0.000 MB | 22.270 MB → 22.270 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 90.601 ms | 0.000 ms | 0.000 ms | 90.601 ms → 90.601 ms | 348.302 ms | 0.000 ms | 0.000 ms | 348.302 ms → 348.302 ms | 22.461 MB | 0.000 MB | 0.000 MB | 22.461 MB → 22.461 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 47.402 ms | 0.000 ms | 0.000 ms | 47.402 ms → 47.402 ms | 295.301 ms | 0.000 ms | 0.000 ms | 295.301 ms → 295.301 ms | 34.594 MB | 0.000 MB | 0.000 MB | 34.594 MB → 34.594 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 78.008 ms | 0.000 ms | 0.000 ms | 78.008 ms → 78.008 ms | 309.133 ms | 0.000 ms | 0.000 ms | 309.133 ms → 309.133 ms | 43.406 MB | 0.000 MB | 0.000 MB | 43.406 MB → 43.406 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 176.738 ms | 0.000 ms | 0.000 ms | 176.738 ms → 176.738 ms | 401.402 ms | 0.000 ms | 0.000 ms | 401.402 ms → 401.402 ms | 43.359 MB | 0.000 MB | 0.000 MB | 43.359 MB → 43.359 MB | 4 |
| Go 1.23 [x86_64] | Go | S | 1 | 29.912 ms | 0.000 ms | 0.000 ms | 29.912 ms → 29.912 ms | 255.384 ms | 0.000 ms | 0.000 ms | 255.384 ms → 255.384 ms | 13.957 MB | 0.000 MB | 0.000 MB | 13.957 MB → 13.957 MB | 4 |
| Go 1.23 [x86_64] | Go | M | 1 | 34.690 ms | 0.000 ms | 0.000 ms | 34.690 ms → 34.690 ms | 295.786 ms | 0.000 ms | 0.000 ms | 295.786 ms → 295.786 ms | 14.227 MB | 0.000 MB | 0.000 MB | 14.227 MB → 14.227 MB | 4 |
| Go 1.23 [x86_64] | Go | L | 1 | 45.028 ms | 0.000 ms | 0.000 ms | 45.028 ms → 45.028 ms | 297.596 ms | 0.000 ms | 0.000 ms | 297.596 ms → 297.596 ms | 14.422 MB | 0.000 MB | 0.000 MB | 14.422 MB → 14.422 MB | 4 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 27.430 ms | 0.000 ms | 0.000 ms | 27.430 ms → 27.430 ms | 276.480 ms | 0.000 ms | 0.000 ms | 276.480 ms → 276.480 ms | 9.113 MB | 0.000 MB | 0.000 MB | 9.113 MB → 9.113 MB | 3 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 30.199 ms | 0.000 ms | 0.000 ms | 30.199 ms → 30.199 ms | 271.207 ms | 0.000 ms | 0.000 ms | 271.207 ms → 271.207 ms | 9.602 MB | 0.000 MB | 0.000 MB | 9.602 MB → 9.602 MB | 3 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 33.624 ms | 0.000 ms | 0.000 ms | 33.624 ms → 33.624 ms | 302.186 ms | 0.000 ms | 0.000 ms | 302.186 ms → 302.186 ms | 9.535 MB | 0.000 MB | 0.000 MB | 9.535 MB → 9.535 MB | 3 |

</details>

<details>
<summary><strong>sort_integers</strong> — Sorting a large array of integers</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 25.556 ms | 0.000 ms | 0.000 ms | 25.556 ms → 25.556 ms | 26.667 ms | 0.000 ms | 0.000 ms | 26.667 ms → 26.667 ms | 23.020 MB | 0.000 MB | 0.000 MB | 23.020 MB → 23.020 MB | 8 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 123.333 ms | 0.000 ms | 0.000 ms | 123.333 ms → 123.333 ms | 126.667 ms | 0.000 ms | 0.000 ms | 126.667 ms → 126.667 ms | 35.207 MB | 0.000 MB | 0.000 MB | 35.207 MB → 35.207 MB | 8 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 175.000 ms | 0.000 ms | 0.000 ms | 175.000 ms → 175.000 ms | 175.000 ms | 0.000 ms | 0.000 ms | 175.000 ms → 175.000 ms | 50.836 MB | 0.000 MB | 0.000 MB | 50.836 MB → 50.836 MB | 8 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 16.923 ms | 0.000 ms | 0.000 ms | 16.923 ms → 16.923 ms | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 22.961 MB | 0.000 MB | 0.000 MB | 22.961 MB → 22.961 MB | 7 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 28.977 MB | 0.000 MB | 0.000 MB | 28.977 MB → 28.977 MB | 7 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 34.953 MB | 0.000 MB | 0.000 MB | 34.953 MB → 34.953 MB | 7 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 21.538 ms | 0.000 ms | 0.000 ms | 21.538 ms → 21.538 ms | 26.273 MB | 0.000 MB | 0.000 MB | 26.273 MB → 26.273 MB | 7 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 32.222 ms | 0.000 ms | 0.000 ms | 32.222 ms → 32.222 ms | 32.222 ms | 0.000 ms | 0.000 ms | 32.222 ms → 32.222 ms | 30.121 MB | 0.000 MB | 0.000 MB | 30.121 MB → 30.121 MB | 7 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 36.176 MB | 0.000 MB | 0.000 MB | 36.176 MB → 36.176 MB | 7 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 27.535 MB | 0.000 MB | 0.000 MB | 27.535 MB → 27.535 MB | 7 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 32.222 ms | 0.000 ms | 0.000 ms | 32.222 ms → 32.222 ms | 33.333 ms | 0.000 ms | 0.000 ms | 33.333 ms → 33.333 ms | 31.578 MB | 0.000 MB | 0.000 MB | 31.578 MB → 31.578 MB | 7 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 52.500 ms | 0.000 ms | 0.000 ms | 52.500 ms → 52.500 ms | 52.500 ms | 0.000 ms | 0.000 ms | 52.500 ms → 52.500 ms | 35.543 MB | 0.000 MB | 0.000 MB | 35.543 MB → 35.543 MB | 7 |
| Python 2.7 [x86_64] | Python | S | 1 | 28.000 ms | 0.000 ms | 0.000 ms | 28.000 ms → 28.000 ms | 30.000 ms | 0.000 ms | 0.000 ms | 30.000 ms → 30.000 ms | 8.035 MB | 0.000 MB | 0.000 MB | 8.035 MB → 8.035 MB | 6 |
| Python 2.7 [x86_64] | Python | M | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 12.621 MB | 0.000 MB | 0.000 MB | 12.621 MB → 12.621 MB | 6 |
| Python 2.7 [x86_64] | Python | L | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 93.333 ms | 0.000 ms | 0.000 ms | 93.333 ms → 93.333 ms | 18.621 MB | 0.000 MB | 0.000 MB | 18.621 MB → 18.621 MB | 6 |
| Python 3.8 [x86_64] | Python | S | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 10.648 MB | 0.000 MB | 0.000 MB | 10.648 MB → 10.648 MB | 6 |
| Python 3.8 [x86_64] | Python | M | 1 | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 14.520 MB | 0.000 MB | 0.000 MB | 14.520 MB → 14.520 MB | 6 |
| Python 3.8 [x86_64] | Python | L | 1 | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 19.570 MB | 0.000 MB | 0.000 MB | 19.570 MB → 19.570 MB | 6 |
| Python 3.11 [x86_64] | Python | S | 1 | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 13.582 MB | 0.000 MB | 0.000 MB | 13.582 MB → 13.582 MB | 6 |
| Python 3.11 [x86_64] | Python | M | 1 | 73.333 ms | 0.000 ms | 0.000 ms | 73.333 ms → 73.333 ms | 76.667 ms | 0.000 ms | 0.000 ms | 76.667 ms → 76.667 ms | 18.137 MB | 0.000 MB | 0.000 MB | 18.137 MB → 18.137 MB | 6 |
| Python 3.11 [x86_64] | Python | L | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 95.000 ms | 0.000 ms | 0.000 ms | 95.000 ms → 95.000 ms | 24.051 MB | 0.000 MB | 0.000 MB | 24.051 MB → 24.051 MB | 6 |
| Python 3.12 [x86_64] | Python | S | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 14.836 MB | 0.000 MB | 0.000 MB | 14.836 MB → 14.836 MB | 6 |
| Python 3.12 [x86_64] | Python | M | 1 | 85.000 ms | 0.000 ms | 0.000 ms | 85.000 ms → 85.000 ms | 95.000 ms | 0.000 ms | 0.000 ms | 95.000 ms → 95.000 ms | 18.078 MB | 0.000 MB | 0.000 MB | 18.078 MB → 18.078 MB | 6 |
| Python 3.12 [x86_64] | Python | L | 1 | 100.000 ms | 0.000 ms | 0.000 ms | 100.000 ms → 100.000 ms | 105.000 ms | 0.000 ms | 0.000 ms | 105.000 ms → 105.000 ms | 23.352 MB | 0.000 MB | 0.000 MB | 23.352 MB → 23.352 MB | 6 |
| Java 21 [x86_64] | Java | S | 1 | 220.000 ms | 0.000 ms | 0.000 ms | 220.000 ms → 220.000 ms | 200.000 ms | 0.000 ms | 0.000 ms | 200.000 ms → 200.000 ms | 47.629 MB | 0.000 MB | 0.000 MB | 47.629 MB → 47.629 MB | 13 |
| Java 21 [x86_64] | Java | M | 1 | 390.000 ms | 0.000 ms | 0.000 ms | 390.000 ms → 390.000 ms | 360.000 ms | 0.000 ms | 0.000 ms | 360.000 ms → 360.000 ms | 51.098 MB | 0.000 MB | 0.000 MB | 51.098 MB → 51.098 MB | 13 |
| Java 21 [x86_64] | Java | L | 1 | 320.000 ms | 0.000 ms | 0.000 ms | 320.000 ms → 320.000 ms | 290.000 ms | 0.000 ms | 0.000 ms | 290.000 ms → 290.000 ms | 56.477 MB | 0.000 MB | 0.000 MB | 56.477 MB → 56.477 MB | 13 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 3.080 ms | 0.000 ms | 0.000 ms | 3.080 ms → 3.080 ms | 3.160 ms | 0.000 ms | 0.000 ms | 3.160 ms → 3.160 ms | 3.832 MB | 0.000 MB | 0.000 MB | 3.832 MB → 3.832 MB | 15 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 7.600 ms | 0.000 ms | 0.000 ms | 7.600 ms → 7.600 ms | 8.000 ms | 0.000 ms | 0.000 ms | 8.000 ms → 8.000 ms | 3.902 MB | 0.000 MB | 0.000 MB | 3.902 MB → 3.902 MB | 15 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 4.016 MB | 0.000 MB | 0.000 MB | 4.016 MB → 4.016 MB | 15 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 52.797 MB | 0.000 MB | 0.000 MB | 52.797 MB → 52.797 MB | 7 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 56.164 MB | 0.000 MB | 0.000 MB | 56.164 MB → 56.164 MB | 7 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 86.667 ms | 0.000 ms | 0.000 ms | 86.667 ms → 86.667 ms | 86.667 ms | 0.000 ms | 0.000 ms | 86.667 ms → 86.667 ms | 60.551 MB | 0.000 MB | 0.000 MB | 60.551 MB → 60.551 MB | 7 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 46.613 MB | 0.000 MB | 0.000 MB | 46.613 MB → 46.613 MB | 7 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 51.219 MB | 0.000 MB | 0.000 MB | 51.219 MB → 51.219 MB | 7 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 87.500 ms | 0.000 ms | 0.000 ms | 87.500 ms → 87.500 ms | 87.500 ms | 0.000 ms | 0.000 ms | 87.500 ms → 87.500 ms | 58.949 MB | 0.000 MB | 0.000 MB | 58.949 MB → 58.949 MB | 7 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 75.027 MB | 0.000 MB | 0.000 MB | 75.027 MB → 75.027 MB | 7 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 78.852 MB | 0.000 MB | 0.000 MB | 78.852 MB → 78.852 MB | 7 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 96.667 ms | 0.000 ms | 0.000 ms | 96.667 ms → 96.667 ms | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 83.578 MB | 0.000 MB | 0.000 MB | 83.578 MB → 83.578 MB | 7 |
| Go 1.23 [x86_64] | Go | S | 1 | 4.080 ms | 0.000 ms | 0.000 ms | 4.080 ms → 4.080 ms | 4.240 ms | 0.000 ms | 0.000 ms | 4.240 ms → 4.240 ms | 9.598 MB | 0.000 MB | 0.000 MB | 9.598 MB → 9.598 MB | 24 |
| Go 1.23 [x86_64] | Go | M | 1 | 7.200 ms | 0.000 ms | 0.000 ms | 7.200 ms → 7.200 ms | 7.200 ms | 0.000 ms | 0.000 ms | 7.200 ms → 7.200 ms | 9.551 MB | 0.000 MB | 0.000 MB | 9.551 MB → 9.551 MB | 24 |
| Go 1.23 [x86_64] | Go | L | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 11.867 MB | 0.000 MB | 0.000 MB | 11.867 MB → 11.867 MB | 24 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.840 ms | 0.000 ms | 0.000 ms | 1.840 ms → 1.840 ms | 1.880 ms | 0.000 ms | 0.000 ms | 1.880 ms → 1.880 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 8 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 4.080 ms | 0.000 ms | 0.000 ms | 4.080 ms → 4.080 ms | 4.160 ms | 0.000 ms | 0.000 ms | 4.160 ms → 4.160 ms | 3.477 MB | 0.000 MB | 0.000 MB | 3.477 MB → 3.477 MB | 8 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 6.720 ms | 0.000 ms | 0.000 ms | 6.720 ms → 6.720 ms | 6.800 ms | 0.000 ms | 0.000 ms | 6.800 ms → 6.800 ms | 4.605 MB | 0.000 MB | 0.000 MB | 4.605 MB → 4.605 MB | 8 |

</details>

<details>
<summary><strong>sqlite_crud</strong> — Implementing a basic database interaction (CRUD operations)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 303.819 ms | 0.000 ms | 0.000 ms | 303.819 ms → 303.819 ms | 758.852 ms | 0.000 ms | 0.000 ms | 758.852 ms → 758.852 ms | 15.660 MB | 0.000 MB | 0.000 MB | 15.660 MB → 15.660 MB | 5 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 1.1266 s | 0.000 ms | 0.000 ms | 1.1266 s → 1.1266 s | 2.1926 s | 0.000 ms | 0.000 ms | 2.1926 s → 2.1926 s | 13.957 MB | 0.000 MB | 0.000 MB | 13.957 MB → 13.957 MB | 5 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 2.8638 s | 0.000 ms | 0.000 ms | 2.8638 s → 2.8638 s | 5.1945 s | 0.000 ms | 0.000 ms | 5.1945 s → 5.1945 s | 14.227 MB | 0.000 MB | 0.000 MB | 14.227 MB → 14.227 MB | 5 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 220.633 ms | 0.000 ms | 0.000 ms | 220.633 ms → 220.633 ms | 698.711 ms | 0.000 ms | 0.000 ms | 698.711 ms → 698.711 ms | 18.281 MB | 0.000 MB | 0.000 MB | 18.281 MB → 18.281 MB | 5 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 826.956 ms | 0.000 ms | 0.000 ms | 826.956 ms → 826.956 ms | 1.9247 s | 0.000 ms | 0.000 ms | 1.9247 s → 1.9247 s | 15.660 MB | 0.000 MB | 0.000 MB | 15.660 MB → 15.660 MB | 5 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 2.0448 s | 0.000 ms | 0.000 ms | 2.0448 s → 2.0448 s | 4.3595 s | 0.000 ms | 0.000 ms | 4.3595 s → 4.3595 s | 15.238 MB | 0.000 MB | 0.000 MB | 15.238 MB → 15.238 MB | 5 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 283.681 ms | 0.000 ms | 0.000 ms | 283.681 ms → 283.681 ms | 753.642 ms | 0.000 ms | 0.000 ms | 753.642 ms → 753.642 ms | 17.270 MB | 0.000 MB | 0.000 MB | 17.270 MB → 17.270 MB | 5 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 1.1266 s | 0.000 ms | 0.000 ms | 1.1266 s → 1.1266 s | 2.2287 s | 0.000 ms | 0.000 ms | 2.2287 s → 2.2287 s | 17.270 MB | 0.000 MB | 0.000 MB | 17.270 MB → 17.270 MB | 5 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 2.8363 s | 0.000 ms | 0.000 ms | 2.8363 s → 2.8363 s | 5.2667 s | 0.000 ms | 0.000 ms | 5.2667 s → 5.2667 s | 15.250 MB | 0.000 MB | 0.000 MB | 15.250 MB → 15.250 MB | 5 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 237.025 ms | 0.000 ms | 0.000 ms | 237.025 ms → 237.025 ms | 726.869 ms | 0.000 ms | 0.000 ms | 726.869 ms → 726.869 ms | 16.867 MB | 0.000 MB | 0.000 MB | 16.867 MB → 16.867 MB | 5 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 891.173 ms | 0.000 ms | 0.000 ms | 891.173 ms → 891.173 ms | 2.0411 s | 0.000 ms | 0.000 ms | 2.0411 s → 2.0411 s | 16.848 MB | 0.000 MB | 0.000 MB | 16.848 MB → 16.848 MB | 5 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 2.2156 s | 0.000 ms | 0.000 ms | 2.2156 s → 2.2156 s | 4.5447 s | 0.000 ms | 0.000 ms | 4.5447 s → 4.5447 s | 18.836 MB | 0.000 MB | 0.000 MB | 18.836 MB → 18.836 MB | 5 |
| Python 2.7 [x86_64] | Python | S | 1 | 338.049 ms | 0.000 ms | 0.000 ms | 338.049 ms → 338.049 ms | 937.977 ms | 0.000 ms | 0.000 ms | 937.977 ms → 937.977 ms | 21.508 MB | 0.000 MB | 0.000 MB | 21.508 MB → 21.508 MB | 3 |
| Python 2.7 [x86_64] | Python | M | 1 | 1.2060 s | 0.000 ms | 0.000 ms | 1.2060 s → 1.2060 s | 2.3436 s | 0.000 ms | 0.000 ms | 2.3436 s → 2.3436 s | 20.207 MB | 0.000 MB | 0.000 MB | 20.207 MB → 20.207 MB | 3 |
| Python 2.7 [x86_64] | Python | L | 1 | 3.0483 s | 0.000 ms | 0.000 ms | 3.0483 s → 3.0483 s | 5.2573 s | 0.000 ms | 0.000 ms | 5.2573 s → 5.2573 s | 17.742 MB | 0.000 MB | 0.000 MB | 17.742 MB → 17.742 MB | 3 |
| Python 3.8 [x86_64] | Python | S | 1 | 360.121 ms | 0.000 ms | 0.000 ms | 360.121 ms → 360.121 ms | 1.0355 s | 0.000 ms | 0.000 ms | 1.0355 s → 1.0355 s | 25.383 MB | 0.000 MB | 0.000 MB | 25.383 MB → 25.383 MB | 3 |
| Python 3.8 [x86_64] | Python | M | 1 | 1.3806 s | 0.000 ms | 0.000 ms | 1.3806 s → 1.3806 s | 2.5703 s | 0.000 ms | 0.000 ms | 2.5703 s → 2.5703 s | 23.434 MB | 0.000 MB | 0.000 MB | 23.434 MB → 23.434 MB | 3 |
| Python 3.8 [x86_64] | Python | L | 1 | 3.5528 s | 0.000 ms | 0.000 ms | 3.5528 s → 3.5528 s | 5.8316 s | 0.000 ms | 0.000 ms | 5.8316 s → 5.8316 s | 23.488 MB | 0.000 MB | 0.000 MB | 23.488 MB → 23.488 MB | 3 |
| Python 3.11 [x86_64] | Python | S | 1 | 235.629 ms | 0.000 ms | 0.000 ms | 235.629 ms → 235.629 ms | 941.880 ms | 0.000 ms | 0.000 ms | 941.880 ms → 941.880 ms | 25.742 MB | 0.000 MB | 0.000 MB | 25.742 MB → 25.742 MB | 3 |
| Python 3.11 [x86_64] | Python | M | 1 | 883.443 ms | 0.000 ms | 0.000 ms | 883.443 ms → 883.443 ms | 2.1703 s | 0.000 ms | 0.000 ms | 2.1703 s → 2.1703 s | 25.219 MB | 0.000 MB | 0.000 MB | 25.219 MB → 25.219 MB | 3 |
| Python 3.11 [x86_64] | Python | L | 1 | 2.2243 s | 0.000 ms | 0.000 ms | 2.2243 s → 2.2243 s | 4.8360 s | 0.000 ms | 0.000 ms | 4.8360 s → 4.8360 s | 25.348 MB | 0.000 MB | 0.000 MB | 25.348 MB → 25.348 MB | 3 |
| Python 3.12 [x86_64] | Python | S | 1 | 242.941 ms | 0.000 ms | 0.000 ms | 242.941 ms → 242.941 ms | 1.0908 s | 0.000 ms | 0.000 ms | 1.0908 s → 1.0908 s | 25.594 MB | 0.000 MB | 0.000 MB | 25.594 MB → 25.594 MB | 3 |
| Python 3.12 [x86_64] | Python | M | 1 | 897.204 ms | 0.000 ms | 0.000 ms | 897.204 ms → 897.204 ms | 2.1979 s | 0.000 ms | 0.000 ms | 2.1979 s → 2.1979 s | 25.910 MB | 0.000 MB | 0.000 MB | 25.910 MB → 25.910 MB | 3 |
| Python 3.12 [x86_64] | Python | L | 1 | 2.2518 s | 0.000 ms | 0.000 ms | 2.2518 s → 2.2518 s | 4.8424 s | 0.000 ms | 0.000 ms | 4.8424 s → 4.8424 s | 25.695 MB | 0.000 MB | 0.000 MB | 25.695 MB → 25.695 MB | 3 |
| Java 21 [x86_64] | Java | S | 1 | 428.119 ms | 0.000 ms | 0.000 ms | 428.119 ms → 428.119 ms | 1.1698 s | 0.000 ms | 0.000 ms | 1.1698 s → 1.1698 s | 40.844 MB | 0.000 MB | 0.000 MB | 40.844 MB → 40.844 MB | 5 |
| Java 21 [x86_64] | Java | M | 1 | 1.3761 s | 0.000 ms | 0.000 ms | 1.3761 s → 1.3761 s | 2.5026 s | 0.000 ms | 0.000 ms | 2.5026 s → 2.5026 s | 42.156 MB | 0.000 MB | 0.000 MB | 42.156 MB → 42.156 MB | 5 |
| Java 21 [x86_64] | Java | L | 1 | 3.4720 s | 0.000 ms | 0.000 ms | 3.4720 s → 3.4720 s | 5.2758 s | 0.000 ms | 0.000 ms | 5.2758 s → 5.2758 s | 53.672 MB | 0.000 MB | 0.000 MB | 53.672 MB → 53.672 MB | 5 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 232.013 ms | 0.000 ms | 0.000 ms | 232.013 ms → 232.013 ms | 794.317 ms | 0.000 ms | 0.000 ms | 794.317 ms → 794.317 ms | 7.883 MB | 0.000 MB | 0.000 MB | 7.883 MB → 7.883 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 860.275 ms | 0.000 ms | 0.000 ms | 860.275 ms → 860.275 ms | 1.9985 s | 0.000 ms | 0.000 ms | 1.9985 s → 1.9985 s | 9.125 MB | 0.000 MB | 0.000 MB | 9.125 MB → 9.125 MB | 6 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 2.1233 s | 0.000 ms | 0.000 ms | 2.1233 s → 2.1233 s | 4.5090 s | 0.000 ms | 0.000 ms | 4.5090 s → 4.5090 s | 9.508 MB | 0.000 MB | 0.000 MB | 9.508 MB → 9.508 MB | 6 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 309.630 ms | 0.000 ms | 0.000 ms | 309.630 ms → 309.630 ms | 835.531 ms | 0.000 ms | 0.000 ms | 835.531 ms → 835.531 ms | 19.918 MB | 0.000 MB | 0.000 MB | 19.918 MB → 19.918 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 1.1901 s | 0.000 ms | 0.000 ms | 1.1901 s → 1.1901 s | 2.2467 s | 0.000 ms | 0.000 ms | 2.2467 s → 2.2467 s | 21.465 MB | 0.000 MB | 0.000 MB | 21.465 MB → 21.465 MB | 4 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 2.8941 s | 0.000 ms | 0.000 ms | 2.8941 s → 2.8941 s | 5.0998 s | 0.000 ms | 0.000 ms | 5.0998 s → 5.0998 s | 21.688 MB | 0.000 MB | 0.000 MB | 21.688 MB → 21.688 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 280.926 ms | 0.000 ms | 0.000 ms | 280.926 ms → 280.926 ms | 843.825 ms | 0.000 ms | 0.000 ms | 843.825 ms → 843.825 ms | 26.895 MB | 0.000 MB | 0.000 MB | 26.895 MB → 26.895 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 1.0062 s | 0.000 ms | 0.000 ms | 1.0062 s → 1.0062 s | 2.0794 s | 0.000 ms | 0.000 ms | 2.0794 s → 2.0794 s | 24.805 MB | 0.000 MB | 0.000 MB | 24.805 MB → 24.805 MB | 4 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 2.3320 s | 0.000 ms | 0.000 ms | 2.3320 s → 2.3320 s | 4.5199 s | 0.000 ms | 0.000 ms | 4.5199 s → 4.5199 s | 24.949 MB | 0.000 MB | 0.000 MB | 24.949 MB → 24.949 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 340.224 ms | 0.000 ms | 0.000 ms | 340.224 ms → 340.224 ms | 898.045 ms | 0.000 ms | 0.000 ms | 898.045 ms → 898.045 ms | 41.461 MB | 0.000 MB | 0.000 MB | 41.461 MB → 41.461 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 1.0699 s | 0.000 ms | 0.000 ms | 1.0699 s → 1.0699 s | 2.2801 s | 0.000 ms | 0.000 ms | 2.2801 s → 2.2801 s | 36.559 MB | 0.000 MB | 0.000 MB | 36.559 MB → 36.559 MB | 4 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 2.4820 s | 0.000 ms | 0.000 ms | 2.4820 s → 2.4820 s | 4.8299 s | 0.000 ms | 0.000 ms | 4.8299 s → 4.8299 s | 49.543 MB | 0.000 MB | 0.000 MB | 49.543 MB → 49.543 MB | 4 |
| Go 1.23 [x86_64] | Go | S | 1 | 210.646 ms | 0.000 ms | 0.000 ms | 210.646 ms → 210.646 ms | 744.763 ms | 0.000 ms | 0.000 ms | 744.763 ms → 744.763 ms | 16.324 MB | 0.000 MB | 0.000 MB | 16.324 MB → 16.324 MB | 4 |
| Go 1.23 [x86_64] | Go | M | 1 | 805.312 ms | 0.000 ms | 0.000 ms | 805.312 ms → 805.312 ms | 1.9411 s | 0.000 ms | 0.000 ms | 1.9411 s → 1.9411 s | 17.293 MB | 0.000 MB | 0.000 MB | 17.293 MB → 17.293 MB | 4 |
| Go 1.23 [x86_64] | Go | L | 1 | 2.0083 s | 0.000 ms | 0.000 ms | 2.0083 s → 2.0083 s | 4.3052 s | 0.000 ms | 0.000 ms | 4.3052 s → 4.3052 s | 19.371 MB | 0.000 MB | 0.000 MB | 19.371 MB → 19.371 MB | 4 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 190.743 ms | 0.000 ms | 0.000 ms | 190.743 ms → 190.743 ms | 734.999 ms | 0.000 ms | 0.000 ms | 734.999 ms → 734.999 ms | 11.293 MB | 0.000 MB | 0.000 MB | 11.293 MB → 11.293 MB | 3 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 694.093 ms | 0.000 ms | 0.000 ms | 694.093 ms → 694.093 ms | 1.8619 s | 0.000 ms | 0.000 ms | 1.8619 s → 1.8619 s | 10.895 MB | 0.000 MB | 0.000 MB | 10.895 MB → 10.895 MB | 3 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 1.7435 s | 0.000 ms | 0.000 ms | 1.7435 s → 1.7435 s | 4.1270 s | 0.000 ms | 0.000 ms | 4.1270 s → 4.1270 s | 11.273 MB | 0.000 MB | 0.000 MB | 11.273 MB → 11.273 MB | 3 |

</details>

<details>
<summary><strong>third_party_api</strong> — Integrating with a third-party API (e.g., Twitter API)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 13.077 ms | 0.000 ms | 0.000 ms | 13.077 ms → 13.077 ms | 13.077 ms | 0.000 ms | 0.000 ms | 13.077 ms → 13.077 ms | 20.816 MB | 0.000 MB | 0.000 MB | 20.816 MB → 20.816 MB | 9 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 21.070 MB | 0.000 MB | 0.000 MB | 21.070 MB → 21.070 MB | 9 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 21.090 MB | 0.000 MB | 0.000 MB | 21.090 MB → 21.090 MB | 9 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 22.969 MB | 0.000 MB | 0.000 MB | 22.969 MB → 22.969 MB | 8 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 22.973 MB | 0.000 MB | 0.000 MB | 22.973 MB → 22.973 MB | 8 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 22.977 MB | 0.000 MB | 0.000 MB | 22.977 MB → 22.977 MB | 8 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 24.039 MB | 0.000 MB | 0.000 MB | 24.039 MB → 24.039 MB | 8 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 14.615 ms | 0.000 ms | 0.000 ms | 14.615 ms → 14.615 ms | 15.385 ms | 0.000 ms | 0.000 ms | 15.385 ms → 15.385 ms | 24.207 MB | 0.000 MB | 0.000 MB | 24.207 MB → 24.207 MB | 8 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 24.172 MB | 0.000 MB | 0.000 MB | 24.172 MB → 24.172 MB | 8 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 25.617 MB | 0.000 MB | 0.000 MB | 25.617 MB → 25.617 MB | 8 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 25.629 MB | 0.000 MB | 0.000 MB | 25.629 MB → 25.629 MB | 8 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 25.586 MB | 0.000 MB | 0.000 MB | 25.586 MB → 25.586 MB | 8 |
| Python 2.7 [x86_64] | Python | S | 1 | 12.857 ms | 0.000 ms | 0.000 ms | 12.857 ms → 12.857 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 7.762 MB | 0.000 MB | 0.000 MB | 7.762 MB → 7.762 MB | 8 |
| Python 2.7 [x86_64] | Python | M | 1 | 12.857 ms | 0.000 ms | 0.000 ms | 12.857 ms → 12.857 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 7.816 MB | 0.000 MB | 0.000 MB | 7.816 MB → 7.816 MB | 8 |
| Python 2.7 [x86_64] | Python | L | 1 | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 15.714 ms | 0.000 ms | 0.000 ms | 15.714 ms → 15.714 ms | 8.129 MB | 0.000 MB | 0.000 MB | 8.129 MB → 8.129 MB | 8 |
| Python 3.8 [x86_64] | Python | S | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 10.953 MB | 0.000 MB | 0.000 MB | 10.953 MB → 10.953 MB | 8 |
| Python 3.8 [x86_64] | Python | M | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 10.965 MB | 0.000 MB | 0.000 MB | 10.965 MB → 10.965 MB | 8 |
| Python 3.8 [x86_64] | Python | L | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 10.918 MB | 0.000 MB | 0.000 MB | 10.918 MB → 10.918 MB | 8 |
| Python 3.11 [x86_64] | Python | S | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 13.520 MB | 0.000 MB | 0.000 MB | 13.520 MB → 13.520 MB | 8 |
| Python 3.11 [x86_64] | Python | M | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.512 MB | 0.000 MB | 0.000 MB | 13.512 MB → 13.512 MB | 8 |
| Python 3.11 [x86_64] | Python | L | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.465 MB | 0.000 MB | 0.000 MB | 13.465 MB → 13.465 MB | 8 |
| Python 3.12 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.695 MB | 0.000 MB | 0.000 MB | 14.695 MB → 14.695 MB | 8 |
| Python 3.12 [x86_64] | Python | M | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 14.852 MB | 0.000 MB | 0.000 MB | 14.852 MB → 14.852 MB | 8 |
| Python 3.12 [x86_64] | Python | L | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.844 MB | 0.000 MB | 0.000 MB | 14.844 MB → 14.844 MB | 8 |
| Java 21 [x86_64] | Java | S | 1 | 130.000 ms | 0.000 ms | 0.000 ms | 130.000 ms → 130.000 ms | 125.000 ms | 0.000 ms | 0.000 ms | 125.000 ms → 125.000 ms | 45.312 MB | 0.000 MB | 0.000 MB | 45.312 MB → 45.312 MB | 11 |
| Java 21 [x86_64] | Java | M | 1 | 166.667 ms | 0.000 ms | 0.000 ms | 166.667 ms → 166.667 ms | 153.333 ms | 0.000 ms | 0.000 ms | 153.333 ms → 153.333 ms | 45.211 MB | 0.000 MB | 0.000 MB | 45.211 MB → 45.211 MB | 11 |
| Java 21 [x86_64] | Java | L | 1 | 160.000 ms | 0.000 ms | 0.000 ms | 160.000 ms → 160.000 ms | 135.000 ms | 0.000 ms | 0.000 ms | 135.000 ms → 135.000 ms | 45.141 MB | 0.000 MB | 0.000 MB | 45.141 MB → 45.141 MB | 11 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 2.200 ms | 0.000 ms | 0.000 ms | 2.200 ms → 2.200 ms | 2.240 ms | 0.000 ms | 0.000 ms | 2.240 ms → 2.240 ms | 3.848 MB | 0.000 MB | 0.000 MB | 3.848 MB → 3.848 MB | 18 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 2.800 ms | 0.000 ms | 0.000 ms | 2.800 ms → 2.800 ms | 2.840 ms | 0.000 ms | 0.000 ms | 2.840 ms → 2.840 ms | 4.008 MB | 0.000 MB | 0.000 MB | 4.008 MB → 4.008 MB | 18 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 3.720 ms | 0.000 ms | 0.000 ms | 3.720 ms → 3.720 ms | 3.800 ms | 0.000 ms | 0.000 ms | 3.800 ms → 3.800 ms | 4.102 MB | 0.000 MB | 0.000 MB | 4.102 MB → 4.102 MB | 18 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 36.000 ms | 0.000 ms | 0.000 ms | 36.000 ms → 36.000 ms | 38.000 ms | 0.000 ms | 0.000 ms | 38.000 ms → 38.000 ms | 46.035 MB | 0.000 MB | 0.000 MB | 46.035 MB → 46.035 MB | 9 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 35.000 ms | 0.000 ms | 0.000 ms | 35.000 ms → 35.000 ms | 37.500 ms | 0.000 ms | 0.000 ms | 37.500 ms → 37.500 ms | 46.234 MB | 0.000 MB | 0.000 MB | 46.234 MB → 46.234 MB | 9 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 46.410 MB | 0.000 MB | 0.000 MB | 46.410 MB → 46.410 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 43.438 MB | 0.000 MB | 0.000 MB | 43.438 MB → 43.438 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 43.645 MB | 0.000 MB | 0.000 MB | 43.645 MB → 43.645 MB | 9 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 44.121 MB | 0.000 MB | 0.000 MB | 44.121 MB → 44.121 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 52.000 ms | 0.000 ms | 0.000 ms | 52.000 ms → 52.000 ms | 70.074 MB | 0.000 MB | 0.000 MB | 70.074 MB → 70.074 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 69.379 MB | 0.000 MB | 0.000 MB | 69.379 MB → 69.379 MB | 9 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 69.914 MB | 0.000 MB | 0.000 MB | 69.914 MB → 69.914 MB | 9 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.960 ms | 0.000 ms | 0.000 ms | 2.960 ms → 2.960 ms | 3.000 ms | 0.000 ms | 0.000 ms | 3.000 ms → 3.000 ms | 7.551 MB | 0.000 MB | 0.000 MB | 7.551 MB → 7.551 MB | 18 |
| Go 1.23 [x86_64] | Go | M | 1 | 4.640 ms | 0.000 ms | 0.000 ms | 4.640 ms → 4.640 ms | 4.680 ms | 0.000 ms | 0.000 ms | 4.680 ms → 4.680 ms | 9.637 MB | 0.000 MB | 0.000 MB | 9.637 MB → 9.637 MB | 18 |
| Go 1.23 [x86_64] | Go | L | 1 | 6.400 ms | 0.000 ms | 0.000 ms | 6.400 ms → 6.400 ms | 6.440 ms | 0.000 ms | 0.000 ms | 6.440 ms → 6.440 ms | 9.727 MB | 0.000 MB | 0.000 MB | 9.727 MB → 9.727 MB | 18 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.440 ms | 0.000 ms | 0.000 ms | 1.440 ms → 1.440 ms | 1.480 ms | 0.000 ms | 0.000 ms | 1.480 ms → 1.480 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 31 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 1.520 ms | 0.000 ms | 0.000 ms | 1.520 ms → 1.520 ms | 1.560 ms | 0.000 ms | 0.000 ms | 1.560 ms → 1.560 ms | 3.051 MB | 0.000 MB | 0.000 MB | 3.051 MB → 3.051 MB | 31 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 1.760 ms | 0.000 ms | 0.000 ms | 1.760 ms → 1.760 ms | 1.840 ms | 0.000 ms | 0.000 ms | 1.840 ms → 1.840 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 31 |

</details>

<details>
<summary><strong>tic_tac_toe</strong> — Implementing a basic game (tic-tac-toe)</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 27.778 ms | 0.000 ms | 0.000 ms | 27.778 ms → 27.778 ms | 28.889 ms | 0.000 ms | 0.000 ms | 28.889 ms → 28.889 ms | 21.027 MB | 0.000 MB | 0.000 MB | 21.027 MB → 21.027 MB | 32 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 90.000 ms | 0.000 ms | 0.000 ms | 90.000 ms → 90.000 ms | 93.333 ms | 0.000 ms | 0.000 ms | 93.333 ms → 93.333 ms | 20.926 MB | 0.000 MB | 0.000 MB | 20.926 MB → 20.926 MB | 32 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 175.000 ms | 0.000 ms | 0.000 ms | 175.000 ms → 175.000 ms | 21.766 MB | 0.000 MB | 0.000 MB | 21.766 MB → 21.766 MB | 32 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 17.692 ms | 0.000 ms | 0.000 ms | 17.692 ms → 17.692 ms | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 22.969 MB | 0.000 MB | 0.000 MB | 22.969 MB → 22.969 MB | 28 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 22.969 MB | 0.000 MB | 0.000 MB | 22.969 MB → 22.969 MB | 28 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 22.922 MB | 0.000 MB | 0.000 MB | 22.922 MB → 22.922 MB | 28 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 20.000 ms | 0.000 ms | 0.000 ms | 20.000 ms → 20.000 ms | 20.769 ms | 0.000 ms | 0.000 ms | 20.769 ms → 20.769 ms | 24.023 MB | 0.000 MB | 0.000 MB | 24.023 MB → 24.023 MB | 28 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 41.429 ms | 0.000 ms | 0.000 ms | 41.429 ms → 41.429 ms | 23.984 MB | 0.000 MB | 0.000 MB | 23.984 MB → 23.984 MB | 28 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 65.000 ms | 0.000 ms | 0.000 ms | 65.000 ms → 65.000 ms | 67.500 ms | 0.000 ms | 0.000 ms | 67.500 ms → 67.500 ms | 24.016 MB | 0.000 MB | 0.000 MB | 24.016 MB → 24.016 MB | 28 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 18.462 ms | 0.000 ms | 0.000 ms | 18.462 ms → 18.462 ms | 19.231 ms | 0.000 ms | 0.000 ms | 19.231 ms → 19.231 ms | 25.555 MB | 0.000 MB | 0.000 MB | 25.555 MB → 25.555 MB | 28 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 25.566 MB | 0.000 MB | 0.000 MB | 25.566 MB → 25.566 MB | 28 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 58.000 ms | 0.000 ms | 0.000 ms | 58.000 ms → 58.000 ms | 60.000 ms | 0.000 ms | 0.000 ms | 60.000 ms → 60.000 ms | 25.527 MB | 0.000 MB | 0.000 MB | 25.527 MB → 25.527 MB | 28 |
| Python 2.7 [x86_64] | Python | S | 1 | 24.000 ms | 0.000 ms | 0.000 ms | 24.000 ms → 24.000 ms | 24.000 ms | 0.000 ms | 0.000 ms | 24.000 ms → 24.000 ms | 7.945 MB | 0.000 MB | 0.000 MB | 7.945 MB → 7.945 MB | 27 |
| Python 2.7 [x86_64] | Python | M | 1 | 63.333 ms | 0.000 ms | 0.000 ms | 63.333 ms → 63.333 ms | 66.667 ms | 0.000 ms | 0.000 ms | 66.667 ms → 66.667 ms | 8.191 MB | 0.000 MB | 0.000 MB | 8.191 MB → 8.191 MB | 27 |
| Python 2.7 [x86_64] | Python | L | 1 | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 8.848 MB | 0.000 MB | 0.000 MB | 8.848 MB → 8.848 MB | 27 |
| Python 3.8 [x86_64] | Python | S | 1 | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 56.667 ms | 0.000 ms | 0.000 ms | 56.667 ms → 56.667 ms | 11.016 MB | 0.000 MB | 0.000 MB | 11.016 MB → 11.016 MB | 24 |
| Python 3.8 [x86_64] | Python | M | 1 | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 125.000 ms | 0.000 ms | 0.000 ms | 125.000 ms → 125.000 ms | 10.918 MB | 0.000 MB | 0.000 MB | 10.918 MB → 10.918 MB | 24 |
| Python 3.8 [x86_64] | Python | L | 1 | 220.000 ms | 0.000 ms | 0.000 ms | 220.000 ms → 220.000 ms | 220.000 ms | 0.000 ms | 0.000 ms | 220.000 ms → 220.000 ms | 11.016 MB | 0.000 MB | 0.000 MB | 11.016 MB → 11.016 MB | 24 |
| Python 3.11 [x86_64] | Python | S | 1 | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 13.586 MB | 0.000 MB | 0.000 MB | 13.586 MB → 13.586 MB | 24 |
| Python 3.11 [x86_64] | Python | M | 1 | 105.000 ms | 0.000 ms | 0.000 ms | 105.000 ms → 105.000 ms | 105.000 ms | 0.000 ms | 0.000 ms | 105.000 ms → 105.000 ms | 13.629 MB | 0.000 MB | 0.000 MB | 13.629 MB → 13.629 MB | 24 |
| Python 3.11 [x86_64] | Python | L | 1 | 155.000 ms | 0.000 ms | 0.000 ms | 155.000 ms → 155.000 ms | 155.000 ms | 0.000 ms | 0.000 ms | 155.000 ms → 155.000 ms | 13.746 MB | 0.000 MB | 0.000 MB | 13.746 MB → 13.746 MB | 24 |
| Python 3.12 [x86_64] | Python | S | 1 | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 14.844 MB | 0.000 MB | 0.000 MB | 14.844 MB → 14.844 MB | 24 |
| Python 3.12 [x86_64] | Python | M | 1 | 115.000 ms | 0.000 ms | 0.000 ms | 115.000 ms → 115.000 ms | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 14.727 MB | 0.000 MB | 0.000 MB | 14.727 MB → 14.727 MB | 24 |
| Python 3.12 [x86_64] | Python | L | 1 | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 175.000 ms | 0.000 ms | 0.000 ms | 175.000 ms → 175.000 ms | 14.906 MB | 0.000 MB | 0.000 MB | 14.906 MB → 14.906 MB | 24 |
| Java 21 [x86_64] | Java | S | 1 | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 170.000 ms | 0.000 ms | 0.000 ms | 170.000 ms → 170.000 ms | 48.516 MB | 0.000 MB | 0.000 MB | 48.516 MB → 48.516 MB | 32 |
| Java 21 [x86_64] | Java | M | 1 | 420.000 ms | 0.000 ms | 0.000 ms | 420.000 ms → 420.000 ms | 400.000 ms | 0.000 ms | 0.000 ms | 400.000 ms → 400.000 ms | 49.836 MB | 0.000 MB | 0.000 MB | 49.836 MB → 49.836 MB | 32 |
| Java 21 [x86_64] | Java | L | 1 | 420.000 ms | 0.000 ms | 0.000 ms | 420.000 ms → 420.000 ms | 400.000 ms | 0.000 ms | 0.000 ms | 400.000 ms → 400.000 ms | 50.844 MB | 0.000 MB | 0.000 MB | 50.844 MB → 50.844 MB | 32 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 2.720 ms | 0.000 ms | 0.000 ms | 2.720 ms → 2.720 ms | 2.760 ms | 0.000 ms | 0.000 ms | 2.760 ms → 2.760 ms | 3.711 MB | 0.000 MB | 0.000 MB | 3.711 MB → 3.711 MB | 37 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 5.960 ms | 0.000 ms | 0.000 ms | 5.960 ms → 5.960 ms | 6.040 ms | 0.000 ms | 0.000 ms | 6.040 ms → 6.040 ms | 3.711 MB | 0.000 MB | 0.000 MB | 3.711 MB → 3.711 MB | 37 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 10.000 ms | 0.000 ms | 0.000 ms | 10.000 ms → 10.000 ms | 10.400 ms | 0.000 ms | 0.000 ms | 10.400 ms → 10.400 ms | 3.699 MB | 0.000 MB | 0.000 MB | 3.699 MB → 3.699 MB | 37 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 54.285 MB | 0.000 MB | 0.000 MB | 54.285 MB → 54.285 MB | 24 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 68.000 ms | 0.000 ms | 0.000 ms | 68.000 ms → 68.000 ms | 57.461 MB | 0.000 MB | 0.000 MB | 57.461 MB → 57.461 MB | 24 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 76.667 ms | 0.000 ms | 0.000 ms | 76.667 ms → 76.667 ms | 57.652 MB | 0.000 MB | 0.000 MB | 57.652 MB → 57.652 MB | 24 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 56.000 ms | 0.000 ms | 0.000 ms | 56.000 ms → 56.000 ms | 54.000 ms | 0.000 ms | 0.000 ms | 54.000 ms → 54.000 ms | 52.867 MB | 0.000 MB | 0.000 MB | 52.867 MB → 52.867 MB | 24 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 70.000 ms | 0.000 ms | 0.000 ms | 70.000 ms → 70.000 ms | 68.000 ms | 0.000 ms | 0.000 ms | 68.000 ms → 68.000 ms | 58.645 MB | 0.000 MB | 0.000 MB | 58.645 MB → 58.645 MB | 24 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 80.000 ms | 0.000 ms | 0.000 ms | 80.000 ms → 80.000 ms | 75.000 ms | 0.000 ms | 0.000 ms | 75.000 ms → 75.000 ms | 64.680 MB | 0.000 MB | 0.000 MB | 64.680 MB → 64.680 MB | 24 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 62.500 ms | 0.000 ms | 0.000 ms | 62.500 ms → 62.500 ms | 57.500 ms | 0.000 ms | 0.000 ms | 57.500 ms → 57.500 ms | 76.336 MB | 0.000 MB | 0.000 MB | 76.336 MB → 76.336 MB | 24 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 83.333 ms | 0.000 ms | 0.000 ms | 83.333 ms → 83.333 ms | 73.333 ms | 0.000 ms | 0.000 ms | 73.333 ms → 73.333 ms | 77.898 MB | 0.000 MB | 0.000 MB | 77.898 MB → 77.898 MB | 24 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 103.333 ms | 0.000 ms | 0.000 ms | 103.333 ms → 103.333 ms | 96.667 ms | 0.000 ms | 0.000 ms | 96.667 ms → 96.667 ms | 81.176 MB | 0.000 MB | 0.000 MB | 81.176 MB → 81.176 MB | 24 |
| Go 1.23 [x86_64] | Go | S | 1 | 3.080 ms | 0.000 ms | 0.000 ms | 3.080 ms → 3.080 ms | 3.080 ms | 0.000 ms | 0.000 ms | 3.080 ms → 3.080 ms | 7.551 MB | 0.000 MB | 0.000 MB | 7.551 MB → 7.551 MB | 42 |
| Go 1.23 [x86_64] | Go | M | 1 | 5.160 ms | 0.000 ms | 0.000 ms | 5.160 ms → 5.160 ms | 5.200 ms | 0.000 ms | 0.000 ms | 5.200 ms → 5.200 ms | 9.574 MB | 0.000 MB | 0.000 MB | 9.574 MB → 9.574 MB | 42 |
| Go 1.23 [x86_64] | Go | L | 1 | 7.280 ms | 0.000 ms | 0.000 ms | 7.280 ms → 7.280 ms | 7.360 ms | 0.000 ms | 0.000 ms | 7.360 ms → 7.360 ms | 9.578 MB | 0.000 MB | 0.000 MB | 9.578 MB → 9.578 MB | 42 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.600 ms | 0.000 ms | 0.000 ms | 1.600 ms → 1.600 ms | 1.600 ms | 0.000 ms | 0.000 ms | 1.600 ms → 1.600 ms | 3.051 MB | 0.000 MB | 0.000 MB | 3.051 MB → 3.051 MB | 25 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 2.560 ms | 0.000 ms | 0.000 ms | 2.560 ms → 2.560 ms | 2.640 ms | 0.000 ms | 0.000 ms | 2.640 ms → 2.640 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 25 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 3.960 ms | 0.000 ms | 0.000 ms | 3.960 ms → 3.960 ms | 4.040 ms | 0.000 ms | 0.000 ms | 4.040 ms → 4.040 ms | 3.105 MB | 0.000 MB | 0.000 MB | 3.105 MB → 3.105 MB | 25 |

</details>

<details>
<summary><strong>web_scraper</strong> — Implementing a simple web scraper</summary>

| Runtime | Family | Size | Samples | CPU median | CPU σ | CPU ±95% CI | CPU range | Wall median | Wall σ | Wall ±95% CI | Wall range | Memory median | Memory σ | Memory ±95% CI | Memory range | LOC |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---|---:|
| PHP 5.6 [x86_64] | PHP | S | 1 | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 20.961 MB | 0.000 MB | 0.000 MB | 20.961 MB → 20.961 MB | 15 |
| PHP 5.6 [x86_64] | PHP | M | 1 | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 21.105 MB | 0.000 MB | 0.000 MB | 21.105 MB → 21.105 MB | 15 |
| PHP 5.6 [x86_64] | PHP | L | 1 | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 13.600 ms | 0.000 ms | 0.000 ms | 13.600 ms → 13.600 ms | 21.059 MB | 0.000 MB | 0.000 MB | 21.059 MB → 21.059 MB | 15 |
| PHP 7.4 [x86_64] | PHP | S | 1 | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 22.957 MB | 0.000 MB | 0.000 MB | 22.957 MB → 22.957 MB | 14 |
| PHP 7.4 [x86_64] | PHP | M | 1 | 12.400 ms | 0.000 ms | 0.000 ms | 12.400 ms → 12.400 ms | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 23.012 MB | 0.000 MB | 0.000 MB | 23.012 MB → 23.012 MB | 14 |
| PHP 7.4 [x86_64] | PHP | L | 1 | 12.800 ms | 0.000 ms | 0.000 ms | 12.800 ms → 12.800 ms | 13.200 ms | 0.000 ms | 0.000 ms | 13.200 ms → 13.200 ms | 22.992 MB | 0.000 MB | 0.000 MB | 22.992 MB → 22.992 MB | 14 |
| PHP 7.2 [x86_64] | PHP | S | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 24.312 MB | 0.000 MB | 0.000 MB | 24.312 MB → 24.312 MB | 14 |
| PHP 7.2 [x86_64] | PHP | M | 1 | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 15.600 ms | 0.000 ms | 0.000 ms | 15.600 ms → 15.600 ms | 24.254 MB | 0.000 MB | 0.000 MB | 24.254 MB → 24.254 MB | 14 |
| PHP 7.2 [x86_64] | PHP | L | 1 | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 15.200 ms | 0.000 ms | 0.000 ms | 15.200 ms → 15.200 ms | 24.293 MB | 0.000 MB | 0.000 MB | 24.293 MB → 24.293 MB | 14 |
| PHP 8.4 [x86_64] | PHP | S | 1 | 14.000 ms | 0.000 ms | 0.000 ms | 14.000 ms → 14.000 ms | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 25.609 MB | 0.000 MB | 0.000 MB | 25.609 MB → 25.609 MB | 14 |
| PHP 8.4 [x86_64] | PHP | M | 1 | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 25.578 MB | 0.000 MB | 0.000 MB | 25.578 MB → 25.578 MB | 14 |
| PHP 8.4 [x86_64] | PHP | L | 1 | 14.400 ms | 0.000 ms | 0.000 ms | 14.400 ms → 14.400 ms | 14.800 ms | 0.000 ms | 0.000 ms | 14.800 ms → 14.800 ms | 25.664 MB | 0.000 MB | 0.000 MB | 25.664 MB → 25.664 MB | 14 |
| Python 2.7 [x86_64] | Python | S | 1 | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 7.703 MB | 0.000 MB | 0.000 MB | 7.703 MB → 7.703 MB | 15 |
| Python 2.7 [x86_64] | Python | M | 1 | 12.857 ms | 0.000 ms | 0.000 ms | 12.857 ms → 12.857 ms | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 7.910 MB | 0.000 MB | 0.000 MB | 7.910 MB → 7.910 MB | 15 |
| Python 2.7 [x86_64] | Python | L | 1 | 14.286 ms | 0.000 ms | 0.000 ms | 14.286 ms → 14.286 ms | 15.714 ms | 0.000 ms | 0.000 ms | 15.714 ms → 15.714 ms | 7.816 MB | 0.000 MB | 0.000 MB | 7.816 MB → 7.816 MB | 15 |
| Python 3.8 [x86_64] | Python | S | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 10.680 MB | 0.000 MB | 0.000 MB | 10.680 MB → 10.680 MB | 15 |
| Python 3.8 [x86_64] | Python | M | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 10.426 MB | 0.000 MB | 0.000 MB | 10.426 MB → 10.426 MB | 15 |
| Python 3.8 [x86_64] | Python | L | 1 | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 10.496 MB | 0.000 MB | 0.000 MB | 10.496 MB → 10.496 MB | 15 |
| Python 3.11 [x86_64] | Python | S | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 13.617 MB | 0.000 MB | 0.000 MB | 13.617 MB → 13.617 MB | 15 |
| Python 3.11 [x86_64] | Python | M | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.586 MB | 0.000 MB | 0.000 MB | 13.586 MB → 13.586 MB | 15 |
| Python 3.11 [x86_64] | Python | L | 1 | 43.333 ms | 0.000 ms | 0.000 ms | 43.333 ms → 43.333 ms | 46.667 ms | 0.000 ms | 0.000 ms | 46.667 ms → 46.667 ms | 13.551 MB | 0.000 MB | 0.000 MB | 13.551 MB → 13.551 MB | 15 |
| Python 3.12 [x86_64] | Python | S | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.539 MB | 0.000 MB | 0.000 MB | 14.539 MB → 14.539 MB | 15 |
| Python 3.12 [x86_64] | Python | M | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.617 MB | 0.000 MB | 0.000 MB | 14.617 MB → 14.617 MB | 15 |
| Python 3.12 [x86_64] | Python | L | 1 | 50.000 ms | 0.000 ms | 0.000 ms | 50.000 ms → 50.000 ms | 53.333 ms | 0.000 ms | 0.000 ms | 53.333 ms → 53.333 ms | 14.766 MB | 0.000 MB | 0.000 MB | 14.766 MB → 14.766 MB | 15 |
| Java 21 [x86_64] | Java | S | 1 | 120.000 ms | 0.000 ms | 0.000 ms | 120.000 ms → 120.000 ms | 106.667 ms | 0.000 ms | 0.000 ms | 106.667 ms → 106.667 ms | 44.797 MB | 0.000 MB | 0.000 MB | 44.797 MB → 44.797 MB | 22 |
| Java 21 [x86_64] | Java | M | 1 | 93.333 ms | 0.000 ms | 0.000 ms | 93.333 ms → 93.333 ms | 83.333 ms | 0.000 ms | 0.000 ms | 83.333 ms → 83.333 ms | 44.770 MB | 0.000 MB | 0.000 MB | 44.770 MB → 44.770 MB | 22 |
| Java 21 [x86_64] | Java | L | 1 | 130.000 ms | 0.000 ms | 0.000 ms | 130.000 ms → 130.000 ms | 105.000 ms | 0.000 ms | 0.000 ms | 105.000 ms → 105.000 ms | 44.863 MB | 0.000 MB | 0.000 MB | 44.863 MB → 44.863 MB | 22 |
| C++ (GCC 14) [x86_64] | C++ | S | 1 | 1.760 ms | 0.000 ms | 0.000 ms | 1.760 ms → 1.760 ms | 1.800 ms | 0.000 ms | 0.000 ms | 1.800 ms → 1.800 ms | 3.848 MB | 0.000 MB | 0.000 MB | 3.848 MB → 3.848 MB | 28 |
| C++ (GCC 14) [x86_64] | C++ | M | 1 | 1.800 ms | 0.000 ms | 0.000 ms | 1.800 ms → 1.800 ms | 1.840 ms | 0.000 ms | 0.000 ms | 1.840 ms → 1.840 ms | 3.852 MB | 0.000 MB | 0.000 MB | 3.852 MB → 3.852 MB | 28 |
| C++ (GCC 14) [x86_64] | C++ | L | 1 | 2.080 ms | 0.000 ms | 0.000 ms | 2.080 ms → 2.080 ms | 2.120 ms | 0.000 ms | 0.000 ms | 2.120 ms → 2.120 ms | 3.852 MB | 0.000 MB | 0.000 MB | 3.852 MB → 3.852 MB | 28 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | S | 1 | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 46.098 MB | 0.000 MB | 0.000 MB | 46.098 MB → 46.098 MB | 14 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | M | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 38.571 ms | 0.000 ms | 0.000 ms | 38.571 ms → 38.571 ms | 46.109 MB | 0.000 MB | 0.000 MB | 46.109 MB → 46.109 MB | 14 |
| Node.js 22 [x86_64] | JavaScript (Node.js) | L | 1 | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 40.000 ms | 0.000 ms | 0.000 ms | 40.000 ms → 40.000 ms | 46.176 MB | 0.000 MB | 0.000 MB | 46.176 MB → 46.176 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | S | 1 | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 37.143 ms | 0.000 ms | 0.000 ms | 37.143 ms → 37.143 ms | 43.320 MB | 0.000 MB | 0.000 MB | 43.320 MB → 43.320 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | M | 1 | 34.286 ms | 0.000 ms | 0.000 ms | 34.286 ms → 34.286 ms | 35.714 ms | 0.000 ms | 0.000 ms | 35.714 ms → 35.714 ms | 43.297 MB | 0.000 MB | 0.000 MB | 43.297 MB → 43.297 MB | 14 |
| Bun 1.3.12 [x86_64] | JavaScript (Node.js) | L | 1 | 41.429 ms | 0.000 ms | 0.000 ms | 41.429 ms → 41.429 ms | 41.429 ms | 0.000 ms | 0.000 ms | 41.429 ms → 41.429 ms | 43.559 MB | 0.000 MB | 0.000 MB | 43.559 MB → 43.559 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | S | 1 | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 42.000 ms | 0.000 ms | 0.000 ms | 42.000 ms → 42.000 ms | 69.688 MB | 0.000 MB | 0.000 MB | 69.688 MB → 69.688 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | M | 1 | 48.000 ms | 0.000 ms | 0.000 ms | 48.000 ms → 48.000 ms | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 69.270 MB | 0.000 MB | 0.000 MB | 69.270 MB → 69.270 MB | 14 |
| Deno 2.7.6 [x86_64] | JavaScript (Node.js) | L | 1 | 46.000 ms | 0.000 ms | 0.000 ms | 46.000 ms → 46.000 ms | 44.000 ms | 0.000 ms | 0.000 ms | 44.000 ms → 44.000 ms | 69.422 MB | 0.000 MB | 0.000 MB | 69.422 MB → 69.422 MB | 14 |
| Go 1.23 [x86_64] | Go | S | 1 | 2.600 ms | 0.000 ms | 0.000 ms | 2.600 ms → 2.600 ms | 2.600 ms | 0.000 ms | 0.000 ms | 2.600 ms → 2.600 ms | 7.551 MB | 0.000 MB | 0.000 MB | 7.551 MB → 7.551 MB | 23 |
| Go 1.23 [x86_64] | Go | M | 1 | 2.680 ms | 0.000 ms | 0.000 ms | 2.680 ms → 2.680 ms | 2.720 ms | 0.000 ms | 0.000 ms | 2.720 ms → 2.720 ms | 7.578 MB | 0.000 MB | 0.000 MB | 7.578 MB → 7.578 MB | 23 |
| Go 1.23 [x86_64] | Go | L | 1 | 2.800 ms | 0.000 ms | 0.000 ms | 2.800 ms → 2.800 ms | 2.800 ms | 0.000 ms | 0.000 ms | 2.800 ms → 2.800 ms | 9.344 MB | 0.000 MB | 0.000 MB | 9.344 MB → 9.344 MB | 23 |
| Rust 1.82 [x86_64] | Rust | S | 1 | 1.280 ms | 0.000 ms | 0.000 ms | 1.280 ms → 1.280 ms | 1.320 ms | 0.000 ms | 0.000 ms | 1.320 ms → 1.320 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 25 |
| Rust 1.82 [x86_64] | Rust | M | 1 | 1.360 ms | 0.000 ms | 0.000 ms | 1.360 ms → 1.360 ms | 1.400 ms | 0.000 ms | 0.000 ms | 1.400 ms → 1.400 ms | 3.059 MB | 0.000 MB | 0.000 MB | 3.059 MB → 3.059 MB | 25 |
| Rust 1.82 [x86_64] | Rust | L | 1 | 1.440 ms | 0.000 ms | 0.000 ms | 1.440 ms → 1.440 ms | 1.520 ms | 0.000 ms | 0.000 ms | 1.520 ms → 1.520 ms | 3.027 MB | 0.000 MB | 0.000 MB | 3.027 MB → 3.027 MB | 25 |

</details>


### What the current executable tests do

This published snapshot uses deterministic local fixtures and a checksum-style output for each task so every language performs the same work and produces a comparable, verifiable result.

#### `ai_service_integration` — Integrating with AI services (e.g., OpenAI API or MCP services)

- **How it works:** Each implementation reads a deterministic mock AI-service response set, extracts prompts, outputs, token counts, and the model name, and computes a checksum over the full interaction set.
- **What it tests:** This measures integration-style response handling for AI outputs, repeated string processing, token-count extraction, and the runtime overhead of consuming structured mock LLM results offline.
- **Why this task matters:** Structured AI-style response parsing and integration glue.
- **Tags:** `integration`, `ai`, `json`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/ai_service_integration.php) · [Python](tasks/implementations/python/tasks/ai_service_integration.py) · [Java](tasks/implementations/java/tasks/ai_service_integration.java) · [C++](tasks/implementations/cpp/tasks/ai_service_integration.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/ai_service_integration.js) · [Go](tasks/implementations/go/tasks/ai_service_integration.go) · [Rust](tasks/implementations/rust/tasks/ai_service_integration.rs)

#### `api_client` — Implementing a simple API client (fetching data from a public API)

- **How it works:** Each implementation reads a deterministic mock public-API JSON payload from the fixtures, parses the returned item records, and computes a checksum from IDs, names, and numeric values.
- **What it tests:** This benchmarks client-side payload parsing, string extraction, numeric conversion, and the general overhead of consuming a simple third-party style API response.
- **Why this task matters:** JSON/API client parsing and glue code.
- **Tags:** `integration`, `api`, `json`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/api_client.php) · [Python](tasks/implementations/python/tasks/api_client.py) · [Java](tasks/implementations/java/tasks/api_client.java) · [C++](tasks/implementations/cpp/tasks/api_client.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/api_client.js) · [Go](tasks/implementations/go/tasks/api_client.go) · [Rust](tasks/implementations/rust/tasks/api_client.rs)

#### `basic_blockchain` — Implementing a basic blockchain

- **How it works:** Each implementation reads deterministic blocks of synthetic transactions, links them through a rolling previous-hash value, computes a simple chain hash for every block, and accumulates a final checksum for the whole chain.
- **What it tests:** This measures integer-heavy stateful iteration, repeated hashing/mixing work, and the overhead of maintaining a minimal blockchain-style data pipeline without relying on external cryptography libraries.
- **Why this task matters:** Stateful hashing-style computation with sequential dependencies.
- **Tags:** `compute`, `stateful`, `hashing`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/basic_blockchain.php) · [Python](tasks/implementations/python/tasks/basic_blockchain.py) · [Java](tasks/implementations/java/tasks/basic_blockchain.java) · [C++](tasks/implementations/cpp/tasks/basic_blockchain.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/basic_blockchain.js) · [Go](tasks/implementations/go/tasks/basic_blockchain.go) · [Rust](tasks/implementations/rust/tasks/basic_blockchain.rs)

#### `basic_web_application` — Implementing a basic web application (a to-do list)

- **How it works:** Each implementation starts a local HTTP to-do style web application, and the neutral browser driver adds and toggles deterministic tasks before computing a checksum from the rendered list state.
- **What it tests:** This measures web-application serving overhead plus browser-side state updates, list rendering, event handling, and the general cost of a small interactive CRUD-style UI contract.
- **Why this task matters:** Interactive web CRUD behavior in a browser contract.
- **Tags:** `ui`, `browser`, `crud`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/basic_web_application.php) · [Python](tasks/implementations/python/tasks/basic_web_application.py) · [Java](tasks/implementations/java/tasks/basic_web_application.java) · [C++](tasks/implementations/cpp/tasks/basic_web_application.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/basic_web_application.js) · [Go](tasks/implementations/go/tasks/basic_web_application.go) · [Rust](tasks/implementations/rust/tasks/basic_web_application.rs)

#### `binary_search_tree` — Implementing a basic data structure (binary search tree)

- **How it works:** Each implementation reads a deterministic sequence of insert values and query values, builds an in-memory binary search tree from the inserts, then searches every query and sums the values that are found.
- **What it tests:** This measures pointer-heavy data structure work, heap allocation patterns, branch behavior, and the ergonomics of implementing a classic mutable tree without external libraries.
- **Why this task matters:** Pointer-heavy data structure work and allocation behavior.
- **Tags:** `compute`, `data-structure`, `memory`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/binary_search_tree.php) · [Python](tasks/implementations/python/tasks/binary_search_tree.py) · [Java](tasks/implementations/java/tasks/binary_search_tree.java) · [C++](tasks/implementations/cpp/tasks/binary_search_tree.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/binary_search_tree.js) · [Go](tasks/implementations/go/tasks/binary_search_tree.go) · [Rust](tasks/implementations/rust/tasks/binary_search_tree.rs)

#### `chat_application` — Implementing a simple chat application

- **How it works:** Each implementation starts a minimal TCP chat-style server, accepts short line-oriented client messages, prepends a deterministic marker to each payload, and the benchmark driver measures repeated round trips over loopback networking.
- **What it tests:** This focuses on TCP socket setup, connection handling, message framing, short-lived request-response behavior, and the language runtime’s overhead for small network services.
- **Why this task matters:** TCP startup and tiny message round trips.
- **Tags:** `service`, `networking`, `tcp`, `startup-sensitive`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/chat_application.php) · [Python](tasks/implementations/python/tasks/chat_application.py) · [Java](tasks/implementations/java/tasks/chat_application.java) · [C++](tasks/implementations/cpp/tasks/chat_application.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/chat_application.js) · [Go](tasks/implementations/go/tasks/chat_application.go) · [Rust](tasks/implementations/rust/tasks/chat_application.rs)

#### `cli_file_search` — Implementing a basic command-line tool (a file search utility)

- **How it works:** Each implementation recursively walks a deterministic directory tree of text files, scans file contents line by line, and counts how many lines contain the target token `needle`.
- **What it tests:** This benchmarks directory traversal, path handling, repeated file opening, line scanning, and the amount of glue code each language needs for a basic command-line search utility.
- **Why this task matters:** Filesystem traversal and text scanning.
- **Tags:** `compute`, `cli`, `io`, `filesystem`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/cli_file_search.php) · [Python](tasks/implementations/python/tasks/cli_file_search.py) · [Java](tasks/implementations/java/tasks/cli_file_search.java) · [C++](tasks/implementations/cpp/tasks/cli_file_search.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/cli_file_search.js) · [Go](tasks/implementations/go/tasks/cli_file_search.go) · [Rust](tasks/implementations/rust/tasks/cli_file_search.rs)

#### `csv_parsing` — Processing a large dataset (CSV file parsing)

- **How it works:** Each implementation opens the same generated CSV file, skips the header, parses numeric columns from every row, and accumulates a deterministic total that is printed at the end.
- **What it tests:** This measures text parsing overhead, per-row iteration cost, string-to-number conversion, streaming/file I/O behavior, and the standard library's ergonomics for simple data ingestion.
- **Why this task matters:** I/O plus text parsing overhead.
- **Tags:** `compute`, `io`, `data`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/csv_parsing.php) · [Python](tasks/implementations/python/tasks/csv_parsing.py) · [Java](tasks/implementations/java/tasks/csv_parsing.java) · [C++](tasks/implementations/cpp/tasks/csv_parsing.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/csv_parsing.js) · [Go](tasks/implementations/go/tasks/csv_parsing.go) · [Rust](tasks/implementations/rust/tasks/csv_parsing.rs)

#### `data_visualization` — Implementing a simple data visualization task (plotting a graph)

- **How it works:** Each implementation starts a local HTTP UI that serves a deterministic visualization page, and the neutral browser driver renders a fixed bar-chart dataset in the DOM and computes a checksum from the resulting bars.
- **What it tests:** This benchmarks UI-serving overhead together with browser rendering, DOM construction, layout/style work, and the cost of a simple deterministic data-visualization workflow.
- **Why this task matters:** UI serving plus browser render/layout work.
- **Tags:** `ui`, `browser`, `visualization`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/data_visualization.php) · [Python](tasks/implementations/python/tasks/data_visualization.py) · [Java](tasks/implementations/java/tasks/data_visualization.java) · [C++](tasks/implementations/cpp/tasks/data_visualization.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/data_visualization.js) · [Go](tasks/implementations/go/tasks/data_visualization.go) · [Rust](tasks/implementations/rust/tasks/data_visualization.rs)

#### `decision_tree` — Implementing a basic machine learning model (decision tree)

- **How it works:** Each implementation trains the same small deterministic decision tree on a synthetic labeled dataset using fixed split candidates, then evaluates the model across the dataset and prints a checksum based on accuracy and predictions.
- **What it tests:** This measures structured CSV parsing, repeated impurity calculations, recursive model construction, and a basic but realistic machine-learning training workload that stays comparable across languages.
- **Why this task matters:** Control flow plus ML-style model-building workload.
- **Tags:** `compute`, `ml`, `control-flow`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/decision_tree.php) · [Python](tasks/implementations/python/tasks/decision_tree.py) · [Java](tasks/implementations/java/tasks/decision_tree.java) · [C++](tasks/implementations/cpp/tasks/decision_tree.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/decision_tree.js) · [Go](tasks/implementations/go/tasks/decision_tree.go) · [Rust](tasks/implementations/rust/tasks/decision_tree.rs)

#### `file_io_large` — Performing file I/O operations on a large file

- **How it works:** Each implementation opens the same large deterministic text file, reads it sequentially, parses one integer per line, and accumulates a total checksum that is printed at the end.
- **What it tests:** This focuses on streaming file I/O, text parsing overhead, buffered reading behavior, and the runtime cost of turning a large raw file into usable numeric values.
- **Why this task matters:** Filesystem streaming and parsing overhead.
- **Tags:** `compute`, `io`, `filesystem`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/file_io_large.php) · [Python](tasks/implementations/python/tasks/file_io_large.py) · [Java](tasks/implementations/java/tasks/file_io_large.java) · [C++](tasks/implementations/cpp/tasks/file_io_large.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/file_io_large.js) · [Go](tasks/implementations/go/tasks/file_io_large.go) · [Rust](tasks/implementations/rust/tasks/file_io_large.rs)

#### `gui_calculator` — Implementing a simple GUI application (a calculator)

- **How it works:** Each implementation starts a local HTTP UI that exposes a browser-based calculator contract, and the neutral headless browser driver performs deterministic add/multiply interactions while collecting a checksum from the rendered result state.
- **What it tests:** This measures HTTP UI serving overhead plus real browser-side event handling, DOM updates, and the cost of driving a tiny interactive calculator contract through a consistent headless-browser workflow.
- **Why this task matters:** UI serving plus browser-side interaction overhead.
- **Tags:** `ui`, `browser`, `startup-sensitive`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/gui_calculator.php) · [Python](tasks/implementations/python/tasks/gui_calculator.py) · [Java](tasks/implementations/java/tasks/gui_calculator.java) · [C++](tasks/implementations/cpp/tasks/gui_calculator.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/gui_calculator.js) · [Go](tasks/implementations/go/tasks/gui_calculator.go) · [Rust](tasks/implementations/rust/tasks/gui_calculator.rs)

#### `image_resizing` — Implementing a basic image processing task (resizing an image)

- **How it works:** Each implementation loads the same deterministic PPM image fixture, downsamples it by a fixed factor using nearest-neighbor sampling, and prints a checksum over the resized pixels instead of writing an output file.
- **What it tests:** This exercises structured file parsing, array indexing, pixel-wise numeric loops, and a simple but realistic image-processing workload using only standard library tools.
- **Why this task matters:** Pixel-oriented compute with structured file parsing.
- **Tags:** `compute`, `image`, `numeric`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/image_resizing.php) · [Python](tasks/implementations/python/tasks/image_resizing.py) · [Java](tasks/implementations/java/tasks/image_resizing.java) · [C++](tasks/implementations/cpp/tasks/image_resizing.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/image_resizing.js) · [Go](tasks/implementations/go/tasks/image_resizing.go) · [Rust](tasks/implementations/rust/tasks/image_resizing.rs)

#### `linear_regression` — Implementing a basic machine learning algorithm (linear regression)

- **How it works:** Each implementation reads the same synthetic regression dataset, computes the least-squares slope and intercept for a single-feature linear model, and prints a rounded checksum of the fitted parameters.
- **What it tests:** This exercises numeric iteration over a realistic machine-learning style dataset, repeated floating-point accumulation, and the cost of basic statistical computation without specialized ML libraries.
- **Why this task matters:** Numeric/data-processing throughput with light ML-style computation.
- **Tags:** `compute`, `ml`, `numeric`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/linear_regression.php) · [Python](tasks/implementations/python/tasks/linear_regression.py) · [Java](tasks/implementations/java/tasks/linear_regression.java) · [C++](tasks/implementations/cpp/tasks/linear_regression.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/linear_regression.js) · [Go](tasks/implementations/go/tasks/linear_regression.go) · [Rust](tasks/implementations/rust/tasks/linear_regression.rs)

#### `matrix_multiplication` — Performing matrix multiplication

- **How it works:** Each implementation reads two dense square matrices from the fixture, performs naive O(n^3) multiplication with a triple nested loop, and prints the sum of all output cells so the work cannot be optimized away.
- **What it tests:** This emphasizes arithmetic throughput, tight-loop overhead, array indexing costs, cache locality, and how well the runtime handles hot numeric code without relying on specialized libraries.
- **Why this task matters:** Numeric hot loops and memory locality.
- **Tags:** `compute`, `numeric`, `cpu`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/matrix_multiplication.php) · [Python](tasks/implementations/python/tasks/matrix_multiplication.py) · [Java](tasks/implementations/java/tasks/matrix_multiplication.java) · [C++](tasks/implementations/cpp/tasks/matrix_multiplication.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/matrix_multiplication.js) · [Go](tasks/implementations/go/tasks/matrix_multiplication.go) · [Rust](tasks/implementations/rust/tasks/matrix_multiplication.rs)

#### `prime_sieve` — Implementing a simple algorithm (prime number generation)

- **How it works:** Each implementation runs a Sieve of Eratosthenes up to a fixed limit for size S, M, or L, then counts and prints the number of primes found.
- **What it tests:** This isolates tight loops, repeated memory writes, boolean-array behavior, and branch-heavy compute in a benchmark that is simple to verify and highly repeatable across runtimes.
- **Why this task matters:** Algorithmic CPU throughput on tight loops.
- **Tags:** `compute`, `algorithm`, `cpu`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/prime_sieve.php) · [Python](tasks/implementations/python/tasks/prime_sieve.py) · [Java](tasks/implementations/java/tasks/prime_sieve.java) · [C++](tasks/implementations/cpp/tasks/prime_sieve.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/prime_sieve.js) · [Go](tasks/implementations/go/tasks/prime_sieve.go) · [Rust](tasks/implementations/rust/tasks/prime_sieve.rs)

#### `producer_consumer` — Implementing a simple multithreading task (producer-consumer problem)

- **How it works:** Each implementation reads the same sequence of produced values, feeds them through a bounded circular buffer that simulates producer and consumer coordination, and prints a checksum over the consumed stream.
- **What it tests:** This benchmarks queue bookkeeping, bounded-buffer logic, stateful iteration, and the implementation overhead of a classic producer-consumer style workload in each language.
- **Why this task matters:** Concurrency-style bookkeeping and queue simulation.
- **Tags:** `compute`, `concurrency`, `queue`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/producer_consumer.php) · [Python](tasks/implementations/python/tasks/producer_consumer.py) · [Java](tasks/implementations/java/tasks/producer_consumer.java) · [C++](tasks/implementations/cpp/tasks/producer_consumer.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/producer_consumer.js) · [Go](tasks/implementations/go/tasks/producer_consumer.go) · [Rust](tasks/implementations/rust/tasks/producer_consumer.rs)

#### `rest_api` — Implementing a simple REST API

- **How it works:** Each implementation starts a deterministic local HTTP API with `/item?id=...` returning a small JSON payload, and the benchmark driver issues repeated GET requests while validating the aggregated numeric response values.
- **What it tests:** This benchmarks lightweight routing, query parsing, JSON serialization, per-request object construction, and service-style runtime overhead beyond pure compute loops.
- **Why this task matters:** Cold-start, request routing, and small JSON API overhead.
- **Tags:** `service`, `web`, `api`, `startup-sensitive`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/rest_api.php) · [Python](tasks/implementations/python/tasks/rest_api.py) · [Java](tasks/implementations/java/tasks/rest_api.java) · [C++](tasks/implementations/cpp/tasks/rest_api.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/rest_api.js) · [Go](tasks/implementations/go/tasks/rest_api.go) · [Rust](tasks/implementations/rust/tasks/rest_api.rs)

#### `sentiment_analysis` — Implementing a simple natural language processing task (sentiment analysis)

- **How it works:** Each implementation scans the same deterministic corpus of text lines, applies a tiny lexicon-based sentiment model with positive and negative word lists, and prints the aggregate sentiment score.
- **What it tests:** This benchmarks tokenization, repeated dictionary/set lookups, string processing, and a minimal natural-language processing workload that stays fully reproducible offline.
- **Why this task matters:** String/token processing and repeated dictionary lookups.
- **Tags:** `compute`, `nlp`, `text`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/sentiment_analysis.php) · [Python](tasks/implementations/python/tasks/sentiment_analysis.py) · [Java](tasks/implementations/java/tasks/sentiment_analysis.java) · [C++](tasks/implementations/cpp/tasks/sentiment_analysis.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/sentiment_analysis.js) · [Go](tasks/implementations/go/tasks/sentiment_analysis.go) · [Rust](tasks/implementations/rust/tasks/sentiment_analysis.rs)

#### `simple_web_server` — Implementing a simple web server

- **How it works:** Each implementation starts a minimal local HTTP server, exposes a `/health` route plus a root route returning a fixed response body, and the neutral runner measures repeated local GET requests against that service.
- **What it tests:** This measures HTTP server startup, request parsing, response generation, socket handling, and the baseline cost of serving a tiny deterministic web workload in each language.
- **Why this task matters:** Cold-start plus tiny steady-state HTTP service behavior.
- **Tags:** `service`, `web`, `networking`, `startup-sensitive`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/simple_web_server.php) · [Python](tasks/implementations/python/tasks/simple_web_server.py) · [Java](tasks/implementations/java/tasks/simple_web_server.java) · [C++](tasks/implementations/cpp/tasks/simple_web_server.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/simple_web_server.js) · [Go](tasks/implementations/go/tasks/simple_web_server.go) · [Rust](tasks/implementations/rust/tasks/simple_web_server.rs)

#### `socket_programming` — Implementing a basic networking task (socket programming)

- **How it works:** Each implementation starts a minimal TCP echo server and the neutral driver performs repeated loopback connect-send-receive cycles with deterministic payloads of increasing count by input size.
- **What it tests:** This isolates low-level networking overhead, socket read/write behavior, connection lifecycle cost, and the ergonomics of implementing a bare-bones network service in each language.
- **Why this task matters:** Low-level networking and echo-style hot path.
- **Tags:** `service`, `networking`, `tcp`, `startup-sensitive`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/socket_programming.php) · [Python](tasks/implementations/python/tasks/socket_programming.py) · [Java](tasks/implementations/java/tasks/socket_programming.java) · [C++](tasks/implementations/cpp/tasks/socket_programming.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/socket_programming.js) · [Go](tasks/implementations/go/tasks/socket_programming.go) · [Rust](tasks/implementations/rust/tasks/socket_programming.rs)

#### `sort_integers` — Sorting a large array of integers

- **How it works:** Each implementation reads a deterministic fixture of integers, parses them into an in-memory array/vector/list, sorts ascending, and prints the sum of the first 100 values as a correctness checksum.
- **What it tests:** This stresses file parsing, allocation behavior, the language's standard-library sort implementation, and raw single-process CPU throughput on a simple but realistic data-processing workload.
- **Why this task matters:** Mostly raw CPU throughput and standard-library algorithm efficiency.
- **Tags:** `compute`, `algorithm`, `cpu`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/sort_integers.php) · [Python](tasks/implementations/python/tasks/sort_integers.py) · [Java](tasks/implementations/java/tasks/sort_integers.java) · [C++](tasks/implementations/cpp/tasks/sort_integers.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/sort_integers.js) · [Go](tasks/implementations/go/tasks/sort_integers.go) · [Rust](tasks/implementations/rust/tasks/sort_integers.rs)

#### `sqlite_crud` — Implementing a basic database interaction (CRUD operations)

- **How it works:** Each implementation starts a local HTTP service backed by SQLite, exposes deterministic create/read/update/delete endpoints, and the benchmark driver executes the full CRUD cycle repeatedly with fixed IDs and values.
- **What it tests:** This measures service routing plus subprocess or database interaction overhead, request parsing, JSON encoding, and the end-to-end cost of a tiny stateful CRUD API.
- **Why this task matters:** Cold-start plus service/database CRUD overhead.
- **Tags:** `service`, `database`, `api`, `startup-sensitive`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/sqlite_crud.php) · [Python](tasks/implementations/python/tasks/sqlite_crud.py) · [Java](tasks/implementations/java/tasks/sqlite_crud.java) · [C++](tasks/implementations/cpp/tasks/sqlite_crud.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/sqlite_crud.js) · [Go](tasks/implementations/go/tasks/sqlite_crud.go) · [Rust](tasks/implementations/rust/tasks/sqlite_crud.rs)

#### `third_party_api` — Integrating with a third-party API (e.g., Twitter API)

- **How it works:** Each implementation reads a deterministic Twitter-like mock response from fixtures, extracts post IDs, text bodies, and like counts, and aggregates them into a checksum.
- **What it tests:** This stresses semi-structured payload parsing, string-heavy extraction, and the glue code needed to consume a typical social-media style third-party API response.
- **Why this task matters:** Third-party style JSON/integration handling.
- **Tags:** `integration`, `api`, `json`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/third_party_api.php) · [Python](tasks/implementations/python/tasks/third_party_api.py) · [Java](tasks/implementations/java/tasks/third_party_api.java) · [C++](tasks/implementations/cpp/tasks/third_party_api.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/third_party_api.js) · [Go](tasks/implementations/go/tasks/third_party_api.go) · [Rust](tasks/implementations/rust/tasks/third_party_api.rs)

#### `tic_tac_toe` — Implementing a basic game (tic-tac-toe)

- **How it works:** Each implementation replays a deterministic set of tic-tac-toe move sequences, applies the rules of the game, detects wins or draws, and accumulates a checksum from the final board state and game outcome.
- **What it tests:** This stresses branch-heavy control flow, small-state mutation, repeated rule checking, and the ergonomics of implementing a tiny game engine in each language.
- **Why this task matters:** Branch-heavy control flow rather than raw numeric throughput.
- **Tags:** `compute`, `control-flow`, `game`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/tic_tac_toe.php) · [Python](tasks/implementations/python/tasks/tic_tac_toe.py) · [Java](tasks/implementations/java/tasks/tic_tac_toe.java) · [C++](tasks/implementations/cpp/tasks/tic_tac_toe.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/tic_tac_toe.js) · [Go](tasks/implementations/go/tasks/tic_tac_toe.go) · [Rust](tasks/implementations/rust/tasks/tic_tac_toe.rs)

#### `web_scraper` — Implementing a simple web scraper

- **How it works:** Each implementation opens a deterministic local fixture site, extracts linked page paths from the index HTML, loads each linked page, and computes a checksum from the scraped titles and paragraph text.
- **What it tests:** This measures file/HTML parsing, lightweight extraction logic, repeated document loading, and the overhead of a tiny offline scraping workflow without depending on live websites.
- **Why this task matters:** HTML parsing and offline integration glue.
- **Tags:** `integration`, `html`, `io`
- **Input sizes:** `s, m, l`
- **Implementations:** [PHP](tasks/implementations/php/tasks/web_scraper.php) · [Python](tasks/implementations/python/tasks/web_scraper.py) · [Java](tasks/implementations/java/tasks/web_scraper.java) · [C++](tasks/implementations/cpp/tasks/web_scraper.cpp) · [JavaScript (Node.js)](tasks/implementations/node/tasks/web_scraper.js) · [Go](tasks/implementations/go/tasks/web_scraper.go) · [Rust](tasks/implementations/rust/tasks/web_scraper.rs)


### What this benchmark is not

- It is **not** a universal truth about a language; it is a comparison across this repository's fixed workload mix.
- It is **not** using every ecosystem's most highly optimized specialist library for every task.
- It is **not** a substitute for benchmarking your own production workload on your own hardware.

> Generated from the latest scored benchmark run via `./bench report --results ... --update-readme`.
<!-- benchmark:end -->
