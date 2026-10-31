# Structured data feature guides: Local business, Math solver, Movie, Organization, Profile page, Q&A, Recipe, Review snippet, Software app, Speakable, Subscription/paywalled content, Vacation rental, Video: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

Shared boilerplate (appears on every page below, stated once here): build, test, release flow is (1) add required properties (JSON-LD, Microdata or RDFa as the page allows; CMS plugin or JavaScript generation are fine), (2) follow the guidelines, (3) validate with the Rich Results Test and fix critical errors (non-critical issues are optional for eligibility), (4) deploy a few pages, check them with URL Inspection (page must not be blocked by robots.txt, `noindex` or login), then request recrawl, (5) submit a sitemap (can be automated with the Search Console Sitemap API). Re-crawl and re-index can take several days. Each page also links Search Essentials and the general structured data guidelines; violating them can trigger a manual action (fix, then request reconsideration). Troubleshooting boilerplate: ask the CMS owner/forward Search Console messages; Google never guarantees a rich result; check structured data errors and the Unparsable structured data report; a structured-data manual action makes Google ignore the markup (page can still rank), fix via the Manual Actions report; rules violations can be spammy content or spammy markup that the Rich Results Test cannot detect; use the "Troubleshoot missing rich results / drop in total rich results" guide; allow time for recrawl; ask in the Search Central forum.

## Organization
https://developers.google.com/search/docs/appearance/structured-data/organization · Last updated: 2026-09-08

### Purpose
- Organization markup on the home page helps Google understand administrative details and disambiguate the organization.
- Some properties work behind the scenes (`iso6523Code`, `naics`); others can change visuals, e.g. which `logo` appears in results and the knowledge panel.
- Merchants can influence the merchant knowledge panel and brand profile (return policy, address, contact info).
- No required properties; add as many relevant recommended ones as apply. Focus on useful ones: `name`/`alternateName`, real-world presence (`address`, `telephone`), online presence (`url`, `logo`).

### Guidelines / technical
- Place it on the home page or a single page describing the organization (e.g. About). Not needed on every page.
- Use the most specific schema.org subtype of `Organization` (e.g. `OnlineStore` rather than `OnlineBusiness` for ecommerce).
- Local businesses (restaurant, physical store): use the most specific `LocalBusiness` subtype(s) and follow the Local business required and recommended fields in addition.
- Examples show: plain `Organization` (url, sameAs, logo, name, description, email, telephone, address, vatID, iso6523Code) and `OnlineStore` with `contactPoint`, `hasShippingService` (`ShippingService` with `ShippingConditions` per origin/destination; rate as `ShippingRateSettings.orderPercentage` or `MonetaryAmount`) and `hasMerchantReturnPolicy`.

### Recommended properties (all optional)
- `name` (Text): same `name` and `alternateName` as used for the site name. `alternateName` (Text): another common name.
- `legalName` (Text): registered name, if different from `name`.
- `url` (URL): the organization's website; helps identify it uniquely.
- `logo` (URL or ImageObject): minimum 112x112 px; URL crawlable and indexable; format supported by Google Images; must look right on a plain white background (mostly white/gray logos may not). `ImageObject` needs a valid `contentUrl` or `url`.
- `description` (Text): detailed description.
- `address` (PostalAddress, may be repeated for several locations): `streetAddress`, `addressLocality`, `addressRegion` (e.g. state), `postalCode`, `addressCountry` (two-letter ISO 3166-1 alpha-2). Include all parts that apply to the country.
- `contactPoint` (ContactPoint): `telephone` (include country and area code) and `email`. With a `LocalBusiness` type, set a primary phone/email at the `LocalBusiness` level first, then use `contactPoint` for additional methods. Include all support methods available.
- `telephone` (Text): primary customer contact number, with country and area code. `email` (Text).
- `sameAs` (URL, repeatable): pages on other sites about the organization (social, review sites).
- `foundingDate` (Date, ISO 8601). `numberOfEmployees` (QuantitativeValue): either `value` or `minValue`/`maxValue`.
- Identifiers: `vatID` (important trust signal; users can look it up in public VAT registries), `taxID` (must match the country in `address`), `iso6523Code`, `duns` and `leiCode` (both: prefer `iso6523Code` with prefix `0060:` / `0199:`), `globalLocationNumber` (GS1 GLN), `naics`.
- `iso6523Code`: ICD, then identifier, separated by `:` (U+003A). Common ICDs: `0060` DUNS, `0088` GS1 GLN, `0199` LEI.
- Merchant: `hasMerchantReturnPolicy` (repeated `MerchantReturnPolicy`), `hasShippingService` (repeated `ShippingService`), `hasMemberProgram` (repeated `MemberProgram`). Each has its own markup page. If no org-level policy exists, or a product needs an override, use the same property in merchant listing markup.

## Local business
https://developers.google.com/search/docs/appearance/structured-data/local-business · Last updated: 2026-09-08

### Overview
- Search or Maps may show a knowledge panel for a matching business, or a carousel for a business-type query ("best NYC restaurants").
- Markup can describe hours, departments, and reviews (only if the site captures reviews about other businesses).
- Reservations/orders directly in results need the Maps Booking API (separate).
- Can go on any page; best on a page about the business.

