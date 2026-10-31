# 05 · SEO

**Why it matters:** SEO makes sure search engines can crawl, understand and rank your pages. Most of it is technical hygiene done once, plus one clear purpose per page. Guide: steps 23–25.

Detail: `reference/google-search/` notes.

Scope: crawling, indexing, on-page, media, structured data, internal links, off-page, local, spam policies, migrations. AI search: [`06-geo-aeo.md`](06-geo-aeo.md). Multilingual: [`12-i18n.md`](12-i18n.md).

Last verified: 2026-10

## Crawling & indexing

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-01 | MUST | Every indexable URL returns `200`, is not blocked by robots.txt and has its content in the initial HTML response. Key information is real text in the DOM, not only in images, video, canvas or CSS `content`. | Crawler; GSC URL Inspection |
| SEO-02 | MUST | Exclude pages from the index with `noindex` (meta tag or `X-Robots-Tag`) on a crawlable URL: `noindex` plus `Disallow` cancels itself, and `noindex` is read only after a recrawl. Files (PDF, images, video) use `X-Robots-Tag`. Never use robots.txt to deindex. Exception: pages made for direct sharing or utility, not search, may be disallowed by default (linked URLs can still be indexed). | Crawler: indexability report; `curl -I` |
| SEO-03 | MUST | `/robots.txt` controls crawling only with `user-agent`, `allow`, `disallow`, `sitemap` (Google ignores other lines; ⚗ GEO-16 lines are optional extras). It lists the sitemap as an absolute URL, stays under 500 KiB, and never blocks CSS, JS, images or APIs needed to render a page (blocking small, frequently requested non-rendering assets is allowed). It blocks state-changing URLs (cart, account, comment post) and internal search results. `*` does not match AdsBot; name it explicitly. Template: [`robots.txt`](../templates/robots.txt). | GSC robots.txt report; URL Inspection |
| SEO-38 | MUST | Every host that serves pages (each subdomain, protocol and port) has its own `/robots.txt` at its root. It returns `200`; a 4xx counts as "no rules", while a `5xx` or timeout halts crawling of the host for up to 12 h. It is never used to hide private content (use authentication). | `curl -I` per host; GSC robots.txt report |
| SEO-04 | MUST | Production carries no leftover `noindex`, `Disallow: /` or password protection from staging. | `curl -I` + view source on live URLs |
| SEO-05 | MUST | One canonical host: HTTPS plus either `www` or apex. Every other variant answers with a single 301 to it. | `curl -I` on http/https × www/apex |
| SEO-06 | MUST | Every indexable page has an absolute, self-referencing `rel=canonical`, in HTML or HTTP header but not both. Duplicates point to the preferred URL. | Crawler: canonical report |
| SEO-41 | MUST | Canonical signals agree: `rel=canonical`, sitemap, internal links, redirects and hreflang all name the same HTTPS URL, and internal links skip parameter and duplicate variants. The certificate matches the host, with no insecure sub-resources (except images) and no HTTPS→HTTP redirects. Canonicals are never steered with robots.txt, `noindex` or the Removals tool. | Crawler; URL Inspection: Google-selected vs. declared canonical |
| SEO-07 | MUST | The XML sitemap (UTF-8, absolute URLs, at the site root) lists only canonical, indexable `200` URLs. `lastmod` changes only on significant edits, never for copyright-year or template changes. No `priority` or `changefreq` (Google ignores them). Max 50,000 URLs or 50 MB per file; use a sitemap index above that. | Crawler sitemap audit; GSC Sitemaps |
| SEO-08 | MUST | Missing content returns `404`/`410`, or a 301 to a true equivalent. No soft 404s: no `200` that serves an error page or the home page. Empty search, filter and category results return `404` or `noindex`. Client-routed apps send error routes to a URL the server answers with `404`, or add `noindex` via JS. | GSC Page indexing → "Soft 404"; crawler |
| SEO-09 | MUST | Permanent moves use server-side 301/308: one hop, no loops (legacy chains at most 3 hops). Genuinely temporary redirects (outage notice, A/B test) use 302/307 so Google keeps the original URL. JavaScript or meta-refresh redirects only where server-side is impossible. Internal links point to final URLs. | Crawler: redirect chains |
| SEO-10 | MUST | Primary content, links, canonical and robots meta are in the server-rendered or prerendered HTML. JavaScript may add a canonical only if it equals the HTML one (or the HTML has none; exactly one tag) and may add `noindex` to error pages. A `noindex` in the source HTML is never removed by JS (rendering may be skipped), so never ship it on pages meant to be indexed. | URL Inspection → rendered HTML vs. source |
| SEO-11 | MUST | Navigation uses crawlable `<a href>` links with real URLs. No `#!`, `javascript:` hrefs, `onclick`-only, `routerLink`-only or form-based navigation, and no `#` fragments for routing or content states (History API paths instead). | Crawler with JS disabled |
| SEO-12 | SHOULD | URLs are lowercase, hyphenated, descriptive (words, not opaque IDs) and use one trailing-slash form. Parameters are `?key=value&key2=value2` (multiple values comma-separated). Internal links carry no session or tracking parameters, are root-relative or absolute (never `../`) and percent-encode non-ASCII characters. | Crawler |
| SEO-13 | SHOULD | Facet, filter and sort URLs not meant to rank are disallowed in robots.txt (or use `#` fragments); canonical and `nofollow` only reduce crawling slowly. Facets meant to rank are crawlable, use `&` parameters or fixed-order path segments, and return `404` for empty combinations. Never use `noindex` to steer canonicals. No infinite crawl spaces (`nofollow` endless calendar pages). | Crawler: parameter URLs; GSC Crawl stats |
| SEO-14 | SHOULD | Paginated lists use linked pages (`?page=2`), each self-canonical, never all canonical to page 1. Multi-part articles never canonicalize to part 1. Infinite scroll and "load more" have crawlable paginated URLs behind them (absolute page numbers, History API updates). | Crawler |
| SEO-39 | MUST | The mobile version carries the same primary content, headings, title, meta description, structured data, image alt text, robots meta and crawlable links as desktop. | URL Inspection (smartphone) vs. desktop crawl |
| SEO-40 | MUST | Content loads when it enters the viewport (`loading="lazy"`, IntersectionObserver), never on click, swipe, typing or scroll events. The rendered HTML shows `src` on lazy `<img>` and `<video>`. | URL Inspection → rendered HTML |
| SEO-42 | SHOULD | Removing a page for good: `404`/`410`, authentication or `noindex`. The Removals tool lasts about 6 months. Cover every URL variant (case, parameters). | GSC Removals; crawler |
| SEO-43 | SHOULD | Snippet controls: `max-snippet`, `max-image-preview:large`, `nosnippet`, `data-nosnippet` (valid closed `span`/`div`/`section`, not toggled by JS), `unavailable_after` for expiring pages. The most restrictive directive wins. Google's meta names are `robots`, `googlebot` and `googlebot-news`. Audit for stray robots meta from plugins (honored even in `<body>`). | Crawler: robots directives; URL Inspection |

