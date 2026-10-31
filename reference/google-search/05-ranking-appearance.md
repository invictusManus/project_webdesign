# Ranking & search appearance: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Overview
https://developers.google.com/search/docs/appearance · Last updated: 2026-09-16

### Search appearance topics listed
- Hub page for how a site can influence its look in Google Search. Topics listed: AI features, Business details, Byline dates, Favicons, Featured snippets, Flexible Sampling general guidance, Google Discover, Images, Preferred sources, Regional differences in Search experience, Search profiles, Site names, Sitelinks, Snippets, Title links, Top Places List, Translated results, Videos, Visual Elements gallery, Web stories.

### Using structured data
- Google uses structured data to understand page content; it can make a site eligible for richer results.
- Linked helpers: list of supported markup, how structured data works, generating structured data with JavaScript, general structured data guidelines, enriched search results.
- Features that use structured data: Article, Breadcrumb, Carousel, Course list, Dataset, Discussion forum, Education Q&A, Employer aggregate rating, Event, Image metadata, Job posting, Local business, Math solver, Movie carousel, Organization, Practice problem, Product (Product snippet, Merchant listing, Variants, Merchant return policy, Merchant shipping policy, Loyalty program), Profile page, Q&A, Recipe, Review snippet, Software app, Speakable, Subscription and paywalled content, Vacation rental, Video.

### Early Adopters Program
- Google pilots some features with a limited number of organizations. Currently listed: Package tracking; Structured data carousels `(beta)`.

---

## AI features
https://developers.google.com/search/docs/appearance/ai-features · Last updated: 2025-12-10

### Core statement
- Applies to AI Overviews and AI Mode in Google Search.
- SEO best practices stay relevant. No additional requirements, no special optimizations to appear in AI Overviews or AI Mode.

### How AI features work
- Both surface links to supporting pages. They may use "query fan-out": multiple related searches across subtopics and data sources to build a response.
- While generating, models find additional supporting pages, so the set of links can be wider and more diverse than classic web search.
- AI Overviews: gist of a complex topic or question plus a jumping-off point; designed for queries where they add benefit beyond classic results. Shown only when systems judge them additive, so they often do not trigger.
- AI Mode: for queries needing exploration, reasoning or complex comparisons; nuanced multi-part questions; answer with links to supporting sites.
- The two may use different models and techniques, so responses and links differ.

### Technical requirements to appear
- A page must be indexed and eligible to be shown in Google Search with a snippet. No other technical requirements.
- Meeting every requirement, practice and policy does not guarantee crawling, indexing or serving.

### SEO practices that still apply
- Allow crawling in robots.txt and in any CDN or hosting layer.
- Make content findable through internal links.
- Provide great page experience.
- Keep important content available as text.
- Support text with high-quality images and videos where applicable.
- Structured data must match visible page text.
- Keep Merchant Center and Business Profile info up to date.
- No new machine-readable files, "AI text files" or markup needed. No special schema.org structured data needed.
- Verify the site in Search Console to find and diagnose technical issues.

### Measuring performance
- AI feature traffic is included in overall Search Console totals, in the Performance report under the "Web" search type.
- Analytics tools (e.g. Google Analytics) can track conversions and time on site. Google reports clicks from results pages with AI Overviews tend to be higher quality (more time spent on site).

### Controlling content in AI features
- AI is built into Search, so robots.txt directives for Googlebot are the crawl control for Search (including AI features).
- To limit what is shown from pages: `nosnippet`, `data-nosnippet`, `max-snippet`, or `noindex`.
- To limit AI training and grounding in other Google systems: Google-Extended (separate control).

### Troubleshooting preview controls
- Confirm the control is correct and visible to Googlebot: use URL Inspection to see the HTML Googlebot received.
- Allow time for recrawl: crawling can take several days to several months depending on how often a page needs refreshing. A recrawl can be requested.
- If still failing, post in the Google Search Central Help Community.

---

## Business details
https://developers.google.com/search/docs/appearance/establish-business-details · Last updated: 2025-12-10

### Purpose
- Establishing your official site and business info with Google helps users recognize the official site; covers location, official site and content info for results, knowledge panel and Google Maps.

### Claim your local business
- Claim and verify the Business Profile to manage how the business appears in Google Maps and Search.
- Verified owners can provide or edit address, contact info, business type and photos; this feeds Maps and the knowledge panel.

