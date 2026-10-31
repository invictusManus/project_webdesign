# 05 · SEO

**Why it matters:** SEO makes sure search engines can crawl, understand and rank your pages. Most of it is technical hygiene done once, plus one clear purpose per page. Guide: steps 23–25.

Scope: crawling, indexing, on-page, internal links, off-page, local, spam policies, migrations. AI search: [`06-geo-aeo.md`](06-geo-aeo.md). Multilingual: [`12-i18n.md`](12-i18n.md).

Last verified: 2026-10

## Crawling & indexing

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-01 | MUST | Every indexable URL returns `200`, is not blocked by robots.txt and has its content in the initial HTML response. | Crawler; GSC URL Inspection |
| SEO-02 | MUST | Exclude pages from the index with `noindex` (meta tag or `X-Robots-Tag`) on a crawlable URL. Never use robots.txt for this. | Crawler: indexability report |
| SEO-03 | MUST | `/robots.txt` controls crawling only with `user-agent`, `allow`, `disallow`, `sitemap` (Google ignores other lines; ⚗ GEO-16 lines are optional extras). It lists the sitemap, stays under 500 KiB and never blocks CSS/JS needed for rendering. Template: [`robots.txt`](../templates/robots.txt). | GSC robots.txt report |
| SEO-04 | MUST | Production carries no leftover `noindex`, `Disallow: /` or password protection from staging. | `curl -I` + view source on live URLs |
| SEO-05 | MUST | One canonical host: HTTPS plus either `www` or apex. Every other variant answers with a single 301 to it. | `curl -I` on http/https × www/apex |
| SEO-06 | MUST | Every indexable page has an absolute, self-referencing `rel=canonical`, in HTML or HTTP header but not both. Duplicates point to the preferred URL. | Crawler: canonical report |
| SEO-07 | MUST | The XML sitemap lists only canonical, indexable `200` URLs. `lastmod` changes only on significant edits. No `priority` or `changefreq` (Google ignores them). Max 50,000 URLs or 50 MB per file; use a sitemap index above that. | Crawler sitemap audit; GSC Sitemaps |
| SEO-08 | MUST | Missing content returns `404`/`410`, or a 301 to a true equivalent. No soft 404s: no `200` that serves an error page or the home page. | GSC Page indexing → "Soft 404"; crawler |
| SEO-09 | MUST | Redirects are server-side 301/308, one hop, no loops. Internal links point to final URLs. | Crawler: redirect chains |
| SEO-10 | MUST | Primary content, links, canonical and robots meta come from server-rendered or prerendered HTML. JavaScript does not change canonical or robots directives. | URL Inspection → rendered HTML vs. source |
| SEO-11 | MUST | Navigation uses crawlable `<a href>` links with real URLs. No `#!`, `onclick`-only or form-based navigation. | Crawler with JS disabled |
| SEO-12 | SHOULD | URLs are lowercase and hyphenated, have a consistent trailing slash and carry no session or tracking parameters in internal links. | Crawler |
| SEO-13 | SHOULD | Decide how each filter/sort parameter is handled (canonical to base, `noindex`, or not linked). Never create infinite crawl spaces. | Crawler: parameter URLs; GSC Crawl stats |
| SEO-14 | SHOULD | Paginated lists use linked pages (`?page=2`), each self-canonical. Never canonicalize every page to page 1. | Crawler |

