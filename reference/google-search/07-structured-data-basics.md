# Structured data basics (how it works, general guidelines, enriched results, generating with JavaScript, feature gallery) plus feature guides Article, Book actions, Breadcrumb, Carousel: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Understand how structured data works
https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data · Last updated: 2025-12-10

### Purpose
- Structured data = standardized format giving explicit clues about page meaning and classifying content (e.g. on a recipe: ingredients, cook time, calories).
- Google also uses it to learn about the web and world (people, books, companies named in markup).
- Can enable rich results (more engaging results, may raise interaction). Case studies cited: Rotten Tomatoes +25% CTR (100,000 pages); Food Network +35% visits (80% of pages); Rakuten 1.5x time on page and 3.6x interaction rate on AMP pages with features; Nestlé 82% higher CTR for rich results.
- Labeled elements let users search by ingredient, calories, cook time, etc.

### Implementation basics
- Markup is in-page, on the page it describes; describes that page's content.
- CMS users (Wix, WordPress, Shopify) usually cannot edit HTML directly: use the CMS search-settings page or a structured-data plugin.
- Don't create blank/empty pages just to hold structured data. Don't mark up information not visible to users, even if accurate.
- Validate with Rich Results Test (also previews some features) during development; monitor Rich result status reports after deployment (templating or serving issues can break pages post-launch).

### Vocabulary and formats
- Most Search structured data uses schema.org vocabulary, but Google Search Central docs are definitive for Google behavior, not schema.org docs. schema.org has more attributes than Google needs; they may help other engines/tools.
- `data-vocabulary.org` markup is no longer eligible for rich results.
- All required properties must be present for eligibility. More recommended properties generally help, but fewer complete and accurate ones beat many incomplete, badly formed or inaccurate ones.
- Google may generally use `sameAs` and other schema.org data beyond the documented properties, possibly for future features.
- Supported formats (all 3 equally fine to Google if valid and correctly implemented per feature docs, unless documented otherwise):
  - JSON-LD (recommended): `<script>` in `<head>` or `<body>`; not interleaved with visible text, so nesting is easier; Google reads it when injected dynamically by JavaScript or CMS widgets. Easiest to maintain at scale, least error-prone.
  - Microdata: HTML attributes nested in content; usually `<body>`, allowed in `<head>`.
  - RDFa: HTML5 extension with attributes matching visible content; used in `<head>` and `<body>`.
- Follow the general guidelines plus type-specific guidelines, else ineligible.

### Getting started and measuring effect
- New to it: schema.org beginner guide (Microdata-focused but concepts apply). Then pick a feature from the gallery.
- Measuring: run a before/after test on a few pages.
  - Choose pages with no structured data, several months of Search Console data, not seasonal or time-sensitive, stable, but popular enough for meaningful data.
  - Add markup; confirm validity and that Google found it via URL Inspection.
  - Record Performance report data for a few months, filtered by URL, and compare.

## Structured data general guidelines
https://developers.google.com/search/docs/appearance/structured-data/sd-policies · Last updated: 2026-07-10

### Scope and consequences
- Must not violate Content policies for Google Search (incl. spam policies); these guidelines apply to all structured data and are required for rich result eligibility.
- A structured data issue can cause a manual action: the page loses rich result eligibility; it does not affect web ranking. Check Manual Actions report in Search Console.
- No guarantee of display even when the Rich Results Test passes. Reasons:
  - markup enables a feature but does not guarantee it; the algorithm tailors results by search history, location, device and may prefer another feature or plain text;
  - markup not representative of main content, or misleading;
  - incorrect in a way the Rich Results Test can't catch;
  - marked-up content hidden from the user;
  - page violates these guidelines, feature-specific guidelines, Search Essentials or content policies.

### Technical guidelines
- Testable with Rich Results Test and URL Inspection tool (catch most technical errors).
- Format: JSON-LD (recommended), Microdata or RDFa.
- Access: don't block structured-data pages from Googlebot via robots.txt, `noindex` or any other access control.

