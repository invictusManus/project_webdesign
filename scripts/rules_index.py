#!/usr/bin/env python3
"""Write rules.csv (one row per rule) from standards/. With --check, print a message and exit 1 if rules.csv is stale."""
import csv, glob, io, re, sys

ROW = re.compile(r"^\| ([A-Z0-9]+-\d{2}) \| (MUST|SHOULD|COULD|RETIRED) \| (.*) \| (.*) \|$")
out = io.StringIO()
w = csv.writer(out, lineterminator="\n")
w.writerow(["id", "level", "tags", "condition", "standard", "rule", "verify"])
for f in sorted(glob.glob("standards/[0-9]*.md")):
    for line in open(f, encoding="utf-8"):
        m = ROW.match(line.rstrip("\n"))
        if not m:
            continue
        rid, level, rule, verify = m.groups()
        tags = " ".join(t for t, k in (("house", "[house]"), ("EU", "[EU]"), ("experimental", "⚗")) if k in rule)
        cond = re.match(r"\*\(([^)]+)\)\*", re.sub(r"^(\[(house|EU)\] )+", "", rule))
        w.writerow([rid, level, tags, cond.group(1) if cond else "", f.split("/")[-1][:-3], rule, verify])

new = out.getvalue()
if "--check" in sys.argv:
    try:
        old = open("rules.csv", encoding="utf-8").read()
    except FileNotFoundError:
        old = ""
    if old != new:
        print("rules.csv is stale: run scripts/rules_index.py")
        sys.exit(1)
else:
    open("rules.csv", "w", encoding="utf-8").write(new)
