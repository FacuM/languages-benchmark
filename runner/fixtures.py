from __future__ import annotations

from pathlib import Path
import random
import shutil

from runner.utils import ensure_dir

SIZE_ROWS = {
    "s": 10_000,
    "m": 50_000,
    "l": 100_000,
}

MATRIX_N = {
    "s": 32,
    "m": 64,
    "l": 96,
}

PRIME_LIMIT = {
    "s": 50_000,
    "m": 125_000,
    "l": 250_000,
}

BST_INSERTS = {
    "s": (5_000, 2_000),
    "m": (20_000, 8_000),
    "l": (50_000, 20_000),
}

SEARCH_TREE_FILES = {
    "s": (3, 6, 24),
    "m": (5, 8, 40),
    "l": (7, 10, 60),
}

TIC_TAC_TOE_GAMES = {
    "s": 1_000,
    "m": 5_000,
    "l": 10_000,
}

BLOCKCHAIN_BLOCKS = {
    "s": 1_000,
    "m": 5_000,
    "l": 10_000,
}

IMAGE_DIMS = {
    "s": (64, 64),
    "m": (128, 128),
    "l": (192, 192),
}

SENTIMENT_LINES = {
    "s": 5_000,
    "m": 20_000,
    "l": 50_000,
}

DECISION_TREE_ROWS = {
    "s": 2_000,
    "m": 10_000,
    "l": 20_000,
}

PRODUCER_CONSUMER_ROWS = {
    "s": 10_000,
    "m": 50_000,
    "l": 100_000,
}

SCRAPER_PAGES = {
    "s": 8,
    "m": 24,
    "l": 60,
}

INTEGRATION_ITEMS = {
    "s": 120,
    "m": 500,
    "l": 1000,
}

AI_RESPONSES = {
    "s": 80,
    "m": 300,
    "l": 700,
}

HTTP_COUNTS = {"s": 60, "m": 240, "l": 600}
TCP_COUNTS = {"s": 40, "m": 160, "l": 400}
SQLITE_COUNTS = {"s": 20, "m": 80, "l": 200}
UI_COUNTS = {"s": 120, "m": 480, "l": 1200}


def prepare_fixtures(root: Path) -> None:
    generated = ensure_dir(root / "fixtures" / "generated")
    _write_sort(generated / "sort")
    _write_matrix(generated / "matrix")
    _write_csv(generated / "csv")
    _write_file_io(generated / "file_io")
    _write_bst(generated / "bst")
    _write_linear_regression(generated / "linear_regression")
    _write_cli_search(generated / "search")
    _write_tic_tac_toe(generated / "tic_tac_toe")
    _write_blockchain(generated / "blockchain")
    _write_image_resizing(generated / "image")
    _write_sentiment(generated / "sentiment")
    _write_decision_tree(generated / "decision_tree")
    _write_producer_consumer(generated / "producer_consumer")
    _write_mocks(root / "fixtures" / "mocks")
    _write_mock_site(root / "fixtures" / "mock_site")
    _write_ui_pages(root / "fixtures" / "ui")


