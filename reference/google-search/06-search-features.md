# Search features: snippets, title links, site names, sitelinks, search profiles, videos, visual elements, translated results, Web Stories, regional features, Early Adopters programs: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Visual Elements gallery of Google Search
https://developers.google.com/search/docs/appearance/visual-elements-gallery · Last updated: 2026-02-04

### Anatomy of the results page
- Visual elements = parts of the results page a user can see or interact with. Each result type has child elements (a text result contains attribution, title link, snippet).
- Appearance varies by device (desktop vs phone), country, query language and other factors. No single result shows every possible element.
- Five common result types: text result, rich result, image result, video result, exploration features.
  - Text result: based on the page's textual content. Formerly "web result" / "plain blue link".
  - Rich result: usually driven by structured data on the page; graphical or interactive.
  - Image result: based on an image embedded on the page; more likely for image-seeking queries (follow image SEO best practices).
  - Video result: based on a video embedded on the page; more likely for video-seeking queries (follow video best practices).
  - Exploration features: help searchers expand or refine a search.

### Attribution (source of a result; appears on text, image and video results)
- Favicon: small site icon (provide a favicon).
- Site name: provided via `WebSite` structured data.
- Visible URL: readable page URL = domain + breadcrumb.
- Domain: the site address (for example example.com).
- Breadcrumb: trail showing the page's place in the site hierarchy; specified with `BreadcrumbList` structured data.

### Text result elements
- Attribution, title link, snippet, byline date, sitelinks group (two or more sitelinks), sitelink (a single link in the group).
- Byline date: date Google estimates the page was published or updated; a byline date can be provided.
- Sitelinks group: two or more links from the same domain or its localized variations, clustered under a text result. Links may be other pages, headings or anchors in the page. Sitelinks are automated; best practices exist.
- Text result image: most relevant image from the page for the query; tapping goes to the page embedding it; more likely for image-seeking queries; optimize with Image SEO best practices.
- Rich attributes: extra lines such as review stars or recipe info, typically from structured data you supply.

### Image result elements
- Image thumbnail (tap goes to the image) and attribution of the embedding page.