### Guidelines
- Follow Search Essentials, general structured data guidelines, and (if used) carousel guidelines.
- Restaurant carousel (limited access): only a small set of restaurant providers; others register interest via a form.

### `LocalBusiness` type
- One `LocalBusiness` per location; use the most specific subtype (`Restaurant`, `DaySpa`, `HealthClub`, ...). It is an `Organization` subtype, so also follow the Organization fields.
- Multiple types: use an `@type` array (e.g. `["Electrician","Plumber","Locksmith"]`); `additionalType` is not supported.
- Required: `address` (PostalAddress, physical location, as many properties as possible), `name` (Text).
- Recommended:
  - `aggregateRating`, `review`: only for sites that capture reviews about other local businesses; follow Review snippet rules (see self-serving rule there).
  - `department` (LocalBusiness, nested; may define any property of this table). Name format `{store name} {department name}` (e.g. `gMart Pharmacy`); if the department is explicitly branded, use its name alone (e.g. `Geek Squad`). Define only properties that differ from the main store.
  - `geo` with `latitude`/`longitude`: precision at least 5 decimal places.
  - `menu` (URL, fully-qualified; food establishments).
  - `openingHoursSpecification` (array or single object): `dayOfWeek` (schema.org URLs like `https://schema.org/Monday`, or short names like `Monday`), `opens`/`closes` (Time, documented as hh:mm:ss), `validFrom`/`validThrough` (Date YYYY-MM-DD, seasonal closure).
  - `priceRange` (Text): `$$$` style or range like "$10-15"; must be shorter than 100 characters or no price range is shown.
  - `servesCuisine`.
  - `telephone`: primary customer contact, with country and area code.
  - `url`: fully-qualified URL of this specific location; must be a working link.

### Business hours patterns
- Standard hours: omit `validFrom`/`validThrough` for year-round hours.
- Past midnight: one `OpeningHoursSpecification`, e.g. Saturday `opens` 18:00, `closes` 03:00 (ends Sunday 3am).
- Open 24 hours: `opens` 00:00, `closes` 23:59. Closed all day: both 00:00.
- Seasonal: `validFrom` + `validThrough` with both times 00:00 marks a closure period.
- Both the schema.org URL and short form for `dayOfWeek` are accepted; Google plans to track the schema.org outcome and keep accepting both.
> Note: the page text says "`open`" for the 24-hour case but means `opens`; times are described as hh:mm:ss while all examples use hh:mm.

### Restaurant carousel (limited access)
- Needs a summary page with Carousel markup plus a details page per restaurant.
- Required on the details page: `image` (repeated URL/ImageObject; crawlable, indexable, representative, Google Images format; for best results several high-res images, minimum 50K pixels width x height, in 16x9, 4x3 and 1x1) and `name`.
- Recommended: `address`, `servesCuisine`.

## Review snippet
https://developers.google.com/search/docs/appearance/structured-data/review-snippet · Last updated: 2026-09-08

### Overview and eligible types
- A review snippet is an excerpt of a review or rating (often an average); Google may show stars and summary info in rich results or knowledge panels.
- Features that take ratings: Book, Course list, Event, Local business (only sites capturing reviews about other local businesses), Movie, Product, Recipe, Software App.
- Also supported schema.org types and subtypes: `CreativeWorkSeason`, `CreativeWorkSeries`, `Episode`, `Game`, `MediaObject`, `MusicPlaylist`, `MusicRecording`, `Organization` (only sites capturing reviews about other organizations).
- Reviews about employers: use `EmployerAggregateRating` instead.
- Four ways to add: simple `Review`, `Review` nested via `review`, `AggregateRating`, `AggregateRating` nested via `aggregateRating`. An individual review's rating can be omitted if the marked-up content has both author and review date. For aggregate reviews, the average rating must be supplied for the snippet to show.

### Guidelines
- Technical:
  - Mark up an aggregate evaluation by many people with `AggregateRating`.
  - Refer clearly to the specific item: nest the review in the item's type (e.g. `Book`, `Recipe`) or use `itemReviewed`.
  - Review content must be visible to users on the marked-up page (review text and rating; the aggregate rating if you use `AggregateRating`).
  - Recommended: accept only ratings that come with review text and author name.
  - Review a specific item, not a category or list of items.
  - If you include several individual reviews, also include an aggregate rating.
  - Do not aggregate reviews or ratings from other websites.
  - No fake or undisclosed incentivized reviews (not based on genuine experience; written for money, discounts, vouchers or free products without clear, prominent disclosure).
- Local business / organization reviews, extra rules:
  - Self-serving reviews: if the reviewed entity controls the reviews about itself (in its own structured data, or via an embedded third-party widget such as Google Business or Facebook reviews), its `LocalBusiness`/`Organization` pages are ineligible for the star review feature.
  - Ratings must be sourced directly from users.
  - Do not rely on human editors to create, curate or compile local-business ratings.