### Register your website with Search Console
- First step for an official presence: verify ownership in Search Console (verifies owners and operators), then use it to monitor how Google shows site information.

### Update your site's knowledge panel
- Google algorithms collect public info (site name, corporate contacts, social profiles).
- A verified official representative can update the knowledge panel and override automatically found info.

### Add structured data
- Structured data = explicit clues about page meaning.
- Site logo: add `Organization` structured data on the official website pointing to the preferred logo; used for the logo in Search results and the knowledge panel.
- Breadcrumbs: `Breadcrumb` structured data shows the page's position in the hierarchy (user can navigate up level by level from the last crumb).

### Highlight customer support methods
- Follow best practices so Google shows accurate contact/support info for the business or service (detail is on a linked page, not this one).

### Troubleshooting
- Wait at least one week after the marked-up page was last crawled, then report wrong knowledge panel info via the Feedback link at the bottom of the panel. Recognized authorities / the represented entity get more edit options.
- Test markup with the Rich Results Test; allow about a week for Google to find and update site details.

---

## Byline dates
https://developers.google.com/search/docs/appearance/publication-dates · Last updated: 2025-12-10

### What it is
- Byline date = Google's estimate of when a page (or video) was updated or published; may be shown in results if useful to the user.
- Google uses several factors, not a single one, to estimate when a page was published or significantly updated.

### How to provide dates
- Add a user-visible date, prominent, with a text label such as "Publish" or "Last updated". Accepted examples: "Posted Feb 4, 2019", "Published February 4, 2019", "Last updated: Feb 14, 2018", "Updated Feb 14, 2019 8pm ET". A publication date, a last-updated date, or both.
- Also specify dates in structured data: use a `CreativeWork` subtype (`Article`, `BlogPosting`, `VideoObject`, `NewsArticle`) with `datePublished` and/or `dateModified` (ISO 8601 with offset, e.g. `2021-07-20T08:00:00+08:00`). Follow Google's structured data guidelines.

### Best practices
- No guarantee a byline date (visible or markup) is shown.
- Date is required; time is not. Adding time and timezone in markup is recommended for precision.
- If timezone is given, it must be correct, including daylight saving time.
- Visible and structured values must be consistent (date, and optional time/timezone); time and timezone may be omitted in visible text even if present in markup.
- No future dates, and not the date of the event/action described. Dates must describe page publication or update, not the story's subject. Use `Event` markup for described activities.
- Minimize other dates on the page; if wrong dates get picked, remove some or all other dates.
- Pages meant for Google News search: follow additional News guidelines.

---

## Favicons
https://developers.google.com/search/docs/appearance/favicon-in-search · Last updated: 2026-10-27

### Scope
- Organic Search results only (Google Ads logos have separate business-logo specs).

### Implementation
- Create a favicon that meets the guidelines; add a `<link>` in the `<head>` of the home page, e.g. `<link rel="icon" href="/path/to/favicon.ico">`.
- `rel` values supported: `icon` (HTML standard; `shortcut icon` also supported for historical reasons), `apple-touch-icon`, `apple-touch-icon-precomposed` (older iOS alternative).
- `href`: relative or absolute URL; may be hosted elsewhere (e.g. a CDN).
- Allow recrawl time (several days to several weeks); indexing of the home page can be requested with URL Inspection.

### Guidelines (all required for eligibility; appearance still not guaranteed)
- One favicon per site, where site = hostname. `www.example.com` and `code.example.com` can differ. A subdirectory shares the favicon of its host.
- Supported home pages: domain-level (`https://example.com`), subdomain-level (`https://news.example.com`). Not supported: subdirectory-level (`https://example.com/news`).
- Googlebot must be able to crawl the home page and follow redirects from it to the page that declares the favicon; Googlebot-Image must be able to crawl the favicon file. No blocking by robots.txt or otherwise.
- Must be visually representative of the brand.
- Shape and size: square (1:1), minimum 8x8 px; recommended larger than 48x48 px.
- Formats: BMP, GIF, ICO, PNG, JPEG, PPM, TIFF.
- URL must be stable (do not change it often).
- Inappropriate imagery (e.g. pornography, hate symbols) is replaced with a default icon.

