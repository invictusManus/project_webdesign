# Website Foundation

A complete web design 101: a stack-agnostic guide and blueprint for building and optimizing professional websites. It covers strategy, design, UX, content, SEO, GEO/AEO, tech, performance, accessibility, security, privacy, measurement, internationalization and QA.

There are three layers:
- **Learn:** [`GUIDE.md`](GUIDE.md) walks you from zero to launch to growth in 41 steps, explaining why each step matters. [`GLOSSARY.md`](GLOSSARY.md) explains the terms.
- **Apply:** the standards, checklists and templates hold the testable rules, which you can apply by hand or through an AI coding agent.
- **Reference:** [`reference/google-search/`](reference/google-search/) condenses every page of Google's Search and crawling documentation (184 pages) into notes. It holds every property, limit and exception behind the SEO rules. [`reference/ai-writing/`](reference/ai-writing/README.md) documents Wikipedia's *Signs of AI writing* (CC BY-SA 4.0); every website text is checked against its checklist (CON-16).

## How to use

| Goal | Start with |
|---|---|
| Learn web design from scratch | [`GUIDE.md`](GUIDE.md) + [`GLOSSARY.md`](GLOSSARY.md) |
| Build a new website | [`checklists/1-preflight.md`](checklists/1-preflight.md) → standards → [`checklists/2-launch.md`](checklists/2-launch.md) |
| Audit or optimize an existing site | [`checklists/2-launch.md`](checklists/2-launch.md) as audit sheet + [`templates/audit-report.md`](templates/audit-report.md) |
| Relaunch or migrate a site | [`checklists/2-launch.md`](checklists/2-launch.md) § D + [`templates/url-map.csv`](templates/url-map.csv) |
| Let an AI agent work on a website repo | Copy [`templates/AGENTS.md`](templates/AGENTS.md) into that repo |
| Operate and grow a live site | [`checklists/3-monitoring.md`](checklists/3-monitoring.md) |
| Pick tools | [`TOOLS.md`](TOOLS.md) |
| Look up what Google says about any SEO topic | [`reference/google-search/`](reference/google-search/README.md) |

## Lifecycle

| Phase | Files |
|---|---|
| 1. Preflight: goals, research, accounts, decisions | `checklists/1-preflight.md`, `templates/project-brief.md`, `templates/url-map.csv`, `standards/01-strategy.md`, `standards/site-types.md` |
| 2. Design & build | `standards/02`–`13`, `templates/DESIGN.md`, `templates/tokens.json`, `templates/content-brief.md`, code templates |
| 3. Launch gate | `checklists/2-launch.md` § A (every MUST rule) |
| 4. Launch & first 14 days | `checklists/2-launch.md` § B–C |
| 5. Monitor & improve | `checklists/3-monitoring.md` |

## Rule format

Every rule exists exactly once, in `standards/`, with a stable ID:

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRF-08 | MUST | The LCP image is in the initial HTML, never lazy-loaded, with `fetchpriority="high"`. | Lighthouse "LCP request discovery" |

- **MUST**: baseline. Blocks launch unless an exception is documented with an owner and a date.
- **SHOULD**: professional standard. Deviate only for a documented reason.
- **COULD**: excellence. Worth doing once the MUST and SHOULD rules hold.
- **[EU]**: legal requirement in the EU/DACH; other regions get short notes. These rules describe requirements; they are not legal advice.
- **⚗**: experimental. No official support or proven effect, but cheap to adopt.
- **[house]**: our own choice, stricter than or beyond what Google documents. It never contradicts Google.
- **Source of truth for search:** Google's documentation, condensed in [`reference/google-search/`](reference/google-search/README.md). Where a rule and Google disagree, Google wins and the rule is fixed. Other areas follow their primary standard: W3C/WCAG for accessibility, OWASP/BSI for security, EU and German law for privacy.
- Checklists reference rule IDs only. [`standards/site-types.md`](standards/site-types.md) raises or relaxes levels per site type.
- IDs are never reused or renumbered. A removed rule keeps its row with level `RETIRED`.