### `Review` properties
- Required:
  - `author` (Person or Organization): valid name (not e.g. "50% off until Saturday"); under 100 characters or the page isn't eligible for an author-based snippet.
  - `itemReviewed` (not needed when nested): valid types are `Book`, `Course`, `CreativeWorkSeason`, `CreativeWorkSeries`, `Episode`, `Event`, `Game`, `HowTo`, `LocalBusiness`, `MediaObject`, `Movie`, `MusicPlaylist`, `MusicRecording`, `Organization`, `Product`, `Recipe`, `SoftwareApplication`.
  - `itemReviewed.name` (or the parent item's `name` when nested): still required when nested.
  - `reviewRating` (Rating or subtype; most typical subtype `AggregateRating`) with `ratingValue` (Number or Text: number, fraction or percentage such as `4`, `60%`, `6 / 10`). Default scale 1-5; otherwise set `bestRating`/`worstRating`. Decimals use a dot (`4.4`, not `4,4`); in Microdata/RDFa use `content` to show a comma to users while exposing the dot.
- Recommended: `datePublished` (ISO 8601 date), `reviewRating.bestRating` (default 5), `reviewRating.worstRating` (default 1).

### `AggregateRating` properties
- Required: `itemReviewed` (not when nested; same type list), `itemReviewed.name` / parent `name`, `ratingValue` (same format rules), and at least one of `ratingCount` (total ratings on your site) or `reviewCount` (people who reviewed, with or without a rating).
- Recommended: `bestRating` (default 5), `worstRating` (default 1).

## Recipe
https://developers.google.com/search/docs/appearance/structured-data/recipe · Last updated: 2026-09-08

### Overview
- Recipes can appear in Search and Google Images (recipe badge). Properties like ratings, cook/prep times and nutrition add detail.
- Enhancement: recipe host carousel via `ItemList` on a gallery/summary page.

### Guidelines
- Use `Recipe` for content about preparing a particular dish; "facial scrub" or "party ideas" are not valid dishes.
- Carousel/grid: provide `ItemList` (separately or together with recipe markup) and have a summary page listing all recipes in the collection, which users reach from the result.
- Violations mean no rich result; the content still appears normally.

### `Recipe` properties
- Required:
  - `image` (URL or ImageObject): image of the finished dish; crawlable/indexable, representative, Google Images format; several high-res images (min 50K px, 16x9, 4x3, 1x1) for best results. It does not control the text-result thumbnail (use image SEO practices for that).
  - `name` (Text): name of the dish.
- Recommended:
  - `aggregateRating`: follow Review snippet rules. If only a single review exists, the reviewer name must be a real person or organization.
  - `author` (Person or Organization), `datePublished` (ISO 8601 date), `description` (short summary).
  - `cookTime` and `prepTime` (Duration, ISO 8601): always use them together. `totalTime`: use it, or both `cookTime` and `prepTime`.
  - `keywords` (Text): season, holiday, descriptors ("quick", "easy"); comma separated; do not repeat `recipeCategory`/`recipeCuisine` values.
  - `nutrition.calories` (Energy): per serving; if set, `recipeYield` must be set with the number of servings.
  - `recipeCategory` (meal type or course), `recipeCuisine` (region).
  - `recipeIngredient` (Text, repeated): only text needed to make the recipe; no definitions of ingredients.
  - `recipeInstructions` (`HowToStep` recommended, `HowToSection`, or Text): with plain text, repeated values are concatenated and Google tries to split steps and strip section names/step numbers; unambiguous `HowToStep` gives best results. No metadata that belongs elsewhere (author, cuisine, category, keywords) and no filler like "Directions", "Watch the video", "Step 1".
  - `recipeYield` (Text or Integer): number of servings as a plain number; extra yields allowed (e.g. `["6","24 cookies"]`); required with per-serving nutrition.
  - `video` (VideoObject): follow the Video property lists.

### `HowToSection`
- Use only if the recipe really has sections (split into `HowToStep` first). Placed in `recipeInstructions` or as `itemListElement` of another `HowToSection` (sub-sections).
- Required: `itemListElement` (`HowToStep` list and/or sub-sections), `name`.
- Never use it for alternative recipes of the same dish; use multiple `Recipe` objects.

### `HowToStep`
- Required: `text` (full instruction; optional if `itemListElement` used) or `itemListElement` (`HowToDirection`/`HowToTip`; optional if `text` used). Text must be instruction only.
- Recommended: `image` (ImageObject or URL; .jpg, .png or .gif; crawlable, representative), `name` (short summary; no "Step 1:" or "1." style), `url` (anchor link to the step), `video` (VideoObject or Clip).

### `HowToDirection` and `HowToTip`
- Same properties; required: `text`.

### `ItemList` (host carousel)
- Required: `itemListElement` (`ListItem`) with `position` (Integer ordinal) and `url` (canonical URL of the item page; unique per item).

### Search Console
- Check Rich result status reports after first deploy (valid items up, invalid not up), after template changes (invalid up = broken template; valid down without invalid up = markup no longer embedded; use URL Inspection), and review traffic in the Performance report/API.

## Video
https://developers.google.com/search/docs/appearance/structured-data/video · Last updated: 2026-09-24

### Overview and features
- `VideoObject` influences description, thumbnail URL, upload date, duration in results. Videos can appear in main results, Video mode, Google Images and Discover. Markup on watch pages also helps Google find the video.
- LIVE badge: via `BroadcastEvent`; any public video live-streamed for any length of time (sports, awards shows, influencer videos, game streams). Use the Indexing API so Google crawls at the right time.
- Key moments (segments like chapters):
  - Google detects segments automatically; it prioritizes segments you set via structured data or the YouTube description.
  - Embedded video or video platform: `Clip` (exact start/end and labels; all languages where Search is available) or `SeekToAction` (tell Google your URL timestamp pattern; supported languages: English, Spanish, Portuguese, Italian, Chinese, French, Japanese, German, Turkish, Korean, Dutch, Russian).
  - YouTube-hosted video: timestamps and labels in the description (all languages). Extra guidelines apply for YouTube Video Chapters.
  - Opt out of key moments entirely (including automatic): `nosnippet` meta tag.

### Guidelines
- Follow Search Essentials, general structured data guidelines and video indexing requirements. Markup outside the guidelines may get a manual action.
- LIVE badge: no vulgar or offensive language in the markup. Call the Indexing API when the video goes live, when streaming has stopped and markup is updated with `endDate`, and whenever the markup changes. The Indexing API supports only livestream videos here.
- YouTube timestamps: format `[hour]:[minute]:[second]` (omit hour if none); label on the same line; one timestamp per line; link the timestamp to the point in the video; label has at least one word; chronological order.
- `Clip` and `SeekToAction`: the video must support deep links to a point other than the start (e.g. `?t=30`); `VideoObject` must be on a page where users can watch the video; total duration at least 30 seconds; required `VideoObject` properties present; `Clip` only: no two clips of the same video on the same page share a start time; `SeekToAction` only: Google must be able to fetch the video content files.

### `VideoObject` properties
- Required:
  - `name` (Text): title; unique per video on the site.
  - `thumbnailUrl` (repeated URL): the video's unique thumbnail file; follow thumbnail image guidelines.
  - `uploadDate` (DateTime, ISO 8601): when first published; include time zone or Googlebot's time zone is assumed.
- Recommended:
  - `contentUrl` (URL): URL of the actual video file bytes (not the page); most effective for Google to fetch the file; use `embedUrl` if unavailable. Supported file types; follow video best practices. Tip: restrict to Googlebot via reverse DNS lookup.
  - `embedUrl` (URL): URL of the player (like an `<embed>` `src`), not the watch page.
  - `creator` (or `author`) (Person or Organization) with `name` (or `alternateName`; one required) and `url` (profile or home page).
  - `description` (Text): unique per video; HTML ignored.
  - `duration` (ISO 8601, e.g. `PT00H30M5S`).
  - `expires` (DateTime): only if the video expires; include time zone.
  - `hasPart`: nested `Clip` for key moments.
  - `ineligibleRegion` or `regionsAllowed` (Place): two- or three-letter ISO 3166-1 codes; multiple values via array or repeated `meta`; no value means allowed everywhere. Use whichever fits.
  - `interactionStatistic` (`InteractionCounter`): `interactionType` one of `WatchAction`, `LikeAction`, `CommentAction`, `ShareAction` (schema.org URLs); `userInteractionCount` (Integer). Since October 2019 `interactionStatistic` is recommended over `interactionCount` (still supported).
  - `publication`: nested `BroadcastEvent` for the LIVE badge.

### `BroadcastEvent` (LIVE badge; nest in `VideoObject.publication`)
- Required for the badge: `publication` (single or list), `isLiveBroadcast` (Boolean; true if is, was or will be live), `startDate`, `endDate` (ISO 8601).
- `startDate` in the past or present: stream started; in the future: scheduled. Same for `endDate`: past/present means stream ended and is no longer live.
- `endDate` must be provided once the video is over; if unknown before the stream starts, give an approximate value.

### `Clip` (nest in `hasPart`)
- Required (to have your timestamps and labels shown instead of automatic segments): `name` (descriptive title), `startOffset` (Number, seconds from start), `url` (points to the clip start; same URL path as the video plus query parameters, e.g. `?t=120`).
- Recommended: `endOffset` (Number, seconds).

### `SeekToAction` (in `VideoObject.potentialAction`)
- Required: `target` (EntryPoint): URL of the page with the `VideoObject`, with the placeholder `{seek_to_second_number}` replacing the timestamp part (e.g. `...?t={seek_to_second_number}`); `startOffset-input` (Text): exactly `required name=seek_to_second_number` (annotated property, see Potential Actions).
- Prefer `Clip` if you want to define key moments yourself.

## Movie carousel
https://developers.google.com/search/docs/appearance/structured-data/movie · Last updated: 2026-09-08

### Overview
- Movie lists marked up so users can browse movies in a carousel in Search. The movie carousel is only available on mobile devices.
- Related: claim a specific movie in the knowledge panel via Google verification; Media Actions enable a watch button.

### Structure
- Summary page + separate detail pages: summary page has `ItemList` of `ListItem` (`position`, `url` to each detail page); each detail page has `Movie` markup.
- Single all-in-one page: `ItemList` whose `ListItem.item` is a full `Movie` (`url` per item, e.g. fragment anchors).

### Guidelines
- Follow Carousel guidelines, Search Essentials, general structured data guidelines. Out-of-guideline markup can cause a manual action.

### `Movie` properties (in addition to Carousel properties)
- Required:
  - `image` (URL or ImageObject): crawlable/indexable, representative, `.jpg`, `.png` or `.gif`; high resolution, 6:9 aspect ratio. Google can crop near-6:9 images; images deviating a lot are ineligible.
  - `name` (Text).
- Recommended: `aggregateRating` (Review snippet rules), `dateCreated` (Date or DateTime; release date), `director` (Person), `review` (nested `Review`, Review snippet rules).

## Q&A
https://developers.google.com/search/docs/appearance/structured-data/qapage · Last updated: 2026-09-08

### Overview
- For pages with one question followed by its answers: `QAPage`, `Question`, `Answer`. Eligible for a Q&A rich result; answer content may also improve the basic snippet.

### Content guidelines
- Use `QAPage` only for a single question followed by its answers.
- Users must be able to submit answers. Valid: forum page where users answer a single question; product support page where users answer a single question. Invalid: site-written FAQ with no user answers, product page with many user questions/answers, how-to guide, blog post, essay that answers a question.
- Do not apply it site-wide when only some pages are questions (e.g. forum pages that are not questions are ineligible).
- Not for FAQ pages or pages with multiple questions; not for advertising.
- Each `Question` and `Answer` contains the entire text, not a portion.
- `Answer` is for answers only; comments on the question or other answers use `comment` / `Comment`.
- Results may not show if content is obscene, profane, sexually explicit, graphically violent, promotes dangerous or illegal activity, or is hateful or harassing.
- Education Q&A carousel: pages whose main purpose is the correct answer to a user-submitted homework question may be eligible; they can have a single answer provided or selected by in-house experts rather than users.

### `QAPage`
- Exactly one `QAPage` per page; Google only uses `Question` data from `QAPage` pages. Required: `mainEntity` (`Question`).

### `Question`
- Exactly one per page, under `mainEntity`. Omit recommended properties the site doesn't support.
- Required:
  - `name` (Text): short form of the question.
  - `answerCount` (Integer): total answers, even if only some are marked up (e.g. 15 total, 10 marked up: 15); may be 0. `answerCount` + `commentCount` = total replies of any type.
  - At least one of `acceptedAnswer` or `suggestedAnswer` (`Answer`) for rich-result eligibility; unanswered questions (answerCount 0) are not eligible.
    - `acceptedAnswer`: zero or more; must be accepted on your site (by asker, moderator or voting). Sorting by recency must not define it.
    - `suggestedAnswer`: zero or more answers not accepted as top.
- Recommended: `author` (Person/Organization; follow author markup best practices, use Article and ProfilePage properties as a guide), `author.url` (profile page, ideally with ProfilePage markup), `comment` (`Comment`, clarification not answer), `commentCount`, `dateModified`, `datePublished` (ISO 8601), `digitalSourceType`, `image` (inline images only; no default/icon/placeholder/author images), `text` (long form of the question), `upvoteCount` (single aggregate: 5 up and 2 down = 3), `video` (VideoObject).

### `Answer`
- Required: `text` (full answer; partial markup may prevent display).
- Recommended: `author`, `author.url`, `comment`, `commentCount` (useful when not all comments are marked up), `dateModified`, `datePublished`, `digitalSourceType`, `image`, `upvoteCount` (aggregate if both up and down votes), `url` (direct link such as `...#answer1`; strongly recommended), `video` (VideoObject or URL).

### `Comment`
- For clarifications or discussion, nested in `Question` or `Answer` via `comment`. Required: `text`.
- Recommended: `author`, `author.url`, `comment` (nested threaded reply), `commentCount`, `dateModified`, `datePublished`, `digitalSourceType`, `image`, `video`.

### `digitalSourceType` (Question, Answer, Comment)
- Type `IPTCDigitalSourceEnumeration`. Supported: `TrainedAlgorithmicMediaDigitalSource` (created by a trained model such as an LLM), `AlgorithmicMediaDigitalSource` (simpler algorithmic process such as an auto-reply bot). If omitted, Google assumes human-generated.

### Search Console
- Same monitoring steps as listed under Recipe (rich result status report, template changes, Performance report).

## Profile page
https://developers.google.com/search/docs/appearance/structured-data/profile-page · Last updated: 2026-09-08

### Overview
- `ProfilePage` is for sites where creators (people or organizations) share first-hand perspectives. Helps Google understand creators in a community and surface better content, including the Discussions and Forums feature.
- Other features (Article, Recipe authors; forum and Q&A authors) can link to pages with `ProfilePage` markup.

### Content guidelines
- The page's main focus must be a single person or organization affiliated with the site.
- Valid: forum/social user profile, news-site author page, blog "About Me" page, employee page on a company site.
- Invalid: a store's home page (lots of non-profile info), an organization review site (organization not associated with the site).

### Technical guidelines
- If the profile shows recent activity, mark those items with URLs pointing to the full content/markup. Example structure: `ProfilePage.mainEntity` (Person with `@id` such as `#main-author`) plus `hasPart` items (e.g. `Article`) whose `author` references that `@id`.

### `ProfilePage` properties
- Required: `mainEntity` (`Person` or `Organization`): use the correct type if known, otherwise default to `Person` (e.g. unknown account type).
- Recommended: `dateCreated` (DateTime, ISO 8601), `dateModified` (DateTime; ideally only human-edited metadata changes, not added outlinks).

### `Person` / `Organization` properties (on `mainEntity`)
- Required: `name` (Text): real name preferred, `alternateName` for handles; may hold a handle if that's the only identifier. If `name` is unavailable, `alternateName` fulfils the requirement.
- Recommended:
  - `agentInteractionStatistic` (`InteractionCounter`): the entity's own behavior; types `FollowAction` (accounts followed), `LikeAction` (likes given), `WriteAction` (posts), `ShareAction` (reshares).
  - `interactionStatistic`: stats applied to the entity, only about the hosting platform (not followers elsewhere); types `FollowAction` (followers), `LikeAction` (likes received), `BefriendAction` (bi-directional relationship).
  - `alternateName` (e.g. handle), `description` (byline or credential), `identifier` (unique ID on your site, e.g. internal DB ID that survives handle changes).
  - `image` (URL or ImageObject): profile image. If none, do not insert a default, icon or placeholder. Crawlable/indexable, representative, Google Images format; several high-res images (min 50K px; 16x9, 4x3, 1x1).
  - `sameAs` (URL): other external profiles or home pages.

### Search Console
- Monitor rich results: after first deploy, after template/code changes, and periodically via the Performance report and API (same steps as under Recipe).

## Software app
https://developers.google.com/search/docs/appearance/structured-data/software-app · Last updated: 2026-09-08

### Overview and guidelines
- Marks up app details in the page body for software app results. Formats shown: JSON-LD, RDFa, Microdata. Follow Search Essentials and general structured data guidelines.

### `SoftwareApplication` properties
- Required:
  - `name` (Text).
  - `offers.price`: price of the app; `0` if free. For developers `offers` can show carrying marketplaces; for marketplaces it shows the app price. If price is above 0, also give `offers.priceCurrency` (otherwise Google guesses).
  - A rating or review, at least one of: `aggregateRating` (`AggregateRating`) or `review` (`Review`); follow Review snippet rules.
- Recommended:
  - `applicationCategory` (Text; must be a supported type): `GameApplication`, `SocialNetworkingApplication`, `TravelApplication`, `ShoppingApplication`, `SportsApplication`, `LifestyleApplication`, `BusinessApplication`, `DesignApplication`, `DeveloperApplication`, `DriverApplication`, `EducationalApplication`, `HealthApplication`, `FinanceApplication`, `SecurityApplication`, `BrowserApplication`, `CommunicationApplication`, `DesktopEnhancementApplication`, `EntertainmentApplication`, `MultimediaApplication`, `HomeApplication`, `UtilitiesApplication`, `ReferenceApplication`.
  - `operatingSystem` (Text), e.g. `Windows 7`, `OSX 10.6`, `Android 1.6`.
- Subtypes: `MobileApplication` and `WebApplication` are supported.
- `VideoGame` alone gets no rich result; co-type it with another type (e.g. `["VideoGame","MobileApplication"]`).

## Math solver
https://developers.google.com/search/docs/appearance/structured-data/math-solvers · Last updated: 2025-12-18

### Overview
- Markup indicates the problem types a solver handles and links to step-by-step solutions; helps students and teachers. Appearance subject to change.
- Types: `MathSolver` plus `LearningResource` (co-typed, e.g. `["MathSolver","LearningResource"]`).
- Examples: one solver with one `SolveMathAction` covering several `eduQuestionType` values and a second language version (separate JSON-LD objects per language; the Spanish markup may sit on the Spanish site's home page instead); two `SolveMathAction` endpoints with different question types (e.g. polynomial, trigonometric).

### Technical guidelines
- Put `MathSolver` markup on the site's home page.
- Googlebot must be able to crawl the site efficiently.
- If identical copies exist under different URLs, use canonical URLs on each copy.
- Solvers entirely behind a login or paywall are not allowed; the solution and step-by-step walkthrough for the user's initial problem must be accessible. Additional content may be gated.

### Content guidelines
- No promotional content disguised as a math solver (e.g. third-party affiliate programs).
- The owner is responsible for accuracy of declared problem types and of solutions. If a certain amount of data is inaccurate in quality review, the solver may be removed from the feature until fixed (depends on severity). Violations may lead to manual action and removal from the math solver experience.

### `MathSolver` properties
- Required:
  - `potentialAction` (`SolveMathAction`) with `target` and `mathExpression-input`.
  - `potentialAction.mathExpression-input` (Text): placeholder for the expression Google sends (annotated property; value pattern `required name=math_expression_string`). The string may be LaTeX, Ascii-Math or keyboard-typable math. For some problem types it encodes type and parameters:
    - Derivatives: `(expr)'` or `d/dvariable expr` (e.g. `(x^2+x)'`, `d/dx (x^2+x)`).
    - Integrals: `\int expr` or `\int_{from}^{to} expr`.
    - Limits: `\lim expr` or `\lim_{variable\rightarrowvalue} expr` (e.g. `\lim_{x\rightarrow0} sin(x)/x`).
  - `potentialAction.target` (EntryPoint): URL template containing `{math_expression_string}`.
  - `url` (URL): the solver. `usageInfo` (URL): privacy policy.
- Recommended:
  - `inLanguage` (Text): supported language(s) (BCP 47 style, e.g. `es`).
  - `assesses` (Text, problem types): use only when `HowTo` markup accompanies `MathSolver` for a specific problem.
  - `potentialAction.eduQuestionType` (Text, problem types): problem types the target can solve.
### `LearningResource`
- Required: `learningResourceType` (Text): fixed value `Math Solver`. Put on the home page.
> Note: the page's own examples use `"Math solver"` (lowercase s) while the property definition says `Math Solver`.

### Problem types (not exhaustive; used in `eduQuestionType` / `assesses`)
- Generic umbrella types that can be combined with others: `Algebra`, `Calculus`, `Geometry`, `Linear Algebra`.
- Equations: `Absolute Value Equation`, `Biquadratic Equation`, `Differential Equation`, `Exponential Equation`, `Linear Equation`, `Logarithmic Equation`, `Polynomial Equation`, `Quadratic Equation`, `Radical Equation`, `Rational Equation`, `System of Equations`, `Line Equation`.
- Inequalities: `Linear Inequality`, `Logarithmic Inequality`, `Polynomial Inequality`, `Quadratic Inequality`, `Radical Inequality`, `Rational Inequality`.
- Expressions/functions: `Polynomial Expression`, `Quadratic Expression`, `Rational Expression`, `Function`, `Function Composition`.
- Calculus: `Derivative`, `Integral`, `Limit`, `Arc Length`, `Inflection Point`.
- Geometry: `Circle`, `Ellipse`, `Hyperbola`, `Parabola`, `Distance`, `Midpoint`, `Slope`, `Intercept`, `Parallel`, `Perpendicular`.
- Linear algebra: `Matrix`, `Eigenvalue`, `Eigenvector`, `Characteristic Polynomial`.
- Other: `Arithmetic`, `Statistics`, `Trigonometry`.

## Speakable (beta)
https://developers.google.com/search/docs/appearance/structured-data/speakable · Last updated: 2026-09-08

### Overview
- (beta) Subject to change; requirements and guidelines may change.
- The `speakable` property marks sections of an `Article` or `WebPage` best suited for text-to-speech playback on Google Assistant-enabled devices.
- Google Assistant uses it for topical news queries on smart speakers: returns up to three articles and plays `speakable` sections via TTS; it names the source and sends the full article URL to the user's phone via the Assistant app.
- Availability (region: US, language: English): users in the U.S. with Google Home devices set to English, and publishers publishing English content. Other countries/languages planned once enough publishers adopt it.

### Guidelines
- Technical:
  - Do not mark content that sounds confusing by voice alone: datelines, photo captions, source attributions.
  - Mark key points, not the whole article, so TTS isn't cut off in the middle of important details.
- Content:
  - Content needs concise headlines and/or summaries that are comprehensible and useful.
  - If the top of the story is included, rewrite it into separate sentences for clearer TTS.
  - Aim for roughly 20-30 seconds of audio per section, about two to three sentences.
- Also follow Search Essentials and the general structured data guidelines.

### Properties
- `speakable` (on `Article` or `WebPage`, repeatable) is a `SpeakableSpecification` with exactly one locator type, not both: `cssSelector` (Text; e.g. class selectors such as `.headline`, `.summary`) or `xPath` (Text; e.g. `/html/head/title`, `/html/head/meta[@name='description']/@content`).
- Minimal shape: `"speakable": {"@type": "SpeakableSpecification", "cssSelector": [".headline", ".summary"]}`.

### Troubleshooting
- Content does not trigger via Assistant: try voice commands "What's the latest news about $topic?", "What's the latest on $topic?", "Play news about $topic". Ranking is algorithmic; up to three articles from different publications play.
- Other audio options exist for news content (e.g. a custom Google Assistant integration via Actions on Google).

## Subscription and paywalled content
https://developers.google.com/search/docs/appearance/structured-data/paywalled-content · Last updated: 2026-09-08

### Purpose
- `CreativeWork` properties flag paywalled content so Google can distinguish it from cloaking (a spam policy violation). Applies only to content you want crawled and indexed.

### Guidelines
- Follow the general structured data guidelines and technical guidelines. Violations can make the page ineligible for display in results (see Spammy Structured Markup).
- JSON-LD and Microdata are accepted.
- Do not nest content sections.
- `cssSelector` accepts only `.class` selectors.
- If content must not reach the browser at serve time, choose a paywall that does not send paywalled content to the browser; for client-side JavaScript paywalls, check Google's JavaScript paywall guidance.

### Adding markup
- Applies to all versions of the page (AMP and non-AMP).
- Steps: wrap each paywalled section in an element with a class; add `NewsArticle` (or other supported type) structured data; add `isAccessibleForFree: false` at top level plus `hasPart` (`WebPageElement`, `isAccessibleForFree: false`, `cssSelector: ".paywall"`) matching the class; validate with the Rich Results Test.
- Several paywalled sections: `hasPart` becomes an array, one `WebPageElement` per class (e.g. `.section1`, `.section2`).

### Supported types
- `CreativeWork` or its subtypes `Article`, `NewsArticle`, `Blog`, `Comment`, `Course`, `HowTo`, `Message`, `Review`, `WebPage`. Multiple types are allowed (e.g. `["Article","LearningResource"]`).
- Required: `isAccessibleForFree` (Boolean): `false` means behind a paywall (or requires subscription or registration).
- Recommended (for section granularity): `hasPart.cssSelector` (CssSelectorType; the class set in HTML), `hasPart.@type` (`WebPageElement`), `hasPart.isAccessibleForFree` (Boolean, `False` for paywalled section).

### AMP
- Use `amp-subscriptions` where appropriate; the authorization endpoint must grant access to the right Google and other bots (differs per publisher); keep the bot access policy identical for AMP and non-AMP or Search Console may show content mismatch errors.

### Generative AI in Search
- AI Overviews and AI Mode use web sources and are subject to Search's preview controls.

### Crawling and snippets
- To have paywalled sections crawled and indexed, Googlebot (and `Googlebot-News` if applicable) must be able to access the page; test with URL Inspection.
- Limit snippet content with the `data-nosnippet` HTML attribute and the `max-snippet` robots meta tag.

## Vacation rental
https://developers.google.com/search/docs/appearance/structured-data/vacation-rental · Last updated: 2026-09-08

### Before you begin (limited access)
- For sites already connected with a Google Technical Account Manager and with Hotel Center access. Others can submit an interest form; that does not guarantee entry to the Early Adopters Program. Extra integration steps beyond markup are required (see the integration starter guide).

### Eligibility guidelines
- Follow Vacation Rental Policies, Search Essentials, general structured data guidelines. Violations can bring a manual action.

### `VacationRental` properties
- Required:
  - `containsPlace` (`Accommodation`; exactly one per listing) with `occupancy` (`QuantitativeValue`) and `occupancy.value` (Integer; max guests).
  - `identifier` (Text): unique per property, independent of listing content (does not change when name or bedroom count changes); the same identifier across languages.
  - `image` (repeated URL): minimum 8 photos, including at least one each of bedroom, bathroom and common area; also follow Property listing image requirements.
  - `latitude` / `longitude` (or `geo.latitude`/`geo.longitude`; Number): precision at least 5 decimals.
  - `name` (Text).
- Recommended:
  - `additionalType` (Text): suggested `Apartment`, `Bungalow`, `Cabin`, `Chalet`, `Cottage`, `Gite`, `HolidayVillageRental`, `House`, `Villa`, `VacationRental`.
  - `address` (PostalAddress): full physical address (street, city, state/region, postal code, unit); P.O. boxes and mailing-only addresses don't count; `addressCountry` is ISO 3166-1 alpha-2.
  - `aggregateRating` (Review snippet rules); `review` (repeated; `review.datePublished` is required for vacation rentals); `review.contentReferenceTime` (DateTime): start of the author's stay; required for listings located in France.
  - `brand` (`Brand` with `name`): brand ID tied to Hotel Center brand setup.
  - `checkinTime`, `checkoutTime` (Time, ISO 8601, e.g. `14:30:00+08:00`).
  - `description`, `knowsLanguage` (repeated Text, BCP 47 like `en-US`).
  - `containsPlace.additionalType`: `EntirePlace`, `PrivateRoom` or `SharedRoom`.
  - `containsPlace.bed` (repeated `BedDetails`): `numberOfBeds` (Integer), `typeOfBed` (suggested `CaliforniaKing`, `King`, `Queen`, `Full`, `Double`, `SemiDouble`, `Single`).
  - `containsPlace.floorSize` (`QuantitativeValue`): `value` plus `unitCode`: `FTK` or `SQFT` for square feet, `MTK` or `SQM` for square meters.
  - `containsPlace.numberOfBathroomsTotal` (simple sum following RESO; 2 full + 1 half = 2.5), `numberOfBedrooms`, `numberOfRooms` (Integer).
  - `containsPlace.amenityFeature` (repeated `LocationFeatureSpecification` with `name` and `value`). Names must be English even for non-English listings.
    - Boolean (`value: true`): `ac`, `airportShuttle`, `balcony`, `beachAccess`, `childFriendly`, `crib`, `elevator`, `fireplace`, `freeBreakfast`, `gymFitnessEquipment`, `heating`, `hotTub`, `instantBookable`, `ironingBoard`, `kitchen`, `microwave`, `outdoorGrill`, `ovenStove`, `patio`, `petsAllowed` (or `containsPlace.petsAllowed`), `pool`, `privateBeachAccess`, `selfCheckinCheckout`, `smokingAllowed` (or `containsPlace.smokingAllowed`), `tv`, `washerDryer`, `wheelchairAccessible`, `wifi`.
    - Non-boolean (English values): `internetType` (`Free`, `Paid`, `None`), `parkingType` (`Free`, `Paid`, `None`), `poolType` (`Indoor`, `Outdoor`, `None`), `licenseNum` (tourist/business license for regions that require it; repeatable; add issuing authority as context, e.g. `Paris: 123456ABC`).
> Note: the page describes `checkoutTime` as "the latest time someone may check into" a lodging establishment; this is likely a copy error for check out.
