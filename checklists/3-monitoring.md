# Monitoring & growth routine

Recurring checks for a live site. Each item names the rule it keeps true. Record each pass in the KPI dashboard (MSR-25) or the issue tracker.

## Weekly

- [ ] Uptime incidents and error-tracker alerts reviewed (MSR-21, MSR-23)
- [ ] Search Console: Page indexing, manual actions, security issues (MSR-02)
- [ ] Rankings for the core keyword set, by device and market (MSR-24)
- [ ] Synthetic test submission of the main form arrives (TEC-17)
- [ ] Backups ran successfully (TEC-12)

## Monthly

- [ ] KPI dashboard review: traffic by channel, key events, conversion rate (MSR-25)
- [ ] Field Core Web Vitals per template (PRF-01, PRF-05)
- [ ] AI visibility: prompt set, Search Console and Bing AI reports (GEO-13); wrong brand facts traced (GEO-14)
- [ ] Funnel drop-off reviewed, 1–3 conversion hypotheses prioritized (UX-14, UX-16)
- [ ] Dependency and CMS updates merged (TEC-25, SEC-15)
- [ ] Broken internal links fixed (SEO-25)
- [ ] New backlinks and brand mentions reviewed (SEO-26, GEO-10)
- [ ] Search Console data exported and changes logged (MSR-26); clicks vs. organic sessions compared by trend (MSR-29)
- [ ] Spam check: `site:` plus spam terms, Security issues, forwarded GSC messages (SEC-20)
- [ ] After template releases: rich result, Merchant listings and Video reports (MSR-27)

## Quarterly

- [ ] Content decay: improve first, merge or remove only the unsalvageable (CON-13)
- [ ] Crawl stats with Page indexing; Google-selected vs. declared canonicals (MSR-28)
- [ ] Backlink profile review (SEO-28)
- [ ] Security headers and TLS re-checked (SEC-01, SEC-03); DAST baseline scan (SEC-19)
- [ ] Accessibility regression: automated scan plus manual spot check of one core flow (A11Y-23, A11Y-24)
- [ ] Third-party inventory matches live network requests (TEC-20)
- [ ] Access review: remove leavers, confirm 2FA (TEC-13, TEC-27)
- [ ] Standards re-verified against the watch list in the README

## Yearly

- [ ] Restore test from backup (TEC-12)
- [ ] `security.txt` `Expires` renewed (SEC-18)
- [ ] Privacy policy, Impressum, accessibility statement and terms reviewed (PRV-04, PRV-10, A11Y-02)
- [ ] Every page past its review date reviewed (CON-12)
- [ ] Domain renewal, registrar lock and DNS records checked (TEC-13, TEC-14, TEC-15)
- [ ] Tool stack review ([`TOOLS.md`](../TOOLS.md))

## Triggers → action

Default thresholds; tune them per site.

| Signal | Threshold | First action |
|---|---|---|
| Organic clicks drop | > 20 % week over week, not seasonal | Triage per MSR-30 (anomalies, ranking updates, seasonality, search type), then indexing, manual actions, tracking; crawl (QA-08) |
| Impressions stable, clicks down | Sustained | Review titles and snippets (SEO-15, SEO-16); check rich-result competitors |
| Crawl stats: `5xx`, host unavailable, response time up | Any | Check server, CDN and WAF rules for Googlebot (TEC-29, TEC-30) |
| Core update finished | Rollout end date | Wait a full week, compare with the week before it began (MSR-30) |
| Indexed pages change | > 10 % up or down | Check noindex, canonicals, soft 404s, spam URLs (SEO-02, SEO-06, SEO-08) |
| Conversion rate drop | > 15 % vs. 4-week average | Test forms and checkout end to end; verify key events (TEC-17, MSR-08) |
| Core Web Vital not "good" | Any metric on any template | Apply the matching performance rules; re-test (PRF-01) |
| New 404s | > 50 per day | Extend the redirect map (SEO-35) |
| AI answer wrong about the brand | Any | Trace and fix at source (GEO-14) |
| Security finding | High or critical | Patch within the SLA (SEC-15) |
| Downtime | Any incident | Post-mortem with a root cause and a prevention step |
