#!/usr/bin/env python3
"""Report license changes and deprecations for the npm packages listed in reference/assets/README.md.

Prints `CHANGED:` / `DEPRECATED:` / `MISSING:` lines (empty output = nothing to do). Used by the weekly maintenance job.
"""
import json, re, sys, urllib.request

SPDX = {"ISC": "ISC", "MIT": "MIT", "CC0 1.0": "CC0-1.0", "no-charge": "no charge"}

def rows(text):
    """Yield (first npm package, expected license marker) for table rows that name a package."""
    for line in text.splitlines():
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 4 or not cells[0].startswith("["):
            continue
        pkg = next((m for c in cells[2:] for m in re.findall(r"`(@?[a-z0-9][\w./-]*)`", c) if "<" not in m), None)
        lic = next((v for k, v in SPDX.items() if cells[1].startswith(k) or k in cells[1]), None)
        if pkg and lic:
            yield pkg, lic

# Self-check of the parser on a known row (keeps the table format and the script in sync).
assert list(rows("| [Lucide](https://lucide.dev) | ISC | 2,313 icons | `lucide`, `lucide-react` | Default |")) == [("lucide", "ISC")]

for pkg, expected in rows(open("reference/assets/README.md", encoding="utf-8").read()):
    try:
        with urllib.request.urlopen(f"https://registry.npmjs.org/{pkg}/latest", timeout=20) as r:
            meta = json.load(r)
    except Exception as e:  # network or 404: report, never fail the job
        print(f"MISSING: {pkg} ({e})")
        continue
    lic = str(meta.get("license", ""))
    if expected not in lic:
        print(f"CHANGED: {pkg} {meta.get('version')} license is '{lic}', reference says '{expected}'")
    if meta.get("deprecated"):
        print(f"DEPRECATED: {pkg} {meta.get('version')}: {meta['deprecated']}")
sys.exit(0)
