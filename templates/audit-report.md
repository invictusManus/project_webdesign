# Website audit: [domain]

Date: [YYYY-MM-DD] · Auditor: [name] · Blueprint version: [commit or tag]

## 1. Summary

- MUST rules: [x] / [y] pass · SHOULD: [x] / [y] · Not verified: [n]
- Top 3 risks:
- Top 3 quick wins:

## 2. Scope & method

| Item | Value |
|---|---|
| URLs / templates audited | |
| Site type (profile) | |
| Tools & data sources | crawl, PageSpeed Insights, Search Console, Observatory, Rich Results Test, axe, manual |
| Access available | GSC yes/no · GA4 yes/no · CMS yes/no · DNS yes/no |
| Limits | e.g. no field data, staging only, no login |

## 3. Baseline

| Metric | Value | Source |
|---|---|---|
| Organic clicks (28 days) | | GSC |
| Indexed pages | | GSC |
| Key events / conversion rate | | GA4 |
| Core Web Vitals (p75 mobile) LCP / INP / CLS | | CrUX |
| Referring domains | | Backlink tool |
| AI visibility (prompt set) | | GEO-13 |

## 4. Findings

Status: pass · fail · n/a · not verified. Severity per QA-10.

| Rule | Status | Evidence | Severity | Fix | Owner | Due |
|---|---|---|---|---|---|---|
| SEO-08 | fail | `/old-page/` returns 200 with home-page content | P1 | 301 to `/new-page/` | | |
| | | | | | | |

## 5. Action plan

| When | Actions |
|---|---|
| Now (P0/P1) | |
| 30 days | |
| 60–90 days | |

## 6. Verification after fixes

For each fixed rule: date, method, result.

## 7. Not verified & assumptions

What could not be checked and why; what would be needed.