## On-page

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-15 | MUST | Each page has a unique, descriptive `<title>`: topic first, brand last, concise (about 50–60 visible characters is a house heuristic; Google sets no limit and truncates to device width). Title and visible `<h1>` agree, match the page's language and script, and are not half-empty (separator plus brand only). Paginated sequences may share titles. | Crawler: duplicate/missing titles |
| SEO-16 | MUST | Each indexable page has a unique meta description that summarizes the page (about 120–160 characters is a house heuristic; Google sets no limit). Generate from page data if needed; keyword lists are less likely to be shown. Home and aggregation pages get site-level text; paginated sequences may share one. | Crawler |
| SEO-17 | SHOULD | One `<h1>` matching the page topic. Google ignores heading count and order; this is house style and accessibility (A11Y-04). | Crawler |
| SEO-18 | SHOULD | The page's primary query (from `url-map.csv`) shows up naturally in the title, H1, slug and first paragraph. No keyword stuffing. | Manual review against `url-map.csv` |
| SEO-19 | SHOULD | Shareable pages carry Open Graph tags (`og:title`, `og:description`, `og:url`, `og:type`, `og:image` with `og:image:alt`) and `max-image-preview:large` in the robots meta. The image is relevant (no logo or text-heavy graphic), at least 1200 px wide and over 300,000 pixels, 16:9 (1200×675) where Discover matters; 1200×630 meets width and pixel count only. Template: [`head.html`](../templates/head.html). | Social preview debuggers; URL Inspection |
| SEO-20 | SHOULD | Images meant to rank are `<img>` elements (not CSS backgrounds) with descriptive file names, informative alt text in page context (no keyword stuffing) and surrounding context. `<picture>`/`srcset` has an `<img src alt>` fallback. Each image keeps one URL on every page and is not blocked by robots.txt (CDN hosts too). | Crawler: image report |
| SEO-44 | SHOULD | The home page carries one `WebSite` node with `name`, `url` and optional `alternateName` (acronym first, lowercase domain last), matching `og:site_name`, `<title>` and H1; duplicate home pages carry the same markup. Site names work per domain or subdomain, never per subdirectory. | Schema Markup Validator; URL Inspection |

