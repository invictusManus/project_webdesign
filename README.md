# Website Foundation

A compact, stack-agnostic blueprint for building and optimizing professional websites: strategy, design, UX, content, SEO, GEO/AEO, tech, performance, accessibility, security, privacy, measurement, internationalization and QA.

It is not a tutorial and not a website. Every file is a rule set, a checklist or a template you can apply directly, by hand or through an AI coding agent.

## How to use

| Goal | Start with |
|---|---|
| Build a new website | [`checklists/1-preflight.md`](checklists/1-preflight.md) → standards → [`checklists/2-launch.md`](checklists/2-launch.md) |
| Audit or optimize an existing site | [`checklists/2-launch.md`](checklists/2-launch.md) as audit sheet + [`templates/audit-report.md`](templates/audit-report.md) |
| Relaunch or migrate a site | [`checklists/2-launch.md`](checklists/2-launch.md) § D + [`templates/url-map.csv`](templates/url-map.csv) |
| Let an AI agent work on a website repo | Copy [`templates/AGENTS.md`](templates/AGENTS.md) into that repo |
| Operate and grow a live site | [`checklists/3-monitoring.md`](checklists/3-monitoring.md) |
| Pick tools | [`TOOLS.md`](TOOLS.md) |

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
- Checklists reference rule IDs only. [`standards/site-types.md`](standards/site-types.md) raises or relaxes levels per site type.
- IDs are never reused or renumbered. A removed rule keeps its row with level `RETIRED`.

## Contents

```
README.md · AGENTS.md · TOOLS.md
standards/   01-strategy · 02-brand-design · 03-ux · 04-content · 05-seo · 06-geo-aeo · 07-tech
             08-performance · 09-accessibility · 10-security-privacy · 11-measurement · 12-i18n · 13-qa
             site-types
checklists/  1-preflight · 2-launch · 3-monitoring
templates/   project-brief · content-brief · audit-report · url-map.csv · AGENTS · DESIGN · tokens.json
             head.html · robots.txt · _headers · security.txt · consent-default.html
             schema/ (site graph, local business, article, product) · ci/ (quality workflow, Lighthouse CI)
scripts/     check.sh (rule ID consistency)
```

## Coverage

| Area | Rules |
|---|---|
| Strategy & competition | `01-strategy` |
| Branding & design | `02-brand-design`, `templates/DESIGN.md`, `templates/tokens.json` |
| UX/UI & conversion | `03-ux` |
| Content, E-E-A-T & media | `04-content` |
| SEO (technical, on-page, off-page, local, migration) | `05-seo` |
| GEO & AEO (AI search) | `06-geo-aeo` |
| Technical foundation, hosting, domains, DNS, integrations | `07-tech` |
| Performance & Core Web Vitals | `08-performance` |
| Accessibility | `09-accessibility` |
| Security & compliance (OWASP, HTTPS, GDPR, consent, legal pages) | `10-security-privacy` |
| Google ecosystem (Search Console, GA4, GTM, sitemaps, indexing, conversions) | `11-measurement` |
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
