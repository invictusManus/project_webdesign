# Search Console runbook

Everything to do in Google Search Console, in order, from setup to routine. Each item names the rule it keeps true; details and verify methods are in [`11-measurement.md`](../standards/11-measurement.md). Conditional items: *(shop)*, *(multilingual)*, *(relaunch)*.

## 1 · Setup (before launch)

- [ ] Domain property verified by DNS TXT; token kept permanently (MSR-01, MSR-31)
- [ ] ≥ 2 owners incl. the site owner; agencies and tools Full or Restricted (MSR-01, MSR-31)
- [ ] Email notifications on, messages forwarded to a monitored mailbox (MSR-05, SEC-20)
- [ ] Associations: GA4 (MSR-05) · *(shop)* Merchant Center · Google Ads where used (MSR-37)
- [ ] Bulk data export to BigQuery on, change log started (MSR-26)
- [ ] Bing Webmaster Tools imported from Search Console, IndexNow live (MSR-04)

## 2 · Launch day

- [ ] robots.txt report: every host "Fetched", no `Disallow: /` (MSR-33, SEO-04)
- [ ] Sitemap index submitted, status "Success" (MSR-02, MSR-32)
- [ ] URL Inspection live test on the home page and top money pages: indexable, rendered HTML complete, canonical correct; then Request indexing (MSR-03, MSR-34)
- [ ] *(relaunch, new domain)* Change of address for every old verified variant (SEO-37)

## 3 · First 14 days

- [ ] Day 2: Page indexing and Crawl stats show no unexpected errors (MSR-02, MSR-28)
- [ ] Day 3–7: every "not indexed" reason classified; defects fixed and "Validate fix" started (MSR-34)
- [ ] Day 7: Sitemaps discovered count ≈ indexable URLs (MSR-32)
- [ ] Day 7: rich result, Merchant listings and Video reports checked (MSR-27)
- [ ] Day 14: Performance baseline recorded: clicks, impressions, CTR, position by page (MSR-36)

## 4 · Weekly

- [ ] Manual actions and Security issues clean; any finding handled per MSR-35
- [ ] Page indexing: new defects triaged, open validations followed up (MSR-34)

## 5 · Monthly

- [ ] Performance review: brand vs. non-brand, CTR opportunities, losers, search types, Discover (MSR-36)
- [ ] Core Web Vitals and HTTPS reports clean (MSR-36)
- [ ] After template releases: enhancement reports (MSR-27)
- [ ] Data exported and changes logged; clicks vs. organic sessions (MSR-26, MSR-29)

## 6 · Quarterly

- [ ] Users and permissions reviewed, leavers removed (MSR-31)
- [ ] Crawl stats with Page indexing; Google-selected vs. declared canonicals (MSR-28)
- [ ] Links report: internal links to key pages, top linking sites (MSR-37, SEO-28)
- [ ] Sitemaps still "Success"; robots.txt fetched for every host (MSR-32, MSR-33)

## On demand

- [ ] Traffic drop: triage per MSR-30
- [ ] Page removed for good or urgently: Removals tool, plus `404`/`410` or `noindex` (SEO-42)
