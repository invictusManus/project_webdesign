# AGENTS.md

This repository is a web design 101: a step-by-step guide (`GUIDE.md`) on top of testable rules, checklists and templates. It contains no application code.

## Applying the blueprint to a website project

1. Read `README.md`. Then find the site's profile in `standards/site-types.md`. `GUIDE.md` gives the order of work.
2. Load only the standards the task touches. A performance fix needs `standards/08-performance.md`, not all of them.
3. MUST rules are hard requirements. SHOULD rules are the default unless the project brief says otherwise. Apply COULD rules only when asked.
4. Cite rule IDs in commits, pull requests and reports, e.g. `fix(PRF-08): eager-load hero image`.
5. Never report a rule as passed without running its Verify method. If a check needs access you lack (Search Console, live analytics, DNS), say so and leave it open.
6. Rules tagged `[EU]` describe legal requirements, not legal advice. Flag them for human review.
7. Never submit real forms, send emails, make purchases, or change DNS, analytics or consent settings without explicit approval.
8. To make an AI agent apply the blueprint in a website repository, copy `templates/AGENTS.md` into that repository.

## Editing this repository

- Write in English and keep it terse. One rule per table row, with a measurable threshold and a Verify method. Put sources at the end of the file.
- Each rule exists once. Elsewhere, reference its ID instead of restating it.
- Never renumber or reuse an ID. To retire a rule, set its level to `RETIRED` and name its replacement.
- Cite official or primary sources only. Mark unofficial proposals with ⚗.
- When you re-check a file's rules against their sources, update its `Last verified` line.
- Keep each standard under about 150 lines. Explanations belong in `GUIDE.md`, `GLOSSARY.md` or a standard's "Why it matters" line, never in rule rows. No lists of example repositories or projects.
- Run `scripts/check.sh` before every commit. It must print `OK`.
