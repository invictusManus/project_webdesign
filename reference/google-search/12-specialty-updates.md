# Site-specific guides (ecommerce, international & multilingual, explicit content) and the Search Central documentation changelog: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Best practices for ecommerce sites in Google Search (overview)
https://developers.google.com/search/docs/specialty/ecommerce · Last updated: 2025-12-10

### Scope
- Guide set for developers building ecommerce sites that should work well with Google and follow SEO best practices.
- Also relevant to sites listing products sold only in physical stores.
- Sharing ecommerce data and site structure helps Google find and parse content and show it on Search and other Google surfaces.
- Pages in the set: where content can appear, share product data, structured data, launch a new site, write high-quality reviews, URL structure, site structure, pagination and incremental loading.

## Where ecommerce content can appear on Google
https://developers.google.com/search/docs/specialty/ecommerce/where-ecommerce-data-can-appear-on-google · Last updated: 2025-12-10

### Surfaces and what each needs
- Google Search: normal SEO plus supported structured data for varied result presentation. Actual appearance may differ from examples.
- Google Images: follow Google Image best practices.
- Google Lens: upload product details to Google Merchant Center, opt in to product listings, follow Image best practices.
- Google Shopping tab: upload products to Merchant Center.
- Business Profile: claim the profile and link Business Profile with Merchant Center.
- Google Maps: upload products with inventory location data to Merchant Center (see Local inventory ads onboarding).
- Several surfaces support multiple display formats; Search picks the presentation by query intent.

### Content types that reach customers at different journey stages
- Company story; special offers (seasonal events); merchant product reviews; customer ratings and reviews; catalog (product descriptions matching shopper search terms, plus category descriptions for broader queries); education (workshops, lessons; event structured data may apply); live streams; customer-service touchpoints (clear return and shipping policies including order-size shipping discounts, visible support contacts).
- Linking to third-party products for financial gain: follow the paid-links guidance.

## Share your product data with Google
https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google · Last updated: 2025-12-10

### Two recommended channels
- Product structured data on product pages (not required to appear in Search, but raises eligibility for Product rich results and improves understanding of price, discount, shipping cost; also helps Merchant Center verify feeds against the site).
- Product feed uploaded to Merchant Center (not mandatory for Search results, but mandatory for some surfaces such as the Shopping tab).
- To keep a page's content out of snippets use the `data-nosnippet` attribute on the HTML element; Google may extract data from pages by other methods too.

### Merchant Center delivery options
- Small, rarely updated sites: automated feed built from crawled content (structured data improves extraction accuracy); lowest effort.
- Large or fast-changing sites: periodic feed files, or the Content API for immediate updates (useful for stock levels).
- Feed benefits: confidence Google knows all products (crawling may miss some); control over update timing (weekly, daily, hourly; crawl timing is not guaranteed); share data absent from the site (e.g. store-level inventory).
> Note: the page still names the Content API as the immediate-update route; repo rule MSR-20 treats the Content API for Shopping as sunset.

### How structured data and Merchant Center data are used (varies by country, device, other factors)
- Product rich results in Search: Product structured data; Search may also use Merchant Center data.
- Google Images product annotations: Product structured data; images listed in Merchant Center.
- Shopping tab: Merchant Center participation required; structured data can help verification.
- Google Lens: image structured data properties where available; images listed in Merchant Center.

### Resolving update delay
- Site and feed can disagree (e.g. sold-out item): configure Merchant Center to automatically update its product data from site contents when price or availability discrepancies are noticed.

## Include structured data relevant to ecommerce
https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce · Last updated: 2025-12-10

### Guidance
- Structured data is a standardized machine-readable format that improves Google's understanding; Google supports many but not all schema.org types.
- With a CMS or ecommerce platform, prefer an integrated extension or plugin that emits the markup.
- Shoppers need more than product pages; mark up other page types too.

### Types particularly relevant
- `BreadcrumbList`: conveys page hierarchy; gives a meaningful breadcrumb trail in results.
- `LocalBusiness`: for physical stores (location, opening hours) on business information pages; also register with Google My Business, register store locations and store codes in Merchant Center, follow Merchant Center guidelines (e.g. return policies on the site).
- `Organization`: logo, contact info, business identifiers, return policies for the business as a whole.
- `Product` and `ProductGroup`: product details and variants; also see "Set up structured data for Merchant Center" for better participation in shopping experiences.
- `Review`: see Review snippet.
- `VideoObject`: pages primarily about one video (prerecorded or livestream), e.g. on a product page.

## How to launch a new ecommerce website
https://developers.google.com/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website · Last updated: 2025-12-10

### Registration steps
- Verify site ownership with Google.
- Ask Google to index: few URLs use the URL Inspection tool; many URLs provide a sitemap.
- Track indexing with the Page Indexing report. Merchant Center may cross-check content against the Search index; to avoid false verification warnings, make sure the site is indexed and products are purchasable.
- Physical store: establish business details with Google.
- Sign up for Merchant Center (required for the Shopping tab; may also unlock features such as a product badge on Google Images).

### Launch strategies
- Grand reveal: whole site inaccessible (password required blocks Google and permits testers) until launch, then follow the launch steps immediately. Pro: nothing known ahead of marketing. Con: slower visibility in Search and the Shopping tab.
- Home page launch: only a placeholder home page public. Verify ownership in advance, finish the steps when products are live. Pro: store name findable, domain awareness, early links. Con: product detail not in Search or Shopping until full launch.
- Launch without product availability: full site live, products marked out of stock; show the official launch date on each page. Send Merchant Center data with stock unavailable using the `excluded_destination` attribute so loading issues surface early without products appearing in Shopping. Pro: indexed at launch. Con: site looks live but orders are impossible; tell shoppers.
- Do not disable add-to-cart to stop purchases: Google may use add-to-cart to verify final price including tax and shipping.
- Soft launch: everything live as soon as production-ready, marketing launch later. Pro: simple, real-user testing at low traffic. Con: social media may draw attention early.

## Write high quality reviews
https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews · Last updated: 2025-12-10

### Practices (products, services, destinations, games, movies and similar)
- Evaluate from the user's perspective; show expertise; provide first-hand evidence (visuals, audio, links) of your own experience.
- Give quantitative measurements across performance categories; explain what sets the item apart from competitors; cover comparable alternatives and which suits which use.
- Discuss benefits and drawbacks from original research; describe evolution from previous models; focus on the key decision factors for the category; describe design choices and their effect on users beyond manufacturer claims.
- Link to other useful resources; consider linking multiple sellers.
- For "best overall" or "best for X" picks, state why with first-hand evidence. Ranked lists must stand alone even if separate in-depth reviews exist.
- Affiliate links in reviews: see Google's position on affiliate programs.
- Prioritize quality and originality over length.

## Designing a URL structure for ecommerce websites
https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites · Last updated: 2025-12-10

Applies if you control URL structure; platform users can mostly skip.

### Why it matters
- Fragment identifiers (`#fragment`) are not used in indexing, so `/product/t-shirt#black` and `#white` are one page and content can be missed.
- Different URLs returning the same page (`/product/black-t-shirt` vs `/product?sku=1234`) cause repeat fetching, slower crawling and server load.
- Continually changing values (timestamps, `/about?now=12:34am`) look like infinite pages.

### General recommendations
- Minimize alternative URLs for the same content.
- If the server treats case identically, normalize to one case.
- Every page in paginated results needs a unique URL (most URL mistakes occur in pagination).
- Use descriptive words in paths (`/product/black-t-shirt-with-a-white-collar`, not `/product/3243`).

