# 11 · Measurement & monitoring

**Why it matters:** Without measurement you can't know what works. Search Console shows how Google sees the site, analytics shows what visitors do, and monitoring tells you when something breaks. Guide: steps 8, 28 and 37.

Detail: `reference/google-search/` notes.

Scope: Search Console, Bing Webmaster Tools, GA4, Google Tag Manager, conversion tracking, Merchant Center, uptime/error monitoring, dashboards. The legal side of consent is in [`10-security-privacy.md`](10-security-privacy.md); AI-visibility measurement is in [`06-geo-aeo.md`](06-geo-aeo.md); the recurring routine is in [`checklists/3-monitoring.md`](../checklists/3-monitoring.md).

Last verified: 2026-10

## Search Console & Bing

| ID | Level | Rule | Verify |
|---|---|---|---|
| MSR-01 | MUST | [house] A Search Console **Domain property** is verified by DNS TXT before launch. At least two people are owners, one of them the site owner. | GSC → Settings → Users |
| MSR-02 | MUST | [house] The XML sitemap is submitted in Search Console, and the Page indexing report shows no key URL excluded unexpectedly. | GSC Sitemaps; Page indexing |
| MSR-03 | MUST | On launch day, the home page and top money pages are checked with URL Inspection and indexing is requested for them. Everything else gets indexed through the sitemap and accurate `lastmod`. | GSC URL Inspection |
| MSR-04 | SHOULD | Bing Webmaster Tools is verified (import from Search Console) with the sitemap submitted. An IndexNow key is hosted, and new or changed URLs are submitted automatically. | Bing WMT; IndexNow response 200/202 |
| MSR-05 | SHOULD | Search Console and Bing email alerts are on, and Search Console messages are forwarded to a monitored mailbox. Search Console is linked to GA4. | Account settings |
| MSR-26 | SHOULD | Search Console keeps only 16 months of data: bulk export to BigQuery (or the API) is on. Every significant title, content, template or migration change is logged with its date so traffic changes can be attributed. | GSC bulk export link; change log |
| MSR-27 | SHOULD | After the first deploy and after every template release, the matching Search Console reports are checked: Rich result status (valid up, invalid not up), Unparsable structured data, Merchant listings and Product snippets (shops), Video indexing (video sites), Manual actions. Fixes are validated there. | GSC reports; URL Inspection |
| MSR-28 | SHOULD | Quarterly (monthly for large sites; house heuristic), Crawl stats (host availability, `5xx`, response time) is read together with Page indexing, and the Google-selected canonical of key URLs is compared with the declared one. | GSC Crawl stats; URL Inspection |
| MSR-31 | MUST | Search Console access: agencies, freelancers and tools get Full or Restricted permission, never Owner; delegated owners come only from the site owner's staff. Leavers are removed on their last day, and access is reviewed quarterly. The verification token (DNS TXT) stays in place permanently, because removing it un-verifies the property. | GSC → Settings → Users and permissions; DNS lookup |
| MSR-32 | SHOULD | Sitemaps report: the sitemap index (or each sitemap) is submitted once per property and shows "Success". Discovered URLs roughly match the indexable URLs in `url-map.csv`, and the Page indexing view filtered by sitemap shows key URLs indexed. No resubmitting or pinging after updates (Google retired the ping endpoint); accurate `lastmod` is enough (SEO-07). | GSC Sitemaps; Page indexing (sitemap filter) |
| MSR-33 | SHOULD | The robots.txt report (Settings) lists every host's file as "Fetched" with a recent fetch date. After an urgent robots.txt fix, request a recrawl there (SEO-03, SEO-38). | GSC → Settings → robots.txt |
| MSR-34 | MUST | Page indexing triage (extends MSR-02): every reason under "Why pages aren't indexed" is classified. Intended: `noindex`, page with redirect, alternate page with proper canonical, not found for removed URLs. Defect: soft 404, server error (5xx), blocked by robots.txt on a wanted URL, "Crawled/Discovered – currently not indexed" or "Duplicate without user-selected canonical" on a key URL. Defects are diagnosed in URL Inspection (indexed vs. live test, rendered HTML and screenshot, smartphone crawler, declared vs. Google-selected canonical), fixed, and closed with "Validate fix" until it shows "Passed". | GSC Page indexing; validation status |
| MSR-35 | MUST | Manual actions and Security issues are checked weekly (SEC-20). On a finding: fix every affected page against the named policy, then file a reconsideration request (Manual actions) or "Request review" (Security issues) stating the problem, the fix and the evidence. Log the case with its dates (MSR-26). | GSC Manual actions; Security issues; case log |
| MSR-36 | SHOULD | Monthly Performance review: brand vs. non-brand split (regex filter on brand terms, or the branded-queries filter where available); queries at positions 4–20 with CTR below the site's median for that position, sent to title and snippet work (SEO-15, SEO-61); the pages and queries losing the most clicks against the previous period; each search type (Web, Image, Video, News) plus Discover; search appearance filters. The Core Web Vitals and HTTPS reports show no Poor or non-HTTPS URLs (PRF-01, SEC-01). | GSC Performance; Core Web Vitals; HTTPS |
| MSR-37 | SHOULD | Quarterly Links report: every key page appears among internally linked pages, with link counts that reflect its importance (SEO-22, SEO-23); top linking sites and anchor texts are reviewed with SEO-28. Associations are in place: GA4 (MSR-05), Merchant Center for shops, Google Ads where used. | GSC Links; Settings → Associations |