### Video result elements
- Video thumbnail (tap goes to the embedding page), title link of the video landing page, attribution, upload date (the publish date from the video's metadata).

### Exploration features
- You cannot control them. Use them as topic research input.
- Related searches group: auto-generated cluster of searches others did; tapping opens another results page.
- Related questions group ("People Also Ask"): questions related to the query; expanding one shows a featured snippet.

## Title links
https://developers.google.com/search/docs/appearance/title-link · Last updated: 2025-12-10

### What it is
- Title link = the title of a result (Google Search and other properties such as Google News) that links to the page. Often the main factor people use to pick a result.
- Generation is fully automated. It uses page content and references to the page on the web. Google cannot manually change title links for individual sites.

### Sources Google uses (all of them)
- `<title>` element content.
- Main visual title shown on the page.
- Heading elements such as `<h1>`.
- `og:title` meta tag content.
- Other large and prominent text made so by style treatments.
- Other text in the page.
- Anchor text on the page.
- Text in links pointing to the page.
- `WebSite` structured data.
- Changes to any of these need a recrawl and reprocessing: a few days to a few weeks. You can request a recrawl.

### Best practices (all of them)
- Every page needs a `<title>` element.
- Descriptive and concise. Avoid vague titles ("Home", "Profile"). No length limit exists, but display is truncated to the device width, so avoid long verbose titles.
- No keyword stuffing; repeating the same words or phrases looks spammy to users and Google.
- No repeated or boilerplate titles. Every page needs distinct text describing its content. Examples of bad: one title for every page of a shop; long titles varying by one piece of info ("Band Name - See videos, lyrics, posters, ..."). Fix: generate titles dynamically from the page's real content (mention "video" or "lyrics" only when the page has them).
- Brand concisely: home page may carry a longer tagline-style title; on other pages put just the site name at the start or end, separated by a delimiter (hyphen, colon, pipe).
- Make the main title clear: the main title should be the most prominent text (larger font, first visible `<h1>`). Several headings with equal weight confuse the system.
- Be careful with crawl blocking: robots.txt can stop crawling but may not stop indexing (a URL found via other sites' links can still be indexed). With no access to the content, Google builds the title link from off-page content such as anchor text from other sites. To keep a URL out of the index use `noindex`.
- Use the same language and writing system (script) as the page's primary content. A Hindi page needs a Hindi `<title>`, not English or transliterated Latin text. On mismatch, Google may pick other text.
- No flight prices in `<title>`: flight prices change within minutes, so Google likely won't show price info in title links for flight pages.

### Common issues Google corrects (it may rewrite the title link from anchors, on-page text or other sources)
- Half-empty `<title>` (for example `| Site Name`): Google uses headers or large prominent text to fill the gap.
- Obsolete `<title>` (year-dated title not updated, such as 2020 vs visible 2021): Google may use the date from the visible title.
- Inaccurate `<title>` (does not reflect page content, such as a keyword list on dynamic content): Google may replace it with text that reflects the page.
- Micro-boilerplate (a subset of pages share identical titles, such as TV seasons): Google can insert distinguishing text such as the season number from prominent title text.
- No clear main title (several equally prominent headings): Google may use the first heading.
- Mismatch of writing system or language between title and page content: Google may generate a better-matching title link.
- Site name duplication: for domain-level site names, Google may omit the site name from the title link if it repeats the site name already shown in the result.
- Why a result might differ from your `<title>` or main heading: Google detected an issue. If none applies, the displayed title may simply fit the query better.

### Feedback
- Check whether your page has one of the issues above; if not, consider whether the shown title fits the query better. Discuss in the Google Search Central Help Community.

## Snippets
https://developers.google.com/search/docs/appearance/snippet · Last updated: 2026-04-20

### How snippets are created
- Snippet = the description/summary part of a result (Google Search and other properties such as Google News).
- Built automatically, primarily from page content, chosen to match the user's query, so different queries can show different snippets.
- Google sometimes uses the `<meta name="description">` element instead when it describes the page more accurately than on-page text.
- Google cannot manually change snippets for individual sites.

### Controls
- `nosnippet` meta tag: no snippet shown.
- `max-snippet:[number]` meta tag: maximum snippet length.
- `data-nosnippet` attribute: keeps specific page parts out of snippets.

### Meta description best practices (all of them)
- No length limit on the tag; the snippet is truncated to fit the device width.
- CMS users (Wix, WordPress, Blogger): use the CMS's search-engine settings or its way to edit `<head>` meta tags.
- Unique description per page. Identical or similar descriptions across pages do not help. Use site-level descriptions on the home page and aggregation pages, page-level descriptions elsewhere. If time is short, prioritize the home page and popular or critical URLs.
- Include relevant facts: news or blog pages can list author, publication date, byline; product pages can gather price, age, manufacturer. Tag and separate the facts clearly (for example `Written by …, Illustrated by …, Price: …, Length: …`).
- Programmatic generation is acceptable and encouraged for large database-driven sites (for example product aggregators) when descriptions are human-readable, diverse and built from page-specific data. Hand-written is easy for news.
- Keyword-list descriptions give users no idea of the page and are less likely to be shown as a snippet.
- Quality examples (key lessons):
  - Bad: list of keywords. Better: say what the shop sells plus details such as opening hours and location.
  - Bad: same description on every news article. Better: a sentence from the specific article.
  - Bad: an anecdote that doesn't summarize the page. Better: summarize the whole page.
  - Bad: too short ("Mechanical pencil"). Better: specific and detailed (features, variants, offer).
- Meta descriptions are not visible on the page, so they are easy to neglect; high-quality ones can improve search traffic quality and quantity.

### "Read more" deep links (a link in the snippet to a specific page section)
- Content must be immediately visible to a human, not hidden behind an expandable section or tabbed interface.
- Do not use JavaScript to control scroll position on page load (for example forcing the page to the top).
- If you use history API calls or `window.location.hash` changes on load, do not remove the hash fragment from the URL (it breaks deep linking).

## Site names
https://developers.google.com/search/docs/appearance/site-names · Last updated: 2025-12-10

### Availability and how it works
- Site name = the name of the whole site shown with a result. It differs from the per-page title link.
- Available in all languages where Search is available; mobile and desktop. Works for domain-level and subdomain-level sites.
- Fully automated, from the home page content and references to it on the web.
- To state a preference add `WebSite` structured data to the home page. Google also considers `og:site_name`, `<title>`, heading elements and other home page text, but `WebSite` structured data is most important for a stated preference.
- Google can't manually change a chosen site name; you can only offer alternatives.

### Choosing the name
- Unique, accurate, not misleading; must follow Search content policies.
- Concise and commonly recognized ("Google", not "Google, Inc"). No length limit, but long names may be truncated on some devices.
- Avoid generic names (for example "Best Dentists In Iowa"); unlikely to be selected unless an extremely well-known brand.
- Use the name consistently: structured data name must match how the home page refers to the site in the other sources Google reads.
- Provide an alternative name: Google generally won't use the same site name for two global sites, and may decide a site is better known by an acronym. `alternateName` lets Google consider other options.

### Technical guidelines
- One name per site. A site = domain or subdomain. Subdirectory-level site names are not supported (`https://example.com/news` cannot have its own). `www` and `m` subdomains are generally treated as equivalent to the apex.
  - Supported: `https://example.com`, `https://www.example.com`, `https://m.example.com`, `https://news.example.com`.
- `WebSite` markup must be on the home page, meaning the domain or subdomain root URI (`https://example.com`; `https://example.com/de/index.html` is not a home page). No need to mark up other pages.
- If a subdomain home page has no structured data, the domain-level site name may be used as a fallback.
- The home page must be crawlable; if blocked, no site name may be generated.
- Duplicate home pages (HTTP/HTTPS, www/non-www): use the same structured data on all duplicates, not only the canonical.
- If `WebSite` data already exists, put the site name properties in that same node; avoid a second `WebSite` block on the home page.
- Formats: JSON-LD, RDFa or microdata.

### Properties
- Required: `name` (`Text`; follows the naming guidelines), `url` (`URL`; canonical home page of the domain or subdomain, for example `https://example.com/`).
- Recommended: `alternateName` (`Text`; acronym or shorter name). Multiple allowed as an array, most preferred first.
- Minimal shape: `{"@type":"WebSite","name":"Burnt Toast","alternateName":["BT","Burnt Toast Shop"],"url":"https://www.example.com/"}`.

### Testing
- Validate with a schema validator such as Schema Markup Validator. Site names are not supported in the Rich Results Test.
- URL Inspection: confirm the home page is accessible (not blocked by robots.txt, `noindex` or login). Then request a recrawl. Recrawl and reprocessing takes days to weeks. Internal pages may need extra time even when the home page already shows the right name.

### If the preferred name isn't selected
- Verify: structured data holds the preferred name; no structured data errors; follows guidelines; other home page sources use the same name; not a subdirectory setup.
- Redirects: Googlebot must reach the redirect target; the site name reflects the redirect target if it is visible to Googlebot. Request a recrawl.
- Multiple versions (HTTP/HTTPS): use one name consistently.
- Still failing, escalate in this order:
  1. Add `alternateName` (strongly considered when confidence in the preferred name is low).
  2. Add the domain or subdomain as an `alternateName` entry, all lowercase (for example `example.com`, not `Example.com`) so it is detected as a name preference; list it last.
  3. Last resort: set the lowercase domain or subdomain as the preferred `name`; Google will generally pick it.
- If it still fails, post in the Search Central Help Community.
- When Google is less confident, it may build the site name from other sources or show the domain or subdomain name.

## Sitelinks
https://developers.google.com/search/docs/appearance/sitelinks · Last updated: 2025-12-10

- Sitelinks = same-domain links clustered under a text result; Google analyses the site's link structure to find shortcuts.
- Shown only when Google judges them useful and relevant to the query; not shown if the site structure doesn't give good candidates.
- Fully automated; site owner input may be considered in the future. No markup controls them.
- Best practices:
  - Page titles and headings: informative, relevant, compact.
  - Logical, easily navigable site structure; link important pages from other relevant pages.
  - Internal link anchor text: concise and relevant to its target.
  - Avoid repetition in content.
- To remove a sitelink: remove the page from the site or use `noindex`.

## Search profiles
https://developers.google.com/search/docs/appearance/search-profiles · Last updated: 2026-09-16

### How Search profiles work
- A Search profile collects a creator's or publisher's content from across the web and social platforms (Instagram, TikTok, YouTube, X, Facebook, own website) into one destination on Google.
- When readers follow the profile, linked content becomes more likely to appear for them in Google Discover.

### Add a Search profile badge (profile must already be claimed)
- Profile URL pattern: `https://profile.google.com/@handle`.
- Download the badge assets and follow the brand guidelines for placement.
- Image badge: `<a href="https://profile.google.com/@example" aria-label="Find us on Google Search">` wrapping `<img src="/path/to/google-search-badge.svg" alt="Google Search">`.
- Text alternative (bylines, newsletters, bio links): a plain link with the text "Find us on Google Search".

### Brand and design rules
- Touch target at least 48 × 48 dp (Android) and 44 × 44 px (iOS and web).
- With official assets, do not stretch, distort, rotate or recolor the "Super G" icon and Search profile button.
- Don't mix monochrome and colored badges (if all icons are monochrome, use the monochrome "G").
- If used together with the Preferred Sources badge, use the higher-emphasis Search profile button with its label, and don't use the "Super G" icon beside the Preferred Sources badge.
- Problems: ask in the Search Central Help Community.

## Videos (Video SEO best practices)
https://developers.google.com/search/docs/appearance/video · Last updated: 2025-12-18

### Where videos appear
- Main results page, Video mode, Google Images, Discover.
- Workflow: help Google find videos; ensure they can be indexed; enable features; remove/restrict/update as needed; monitor in Search Console; troubleshoot.

### Help Google find your videos
- General Search technical requirements also apply to videos.
- Embed with `<video>`, `<embed>`, `<iframe>` or `<object>`; Google finds videos referenced by these.
- Don't load the video via URL fragment identifiers (generally unsupported).
- JavaScript-injected video must appear in the rendered HTML shown in URL Inspection.
- With a media API (for example Media Source API), still inject the HTML video container element even if the API call fails, and give metadata about the video, so Google can locate the container.
- Don't require user actions (swiping, clicking, typing) to load the video.
- Metadata recommended to ease discovery: structured data, video sitemaps, Open Graph protocol (OGP).

### Indexing requirements (all)
- The watch page must be indexed.
- That indexed watch page must perform well in Search before its video is considered for indexing; an indexed page does not guarantee an indexed video.
- The video must be embedded on a watch page.
- The video can't be hidden behind other elements. With a paywall (sign-in or subscription before viewing) add paywall structured data so Google can still find and index the video.
- The video must have a valid thumbnail at a stable URL.
- Data URLs are not supported.

### Supported video file types
- 3GP, 3G2, ASF, AVI, DivX, M2V, M3U, M3U8, M4V, MKV, MOV, MP4, MPEG, OGV, QVT, RAM, RM, VOB, WebM, WMV, XAP.

### Stable URLs
- CDNs with quickly expiring URLs can break indexing if the thumbnail URL changes too often. Use one unique stable thumbnail URL per video.
- For key moments and video previews, the video files themselves also need stable URLs. This also lets Google confirm availability and collect signals.
- To guard against scrapers, you may verify Googlebot before serving stable media URLs. Example: serve `contentUrl` only to trusted clients such as Googlebot.

### Watch pages
- Create a dedicated watch page per video (where it makes business sense) to be eligible for video results on the main page, Video mode, Key Moments, Live Badge and other rich formats.
- A watch page's main purpose is showing one video. Examples that are watch pages: video landing page, TV episode player page, news video watch page, sports highlight page, events clip page.
- Not watch pages (video is secondary): blog post reviewing an embedded video, product page with a 360 video, category page listing several equal-prominence videos, movie review page with an embedded trailer.
- Each watch page needs a title and description unique to that video.
- The same video may also appear on a non-watch page; such a page can still be a text result and Google Image result with a video badge.

### Third-party embedded players (YouTube, Vimeo, Facebook)
- Google may index the video on your page and on the platform's page; both can appear in video features if they meet the criteria.
- Still provide structured data on your own watch page; you may include it in video sitemaps.
- For more features, make sure the video host allows Google to fetch the video file.

### The three URLs
- Watch page URL: the page embedding the video; in a video sitemap it is `<loc>`.
- Video player URL: a specific player, usually an `<iframe src>`. In structured data `VideoObject.embedUrl`; in a video sitemap `<video:player_loc>`.
- Video file URL: the actual content bytes (embedding site, CDN or streaming service). HTML: `<object data>`, `<source src>` in `<video>`, `<embed src>`. In structured data `VideoObject.contentUrl`; in a video sitemap `<video:content_loc>`.

### Thumbnail
- Valid thumbnail required for video features. If Google may fetch the video file it will try to generate one automatically.
- Provide your preferred thumbnail via: `poster` attribute on `<video>`; `<video:thumbnail_loc>` (or `<media:thumbnail>` in mRSS) in a video sitemap; `thumbnailUrl` in structured data; `og:video:image` in OGP.
- If several metadata sources specify a thumbnail, use the same thumbnail URL per video in all of them.
- Specs:
  - Formats: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF.
  - Size: minimum 60x30 px; larger preferred.
  - Location: accessible to Googlebot and Googlebot Images (not blocked by robots.txt or login); stable URL.
  - Transparency: at least 80% of pixels must have an alpha value above 250.

### Structured data consistency
- Describe videos with structured data. Data must be consistent with the actual video and other metadata.
- Provide unique `thumbnailUrl`, `name` and `description` for each video.

### Video features (no guarantee a markup yields a feature; not all features trigger on all queries)
- Video previews: Google picks a few seconds for a moving preview. Requires that Google may fetch the video file. Maximum preview duration is set with the `max-video-preview` robots meta tag.
- Key moments: chapter-like navigation of segments. Google detects segments automatically; your own markup takes priority (structured data or YouTube description).
  - Embedded or platform videos: `Clip` structured data (exact start/end time and a label per segment; all languages where Search is available) or `SeekToAction` structured data (tells Google the URL timestamp pattern so it can find key moments; supported languages: English, Spanish, Portuguese, Italian, Chinese, French, Japanese, German, Turkish, Korean, Dutch, Russian).
  - YouTube-hosted: timestamps and labels in the YouTube description (all languages); extra guidelines apply to enable YouTube Video Chapters.
  - Opt out of key moments entirely (including automatic ones): `nosnippet` meta tag.
- Live Badge: red "LIVE" badge for livestreams via `BroadcastEvent` structured data.

### Allow Google to fetch video files
- Google must fetch the actual video bytes for previews and key moments. Google doesn't expose the video file in results; users land on your site to watch.
- Don't block the actual video URL (for example the M3U8 streaming URL) with `noindex` or robots.txt.
- Video file at a stable URL; supply `contentUrl` with a supported file type via structured data.
- Both the watch page host and the video-serving host (for example `example.com` and `streamserver.example.com`) must meet Search technical requirements and have crawl capacity.
- With a CDN you may get Search Console crawl error notifications if you can verify ownership of your allocated URL space (subdomain or subdirectory reserved for your content).
- Googlebot can be verified.

### Remove or restrict videos
- Fast removal: file a removal request for the watch page embedding the video. For permanence the watch page must be gone or inaccessible to Google (`404`, `noindex` robots meta tag, or server-side authentication). Other pages or sites embedding the video are not removed unless you file requests for each.
- Ways to remove from your site: return `404` for every watch page embedding the removed or expired video (you may still serve the page HTML to users); add `noindex` robots meta to those pages; set an expiration date via `expires` in structured data or `<video:expiration_date>` in a video sitemap.
- Expired (past) date: video leaves video results; the watch page may still show as a text result without video thumbnail. Applies to expirations from sitemaps, structured data and meta tags. Easy to set a past date by mistake; omit expiration if the video doesn't expire.
- Location restrictions (omit if none):
  - Structured data: `regionsAllowed` (omit to allow all regions) or `ineligibleRegion` (regions that can't get the result).
  - Video sitemap: one `<video:restriction>` per video; space-delimited ISO 3166-1 two- or three-letter country codes; required attribute `relationship`. `allow` = appears only in the listed countries (empty list = appears nowhere). `deny` = appears everywhere except the listed countries (empty list = appears everywhere).

### SafeSearch
- Make sure Google understands the nature of your site so SafeSearch filtering can be applied where appropriate (labeling SafeSearch pages).

### Search Console
- Video indexing report: how many indexed watch pages have an indexed video, and reasons others weren't indexed.
- Video rich result report: fix issues in `VideoObject` markup.
- Performance report: "Videos" search appearance filter.
- A video troubleshooting guide exists for Search Console.

> Note: the page writes `contentURL` once (in "Allow Google to fetch your video files") but `contentUrl` elsewhere and in the property lists; the property is `VideoObject.contentUrl`.

## Translated results in Google Search
https://developers.google.com/search/docs/appearance/translated-results · Last updated: 2025-12-10

- Google may translate the title link and snippet of results that are not in the query language, when available, to widen audience reach.
- Target languages: Arabic, Bengali, English, French, German, Gujarati, Hindi, Indonesian, Kannada, Korean, Malayalam, Marathi, Persian, Portuguese, Spanish, Tamil, Telugu, Thai, Turkish, Urdu, Vietnamese. Mobile and desktop.
- Clicking a translated title link opens a machine-translated page; users can view the original result and the full original-language page.
- Google hosts no translated pages. It is equivalent to opening the page through Google Translate or Chrome in-browser translation, so page JavaScript, embedded images and other features are usually supported.
- Ad networks may need extra work for correct display after clicking a translated result (see next section).
- Monitoring: Search Appearance filter in the Performance report (clicks and impressions of translated results).
- Opt in: automatic, nothing to do. Opt out of all translation features in Google Search with `notranslate`:
  - `<meta name="robots" content="notranslate">` (all engines that support it)
  - `<meta name="googlebot" content="notranslate">` (Google only)
  - HTTP response header `X-Robots-Tag: notranslate`

## Ad networks and translation-related Google Search features
https://developers.google.com/search/docs/appearance/ad-network-and-translation · Last updated: 2025-12-10

### Approach
- On click of a translated result, Google fetches the page from the publisher, rewrites the source URL and translates it. Ad networks that rely on the publisher's source URL must convert the Google Translate URL back to the original.

### Decode the hostname (steps)
1. Take the hostname prefix, removing the `.translate.goog` suffix.
2. Split the `_x_tr_enc` parameter on `,` into `encoding_list`.
3. Prepend `_x_tr_hp` (if present) to the prefix.
4. If `encoding_list` contains `1` and the result starts with `1-`, remove `1-`.
5. If `encoding_list` contains `0` and the result starts with `0-`, remove `0-` and set `is_idn = true`; otherwise `is_idn = false`.
6. Replace the regex `/\b-\b/` with `.`.
7. Replace `--` with `-`.
8. If `is_idn`, prepend punycode prefix `xn--`.
9. Optional: convert to Unicode.
- Examples: `example-com.translate.goog` -> `example.com`; `foo--example-com.translate.goog` -> `foo-example.com`; `0-57hw060o-com.translate.goog/?_x_tr_enc=0` -> `xn--57hw060o.com`.

### Reconstruct the URL
- Use the original page URL, swap in the decoded hostname, remove all `_x_tr_*` parameters. Path, fragment and original parameters stay unchanged.
- The page ships sample JavaScript and a unit-test table; the table tests hostname decoding only.

## Enable Web Stories on Google
https://developers.google.com/search/docs/appearance/enable-web-stories · Last updated: 2026-07-01

### Overview and availability
- Web Stories: tap/swipe format mixing video, audio, images, animation, text. Steps: create the story, make sure it is valid AMP, verify metadata, check indexing, follow content policies.
- Search: can appear as a single result in all regions and languages where Search is available.
- Discover: can appear as one tap-through card in all regions and languages where Discover is available; most likely in the United States, India and Brazil.

### Create
- Web Stories are web pages: the same guidelines and best practices as regular pages apply.
- Options: a story editor tool (no code) or AMP (needs engineering). Test device sizes and formats with Chrome DevTools.

### Valid AMP
- Check with the Web Stories Google Test Tool, URL Inspection tool (valid AMP plus indexing status) or AMP Linter (command line during development).

### Metadata
- Required on every story: `publisher-logo-src`, `poster-portrait-src`, `title`, `publisher`.
- Verify the preview in the Web Stories Google Test Tool.

### Indexing check
- URL Inspection to submit individual URLs; Page Indexing report or Sitemaps report for status.
- If not indexed: link stories from the site or add them to the sitemap; every story must be canonical, with `<link rel="canonical">` pointing to itself (tell Google about localized versions of multi-language stories); make sure the URL isn't blocked by robots.txt or `noindex`.

## Best practices for creating Web Stories
https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices · Last updated: 2026-06-09

### Storytelling
- Critical: video first (more engaging than text or images; supplement with images and text).
- Recommended: bring your perspective (opinions, relatable); narrative arc (suspense page to page, payoff at the end).

### Design
- Critical:
  - Reduce character count: no multiple walls of text; about 280 characters per page.
  - Don't let other content block text; avoid burned-in text so it isn't blocked when resized.
  - Keep text within bounds (visible); avoid burned-in text so it doesn't overflow on other device sizes.
  - Use animations mindfully (avoid distracting or repetitive ones).
- Recommended: platform-neutral calls to action (remove Instagram/Snapchat/YouTube-specific CTAs; actions must be followable); full-bleed video and images; avoid low-resolution or distorted media (take care when resizing to portrait); high-resolution logo on the cover page; videos under 15 s per page, 60 s maximum; audio clips of at least 5 s with balanced volume and audible speech; consider auto-advance for video-only stories.

### SEO (a Web Story is still a web page; normal page SEO applies)
- Critical:
  - High-quality, complete-narrative content.
  - Title shorter than 90 characters; descriptive title shorter than 70 recommended.
  - Findable: no `noindex`; add stories to the sitemap; check the Index Coverage report and Sitemaps report.
  - Self-canonical (`link rel="canonical"` to itself); tell Google about localized versions.
  - Attach metadata: follow AMP story metadata guidelines; include normal page markup (`title` and `description` meta tags, structured data, OGP, Twitter card).
- Recommended: structured data; alt text on images; integrate stories into the site (link from home and category pages; optional landing page like `/stories`; no need for a story-specific URL pattern, reuse the site's URL structure); AMP story page attachments for extra detail; captions on video (not burned in); for video-only stories exported with baked-in text, add the exact displayed text as a `title` attribute on `amp-video` (only if semantic markup isn't possible; semantic HTML preferred); add landscape display support so stories can appear in desktop results.

### Technical
- Critical: valid AMP (test with the AMP Validator, fix errors); no text in the poster image (it could obstruct the title in previews); `poster-portrait-src` image at least 640x853 px, aspect ratio 3:4; `publisher-logo-src` image at least 96x96 px, aspect ratio 1:1.
- Recommended: include `og:image`.

> Note: this page recommends about 280 characters per page, while the content policy marks a story ineligible when the majority of pages exceed 180 characters. Treat 180 as the safer bound.

## Web Story content policy
https://developers.google.com/search/docs/appearance/web-stories-content-policy · Last updated: 2025-12-10

- For single results on Discover and Search, stories must comply with Discover policies, Google Search Essentials and Search's overall policies. For richer experiences (for example the carousel view) they must also comply with the Search Feature content policies and the policies below.
- Egregious violations: a site may be permanently excluded from richer Search experiences.
- Not allowed:
  - Copyright infringement: no third-party copyrighted work without permission. Google takes no responsibility for rights; infringing stories may be blocked.
  - Text-heavy stories: may be ineligible if most pages have more than 180 characters of text. Bite-sized video under 60 seconds per page is encouraged.
  - Low-quality assets: stretched or pixelated images/video that hurt the experience.
  - Lack of narrative: no binding theme or structure page to page.
  - Incomplete stories: incomplete, or needing clicks to other sites or apps for essential information.
  - Overly commercial: sole purpose to advertise a product or service, especially when you benefit directly. Affiliate links are fine if limited to a minor part. Display ads may follow the Story Ad Guidelines. Good affiliate programs are supported per the web search spam policies.

## Regional differences in Search experience (overview)
https://developers.google.com/search/docs/appearance/aggregator-features · Last updated: 2026-09-18

- Google is evolving results pages for some query types to create opportunities for Vertical Search Services (VSS), Comparison Shopping Services (CSS), direct suppliers and content providers.
- Features by region (region: EEA / South Africa / Türkiye):
  - Aggregator unit (region: EEA): hotels, flights, ground transportation, local businesses, products.
  - Supplier unit (region: EEA): same query types.
  - Ecosystem carousel (region: EEA): weather, sports, finance, translate.
  - Job sites features (region: EEA): jobs.
  - Places sites features (region: Türkiye): hotels, local businesses.
  - South Africa badge and refinement chip (region: South Africa): travel, products, car hire, food delivery, ground transportation.
  - Structured data carousels (beta), also called host carousels:
    - EEA: hotels, local businesses, things to do, products, ground transportation, flights, vacation rentals.
    - South Africa: hotels, things to do, flights, products, food delivery, car hire, vacation rentals, ground transportation.
    - Türkiye: hotels, local businesses, vacation rentals.
- Filter dimensions on the page: region (EEA, South Africa, Türkiye) and query type (car hire, finance, flights, food delivery, ground transportation, hotels, jobs, local businesses, products, sports, things to do, translate, travel, vacation rentals, weather).

## Aggregator unit in Google Search
https://developers.google.com/search/docs/appearance/aggregator-unit · Last updated: 2026-10-19

### How it works (region: EEA)
- Multi-provider unit for Vertical Search Services: Online Travel Agencies, Comparison Shopping Services, metasearch engines, directories.
- Eligible aggregators populate the unit with results relevant to the query; the top-ranked provider is expanded by default (for example a hotel list with photos, prices or star ratings). Clicks go to the aggregator's web page.
- Users can switch to an alternative aggregator; only one aggregator unit shows at a time.
- A supplier unit for direct providers appears alongside.

### Availability
- Users in the EEA; queries for hotels, flights, long distance trains or buses, products, local businesses.

### Eligibility
- Approved as a VSS, provide required data, meet quality standards.
- Express interest if you serve EEA users: ground transportation, flights, hotels, local businesses use the Google Search Aggregator Features form; products use the comparison shopping services contact form.
- Relevant content for the respective query type.
- Data: direct data feed integrations or real-time APIs (flights, long distance trains and buses). Per vertical: hotels = Lodging Point of Interest Feed; ground transportation = Transport features API; flights = Partner standard Live API; products = product pages across Google (Merchant program); local businesses = Local Point of Interest Feed.
- Comply with Search content policies.

### Best practices
- Flight and transport units use real-time APIs; lodging and local business units use feeds.
- Rich entity details: images, descriptions and specs, verified ratings and review counts, specific categories (for example "Boutique hotel" rather than "Hotel"), amenities, features, operating hours.
- Accurate titles: factual, descriptive, title case; avoid all caps, excessive punctuation, emoji and promotional text such as "BEST DEALS" or "Free shipping" in entity names.
- High-quality original imagery with clean backgrounds, no watermarks or promo overlay badges; high resolution where possible.
- Prices and availability in feeds should match the landing page as closely as possible; refresh regularly and remove expired or out-of-stock listings.
- Monitor performance in Search Console.
- Display is based on what is most helpful for the query (Search Quality Rater Guidelines are referenced).

## Supplier unit in Google Search
https://developers.google.com/search/docs/appearance/supplier-unit · Last updated: 2026-09-18

- (region: EEA) Dedicated unit for direct providers (individual hotels or airlines, brick-and-mortar owners, service providers such as plumbers). Shown alongside the aggregator unit and only when the aggregator unit appears.
- Availability: EEA users, when the aggregator unit shows for hotel, flight, long distance train or bus, product and local business queries.
- Eligibility: the site serves users in the EEA and the business is a direct provider for those query types.
- No extra data beyond what crawling finds is needed; results can be enhanced with supplier feeds if available.

## Ecosystem carousel in Google Search
https://developers.google.com/search/docs/appearance/ecosystem-carousel · Last updated: 2026-09-08

- (region: EEA) Carousel that may show for queries needing data visualization or data interactivity: stock charts, weather, sports scores, translation. Desktop and mobile. Queries: weather, sports, finance, translate.
- A tile click goes directly to that website. Order comes from Search ranking algorithms using non-discriminatory ranking principles, relevant to location and language.
- Requirements: site serves EEA users; publishes finance, weather or sports information or provides translation; is an authoritative source or specialized provider (for example major media outlets, commercial weather services).
- No new structured data or special feeds required.
- Express interest via the interest form.

## Job sites: aggregator carousel and refinement chip
https://developers.google.com/search/docs/appearance/job-sites · Last updated: 2026-09-11

- (region: EEA) "Job sites" aggregator carousel shows top aggregator results for job queries; "More sites" reveals more aggregators. A "Job sites" refinement chip focuses the page on aggregator text results; activate at the top of the results page or via "More sites".
- No markup needed.
- Express interest via the interest form if you serve EEA users.

## Places sites: aggregator carousel and refinement chip
https://developers.google.com/search/docs/appearance/places-sites · Last updated: 2026-09-11

- (region: Türkiye) "Places sites" aggregator carousel and refinement chip for local business and hotel queries; same mechanics as job sites ("More sites", chip at top or via "More sites").
- No markup needed.
- Express interest via the interest form if you serve users in Türkiye.

## Search experiences in South Africa: badge and refinement chip
https://developers.google.com/search/docs/appearance/south-africa-features · Last updated: 2026-09-08

- (region: South Africa) Goals: improve visibility of South African platforms; make filtering and exploring South African results easier.
- "South African" badge: shown on applicable web results and ads from eligible South African platforms. It doesn't change ranking. Web results: travel, car hire, bus booking, products, food delivery queries. Ads: travel and shopping.
- "South African" refinement chip: at the top of results; narrows to eligible South African travel and shopping platforms. No markup needed.
- Launched for eligible sites in South Africa only; businesses based there can express interest via the interest form.

> Note: the overview page lists "ground transportation" for South Africa; this page says "bus booking".

## Structured data carousels (beta)
https://developers.google.com/search/docs/appearance/structured-data/carousels-beta · Last updated: 2026-09-11

### Feature and availability (beta) (region: EEA, Türkiye, South Africa)
- Horizontally scrollable list-like rich result ("host carousel") of entities from one site; tiles may show price, rating and images.
- Eligible with `ItemList` plus at least one supported item type: `LocalBusiness` and subtypes (`Restaurant`, `Hotel`, `VacationRental`, ...), `Product`, `Event`.
- Beta: requirements and guidelines may change. Desktop and mobile only in these regions:
  - EEA: hotels, vacation rentals, ground transportation, flights, local businesses, things to do (events, tours, activities), products.
  - Türkiye: hotels, vacation rentals, local businesses only.
  - South Africa: hotels, vacation rentals, things to do, flights, products, food delivery, car hire, bus booking.
- Forms to fill in: EEA or Türkiye: aggregator features interest form (ground transportation, hotels, vacation rentals, local business, things to do); flight queries interest form (flights); Comparison Shopping Services program for products in CSS Program countries. South Africa-based businesses: the South African Badging and Refinement Chips interest form.

### Add structured data (steps)
- Pick one summary page containing information on every listed entity (for example "Top hotels in Paris" linking to detail pages). Mixed entity types are allowed (for example hotels and restaurants).
- Put markup on that summary page only; detail pages need no markup.
- Add required and recommended properties for the content type. Use the closest type (for example both `Hotel` and `VacationRental` for a mixed list); generic `LocalBusiness` is allowed.
- Follow guidelines, validate in the Rich Results Test, deploy a few pages, check with URL Inspection (not blocked by robots.txt, `noindex` or login), request recrawl, submit a sitemap (can be automated via the Search Console Sitemap API). Allow days for recrawl.

### Guidelines
- Follow Search Essentials and the general structured data guidelines.
- Generic types are allowed, but recommended properties need the matching type (for example `amenityFeature` needs `LodgingBusiness`).
- Extra fields are allowed but may not display.
- A summary page plus multiple detail pages is required. Not supported: an all-in-one page with anchors as the "details".
- Summary or category page: list-like, at least three entities, links out to other pages; detail page URLs must be in the markup.
- Mark up all items on the page. Paginated categories: an `ItemList` on each page with that page's entities. Infinite scroll: mark up entities initially loaded in the viewport.
- Markup order = tile order in the carousel.

### Property reference
- `ItemList` (container; all item URLs must be different pages on the same domain)
  - Required `itemListElement` (`ListItem`): at least three `itemListElement.item` entries.
  - Required `itemListElement.item`: subtype of `LocalBusiness`, `Product` or `Event`, carrying the common properties (`image`, `url`, `name`) plus the type's properties.
  - Required `itemListElement.position` (`Integer`): 1-based position.
- Common item properties
  - Required `image` (repeated `URL` or `ImageObject`): images of the entity (no logos); crawlable and indexable URLs; must represent the marked up content; Google Images supported file format; best results with multiple high-resolution images (at least 50K pixels, width times height) in aspect ratios 16x9, 4x3 and 1x1.
  - Required `name` (`Text`): shown as the tile title; HTML formatting ignored.
  - Required `url` (`URL`): canonical URL of the standalone detail page. Unique per item; same domain (or sub/super domain) as the summary page. Anchor links within the summary page are not supported.
  - Recommended `aggregateRating.ratingValue` (`Number` or `Text`): number, fraction or percentage; default scale 1-5; use `bestRating`/`worstRating` for other scales; decimals use a dot (in microdata/RDFa use a `content` attribute to keep a visible comma).
  - Recommended `aggregateRating.bestRating` (`Number`; default 5 if omitted).
  - Recommended `aggregateRating.ratingCount` (`Number`): total ratings on your site.
- `LocalBusiness` (and subtypes), nest under `itemListElement.item`; all recommended
  - `amenityFeature` (`LocationFeatureSpecification`): `LodgingBusiness` only; `name` and `value` pairs (for example `beachAccess` true).
  - `priceRange` (`Text`): price level ("$", "$$$") or range ("$-$$"); must be shorter than 12 characters or no price range is shown.
  - `servesCuisine` (`Text`): restaurants only.
- `Product`, nest under `itemListElement.item`; all recommended
  - `offers` (`Offer` or `AggregateOffer`): for `Offer` use `offers.price` and `offers.priceCurrency`; for `AggregateOffer` use `offers.lowPrice`, `offers.highPrice` and `offers.priceCurrency`.
  - `offers.price` (`Number`): omit when giving a low/high range. `offers.lowPrice` / `offers.highPrice` (`Number`): omit when giving a single `price`.
  - `offers.priceCurrency` (`Text`): ISO 4217 three-letter code; defaults to `USD` if missing.
- `Event`, nest under `itemListElement.item`; all recommended
  - `offers` as for `Product`. `offers.price` is the ticket price including service charges and fees; keep it updated as prices change or tickets sell out; use `0` if the event is free.
  - `offers.lowPrice`, `offers.highPrice`, `offers.priceCurrency` as above (`USD` default).

### Examples (key lessons)
- Restaurant list: each tile carries `image` array (1x1, 4x3, 16x9), `priceRange`, `servesCuisine`, `aggregateRating`, `url`.
- Lodging list: `Hotel` and `VacationRental` mixed in one `ItemList`; `amenityFeature` per item.
- Things to do: mixes `Event` (with `offers`) and `LocalBusiness` in one list.
- Products: `AggregateOffer` for series, `Offer` for single price.
- Skeleton: `ItemList` > `itemListElement[]` > `ListItem` (`position`, `item` with `@type`, `name`, `image`, `url`, ...).

### Troubleshooting
- Ask the CMS owner for help and forward Search Console messages. No guarantee that structured data shows as a rich result (general guidelines list reasons).
- Check structured data errors and the Unparsable structured data report.
- A structured data manual action makes the page's markup ignored (the page can still rank); fix via the Manual Actions report.
- Review guidelines: problems may be spammy content or markup that the Rich Results Test can't detect.
- Use the "Troubleshoot missing rich results / drop in total rich results" guide; allow time for recrawl; use the crawling and indexing FAQ and the Search Central forum.

> Note: property lists recommend `aggregateRating.ratingCount`, but every code example uses `reviewCount`. The two are both schema.org review count fields; the page does not say which Google prefers.
> Note: the example headings say "Top 5" but each shows three items (the minimum).

## Package tracking Early Adopters Program
https://developers.google.com/search/docs/appearance/package-tracking · Last updated: 2026-07-14

- The program is no longer accepting new partners. Available in all languages and countries where Search is available.
- Feature: users enter a package ID in Search; Google calls the carrier's API and displays tracking info.
- API requirements: almost no downtime; average response within 700 ms with the 95th percentile at most 1,000 ms. If not met, Google may stop showing the data.
- Required field: `CurrentStatus` (current status, with the date and time it became valid and any error states).
- Strongly recommended fields: `DeliveredDate`, `PromisedDate`, `TrackingNumber`, `TrackingURL`, `SupportPhoneNumbers` (per region), `TransitEvents` (Day, Time, City, State, Country where applicable), `CreateDate`, `PickupDate`, `TimestampEvent`, `LocationEvent`, `CanReschedule`.
- Not accepted: any personal data about the recipient or sender; any geographic information about the recipient or sender.

## UGC Fresh Data Program
https://developers.google.com/search/docs/appearance/ugc-fresh-data-program · Last updated: 2026-10-08

- Program for platforms to push fresh, high-quality, authentic user-generated content and interaction signals through a dedicated ingestion pipeline. Applies to trending UGC only; independent of the Google Indexing API and ordinary organic crawling. No guarantee that content appears in Search.
- Eligibility (all):
  - Content focus: platform mainly hosts UGC, social posts or forum discussions, on dedicated pages with stable URLs (not profile or feed pages). UGC = material created entirely by independent users, not the platform.
  - Volume and audience: high volume of UGC and a significant user base.
  - Accessibility: public pages accessible to Googlebot and users; gated content (login or paywall) is ineligible; all UGC attributable to a creator with a public profile.
  - Technical readiness: secure OAuth 2.0 API authentication; strictly validated JSON-LD payloads; valid on-page schema.org markup already in use or planned (for example `SocialMediaPosting` or `DiscussionForumPosting` with `interactionStatistic`).
  - Content health: no illegal content; active moderation including a user reporting mechanism.
  - Freshness: submit content as fast as possible (ideally within minutes); submit engagement counter updates regularly (within 72 hours of creation). Developer docs shared after acceptance.
- Application: form-based; acceptance not guaranteed; response within 6-8 weeks; selected platforms get integration documentation and onboarding.