## Contents

```
README.md · GUIDE.md · GLOSSARY.md · AGENTS.md · TOOLS.md
standards/   01-strategy · 02-brand-design · 03-ux · 04-content · 05-seo · 06-geo-aeo · 07-tech
             08-performance · 09-accessibility · 10-security-privacy · 11-measurement · 12-i18n · 13-qa
             14-ux-psychology · 15-layout-responsive · 16-components
             site-types
checklists/  1-preflight · 2-launch · 3-monitoring · 4-search-console
templates/   project-brief · content-brief · audit-report · url-map.csv · AGENTS · DESIGN · tokens.json
             component-spec · page-blueprint · accessibility-statement
             head.html · robots.txt · _headers · security.txt · consent-default.html
             schema/ (site graph, local business, article, product) · ci/ (quality workflow, Lighthouse CI)
reference/   google-search/ (notes on all 184 Google Search documentation pages)
             ai-writing/ (Wikipedia: Signs of AI writing, notes and pre-publish checklist)
scripts/     check.sh (rule IDs, checklist coverage, reference coverage, file length, rules.csv)
             rules_index.py (generates rules.csv)
rules.csv    every rule as one row: id, level, tags, condition, standard, rule, verify
```

## Coverage

| Area | Rules |
|---|---|
| Strategy & competition | `01-strategy` |
| Branding & design (golden-ratio system, design intake, type roles, hierarchy, tokens) | `02-brand-design`, `templates/DESIGN.md`, `templates/tokens.json` |
| Layout & responsive design (grid, breakpoints, desktop/tablet/mobile, page structure, header, footer) | `15-layout-responsive` |
| UI components (cards, tables, forms, dialogs, tabs, accordions, states, patterns) | `16-components` |
| UX/UI & conversion, product pages, cart, checkout, on-site search | `03-ux` |
| UX psychology (Gestalt, Hick, Fitts, Jakob, Nielsen, cognitive load, social proof, ethical conversion) | `14-ux-psychology` |
| Content, E-E-A-T & media, editorial style guide, AI-writing review | `04-content`, `reference/ai-writing/` |
| SEO (technical, on-page, off-page, local, migration) | `05-seo`, `reference/google-search/` |
| GEO & AEO (AI search) | `06-geo-aeo`, `reference/google-search/` |
| Technical foundation, hosting, domains, DNS, integrations, CMS and editors | `07-tech` |
| Performance & Core Web Vitals | `08-performance` |
| Accessibility | `09-accessibility` |
| Security & compliance (OWASP, HTTPS, GDPR, consent, legal pages) | `10-security-privacy` |
| Google ecosystem (Search Console, GA4, GTM, sitemaps, indexing, conversions) | `11-measurement`, `checklists/4-search-console.md` |
| Internationalization | `12-i18n` |
| Quality assurance | `13-qa`, `templates/ci/` |
| Monitoring & growth | `11-measurement`, `checklists/3-monitoring.md` |
| Site types (corporate, landing page, blog, SaaS, e-commerce, web app) | `site-types` |

## Keeping it current

Each standard states when its rules were last checked against their sources (`Last verified`). Re-verify every quarter against:

- [Google Search Central updates](https://developers.google.com/search/updates)
- [web.dev blog & Baseline](https://web.dev/blog)
- [Chrome UX Report release notes](https://developer.chrome.com/docs/crux/release-notes)
- [W3C WAI news](https://www.w3.org/WAI/news/)
- [OWASP Top 10](https://owasp.org/Top10/)
- [Schema.org releases](https://schema.org/docs/releases.html)
- [Datenschutzkonferenz](https://www.datenschutzkonferenz-online.de/)
- [EUR-Lex](https://eur-lex.europa.eu/)

Run `scripts/check.sh` after every change.

## License

[MIT](LICENSE)
