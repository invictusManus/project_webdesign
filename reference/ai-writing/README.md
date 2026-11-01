# AI-writing signs: complete notes

Notes on Wikipedia's field guide "Signs of AI writing" and the guidance pages that belong to it. The guide lists patterns typical of chatbot output (vocabulary, tone, structure, punctuation, chat and markup leftovers) with exact indicator words and phrases.

- Rule for this repository: check every text written for a website against [`checklist.md`](checklist.md) before publishing. That covers pages, sections, blog posts, navigation labels, buttons, and meta titles and descriptions.
- Use the notes files when a checklist item needs its source: the exact words, the explanation, the examples, and the false-positive warnings.
- The guide is descriptive, not prescriptive. Its patterns are signs of generic or unverified content, not the problem itself. Fix the content (specific, sourced, checkable), not only the symptom. A clean pass does not prove text is human or accurate.

## License and status

- Source content © Wikipedia contributors, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Authors are listed in each page's history (append `?action=history` to the page URL).
- These notes are an adaptation: summarized and restructured, with indicator words and phrases kept exact. They are themselves licensed CC BY-SA 4.0, unlike the rest of this repository (MIT). Keep that license and this attribution if you copy or adapt them.
- Not an official Wikipedia policy. The pages are essays and information pages by editors of WikiProject AI Cleanup. When in doubt, the linked page wins.
- Retrieval date for every page: 2026-11-01 (raw wikitext). The revision ID and timestamp of each page are in its notes file.
- The pages are written for Wikipedia editors. Signs that only make sense on a wiki are kept in the notes for completeness and marked as not transferable in the checklist.

## Page index

| Page | URL | Retrieved | Notes file |
|---|---|---|---|
| Wikipedia:Signs of AI writing (main page) | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | 2026-11-01 | [`signs-of-ai-writing.md`](signs-of-ai-writing.md) |
| Wikipedia:Signs of AI writing/Style | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style | 2026-11-01 | [`signs-style.md`](signs-style.md) |
| Wikipedia:Signs of AI writing/Markup | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Markup | 2026-11-01 | [`signs-markup.md`](signs-markup.md) |
| Wikipedia:Signs of AI writing/Wikitext wrapped in Markdown code blocks from chatbots | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Wikitext_wrapped_in_Markdown_code_blocks_from_chatbots | 2026-11-01 | [`signs-markup.md`](signs-markup.md) (second `##`) |
| Wikipedia:Signs of AI use in comments | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_use_in_comments | 2026-11-01 | [`signs-comments.md`](signs-comments.md) |
| Wikipedia:Canned user pages | https://en.wikipedia.org/wiki/Wikipedia:Canned_user_pages | 2026-11-01 | [`canned-user-pages.md`](canned-user-pages.md) |
| Wikipedia:Marketing buzzspeak (incl. "Marketing buzzspeak and artificial intelligence") | https://en.wikipedia.org/wiki/Wikipedia:Marketing_buzzspeak | 2026-11-01 | [`marketing-buzzspeak.md`](marketing-buzzspeak.md) |
| Wikipedia:Identifying LLM unblock requests | https://en.wikipedia.org/wiki/Wikipedia:Identifying_LLM_unblock_requests | 2026-11-01 | [`identifying-llm-unblock-requests.md`](identifying-llm-unblock-requests.md) |
| Wikipedia:WikiProject AI Cleanup/Guide and resources (also reached as "Guide") | https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide_and_resources | 2026-11-01 | [`ai-cleanup-guide.md`](ai-cleanup-guide.md) |
| Wikipedia:WikiProject AI Cleanup (project hub; "Editing advice" only) | https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup | 2026-11-01 | [`ai-cleanup-guide.md`](ai-cleanup-guide.md) (second `##`) |

Derived file: [`checklist.md`](checklist.md), the pre-publish checklist built only from the signs in these notes.

## How the notes are structured

- One `##` heading per source page, with its URL on the next line. `###` is the source's top-level section, `####` and `#####` its subsections.
- Indicator words are in backticks and kept exact, including the source's alternation syntax such as `a crucial/pivotal/vital/significant/key role/moment`. Slashes mean alternatives; `...` is a gap to fill.
- Long example galleries, search-link lists, per-user example tables and process instructions for Wikipedia editors are summarized or skipped, and the notes say so where it happens.
- Where a sign has a web-copy angle the notes say so, so the checklist items can point back to their source section.

## Pages checked and left out

Scope was guidance on recognizing or avoiding AI-style writing, found from the main page's header links, "see also", "further" hatnotes and the navigation box ("Wikipedia artificial intelligence"). Left out:

- Article examples: the subpages under `Wikipedia:Signs of AI writing/Examples/` (many linked from the main page). Raw example material only.
- `Wikipedia:AI or not quiz`: a practice quiz. Retrieved and read; no signs not already covered.
- `Wikipedia:The LLM-written ANI report`: a noticeboard-report format essay. Retrieved and read; it is about one report genre at a conduct noticeboard, and the comments page links to it.
- `Wikipedia:Writing articles with large language models` (the LLM content guideline): a usage rule for editors, no signs. Retrieved and read.
- `Wikipedia:Artificial intelligence resources`: a directory. Retrieved and read, used only to find candidate pages.
- Remaining navigation-box pages (policies on AI images, speedy deletion G15, presumptive removal, LLM-assisted translation, talk page guidelines, disruptive editing, AI noticeboard and cases, deletion sorting, WikiProject AI Tools, templates, tracking) and conduct essays (for example "Help, I've been accused of using AI!", "Do not lie about AI"). Policy, process or conduct, not writing signs.
- User pages and noticeboards: for example a user guide to finding AI-generated text, an AI slop detection user page, user essays. Excluded by scope.
- `Template:Looks AI-generated`: a maintenance tag, no content.
- The encyclopedia article "Signs of AI writing" (the main page's "for" hatnote): encyclopedic coverage, not guidance.
- External links and further reading on the main page: CanYouPasstheTuringTest.com, the Tropes AI Writing Pattern Directory (tropes.fyi), and a New York Times Magazine article by Sam Kriss (subscription). Not retrieved.

## Keeping it current

The guide changes often (the main page was edited the day before retrieval, and it dates model-specific signs by month). Re-fetch the raw wikitext with `curl -s "https://en.wikipedia.org/w/index.php?title=<Page_title>&action=raw"`, compare the revision ID in each notes file, and update the notes and the checklist together. Early signs go stale as models change, so treat the checklist as a screening aid and not a standard.