> Note: SVG is not in the supported favicon format list on this page (it is supported for page images, see Images). A favicon feedback form exists; feedback is not acted on individually.

---

## Featured snippets
https://developers.google.com/search/docs/appearance/featured-snippets · Last updated: 2025-12-10

### What they are
- Boxes with the format reversed: descriptive snippet first. Can also appear inside a related-questions group ("People Also Ask").

### Opting out
- Block all snippets (featured and regular): `nosnippet` on the page. `data-nosnippet` text is also excluded from both. If both are present, `nosnippet` wins.
- Block featured only: experiment with lower `max-snippet` values (regular snippets stay). Featured snippets appear only if enough text can be shown to generate a useful one. Keep lowering if it persists; shorter value means lower likelihood.
- No exact minimum length published: it varies with snippet info, language and platform (mobile, app, desktop).
- Low `max-snippet` is not a guarantee; `nosnippet` is the guaranteed method.

### Getting one
- You cannot mark a page as a featured snippet. Google systems decide and elevate.

### Click behaviour
- A click takes the user to the exact section shown; scroll happens automatically with no site annotation. Falls back to the top of the page if the browser lacks the underlying technology or Google cannot confidently locate the position.

---

## Flexible Sampling
https://developers.google.com/search/docs/appearance/flexible-sampling · Last updated: 2025-12-10

### Background
- Experiments with publishers showed even minor changes to sampling levels can degrade user experience and, as access is restricted, can unintentionally affect article ranking in Search.
- Two sampling types: metering (a quota of articles before a paywall or login wall) and lead-in (part of an article shown without the full text). "Paywall" here includes registration walls.
- Experiment cautiously.

### Metering
- Monthly metering is preferred over daily: more flexible, safer to test (changing 10 monthly samples by one has less impact than changing 3 daily), focuses paywall views on engaged users while newer users see value first.
- Amount: no universal value; for most daily news publishers expected 6 to 10 articles per user per month. Suggested starting point: 10 per month for Google search users, then iterate. Compare the current share of search users who hit the paywall and choose a number with a similar result. Lower later once stable.

### Lead-in
- Showing the first few sentences above the paywall after the meter runs out is endorsed: lets users experience the value and builds curiosity.

### Making changes
- Test values against referral traffic and conversion.
- Users forced to subscribe after little content lose interest sharply. General satisfaction degrades significantly when paywalls show more than 10% of the time (about 3% of audience exposed). Approach that limit with caution.
- Advanced option: target the engaged segment (users who use up the monthly allotment) with a lower allowance while giving others more liberal access.

### Indicating paywalled content
- Enclose paywalled content with structured data so Google can tell it from cloaking (different content for Googlebot vs. users).
- If content must not reach the browser at serve time, use a paywall implementation that does not send the paywalled content to the browser.
- See the paywalled-content structured data and JavaScript paywall guidance pages.

---

## Google Discover
https://developers.google.com/search/docs/appearance/google-discover · Last updated: 2026-03-09

### Eligibility
- Part of Search showing content by interest, based on Web and App Activity.
- Automatically eligible if indexed and compliant with Discover content policies. No special tags or structured data. Eligible does not mean guaranteed.
- Older content can appear if helpful and relevant.
- Policy violations can trigger Discover manual actions, shown in Search Console under Security and Manual actions.
- Discover uses many of the same signals and systems as Search for helpful, people-first content.

### Recommendations
- Avoid clickbait: misleading or exaggerated preview details (title, snippet, image) or withholding key info to inflate engagement.
- Titles and headlines should capture the essence of the content.
- Avoid sensationalism (morbid curiosity, titillation, outrage).
- Provide timely content, good storytelling or unique insight.
- Include compelling, relevant, high-quality images; large images are more likely to generate visits. Recommended specs:
  - at least 1200 px wide;
  - more than 300,000 total pixels (example: 1280x720 = 921,600);
  - 16:9 aspect ratio. Google auto-crops; if you crop yourself, make sure key details stay in the crop specified in `og:image` and avoid automatically applying an aspect ratio;
  - enabled by the `max-image-preview:large` setting, or by AMP.
- Use schema.org markup or the `og:image` `meta` tag to name a large, relevant, representative image (influences the thumbnail). Avoid generic images (e.g. a logo) and text-heavy images.
- Provide great page experience.
- Discover favors suitable feed content (articles, videos) and may filter out job applications, petitions, forms, code repositories, or satire without context. Uses SafeSearch and also filters content seen as shocking or unexpected.