### Query parameters
- Prefer `?key=value` over `?value` (`/photo-frames?page=2`, `/t-shirt?color=green`).
- Do not repeat a parameter (`?type=candy&type=sweet`); use `?type=candy,sweet`. Googlebot may ignore one value otherwise.
- Do not internally link temporary parameters: session IDs, tracking codes, user-relative values (`location=nearby`, `time=last-week`), current time. Use long-term persistent URLs (`/t-shirt?location=UK` is fine).

### Product variants
- Each variant needs its own URL: path segment (`/t-shirt/green`) or query parameter (`/t-shirt?color=green`).
- If variants use optional query parameters, use the URL without the parameter as canonical.
- Also see product variant structured data.

### URLs in content
- Use the same URL form in internal links, sitemaps and `<link rel="canonical">` (e.g. consistently include or omit `?page=1`).
- Self-referencing `rel="canonical"` on all indexable pages, and list those URLs in a sitemap.
- Variants with unique URLs: include the canonical product URL on all variant pages (relates to Merchant Center `canonical_link`).
- Use `<a href>` links; no JavaScript-only navigation (Googlebot may miss it).
- Meaningful link text (e.g. product title), not "click here".
- Avoid linking to or indexing pages without useful content: empty category gets robots `meta` `noindex`; if the site detects an emptied category and removes it from on-site search and browse, return `404`.
- Related guides: site structure, duplicate content, pagination, faceted navigation crawling.

## Help Google understand your ecommerce website structure
https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure · Last updated: 2025-12-10

### Crawler-friendly navigation
- Google infers page importance from links: number of links to a page and number of clicks needed to reach it.
- Link menus to categories, categories to subcategories, subcategories to all products. Structured data reinforces page purposes.
- If categories do not link to every product, Googlebot may miss products reachable only via the search box; Googlebot generally does not submit search boxes. Strongly recommended: link every product you want indexed. Where impossible, use a sitemap or Merchant Center feed.
- Use `<a href>`; not JavaScript events on other DOM elements.

### Promote best categories or products
- Google generally does not use URL structure to infer site structure; link analysis does.
- More internal links means higher relative importance; link a bestseller from the home page, blog posts, newsletters.
- Ultimate best practice: useful, interesting content for users.

## Pagination, incremental page loading, and their impact on Google Search
https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading · Last updated: 2025-12-10

### Why load partial results
- Applies to search results, category pages, blog or newsletter lists, product reviews, comments.
- Benefits: faster initial load, less network traffic (mobile), lower backend load, avoids resource-limit errors from huge lists.

### UX patterns
- Pagination: shows size and position; but more complex controls, content split across pages, new page loads.
- Load more: single page, can show total near the button; cannot handle very large result sets.
- Infinite scroll: single page, intuitive; scrolling fatigue, unclear size, cannot handle very large sets.

### How Google indexes them
- Google generally crawls URLs in `href` of `<a>`; crawlers do not click buttons or trigger user-action JavaScript.
- Load more and infinite scroll are usually JavaScript: follow JavaScript SEO practices (crawlable links) and consider a sitemap or Merchant Center feed to expose all products.

### Pagination best practices
- Link pages sequentially: each page links to the next with `<a href>`; consider linking every page back to the first page so Google treats it as the better landing page.
- Paginated pages may share titles and descriptions; Google recognizes sequences.
- Unique URL per page (e.g. `?page=n`); each page has its own canonical, not page one as canonical for all.
- No fragment identifiers for page numbers (Google ignores them; may not follow the link).
- Consider preload, preconnect or prefetch for next-page speed.
- `<link rel="next">` and `rel="prev"` are no longer used by Google (other engines may use them).
- Filters and alternate sort orders (`?order=price`): block from indexing with `noindex` robots `meta`, or discourage crawling of those patterns via robots.txt.

## Overview of international and multilingual site topics
https://developers.google.com/search/docs/specialty/international · Last updated: 2025-12-10

- Covers sites with multiple languages or location-specific content. Pages: managing multi-regional and multilingual sites; localized versions (hreflang); locale-adaptive page crawling.

## Managing multi-regional and multilingual sites
https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites · Last updated: 2025-12-10