### Quality guidelines
- Not easily testable by tools; violations can stop rich result display or get markup marked as spam.
- Content:
  - follow web search spam policies;
  - provide up-to-date info (no rich result for time-sensitive content no longer relevant);
  - original content by you or your users;
  - don't mark up content not visible to readers (JSON-LD performer must match the performer described in the body);
  - don't mark up irrelevant or misleading content (fake reviews, content unrelated to page focus);
  - don't deceive: no impersonating a person or organization, no misrepresenting ownership, affiliation or primary purpose;
  - also follow feature-specific content policies (e.g. `JobPosting` content policies).
- Relevance: markup must truly represent page content. Bad examples: sports live-stream site labeling broadcasts as local events; woodworking site labeling instructions as recipes.
- Completeness:
  - specify all required properties; items missing them aren't eligible;
  - more recommended properties = higher quality for users (users prefer jobs with stated salaries, recipes with real user reviews and genuine ratings; reviews/ratings not by actual users may cause manual action); rich result ranking considers extra info.
- Location:
  - put markup on the page it describes unless the feature doc says otherwise;
  - for duplicate pages, recommended: same structured data on all duplicates, not only the canonical.
- Specificity: use the most specific applicable schema.org types and properties; follow feature-specific guidelines.
- Images:
  - image in markup must be relevant to the page (e.g. `NewsArticle.image` relevant to that article);
  - all image URLs in markup must be crawlable and indexable (check with URL Inspection).

### Multiple items on a page
- A page may hold several kinds of things (recipe + how-to video + breadcrumb); marking all up gives fuller understanding and eligibility for more features.
- Google understands both nesting and individual items:
  - Nesting: one main item with others grouped under it (e.g. `Recipe` with nested `aggregateRating` and `video`).
  - Individual items: separate blocks (e.g. `Recipe` plus `BreadcrumbList`, as a JSON-LD array). When items are more useful linked (recipe and video), use `@id` in both to state the video is about the page's recipe; unlinked, Google may not show the video as part of the Recipe rich result.
- Tips:
  - include the main type reflecting the page's focus (a recipe page needs `Recipe`, not only `VideoObject`, to be eligible for recipe rich results; with Video and Review markup it can qualify for recipe results, video search and review snippets);
  - items must be complete versus visible content: if you mark up reviews, mark up all reviews visible on the page; partial markup is misleading.

## Enriched search results
https://developers.google.com/search/docs/appearance/enriched-search-results · Last updated: 2025-12-10

### What it is
- A more interactive, immersive class of rich result (e.g. Jobs experience). Lets users search across structured properties (e.g. chicken soup recipes under 200 calories; recipes under 1 hour prep).
- Subset of rich results, implemented with structured data. Some types exist only as enriched (recipes, jobs, events); others can be extended from basic rich result with a few extra properties; the type's doc says whether/how.
- Enriched search types: Job Posting, Recipe, Event.
- Driven by the Search ranking algorithm: follow structured data quality guidelines, Search Essentials and enriched search quality guidelines.
- Structured data duplicated across pages (e.g. same job in several locations, same `description`, different `location`) is not treated as duplicate by the enriched algorithm.

### Enriched search quality guidelines
- If a large part of a site misses the quality bar, the algorithm can exclude the entire site from enriched results.
- Required properties: each type defines a set; items missing them are ineligible.
- Completeness: more recommended properties = higher quality; described as one of the most important enriched-search ranking signals (stated salaries for jobs, real reviews and genuine star ratings for recipes).
- Relevance: same examples as general guidelines (live streams as local events; woodworking as recipes).
- Leaf content: enriched search is only for leaf pages (detailed properties of one item), not listing/category pages linking to several leaf pages (e.g. "10 best ideas for cooking turkey" page, or page listing all jobs in Mountain View).
- Content policies: type-specific; violators may rank less favorably or be ineligible.

## Generate structured data with JavaScript
https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript · Last updated: 2025-12-10

### Overview
- Common methods: Google Tag Manager (GTM) and custom JavaScript.
- `Product` markup warning: dynamically generated markup can make Shopping crawls less frequent and less reliable, a problem for fast-changing availability and price. Merchants optimizing for all shopping results should ensure the server can handle increased Google traffic.

### Google Tag Manager
- Steps: install GTM; add a Custom HTML tag; paste a supported structured data block; install container per the admin menu's install section; publish the container; test.
- Use GTM variables to pull values from the page instead of duplicating data in GTM (duplication risks page/markup mismatch). Example: custom variable `recipe_name` returning `document.title`, used as `{{recipe_name}}` in the tag; create variables for all needed fields (e.g. `recipe_image`, `recipe_author`).

