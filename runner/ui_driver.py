from __future__ import annotations

import sys
from playwright.sync_api import sync_playwright

COUNTS = {
    "gui_calculator": {"s": 80, "m": 320, "l": 800},
    "data_visualization": {"s": 40, "m": 160, "l": 400},
    "basic_web_application": {"s": 60, "m": 240, "l": 600},
}


def main() -> int:
    task_id, size, url = sys.argv[1], sys.argv[2], sys.argv[3]
    count = COUNTS[task_id][size]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(url, wait_until="load")
        if task_id == "gui_calculator":
            value = page.evaluate("(count) => window.benchCalculator(count)", count)
        elif task_id == "data_visualization":
            values = [((i * 13) % 180) + 20 for i in range(count)]
            value = page.evaluate("(values) => window.renderChart(values)", values)
        elif task_id == "basic_web_application":
            value = page.evaluate("(count) => window.benchTodo(count)", count)
        else:
            raise SystemExit(f"unsupported ui task: {task_id}")
        print(value)
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
