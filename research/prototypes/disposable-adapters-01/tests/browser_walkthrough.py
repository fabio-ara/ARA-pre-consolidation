import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "standalone.html").read_text(encoding="utf-8")
report = {"environment": {}, "checks": [], "focus_sequence": [], "requests": []}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.on("request", lambda request: report["requests"].append(request.url))
    init_started = time.perf_counter()
    page.set_content(html, wait_until="load")
    page.wait_for_function("window.__araAdapters !== undefined")
    init_ms = (time.perf_counter() - init_started) * 1000
    report["environment"] = {
        "user_agent": page.evaluate("navigator.userAgent"),
        "viewport": page.viewport_size,
        "external_requests": [u for u in report["requests"] if not u.startswith("blob:")],
        "standalone_bytes": len(html.encode("utf-8")),
        "initialization_ms": init_ms,
    }

    page.fill("#math-input", "2*(x+")
    page.click("#math-validate")
    invalid = page.locator("#math-status").inner_text()
    report["checks"].append({"id": "math-invalid", "passed": "inválida" in invalid.lower(), "observed": invalid})
    page.fill("#math-input", "2*x+6")
    page.click("#math-validate")
    partial = page.locator("#math-status").inner_text()
    report["checks"].append({"id": "math-partial", "passed": "parcialmente" in partial.lower(), "observed": partial})
    page.fill("#math-input", "2*(x+3)")
    page.click("#math-validate")
    correct = page.locator("#math-status").inner_text()
    preview = page.locator("#math-preview").inner_text()
    report["checks"].append({"id": "math-correct", "passed": "correta" in correct.lower() and "x + 3" in preview, "observed": {"status": correct, "preview": preview}})

    page.select_option("#edge-from", "A")
    page.select_option("#edge-to", "B")
    page.click("#edge-add")
    page.select_option("#edge-from", "B")
    page.select_option("#edge-to", "D")
    page.click("#edge-add")
    page.click("#graph-validate")
    graph_status = page.locator("#graph-status").inner_text()
    graph_json = json.loads(page.locator("#graph-json").text_content())
    serialized = json.dumps(graph_json)
    report["checks"].append({"id": "graph-correct", "passed": "correta" in graph_status.lower(), "observed": graph_status})
    report["checks"].append({"id": "graph-no-geometry", "passed": all(token not in serialized for token in ['"x"', '"y"', "rendererState", "layout"]), "observed": serialized})
    report["checks"].append({"id": "graph-linear-view", "passed": page.locator("#edge-list li").count() == 2, "observed": page.locator("#edge-list").inner_text()})

    page.fill("#code-input", "function sumEven(values) { return 0; }")
    page.click("#code-run")
    page.wait_for_function("document.querySelector('#code-status').textContent.includes('falhas')")
    failed = page.locator("#code-status").inner_text()
    report["checks"].append({"id": "program-public-fail", "passed": "falhas" in failed.lower(), "observed": failed})
    page.fill("#code-input", "function sumEven(values) { return values.filter(v => v % 2 === 0).reduce((a,b) => a+b, 0); }")
    page.click("#code-run")
    page.wait_for_function("document.querySelector('#code-status').textContent.includes('corretos')")
    passed = page.locator("#code-status").inner_text()
    program_json = page.locator("#code-json").text_content()
    report["checks"].append({"id": "program-public-pass", "passed": "protegida permanece fora" in passed.lower(), "observed": passed})
    report["checks"].append({"id": "program-no-protected-export", "passed": "negative" not in program_json and "protected" not in program_json, "observed": program_json})
    page.fill("#code-input", "while (true) {}\nfunction sumEven(values) { return 0; }")
    page.click("#code-run")
    page.wait_for_function("document.querySelector('#code-status').textContent.includes('limite de tempo')", timeout=3000)
    timed = page.locator("#code-status").inner_text()
    report["checks"].append({"id": "program-timeout", "passed": "limite de tempo" in timed.lower(), "observed": timed})

    source_text = page.locator("#source-text").input_value()
    quote = "Muitos estudantes trabalham durante o dia"
    start = source_text.index(quote)
    page.locator("#source-text").evaluate("(el, range) => { el.focus(); el.setSelectionRange(range.start, range.end); }", {"start": start, "end": start + len(quote)})
    page.click("#capture-selection")
    page.click("#source-validate")
    page.wait_for_function("document.querySelector('#source-status').textContent.includes('revisão humana')")
    source_status = page.locator("#source-status").inner_text()
    report["checks"].append({"id": "source-review-handoff", "passed": "revisão humana" in source_status.lower(), "observed": source_status})
    rereso = page.evaluate("""async () => {
      const a = window.__araAdapters.source;
      a.response.annotations[0].selector.start = 0;
      a.response.annotations[0].selector.end = a.response.annotations[0].selector.quote.length;
      return await a.validate();
    }""")
    method = rereso["evidence"]["selectors"][0]["resolution"].get("method")
    report["checks"].append({"id": "source-selector-reresolution", "passed": rereso["finalState"] == "review-required" and method == "quote-context", "observed": {"state": rereso["finalState"], "method": method}})

    page.focus("body")
    for _ in range(24):
        page.keyboard.press("Tab")
        report["focus_sequence"].append(page.evaluate("document.activeElement.id || document.activeElement.className || document.activeElement.tagName"))
    expected_focus = {"math-input", "math-validate", "edge-from", "edge-to", "edge-add", "edge-remove", "graph-validate"}
    report["checks"].append({"id": "keyboard-focus-order", "passed": expected_focus.issubset(set(report["focus_sequence"])), "observed": report["focus_sequence"]})
    live_regions = page.locator("[aria-live]").count()
    report["checks"].append({"id": "status-announcements", "passed": live_regions >= 4, "observed": live_regions})

    page.set_viewport_size({"width": 320, "height": 900})
    page.wait_for_timeout(100)
    overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    report["checks"].append({"id": "reflow-320", "passed": overflow <= 1, "observed": overflow})
    cdp = page.context.new_cdp_session(page)
    cdp.send("Performance.enable")
    metrics = cdp.send("Performance.getMetrics")["metrics"]
    report["environment"]["performance_metrics"] = {item["name"]: item["value"] for item in metrics if item["name"] in {"JSHeapUsedSize", "JSHeapTotalSize", "Nodes", "Documents", "Frames"}}
    browser.close()

report["summary"] = {
    "total": len(report["checks"]),
    "passed": sum(1 for check in report["checks"] if check["passed"]),
    "failed": [check["id"] for check in report["checks"] if not check["passed"]],
}
(ROOT / "reports" / "browser-walkthrough.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report["summary"], ensure_ascii=False))
if report["summary"]["failed"]:
    raise SystemExit(1)
