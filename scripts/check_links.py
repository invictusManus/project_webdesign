#!/usr/bin/env python3
"""Print relative Markdown links that point to missing files (code spans and fenced blocks ignored)."""
import glob, os, re

for f in glob.glob("**/*.md", recursive=True):
    text = re.sub(r"```.*?```", "", open(f).read(), flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    for t in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"[a-z]+:|#", t):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), t.split("#")[0]))):
            print(f"{f} -> {t}")