## On-page

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-15 | MUST | Each page has a unique, descriptive `<title>`: topic first, brand last, about 50–60 characters visible. | Crawler: duplicate/missing titles |
| SEO-16 | MUST | Each indexable page has a unique meta description of about 120–160 characters that summarizes the page. | Crawler |
| SEO-17 | MUST | Exactly one `<h1>`, matching the page topic. | Crawler |
| SEO-18 | SHOULD | The page's primary query (from `url-map.csv`) shows up naturally in the title, H1, slug and first paragraph. No keyword stuffing. | Manual review against `url-map.csv` |
| SEO-19 | SHOULD | Shareable pages carry Open Graph tags (`og:title`, `og:description`, `og:url`, `og:type`, `og:image` 1200×630 with `og:image:alt`). Template: [`head.html`](../templates/head.html). | Social preview debuggers |
| SEO-20 | SHOULD | Images meant to rank are `<img>` elements (not CSS backgrounds), with descriptive file names and surrounding context. | Crawler: image report |
| SEO-21 | MUST | Structured data is JSON-LD, describes only content visible on the page and passes with zero errors. Only currently supported features are used: FAQ and HowTo no longer produce rich results. Templates: [`schema/`](../templates/schema/). | Rich Results Test; Schema Markup Validator |

## Internal linking

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-22 | MUST | No orphan pages: every indexable URL is linked from at least one other indexable page. | Crawler vs. sitemap comparison |
| SEO-23 | SHOULD | Key pages are ≤ 3 clicks from the home page. Pillar pages link to every cluster page, and each cluster page links back. | Crawler: crawl depth |
| SEO-24 | SHOULD | Body copy links related pages in context, with anchor text that names the target topic. | Crawler: inlinks/anchor report |
| SEO-25 | MUST | Zero broken internal links (4xx/5xx). | Crawler; link checker in CI |

## Off-page

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-26 | SHOULD | Earn links with linkable assets (original data, tools, in-depth guides) and digital PR. Ask for links from unlinked brand mentions. | Backlink tool: new referring domains |
| SEO-27 | MUST | No link schemes: no bought, exchanged or network links. Paid links use `rel="sponsored"`, user-generated links `rel="ugc"`. | Backlink audit |
| SEO-28 | COULD | Review the backlink profile every quarter. Disavow only after a manual action or clear negative SEO. | GSC Manual actions; backlink tool |

## Local (sites with a location or service area)

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-29 | MUST | Google Business Profile is verified and uses the real-world business name (no keywords) and the fewest, most specific categories. Service-area businesses hide their address. | GBP dashboard |
| SEO-30 | MUST | Name, address and phone (NAP) are identical on the site, the Business Profile and major directories. | Citation audit |
| SEO-31 | SHOULD | Each real location has one page with unique content (team, directions, photos, reviews) and `LocalBusiness` markup. No near-identical city pages (doorways). | Manual review; [`local-business.jsonld`](../templates/schema/local-business.jsonld) |
| SEO-32 | SHOULD | Ask every customer for a review and answer all reviews within 7 days. No review gating, no incentives. | GBP reviews |

## Spam policies

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-33 | MUST | Comply with Google's spam policies. In particular: no cloaking, doorways, hidden text, keyword stuffing, scaled content abuse, site reputation abuse, sneaky redirects or back-button hijacking. | Manual review; GSC Manual actions |

## Migration & relaunch

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-34 | MUST | Before a relaunch, inventory every URL that has traffic, links or rankings (GSC, analytics, crawl, backlinks) in [`url-map.csv`](../templates/url-map.csv). | Inventory complete vs. GSC export |
| SEO-35 | MUST | Map every old URL 1:1 to its most relevant new URL with a 301. Use `410` only when no equivalent exists. Never bulk-redirect to the home page. | Crawl of old URL list after launch |
| SEO-36 | MUST | Migrated pages keep their content, title, internal links and structured data, unless a change is an intended improvement. | Diff of old vs. new crawl |
| SEO-37 | SHOULD | On a domain move, use GSC "Change of address" and keep redirects for at least a year. Check 404s and indexing weekly for 8 weeks. | GSC; server 404 log |

## Sources

- [Google Search Essentials](https://developers.google.com/search/docs/essentials) · [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt) · [Robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [Canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) · [Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) · [Crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- [Title links](https://developers.google.com/search/docs/appearance/title-link) · [Snippets](https://developers.google.com/search/docs/appearance/snippet)
- [Structured data gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) · [Search updates](https://developers.google.com/search/updates)
- [Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)
- [Google Business Profile guidelines](https://support.google.com/business/answer/3038177)
