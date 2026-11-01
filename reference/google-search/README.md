# Google Search documentation: complete notes

Every page of Google's official Search documentation, read in full and condensed into notes: [Search Central docs](https://developers.google.com/search/docs) plus the [crawling infrastructure docs](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers). This is the knowledge base behind [`05-seo.md`](../../standards/05-seo.md) and [`06-geo-aeo.md`](../../standards/06-geo-aeo.md).

- **Scope:** 184 pages, retrieved 2026-10-31. Each note gives the source URL and the page's own "last updated" date.
- **License:** Source content © Google, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). These notes are summarized and restructured. They are not an official Google document; when in doubt, the linked page wins.
- **Use:** the standards hold the testable rules; these notes hold the detail behind them (every property, limit and exception). `scripts/check.sh` verifies that every page listed below has notes.
- **Keeping it current:** `scripts/google-docs.py` compares the live documentation with the dates below and lists new, removed and changed pages. `--text DIR` saves the full text of those pages so their notes can be re-written. The weekly `maintenance` GitHub workflow runs this and opens or updates an issue when something changed. After refreshing notes, update the page's date here.

## Notes files

| File | Area | Pages |
|---|---|---|
| [`01-essentials-fundamentals.md`](01-essentials-fundamentals.md) | Search Essentials & SEO fundamentals | 12 |
| [`02-crawling.md`](02-crawling.md) | Crawling & Google crawlers | 26 |
| [`03-indexing-urls-sitemaps.md`](03-indexing-urls-sitemaps.md) | Indexing: URLs, links, sitemaps, canonicalization, mobile, AMP | 19 |
| [`04-indexing-javascript-metadata-moves.md`](04-indexing-javascript-metadata-moves.md) | Indexing: JavaScript, metadata, robots directives, removals, site moves | 18 |
| [`05-ranking-appearance.md`](05-ranking-appearance.md) | Ranking & search appearance | 18 |
| [`06-search-features.md`](06-search-features.md) | Search features & regional features | 22 |
| [`07-structured-data-basics.md`](07-structured-data-basics.md) | Structured data: basics, Article, Book, Breadcrumb, Carousel | 9 |
| [`08-structured-data-features-1.md`](08-structured-data-features-1.md) | Structured data: Course to Job posting | 9 |
| [`09-structured-data-shopping.md`](09-structured-data-shopping.md) | Structured data: Shopping | 7 |
| [`10-structured-data-features-2.md`](10-structured-data-features-2.md) | Structured data: Local business to Video | 13 |
| [`11-monitoring-debugging.md`](11-monitoring-debugging.md) | Monitoring & debugging | 15 |
| [`12-specialty-updates.md`](12-specialty-updates.md) | Site-specific guides & documentation changelog | 16 |

## Page index

### Search Essentials & SEO fundamentals → [`01-essentials-fundamentals.md`](01-essentials-fundamentals.md)

