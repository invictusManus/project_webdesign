#!/usr/bin/env python3
"""Print relative Markdown links that point to missing files (code spans and fenced blocks ignored)."""
import glob, os, re

for f in glob.glob("**/*.md", recursive=True):
    lines, fenced = [], False
    for line in open(f):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            lines.append(line)
    text = re.sub(r"`[^`\n]*`", "", "".join(lines))
    for t in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"[a-z]+:|#", t):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), t.split("#")[0]))):
            print(f"{f} -> {t}")