### Why traffic changes
- Less predictable than keyword search; treat as supplemental.
- Causes: changing user interests; adjustments to content types (regularly includes sports, health, entertainment, lifestyle); Search updates (see core updates); ongoing Discover UX changes unrelated to content quality or publishing frequency.

### Monitoring
- Search Console Performance report for Discover: impressions, clicks, CTR for content shown in the last 16 months, once a minimum impressions threshold is met. Includes traffic from Chrome and tracks Discover across all surfaces.

---

## Images
https://developers.google.com/search/docs/appearance/google-images · Last updated: 2026-03-02

### Scope
- One set of recommendations for text-result images, Discover and Google Images. Two areas: help Google discover/index images; optimize the landing pages.

### Discovery and indexing
- Use standard HTML `<img>` elements: Google finds images in the `src` attribute (also when nested in `<picture>`). CSS background images are not indexed.
- Image sitemap: submit to surface images not otherwise found. `<image:loc>` may point to other domains (CDNs). Verify the CDN domain in Search Console to receive crawl-error info.
- Responsive images: `<picture>` or `srcset`, but some browsers/crawlers do not understand them, so always give a fallback `src`. With `<picture>`, include an `<img src alt>` fallback (HTML Standard 4.8.1); `<source type="image/avif|webp|svg+xml" srcset>` allows newer formats with graceful degradation.
- Supported formats (in `img` `src`): BMP, GIF, JPEG, PNG, WebP, SVG, AVIF. File extension should match the file type.
- Data URIs allowed (`src="data:image/svg+xml;base64,..."`); inlining reduces requests but can greatly increase page size, so use deliberately.
- Speed and quality: sharp images attract more clicks in thumbnails; images are often the biggest page-weight contributor, so apply current optimization and responsive techniques; analyze with PageSpeed Insights.

