# Structured data feature guides: Course list, Dataset, Discussion forum, Education Q&A, Employer aggregate rating, Fact check, Event, Image metadata, Job posting: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

> Shared boilerplate (appears on every page below unless noted): "How to add structured data" workflow, Rich Results Test, URL Inspection, sitemap, Rich result status reports, Troubleshooting. It is documented once here to avoid repetition.
>
> - Workflow: add required properties in the chosen format (CMS plugin or JavaScript generation are options) → follow the guidelines → validate with the Rich Results Test and fix critical errors (non-critical issues are optional, not needed for eligibility) → deploy a few pages and check them with URL Inspection (page must not be blocked by robots.txt, `noindex` or a login) → request recrawl → submit a sitemap (can be automated with the Search Console Sitemap API). Recrawl/reindex can take several days.
> - Monitoring (Event, Dataset, Discussion forum, Education Q&A, Fact check pages): check Search Console after first deployment (valid items should rise, invalid items should not; fix, inspect the live URL, request validation), after new templates or code changes (rise in invalid items means a broken template; a drop in valid items without a rise in invalid ones means markup is no longer embedded; use URL Inspection), and periodically in the Performance report (impressions, clicks, average position as rich result; also available through the Search Console API).
> - Troubleshooting (all pages): ask the CMS owner and forward Search Console messages; Google does not guarantee rich results even with valid markup (see General Structured Data Guidelines); check structured data errors and the Unparsable structured data report; a structured data manual action makes Google ignore the page's structured data (the page can still rank), fix via the Manual Actions report; re-read the guidelines because spammy content or spammy markup is not detected by the Rich Results Test; use the "Troubleshoot missing rich results / drop in total rich results" guide; allow time for recrawl; ask in the Google Search Central forum.

## Course list (`Course`) structured data
https://developers.google.com/search/docs/appearance/structured-data/course · Last updated: 2026-09-08

### Overview and availability
- Course list structured data gives details (course name, provider, short description) so prospective students find courses; shown as a list of courses from one site.
- Availability: English, all regions where Google Search is available.

### Page setups (examples)
- Summary page + detail pages: each detail page carries a `Course`; the summary page carries the `ItemList`.
- All-in-one page: one `ItemList` whose `ListItem.item` entries are `Course` objects, each with `url`, `name`, `description`, `provider` (`Organization` with `name`, `sameAs`).
- Rich Results Test may show errors for other rich result types; only warnings/errors in the "Course list item" section (single detail page) or "Course list item" and "Carousels" sections (all-in-one) matter.

```json
{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":1,
 "item":{"@type":"Course","url":"…#intro","name":"…","description":"…","provider":{"@type":"Organization","name":"…","sameAs":"…"}}}]}
```

### Guidelines
- Must follow: content, technical and Carousel guidelines, Search Essentials, general structured data guidelines. Violations can trigger a manual action; fix then request reconsideration.
- Content: use `Course` only for educational content that is a series or unit of curriculum with lectures, lessons or modules on a subject. It needs an explicit educational outcome (knowledge or skill) and is led by one or more instructors with a roster of students. Not courses: a public event such as "Astronomy Day"; a single 2-minute how-to video.
- Technical: mark up at least 3 courses (separate detail pages or all-in-one). Carousel (`ItemList`) markup is required on the summary page or the all-in-one page. Each course needs valid `name` and `provider`.
- Invalid names: promotional phrases ("Best school in the world"), prices in titles ("only $30!"), non-course titles ("Make money fast with this class!"), discounts or purchase offers ("25% off").