### Definitions
- Multilingual: content in more than one language (Google tries to match the searcher's language).
- Multi-regional: explicitly targets users in different countries (Google tries to match the locale). A site can be both.

### Multilingual versions
- Use different URLs per language, not cookies or browser settings; add `hreflang`.
- Dynamic content switching or rerouting by language settings may not be fully crawled: Googlebot usually originates from the USA and sends requests without `Accept-Language`.
- Labeling methods: `hreflang` annotations and sitemaps.
- Page language is determined from visible content only; Google does not use code-level language information (`lang` attributes) or the URL. Keep one language for content and navigation per page; avoid side-by-side translations.
- Translating only boilerplate while the main content stays in one language (typical for user-generated content) creates duplicate-looking results with different boilerplate languages.
- Do not auto-redirect between language versions based on assumed language; offer hyperlinks to other language versions instead.
- Localized words in URLs or IDNs are fine; use UTF-8 and escape URLs correctly when linking.

### Geotargeting (single country and language)
- Can improve rankings in the target country at the expense of other locales.
- Page or site level: locale-specific URLs. Page level: `hreflang` or sitemaps.
- Geotargeting is inexact: give users who land on the wrong version links to choose region or language.
- Do not adapt content by IP analysis (unreliable; Google crawls mostly from the US and does not vary location to detect variants). Use `hreflang`, alternate URLs, explicit links.

### URL structure options
- Country-specific domain (`example.de`): clear geotargeting, server location irrelevant, easy site separation. Cons: expensive or limited availability, more infrastructure, sometimes strict ccTLD requirements, single country only.
- Subdomain on gTLD (`de.example.com`): easy setup, different server locations allowed, easy separation. Con: users may not recognize country vs language.
- Subdirectory on gTLD (`example.com/de/`): easy setup, low maintenance (same host). Cons: unclear country vs language, single server location, harder separation.
- URL parameters (`site.com?loc=de`): not recommended (hard segmentation, unclear to users).

### How Google determines target locale
- ccTLD (strong signal; some countries restrict registration; vanity ccTLDs such as `.tv` and `.me` treated as gTLDs).
- `hreflang` statements in tags, headers or sitemaps.
- Server location by IP (not definitive because of CDNs or foreign hosting).
- Other signals: local addresses and phone numbers, local language and currency, links from local sites, Business Profile signals.
- Google ignores locational `meta` tags (`geo.position`, `distribution`) and geotargeting HTML attributes.
- Google does not vary crawler location per site to discover variants.

### Duplicate pages
- Similar or duplicate same-language content on different URLs in a multi-regional site (`example.de/` and `example.com/de/`): pick a preferred version and use `rel="canonical"` plus `hreflang` so the right URL is served.

### gTLD treatment
- Any TLD not listed by ICANN as ccTLD is a gTLD (`.com`, `.org`, `.edu`, `.gov` and others). For a gTLD site targeting a location, set the country explicitly.
- Generic regional TLDs `.eu` and `.asia` are treated as gTLDs.
- ccTLDs treated as gTLDs (list may change): `.ad .ai .as .bz .cc .cd .co .dj .fm .io .la .me .ms .nu .sc .sr .su .tv .tk .ws`.

## Tell Google about localized versions of your page
https://developers.google.com/search/docs/specialty/international/localized-versions · Last updated: 2026-09-21

### When to annotate
- Recommended when: only the template is translated (UGC such as forums); small regional variations in one language (US, GB, IE English); full translation into several languages.
- Localized versions count as duplicates only if main content stays untranslated.
- Google may find alternates unaided, but explicit annotation is usually best.

### Methods
- Three equivalent methods: HTML `<link>` tags, HTTP `Link` header, XML sitemap. Using several gives no Search benefit and is harder to maintain; pick one.
- Google detects language by algorithm, not `hreflang` or `lang`.

### Guidelines for all methods
- Each version lists itself and all other versions; identical set on every version.
- Alternate URLs fully qualified with protocol (`https://example.com/foo`, not `//example.com/foo` or `/foo`); may be on different domains.
- With several locale-specific URLs for one language (`en-IE`, `en-CA`, `en-AU`), also give a generic language URL (`en`) for unspecified users; it can be one of the specific pages.
- Non-reciprocal annotations are ignored (prevents third parties claiming your pages).
- If full bidirectional sets are hard, some languages may be omitted per page; prioritize bidirectional links from new language pages to the originating or dominant language pages (e.g. link new `.mx` and `.es` to the strong `.fr` site before linking them to each other).
- Fallback for unmatched languages: `x-default`, e.g. `<link rel="alternate" href="https://example.com/" hreflang="x-default" />`, especially for language or country selectors and auto-redirecting home pages.
- Subdomain or folder names (`en-gb.example.com`) are not used to determine audience; map explicitly.

### HTML tags
- In a well-formed `<head>` (validate rendered HTML), one `<link rel="alternate" hreflang="lang_code" href="url_of_page" />` per variant including itself.
- Do not combine `hreflang` with other attributes such as `media` in one `<link>` tag.
- `lang_code`: supported language/region code or `x-default`.

### HTTP header
- Useful for non-HTML files (PDF). Format: `Link: <url1>; rel="alternate"; hreflang="code1", <url2>; rel="alternate"; hreflang="code2"`. Include every version, including the requested one; same header on every version; URLs in `<` `>`.

### Sitemap
- Declare `xmlns:xhtml="http://www.w3.org/1999/xhtml"`.
- One `<url>` per URL with `<loc>`, plus child `<xhtml:link rel="alternate" hreflang="..." href="..."/>` for every variant including itself (order irrelevant). Child elements do not count towards the sitemap URL limit.
- Sitemap must live in a directory covering the URLs (descendant URLs only); follow general sitemap guidelines.

### Supported codes
- Language ISO 639-1, optional region ISO 3166-1 Alpha 2 (`en-US`); case-insensitive, uppercase region by convention. Codes outside those standards (e.g. `es-419`) are unsupported.
- Region alone is invalid (`be` is Belarusian, not Belgium). Belgium: `de-BE`, `nl-BE`, `fr-BE`.
- Language alone allowed (`de`); `de-ES` means German for Spain.
- Script derived from region (`zh-TW` gives Traditional); explicit ISO 15924 script allowed: `zh-Hant`, `zh-Hans`, with optional region (`zh-Hans-US`).
- `x-default`: fallback when no other language or region matches; designed for language selector pages; no language code needed.

### Troubleshooting
- Missing return links (A to B requires B to A) cause annotations to be ignored or misread.
- Incorrect language codes (must identify language; region alone invalid).
- Incorrect region codes: reserved or unassigned codes (`EU`, `UN`, `UK`) are ignored by Google Search.
- Third-party debugging tools (not maintained by Google): Aleyda Solis hreflang generator, Merkle hreflang tag tester.

## How Google crawls locale-adaptive pages
https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages · Last updated: 2025-12-10

- Locale-adaptive pages (content varies by perceived country or language) may not be fully crawled, indexed or ranked: default Googlebot IPs appear US-based and requests carry no `Accept-Language`.
- Recommended instead: separate locale URLs annotated with `rel="alternate"` `hreflang`.

### Geo-distributed crawling
- Googlebot also crawls from IP addresses outside the USA.
- Treat Googlebot as a visitor from its apparent country: block it if you block that country's users, allow it if you allow them.
- Googlebot uses the same user agent string in all configurations; geo-distributed crawls can be verified with reverse DNS lookups.
- If using the robots exclusion protocol, apply identical rules in every locale (robots `meta` tags and robots.txt).

## Guidelines for sites with explicit content
https://developers.google.com/search/docs/specialty/explicit/guidelines · Last updated: 2026-09-17

### How Google handles explicit content
- Ranking weighs query intent, quality and relevance of explicit results; SafeSearch filters results.
- SafeSearch filters results leading to visual depictions of: explicit sexual content (including pornography), nudity, photo-realistic sex toys, sex-oriented dating or escort services, violence or gore, links to pages containing such content (including links, pop-ups, ads that display or point to it).
- Allows explicit content with educational, documentary, scientific or artistic (EDSA) value. Uses machine learning over text, images, video on the page and in links.
- With SafeSearch off or blur, query understanding still tries to avoid unwanted exposure.
- Regardless of setting, Google removes policy-violating pages (e.g. CSAM) and, on request, non-consensual explicit imagery and non-consensual explicit fake content.
- Removal-based demotion: all CSAM is removed and sites with a significant proportion of CSAM are demoted entirely; sites with significant volume of personal-information removals for non-consensual explicit imagery or fakes are demoted across all pages.

### Best practices
- Prevent user-generated harmful content: platforms with explicit content should use publisher verification and content moderation; use hash matching for known CSAM and classifiers for novel content.
- Allow Googlebot to fetch video content files. Otherwise Google cannot run automated protections; pages with unfetchable embedded video that look explicit may be demoted or filtered, possibly strongly in Search overall and especially in Video mode (ranking algorithms updated to affect such sites more strongly). Verify Googlebot requests if worried about exposure.
- Allow Googlebot to crawl without an age gate: verify Googlebot requests and serve content without the gate. Otherwise ranking suffers, image or video bytes may not be fetched, and non-explicit content behind the gate (or the whole site) is more likely auto-classified explicit and excluded under SafeSearch.
- Group explicit pages on a separate domain or subdomain (`explicit.example.com` vs `www.example.com`); the name need not contain "explicit". Without grouping, the whole site may be filtered.
- Optional metadata: `<meta name="rating" content="adult">` (meta tag or HTTP response header) on sexually explicit pages; `<meta name="rating" content="RTA-5042-1996-1400-1577-RTA">` is equivalent (one is enough). CMS users can use search-engine settings for head meta tags.
- Video sitemap: `<video:family_friendly>` set to `no`, only for explicit videos.
- Google Shopping: label adult products in Merchant Center feeds with the `adult` attribute or with `hasAdultConsideration` structured data; no effect on organic web search visibility.

## What to do if your site is incorrectly flagged as explicit
https://developers.google.com/search/docs/specialty/explicit/troubleshooting · Last updated: 2025-12-10

### Scope
- Nuanced content (lingerie, sex education, massage, racy content) may be wrongly filtered by SafeSearch.

### Diagnose
- Single page: SafeSearch Off, find page for a query, switch SafeSearch to Filter; if it disappears, filtering applies.
- Whole site: `site:` query with SafeSearch Filter; if the site disappears the whole site is filtered.
- Fix common mistakes, then request a review.
- Review timing: after fixes wait at least 2-3 months (classifier reprocessing); if the site always followed guidance, request immediately. Only clearly incorrect automatic categorization is overturned.

### Common mistakes
- Adult rating `meta` tag on non-explicit pages: SafeSearch filters every page carrying it regardless of content; remove it from non-explicit pages.
- `<video:family_friendly>` set to `no` too broadly: use `no` only for sexually explicit or graphically violent content.
- Unmoderated UGC comments or uploads: add anti-spam and moderation.
- Age gate blocking Googlebot: allow Googlebot to crawl without it, follow the mandatory interstitials guidelines, and confirm with the Live URL test in Search Console.
- Explicit and non-explicit pages not separated: group explicit pages on a separate domain or subdomain.

### Further troubleshooting
- Changes can take up to 2-3 months to be processed.
- Significant nudity or sexually explicit content (including computer-generated) or graphic violence can classify the whole site as explicit.
- Blurred explicit images: page may still be explicit if images can be unblurred or lead to unblurred images.
- Explicit pages are ineligible for some features (rich results, featured snippets, video previews) regardless of SafeSearch setting.

## Documentation changelog
https://developers.google.com/search/updates · Last updated: 2026-10-26

Dated list of substantive Search Central documentation changes, newest first. Feed: `https://developers.google.com/search/updates/search_docs_updates.rss`. Crawling-infrastructure docs have their own changelog since 2025-11-20 (`https://developers.google.com/crawling/docs/changelog/crawling_docs_updates.rss`). Entries before 2026 use month and day only on the source page; dates are reconstructed.

### 2026
- 2026-10-26: user-generated spam prevention guide: block indexing of link-shared content, monitor abuse in Search Console.
- 2026-10-23: crawlable URL structure: clarified word separation with hyphens vs underscores.
- 2026-10-21: "control what you share" page now lists robots `meta`, `data-nosnippet`, `X-Robots-Tag` and the Search generative AI control.
- 2026-10-16: Indexing API quota page updated to current limits; outdated form removed.
- 2026-10-08: new page, UGC Fresh Data Program (purpose, eligibility, how to join).
- 2026-10-01: generative AI content guide updated with Search Quality Raters guidelines information.
- 2026-09-24: `VideoObject`: added `creator` (`author` also supported); `interactionStatistic` supported interaction types documented.
- 2026-09-18: aggregator and supplier units support local business queries (region-specific experiences).
- 2026-09-16: new guide: add a Search profile badge to your website.
- 2026-09-08: new docs on regional differences in Search experience (aggregator units, supplier units, carousels in certain countries).
- 2026-08-31: European Search Dataset Licensing Program page refreshed (overview, eligibility, application).
- 2026-08-28: favicon docs list supported file formats explicitly (support unchanged; previously linked an evolving external reference).
- 2026-08-28: site reputation policy updated: enforcement approach adjusted within the EEA.
- 2026-08-20: preferred sources: instructions for a new custom interactive button that returns users to where they left off.
- 2026-07-29: new guide: analyzing social and video platform content performance in Search Console.
- 2026-07-24: review snippet: new guideline on fake and undisclosed incentivized reviews.
- 2026-07-14: package tracking early adopters program no longer accepts new partners.
- 2026-07-10: canonicalization troubleshooting: clarified re-evaluation time.
- 2026-07-07: merchant listing: `Product.category` accepts `Text` and `CategoryCode` (aligns with Merchant Center `product_type` and `google_product_category`).
- 2026-07-07: merchant listing: new "Sale duration" section: `validFrom`, `validThrough`, `priceValidUntil` on `Offer` or `PriceSpecification` (aligns with `sale_price_effective_date`).
- 2026-07-01: AMP docs simplified: AMP viewer, AMP Cache and signed exchange references removed; Search now links directly to publisher AMP host pages; AMP ranks like any page.
- 2026-06-17: site move guide: use Change of Address for all subdomain variants (www and non-www).
- 2026-06-15: AI optimization guide: `llms.txt` not needed for Search and neither helps nor hurts rankings.
- 2026-06-15: FAQ rich result documentation removed (feature no longer shown).
- 2026-06-12: new article for Tennessee small businesses on receiving notifications about removed or restricted web content.
- 2026-06-05: new guidance on third-party SEO tools, services and advice; "Do you need an SEO?" updated.
- 2026-05-27: preferred sources rolling out to AI Overviews and AI Mode.
- 2026-05-20: `hasAdultConsideration` added to merchant listing and product variant docs (parity with Merchant Center `adult`).
- 2026-05-15: new guide on optimizing for generative AI features (non-commodity content, local, shopping, image, video tips, AEO/GEO myths, initial AI agent guidance).
- 2026-05-15: clarified spam policies apply to generative AI responses in Search.
- 2026-05-08: FAQ rich result deprecation notice (deprecated 2026-05-07, no longer shown).
- 2026-04-30: preferred sources available in all Search languages; translated button assets.
- 2026-04-23: further clarification of when and why manual action follows spam reports.
- 2026-04-20: snippet docs: new "read more" deep links section.
- 2026-04-14: Google may use spam report submissions to take manual action.
- 2026-04-13: new spam policy: back button hijacking (malicious practices policy).
- 2026-03-24: Discussion Forum and QA Page: more supported properties (comment thread structure).
- 2026-03-24: robots meta docs: note on robots meta tags outside the HTML head (behavior unchanged, previously undocumented).
- 2026-03-04: JavaScript SEO basics: outdated accessibility section removed (Google has rendered JavaScript for years; JS loading does not hinder Search).
- 2026-03-02: image SEO and Discover: preferred image via metadata; schema.org markup and `og:image` both used for thumbnails.
- 2026-02-05: Get on Discover expanded alongside the February 2026 Discover Core Update.
- 2026-02-03: default crawler file size limits moved to crawler docs; Googlebot's own limits made more precise.
- 2026-01-30: new preferred sources documentation.
- 2026-01-21: South African carousels, badges and refinement chips: added food delivery, car hire, bus booking (region: South Africa, beta).
- 2026-01-06: practice problem structured data documentation removed.

### 2025
- 2025-12-18: JavaScript: pages with non-`200` status may not be sent to rendering.
- 2025-12-18: migrated to crawling infrastructure site: faceted navigation URLs, crawl budget, HTTP status codes, DNS and network errors.
- 2025-12-17: JavaScript canonicalization: keep canonical identical to the original HTML, or omit it there (canonicalization runs before and after rendering).
- 2025-12-15: JavaScript and `noindex`: behavior on rendered pages is not well defined; do not put `noindex` in original code if the page might be indexed.
- 2025-12-09: core updates: continual smaller core updates; improvements can lift rankings without waiting for a major update.
- 2025-11-20: migrated crawler overview, request verification, crawl rate reduction, common crawlers and robots.txt interpretation docs to the crawling infrastructure site (content unchanged).
- 2025-11-19: Discover Follow feature guidance removed (feature gone).
- 2025-11-12: review snippet: avoid multiple ways of indicating what is reviewed.
- 2025-11-12: `Google-Pinpoint` user-triggered fetcher added.
- 2025-11-12: new merchant shipping policies docs (merchant-level shipping policy markup).
- 2025-11-05: practice problem deprecated (support removed from Search Console rich result reporting, Rich Result Test and filters from Jan 2026; Search Console API through Jan 2026).
- 2025-11-05: `Dataset` structured data used only by Dataset Search, not Google Search; Book actions deprecation banner removed (feature still uses markup).
- 2025-11-03: `Google-CWS` user-triggered fetcher added.
- 2025-10-15: Read Aloud: updated list of Google products using the service.
- 2025-10-09: `Google-NotebookLM` user-triggered fetcher added.
- 2025-09-09: docs removed for course info, estimated salary, learning video, special announcement, vehicle listing (no longer shown).
- 2025-08-28: new guidance on JavaScript-based paywalls.
- 2025-08-28: structured data carousels (beta) expanded to South Africa.
- 2025-07-11: return policy: offer-level supports only a subset of organization-level; merchant-level policies defined under `Organization`. Loyalty: program info defined separately under `Organization` (separate page or Merchant Center); shipping and returns loyalty benefits unsupported.
- 2025-07-01: Google Read Aloud user agent updated with newer browser versions.
- 2025-06-18: URL structure documentation reorganized with real-world examples (docs only).
- 2025-06-17: loyalty program availability: Australia, Brazil, Canada, France, Germany, Mexico, UK, US; desktop and mobile.
- 2025-06-16: AI Mode counted in Search Console Performance report totals.
- 2025-06-12: phase-out banners: book actions, course info, estimated salary, `ClaimReview`, learning video, special announcement, vehicle listing.
- 2025-06-11: multilingual docs: removed section on blocking auto-translated pages via robots.txt (aligns with March 2024 spam policy; docs only).
- 2025-06-10: loyalty program markup documentation launched; merchant return policy moved to its own page.
- 2025-06-05: event structured data: events must be bookable by the general public and held at a physical location; online event properties removed; more eligible and ineligible examples.
- 2025-06-05: `Recipe` `image` property does not influence the text result image.
- 2025-06-04: SafeSearch/explicit content docs revamped (moderation and CSAM best practices, video byte fetching, troubleshooting split out); ranking updated to hit explicit-video sites that block video fetching (significant drops possible, especially Video mode).
- 2025-05-21: new docs on AI features and your site, and on using generative AI content.
- 2025-05-21: structured data carousels (beta) expanded to Turkey.
- 2025-05-12: image best practices: reference image URLs consistently on large sites.
- 2025-04-25: `Google-Extended` token description clarified; `Googlebot-News` description corrected (its preferences do not affect the News tab).
- 2025-04-24: merchant listing energy efficiency: `EnergyConsumptionDetails` properties removed (backward-compat note), `certificationIdentification` alternative for merchants without EPREL codes.
- 2025-04-23: special announcement deprecation notice (deprecated 2025-07-31).
- 2025-04-11: carousels (beta): updated interest forms and supported query types.
- 2025-04-01: education Q&A carousel: Portuguese added (region/language).
- 2025-03-27: AI while browsing removed from paywall docs.
- 2025-03-17: education Q&A carousel: Spanish and Vietnamese added.
- 2025-03-14: return policy examples now include `returnPolicyCountry` (required for `MerchantReturnPolicy`).
- 2025-03-07: Page Annotations removed from "control what you share" docs.
- 2025-03-05: AI Mode added to robots `meta`, `data-nosnippet`, `X-Robots-Tag` specs (AI Mode in Search Labs).
- 2025-02-13: merchant listing: `priceType` and beta `validForMemberTier` for active, sale, strikethrough and member prices.
- 2025-02-06: new documentation on using Search Console and Google Analytics together.
- 2025-01-22: breadcrumb markup shown on desktop results only, not mobile.
- 2025-01-21: site reputation abuse policy: FAQ guidance folded in (editorial).
- 2025-01-15: review snippet: recommend accepting only ratings with a review comment and author name.

### 2024
- 2024-12-18: robots.txt error handling consolidated in one place (docs only).
- 2024-12-17: new docs: managing crawling of faceted navigation URLs.
- 2024-12-09: crawler overview: cache control header handling documented.
- 2024-11-29: sitelinks search box docs removed; `nositelinkssearchbox` archived (feature gone).
- 2024-11-20: opt-out info for the Page Annotations feature (iOS Google app).
- 2024-11-19: site reputation abuse policy: third-party content used to exploit ranking signals violates it regardless of first-party involvement.
- 2024-11-19: ranking systems guide: page-level and site-wide signals described.
- 2024-11-13: C2PA metadata extraction for "About this image".
- 2024-11-01: crawl budget: sites with separate mobile and desktop HTML must include all links on mobile.
- 2024-10-24: new Google Trends getting-started page.
- 2024-10-24: favicon: 1:1 aspect ratio, minimum 8x8 px, strongly recommended at least 48x48 px.
- 2024-10-23: URL structure: URL parameter best practice added.
- 2024-10-07: robots.txt fields not listed in the docs are unsupported.
- 2024-10-03: `Certification` markup for merchant listings; replaces `EnergyConsumptionDetails` from April 2025.
- 2024-10-02: `noarchive` moved to historical reference (cached link gone; tag can stay for other services).
- 2024-10-01: `Product` markup best practices: put it in initial HTML; ensure servers handle load when generated by JavaScript.
- 2024-09-25: spam policies clarified (what spam is, close involvement, circumvention can lower or remove ranking).
- 2024-09-24: `cache:` operator docs removed (no longer works).
- 2024-09-23: merchant listing: `priceType` and sale pricing examples.
- 2024-09-17: infinite scroll guidance migrated from blog into docs.
- 2024-09-16: `GoogleProducer` user agent URL updated; crawler docs gained content encodings and were reorganized with per-crawler robots.txt snippets.
- 2024-09-11: Indexing API submissions subject to spam detection; exceeding quotas may revoke access.
- 2024-09-10: video markup accepts `ineligibleRegion`.
- 2024-09-04: Indexing API: default quota is for setup and testing, approval needed for use; `DefaultRequestsPerMinutePerProject` is 380.
- 2024-08-30: AVIF added to supported image formats.
- 2024-08-26: organization markup: some properties influence which logo is shown, others used behind the scenes.
- 2024-08-26: `og:title` added as a title link source.
- 2024-08-23: video SEO docs overhauled (indexing criteria, technical requirements, watch page section).
- 2024-08-23: profile page and discussion forum markup: Perspectives renamed Forums.
- 2024-08-20: `Google-CloudVertexBot` crawler added (crawls on site owner's request for Vertex AI Agents).
- 2024-08-15: core updates docs restructured; helpful content system now part of core ranking systems (moved to archived section).
- 2024-08-15: AI Overviews counted in Search Console Performance report (clarification only).
- 2024-08-09: Notes documentation removed (experiment ended).
- 2024-07-31: Geo Data Upload references replaced by Google Maps Content Partners.
- 2024-07-31: spam policies and ranking systems: handling of sites with many non-consensual explicit fake images clarified.
- 2024-07-24: `GoogleProducer` user agent string changed (goo.gl retirement); hardcoded values need updating.
- 2024-07-19: note that Notes winds down end of July 2024.
- 2024-07-11: Search Console shipping and return settings; precedence rules expanded.
- 2024-07-10: translated results: added Arabic, Gujarati, Korean, Persian, Thai, Turkish, Urdu, Vietnamese.
- 2024-07-09: IPTC `compositeWithTrainedAlgorithmicMedia` supported.
- 2024-07-05: fragment URL guidance in URL structure docs.
- 2024-06-21: return policy precedence: product-level over organization-level; Merchant Center info overrides for feed products.
- 2024-06-20: carousels (beta): marking up categories with many items (pagination, infinite scroll).
- 2024-06-12: hreflang docs: `link` tags for alternates must not be combined in one tag.
- 2024-06-11: `Organization`-level return policies added.
- 2024-06-11: home activity structured data docs removed.
- 2024-06-04: Discussion Forum guidelines: `SocialMediaPosting` supported; image-only or video-only comments allowed.
- 2024-06-04: site names warning removed (issue resolved; recrawl takes time).
- 2024-05-23: EPUB added to indexable file types.
- 2024-05-16: `GoogleOther-Image` and `GoogleOther-Video` crawlers added.
- 2024-05-14: AI Overviews docs page added (replaces Search Generative Experience); robots meta and paywall docs updated.
- 2024-05-01: `Product` structured data split into intro, product snippet, merchant listing pages.
- 2024-04-26: traffic drop debugging: algorithmic update effects expanded; policy and manual action simplified to spam issues.
- 2024-04-25: new `user-triggered-fetchers-google.json` IP list; iOS variant of AdsBot Mobile Web removed.
- 2024-04-24: favicon `rel` value definitions added.
- 2024-04-17: video carousel (limited access) docs removed.
- 2024-04-16: images extracted only from the `src` attribute of `img` tags.
- 2024-04-11: carousels (beta): markup goes on the summary page only; detail pages need none.
- 2024-03-28: Web Stories still appear in Google Images, without the icon.
- 2024-03-25: `3DModel` markup for merchant listings.
- 2024-03-12: INP replaces FID as a Core Web Vital; page experience docs updated.
- 2024-03-06: guided recipes removed from `Recipe` docs (Assistant feature gone).
- 2024-03-05: three new spam policies: expired domain abuse, scaled content abuse, site reputation abuse; new helpful content FAQ.
- 2024-03-05: Google StoreBot user agent uses placeholder Chrome version.
- 2024-02-29: structured data carousels (beta) docs for travel, local, shopping queries.
- 2024-02-29: opt-out information for place entities in Page Insights.
- 2024-02-20: product variants: new docs, `isVariantOf`, variants with distinct URLs supported; `FreeReturn` vs `ReturnShippingFees` for `returnFees`.
- 2024-02-15: `rel="canonical"` links with extra attributes (device or language) are ignored for canonicalization (always the case).
- 2024-02-09: allowed characters in product `sku` clarified.
- 2024-02-08: Web Stories availability updated (no icon in Images, grid became carousel).
- 2024-02-08: `Google-Extended` affects Gemini Apps (formerly Bard) and does not affect Search.
- 2024-02-07: Dynamic Search Ad target crawls every 21 days instead of 14.
- 2024-02-06: JavaScript docs reviewed; dynamic rendering documented as a deprecated workaround.
- 2024-02-02: SEO Starter Guide revamped.
- 2024-01-09: `suggestedAge` supported on `Product` as alternative to `suggestedMinAge`/`suggestedMaxAge`.
- 2024-01-05: snippet docs: the page content itself is the primary snippet source (not structured data or meta description).
- Maintenance 2024: Googlebot doc refresh (Jan 25), descriptive anchor texts (Jan 10), in-page `@id` examples switched to hashtags (Jan 9), image removals doc refresh (Feb 9), case studies (Wix Feb 5, Vidio Jun 4).

### 2023
- 2023-12-19: spam policies/ranking systems: further clarification for sites with many non-consensual explicit images.
- 2023-12-14: Discussion Forum and Q&A: author URLs recommended.
- 2023-12-13: `Organization`: `telephone` and `email` allowed besides `contactPoint`.
- 2023-12-12: course info availability added.
- 2023-12-04: vacation rental structured data docs added.
- 2023-12-01: Mobile Friendly Test and Mobile Usability report mentions removed (retired).
- 2023-11-29: new `Organization` docs merging Logo docs (contact info, legal name, identifiers).
- 2023-11-27: profile page and discussion forum docs added; Q&A page recommendations expanded.
- 2023-11-15: Notes docs added; course info docs added; avoid flight prices in title links.
- 2023-11-14: Google Safety crawler added to crawler list.
- 2023-11-08: reviews system documented as improving at a regular, ongoing pace.
- 2023-11-01: video markup: include time and timezone.
- 2023-10-18: paywalled structured data supported in Rich Results Test; generative AI in Search considerations; SGE noted for `nosnippet` and `max-snippet`.
- 2023-10-18: favicon: both the favicon file and home page must be crawlable by Googlebot-Image and Googlebot; Google Favicon user agent string removed (tokens unchanged).
- 2023-10-17: Article: provide timezone; Googlebot timezone is PST.
- 2023-10-16: vehicle listing structured data added.
- 2023-10-13: host group visual element removed from the Visual Elements gallery.
- 2023-09-29: more explanation of why Discover traffic fluctuates.
- 2023-09-28: new `Google-Extended` token controlling use for Bard and Vertex AI generative APIs.
- 2023-09-27: CSAM handling clarified in spam policies and ranking systems guide.
- 2023-09-26: new docs on debugging search traffic drops and Search Console bubble chart; two Search Console intro articles merged.
- 2023-09-22: content in CSS `content` properties may not be indexed (not in DOM).
- 2023-09-14: guidance on hosting third-party content; what to do after a helpful content update; removing content or changing dates.
- 2023-09-14: How-to rich result removed (docs and case study); FAQ rich result limited to well-known authoritative government and health sites.
- 2023-09-11: typo fixed in `Google-InspectionTool` user agent string.
- 2023-09-07: site names available in all Search languages.
- 2023-08-24: CSV added to indexable file types.
- 2023-08-15: local business opening hours: only schema.org enumeration values, in English.
- 2023-08-02: local business: `review` and `aggregateRating` only recommended for sites collecting reviews about other businesses (no self-serving reviews).
- 2023-07-28: site name docs: preferred name not chosen, alternative names, known issue; available on desktop and mobile.
- 2023-07-20: characters supported in URLs clarified.
- 2023-07-18: `related:` operator removed (unsupported).
- 2023-06-13: `MathSolver`: examples for derivatives, integrals, limits in `potentialAction.mathExpression-input`.
- 2023-05-30: `.ai` added to TLDs treated as gTLD.
- 2023-05-26: recommendation for adult sites with age gate interstitials.
- 2023-05-24: events search experience country list limited to countries where users see it.
- 2023-05-22: site names documentation mentions subdomains.
- 2023-05-17: translated results: Bengali, English, French, German, Marathi, Portuguese, Spanish, Tamil, Telugu; `Google-InspectionTool` crawler added.
- 2023-05-10: Digital Source Type recommendation for image metadata; banner announcing INP replacing FID in March 2024.
- 2023-05-04: video `description` moved to recommended.
- 2023-05-02: canonicalization: explicit recommendations for syndicated content.
- 2023-04-28: opt-out section removed from Education Q&A docs.
- 2023-04-26: return countries (`applicableCountry`) maximum raised from 25 to 50.
- 2023-04-24: crawler page reorganized by capability and trigger.
- 2023-04-21: crawler IP address JSON lists published.
- 2023-04-20: `GoogleOther` generic crawler added.
- 2023-04-19: helpful content guidance includes page experience; page experience page revised, Core Web Vitals page split out.
- 2023-04-17: return policy information added to `Product` docs.
- 2023-04-03: package tracking early adoption focused on India, Japan, Brazil.
- 2023-03-17: 15 MB fetch limit also applies to each subresource (JavaScript, CSS).
- 2023-03-13: AdsBot Mobile Web Android user agent string updated.
- 2023-03-02: South Korea removed from job search experience regions.
- 2023-02-23: favicon hosting-location requirement removed (can be hosted on another domain).
- 2023-02-22: Discover uses many of the same signals as Search.
- 2023-02-15: new best practices for links.
- 2023-02-13: policy circumvention wording simplified; sitemap docs revamped (sitemap extensions combined).
- 2023-02-10: `GoogleProducer` user agent listed (documentation only).
- 2023-02-08: "Who, How, and Why" guidance on content production.
- 2023-02-03: JSON-LD recommended as easiest to maintain; all three formats equal for Google if valid.
- 2023-02-02: canonicalization docs split into three (what, how to specify, fix issues).
- 2023-01-23: Follow feature RSS: include `<title>` and per-item `<link>`; images parsed from `<img>` even inside `<picture>`.
- 2023-01-06: `www` and `m` prefixes treated as root domain for site names.
- 2023-01-05: `If-Modified-Since` request header added to crawl budget docs.
- 2023-01-03: Article `headline` 110-character limit removed (concise titles recommended).
- Maintenance 2023: monthly SEO Office Hours transcripts and overview page, Vimeo case study (Jan 25), video SEO case study (Jul 19), Search Central Blog Authors section (Feb 1), URL/crawler clarifications.

### 2022
- 2022-12-19: Web Light docs removed and user agent retired.
- 2022-12-14: link spam information added to spam updates docs; new Google Search Status Dashboard page; Learning Video `text` recommended instead of required.
- 2022-12-13: Visual Elements Gallery added; mobile-first indexing and mobile site docs consolidated.
- 2022-12-06: helpful content classifier works globally across languages.
- 2022-12-02: crawl budget myths: `noindex` is not a good crawl-budget control; `4xx` responses (except `429`) do not waste crawl budget.
- 2022-12-01: Duplex on the web user agent retired.
- 2022-11-23: enumerated Product properties (e.g. `availability`) described to support translation.
- 2022-11-22: supported languages for video key moments listed; rich result eligibility criteria clarified in general structured data guidelines.
- 2022-11-21: new Guide to Google Search ranking systems; policy circumvention section added.
- 2022-11-15: Mobile recharge early adopters signup removed.
- 2022-11-14: review snippet: use dot separators for decimal ratings (commas still eligible).
- 2022-11-09: JavaScript may insert crawlable links.
- 2022-11-08: localized sitemap child elements do not count towards URL limit; AdsBot ignores global `*` rules (notes added).
- 2022-10-24: site names supported at domain level only; favicons at domain and subdomain, not subdirectory.
- 2022-10-14: site name documentation added.
- 2022-10-13: ranking update pages (core, helpful content, product reviews, spam); Webmaster Guidelines renamed Google Search Essentials with technical requirements, spam policies (new: misleading functionality, copyright-removal requests, online harassment removals, scam and fraud; consolidated link spam, malware, hacked content, thin affiliate pages) and the people-first content guide.
- 2022-10-12: image credits in Image Metadata structured data.
- 2022-10-07: product review page examples added.
- 2022-09-20: Google Site Verifier user agent added.
- 2022-09-13: major `Product` docs update: eligibility for merchant listing experiences via structured data; `itemReviewed.datePublished` re-added.
- 2022-09-09: Fact Check `datePublished` removed.
- 2022-09-02: indexable file types docs migrated from Search Console Help.
- 2022-08-31: JavaScript may add, change or remove `meta` tags.
- 2022-08-29: Learning video `educationalLevel` values; Local Business multiple types go in an array (`additionalType` unsupported).
- 2022-08-24: Education Q&A content guidelines; International Targeting report references removed (multiregional advice still valid).
- 2022-08-22: `Article` markup open to all page types.
- 2022-08-11: rich-media (Silverlight, Flash) docs removed.
- 2022-08-10: `gtin12` documented (generic `gtin` fine, most specific recommended); dynamic rendering documented as workaround.
- 2022-08-09: Follow feature feed best practices (descriptive title, single feed).
- 2022-08-08: URL form of GTINs unsupported; use numerical GTIN.
- 2022-08-05: pros and cons enhancement for editorial product review pages documented.
- 2022-07-13: AdsBot Mobile Web user agent updated.
- 2022-07-07: Google Search ranking updates page added.
- 2022-07-06: navigation reorganized by topic; duplicate beginner guides removed.
- 2022-07-04: `Course` rich result requires three courses.
- 2022-06-30: JavaScript-injected canonical link tags documented.
- 2022-06-23: bytes of textual content Googlebot crawls documented.
- 2022-06-22: `JobPosting`: `jobLocation` requires `addressCountry`.
- 2022-06-17: product rich results cover single-product pages, including variants with distinct URLs.
- 2022-06-10: `Vary: Cookie` support for signed exchanges.
- 2022-06-03: `<title>` should match the page's primary script and language.
- 2022-06-01: Article author markup best practices; Learning Video docs.
- 2022-05-31: Job training docs removed (markup may stay).
- 2022-05-22: video thumbnails: at least 80% of pixels with little or no transparency for indexing.
- 2022-05-10: Education Q&A docs; valid page metadata docs; title link headline troubleshooting.
- 2022-05-06: deprecated Image and Video sitemap tags removed from docs.
- 2022-04-14: How Search Works docs merged into one.
- 2022-03-23: two more best practices for multi-product reviews.
- 2022-03-17: SafeSearch docs: allow Google to fetch video content files.
- 2022-02-25: Crawl Stats reference removed from signed exchange docs.
- 2022-01-28: SafeSearch docs merged and expanded (`rating` meta tag on explicit pages, separate location, troubleshooting).
- 2022-01-21: `indexifembedded` robots meta tag added.
- 2022-01-20: `Car` markup note for product review snippet eligibility.
- 2022-01-18: Recipe `cookTime`, `prepTime`, `totalTime` accept exact times only (no ranges).
- Maintenance 2022: SEO Office Hours transcripts and section (Dec 13), signed exchange validator link (Feb 11).

### 2021
- 2021-12-16: intrusive interstitials blog post converted to guidelines.
- 2021-12-01: "Write high quality product reviews" added.
- 2021-11-18: how to opt out of Google Read Aloud; crawling behavior clarified.
- 2021-11-17: interactive reading checklist; translated results docs.
- 2021-11-16: guideline on logos and white backgrounds.
- 2021-11-10: Logo: `ImageObject` allowed; Googlebot IP list published.
- 2021-11-04: signed exchanges: well-formed SXG recommendation removed (Google retries without SXG `Accept`); page experience desktop rollout.
- 2021-11-02: video best practice: dedicated page per video.
- 2021-10-28: unused fields removed from `HowTo`, `QAPage`, `SpecialAnnouncement` docs.
- 2021-10-15: Review snippet `author.name` must be under 100 characters.
- 2021-10-13: `VideoGame` invalid for Software App; co-type with another supported type.
- 2021-10-08: title link and snippet docs split; "title link" term introduced.
- 2021-09-27: "Best practices for ecommerce sites in Google Search" added.
- 2021-09-01: beta Follow feature docs.
- 2021-08-09: Schema Markup Validator stable; Structured Data Testing Tool redirected.
- 2021-08-06: `Article` `author.url` recommended.
- 2021-07-30: Math solver guidelines; solution page markup removed.
- 2021-07-28: single fact check per page; signed exchange cache lifetime.
- 2021-07-26: local business `priceRange` under 100 characters.
- 2021-07-22: FAQ hidden-content guideline examples (expandable sections valid); `@id` removed from Local business.
- 2021-07-21: search operators documentation added.
- 2021-07-13: `JobPosting` editorial guideline; optional `directApply`.
- 2021-06-29: redirects guide expanded.
- 2021-06-25: HTTP status codes and network/DNS errors page added.
- 2021-06-18: robots.txt docs simplified and expanded; redundant structured data docs removed; troubleshooting improved.
- 2021-06-15: page experience rollout timeline (complete by end of August 2021).
- 2021-06-11: sitelinks search box `urlTemplate` standard form; Dataset `funder`.
- 2021-06-10: critic review docs deprecated (markup may stay).
- 2021-06-08: `BackOrder` allowed for `availability`.
- 2021-06-04: `gtin` allowed; `isbn` usage clarified.
- 2021-06-03: Math solvers `inLanguage`.
- 2021-06-01: six new Math Solver problem types; `DuplexWeb` user agent updated.
- 2021-05-18: `SeekToAction` for key moments; `Clip` out of beta; JobPosting regions add Austria, Denmark.
- 2021-05-06: AMP `Article` publisher logo: raw URLs and `ImageObject` both understood.
- 2021-04-19: signed exchanges getting-started docs.
- 2021-04-08: Discover quality guideline (filters job applications, petitions, forms, code repositories, decontextualized satire).
- 2021-04-07: video `thumbnailUrl` must use supported Google Images formats.
- 2021-04-01: key moments: automatic detection, `Clip` or YouTube description for manual labels.
- 2021-03-29: key moments interest form removed.
- 2021-03-25: practice problems and math solvers structured data added.
- 2021-03-24: `experienceRequirements.monthsOfExperience` examples; Dataset `isAccessibleForFree`.
- 2021-03-16: `max-snippet` examples; defaults per tag stated.
- 2021-03-11: beta JobPosting properties (credential, experience requirements).
- 2021-03-08: `JP_E-CODE` accepted in Book.
- 2021-03-01: Google Sites sitemap instructions removed.
- 2021-02-08: 3D and AR Early Adopters Program page removed.
- 2021-02-02: cross-language search results docs removed.
- 2021-01-28: `Event` `offers.priceCurrency` requires ISO 4217 code.
- 2021-01-22: price drop enhancement for product rich results documented.
- 2021-01-20: Job Training appearance not available on Search.
- 2021-01-05: hreflang checker tool list pruned.
- Maintenance 2021: wording clarifications and examples (e.g. Mar 17 video best practices tidy-up, Jun 18 robots.txt simplification).

### 2020
- 2020-12-04: migrated from Search Console Help: crawl budget guide, web hosting, redacted information, bloggers, `Soft 404`.
- 2020-11-19: Webmaster blogs migrated to Search Central Blog.
- 2020-11-12: STEM Q&A guideline; Googlebot HTTP/2 crawling documented.
- 2020-11-11: site redesign as Google Search Central; 100+ pages migrated from Search Console Help (international overview, site move, block access, Search Appearance overview).
- 2020-11-10: page experience ranking change planned for May 2021.
- 2020-10-30: Book `librarySystem` value `government` replaces `national`; data-vocabulary.org markup ineligible for rich results after 2021-01-29 (use schema.org).
- 2020-10-29: image ratio specs for `hiringOrganization.logo`.
- 2020-10-22: package tracking API accepts POST only.
- 2020-10-06: Web Stories examples, best practices, content policy.
- 2020-09-22: `shippingDetails` added to `Product`.
- 2020-09-18: fact check guidelines consolidated: corrections policy, no political entity sites, attribute claims to distinct origin.
- 2020-09-15: Video `regionsAllowed` and Microdata examples; `bestRating`/`worstRating` recommended for non-5-point scales.
- 2020-08-31: Image License badge out of beta.
- 2020-08-27: robots.txt user-agent group merging clarified.
- 2020-08-26: Home activities rich result docs.
- 2020-08-21: non-HTTP network connections in JavaScript fixes.
- 2020-08-10: different `Article` requirements for AMP and non-AMP.
- 2020-08-05: images in structured data must use Google Images formats.
- 2020-08-03: Estimated salary `jobBenefits`, `industry`.
- 2020-07-23: multiple fact checks per page not yet displayed.
- 2020-07-21: Dataset `measurementTechnique`; unique `name` per dataset.
- 2020-07-20: `EmployerAggregateRating` `reviewCount` (either `reviewCount` or `ratingCount` required).
- 2020-07-16: Book provider feeds; product rich results only for single-product pages (not categories or lists); small font size defined.
- 2020-07-08: multiple structured data items on a page understood nested or separate.
- 2020-07-01: AMP logo may use any Google Images format.
- 2020-06-30: Carousel docs: more examples and supported types.
- 2020-06-19: Image License requires `contentUrl`.
- 2020-06-16: browser-native lazy-loading added.
- 2020-06-12: `.webp` and (06-10) `.svg` allowed for `Logo`.
- 2020-06-08: Software App `applicationCategory` is `Text`.
- 2020-06-04: sitelinks search box query key can be any RFC 3986 string.
- 2020-05-28: page experience docs added.
- 2020-05-27: Job training: `occupationalCategory` required, `description` recommended, `url` not required.
- 2020-05-19: Web Stories enablement guidance.
- 2020-05-15: Product docs: note on Google Shopping tab eligibility.
- 2020-05-12: JavaScript SEO: JavaScript-generated links, History API over fragment URLs, avoid soft 404s.
- 2020-05-11: Googlebot crawl rate reduction guidance; removed docs deprecated since June 2019 (Social Profile, Corporate Contact, Place Actions).
- 2020-05-07: Rich Result Test supports AMP `Article`; removed `description`, `publisher.logo.height/width`; Mini-apps program page removed.
- 2020-05-06: robots.txt testing information.
- 2020-05-05: Job posting content policies (irrelevant, incomplete, unauthorized, disguised ads); `SpecialAnnouncement` Search Console info; Podcasts docs migrated to Podcasts Manager help.
- 2020-05-01: Indexing API: `noindex` meta tag as a removal option.
- 2020-04-30: cached links unreliable for debugging, use URL Inspection; Breadcrumb explanation of URL path relation.
- 2020-04-27: Job training: 2-letter country codes for provider addresses.
- 2020-04-23: missing meta description issue in mobile-first indexing best practices.
- 2020-04-22: Paywalled content: supported types list.
- 2020-04-20: COVID-19 resources and education site best practices.
- 2020-04-16: `governmentBenefitsInfo` properties for COVID-19 announcements; JobPosting work-from-home markup.
- 2020-04-14: `Event` `organizer` properties.
- 2020-04-07: `Event` online events require timezone UTC/GMT offset.
- 2020-04-03: structured data via JavaScript guidance; COVID-19 announcements update.
- 2020-04-02: COVID-19 announcements submission in Search Console and technical support group (national governments, US state agencies first).
- 2020-03-31: COVID-19 announcement structured data guidance (under development).
- 2020-03-26: guidance on pausing an online business.
- 2020-03-24: Estimated Salary requires `duration` instead of `unitText`; Google Podcasts badges in 49 languages.
- 2020-03-23: Package tracking `CanReschedule`.
- 2020-03-20: Latest updates page created; long-lived caching and content fingerprinting for JavaScript.
- 2020-03-17: `Event` `eventAttendanceMode`, `VirtualLocation`; sitelinks search box troubleshooting; `hasCredential` dropped from Job training recommendations.
- 2020-03-16: `Event` `eventStatus`, `previousStartDate`.
- 2020-03-05: `Product`: one of `review`, `aggregateRating`, `offers` required; `brand` type `Brand` or `Organization`; Package tracking `TimestampEvent`, `LocationEvent`.
- 2020-03-03: hostload issues in mobile-first indexing error list.
