#!/usr/bin/env python3
"""Assemble the publishable site into ./site.

Copies site content (index, lessons, labs, assets, notebooks, decks, output,
tour, and key markdown/docs) so the built directory can be served locally or
published to GitHub Pages. Existing `site/.git` is preserved.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

DIRS = ["lessons", "assets", "notebooks", "decks", "output", "labs"]
FILES = ["index.html", "tour.html", "CURRICULUM.md", "README.md", ".nojekyll", "robots.txt"]

if SITE.exists():
    for child in SITE.iterdir():
        if child.name == ".git":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()
else:
    SITE.mkdir()

for d in DIRS:
    src = ROOT / d
    if src.exists():
        shutil.copytree(src, SITE / d)

for f in FILES:
    src = ROOT / f
    if src.exists():
        shutil.copy2(src, SITE / f)

(SITE / ".nojekyll").write_text("", encoding="utf-8")
if not (SITE / "robots.txt").exists():
    (SITE / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
(SITE / "README.md").write_text(
    "# Distributed and Parallel Architectures\n\n"
    "Static course website (fundamentals + 13 lectures) with diagrams, animations, and research activities.\n\n"
    "Open `index.html` locally or publish this directory to GitHub Pages.\n\n"
    "Generated from the source workspace — do not edit generated files here by hand.\n",
    encoding="utf-8",
)

total = sum(1 for _ in SITE.rglob("*") if _.is_file())
size_mb = sum(f.stat().st_size for f in SITE.rglob("*") if f.is_file()) / 1e6
print(f"site assembled: {total} files, {size_mb:.2f} MB")
