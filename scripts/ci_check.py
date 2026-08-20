#!/usr/bin/env python3
"""Dependency-free CI checks for the RSGE Recognition Planner."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


class PlannerHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: set[str] = set()
        self.ids: set[str] = set()
        self.title_text: list[str] = []
        self.h1_text: list[str] = []
        self._in_title = False
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs):
        self.tags.add(tag)
        attrs_dict = dict(attrs)
        if attrs_dict.get("id"):
            self.ids.add(attrs_dict["id"])
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag: str):
        if tag == "title":
            self._in_title = False
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data: str):
        if self._in_title:
            self.title_text.append(data)
        if self._in_h1:
            self.h1_text.append(data)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def check_required_files() -> None:
    required = [
        "index.html",
        ".github/ISSUE_TEMPLATE/inaccuracy.yml",
        ".github/workflows/report-to-jira.yml",
        ".github/workflows/research-agent.yml",
        ".github/workflows/deploy-close-jira.yml",
        "docs/CONTENT_GOVERNANCE.md",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    require(not missing, f"Missing required file(s): {', '.join(missing)}")


def check_text_hygiene() -> None:
    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    markers = ("<<<<<<<", ">>>>>>>")
    for path in files:
        if path.suffix.lower() not in {".html", ".md", ".py", ".yml", ".yaml", ".js", ".css"}:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            require(marker not in text, f"Merge-conflict marker {marker!r} found in {path.relative_to(ROOT)}")
        if path.suffix.lower() in {".yml", ".yaml"}:
            require("\t" not in text, f"Tab character found in YAML file {path.relative_to(ROOT)}")


def check_html() -> str:
    text = INDEX.read_text(encoding="utf-8")
    require(text.lstrip().lower().startswith("<!doctype html>"), "index.html must start with an HTML doctype")
    require('name="viewport"' in text, "index.html must include a viewport meta tag")
    require("issues/new?template=inaccuracy.yml" in text, "Accuracy report link must use the controlled inaccuracy issue template")
    require("Planning only" in text, "Calculator planning disclaimer is missing")
    require("official BC or legal deadlines override" in text, "Deadline disclaimer is missing")

    parser = PlannerHTMLParser()
    parser.feed(text)
    for tag in ("html", "head", "body", "main", "title", "h1", "script"):
        require(tag in parser.tags, f"Required <{tag}> element is missing")

    require("RSGE Recognition Planner" in "".join(parser.title_text), "Unexpected or missing page title")

    required_ids = {
        "plus", "minus", "reset", "target", "daysleft", "nextmile", "gcal", "ics",
        "priv", "sub", "kids", "days", "rate", "rent", "ops", "income", "gross",
        "net", "delta", "now", "next", "later", "n1", "n2", "n3",
    }
    missing_ids = sorted(required_ids - parser.ids)
    require(not missing_ids, f"DOM id(s) required by planner JavaScript are missing: {', '.join(missing_ids)}")
    return text


def check_inline_javascript(html: str) -> None:
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, flags=re.IGNORECASE | re.DOTALL)
    require(scripts, "No inline JavaScript found in index.html")
    js = "\n".join(scripts)
    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tmp:
        tmp.write(js)
        path = tmp.name
    result = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    if result.returncode != 0:
        fail("JavaScript syntax check failed:\n" + (result.stderr or result.stdout))


def check_workflow_contracts() -> None:
    report = (ROOT / ".github/workflows/report-to-jira.yml").read_text(encoding="utf-8")
    research = (ROOT / ".github/workflows/research-agent.yml").read_text(encoding="utf-8")
    deploy = (ROOT / ".github/workflows/deploy-close-jira.yml").read_text(encoding="utf-8")

    require("accuracy-report" in report, "Jira intake workflow no longer recognizes accuracy reports")
    require("JIRA_API_TOKEN" in report, "Jira intake workflow is missing token configuration")
    require("--draft" in research, "Research workflow must create draft PRs for HITL review")
    require("Not approved" in research, "Research evidence scaffold must default to not approved")
    require("JIRA_DONE_TRANSITION_ID" in deploy, "Deployment trace workflow contract changed unexpectedly")


def main() -> int:
    check_required_files()
    check_text_hygiene()
    html = check_html()
    check_inline_javascript(html)
    check_workflow_contracts()
    print("CI checks passed: required files, HTML contracts, JavaScript syntax, and governance workflow guards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