## Analytics (GA4)

| ID | Level | Rule | Verify |
|---|---|---|---|
| MSR-06 | MUST | A measurement plan exists before implementation: business goals → KPIs → key events → parameters ([`project-brief.md`](../templates/project-brief.md)). | Brief |
| MSR-07 | MUST | If GA4 is used: setup with data retention 14 months, internal and developer traffic filtered, unwanted referrals excluded, cross-domain measurement where needed, correct time zone and currency. | GA4 Admin |
| MSR-08 | MUST | Every primary conversion (successful form submit, purchase, sign-up, call click) is a key event and has been tested in DebugView. | GA4 DebugView; Realtime |
| MSR-09 | SHOULD | Enhanced measurement is reviewed: keep page views, scrolls, outbound clicks, downloads and site search. Turn off form interactions if they misfire, and replace them with custom events. | DebugView |
| MSR-10 | SHOULD | Events and parameters follow a documented naming convention (`snake_case`, `verb_object`). | Event list vs. plan |
| MSR-11 | SHOULD | E-commerce uses the recommended GA4 events (`view_item` → `purchase`) with a unique `transaction_id`. | DebugView; e-commerce report |
| MSR-12 | COULD | BigQuery export is on for raw-data ownership and history beyond the retention limit. | GA4 → BigQuery links |
| MSR-13 | SHOULD | Without Google Ads, privacy-friendly analytics (EU-hosted or self-hosted, cookieless) is considered. The consent requirement is assessed legally (PRV-07). | Decision record |
| MSR-29 | SHOULD | Search Console is the source of truth for search performance, GA4 for on-site behavior. The organic dashboard pairs GSC clicks with GA4 sessions (source `google`, medium `organic`) under identical country and device filters and compares trend shape, not totals (GSC uses Pacific Time, counts canonical URLs only and ignores consent; GA4 depends on its tag and opt-outs). | Looker Studio or GA4 vs. GSC |

## Tag management

| ID | Level | Rule | Verify |
|---|---|---|---|
| MSR-14 | MUST | If marketing or Google tags are used: all tags run through one tag manager container owned by the site owner. No duplicate hard-coded tags. | Tag Assistant; source |
| MSR-15 | MUST | Every tag has consent settings. Basic Consent Mode (tags load after consent) is the default; advanced mode needs a documented legal assessment. A test shows no Google request that sets or reads cookies before consent (PRV-03). | Tag Assistant; network before consent |
| MSR-16 | SHOULD | Use one workspace per change and named versions with notes. Test in preview before publishing. At most 3 people can publish. | GTM versions |
| MSR-17 | SHOULD | A UTM convention (lowercase, fixed vocabulary for `utm_source`, `utm_medium`, `utm_campaign`) is used for all campaigns, never on internal links. | Acquisition report: no "(other)" spikes |
| MSR-18 | COULD | Server-side tagging on a first-party subdomain controls what data reaches vendors. | Server container |
| MSR-19 | SHOULD | Ads conversions are imported from GA4 key events, or use the Ads tag with enhanced conversions. Both are consent-gated. | Google Ads → Conversions |
| MSR-20 | MUST | [house] E-commerce: Merchant Center gets its product feed by file, a platform integration or the Merchant API, never the sunset Content API for Shopping. Feed, on-page `Product` markup and the visible page agree on price, currency, availability and condition. Free listings are opted in, and Merchant Center updates price and availability automatically from the website when they differ. | Merchant Center diagnostics |

