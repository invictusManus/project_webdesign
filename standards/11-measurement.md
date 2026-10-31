# 11 · Measurement & monitoring

Scope: Search Console, Bing Webmaster Tools, GA4, Google Tag Manager, conversion tracking, Merchant Center, uptime/error monitoring, dashboards. The legal side of consent is in [`10-security-privacy.md`](10-security-privacy.md); AI-visibility measurement is in [`06-geo-aeo.md`](06-geo-aeo.md); the recurring routine is in [`checklists/3-monitoring.md`](../checklists/3-monitoring.md).

Last verified: 2026-10

## Search Console & Bing

| ID | Level | Rule | Verify |
|---|---|---|---|
| MSR-01 | MUST | A Search Console **Domain property** is verified by DNS TXT before launch. At least two people are owners, one of them the site owner. | GSC → Settings → Users |
| MSR-02 | MUST | The XML sitemap is submitted in Search Console, and the Page indexing report shows no key URL excluded unexpectedly. | GSC Sitemaps; Page indexing |
| MSR-03 | MUST | On launch day, the home page and top money pages are checked with URL Inspection and indexing is requested for them. Everything else gets indexed through the sitemap and accurate `lastmod`. | GSC URL Inspection |
| MSR-04 | SHOULD | Bing Webmaster Tools is verified (import from Search Console) with the sitemap submitted. An IndexNow key is hosted, and new or changed URLs are submitted automatically. | Bing WMT; IndexNow response 200/202 |
| MSR-05 | SHOULD | Search Console and Bing email alerts are on. Search Console is linked to GA4. | Account settings |

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

## Tag management

| ID | Level | Rule | Verify |
|---|---|---|---|
| MSR-14 | MUST | If marketing or Google tags are used: all tags run through one tag manager container owned by the site owner. No duplicate hard-coded tags. | Tag Assistant; source |
| MSR-15 | MUST | Every tag has consent settings. Basic Consent Mode (tags load after consent) is the default; advanced mode needs a documented legal assessment. A test shows no Google request that sets or reads cookies before consent (PRV-03). | Tag Assistant; network before consent |
| MSR-16 | SHOULD | Use one workspace per change and named versions with notes. Test in preview before publishing. At most 3 people can publish. | GTM versions |
| MSR-17 | SHOULD | A UTM convention (lowercase, fixed vocabulary for `utm_source`, `utm_medium`, `utm_campaign`) is used for all campaigns, never on internal links. | Acquisition report: no "(other)" spikes |
| MSR-18 | COULD | Server-side tagging on a first-party subdomain controls what data reaches vendors. | Server container |
| MSR-19 | SHOULD | Ads conversions are imported from GA4 key events, or use the Ads tag with enhanced conversions. Both are consent-gated. | Google Ads → Conversions |
| MSR-20 | MUST | E-commerce: Merchant Center gets its product feed by file, a platform integration or the Merchant API, never the sunset Content API for Shopping. The feed matches the on-page Product data. | Merchant Center diagnostics |

## Monitoring

| ID | Level | Rule | Verify |
|---|---|---|---|
| MSR-21 | MUST | Uptime monitoring runs every ≤ 5 minutes with a keyword check on the home page and one key page. Alerts go to ≥ 2 people or channels. | Monitor config; test alert |
| MSR-22 | MUST | Expiry alerts at least 30 days ahead for TLS certificates, domain registration and the `security.txt` `Expires` date. | Monitor config |
| MSR-23 | SHOULD | JavaScript and server errors are tracked with alerting. Source maps are uploaded privately. | Error tracker |
| MSR-24 | SHOULD | Real-user Core Web Vitals per template (PRF-05) and rankings for the core keyword set (from `url-map.csv`) are tracked weekly, by device and market. | RUM; rank tracker |
| MSR-25 | SHOULD | One KPI dashboard is reviewed monthly. It covers sessions by channel, key events, conversion rate, organic clicks and impressions, Core Web Vitals and AI visibility. | Dashboard |

## Sources

- [Search Console: Add a property](https://support.google.com/webmasters/answer/34592) · [Request indexing](https://support.google.com/webmasters/answer/9012289) · [API limits](https://developers.google.com/webmaster-tools/limits)
- [GA4: Key events](https://support.google.com/analytics/answer/13965727) · [Enhanced measurement](https://support.google.com/analytics/answer/9216061) · [Data retention](https://support.google.com/analytics/answer/7667196)
- [GA4: Recommended e-commerce events](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [Tag Manager: Server-side tagging](https://developers.google.com/tag-platform/tag-manager/server-side/intro) · [Consent mode](https://developers.google.com/tag-platform/security/guides/consent)
- [Merchant API](https://developers.google.com/merchant/api/overview) · [Content API sunset](https://developers.google.com/shopping-content/guides/deprecation-and-sunset)
- [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)