## Media

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-45 | SHOULD | Videos meant to rank have one watch page per video (the video is the main content) with a unique title and description. The `<video>`, `<iframe>`, `<embed>` or `<object>` is in the rendered HTML without user action, with `VideoObject` (`name`, `thumbnailUrl`, `uploadDate` with timezone, `contentUrl` or `embedUrl`), one stable crawlable thumbnail URL, and a video file not blocked by robots.txt or `noindex`. | URL Inspection → rendered HTML; GSC Video indexing |

## Structured data

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-21 | MUST | Structured data describes content visible on the page (identifiers such as `@id` and `sameAs` may be non-visible) and passes with zero errors. JSON-LD is recommended; Microdata and RDFa are equally valid. Use only supported features: FAQ (deprecated 2026-05-07), HowTo (2023), practice problems, course info, estimated salary, learning video, special announcement, vehicle listing, sitelinks search box, home activity, critic review and job training no longer produce rich results; `ClaimReview` is being phased out; `Dataset` feeds only Dataset Search. No `data-vocabulary.org`. Templates: [`schema/`](../templates/schema/). | Schema Markup Validator; Rich Results Test on the live URL; URL Inspection |
| SEO-46 | MUST | Markup sits on crawlable, indexable pages (not blocked, `noindex` or behind login) and includes every required property of the feature with the most specific type. Image URLs are crawlable, indexable and show the marked-up item. Duplicate pages carry the same markup as the canonical. | URL Inspection; GSC Rich result status |
| SEO-47 | MUST | `Review`/`AggregateRating` markup covers one specific item and the reviews shown on the page, from real users: no fake, undisclosed incentivized or other-site ratings. Pages marked up as `LocalBusiness`/`Organization` carry no reviews about themselves (own markup or third-party widget). Author is a real name under 100 characters. | Rich Results Test; GSC Manual actions |
| SEO-48 | MUST | *(shops)* Product pages carry `Product` + `Offer` (not `AggregateOffer`) with `name`, `image`, `price` > 0 and `priceCurrency`, in the server-rendered HTML. Only single-product pages (never category pages), one currency per URL, one `availability` and one `itemCondition` value. Price, currency and availability equal the visible page and the feed (MSR-20). Template: [`product.jsonld`](../templates/schema/product.jsonld). | Rich Results Test; GSC Merchant listings |
| SEO-49 | SHOULD | *(variants)* Each variant has its own URL that preselects it (path or `?color=green`) and unique `sku`/GTIN. Mark up with `ProductGroup` (`productGroupID`, `variesBy`, `hasVariant`). With optional parameters, the URL without the parameter is canonical. | URL Inspection; GSC Merchant listings |
| SEO-50 | SHOULD | *(shops)* The standard shipping and return policy is marked up once, on one policy page, under `Organization` (`OnlineStore`: `hasShippingService`, `hasMerchantReturnPolicy`); product offers reference it by `@id`. Offer-level policy only overrides it and wins over it. Markup, Merchant Center and visible text agree (PRV-12). `priceValidUntil` is never in the past. In [`product.jsonld`](../templates/schema/product.jsonld) the `OnlineStore` node belongs on the policy page only. | Rich Results Test; Merchant Center |
| SEO-51 | MUST | *(job pages)* `JobPosting` sits only on the leaf page of exactly one open job, never on lists. Expired jobs get `validThrough` in the past, `404`/`410` or no markup (else manual action). The full description is visible without login, with an application route. | Rich Results Test; GSC Manual actions |
| SEO-52 | MUST | *(paywalls)* Googlebot sees the same full content a subscriber sees. Gated content is marked with `isAccessibleForFree: false` and `hasPart` (`WebPageElement` with a `.class` `cssSelector`) so it is not cloaking (SEO-33). Content that must stay private is not sent to the browser. | URL Inspection; Rich Results Test |
| SEO-53 | SHOULD | `QAPage` only on a page focused on one question that users can answer (never site-written FAQs or multi-question pages). `DiscussionForumPosting` only for genuine user posts. `Recipe`, `Event` and `JobPosting` only on leaf pages. | Rich Results Test |
| SEO-54 | SHOULD | Article markup lists every visible author as its own `author` (`Person`/`Organization` with `url` or `sameAs`, `name` holding only the name), `datePublished`/`dateModified` in ISO 8601 with timezone equal to the visible dates (CON-06), a concise `headline` and several crawlable images (≥ 50,000 px each; 16×9, 4×3, 1×1). Template: [`article.jsonld`](../templates/schema/article.jsonld). | Schema Markup Validator |