| Page | Last updated |
|---|---|
| [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies) | 2026-08-28 |
| [Technical requirements](https://developers.google.com/search/docs/essentials/technical) | 2025-12-18 |
| [Overview](https://developers.google.com/search/docs/essentials) | 2025-12-10 |
| [Optimizing for generative AI](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | 2026-07-10 |
| [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 2026-10-05 |
| [Do you need an SEO?](https://developers.google.com/search/docs/fundamentals/do-i-need-seo) | 2026-06-05 |
| [Developer's guide to Search](https://developers.google.com/search/docs/fundamentals/get-started-developers) | 2025-12-10 |
| [Maintaining your site's SEO](https://developers.google.com/search/docs/fundamentals/get-started) | 2025-12-18 |
| [How Google Search works](https://developers.google.com/search/docs/fundamentals/how-search-works) | 2025-12-18 |
| [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | 2025-12-10 |
| [Guidance on third-party SEO tools and advice](https://developers.google.com/search/docs/fundamentals/third-party-seo) | 2026-06-05 |
| [Guidance on using generative AI](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) | 2026-10-01 |

### Crawling & Google crawlers → [`02-crawling.md`](02-crawling.md)

| Page | Last updated |
|---|---|
| [About Google's web crawling](https://developers.google.com/crawling/docs/about-crawling) | 2026-03-03 |
| [Crawling changelog](https://developers.google.com/crawling/docs/changelog) | 2026-10-30 |
| [Optimize your crawl budget](https://developers.google.com/crawling/docs/crawl-budget) | 2026-07-22 |
| [APIs-Google](https://developers.google.com/crawling/docs/crawlers-fetchers/apis-user-agent) | 2025-11-21 |
| [Feedfetcher](https://developers.google.com/crawling/docs/crawlers-fetchers/feedfetcher) | 2026-02-11 |
| [Common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) | 2026-10-30 |
| [Special case crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-special-case-crawlers) | 2026-09-17 |
| [User-triggered fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) | 2026-08-19 |
| [List of Google crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers) | 2026-06-12 |
| [Google Read Aloud](https://developers.google.com/crawling/docs/crawlers-fetchers/read-aloud-user-agent) | 2025-12-02 |
| [Reduce the Google crawl rate](https://developers.google.com/crawling/docs/crawlers-fetchers/reduce-crawl-rate) | 2026-10-06 |
| [Verify requests from Google](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests) | 2026-03-20 |
| [Verifying Googlebot and other Google crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/verifying-googlebot) | 2026-03-20 |
| [Authenticate requests with Web Bot Auth (experimental)](https://developers.google.com/crawling/docs/crawlers-fetchers/web-bot-auth) | 2026-10-13 |
| [Improve crawling of faceted navigation URLs](https://developers.google.com/crawling/docs/faceted-navigation) | 2025-12-18 |
| [Myths about crawling](https://developers.google.com/crawling/docs/myths-about-crawling) | 2025-12-18 |
| [Create and submit a robots.txt file](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt) | 2025-11-21 |
| [How Google interprets the robots.txt specification](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec) | 2026-10-23 |
| [Update your robots.txt file](https://developers.google.com/crawling/docs/robots-txt/submit-updated-robots-txt) | 2025-11-21 |
| [List of useful robots.txt rules](https://developers.google.com/crawling/docs/robots-txt/useful-robots-txt-rules) | 2026-06-12 |
| [Network and DNS errors](https://developers.google.com/crawling/docs/troubleshooting/dns-network-errors) | 2025-12-18 |
| [HTTP status codes](https://developers.google.com/crawling/docs/troubleshooting/http-status-codes) | 2026-02-04 |
| [Ask Google to recrawl your URLs](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) | 2025-12-10 |
| [Googlebot](https://developers.google.com/search/docs/crawling-indexing/googlebot) | 2026-02-03 |
| [Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) | 2025-12-10 |
| [Troubleshoot crawl errors](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors) | 2025-12-18 |

### Indexing: URLs, links, sitemaps, canonicalization, mobile, AMP → [`03-indexing-urls-sitemaps.md`](03-indexing-urls-sitemaps.md)

| Page | Last updated |
|---|---|
| [Enhance AMP content](https://developers.google.com/search/docs/crawling-indexing/amp/enhance-amp) | 2026-07-01 |
| [Remove AMP content](https://developers.google.com/search/docs/crawling-indexing/amp/remove-amp) | 2026-07-01 |
| [Validate AMP content](https://developers.google.com/search/docs/crawling-indexing/amp/validate-amp) | 2026-07-01 |
| [About AMP on Google Search](https://developers.google.com/search/docs/crawling-indexing/amp) | 2026-07-01 |
| [Fix canonicalization issues](https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting) | 2026-08-21 |
| [What is URL canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization) | 2026-08-20 |
| [How to specify a canonical URL with rel="canonical" and other methods](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) | 2026-07-10 |
| [File types Google can index](https://developers.google.com/search/docs/crawling-indexing/indexable-file-types) | 2026-02-03 |
| [Links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) | 2025-12-10 |
| [Mobile site and mobile-first indexing](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) | 2025-12-10 |
| [Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) | 2026-07-08 |
| [Combining sitemap extensions](https://developers.google.com/search/docs/crawling-indexing/sitemaps/combine-sitemap-extensions) | 2025-12-10 |
| [Image sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps) | 2025-12-10 |
| [Manage sitemaps with sitemap index file](https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps) | 2025-12-10 |
| [News sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap) | 2025-12-10 |
| [Learn about sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview) | 2025-12-10 |
| [Video sitemaps and alternatives](https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps) | 2026-05-20 |
| [URL structure](https://developers.google.com/search/docs/crawling-indexing/url-structure) | 2026-10-21 |
| [Overview](https://developers.google.com/search/docs/crawling-indexing) | 2025-12-10 |

### Indexing: JavaScript, metadata, robots directives, removals, site moves → [`04-indexing-javascript-metadata-moves.md`](04-indexing-javascript-metadata-moves.md)

| Page | Last updated |
|---|---|
| [Redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects) | 2026-04-14 |
| [noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) | 2025-12-10 |
| [Control what you share with Google](https://developers.google.com/search/docs/crawling-indexing/control-what-you-share) | 2026-10-21 |
| [Dynamic rendering as a workaround](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering) | 2025-12-10 |
| [Fix search-related JavaScript problems](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript) | 2025-12-18 |
| [Understand the JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) | 2026-03-04 |
| [Fix lazy-loaded content](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading) | 2025-12-10 |
| [Redacted information](https://developers.google.com/search/docs/crawling-indexing/keep-redacted-information-out) | 2025-12-10 |
| [Temporarily pause or disable a website](https://developers.google.com/search/docs/crawling-indexing/pause-online-business) | 2025-12-10 |
| [Image removals](https://developers.google.com/search/docs/crawling-indexing/prevent-images-on-your-page) | 2025-12-10 |
| [rel attributes](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links) | 2025-12-10 |
| [Page removals](https://developers.google.com/search/docs/crawling-indexing/remove-information) | 2025-12-10 |
| [Robots meta tag, data-nosnippet, and X-Robots-Tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) | 2026-03-24 |
| [Changing your hosting](https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes) | 2025-12-10 |
| [Move a site with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) | 2026-08-20 |
| [Meta tags and HTML attributes that Google supports](https://developers.google.com/search/docs/crawling-indexing/special-tags) | 2025-12-10 |
| [Page metadata](https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata) | 2025-12-10 |
| [A/B testing](https://developers.google.com/search/docs/crawling-indexing/website-testing) | 2025-12-10 |

### Ranking & search appearance → [`05-ranking-appearance.md`](05-ranking-appearance.md)

| Page | Last updated |
|---|---|
| [AI features](https://developers.google.com/search/docs/appearance/ai-features) | 2025-12-10 |
| [Interstitials and dialogs](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials) | 2025-12-10 |
| [Core updates](https://developers.google.com/search/docs/appearance/core-updates) | 2025-12-10 |
| [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) | 2025-12-10 |
| [Business details](https://developers.google.com/search/docs/appearance/establish-business-details) | 2025-12-10 |
| [Favicons](https://developers.google.com/search/docs/appearance/favicon-in-search) | 2026-10-27 |
| [Featured snippets](https://developers.google.com/search/docs/appearance/featured-snippets) | 2025-12-10 |
| [Flexible Sampling](https://developers.google.com/search/docs/appearance/flexible-sampling) | 2025-12-10 |
| [Google Discover](https://developers.google.com/search/docs/appearance/google-discover) | 2026-03-09 |
| [Images](https://developers.google.com/search/docs/appearance/google-images) | 2026-03-02 |
| [Understanding page experience](https://developers.google.com/search/docs/appearance/page-experience) | 2026-09-22 |
| [Preferred sources](https://developers.google.com/search/docs/appearance/preferred-sources) | 2026-09-18 |
| [Byline dates](https://developers.google.com/search/docs/appearance/publication-dates) | 2025-12-10 |
| [A guide to Google Search ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide) | 2025-12-10 |
| [Reviews system](https://developers.google.com/search/docs/appearance/reviews-system) | 2025-12-10 |
| [Spam updates](https://developers.google.com/search/docs/appearance/spam-updates) | 2025-12-10 |
| [Top Places List](https://developers.google.com/search/docs/appearance/top-places-list) | 2025-12-10 |
| [Overview](https://developers.google.com/search/docs/appearance) | 2026-09-16 |

### Search features & regional features → [`06-search-features.md`](06-search-features.md)

| Page | Last updated |
|---|---|
| [Ad networks and translation-related Google Search features](https://developers.google.com/search/docs/appearance/ad-network-and-translation) | 2025-12-10 |
| [Overview](https://developers.google.com/search/docs/appearance/aggregator-features) | 2026-09-18 |
| [Aggregator unit](https://developers.google.com/search/docs/appearance/aggregator-unit) | 2026-10-19 |
| [Ecosystem carousel](https://developers.google.com/search/docs/appearance/ecosystem-carousel) | 2026-09-08 |
| [Enable Web Stories on Google](https://developers.google.com/search/docs/appearance/enable-web-stories) | 2026-07-01 |
| [Job sites features](https://developers.google.com/search/docs/appearance/job-sites) | 2026-09-11 |
| [Package tracking](https://developers.google.com/search/docs/appearance/package-tracking) | 2026-07-14 |
| [Places sites features](https://developers.google.com/search/docs/appearance/places-sites) | 2026-09-11 |
| [Search profiles](https://developers.google.com/search/docs/appearance/search-profiles) | 2026-09-16 |
| [Site names](https://developers.google.com/search/docs/appearance/site-names) | 2025-12-10 |
| [Sitelinks](https://developers.google.com/search/docs/appearance/sitelinks) | 2025-12-10 |
| [Snippets](https://developers.google.com/search/docs/appearance/snippet) | 2026-04-20 |
| [South Africa features](https://developers.google.com/search/docs/appearance/south-africa-features) | 2026-09-08 |
| [Structured data carousels (beta)](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta) | 2026-09-11 |
| [Supplier unit](https://developers.google.com/search/docs/appearance/supplier-unit) | 2026-09-18 |
| [Title links](https://developers.google.com/search/docs/appearance/title-link) | 2025-12-10 |
| [Translated results](https://developers.google.com/search/docs/appearance/translated-results) | 2025-12-10 |
| [UGC Fresh Data](https://developers.google.com/search/docs/appearance/ugc-fresh-data-program) | 2026-10-08 |
| [Videos](https://developers.google.com/search/docs/appearance/video) | 2025-12-18 |
| [Visual Elements gallery](https://developers.google.com/search/docs/appearance/visual-elements-gallery) | 2026-02-04 |
| [Web Story content policy](https://developers.google.com/search/docs/appearance/web-stories-content-policy) | 2025-12-10 |
| [Best practices for creating Web Stories](https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices) | 2026-06-09 |

### Structured data: basics, Article, Book, Breadcrumb, Carousel → [`07-structured-data-basics.md`](07-structured-data-basics.md)

| Page | Last updated |
|---|---|
| [Enriched search results](https://developers.google.com/search/docs/appearance/enriched-search-results) | 2025-12-10 |
| [Article](https://developers.google.com/search/docs/appearance/structured-data/article) | 2026-09-08 |
| [Book actions](https://developers.google.com/search/docs/appearance/structured-data/book) | 2025-12-10 |
| [Breadcrumb](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) | 2026-09-08 |
| [Carousel](https://developers.google.com/search/docs/appearance/structured-data/carousel) | 2026-09-08 |
| [Generate structured data with JavaScript](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript) | 2025-12-10 |
| [Understand how structured data works](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | 2025-12-10 |
| [Structured data general guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | 2026-07-10 |
| [All structured data features](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) | 2026-10-16 |

### Structured data: Course to Job posting → [`08-structured-data-features-1.md`](08-structured-data-features-1.md)

| Page | Last updated |
|---|---|
| [Course list](https://developers.google.com/search/docs/appearance/structured-data/course) | 2026-09-08 |
| [Dataset](https://developers.google.com/search/docs/appearance/structured-data/dataset) | 2026-09-08 |
| [Discussion forum](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum) | 2026-09-08 |
| [Education Q&A](https://developers.google.com/search/docs/appearance/structured-data/education-qa) | 2026-09-08 |
| [Employer aggregate rating](https://developers.google.com/search/docs/appearance/structured-data/employer-rating) | 2026-09-08 |
| [Event](https://developers.google.com/search/docs/appearance/structured-data/event) | 2026-09-08 |
| [Fact check](https://developers.google.com/search/docs/appearance/structured-data/factcheck) | 2026-09-08 |
| [Image metadata](https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata) | 2025-12-10 |
| [Job posting](https://developers.google.com/search/docs/appearance/structured-data/job-posting) | 2026-09-08 |

### Structured data: Shopping → [`09-structured-data-shopping.md`](09-structured-data-shopping.md)

| Page | Last updated |
|---|---|
| [Loyalty program](https://developers.google.com/search/docs/appearance/structured-data/loyalty-program) | 2026-09-08 |
| [Merchant listing](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) | 2026-09-08 |
| [Product snippet](https://developers.google.com/search/docs/appearance/structured-data/product-snippet) | 2026-09-08 |
| [Variants](https://developers.google.com/search/docs/appearance/structured-data/product-variants) | 2026-09-08 |
| [Overview](https://developers.google.com/search/docs/appearance/structured-data/product) | 2025-12-10 |
| [Merchant return policy](https://developers.google.com/search/docs/appearance/structured-data/return-policy) | 2026-09-08 |
| [Merchant shipping policy](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy) | 2026-09-08 |

### Structured data: Local business to Video → [`10-structured-data-features-2.md`](10-structured-data-features-2.md)

| Page | Last updated |
|---|---|
| [Local business](https://developers.google.com/search/docs/appearance/structured-data/local-business) | 2026-09-08 |
| [Math solver](https://developers.google.com/search/docs/appearance/structured-data/math-solvers) | 2025-12-18 |
| [Movie carousel](https://developers.google.com/search/docs/appearance/structured-data/movie) | 2026-09-08 |
| [Organization](https://developers.google.com/search/docs/appearance/structured-data/organization) | 2026-09-08 |
| [Subscription and paywalled content](https://developers.google.com/search/docs/appearance/structured-data/paywalled-content) | 2026-09-08 |
| [Profile page](https://developers.google.com/search/docs/appearance/structured-data/profile-page) | 2026-09-08 |
| [Q&A](https://developers.google.com/search/docs/appearance/structured-data/qapage) | 2026-09-08 |
| [Recipe](https://developers.google.com/search/docs/appearance/structured-data/recipe) | 2026-09-08 |
| [Review snippet](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) | 2026-09-08 |
| [Software app](https://developers.google.com/search/docs/appearance/structured-data/software-app) | 2026-09-08 |
| [Speakable](https://developers.google.com/search/docs/appearance/structured-data/speakable) | 2026-09-08 |
| [Vacation rental](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental) | 2026-09-08 |
| [Video](https://developers.google.com/search/docs/appearance/structured-data/video) | 2026-09-24 |

### Monitoring & debugging → [`11-monitoring-debugging.md`](11-monitoring-debugging.md)

| Page | Last updated |
|---|---|
| [Analyze social and video platform content](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content) | 2026-07-29 |
| [Improve SEO with a bubble chart](https://developers.google.com/search/docs/monitor-debug/bubble-chart-analysis) | 2025-12-10 |
| [Debug drops in Search traffic](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) | 2025-12-10 |
| [Using Search Console and Google Analytics data for SEO](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console) | 2026-01-07 |
| [Prevent user-generated spam](https://developers.google.com/search/docs/monitor-debug/prevent-abuse) | 2026-10-26 |
| [Get started with Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start) | 2025-12-10 |
| [site: search operator](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site) | 2025-12-10 |
| [Google Images search operators](https://developers.google.com/search/docs/monitor-debug/search-operators/image-search) | 2025-12-10 |
| [Overview](https://developers.google.com/search/docs/monitor-debug/search-operators) | 2025-12-10 |
| [Malware and unwanted software](https://developers.google.com/search/docs/monitor-debug/security/malware) | 2025-12-10 |
| [Prevent a malware infection](https://developers.google.com/search/docs/monitor-debug/security/prevent-malware) | 2025-12-10 |
| [Google Safe Browsing Repeat Offenders Policy](https://developers.google.com/search/docs/monitor-debug/security/safe-browsing-repeat-offenders) | 2025-12-10 |
| [Social engineering (phishing and deceptive sites)](https://developers.google.com/search/docs/monitor-debug/security/social-engineering) | 2025-12-10 |
| [Overview](https://developers.google.com/search/docs/monitor-debug/security) | 2025-12-10 |
| [Get started with Google Trends](https://developers.google.com/search/docs/monitor-debug/trends-start) | 2025-12-10 |

### Site-specific guides & documentation changelog → [`12-specialty-updates.md`](12-specialty-updates.md)

| Page | Last updated |
|---|---|
| [Design a URL structure](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites) | 2025-12-10 |
| [Ecommerce site structure](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure) | 2025-12-10 |
| [Launch a new website](https://developers.google.com/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website) | 2025-12-10 |
| [Include structured data](https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce) | 2025-12-10 |
| [Pagination, incremental page loading, and Search](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading) | 2025-12-10 |
| [Share product data](https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google) | 2025-12-10 |
| [Where content can appear](https://developers.google.com/search/docs/specialty/ecommerce/where-ecommerce-data-can-appear-on-google) | 2025-12-10 |
| [Write high quality reviews](https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews) | 2025-12-10 |
| [Overview](https://developers.google.com/search/docs/specialty/ecommerce) | 2025-12-10 |
| [Guidelines for sites with explicit content](https://developers.google.com/search/docs/specialty/explicit/guidelines) | 2026-09-17 |
| [What to do if your site is incorrectly flagged as explicit](https://developers.google.com/search/docs/specialty/explicit/troubleshooting) | 2025-12-10 |
| [How Google crawls locale-adaptive pages](https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages) | 2025-12-10 |
| [Tell Google about localized versions of your page](https://developers.google.com/search/docs/specialty/international/localized-versions) | 2026-09-21 |
| [Managing multi-regional and multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites) | 2025-12-10 |
| [Overview](https://developers.google.com/search/docs/specialty/international) | 2025-12-10 |
| [Search Central documentation updates](https://developers.google.com/search/updates) | 2026-10-26 |
