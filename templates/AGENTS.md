# AGENTS.md

This website follows the Website Foundation blueprint: https://github.com/invictusManus/project_webdesign (pinned at: [tag or commit]). Rules are cited by ID, e.g. `PRF-08`.

## Project facts

- Site type: [profile from standards/site-types.md]
- Stack & rendering: [framework, CMS, hosting; rendering per page type]
- Commands: dev `[…]` · build `[…]` · verify `[…]`
- Brand: `DESIGN.md` · tokens: `tokens.json` · URL and keyword map: `url-map.csv` · brief: `[path]`
- Production URL: [URL] · staging: [URL] (auth required)

## Before you change anything

0. Use the ponytail skill at level full (`/ponytail full`). If it isn't installed, stop and ask the user to install it (marketplace `DietrichGebert/ponytail`).
1. Read `DESIGN.md` before UI or copy work. Use tokens only; never raw colors, sizes or spacings.
2. Read the blueprint standards for the area you touch. MUST rules are hard requirements.
3. Content changes follow `url-map.csv`: one intent per URL, and no new indexable page without an entry.
4. Standards 02 (design system), 03 (UX), 09 (accessibility), 14 (UX psychology), 15 (layout & responsive) and 16 (components) are foundational requirements. If `DESIGN.md` has no intake answers, ask for palette and style direction first (DES-13).
5. Check every new or changed text line by line against the blueprint's `reference/ai-writing/checklist.md` (CON-16).

## Never, without explicit approval

- Submit live forms, send email, or trigger payments.
- Change DNS, consent settings, analytics or tag manager, or publish to production.
- Add a third-party script, font or embed without a third-party inventory entry (TEC-20).
- Add `noindex`, `Disallow` or redirects on production, or remove any.

## Definition of done (QA-11)

- The affected rule IDs are verified with their Verify method, and cited in the commit message.
- `[verify command]` passes: build, HTML validation, links, Lighthouse CI assertions.
- The preview is checked at 390 px and 1440 px, keyboard-only, with no console errors.
- Report what changed, which rules you verified and how, and what remains unverified.