## Internal linking

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-22 | MUST | No orphan pages: every indexable URL is linked from at least one other indexable page. | Crawler vs. sitemap comparison |
| SEO-23 | SHOULD | Key pages are ≤ 3 clicks from the home page. Pillar pages link to every cluster page, and each cluster page links back. | Crawler: crawl depth |
| SEO-24 | SHOULD | Body copy links related pages in context, with descriptive anchors that name the target (no "click here", no empty anchors). Image links have alt text that describes the target. | Crawler: inlinks/anchor report |
| SEO-25 | MUST | Zero broken internal links (4xx/5xx). | Crawler; link checker in CI |

## Off-page

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-26 | SHOULD | Earn links with linkable assets (original data, tools, in-depth guides) and digital PR. Ask for links from unlinked brand mentions. | Backlink tool: new referring domains |
| SEO-27 | MUST | No link schemes: no bought, exchanged or network links. Paid links use `rel="sponsored"`, user-generated links `rel="ugc"`, other untrusted targets `nofollow`; normal source citations stay followed. | Backlink audit |
| SEO-28 | COULD | Review the backlink profile every quarter. Disavow only after a manual action or clear negative SEO. | GSC Manual actions; backlink tool |
| SEO-55 | SHOULD | *(UGC)* Sites with comments, profiles, forums or uploads put `rel="ugc"` on user links, `noindex` content from new users until they earn reputation, publish an abuse report function, verify sign-ups (TEC-18) and review public areas for spam. Pages made for sharing, not search, default to `noindex`. | Crawler; GSC Performance spikes |

## Local (sites with a location or service area)

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-29 | MUST | Google Business Profile is verified and uses the real-world business name (no keywords) and the fewest, most specific categories. Service-area businesses hide their address. | GBP dashboard |
| SEO-30 | MUST | Name, address and phone (NAP) are identical on the site, the Business Profile and major directories. | Citation audit |
| SEO-31 | SHOULD | Each real location has one page with unique content (team, directions, photos, reviews) and `LocalBusiness` markup. No near-identical city pages (doorways). | Manual review; [`local-business.jsonld`](../templates/schema/local-business.jsonld) |
| SEO-32 | SHOULD | Ask every customer for a review and answer all reviews within 7 days. No review gating, no incentives. | GBP reviews |
| SEO-56 | SHOULD | `LocalBusiness` markup uses the most specific subtype with `name` and `address`, one block per location with its own `url`, `geo` with ≥ 5 decimals, `telephone` with country code, and opening hours equal to the Business Profile. | Rich Results Test |