def fixture_manifest(root: Path) -> dict[str, dict[str, str]]:
    fixtures = root / "fixtures"
    return {
        "sort_integers": {size: f"{SIZE_ROWS[size]:,} integers from generated/sort/{size}.txt" for size in SIZE_ROWS},
        "matrix_multiplication": {size: f"2 dense {MATRIX_N[size]}×{MATRIX_N[size]} matrices from generated/matrix/{size}.txt" for size in MATRIX_N},
        "csv_parsing": {size: f"{SIZE_ROWS[size]:,} CSV data rows from generated/csv/{size}.csv" for size in SIZE_ROWS},
        "prime_sieve": {size: f"sieve limit {PRIME_LIMIT[size]:,}" for size in PRIME_LIMIT},
        "file_io_large": {size: f"{SIZE_ROWS[size]:,} newline-delimited integers from generated/file_io/{size}.txt" for size in SIZE_ROWS},
        "binary_search_tree": {size: f"{BST_INSERTS[size][0]:,} inserts + {BST_INSERTS[size][1]:,} queries from generated/bst/{size}.txt" for size in BST_INSERTS},
        "linear_regression": {size: f"{SIZE_ROWS[size]:,} training rows from generated/linear_regression/{size}.csv" for size in SIZE_ROWS},
        "cli_file_search": {size: f"{SEARCH_TREE_FILES[size][0]} dirs × {SEARCH_TREE_FILES[size][1]} files/dir × {SEARCH_TREE_FILES[size][2]} lines/file under generated/search/{size}" for size in SEARCH_TREE_FILES},
        "tic_tac_toe": {size: f"{TIC_TAC_TOE_GAMES[size]:,} deterministic games from generated/tic_tac_toe/{size}.txt" for size in TIC_TAC_TOE_GAMES},
        "basic_blockchain": {size: f"{BLOCKCHAIN_BLOCKS[size]:,} blocks × 6 synthetic transactions/block from generated/blockchain/{size}.txt" for size in BLOCKCHAIN_BLOCKS},
        "image_resizing": {size: f"{IMAGE_DIMS[size][0]}×{IMAGE_DIMS[size][1]} PPM image from generated/image/{size}.ppm" for size in IMAGE_DIMS},
        "sentiment_analysis": {size: f"{SENTIMENT_LINES[size]:,} text lines from generated/sentiment/{size}.txt" for size in SENTIMENT_LINES},
        "decision_tree": {size: f"{DECISION_TREE_ROWS[size]:,} labeled rows from generated/decision_tree/{size}.csv" for size in DECISION_TREE_ROWS},
        "producer_consumer": {size: f"{PRODUCER_CONSUMER_ROWS[size]:,} queued values from generated/producer_consumer/{size}.txt" for size in PRODUCER_CONSUMER_ROWS},
        "web_scraper": {size: f"{SCRAPER_PAGES[size]:,} local HTML pages (+ index) under mock_site/{size}" for size in SCRAPER_PAGES},
        "api_client": {size: f"{INTEGRATION_ITEMS[size]:,} mock API items from mocks/public_api_{size}.json" for size in INTEGRATION_ITEMS},
        "third_party_api": {size: f"{INTEGRATION_ITEMS[size]:,} mock social posts from mocks/twitter_like_{size}.json" for size in INTEGRATION_ITEMS},
        "ai_service_integration": {size: f"{AI_RESPONSES[size]:,} mock AI responses from mocks/ai_service_{size}.json" for size in AI_RESPONSES},
        "simple_web_server": {size: f"{HTTP_COUNTS[size]:,} local GET / requests" for size in HTTP_COUNTS},
        "rest_api": {size: f"{HTTP_COUNTS[size]:,} local GET /item requests" for size in HTTP_COUNTS},
        "sqlite_crud": {size: f"{SQLITE_COUNTS[size]:,} CRUD cycles (create/read/update/read/delete)" for size in SQLITE_COUNTS},
        "chat_application": {size: f"{TCP_COUNTS[size]:,} TCP chat round-trips" for size in TCP_COUNTS},
        "socket_programming": {size: f"{TCP_COUNTS[size]:,} TCP echo round-trips" for size in TCP_COUNTS},
        "gui_calculator": {size: f"{UI_COUNTS[size]:,} browser-side calculator updates against fixtures/ui/gui_calculator.html" for size in UI_COUNTS},
        "data_visualization": {size: f"{UI_COUNTS[size]:,} browser-side chart bars rendered against fixtures/ui/data_visualization.html" for size in UI_COUNTS},
        "basic_web_application": {size: f"{UI_COUNTS[size]:,} browser-side to-do operations against fixtures/ui/basic_web_application.html" for size in UI_COUNTS},
    }


def _write_sort(path: Path) -> None:
    ensure_dir(path)
    base_seed = 424242
    for size, count in SIZE_ROWS.items():
        rng = random.Random(base_seed + count)
        values = [str(rng.randint(0, 1_000_000)) for _ in range(count)]
        (path / f"{size}.txt").write_text("\n".join(values) + "\n", encoding="utf-8")


def _write_matrix(path: Path) -> None:
    ensure_dir(path)
    for size, n in MATRIX_N.items():
        rng = random.Random(1000 + n)
        numbers = [str(rng.randint(0, 9)) for _ in range(2 * n * n)]
        content = [str(n)] + numbers
        (path / f"{size}.txt").write_text("\n".join(content) + "\n", encoding="utf-8")


