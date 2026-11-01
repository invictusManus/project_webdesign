#!/usr/bin/env python3
"""Compare Google's Search documentation with reference/google-search/.

Usage:
  scripts/google-docs.py              list new, removed and changed pages (exit 1 if any)
  scripts/google-docs.py --text DIR   also save the full text of new/changed pages to DIR

Changes are detected via each page's "Last updated" date against the index in
reference/google-search/README.md. Re-document changed pages from the saved text.
"""
import concurrent.futures as cf
import html
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "reference", "google-search", "README.md")
BASE = "https://developers.google.com"
NAV_PAGES = (BASE + "/search/docs", BASE + "/crawling/docs/crawlers-fetchers/overview-google-crawlers")
EXTRA = (BASE + "/search/updates", BASE + "/crawling/docs/changelog")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (docs change check)"})
    return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")


def nav_urls():
    urls = set(EXTRA)
    for page in NAV_PAGES:
        h = get(page)
        nav = h[h.find("<devsite-book-nav"):h.find("</devsite-book-nav>")]
        for m in re.finditer(r'<a href="(/(?:search/docs|crawling/docs)[^"#?]*)"', nav):
            u = BASE + m.group(1).rstrip("/")
            if not u.endswith("/search/docs"):
                urls.add(u)
    return urls


class Text(HTMLParser):
    """Article body to plain markdown-ish text (headings, lists, tables, code)."""
    SKIP = ("script", "style", "devsite-feedback", "devsite-thumb-rating", "button")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.pre, self.skip = [], 0, 0

    def handle_starttag(self, t, a):
        if t in self.SKIP:
            self.skip += 1
        mark = {"pre": "\n```\n", "li": "\n- ", "p": "\n", "div": "\n", "br": "\n", "tr": "\n|", "td": " ", "th": " "}
        if t in ("h1", "h2", "h3", "h4", "h5"):
            self.out.append("\n\n" + "#" * int(t[1]) + " ")
        elif t in mark:
            self.out.append(mark[t])
        if t == "pre":
            self.pre += 1

    def handle_endtag(self, t):
        if t in self.SKIP:
            self.skip = max(0, self.skip - 1)
        if t == "pre":
            self.pre -= 1
            self.out.append("\n```\n")
        elif t in ("td", "th"):
            self.out.append(" |")
        elif t in ("p", "h1", "h2", "h3", "h4", "h5", "table", "ul", "ol"):
            self.out.append("\n")

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d if self.pre else re.sub(r"\s+", " ", d))


def page(url):
    try:
        h = get(url)
    except Exception as e:  # report, don't abort the whole run
        return url, None, None, f"ERR {e}"
    date = re.search(r"Last updated (\d{4}-\d{2}-\d{2})", h)
    title = re.search(r'<h1 class="devsite-page-title"[^>]*>(.*?)</h1>', h, re.S)
    i = h.find('class="devsite-article-body')
    body = ""
    if i >= 0:
        end = h.find("devsite-content-footer", i)
        p = Text()
        p.feed(h[h.rfind("<", 0, i):end if end > 0 else len(h)])
        body = re.sub(r"\n{3,}", "\n\n", "".join(p.out)).strip()
    name = html.unescape(re.sub("<[^>]+>", "", title.group(1)).strip()) if title else url
    return url, name, date.group(1) if date else "unknown", body


def main():
    text_dir = sys.argv[sys.argv.index("--text") + 1] if "--text" in sys.argv else None
    indexed = dict(re.findall(r"\| \[[^\]]+\]\((https://developers\.google\.com/[^)]+)\) \| (\S+) \|", open(INDEX).read()))
    live = nav_urls()
    with cf.ThreadPoolExecutor(8) as ex:
        pages = {u: r for u, *r in ex.map(page, sorted(live))}
    new = sorted(live - indexed.keys())
    removed = sorted(indexed.keys() - live)
    changed = sorted(u for u in live & indexed.keys() if pages[u][1] not in (indexed[u], "unknown"))
    errors = sorted(u for u, r in pages.items() if r[2].startswith("ERR"))
    for label, items in (("NEW", new), ("REMOVED", removed), ("CHANGED", changed), ("ERROR", errors)):
        for u in items:
            extra = f" ({indexed.get(u, '-')} -> {pages[u][1]})" if label == "CHANGED" else ""
            print(f"{label}: {u}{extra}")
    if text_dir:
        os.makedirs(text_dir, exist_ok=True)
        for u in new + changed:
            name, date, body = pages[u]
            slug = re.sub(r"[^a-z0-9]+", "-", u.split("developers.google.com/")[1].lower()).strip("-")
            with open(os.path.join(text_dir, slug + ".md"), "w") as f:
                f.write(f"TITLE: {name}\nURL: {u}\nLAST UPDATED: {date}\n\n{body}\n")
    print(f"{len(live)} live pages · {len(new)} new · {len(removed)} removed · {len(changed)} changed · {len(errors)} errors")
    sys.exit(1 if new or removed or changed or errors else 0)


if __name__ == "__main__":
    main()