## Spam policies

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-33 | MUST | Comply with all Google spam policies: no cloaking, doorways, expired-domain abuse, hacked content, hidden text or links, keyword stuffing, link spam, automated queries to Google, malware or back-button hijacking, misleading functionality, scaled content abuse (including one page per query variation), scraping, site reputation abuse, sneaky redirects, thin affiliation, user-generated spam, scams, or circumventing a penalty with new sites. | Manual review; GSC Manual actions |
| SEO-57 | MUST | Third-party content (sponsored, partner, freelancer, white-label) is integrated into the site: site design, a named author or responsible editor, commercial disclosure, linked from navigation, not copied from other sites. Affiliate pages add original value (own reviews or tests, prices, comparisons), never merchant text copies. | Editorial review |

## Migration & relaunch

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEO-34 | MUST | Before a relaunch, inventory every URL that has traffic, links or rankings, including images, videos, PDFs, JS and CSS (GSC, analytics, crawl, backlinks), in [`url-map.csv`](../templates/url-map.csv). | Inventory complete vs. GSC export |
| SEO-35 | MUST | Map every old URL 1:1 to its most relevant new URL with a 301 (ideally one hop, at most 3). Use `404`/`410` only when no equivalent exists, and for merged or removed content. Never bulk-redirect to the home page. | Crawl of old URL list after launch |
| SEO-36 | MUST | Migrated pages keep their content, title, internal links and structured data, unless a change is an intended improvement. Each new URL has a self-referencing canonical, rewritten hreflang and sitemap entries and updated internal links. Migration `noindex` and robots blocks are removed at launch. Change one thing at a time (domain, CMS, layout), at a traffic low. | Diff of old vs. new crawl |
| SEO-37 | SHOULD | On a domain or subdomain move, use GSC "Change of address" for every verified old variant (apex, `www`, subdomains; not for HTTP→HTTPS or path moves) and keep redirects for at least a year. Update external links, profiles and ad landing pages. Check 404s and indexing weekly for 8 weeks; expect weeks of fluctuation. | GSC; server 404 log |

## Sources

- [Google Search Essentials](https://developers.google.com/search/docs/essentials) · [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt) · [Create robots.txt](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt) · [robots.txt spec](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec) · [Robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) · [Block indexing](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- [Canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) · [Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) · [Redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects) · [URL structure](https://developers.google.com/search/docs/crawling-indexing/url-structure) · [Remove information](https://developers.google.com/search/docs/crawling-indexing/remove-information)
- [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) · [Fix lazy-loaded content](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading) · [Crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) · [Mobile-first indexing](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
- [Faceted navigation](https://developers.google.com/crawling/docs/faceted-navigation) · [Pagination](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading) · [E-commerce URL structure](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites) · [Prevent abuse](https://developers.google.com/search/docs/monitor-debug/prevent-abuse)
- [Title links](https://developers.google.com/search/docs/appearance/title-link) · [Snippets](https://developers.google.com/search/docs/appearance/snippet) · [Site names](https://developers.google.com/search/docs/appearance/site-names) · [Discover](https://developers.google.com/search/docs/appearance/google-discover) · [Images](https://developers.google.com/search/docs/appearance/google-images) · [Video](https://developers.google.com/search/docs/appearance/video)
- [Structured data gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) · [Intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) · [General guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) · [Article](https://developers.google.com/search/docs/appearance/structured-data/article) · [Review snippet](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) · [Q&A page](https://developers.google.com/search/docs/appearance/structured-data/qapage)
- [Merchant listing](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) · [Product variants](https://developers.google.com/search/docs/appearance/structured-data/product-variants) · [Return policy](https://developers.google.com/search/docs/appearance/structured-data/return-policy) · [Shipping policy](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy)
- [Job posting](https://developers.google.com/search/docs/appearance/structured-data/job-posting) · [Paywalled content](https://developers.google.com/search/docs/appearance/structured-data/paywalled-content) · [Local business](https://developers.google.com/search/docs/appearance/structured-data/local-business) · [Search updates](https://developers.google.com/search/updates)
- [Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)
- [Google Business Profile guidelines](https://support.google.com/business/answer/3038177)