def _write_csv(path: Path) -> None:
    ensure_dir(path)
    for size, count in SIZE_ROWS.items():
        rows = ["id,value_a,value_b,label"]
        rng = random.Random(555 + count)
        for idx in range(count):
            rows.append(f"{idx},{rng.randint(1,999)},{rng.randint(1,999)},item-{idx}")
        (path / f"{size}.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")


def _write_file_io(path: Path) -> None:
    ensure_dir(path)
    for size, count in SIZE_ROWS.items():
        rng = random.Random(9090 + count)
        values = [str(rng.randint(1, 9_999_999)) for _ in range(count)]
        (path / f"{size}.txt").write_text("\n".join(values) + "\n", encoding="utf-8")


def _write_bst(path: Path) -> None:
    ensure_dir(path)
    for size, (insert_count, query_count) in BST_INSERTS.items():
        rng = random.Random(1212 + insert_count + query_count)
        inserts = rng.sample(range(1, insert_count * 20), insert_count)
        hits = inserts[: query_count // 2]
        misses = [insert_count * 30 + i * 17 for i in range(query_count - len(hits))]
        queries = hits + misses
        rng.shuffle(queries)
        payload = [str(insert_count), *(str(v) for v in inserts), str(query_count), *(str(v) for v in queries)]
        (path / f"{size}.txt").write_text("\n".join(payload) + "\n", encoding="utf-8")


def _write_linear_regression(path: Path) -> None:
    ensure_dir(path)
    for size, count in SIZE_ROWS.items():
        rows = ["x,y"]
        for x in range(count):
            noise = ((x % 13) - 6) * 3
            y = 7 + 3 * x + noise
            rows.append(f"{x},{y}")
        (path / f"{size}.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")


def _write_cli_search(path: Path) -> None:
    keyword = "needle"
    for size, (dir_count, files_per_dir, lines_per_file) in SEARCH_TREE_FILES.items():
        size_dir = path / size
        if size_dir.exists():
            shutil.rmtree(size_dir)
        ensure_dir(size_dir)
        for dir_index in range(dir_count):
            dir_path = ensure_dir(size_dir / f"group_{dir_index}")
            nested = ensure_dir(dir_path / "nested")
            for file_index in range(files_per_dir):
                target_dir = dir_path if file_index % 2 == 0 else nested
                lines = []
                for line_index in range(lines_per_file):
                    if (line_index + file_index + dir_index) % 7 == 0:
                        lines.append(f"line {line_index} contains {keyword} token")
                    else:
                        lines.append(f"line {line_index} contains filler text {dir_index}-{file_index}")
                (target_dir / f"file_{file_index}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_mocks(path: Path) -> None:
    ensure_dir(path)
    (path / "public_api.json").write_text('{"items": [{"id": 1, "name": "alpha"}, {"id": 2, "name": "beta"}]}\n', encoding="utf-8")
    (path / "twitter_like.json").write_text('{"posts": [{"id": "t1", "text": "hello"}, {"id": "t2", "text": "world"}]}\n', encoding="utf-8")
    (path / "ai_service.json").write_text('{"model": "mock-1", "output": "This is a deterministic mock response."}\n', encoding="utf-8")

    for size, count in INTEGRATION_ITEMS.items():
        api_lines = ['{"items": [']
        third_party_lines = ['{"posts": [']
        rng = random.Random(2020 + count)
        for idx in range(count):
            value = (idx * 7) % 997
            api_lines.append(f'  {{"id": {idx + 1}, "name": "item-{size}-{idx}", "value": {value}}}' + (',' if idx + 1 < count else ''))
            likes = rng.randint(10, 999)
            third_party_lines.append(f'  {{"id": "t{idx + 1}", "text": "post {size} {idx} benchmark payload", "likes": {likes}}}' + (',' if idx + 1 < count else ''))
        api_lines.append(']}')
        third_party_lines.append(']}')
        (path / f"public_api_{size}.json").write_text("\n".join(api_lines) + "\n", encoding="utf-8")
        (path / f"twitter_like_{size}.json").write_text("\n".join(third_party_lines) + "\n", encoding="utf-8")

    for size, count in AI_RESPONSES.items():
        lines = ['{"model": "mock-1", "responses": [']
        for idx in range(count):
            tokens = 20 + (idx % 17)
            lines.append(f'  {{"prompt": "prompt {size} {idx}", "output": "deterministic response {size} {idx}", "tokens": {tokens}}}' + (',' if idx + 1 < count else ''))
        lines.append(']}')
        (path / f"ai_service_{size}.json").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_mock_site(path: Path) -> None:
    ensure_dir(path)
    (path / "index.html").write_text(
        "<html><body><h1>Fixture Site</h1><a href='about.html'>About</a><p>Static benchmark fixture.</p></body></html>\n",
        encoding="utf-8",
    )
    (path / "about.html").write_text(
        "<html><body><h2>About</h2><p>Deterministic local fixture page.</p></body></html>\n",
        encoding="utf-8",
    )
    for size, count in SCRAPER_PAGES.items():
        size_dir = path / size
        if size_dir.exists():
            shutil.rmtree(size_dir)
        ensure_dir(size_dir)
        index_lines = ["<html><body>", f"<h1>Fixture {size}</h1>"]
        for idx in range(count):
            name = f"page_{idx}.html"
            index_lines.append(f'<a href="{name}">Page {idx}</a>')
            (size_dir / name).write_text(
                "\n".join([
                    "<html><body>",
                    f"<h2>Title {size} {idx}</h2>",
                    f"<p>Paragraph {size} {idx} deterministic benchmark content.</p>",
                    "</body></html>",
                ]) + "\n",
                encoding="utf-8",
            )
        index_lines.append("</body></html>")
        (size_dir / "index.html").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


def _write_tic_tac_toe(path: Path) -> None:
    ensure_dir(path)
    for size, game_count in TIC_TAC_TOE_GAMES.items():
        rng = random.Random(31337 + game_count)
        lines = []
        for _ in range(game_count):
            moves = list(range(9))
            rng.shuffle(moves)
            lines.append(" ".join(str(move) for move in moves))
        (path / f"{size}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_blockchain(path: Path) -> None:
    ensure_dir(path)
    for size, block_count in BLOCKCHAIN_BLOCKS.items():
        rng = random.Random(8080 + block_count)
        lines = []
        for _ in range(block_count):
            txs = [str(rng.randint(1, 999_999)) for _ in range(6)]
            lines.append(" ".join(txs))
        (path / f"{size}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_image_resizing(path: Path) -> None:
    ensure_dir(path)
    for size, (width, height) in IMAGE_DIMS.items():
        rng = random.Random(5150 + width + height)
        parts = ["P3", str(width), str(height), "255"]
        for _ in range(width * height * 3):
            parts.append(str(rng.randint(0, 255)))
        (path / f"{size}.ppm").write_text("\n".join(parts) + "\n", encoding="utf-8")


def _write_sentiment(path: Path) -> None:
    ensure_dir(path)
    positives = ["good", "great", "happy", "clean", "fast", "love"]
    negatives = ["bad", "sad", "dirty", "slow", "hate", "poor"]
    neutrals = ["movie", "device", "system", "service", "product", "team", "story", "tool"]
    for size, line_count in SENTIMENT_LINES.items():
        rng = random.Random(9191 + line_count)
        lines = []
        for idx in range(line_count):
            pos_count = 1 + (idx % 3)
            neg_count = idx % 2
            words = [rng.choice(positives) for _ in range(pos_count)]
            words.extend(rng.choice(negatives) for _ in range(neg_count))
            while len(words) < 10:
                words.append(rng.choice(neutrals))
            rng.shuffle(words)
            lines.append(" ".join(words))
        (path / f"{size}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_decision_tree(path: Path) -> None:
    ensure_dir(path)
    for size, count in DECISION_TREE_ROWS.items():
        rng = random.Random(7070 + count)
        rows = ["f0,f1,f2,label"]
        for _ in range(count):
            f0 = rng.randint(0, 1000)
            f1 = rng.randint(0, 1000)
            f2 = rng.randint(0, 1000)
            label = 1 if (f0 > 520 and f1 < 460) or (f2 > 760) else 0
            rows.append(f"{f0},{f1},{f2},{label}")
        (path / f"{size}.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")


def _write_producer_consumer(path: Path) -> None:
    ensure_dir(path)
    for size, count in PRODUCER_CONSUMER_ROWS.items():
        rng = random.Random(6060 + count)
        values = [str(rng.randint(1, 10000)) for _ in range(count)]
        (path / f"{size}.txt").write_text("\n".join(values) + "\n", encoding="utf-8")


def _write_ui_pages(path: Path) -> None:
    ensure_dir(path)
    (path / "gui_calculator.html").write_text(
        """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Benchmark GUI Calculator</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 24px; background: #f6f8fa; color: #1f2328; }
    .card { max-width: 420px; padding: 16px; border: 1px solid #d0d7de; border-radius: 12px; background: white; }
    .display { font-size: 28px; font-weight: 700; margin-bottom: 12px; }
    .keys { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
    button { padding: 10px; border-radius: 8px; border: 1px solid #d0d7de; background: #f6f8fa; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Calculator</h1>
    <div id="display" class="display">0</div>
    <div class="keys">
      <button>7</button><button>8</button><button>9</button><button>+</button>
      <button>4</button><button>5</button><button>6</button><button>-</button>
      <button>1</button><button>2</button><button>3</button><button>*</button>
      <button>0</button><button>.</button><button>=</button><button>/</button>
    </div>
  </div>
  <script>
    window.benchCalculator = function(count) {
      let acc = 0;
      const display = document.getElementById("display");
      for (let i = 1; i <= count; i += 1) {
        acc = (((acc + i) * 3) - (i % 7)) % 1000003;
        display.textContent = String(acc);
      }
      return acc;
    };
  </script>
</body>
</html>
""",
        encoding="utf-8",
    )
    (path / "data_visualization.html").write_text(
        """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Benchmark Data Visualization</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 24px; background: #ffffff; color: #1f2328; }
    svg { border: 1px solid #d0d7de; border-radius: 12px; background: #f6f8fa; }
  </style>
</head>
<body>
  <h1>Visualization</h1>
  <svg id="chart" width="960" height="360" viewBox="0 0 960 360"></svg>
  <script>
    window.renderChart = function(values) {
      const svg = document.getElementById("chart");
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      const width = 960;
      const height = 360;
      const barWidth = Math.max(1, Math.floor(width / values.length));
      let checksum = 0;
      values.forEach((value, idx) => {
        const h = Math.max(1, Math.floor((value / 220) * (height - 20)));
        const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        rect.setAttribute("x", String(idx * barWidth));
        rect.setAttribute("y", String(height - h));
        rect.setAttribute("width", String(Math.max(1, barWidth - 1)));
        rect.setAttribute("height", String(h));
        rect.setAttribute("fill", idx % 2 === 0 ? "#0969da" : "#1a7f37");
        svg.appendChild(rect);
        checksum = (checksum + ((idx + 1) * h)) % 10000019;
      });
      return checksum;
    };
  </script>
</body>
</html>
""",
        encoding="utf-8",
    )
    (path / "basic_web_application.html").write_text(
        """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Benchmark To-Do App</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 24px; background: #f6f8fa; color: #1f2328; }
    .app { max-width: 560px; padding: 16px; border: 1px solid #d0d7de; border-radius: 12px; background: white; }
    li.done { text-decoration: line-through; color: #57606a; }
  </style>
</head>
<body>
  <div class="app">
    <h1>To-Do List</h1>
    <ul id="items"></ul>
  </div>
  <script>
    window.benchTodo = function(count) {
      const list = document.getElementById("items");
      list.textContent = "";
      let checksum = 0;
      for (let i = 0; i < count; i += 1) {
        const li = document.createElement("li");
        li.textContent = "task-" + i;
        if (i % 3 === 0) li.className = "done";
        list.appendChild(li);
        checksum = (checksum + ((i + 1) * li.textContent.length) + (li.className === "done" ? 7 : 3)) % 10000019;
      }
      return checksum;
    };
  </script>
</body>
</html>
""",
        encoding="utf-8",
    )