### `Course` properties
- Required: `description` (`Text`, display limit 60 characters), `name` (`Text`, course title).
- Recommended: `provider` (`Organization`, publisher of the course's source content, e.g. UC Berkeley).

### `ItemList` properties (summary or all-in-one page)
- Required: `itemListElement` (`ListItem`), `ListItem.position` (`Integer`, ordinal position), `ListItem.url` (`URL`, canonical URL of the item page; every item needs a unique URL).

> Note: the page lists `provider` as recommended but its technical guidelines require "valid name and provider"; treat `provider` as required in practice. The all-in-one example puts `url` on the nested `Course` rather than on `ListItem`.

## Dataset (`Dataset`, `DataCatalog`, `DataDownload`) structured data
https://developers.google.com/search/docs/appearance/structured-data/dataset · Last updated: 2026-09-08

### Overview
- Markup improves discovery in Dataset Search (life sciences, social sciences, machine learning, civic/government data and more). Appearance may differ from previews; most features can be previewed in the Rich Results Test.
- What qualifies as a dataset: a table or CSV; an organized collection of tables; a proprietary-format data file; a collection of files forming one dataset; a structured object loadable into a processing tool; images capturing data; machine-learning files (trained parameters, network structure definitions).
- Remove a dataset from Dataset Search with the robots `meta` tag; changes take days or weeks depending on crawl schedule.

### Approach to dataset discovery
- Understands schema.org `Dataset` markup or equivalent W3C DCAT structures. CSVW support is experimental. JSON-LD with schema.org is preferred; RDFa 1.1 and Microdata are also possible. DCAT in RDFa is not supported by the Rich Results Test.

### Guidelines
- Follow general structured data guidelines plus the best practices below.
- Sitemap: use a sitemap to help Google find URLs. Put dataset markup on canonical "landing" pages, not on list/search pages. If markup appears on multiple copies (e.g. in search result listings), link the canonical page with `sameAs`. Not every mention needs markup, but use `sameAs` if you do.
- Source and provenance: `sameAs` for simple republication, pointing to the most canonical original URL (value must unambiguously identify one dataset; never reuse the same `sameAs` for two datasets); `isBasedOn` when a republished dataset changed significantly or derives from/aggregates several originals; `identifier` for DOIs or Compact Identifiers (repeat the property or use a JSON array for several).
- Text properties: keep all under 5000 characters; Dataset Search only uses the first 5000. Names and titles are normally short.
- Known validator noise: validators may demand organization contact info with `contactType` (useful values: `customer service`, `emergency`, `journalist`, `newsroom`, `public engagement`); ignore errors about `csvw:Table` as an unexpected `mainEntity` value.
- Metadata only: describe what the dataset is about, which variables it measures and who made it, not the data values.

### `Dataset` properties
- Required:
  - `description` (`Text`): 50 to 5000 characters; Markdown allowed (embedded images need absolute URLs); in JSON-LD denote newlines with `\n`.
  - `name` (`Text`): descriptive; unique for distinct datasets (e.g. "Snow depth in the Northern Hemisphere" vs "... Southern Hemisphere", not "Snow depth" twice).
- Recommended:
  - `alternateName` (`Text`): aliases/abbreviations; repeatable.
  - `creator` (`Person` or `Organization`): use ORCID as `sameAs` for people, ROR ID for organizations.
  - `citation` (`Text` or `CreativeWork`): related academic articles recommended for citation (data paper, descriptor), not citation for the dataset itself (use `name`, `identifier`, `creator`, `publisher` for that). Include an article identifier such as a DOI when giving a text snippet.
  - `funder` (`Person` or `Organization`): ORCID/ROR as above.
  - `hasPart` / `isPartOf` (`URL` or `Dataset`): collection and sub-dataset relationship. A `Dataset` value must contain all properties required for a standalone dataset.
  - `identifier` (`URL`, `Text` or `PropertyValue`): DOI or Compact Identifier.
  - `isAccessibleForFree` (`Boolean`).
  - `keywords` (`Text`).
  - `license` (`URL` or `CreativeWork`): use a URL that identifies a specific license version (`.../licenses/by/4.0`, not `.../licenses/by`); custom license as `CreativeWork` with `name`, `url`.
  - `measurementTechnique` (`Text` or `URL`): proposed at schema.org, pending standardization.
  - `sameAs` (`URL`): reference page that unambiguously identifies the dataset.
  - `spatialCoverage` (`Text` or `Place`): only if the dataset has a spatial dimension; point (`GeoCoordinates`), shape (`GeoShape` with `box`, `circle`, `line`, `polygon`) or a named location string. Points inside shapes are space-separated "latitude longitude" (that order).
  - `temporalCoverage` (`Text`): only if temporal; ISO 8601; single date `2008`, interval `1950-01-01/2013-12-18`, open-ended `2013-12-19/..`.
  - `variableMeasured` (`Text` or `PropertyValue`): proposed at schema.org, pending standardization.
  - `version` (`Text` or `Number`).
  - `url` (`URL`): page describing the dataset.

### `DataCatalog`
- Recommended: `includedInDataCatalog` (`DataCatalog`), the repository catalog the dataset belongs to. A dataset can be in several catalogs.

### `DataDownload`
- `distribution` describes where to get the data and in what format (the `url` usually points to a landing page); can hold several values (e.g. CSV at one URL, Excel at another).
- Required: `distribution.contentUrl` (`URL`, download link).
- Recommended: `distribution` (`DataDownload`), `distribution.encodingFormat` (`Text` or `URL`, file format).

### Tabular datasets (beta)
- Pages embedding tabular data can add CSVW ("CSV on the Web") JSON-LD in parallel to the visible table, via `mainEntity` of type `csvw:Table` with `csvw:tableSchema` / `csvw:columns` (`csvw:name`, `csvw:datatype`, `csvw:cells` with `csvw:value`, optional `csvw:notes`, `csvw:primaryKey`). Known errors appear in the Rich Results Test. Subject to change.

### Troubleshooting (page-specific)
- Dataset missing from Dataset Search: no dataset markup on the page or not yet crawled. Run the URL in the Rich Results Test; "Page not eligible for rich results known by this test" or "Not all markup is eligible" means missing or incorrect markup. If markup exists, check crawl status in Search Console.
- Company logo missing or wrong: add logo structured data and establish business details with Google.

## Discussion forum (`DiscussionForumPosting`) structured data
https://developers.google.com/search/docs/appearance/structured-data/discussion-forum · Last updated: 2026-09-08

### Overview
- For forum-style sites where people share first-hand perspectives; helps Google identify discussions for features such as Discussions and Forums.
- Question-and-answer forums should use Q&A markup (`QAPage`) instead.

### Using `DiscussionForumPosting` within a forum
- Threaded forum: nest comments under the post they reply to, as a tree (`comment` inside `comment`).
- Linear forum (post plus replies): nest all replies as `comment` under the original post. On later pages of a multi-page thread, ideally still include the original post with the main page URL (`url`); only the headline needs to be present there.
- If the URL is primarily about one post, identify it with `mainEntity` (or `mainEntityOfPage`) on a `WebPage`.
- Pages listing many posts (profile, topic, category): you may include only what is on the page plus the URL of the discussion page. Do not mark one post as main entity on a page that is not that post's discussion page. Optionally group related posts in a `Collection` or `ItemList`.

### Guidelines
- Must follow: general structured data guidelines, Search Essentials, content and technical guidelines below.
- Content:
  - Use only for user-generated posts; not for content mainly authored by the site's publisher or agents.
  - `SocialMediaPosting` (parent type, same requirements) is acceptable for generic social platforms.
  - Valid: community forum page about a game; generic forum platform with many subforums; social platform with posts, replies and media. Invalid: an article or blog written by the site (even with comments); user reviews about a product.
  - Other types (`Article`, `ImageObject`, `VideoObject`) may carry similar comment/author/interaction markup but must not use `DiscussionForumPosting`.
  - A Q&A page is a special case of a forum page; if the structure is mainly questions with answers use Q&A markup, otherwise `DiscussionForumPosting`.
  - Each `DiscussionForumPosting` must include the whole post text and each `Comment` the whole response text if it is on that page.
- Technical: Microdata (or RDFa) is recommended, unlike Google's usual JSON-LD preference, because it avoids duplicating large text blocks in markup. JSON-LD remains fully supported.

### `DiscussionForumPosting` (or `SocialMediaPosting`) properties
- Required:
  - `author` (`Person` or `Organization`) and `author.name` (`Text`). Follow author markup best practices; use article and profile page properties as a guide.
  - `datePublished` (`DateTime`, ISO 8601).
  - One of `text`, `image`, `video`. Not required when representing a post whose content lives on another page (external `url`), such as later forum pages or category pages.
- Recommended:
  - `author.url` (`URL`): profile page identifying the author; mark that page up as a profile page.
  - `comment` (`Comment`): in on-page order.
  - `commentCount` (`Integer`): useful when not all comments are in markup.
  - `creativeWorkStatus` (`Text`): `Deleted` when the post is deleted but kept for context or threading.
  - `dateModified` (`DateTime`): only if edited; do not duplicate the publish date.
  - `digitalSourceType` (`IPTCDigitalSourceEnumeration`): `TrainedAlgorithmicMediaDigitalSource` (trained model, e.g. LLM) or `AlgorithmicMediaDigitalSource` (simpler algorithmic process, e.g. auto-reply bot). If absent, Google assumes human-generated.
  - `headline` (`Text`): title of the post; if no separate title, do not duplicate or truncate the text into one; not recommended for `SocialMediaPosting`.
  - `image` (`ImageObject` or `URL`): inline images only; no default, icon, placeholder or author images. A link-preview image goes in the `image` of a `WebPage` in `sharedContent`.
  - `interactionStatistic` (`InteractionCounter`): supported `interactionType` values: `https://schema.org/LikeAction` (likes/upvotes), `DislikeAction`, `ViewAction`, `CommentAction` or `ReplyAction` (comments), `ShareAction` (reshares).
  - `isPartOf` (`CreativeWork` or `URL`): subforum or group; if a `CreativeWork` such as `WebPage`, give its `url`.
  - `sharedContent` (subtype of `CreativeWork`): `WebPage` (shared link, with `url`), `ImageObject`, `VideoObject`, or `DiscussionForumPosting`/`Comment` (quoted or reposted item).
  - `text` (`Text`): may be omitted if other media carries the post.
  - `url` (`URL`): canonical URL of the discussion; in multi-page threads the first page URL.
  - `video` (`VideoObject`): inline videos.

### `Comment` properties
- Required: `author` (`Person` or `Organization`), `datePublished` (`DateTime`, ISO 8601), and one of `text`, `image`, `video`.
- Recommended: `author.url`, nested `comment` (replies, in page order), `commentCount` (comments on this comment), `creativeWorkStatus` (`Deleted`), `dateModified`, `digitalSourceType` (same values and default as above), `image` (same rules), `interactionStatistic` (same types), `sharedContent`, `url` (URL of this specific comment; omit if it would just be the post URL), `video`.

### `InteractionCounter`
- Used on posts, comments and on `author` (e.g. `agentInteractionStatistic` with `WriteAction` for the author's post count, as in the example).
- Required: `userInteractionCount` (`Integer`), `interactionType` (subtype of `Action`; valid values depend on the parent property).

## Education Q&A (`Quiz`, `Question`, `Answer`) structured data
https://developers.google.com/search/docs/appearance/structured-data/education-qa · Last updated: 2026-09-08

### Overview and availability
- `Quiz` markup on flashcard pages makes them eligible for the Q&A carousel in Google Search, Google Assistant and Google Lens.
- Eligible page types: flashcard pages (this guide); single Q&A pages with one question and user-submitted answers use `QAPage` instead.
- Only shown for education-related queries, on desktop and mobile.
- Languages/regions: English (all regions), Portuguese (all regions), Spanish (Mexico only), Vietnamese (all regions).

### Guidelines
- Must follow: general structured data guidelines, Search Essentials, technical and content guidelines.
- Technical:
  - Put markup on the most detailed leaf page; none on pages without questions.
  - All questions must use `eduQuestionType` = `Flashcard`; pages with other question types are ineligible.
  - Googlebot must be able to crawl the site efficiently.
  - Questions must be immediately visible on the page, not only in a data file or PDF.
  - One question with several user-submitted answers: use `QAPage`.
- Content: follow the Q&A page content guidelines; the page needs education-related questions and at least one question and answer pair where the answer actually answers it. The site owner is responsible for accuracy; if a certain amount of content fails quality and pedagogical review, all or a subset of Q&A pages may lose eligibility until fixed. Violations can lead to manual action and non-display.

### Educational standards (`educationalAlignment`)
- Marking up learning standards (e.g. Common Core, TEKS, Virginia SOL, BC Performance Standards, Alberta Programs of Studies, Australian Curriculum (ACARA), Victorian Curriculum F-10, UK National Curriculum) via `educationalAlignment` helps Google organize and surface content by standard.

```json
{"@type":"Quiz","about":{"@type":"Thing","name":"Cell Transport"},
 "educationalAlignment":[{"@type":"AlignmentObject","alignmentType":"educationalSubject","targetName":"Biology"}],
 "hasPart":[{"@type":"Question","eduQuestionType":"Flashcard","text":"…","acceptedAnswer":{"@type":"Answer","text":"…"}}]}
```

### `Quiz` properties
- Required: `hasPart` (`Question`), one per flashcard; repeat for multiple flashcards.
- Recommended:
  - `about` (`Thing`) and `about.name` (`Text`, underlying concept; multiple allowed).
  - `educationalAlignment` (`AlignmentObject`, repeatable).
  - `educationalAlignment.alignmentType` (`Text`; LRMI standard): `educationalSubject` for field of study, `educationalLevel` for target grade or standard; repeat to give both.
  - `educationalAlignment.targetName` (`Text`, node of an educational framework, e.g. "Grade 7: Cell Structure").

### `Question` properties (differ from `QAPage` Question requirements)
- Required: `acceptedAnswer` (`Answer`, full answer text; exactly one per `Question`), `eduQuestionType` (`Text`, fixed value `Flashcard`), `text` (`Text`, full flashcard question text).

## Employer aggregate rating (`EmployerAggregateRating`) structured data
https://developers.google.com/search/docs/appearance/structured-data/employer-rating · Last updated: 2026-09-08

### Overview
- For sites publishing user-generated ratings of hiring organizations. Gives job seekers ratings and brand placement in the enriched job search experience.
- Beta history: during beta, review snippet markup was recommended for job-search eligibility; sites with review snippet markup for this purpose should move to `EmployerAggregateRating` soon.
- Job posting pages: also add `JobPosting` markup.

### Guidelines
- Must follow to be eligible: technical, content and enriched search quality guidelines, Search Essentials, general structured data guidelines. Violations can trigger manual action; fix then request reconsideration.
- Technical:
  - Ratings must be available to users on the page carrying the markup and the presence of rating content must be immediately obvious.
  - Rate one specific hiring organization, not a category or list ("top 10 best places to work", "tech companies" are invalid).
  - Default scale is 1 to 5; any other scale is allowed if you set `bestRating` and `worstRating` (Google normalizes to 5 stars).
- Content: users must be able to post their own ratings and the site must host them; rating counts must reflect actual user ratings; the aggregate score must be accurately derived from them.

### `EmployerAggregateRating` properties
- Required:
  - `itemReviewed` (`Organization`): the rated company (with `name`, `sameAs`).
  - `ratingCount` (`Number`): total ratings on your site. At least one of `ratingCount` or `reviewCount` is required.
  - `ratingValue` (`Number` or `Text`): number, fraction or percentage ("4", "60%", "6 / 10"); scale for fractions/percentages is implied; numbers default to 1 to 5.
  - `reviewCount` (`Number`): people who gave a review with or without a rating. Same either-or rule as `ratingCount`.
- Recommended: `bestRating` (`Number`, default 5), `worstRating` (`Number`, default 1).

## Fact check (`ClaimReview`) structured data
https://developers.google.com/search/docs/appearance/structured-data/factcheck · Last updated: 2026-09-08

### Status
- (deprecated) Google is phasing out `ClaimReview` support in Google Search; the markup remains supported by the Factcheck Explorer tool. The page gives no date.
- Intended behavior (while supported): a summarized fact check can appear in results when the page ranks for the claim. The Fact Check Markup Tool can generate markup.

### Eligibility guidelines
- Google does not guarantee display; eligibility is determined algorithmically.
- Required for eligibility:
  - Several pages on the site carry `ClaimReview`.
  - Follow all structured data guidelines and Search Essentials.
  - No mismatch between markup and page content (e.g. markup says true, page says false).
  - Meet Google News General Guidelines standards for accountability, transparency, readability and site misrepresentation.
  - Have a corrections policy or a way for users to report errors.
  - Political entities' sites (campaigns, parties, elected officials) are not eligible.
  - Readers can easily identify the claims and checks in the article body and understand what was checked and concluded.
  - The claim is clearly attributed to a distinct origin separate from your site (website, public statement, social media or other traceable source).
  - Analysis is traceable and transparent about sources and methods, with citations to primary sources.

### Technical guidelines
- Single fact check rich result: exactly one `ClaimReview` per page (multiple makes the page ineligible for it).
- The page must contain at least a brief summary of the fact check and its evaluation, if not the full text.
- A given `ClaimReview` appears on only one page of your site (exceptions: variants such as mobile and desktop versions).
- Fact-check aggregators: all aggregated articles must meet the criteria and you must publish an open, public list of the fact-check sites you aggregate.

### `ClaimReview` properties
- Required:
  - `claimReviewed` (`Text`): short summary of the claim; keep under about 75 characters to limit mobile wrapping; do not include the rating.
  - `reviewRating` (`Rating`): numeric and/or textual assessment; only the textual value is currently shown. Document your rating scheme; minimally provide a number-to-text mapping for numeric scores (1 False, 2 Mostly false, 3 Half true, 4 Mostly true, 5 True).
  - `url` (`URL`): page with the full fact check article; domain must be the same as, or a subdomain of, the page hosting the `ClaimReview`. Redirects and shortened URLs are not resolved.
- Recommended:
  - `author` (`Organization` or `Person`): publisher of the fact check, not of the claim; needs at least `name` or `url` (home, contact or other suitable page). Follow author markup best practices.
  - `itemReviewed` (`Claim`): the claim. Backwards compatibility: the original launch used `CreativeWork` as `itemReviewed`; that older pattern is still supported.

### `Claim` properties (all recommended)
- `appearance` (`URL` or `CreativeWork`): where the claim appears; repeatable when several publishers report it.
- `author` (`Organization` or `Person`): author of the claim, not of the fact check; omit if the claim has no author; repeatable when several parties make essentially the same claim. Sub-properties: `name` (`Text`, required when `author` is used), `sameAs` (`URL`, recommended: home page, or Wikipedia/Wikidata entry of the claimant).
- `datePublished` (`DateTime` or `Date`): when the claim was made or entered public discourse.
- `firstAppearance` (`URL` or `CreativeWork`): where the claim first appeared. Add either `appearance` or `firstAppearance`; both are not needed.

### `Rating` properties
- Required: `alternateName` (`Text`): short human-readable truthfulness label shown in results (e.g. "True", "Mostly true"). If a longer sentence, put the meaning at the start in case of truncation.
- Recommended:
  - `bestRating` (`Number`): must be greater than `worstRating`, numeric.
  - `name` (`Text`): same as `alternateName`, used only if `alternateName` is absent; prefer `alternateName`.
  - `ratingValue` (`Number`): in the range `worstRating` to `bestRating` inclusive; integers recommended not required; closer to best means more true.
  - `worstRating` (`Number`): must be less than `bestRating`; minimum value 1.

## Event (`Event`) structured data
https://developers.google.com/search/docs/appearance/structured-data/event · Last updated: 2026-09-08

### Overview and options
- The event experience in Google Search and other products (e.g. Maps) can show logo, description and more, and aims to increase discovery and conversion.
- Three routes: (1) a third-party site that already participates in Google's event experience (ticketing, social platforms): keep posting there, no markup needed; (2) CMS users without HTML access: use a CMS plugin or the Data Highlighter; (3) editors of HTML: add structured data directly.

### Region and language availability
- Australia (English), Brazil (Portuguese), Canada (English), Germany (German), India (English), Latin America (Spanish), Spain (Spanish), United Kingdom (English), United States (English).

### Guidelines
- Must follow: technical, content, date and time guidelines, Search Essentials, general structured data guidelines. Violations can trigger manual action; fix then request reconsideration.
- Technical:
  - Target page must contain schema.org event types.
  - Each event needs a unique URL (leaf page) with markup on it. Only pages focused on a single event are supported; avoid markup on schedule or multi-event listing pages.
  - Multi-day event or ticket: give both start and end dates. Separate performances on different days with individual tickets: one `Event` per performance.
- Content:
  - Name, start date and location must accurately describe the event.
  - Not events: non-event products/services (e.g. trip packages), short-term discounts or purchase prompts ("buy tickets now", "50% off until Saturday"), business hours, coupons or vouchers.
  - Events must be bookable by the general public; membership- or invitation-only events are ineligible.
  - Spectator events whose main participants and audience are minors on school premises are ineligible.
  - Events must have a physical location; purely virtual experiences are not supported.

### Date and time guidelines
- Timezone: include the UTC/GMT offset (e.g. New York 19:00 on 5 Sept = `2019-09-05T19:00:00-04:00` in daylight time, `-05:00` in standard time). With no timezone, Google uses the timezone of `location`.
- Multi-day events: give start and end dates; omit times you do not know. Good: `2019-07-01T10:00:00-05:00` / `2019-07-26T17:00:00-05:00` or `2019-07-01` / `2019-07-26`. Bad: `T00:00:00+00:00` to `T23:59:59+00:00` placeholders.
- Event starting at a specific hour: use local time with correct offset (e.g. `2019-07-20T17:00:00-07:00`).
- All-day or unknown start hour: date only (e.g. `2019-08-15` for both `startDate` and `endDate`); never midnight placeholders such as `2019-08-15T00:00:00+00:00` or `2019-07-20T00:00:00`.
- How Google reads values: `...T00:00:00+00:00` is converted to local time at the event location (e.g. previous day 17:00 in California); `...T23:59:59+00:00` is not "end of day" unless in GMT; a date-only value means that day regardless of timezone (start: begins sometime that day in `location`; end: ends sometime that day); `...T00:00:00` with no offset means local midnight, probably wrong.

### Required properties
- `location` (`Place`): set `@type` to `Place`; add `location.address` and `location.name`.
- `location.address` (`PostalAddress`): detailed street address ("Bennelong Point, Sydney NSW 2000, Australia", not "Sydney"). Japanese addresses may be split across fields or given on one line. Best practices: for events spanning several streets give the start location and detail in `description`; with no well-defined location use the city or most representative place; for simultaneous events at several locations create separate events.
- `name` (`Text`): full title of the event. Do not use the venue name or the event type alone ("Concert"); no URLs, prices or performers; no short-term promotions or all-caps sales text; highlight a unique aspect (e.g. "feat. Q&A with the artist").
- `startDate` (`DateTime`, ISO 8601): include date and time so users can fit it into their schedule; follow the date and time guidelines.

### Recommended properties
- `description` (`Text`): clear, concise, event-specific; do not repeat date and location; focus on the event, not site features. Google shows only a snippet.
- `endDate` (`DateTime`): same format as `startDate`.
- `eventStatus` (`EventStatusType`): default is `EventScheduled` if omitted; multiple statuses allowed. Never remove `startDate` when the status changes (it identifies the unique event).
  - `EventCancelled`: keep all other values (`startDate`, `location` etc.) unchanged and only set the status.
  - `EventPostponed`: new date unknown; keep the original `startDate` until known, then switch to `EventRescheduled` and update `startDate` and `endDate`.
  - `EventRescheduled`: update `startDate` and `endDate`; optionally set the status and add `previousStartDate`.
  - `EventScheduled`: the default.
- `image` (repeated `ImageObject` or `URL`): crawlable and indexable URLs (check with URL Inspection), representing the event, in a format supported by Google Images. Recommended 1920 px wide (minimum width 720 px). Best results: multiple high-resolution images (at least 50K pixels, width x height) in 16x9, 4x3 and 1x1 ratios.
- `location.name` (`Text`): venue name only for physical locations (not "San Francisco, CA", not the event title); no city name unless the event is city-wide; omit if the venue name is unknown.
- `offers` (`Offer`): one per ticket type.
  - `offers.availability`: `InStock`, `SoldOut` or `PreOrder`. If tickets are not yet on sale to the public, omit it and give `validFrom`.
  - `offers.price` (`Number`): lowest available price including service charges and fees; update as prices change or tickets sell out; `0` if free.
  - `offers.priceCurrency` (`Text`): 3-letter ISO 4217.
  - `offers.validFrom` (`DateTime`): when tickets go on sale (needed only for date-restricted offers).
  - `offers.url` (`URL`): landing page that clearly and predominantly offers tickets to that event for the general public; must be linkable from the event page and crawlable by Googlebot (not blocked by robots.txt).
- `organizer` (`Organization` or `Person`) with `organizer.name` (`Text`) and `organizer.url` (`URL`, host's domain): encouraged if `organizer` is used.
- `performer` (`Person` or `PerformingGroup`, one per performer) with `performer.name` (`Text`).
- `previousStartDate` (`DateTime`): only with `eventStatus` = `EventRescheduled` (no other status); `startDate` must then hold only the new date; repeatable for multiply rescheduled events.

### Troubleshooting (page-specific)
- Location missing or incorrect: Google must match the values to a real place. Ensure values are present for the location properties and that `location.name` holds the venue, not the event name. Validate with Rich Results Test > fetch URL > Validate > Preview; the preview should show the right location ("false" means the location is not real).
- Not offered as a ticket source: `offers.url` missing or not meeting the requirements; fix, ask Google to recrawl, request (re)evaluation.
- Wrong time/date: missing timezone offset or midnight placeholders. If the offset is unknown, omit it entirely (e.g. `2019-08-15T19:00:00`); use date only for all-day or unannounced-time events.
- Manual action "Spammy Structured Markup", or event not appearing: fix common issues, check the Event FAQ or the forum.

> Note: the troubleshooting text refers to an `eventLocation` property, but the properties tables and examples use `location`. Use `location`.

## Image metadata in Google Images
https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata · Last updated: 2025-12-10

### Overview and availability
- Image metadata lets Google Images show creator, usage terms and credit; license data can earn the Licensable badge (link to license plus how to use the image).
- Available on mobile and desktop in all regions and languages where Google Search is available.

### Prepare pages and images
- Pages must be viewable without an account or login.
- Googlebot must access pages containing images (not blocked by robots.txt or robots `meta`); check blocked pages in the Page Indexing report or with URL Inspection.
- Follow Search Essentials and image SEO best practices; submit a sitemap (Search Console Sitemap API can automate it).

### Two ways to supply metadata
- Structured data: ties the image to the page where it appears; must be added for every instance of an image, including the same image on several pages.
- IPTC photo metadata: embedded in the image file, travels with it; embed once per image.
- One method is sufficient for enhancements like the Licensable badge. If both are used and conflict, Google uses the structured data.
- Displayed license links come from: `license` (or IPTC Web Statement of Rights) = license page URL; `acquireLicensePage` (or IPTC Licensor URL) = page about how to license the image.
- Structured data validation: General structured data guidelines and Rich Results Test (the page does not apply the usual "fix non-critical issues" wording here).

### Examples (key lessons)
- Supported syntaxes: JSON-LD, RDFa, Microdata, each on `ImageObject`.
- Single image, image in `srcset`, and multiple images per page: each image gets its own `ImageObject` (JSON-LD uses an array on multi-image pages). With `srcset`, `contentUrl` points to one chosen file (the example uses the `src` fallback URL).
- The visible page repeats the license link, how-to-use link, photographer, copyright and credit.

### `ImageObject` properties
- Required:
  - `contentUrl` (`URL`): the image file; how Google decides which image the metadata applies to. `url` is also accepted if `contentUrl` is absent (less precise; older markup).
  - At least one of `creator`, `creditText`, `copyrightNotice`, `license`. After one is present, the other three become recommended in the Rich Results Test.
- Recommended:
  - `acquireLicensePage` (`URL`): e.g. a checkout page (resolutions/usage rights) or a contact page.
  - `creator` (`Organization` or `Person`) with `creator.name` (`Text`): usually the photographer; may be a company.
  - `creditText` (`Text`): who is credited when published.
  - `copyrightNotice` (`Text`): current copyright owner.
  - `license` (`URL`): page describing the usage license (site terms or a Creative Commons license such as BY-NC 4.0). With structured data, `license` is required for the Licensable badge; add `acquireLicensePage` too if available.

### IPTC photo metadata fields Google extracts (all recommended)
- Copyright Notice; Creator; Credit Line.
- Digital Source Type (IPTC NewsCodes): `trainedAlgorithmicMedia`, `compositeSynthetic`, `algorithmicMedia`, `compositeWithTrainedAlgorithmicMedia`.
- Licensor URL (must be a property of a Licensor object, not of the image object): license/contact info page.
- Web Statement of Rights: license URL; required for the Licensable badge, add Licensor URL too if available.
- Use metadata management software to manage IPTC data.

### C2PA metadata
- If an image contains C2PA metadata, Google may show details (how it was created, AI editing) in "About this image". The signer (app, device or service) must have adopted C2PA 2.1 or later, and the manifest must be signed with a certificate from a Certification Authority on the C2PA Trust List.

### Troubleshooting
- Google does not guarantee display of structured data or IPTC metadata. Resources: Image License FAQ, structured data error list, Manual Actions report (structured data manual action means markup is ignored), guidelines review, missing rich results guide, crawling/indexing FAQ, Search Central office hours and forum (IPTC help also on the IPTC forum).

### Removing image metadata
- Stripping metadata shrinks files and speeds pages, but may be illegal in some jurisdictions and removes rights information. Google recommends keeping at least rights and identification metadata; where possible keep IPTC `creator`, `credit line` and `copyright notice`.

## Job posting (`JobPosting`) structured data for Job Search
https://developers.google.com/search/docs/appearance/structured-data/job-posting · Last updated: 2026-09-08

### Overview
- `JobPosting` markup makes postings eligible for the Google job search experience (logo, reviews, ratings, job details; filtering by location or title). A third-party job site integration is an alternative route.
- Sites with employer reviews: also add `EmployerAggregateRating`.

### How to add structured data (job-specific workflow)
- Googlebot must be able to crawl efficiently.
- Several copies of one posting under different URLs: use canonical URLs on each copy.
- Add required and recommended properties; follow technical guidelines and job posting content policies; validate with the Rich Results Test (and preview in Search); deploy a few pages and inspect them.
- Keep Google informed with the Indexing API and a sitemap.

### Indexing API and sitemap usage (job posting URLs)
- Recommendation: use the Indexing API rather than sitemaps for job posting URLs, because it prompts Googlebot to crawl sooner. Use it to notify Google of a new URL to crawl or that content at a URL changed, and to request removal of a job posting URL from the Google index.
- Still submit a sitemap for coverage of the whole site. Google ingests the entire sitemap and recrawls pages whose `lastmod` is more recent than the last crawl.
- Removal: the Indexing API prompts a faster crawl than removing the URL from the sitemap; use it together with one of the expiry actions below.
- Indexing API request-format, endpoint, authentication, quota and eligibility details are not on this page.
- If using sitemaps for job URLs, follow the general sitemap guidelines plus:
  - URLs must be reachable by Googlebot (not behind a firewall or disallowed in robots.txt).
  - `<lastmod>` (sitemap), `<pubDate>` (RSS) or `<updated>` (Atom) must be as accurate as possible: the last time the content at the URL changed. Accurate times save limited crawl bandwidth and reduce server load.
  - Do not include search results pages, list pages or other dynamic pages.
  - Include the canonical page for each job posting.

### Examples (key lessons)
- Standard posting: `title`, `description` (HTML), `identifier` (`PropertyValue` with `name`, `value`), `datePosted`, `validThrough`, `employmentType`, `hiringOrganization` (`name`, `sameAs`, `logo`), `jobLocation` (`Place` with full `PostalAddress`), `baseSalary` (`MonetaryAmount` with `currency` and `QuantitativeValue` `value` + `unitText`).
- Work from home: replace `jobLocation` with `applicantLocationRequirements` (`Country`) and `jobLocationType` = `TELECOMMUTE`.
- Beta example adds `educationRequirements` (`EducationalOccupationalCredential`) and `experienceRequirements` (`OccupationalExperienceRequirements` with `monthsOfExperience`).

### Remove a job posting
- Jobs no longer open must be expired; failing to act in time may cause a manual action. Do one of:
  - Populate `validThrough` with a past date.
  - Remove the page so it returns `404` or `410`.
  - Remove the `JobPosting` markup from the page.
- Also notify Google through the Indexing API (see above); keep submitting the sitemap.

### Mark up work from home jobs
- Feature appearance may differ and may not show in your region immediately; mark up remote jobs in advance to be eligible. Related search: "Work from home jobs".
- Three properties: `jobLocationType` (flags work-from-home), `applicantLocationRequirements` (geography where employees may live; at least one country required), `jobLocation` (physical place the job can be done; omit if there is none; `addressCountry` required when used).
- Scenarios: home work with geographic restriction and no office: `applicantLocationRequirements` + `jobLocationType`; physical site (e.g. Detroit) or home in the US: `jobLocation` + `jobLocationType`; physical site in Detroit or home in Michigan or Texas: `jobLocation` + `jobLocationType` + `applicantLocationRequirements` as an array of `State` values ("Michigan, USA", "Texas, USA").

### Company logo
- Google uses the same logo for postings as the company's Knowledge Graph card. Suggest a change or state the preferred logo in structured data (Google usually reviews requests within a few days).
- Third-party job sites may supply a different logo per organization through `hiringOrganization.logo`; Google picks the best logo (knowledge panel or markup). That `logo` is only eligible on your job site and is not the organization's canonical logo.

### Technical guidelines
- Put markup on the most detailed leaf page for one job; never on list or search results pages.
- Add a `JobPosting` for each posting you want to advertise; markup must be on the same page as the job description visible in the browser.
- Most properties may appear once only unless stated as repeatable.
- Sitemap guidelines: see "Indexing API and sitemap usage".

### Job posting content policies
- General structured data guidelines and spam policies also apply. Violations may lead to manual action and removal from job search.
- Irrelevant content: `JobPosting` only on pages with a single job posting, never on pages listing no job or other pages.
- Incomplete content: incomplete descriptions not allowed.
- Misrepresentation: no impersonation, deception or fraud, no false affiliation or endorsement, no multiple accounts to evade policies. Violations include: inaccurate employer representation; fake jobs or jobs whose main aim is collecting applicant data; keyword stuffing in titles or descriptions; false location data; postings for an organization without authorization.
- Profanity: obscene, profane or offensive language not allowed.
- Disguised ads: promotional content (e.g. affiliate programs) posing as jobs not allowed.
- Legal removal requests: complaints about legality are handled per Search policies.
- Expired jobs: not allowed; ideally remove them, otherwise ensure `validThrough` is populated and past.
- No way to apply: not allowed; includes career-fair invitations and postings requiring login to view the description.
- Resume collection: only for open positions; solicitations for non-hiring roles may be removed.
- Job requests: postings must describe an open position and qualifications; applicants offering to work are not allowed.
- Payment required: postings that require payment from applicants not allowed.
- Editorial: no obstructive text or images, excessive or distracting ads, or valueless content. Grammar must be correct for the language (proper capitalization, no all-caps), and only widely understood acronyms.

### `JobPosting` required properties
- `datePosted` (`Date`): original posting date, ISO 8601 (`2017-01-24` or `2017-01-24T19:33:17+00:00`).
- `description` (`Text`): full job description in HTML; must be complete (responsibilities, qualifications, skills, working hours, education and experience requirements) and not identical to `title`. At minimum use paragraph breaks (`<br>`, `<p>` or `\n`). Recognized tags: `<p>`, `<ul>`, `<li>`. Headings and character-level tags (`<h1>`, `<strong>`, `<em>`) are not recognized but harmless.
- `hiringOrganization` (`Organization`): company name (not the specific location, e.g. "Starbucks, Inc" not "Starbucks on Main Street"); use `confidential` as `name` for anonymous employers (e.g. staffing agencies, direct employers on your platform). Third-party sites may add `logo`; image width/height ratio must be between 0.75 and 2.5; follow logo image and company logo guidelines.
- `jobLocation` (`Place`): physical place where the employee reports (office or worksite), not where the job was posted; include as many address properties as possible; `addressCountry` is mandatory. Multiple locations: array of `jobLocation`; Google picks the best to display for the query. For 100% remote jobs, use `jobLocationType`; `jobLocation` is not required if `applicantLocationRequirements` is present.
- `title` (`Text`): job title only (not the posting title). Do not include job codes, addresses, dates, salaries or company names. Concise, readable; avoid special-character abuse (`!`, `*`; numbers, `/` and `-` are fine), which can be treated as Spammy Structured Markup. Do not use `name` instead of `title`. Third-party sites must pass the title as received from the employer, not rewrite it.

### `JobPosting` recommended properties
- `applicantLocationRequirements` (`AdministrativeArea`): where remote workers may live; the description must clearly state the geographic restriction. Required if applicants may be in specific places and the job is 100% remote.
- `baseSalary` (`MonetaryAmount`): actual base salary from the employer, not an estimate; only employers may provide it. `QuantitativeValue.unitText` (case-sensitive): `HOUR`, `DAY`, `WEEK`, `MONTH`, `YEAR`. A range uses `minValue` and `maxValue` instead of `value`. Salary in markup must also be visible on the page.
- `directApply` (`Boolean`): whether the URL enables direct application. Effects in Search may not be visible yet. Direct apply means a short, simple process without extra steps: no more than one click on apply, one application form or one sign-in; typical cases: application completed on your site; instructions to contact the hiring company or its representative directly (email, phone, address) or schedule an interview.
- `employmentType` (`Text`, case-sensitive, may be repeated or an array): `FULL_TIME`, `PART_TIME`, `CONTRACTOR`, `TEMPORARY`, `INTERN`, `VOLUNTEER`, `PER_DIEM`, `OTHER`.
- `identifier` (`PropertyValue`): employer's unique job ID (`name`, `value`).
- `jobLocationType` (`Text`): `TELECOMMUTE` for jobs that may or must be 100% remote; the description must say so; required for 100% remote jobs. Do not use for occasional work-from-home, negotiable remote benefits or hybrid arrangements; the gig nature of a job says nothing about being remote. Requires at least one eligible country via `applicantLocationRequirements` (preferred) or, if the job can also be done at a physical site, a default to the `jobLocation` country (Google shows such remote jobs to anyone in that country). `TELECOMMUTE` as `additionalProperty` of `jobLocation` is still supported (no immediate deprecation plans) but the new schema is preferred.
- `validThrough` (`DateTime`): ISO 8601 expiry; required for postings that have an expiration date. Omit if the job never expires or the date is unknown. If the job is filled before expiry, remove the posting.

### Education and experience properties (beta)
- Beta: Google is still developing use of these; effect in Search may not be visible.
- `educationRequirements` (`EducationalOccupationalCredential` or `Text`): use `no requirements` if none; omit if unknown; repeatable (array). Sub-property `credentialCategory` (`Text`): `high school`, `associate degree`, `bachelor degree`, `professional certificate`, `postgraduate degree` (pick the closest equivalent per country). Keep describing education in `description` too.
- `experienceRequirements` (`OccupationalExperienceRequirements` or `Text`): use `no requirements` if none. Sub-property `monthsOfExperience` (`Number`): minimum months; with alternatives ("12 months chef or 24 months sous chef") use the lowest minimum (12); with combined requirements ("and") use the highest (24). Keep describing experience in `description` too.
- `experienceInPlaceOfEducation` (`Boolean`): `true` means experience can replace formal education; then both `experienceRequirements` and `educationRequirements` must be present.

### Troubleshooting (page-specific)
- Structured data on the wrong page (Search Console message: "A list page should not include structured data for individual jobs"): remove `JobPosting` from list/search pages, keep only single-job pages, then request reconsideration.
- Content does not match markup (message: "Content on pages found to be different than structured data on the page"): e.g. title mismatch, clickbait, fake or unrepresentative job, or salary only in markup. Align markup with content, confirm content is visible in the rendered page via URL Inspection, request reconsideration.
- Expired jobs still live (message: "JobPosting structured data on expired job"): causes are missing or non-past `validThrough`, page still live, apply flow leading to an expired page, markup still present. Fix by expiring (as in "Remove a job posting"), using the Indexing API, then request reconsideration.
- Apply option missing (message: "Can't submit application on job offer page"): add a way to apply on the page, then request reconsideration.
- Logo incorrect: no knowledge panel or wrong logo there. Fix with `hiringOrganization.logo` (ratio 0.75 to 2.5; faster, no verification needed) or by suggesting a knowledge panel change (more control, slower).
- Job location missing or incorrect: ensure `jobLocation`, `addressLocality`, `addressRegion` are valid and as complete as possible; validate in Rich Results Test > fetch URL > Validate > Preview (location shown correctly; "false" means not a real location).

### Analytics: custom UTM parameters
- Visits arriving from the Google job detail page to your site carry `utm_campaign=google_jobs_apply`, `utm_source=google_jobs_apply`, `utm_medium=organic`; use them in Google Analytics or third-party tools. A traffic troubleshooter is linked for unexpected fluctuations.

### Region availability (region)
- Asia: Bangladesh, Hong Kong, India, Indonesia, Japan, Kazakhstan, Kyrgyzstan, Malaysia, Pakistan, Philippines, Singapore, Sri Lanka, Taiwan, Thailand, Uzbekistan, Vietnam.
- Europe: Austria, Belarus, Belgium, Denmark, France, Germany, Greece, Italy, Netherlands, Portugal, Russia, Spain, Switzerland, United Kingdom.
- Latin America: entire region. North America: entire region. Sub-Saharan Africa: entire region.
- Middle East and North Africa: Algeria, Bahrain, Egypt, Iraq, Jordan, Kuwait, Lebanon, Libya, Morocco, Oman, Palestine, Qatar, Saudi Arabia, Tunisia, United Arab Emirates.