## Monitoring

| ID | Level | Rule | Verify |
|---|---|---|---|
| MSR-21 | MUST | Uptime monitoring runs every ≤ 5 minutes with a keyword check on the home page and one key page. Alerts go to ≥ 2 people or channels. | Monitor config; test alert |
| MSR-22 | MUST | Expiry alerts at least 30 days ahead for TLS certificates, domain registration and the `security.txt` `Expires` date. | Monitor config |
| MSR-23 | SHOULD | JavaScript and server errors are tracked with alerting. Source maps are uploaded privately. | Error tracker |
| MSR-24 | SHOULD | Real-user Core Web Vitals per template (PRF-05) and rankings for the core keyword set (from `url-map.csv`) are tracked weekly, by device and market. Rank data comes from Search Console or a licensed provider, never from automated queries to Google. | RUM; rank tracker |
| MSR-25 | SHOULD | One KPI dashboard is reviewed monthly. It covers sessions by channel, key events, conversion rate, organic clicks and impressions, Core Web Vitals and AI visibility. | Dashboard |
| MSR-30 | SHOULD | Traffic-drop triage order: check Search Console Data anomalies and Google's ranking-updates list; view the last 16 months (seasonality); split by search type, device and country; stable impressions with fewer clicks means a title or snippet problem; compare the query in Google Trends. After a core update, wait a full week after rollout ends and compare with the week before it began. Leave pages that lost only a few positions (2 to 4) unchanged. | GSC Performance; Search Status Dashboard |

## Sources

- [Search Console: Add a property](https://support.google.com/webmasters/answer/34592) · [Users and permissions](https://support.google.com/webmasters/answer/7687615) · [Sitemaps report](https://support.google.com/webmasters/answer/7451001) · [robots.txt report](https://support.google.com/webmasters/answer/6062598) · [Page indexing report](https://support.google.com/webmasters/answer/7440203) · [URL Inspection](https://support.google.com/webmasters/answer/9012289) · [Manual actions](https://support.google.com/webmasters/answer/9044175) · [Security issues](https://support.google.com/webmasters/answer/9044101) · [Performance report](https://support.google.com/webmasters/answer/7576553) · [Links report](https://support.google.com/webmasters/answer/9049606)
- [Google: Sitemaps ping endpoint is going away (2023)](https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping)
- [Request indexing](https://support.google.com/webmasters/answer/9012289) · [API limits](https://developers.google.com/webmaster-tools/limits)
- [GA4: Key events](https://support.google.com/analytics/answer/13965727) · [Enhanced measurement](https://support.google.com/analytics/answer/9216061) · [Data retention](https://support.google.com/analytics/answer/7667196)
- [GA4: Recommended e-commerce events](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [Tag Manager: Server-side tagging](https://developers.google.com/tag-platform/tag-manager/server-side/intro) · [Consent mode](https://developers.google.com/tag-platform/security/guides/consent)
- [Google: Debugging traffic drops](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) · [Search Console and Analytics](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console) · [Core updates](https://developers.google.com/search/docs/appearance/core-updates) · [Spam policies (machine-generated traffic)](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google: Share product data](https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google) · [Prevent malware (message forwarding)](https://developers.google.com/search/docs/monitor-debug/security/prevent-malware)
- [Merchant API](https://developers.google.com/merchant/api/overview) · [Content API sunset](https://developers.google.com/shopping-content/guides/deprecation-and-sunset)
- [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)