### Custom JavaScript
- JS can generate all structured data or add to server-rendered markup. Google processes structured data present in the DOM when it renders the page (see JavaScript basics guide).
- Pattern: find the type, then add a snippet that builds a `<script type="application/ld+json">`, sets its text content (e.g. from a fetched API response) and appends it to `document.head`. Test with Rich Results Test.

### Server-side rendering
- Structured data may also be emitted in server-rendered output (see the framework's docs).

### Testing
- Open Rich Results Test, enter the URL, click Test URL. Prefer URL input over code input: code input has JS limitations (e.g. CORS restrictions).
- Success message: "Page is eligible for rich results" (if the type is supported by the tool).
- Type not supported by the tool: inspect rendered HTML; if it contains the markup, Google can process it.
- Errors/warnings: usually syntax error or missing property; recheck the type's docs and the fixing search-related JavaScript problems guide.

## All structured data features
https://developers.google.com/search/docs/appearance/structured-data/search-gallery · Last updated: 2026-10-16

### Gallery notes
- Structured data lets Google understand content and show rich results. Appearance may differ from gallery images; most features can be previewed in Rich Results Test.
- Page has category filters: Ecommerce, Organizations, Sports, Jobs, Entertainment, News, Food and Drink, Education and Science.
- > Note: this page lists only currently supported features. It contains no deprecated or removed features and gives no deprecation dates. The repo rule SEO-21 says FAQ and HowTo no longer produce rich results; that is not stated in these pages.

### Currently supported features (25)
- Article: news, sports or blog article; better title text, larger-than-thumbnail images (News, Sports).
- Breadcrumb: page position in site hierarchy (generic).
- Carousel: sequential list/gallery from a single site; must combine with Recipe, Course list, Restaurant or Movie (Food and Drink, Education and Science, Entertainment).
- Course list: list of courses from one provider (title, provider, short description).
- Dataset: large datasets in Google Dataset Search.
- Discussion forum: user-generated content (traditionally shorter than `Article`) plus threaded or non-threaded discussion.
- Education Q&A: education questions and answers, helps students find flashcards.
- Employer aggregate rating: aggregated evaluation of a hiring organization, shown in job search experience (Jobs).
- Event: interactive result listing events at a time and place (Entertainment).
- Image metadata: Google Images shows creator, usage rights, credit.
- Job posting: interactive job search experience; logo, reviews, ratings, details (Jobs).
- Local business: knowledge panel details, open hours, ratings, directions, booking/order actions (Organizations).
- Math solver: indicate math problem types and step-by-step solutions.
- Movie: movie carousel for lists such as "best movies of 2023" (title, director, images).
- Organization: logo, legal name, address, contact info, identifiers; knowledge panels and attribution.
- Product: price, availability, review ratings (Ecommerce).
- Profile page: page primarily about a single person or organization affiliated with the site.
- Q&A: pages in question-then-answers format.
- Recipe: individual rich result or part of a host carousel.
- Review snippet: excerpt or aggregate rating of a review; can be about Book, Recipe, Movie, Product, Software App, Local business.
- Software app: rating, description, link.
- Speakable: mark news content for text-to-speech reading on Google Assistant-enabled devices (News).
- Subscription and paywalled content: marks paywalled content so Google can distinguish it from cloaking (spam) (News).
- Vacation rental: property name, description, images, location, rating, reviews.
- Video: video results with play option, video segments, live-stream content.

### Deprecated or removed features
- None listed on this page.

## Article
https://developers.google.com/search/docs/appearance/structured-data/article · Last updated: 2026-09-08

### Overview
- Types: `Article`, `NewsArticle`, `BlogPosting` (news, blog, sports articles). Helps Google show better title text, images, date info in Search and other properties (Google News, Google Assistant).
- No markup requirement for Google News features such as Top stories; `Article` markup just states more explicitly what the content is (news article, author, title).

### How to add
- No required properties: add as many recommended properties as apply.
- Steps: add markup in a supported format; follow guidelines; validate with Rich Results Test (fix critical errors; non-critical issues optional but improve quality); deploy a few pages and check with URL Inspection (page not blocked by robots.txt, `noindex` or login), then request recrawl; allow days for recrawl; submit a sitemap (automatable via Search Console Sitemap API).
- Page examples show JSON-LD and Microdata: key lesson is multiple images in 3 aspect ratios, `datePublished`/`dateModified` with timezone offset, and each author as its own `Person` object with `name` and `url`.

### Guidelines
- Must follow: Search Essentials, general structured data guidelines, technical guidelines. Violations may lead to manual action (reconsideration request after fixing).
- Technical:
  - multi-part articles: `rel=canonical` points to each individual page or a "view-all" page, never to page 1 of the series;
  - sites with subscriptions or registration: consider subscription and paywalled content markup.

### `Article` properties (all recommended; none required)
- `author` (`Person` or `Organization`): follow author markup best practices below.
  - `author.name` (`Text`): author's name.
  - `author.url` (`URL`): page uniquely identifying the author (social profile, about, bio). If an internal profile page, recommended to mark it up with profile page structured data. `sameAs` is an alternative; Google understands both for disambiguation.
- `dateModified` (`DateTime`): last modification, ISO 8601, provide timezone (else Googlebot's timezone is assumed). Rich Results Test shows no warning when missing (only recommended if applicable).
- `datePublished` (`DateTime`): first publication, ISO 8601, same timezone advice and no-warning note.
- `headline` (`Text`): article title; keep concise as long titles may be truncated on some devices.
- `image` (repeated `ImageObject` or `URL`): representative of the article; relevant images, not logos or captions.
  - crawlable and indexable URLs; must represent the marked-up content; file format supported by Google Images;
  - best results: multiple high-resolution images, minimum 50K pixels (width x height), aspect ratios 16x9, 4x3 and 1x1.

### Author markup best practices
- Include all authors shown on the page.
- Multiple authors: one `author` entry per person; don't merge names into one `name` string.
- Strongly recommended: `@type` plus `url` (or `sameAs`) with valid URLs. Person: link to author page; Organization: link to its home page.
- `author.name` holds only the name: no publisher name (use `publisher`), no job title (`jobTitle`), no honorific prefix/suffix (`honorificPrefix`/`honorificSuffix`), no introductory words like "posted by".
- Use `Person` for people and `Organization` for organizations; never `Thing`, never the wrong type.

### Troubleshooting
- Ask CMS vendor/site owner; forward Search Console messages.
- No guarantee of rich result display (see general guidelines).
- Check structured data errors list and the Unparsable structured data report.
- A structured data manual action means the page's markup is ignored (page can still appear in results); fix via Manual Actions report.
- Re-read guidelines: problems may be spammy content or markup that the Rich Results Test can't flag.
- Use the "Troubleshoot missing rich results / drop in total rich results" guide.
- Allow days for recrawl; ask in Google Search Central forum.

## Book actions
https://developers.google.com/search/docs/appearance/structured-data/book · Last updated: 2025-12-10

### Overview and availability (limited)
- Lets users buy or borrow books from Search results/knowledge panels via `ReadAction` (buy/access) and `BorrowAction` (borrow). Links send users from the knowledge panel and other Google surfaces to your book page on site or app.
- (limited) Currently limited to book providers with a wide selection of available books, who must fill in an interest form and be onboarded; expressing interest does not guarantee participation. Feed upload is for onboarded partners only; a Google support team gives upload details.
- Provider order in the knowledge panel is personalized and dynamic (e.g. frequently clicked providers rank higher); cannot be controlled.
- Delivered as a data feed, not on-page markup.

### Guidelines
- Follow these plus general structured data guidelines and Search Essentials.
- Works vs editions:
  - Work = abstract book (title, author, original language); Edition = concrete copy (publication year, edition name, ISBN).
  - Two `Book` entities: `Book` (`Work`) top level, with `workExample` (at least one per work) pointing to `Book` (`Edition`).
  - Group editions under one work where possible; if split into several works, each needs a different `@id` and at least one edition with an ISBN or other supported identifier.
- Library systems and members (only for lenders):
  - `Library` is abstract: a `LibrarySystem` plus its `Library (member)` entities.
  - `LibrarySystem` = collaborative network (e.g. Austin Public Library with ~20 member libraries); needs at least one member even if a standalone library (then it is its own sole member).
  - Member is concrete, has a physical address, and must belong to at least one `LibrarySystem`.
- Identifiers:
  - ISBN is the main matching signal; supply an ISBN or other supported identifier for every book to be surfaced.
  - Preferred: ISBN-13. Alternatives: OCLC Number, LCCN, JP e-code.
  - ISBN-10 not accepted: convert to ISBN-13 first.
  - Books without identifier may be fed but might not surface; mitigate by grouping editions under one work with at least one identified edition, and adding OCLC Number or LCCN.
- Links:
  - duplicates: link to the canonical URL containing title and book info;
  - action links must land on a page that directly supports purchase/borrowing; no search results or product summary pages needing more clicks.

### Create, host, submit, update the feed
- Sellers upload a `Book` feed; lenders upload two separate feeds: `Book` and `Library`.
- Size/format:
  - uncompressed file under 1 GB; a file to be compressed also under 1 GB (split if larger);
  - compression allowed: zip, gz, tar, tar.gz, JAR, ar, arj, cpio, dump;
  - multiple files can be uploaded as is or listed in a sitemap index file;
  - single feed files use the `.json` extension.
- Content:
  - no stale entities (`availabilityEnds` in the past or no longer available);
  - only production deep links (`urlTemplate`) and URLs (`url`), no QA/dev URLs; all URLs canonical;
  - each entity needs a unique `@id`, unique `url`, unique `urlTemplate`.
- Validation: use the Data Feed validation tool with "Books Action" selected in Validate on; check `@type` spelling; `"@context": "https://schema.org"` for both `ReadAction` and `BorrowAction`.
- Hosting (Google fetches regularly): Google Cloud Storage (Storage Object Viewer permission); HTTPS (username+password or HTTP client certificates); SFTP (password, key+phrase, or both); AWS S3 (Key ID + Access Key).
- Review: a Google support team reviews deep-link quality; manually test links first. Provide feed host location and authentication credentials if any.
- Updates: update daily if the catalog changes that often; no real-time updates; Google fetches once a day and typically indexes within two days. For foreseeable availability changes use `availabilityStarts`/`availabilityEnds`; if no longer available, remove the entity.

### `DataFeed` entity (feed root)
- Required: `@context` (`https://schema.org`), `@type` (`DataFeed`), `dataFeedElement` (`Book` or `LibrarySystem`: single entity or array of only one kind, never mixed), `dateModified` (`DateTime`, ISO 8601, feed last update).
- Exactly one `DataFeed` at root; all `Book`/`Library` entities listed under `dataFeedElement`.

### `Book` (`Work`)
- Required: `@context` (`https://schema.org`); `@id` (globally unique, stable, URL format suggested but not required, need not resolve; domain must be owned by you); `@type` (`Book`); `author` (`Person` or `Organization`; if none, use contributors per schema.org/Book, e.g. editors; organization authors typed as `Organization`); `name` (title); `url` (page introducing the book, used for reconciliation; may equal `workExample.target.urlTemplate`, which is the actual landing page); `workExample` (`Book` Edition(s)).
- Recommended: `sameAs` (`URL`: Wikipedia, Wikidata, VIAF, Library of Congress page).

### `Book` (`Edition`)
- Required:
  - `@id` (same rules as work);
  - `@type` (`Book`);
  - `bookFormat` (enum: `https://schema.org/AudiobookFormat`, `https://schema.org/EBook`, `https://schema.org/Hardcover`, `https://schema.org/Paperback`);
  - `inLanguage` (ISO 639-1 alpha-2 code);
  - `isbn` (ISBN-13; convert ISBN-10);
  - `potentialAction` (`ReadAction` or `BorrowAction`).
- Recommended:
  - `author` (only if different from the work's author);
  - `bookEdition` (e.g. `2nd Edition`);
  - `datePublished` (`Date`, `YYYY-MM-DD` or `YYYY`);
  - `identifier` (`PropertyValue`, repeatable);
  - `name` (only if different from the work title);
  - `sameAs` (reference page for this edition; don't reuse the work's);
  - `url` (edition page; may equal `workExample.target.urlTemplate`).

### `author` (`Person` or `Organization`)
- Required: `@type` (`Person` or `Organization`), `name`. Recommended: `sameAs` (`URL`). Multiple authors allowed as array.

### `PropertyValue` (`identifier`)
- Required: `@type` (`PropertyValue`); `propertyID` (`OCLC_NUMBER`, `LCCN` or `JP_E-CODE`); `value` (`Text`, external ID with all non-numeric prefixes removed).

### `ReadAction` (`potentialAction`)
- Defines deep links, retailer and access criteria (membership, login, location).
- Required:
  - `@type` (`ReadAction`);
  - `expectsAcceptanceOf` (`Offer`, repeatable; a user matching any Offer may access), with `@type` (`Offer`) and `category` (one of `nologinrequired`, `free` (needs login but no purchase/paid subscription), `subscription`, `purchase`, `rental` (finite time after purchase));
  - `expectsAcceptanceOf.eligibleRegion` (`Country`, repeatable; `@type` `Country`, `name` = ISO 3166-1 alpha-2 code);
  - `target` (`EntryPoint`, repeatable for different platform sets), with `@type` (`EntryPoint`), `actionPlatform` (repeatable: `https://schema.org/DesktopWebPlatform`, `https://schema.org/AndroidPlatform`, `https://schema.org/IOSPlatform`) and `urlTemplate` (`URL`, deep link to the book landing page).
- Recommended: `expectsAcceptanceOf.availabilityStarts` / `availabilityEnds` (`DateTime`, exact exposure window); `expectsAcceptanceOf.price` (`Number`, required when category is `purchase` or `rental`); `expectsAcceptanceOf.priceCurrency` (ISO 4217, 3 letters).
- > Note: the page's own examples use inconsistent category casing (`noLoginRequired`, `Subscription`) versus the documented lowercase values.

### `BorrowAction` (`potentialAction`)
- Required: `@type` (`BorrowAction`); `lender` (`LibrarySystem`) with `lender.@type` (`LibrarySystem`) and `lender.@id` (reference to the system fully described in the separate Library feed); `target` (`EntryPoint`, repeatable) with the same `@type`, `actionPlatform` and `urlTemplate` rules as `ReadAction`.
- No recommended properties listed.

### `Library` feed
- Separate from the `Book` feed.
- `LibrarySystem` required: `@context`, `@id` (URL, stable, opaque, domain owned by you), `@type` (`LibrarySystem`), `additionalProperty` (`PropertyValue` with `name` = `librarytype` and `value` one of `public`, `academic`, `corporate`, `government`, `school`, `special`), `member` (`Library`), `name`, `url` (reconciliation link; the actual landing page comes from `workExample.target.urlTemplate`).
- `Library` (`member`) required: `@id`, `@type` (`Library`), `name`, `location` (`PostalAddress`) with `addressCountry` (ISO 3166-1, e.g. `US`), `addressLocality`, `addressRegion`, `postalCode`, `streetAddress`. Include as many address properties as apply to the country (Japan example omits `addressRegion`).

## Breadcrumb
https://developers.google.com/search/docs/appearance/structured-data/breadcrumb · Last updated: 2026-09-08

### Overview and availability
- `BreadcrumbList` shows page position in site hierarchy; users can move up one level at a time from the last crumb.
- Availability: desktop, in all regions and languages where Google Search is available.

### How to add
- Same flow as other types: add required properties, follow guidelines, validate with Rich Results Test, deploy a few pages and check URL Inspection (not blocked by robots.txt, `noindex` or login), request recrawl, submit a sitemap.

### Examples (key lessons)
- Google uses breadcrumb markup to categorize the page within the context of the query; different queries can reach the same page via different trails.
- Single trail: a `BreadcrumbList` with 3 `ListItem`s; last item (current page) may omit `item`. Formats shown: JSON-LD, RDFa, Microdata, plus a plain HTML breadcrumb block as part of the visual design.
- Multiple trails: a page reachable several ways can carry several `BreadcrumbList`s (JSON-LD array, or separate `<ol>` blocks in RDFa/Microdata).

### Guidelines
- Follow Search Essentials and general structured data guidelines. Markup outside the guidelines may trigger a manual action.
- Recommended: breadcrumbs represent a typical user path to the page, not mirror the URL structure.
- Not required: a `ListItem` for the top level (domain/host) or for the page itself.
- `BreadcrumbList` must contain at least two `ListItem`s.
- `data-vocabulary.org` markup is no longer eligible.

### `BreadcrumbList` (container)
- Required: `itemListElement` (array of `ListItem`s in order).

### `ListItem`
- Required:
  - `item` (`URL` or `Thing` subtype): URL of the breadcrumb's page. As `Thing`, set the URL via `@id` (JSON-LD), `href` or `itemid` (Microdata), `about`/`href`/`resource` (RDFa). Not required on the last item; if omitted Google uses the containing page's URL.
  - `name` (`Text`): breadcrumb title shown to users; not required if `item` is a `Thing` with its own `name`.
  - `position` (`Integer`): 1 = start of trail.

### Monitoring with Search Console
- Check after first deployment, after new templates/code changes, and periodically.
- First deployment: use the relevant Rich result status report once indexed; expect valid items up, invalid items not up. Fix invalid items, inspect the live URL, then request validation in the report.
- After template releases: rise in invalid items = broken template or bad interaction; drop in valid items without matching rise in invalid = markup no longer embedded (diagnose with URL Inspection).
- Periodically: Performance report (impressions, clicks, average position of rich result appearances); also via Search Console API.

### Troubleshooting
- Same resource list as Article (CMS help, no display guarantee, errors list and Unparsable structured data report, manual action means markup ignored, review guidelines for spammy content, missing/dropped rich results guide, allow days to recrawl, forum).

## Carousel
https://developers.google.com/search/docs/appearance/structured-data/carousel · Last updated: 2026-09-08

### Overview
- Host carousel: swipeable (mobile) list of cards from the same site, via `ItemList` combined with one of: Course list, Movie, Recipe, Restaurant.
- Carousels like Top stories (multiple sites) cannot be controlled with this markup.

### Choosing page structure
- Summary page + multiple detail pages: summary lists short descriptions each linking to a detail page focused on one item (e.g. best cookie recipes linking to full recipes).
- Single all-in-one-page list: one page with full text of every item (e.g. top movies of a year), no detail pages.
- Also: add required properties; add required and recommended properties of the underlying type (Course, Movie, Recipe, Restaurant); follow guidelines; validate; deploy and use URL Inspection; submit sitemap.

### Summary page pattern
- `ItemList`; each `ListItem` has only `@type` (`ListItem`), `position`, `url` (page with full details).
- Each detail page carries the full structured data of the specific type (e.g. `Recipe`).

### All-in-one-page pattern
- Each `ListItem` has `position` and `item`; `item` carries the full type markup (the example uses `Movie` with `name`, `url` anchor, image, director, review, aggregateRating).
- Key lesson: item `url` is the current page plus an anchor.

### Guidelines
- Follow Search Essentials and general structured data guidelines, plus:
  - all items the same type (e.g. only `Recipe`), no mixing;
  - markup must be complete and contain all items listed on the page;
  - visible text must be similar to the structured data;
  - items appear in `position` order.

### Validate and deploy
- Rich Results Test; for a summary page also verify manually: `itemListElement` has 2+ `ListItem`s; all same type; validate each linked URL with Rich Results Test, each page valid per its content type docs (Recipe, Course, Restaurant, Movie).
- Deploy a few pages, URL Inspection, recrawl, sitemap (as elsewhere).

### `ItemList`
- Required: `itemListElement` (`ListItem`, at least two, same type).
- Summary page: all URLs point to different pages on the same domain. All-in-one page: all URLs point to an anchor on the hosting page.

### `ListItem`, summary page
- Required: `position` (`Integer`, 1-based); `url` (`URL`, canonical URL of the detail page; unique; same domain or sub/super domain as the current page).
- Include only `type`, `position`, `url`.

### `ListItem`, all-in-one page
- Required:
  - `position` (`Integer`, 1-based);
  - `item` (`Thing`): all properties of the specific type (Course, Movie, Recipe, Restaurant) including those it requires (e.g. a recipe needs `prepTime`, `image`), plus:
    - `item.name` (`Text`): shown as the card title; HTML formatting ignored;
    - `item.url` (`URL`): fully-qualified current-page URL plus an HTML anchor (`<a>`, `name` or `id`) near the visible text, e.g. `https://example.org/recipes/pies#apple_pie`.

### Troubleshooting
- Same resource list as Article.