### Landing-page optimization
- Preferred image via metadata (Google's selection is automated; these influence it):
  - schema.org `primaryImageOfPage` on `WebPage` (URL or `ImageObject`); or
  - an `image` (URL or `ImageObject`) on the main entity linked by `mainEntity` / `mainEntityOfPage`; or
  - `og:image` meta tag.
- Preferred image practices: relevant and representative; not generic (logo) or text-bearing; no extreme aspect ratio (too narrow or too wide); high resolution if possible.
- Title link and snippet are generated from sources including `title` and `meta` tags; follow Google's title and snippet guidelines.
- Structured data: enables rich results such as a prominent badge in Google Images. Follow the general and type-specific guidelines or the page is ineligible. `image` is a required field in each of these types to qualify for the badge/rich result.
- Filenames: short, descriptive (`my-new-black-kitten.jpg` over `IMG00023.JPG`); avoid `image1.jpg`, `pic.gif`, `1.jpg`. Consider automating naming at scale. Translate filenames for localized images (mind URL encoding for non-Latin characters). Filenames are only a light clue.
- Context: place images near relevant text on relevant pages; captions and image titles are used.
- Alt text: the most important image metadata; also helps accessibility and works as anchor text when the image is a link. Be useful and information-rich, in page context. No keyword stuffing (poor UX, may be seen as spam). Missing alt is bad; `alt="puppy"` better; a descriptive alt best. For inline `<svg>` use a `<title>` (with `aria-labelledby`).
- Test with an accessibility audit and a slow-network emulator.
- Crawl budget: reference an image by the same URL on every page so Google can cache and reuse it.

### Opt out of Google Images inline linking
- When an image request's HTTP referrer is a Google domain, reply `200` or `204` with no content. Google still crawls the page and shows a crawl-time thumbnail instead of the full-size image. Reversible anytime, no reprocessing, not cloaking, no manual action. Alternatively block the image from search entirely.

### SafeSearch
- Make sure Google understands the nature of the site (label pages for SafeSearch) so filters apply correctly.

---

## Top Places List
https://developers.google.com/search/docs/appearance/top-places-list · Last updated: 2025-12-10

### What it is
- A rich result showing "top places" lists that mention a business (e.g. "Top 10 Chinese restaurants in NYC"). Only for businesses with a physical location. Actual appearance may differ.

### Requirements for the listing site
- List is curated by the content provider; genuine, independent, not sponsored.
- Not made of templated sentences built from data or automated metrics.
- No vulgar or potentially offensive language.

### Opting out
- To keep your site's lists out of this feature, opt out of display in local search results and other Google properties.

---

## Understanding page experience
https://developers.google.com/search/docs/appearance/page-experience · Last updated: 2026-09-22

### Principle
- Core ranking systems reward good page experience overall; do not focus on one or two aspects.

### Self-assessment questions
- Good Core Web Vitals? Secure (HTTPS)? Displays well on mobile? No excessive ads distracting from or interfering with main content? No intrusive interstitials? Main content easy to tell apart from other content?
- Not an exhaustive list of aspects.

### Resources
- Core Web Vitals guidance; Search Console HTTPS report; check connection security as reported by Chrome (and move to HTTPS if needed); interstitials guidance; Chrome Lighthouse (incl. mobile usability); CrUX ad metrics (experimental: ad count, ad density, ad weight).

### FAQ
- No single "page experience signal"; core ranking systems use a variety of aligned signals.
- Core Web Vitals are used by ranking systems; good CWV recommended. Good scores in Search Console or third-party tools do not guarantee top ranking; chasing a perfect score for SEO alone may not be the best use of time.
- Other page experience aspects do not directly boost ranking but make the site more satisfying, which aligns with what ranking seeks to reward.
- Evaluation is generally page-specific, with some site-wide assessments.
- Importance: Google still shows the most relevant content even with sub-par page experience; for many queries with plenty of helpful content, great page experience can contribute to success.

---

## Core Web Vitals
https://developers.google.com/search/docs/appearance/core-web-vitals · Last updated: 2025-12-10

### Definition and role
- Metrics for real-world loading performance, interactivity and visual stability. Highly recommended for Search success; aligns with what core ranking systems reward.

### Metrics and thresholds
- Largest Contentful Paint (LCP), loading: occur within the first 2.5 seconds of the page starting to load.
- Interaction to Next Paint (INP), responsiveness: less than 200 milliseconds.
- Cumulative Layout Shift (CLS), visual stability: less than 0.1.

### Tools
- Search Console Core Web Vitals report; web.dev CWV guide (measure, debug, improve); tools that measure LCP, INP, CLS.

> Note: this page states the thresholds without naming a percentile or data source; the "75th percentile of field data" convention is not on this page.

---

## Interstitials and dialogs
https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials · Last updated: 2025-12-10

### Definitions and impact
- Interstitial = overlay on the whole page; dialog = overlay on part of the page. Intrusive ones obstruct content, usually for promotion.
- They frustrate users, erode trust, make content harder for Google to understand, and may hurt search performance.

### Unintrusive practices (apply to all promotional dialogs, including app install prompts)
- Use banners instead of full-page interstitials: small fraction of the screen. App install options: Smart App Banners (Safari), in-app install experience (Chrome), or an HTML banner linking to the app store. Same container can serve newsletter prompts.
- Use common libraries/CMS plugins for standard dialogs (e.g. newsletter sign-up); plugin developers can ship improvements at scale.
- Avoid (unless legally mandatory): obscuring the entire page; redirecting the user to a separate page for consent or input.

### Mandatory interstitials
- Legally required interstitials (e.g. casino age gate) are exempt from these guidelines, but recommended:
  - overlay the content (so Google can still index some of it);
  - do not redirect incoming HTTP requests to a different page to collect consent or data (redirecting all URLs to one page leaves only that page in search results because Googlebot can fetch only it).
- Adult-content age gates: let Googlebot crawl without triggering the gate by verifying Googlebot requests and serving content without the gate.

---

## Preferred sources
https://developers.google.com/search/docs/appearance/preferred-sources · Last updated: 2026-09-18

### What it does
- If users select your site as a preferred source, its content is more likely to appear in "Top Stories" with a "preferred" badge. In AI Mode and AI Overviews, content can carry a "preferred" badge for those users.

### Availability
- Top Stories: global, all languages where Search is available.
- AI Mode and AI Overviews: all languages and locales where those features exist; the site must be included in Search generative AI features in Search Console.
- Only domain-level and subdomain-level sites are eligible in the source preferences tool (`https://www.example.com/`, `https://code.example.com/` yes; `https://www.example.com/blog` no). Check by searching the site in the tool.

### Ways to promote (all optional, none required to appear)
- Standard JavaScript button (recommended): two lines of HTML; localized, Google-styled, returns the reader to the page.
- Advanced JavaScript with custom design assets: same user flow, programmatic control.
- Deeplink: for when the button cannot be used (e.g. CMS limits); text link or clickable image on pages, social posts, newsletters, promotions.

### Standard JavaScript implementation
- Load the library, preferably in `<head>`: `<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>`.
- Place `<div google-add-preferred-source-btn></div>` where the button should appear.
- Theme: `data-theme="light"` (default) or `"dark"`.
- Language: `data-lang="en"` etc. overrides the browser-language default (list of supported codes downloadable).

### Advanced JavaScript implementation
- Default behaviour scans the DOM for `google-add-preferred-source-btn` elements. For custom triggers, init programmatically.
- ES module: `import { preferredSource } from "https://news.google.com/swg/js/v1/publisher.mjs"`; `preferredSource.init({ theme: 'light'|'dark', lang })` (lang defaults to page language); call `preferredSource.addPreferredSource()` from a click handler.
- Script-queue (IIFE): load `publisher.js` with `preferred-sources-control="manual"` to stop auto-render (omit it and any `google-add-preferred-source-btn` element initializes immediately); push a callback onto `self.PREFERRED_SOURCE`, then `init` and `addPreferredSource()` as above.
- Both approaches expose the same methods; a demo page exists.

### Deeplink implementation
- Format: `https://www.google.com/preferences/source?q=<your domain>` (example `q=example.com`). Works as a text link or an `<a>` wrapping an `<img>` (give it alt text).
- Button assets: design your own badge or download Google's translated graphic assets.

---

## A guide to Google Search ranking systems
https://developers.google.com/search/docs/appearance/ranking-systems-guide · Last updated: 2025-12-10

### Overview
- Automated systems weigh many factors and signals across hundreds of billions of pages. Guide covers notable systems: some are part of the core ranking systems, others serve specific needs.
- Systems work at page level, using page and site-wide signals/classifiers. Some good site-wide signals do not guarantee all content ranks well; some poor ones do not doom all content.
- Systems are improved by testing and notice of updates is given when useful.

### Active systems (alphabetical as on the page)
- BERT: AI system that understands how word combinations express meaning and intent.
- Crisis information systems: personal crisis (hotlines and trusted-organization content for queries on suicide, sexual assault, poison ingestion, gender-based violence, drug addiction); SOS Alerts (updates from local, national or international authorities in disasters or widespread crises: emergency numbers and sites, maps, translations of useful phrases, donation opportunities).
- Deduplication systems: very similar results are collapsed to the most relevant; omitted results can be shown on request. Also applies to featured snippets: an elevated listing is not repeated later on the first page.
- Exact match domain system: domain-name words are one relevance factor, but content on domains built to exactly match a query (e.g. `best-places-to-eat-lunch`) does not get excess credit.
- Freshness systems: "query deserves freshness"; fresher content for queries where expected (new movie reviews; news after an earthquake).
- Link analysis systems and PageRank: understand how pages link to infer topics and helpfulness. PageRank is still part of core ranking systems though evolved from launch.
- Local news systems: surface local news sources (Top stories, Local news features).
- MUM (Multitask Unified Model): understands and generates language; not currently used for general ranking, only specific uses (COVID-19 vaccine searches, featured snippet callouts).
- Neural matching: AI system matching representations of concepts in queries to pages.
- Original content systems: show original content, including original reporting, ahead of those who merely cite it. Supports a special canonical markup creators can use to flag the primary page when duplicated.
- Removal-based demotion systems:
  - legal removals: significant volume of valid copyright removal requests against a site can demote the site's other content; similar for defamation, counterfeit goods, court-ordered removals; CSAM is always removed and sites with a significant proportion of it are demoted entirely;
  - personal information removals: significant volume against a site with exploitative removal practices demotes its other content, with checks for the same pattern on other sites; similar demotion possible for doxxing, non-consensual explicit imagery, non-consensual explicit fake content.
- Passage ranking system: AI system that identifies individual passages to judge page relevance.
- RankBrain: AI system relating words to concepts so relevant content can return even without the exact query words.
- Reliable information systems: elevate authoritative pages, demote low-quality content, elevate quality journalism; show automatic content advisories on rapidly changing topics or when result quality confidence is low (with tips on searching better).
- Reviews system: rewards high-quality reviews with insightful analysis and original research from experts or enthusiasts (see Reviews system).
- Site diversity system: generally no more than two listings from the same site in top results, with exceptions when especially relevant. Subdomains are generally treated as part of the root domain, but sometimes as separate sites.
- Spam detection systems: include SpamBrain; constantly updated against evolving spam violating the spam policies.

### Retired systems (historical)
- Helpful content system: announced 2022 as the Helpful Content Update (original, helpful, people-first content over search-engine-first content); became part of core ranking systems in March 2024.
- Hummingbird: major overall ranking improvement, August 2013.
- Panda system: high-quality, original content; announced 2011; part of core ranking systems since 2015.
- Penguin system: link spam; announced 2012; integrated into core ranking systems in 2016.

---

## Reviews system
https://developers.google.com/search/docs/appearance/reviews-system · Last updated: 2025-12-10

### How it works
- Rewards reviews with in-depth research over thin content that merely summarizes products, services or other things. Improved at an ongoing pace.
- Evaluates first-party standalone content (articles, blog posts, pages) written to recommend, give an opinion or analyze. Does not evaluate third-party reviews such as user reviews on a product or service page.
- Covers single-item reviews, head-to-head comparisons and ranked lists, on any topic (products, media, services, businesses).
- Evaluated mainly per page; sites with a substantial amount of review content may have any of their content evaluated. With few reviews, a site-wide evaluation is not likely.
- Languages (global): English, Spanish, German, French, Italian, Vietnamese, Indonesian, Russian, Dutch, Portuguese, Polish.
- Product structured data may help identify product reviews, but the system does not rely on it solely.

### Implications
- Content can recover over time after improvements. The assessment is only one of many ranking factors, so changes can happen anytime. Guidance on writing high-quality reviews is a separate page.

---

## Core updates
https://developers.google.com/search/docs/appearance/core-updates · Last updated: 2025-12-10

### How they work
- Several times a year Google makes broad, significant changes to algorithms and systems; announced on the Google Search ranking updates list. Most sites need not worry.
- Goal: deliver helpful, reliable results overall. Broad, not targeted at specific sites or pages. Pages that drop are not necessarily "bad"; others now fit better.

### Check for a drop in Search Console
- Confirm the update finished (Search Status Dashboard: note start and end dates).
- Wait at least a full week after completion before analyzing; then compare that week with the week before the rollout began.
- Review top pages and queries before vs after:
  - small drop (e.g. position 2 to 4): no drastic action; avoid changing content that already performs well;
  - large drop (e.g. position 4 to 29): deeper assessment.
- Analyze search types separately (Web, Google Images, Video mode, News tab).

### Assessing a large drop
- For sustained, large site-wide drops, use the helpful/reliable/people-first self-assessment on the whole site (not just pages). Be objective, ask unaffiliated people to answer the questions.
- Evaluate the most affected pages against the questions; other pages may help searchers better.

### Making changes
- No quick fixes (e.g. removing a page element because it was "bad for SEO"); make sustainable, user-focused changes.
- Improve content meaningfully (e.g. rewrite or restructure for readability and navigation).
- Deleting content is a last resort for unsalvageable content. Wanting to delete whole sections suggests they were made for search engines first; removing unhelpful content can help the good content.

### Timing
- Some changes take effect in days; confirming site-wide helpfulness can take several months. If nothing after months, effects may wait for the next core update.
- Smaller unannounced core updates happen continuously and can also lift improved content.
- No guarantee of impact. Rankings are dynamic (changing user expectations and web content), causing both gains and drops.

---

## Spam updates
https://developers.google.com/search/docs/appearance/spam-updates · Last updated: 2025-12-10

- Spam detection runs constantly; a "spam update" is a notable improvement, announced on the Google Search ranking updates list. Example: SpamBrain, the AI-based spam-prevention system, is improved from time to time.
- After a change tied to a spam update, review the spam policies. Violating sites may rank lower or not appear. Improvement is possible if automated systems learn over months that the site complies.
- Link spam update: fixing may not bring recovery, because the systems nullify the effect of spammy links; any ranking benefit those links gave is lost permanently.
