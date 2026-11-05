#!/usr/bin/env bash
# Rule ID consistency check. Usage: scripts/check.sh (exit 1 on any failure)
set -euo pipefail
cd "$(dirname "$0")/.."

ID='(STR|DES|UX|CON|SEO|GEO|TEC|PRF|A11Y|SEC|PRV|MSR|I18N|QA|PSY|LAY|CMP|PRJ)-[0-9]{2}'
fail=0
err() { echo "FAIL: $*"; fail=1; }

# Rule rows look like: | SEO-01 | MUST | rule | verify |
rows=$(grep -hE "^\| $ID \| (MUST|SHOULD|COULD|RETIRED) \|" standards/[0-9]*.md || true)
defined=$(awk -F'|' 'NF { gsub(/ /, "", $2); print $2 }' <<<"$rows" | sort)
[ -n "$defined" ] || err "no rules found in standards/"

dups=$(uniq -d <<<"$defined")
[ -z "$dups" ] || err "duplicate IDs: $(echo $dups)"

refs=$(grep -rhoE "$ID" --exclude-dir=.git --exclude-dir=scripts . | sort -u)
missing=$(comm -23 <(echo "$refs") <(sort -u <<<"$defined"))
[ -z "$missing" ] || err "referenced but not defined: $(echo $missing)"

musts=$(awk -F'|' '$3 ~ /MUST/ { gsub(/ /, "", $2); print $2 }' <<<"$rows" | sort -u)
listed=$(grep -hoE "$ID" checklists/*.md 2>/dev/null | sort -u || true)
unlisted=$(comm -23 <(echo "$musts") <(echo "$listed"))
[ -z "$unlisted" ] || err "MUST rules missing from checklists/: $(echo $unlisted)"

for f in standards/[0-9]*.md; do
  grep -q '^Last verified: ' "$f" || err "$f has no 'Last verified:' line"
done

# Every Google doc page in the reference index has notes
idx=reference/google-search/README.md
if [ -f "$idx" ]; then
  for u in $(grep -oE '\| \[[^]]+\]\(https://developers\.google\.com/[^)]+\)' "$idx" | sed -E 's/.*\((.*)\)/\1/' | sort -u); do
    grep -qE "${u//./\\.}([^a-z0-9/-]|$)" reference/google-search/[0-9]*.md 2>/dev/null || err "no notes for $u"
  done
fi

# Standards stay short and are all listed in README
for f in standards/[0-9]*.md; do
  n=$(wc -l <"$f"); [ "$n" -le 150 ] || err "$f has $n lines (limit 150)"
  b=$(basename "$f" .md); grep -q "$b" README.md || err "$b not listed in README.md"
done

# Design tokens: types, units, references, dark coverage, contrast (DES-03, DES-41)
python3 scripts/check_tokens.py || err "templates/tokens*.json invalid"
python3 scripts/tokens_to_css.py --check || err "templates/tokens.css out of date"

# rules.csv matches standards/
python3 scripts/rules_index.py --check || err "rules.csv out of date"

# Relative Markdown links resolve
broken=$(python3 scripts/check_links.py)
[ -z "$broken" ] || err "broken relative links: $(echo $broken)"

[ "$fail" -eq 0 ] && echo "OK: $(wc -l <<<"$defined" | tr -d ' ') rules, $(wc -l <<<"$musts" | tr -d ' ') MUST, all referenced and listed"
exit "$fail"
