# Indexing: JavaScript SEO, page metadata, meta tags, robots meta / X-Robots-Tag, noindex, rel attributes, removals, redirects, site moves, A/B testing, pausing a site: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Control what you share with Google
https://developers.google.com/search/docs/crawling-indexing/control-what-you-share · Last updated: 2026-10-21

### Why block content
- Restrict data meant only for users already on the site; files can also carry metadata that shows up in Search.
- Hide low-value content (for example user-generated content that may be low quality or spam); indexing it can hurt site ranking.
- Focus Google on important content: for very large sites (over hundreds of thousands of URLs) with unimportant or duplicate pages, block those from crawling.

### Methods (with applicability)
- Remove the content from the site: all content types; the only way to keep it out of Search and everywhere else on the internet.
- Password-protect files: all content types; also eventually drops already-indexed content.
- `noindex` rule (robots `meta`): all content types; content stays linkable and visitable, just not in results.
- Disallow crawling with robots.txt: images and video only. Google indexes only images/videos Googlebot may crawl.
- Robots `meta` tag, `data-nosnippet`, `X-Robots-Tag`: various content types; adjust how content is presented.
- Search generative AI control in Search Console: site-wide; manages inclusion in generative AI features (AI Overviews, AI Mode).
- Opt out of specific Google properties (Google Shopping, Google Hotels, vacation rentals): web pages.
- Already-indexed content: request removal (see Page removals).

## Understand the JavaScript SEO basics
https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics · Last updated: 2026-03-04

### How Google processes JavaScript
- Three phases: crawling, rendering, indexing. Google runs JS with an evergreen Chromium.
- Crawl: Googlebot takes a URL from the crawl queue, checks robots.txt first. If disallowed it makes no HTTP request, and Google won't render JS from blocked files or on blocked pages.
- Googlebot parses the HTML response for URLs in `href` attributes of links and queues them. Prevent discovery with `nofollow`. JS-injected links are fine if they follow crawlable-link best practices.
- App shell model: initial HTML lacks content and Google must execute JS to see it.
- Render queue: every page with HTTP `200` is queued for rendering (JS present or not), unless a robots `meta` tag or header says not to index. Wait can be seconds or longer. Non-`200` pages (for example `404`) may skip rendering.
- Headless Chromium renders, then Googlebot re-parses rendered HTML for links and indexes from the rendered HTML.
- Server-side or pre-rendering is still recommended: faster for users and crawlers, and not all bots run JS.

### Titles, snippets, canonical
- JS may set or change `<title>` and the meta description.
- `rel="canonical"`: best set in HTML. If JS is used, it must equal the canonical in the original HTML; never change it to a different URL. If it cannot be in HTML, JS may set it and the HTML omits it.
- Injected canonical is picked up at render time. There must be exactly one `rel="canonical"` `<link>`; multiple or modified ones give unexpected results.

### Code compatibility
- Google supports only some APIs and JS features. Use differential serving and polyfills when feature detection finds a missing API (some features cannot be polyfilled; check polyfill docs).

### HTTP status codes and soft 404 in single-page apps
- Use meaningful codes: `404` for not found, `401` for login-protected, redirect codes for moved pages.
- Client-side routed SPAs often cannot return real status codes. Two strategies to avoid `soft 404`:
  - JS redirect (`window.location.href`) to a URL the server answers with `404` (for example `/not-found`).
  - Add `<meta name="robots" content="noindex">` to error pages via JS (example assumes no other robots meta exists).

### History API instead of fragments
- Google discovers links only as `<a>` elements with an `href` attribute.
- Do not load views via fragments (`#/products`); Googlebot cannot reliably resolve them. Use real paths (`/products`) with `history.pushState` and `preventDefault` on click.

### Robots meta in JS
- JS may add or change a robots `meta` tag (example: set `noindex` when an API returns an error).
- If Google sees `noindex` in the original page code it may skip rendering and JS execution, so JS that removes or changes `noindex` may not work. To have a page indexed, do not ship `noindex` in the original code.

### Caching
- Googlebot caches aggressively; the Web Rendering Service (WRS) may ignore caching headers and use stale JS/CSS. Use content fingerprinting in file names (like `main.2bb85551.js`).

### Structured data, web components, lazy loading
- JS-generated JSON-LD is allowed; test it.
- Web components are supported. Google flattens shadow DOM and light DOM, so only content visible in rendered HTML is indexable. Use a `<slot>` to project light DOM content into shadow DOM. Verify with Rich Results Test or URL Inspection Tool (rendered HTML).
- Lazy-load images per the lazy-loading guidelines (next pages).

## Fix search-related JavaScript problems
https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript · Last updated: 2025-12-18

### Context
- Googlebot prioritizes crawling without degrading user experience; it and WRS skip resources not contributing to essential content (for example reporting and error requests). Client-side analytics therefore do not give an accurate picture of Googlebot/WRS activity; use the Crawl Stats report in Search Console.

### Debugging checklist
- Test with Rich Results Test or URL Inspection Tool: shows loaded resources, JS console output, exceptions, rendered DOM.
- Optionally log JS errors from real users and Googlebot via `window.addEventListener('error', …)` (to the page for debugging or to a remote endpoint). Parse errors cannot be caught this way.
- Prevent `soft 404` in SPAs: same two strategies as above (redirect to a server `404` URL; add or change robots `meta` to `noindex`). SPAs that handle errors client-side often return `200`, so error pages can get indexed and shown.
- Expect Googlebot to decline permission requests (for example camera); give an alternative path to content.
- No URL fragments for different content. The AJAX-crawling scheme has been deprecated since 2015; use the History API.
- Do not rely on data persistence: WRS loads each URL like a browser (follows server and client redirects) but clears Local Storage, Session Storage and HTTP cookies across page loads.
- Use content fingerprinting for cache problems (WRS may ignore caching headers).
- Feature-detect every critical API and provide fallback or polyfill. Example: Googlebot does not support WebGL; skip the effect or server-prerender it.
- Content must work over plain HTTP: no support for `WebSockets` or `WebRTC`; provide an HTTP fallback with error handling.
- Web components: check rendered HTML; WRS flattens light and shadow DOM, so components must use `<slot>` for light DOM content, otherwise consult the component docs or pick another.
- JS paywalls: shipping full content in the server response and hiding it with JS is not a reliable access limit; only deliver full content after subscription is confirmed.
- After fixes, re-test with Rich Results Test or URL Inspection; a green check and no errors means fixed. Otherwise ask in the Search Central help community.

## Dynamic rendering as a workaround
https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering · Last updated: 2025-12-10

- Dynamic rendering was a workaround, not a long-term solution; recommended instead: server-side rendering, static rendering, or hydration. It adds complexity and resource needs.
- Mechanism: the server detects crawlers (for example by user agent) that can't handle JS-generated content and routes them to a renderer that returns static HTML; users get the client-side rendered version. Can be enabled for all pages or per page.
- Intended for indexable, public, rapidly changing JS content, or content using JS features unsupported by target crawlers. Other search engines may ignore JS entirely.
- Not cloaking as long as content is similar. Error pages produced while setting it up are treated as ordinary error pages, not cloaking.
- Serving completely different content to users and crawlers (a page about cats to users, about dogs to crawlers) is cloaking.

## Fix lazy-loaded content
https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading · Last updated: 2025-12-10

### Load when visible in viewport
- Lazy-loading must load all relevant content whenever it enters the viewport. Google does not interact with the page (no scrolling or clicking).
- Valid methods: browser built-in lazy-loading for images and iframes; `IntersectionObserver` API plus polyfill; a JS library that loads on viewport entry.
- Don't lazy-load content likely visible immediately on open (slows display, noticeable to users). Test the implementation.

### Infinite scroll
- Give each chunk its own persistent, unique URL whose content is the same on every load; use absolute page numbers (`?page=12`), not relative ones (`?date=yesterday`).
- Link sequentially between the chunk URLs so they are discoverable (see pagination best practices).
- When a new chunk becomes the primary visible element, update the displayed URL with the History API.

### Test
- URL Inspection Tool: confirm content is in rendered HTML. Image/video URLs in `src` of `<img>`/`<video>` in rendered HTML means the setup works.

## Page metadata
https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata · Last updated: 2025-12-10

- Use valid HTML in `<head>`. Google tries to cope with invalid HTML, but errors can break how metadata is used.
- Valid `<head>` children only: `title`, `meta`, `link`, `script`, `style`, `base`, `noscript`, `template`.
- Invalid elements commonly found in `<head>`: `iframe`, `img`. On meeting an invalid element Google assumes `<head>` ended and ignores all later head elements.
- If an invalid element is unavoidable, place it after every element you want Google to read.

## Meta tags and HTML attributes that Google supports
https://developers.google.com/search/docs/crawling-indexing/special-tags · Last updated: 2025-12-10

### General
- `meta` tags go in `<head>`; clients ignore tags they don't support. CMS users: use the CMS search-settings or head-editing mechanism.
- Google reads both HTML and XHTML-style meta tags. `<head>` must be valid HTML with parent tags closed. Letter case doesn't matter except for `google-site-verification`.
- Other (unsupported) meta tags may be used but Google ignores them.
- Avoid injecting or changing meta tags with JS where possible; test thoroughly if you must. Check tags with URL Inspection Tool.

### Supported meta tags
- `<meta name="description" content="…">`: short page description; sometimes used in the snippet.
- `<meta name="robots" content="…, …">` and `<meta name="googlebot" content="…, …">`: control crawling/indexing behavior. `robots` applies to all search engines, `googlebot` only to Google. Conflicts: the more restrictive applies (`max-snippet:50` plus `nosnippet` gives `nosnippet`). Defaults are `index, follow` (no need to specify). Also available as `X-Robots-Tag` header, useful for non-HTML files.
- `<meta name="googlebot" content="notranslate">`: no translated title link/snippet for that page (otherwise Google may offer one, after which the user's interaction runs through Google Translate).
- `<meta name="google" content="nopagereadaloud">`: prevents Google text-to-speech services reading the page aloud.
- `<meta name="google-site-verification" content="…">`: Search Console ownership verification on the top-level page; `name` and `content` must match the provided values exactly, including case.
- `<meta http-equiv="Content-Type" content="…; charset=…">` and `<meta charset="…">`: content type and character set. Quote the `content` value of the `http-equiv` form or `charset` may be misread. UTF-8 recommended.
- `<meta http-equiv="refresh" content="…;url=…">` (meta refresh): redirect after a delay; not supported by all browsers and can confuse users; use server-side `301` instead.
- `<meta name="viewport" content="…">`: render instructions for mobile; its presence signals mobile-friendly to Google.
- `<meta name="rating" content="adult">` or `content="RTA-5042-1996-1400-1577-RTA"`: labels sexually explicit adult content so SafeSearch filters it.

### Supported HTML attributes
- `src`, `href` are used to discover resources and URLs.
- Various `rel` values qualify outbound links (see rel attributes).
- `data-nosnippet` on `div`, `span`, `section` excludes parts of the page from snippets.

### Unsupported (ignored)
- `<meta name="keywords">`: no effect on indexing or ranking.
- HTML `lang` attribute: Google detects language from the text content.
- `<link rel="next">` and `<link rel="prev">`: no longer used, no effect on indexing.
- `<meta name="google" content="nositelinkssearchbox">`: feature no longer exists.

## Robots meta tag, data-nosnippet, and X-Robots-Tag specifications
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag · Last updated: 2026-03-24

### Basics
- Page-level settings: `meta` tag in HTML or HTTP header. Text-level: `data-nosnippet` attribute.
- Settings are read only if crawlers may access the page.
- `<meta name="robots">` targets search crawlers. Non-search crawlers (for example `AdsBot-Google`) need their own tag, such as `<meta name="AdsBot-Google" content="noindex">`.

### Robots `meta` tag
- Put in `<head>`. `name` and `content` are case-insensitive. `name="robots"` addresses all crawlers; to address one, use its user agent token. Google recognizes only two tokens in meta (others ignored):
  - `googlebot`: all text results.
  - `googlebot-news`: news results.
- Several crawlers with different rules: use several tags (for example `googlebot` `notranslate` plus `googlebot-news` `nosnippet`).
- Google does not enforce placement in `<head>`; a robots meta in `<body>` is also respected.
- Non-HTML resources (PDF, video, images): use `X-Robots-Tag` header.

### `X-Robots-Tag` HTTP header
- Any rule valid in the robots meta can be sent as `X-Robots-Tag: <rule>`.
- Multiple headers allowed, or one comma-separated list (for example `X-Robots-Tag: noimageindex` plus `X-Robots-Tag: unavailable_after: 25 Jun 2010 15:00:00 PST`).
- Optional user-agent prefix: `X-Robots-Tag: googlebot: nofollow` / `X-Robots-Tag: otherbot: noindex, nofollow`. Rules with no user agent apply to all crawlers.
- Header name, user agent and values are case-insensitive.
- Conflicting rules: the more restrictive wins.
- Implementation: web server config (Apache `.htaccess`/`httpd.conf`, NGINX `.conf`), site-wide with regex matching; per-file possible.
  - Apache: `<Files ~ "\.pdf$"> Header set X-Robots-Tag "noindex, nofollow" </Files>`; images: `<Files ~ "\.(png|jpe?g|gif)$"> Header set X-Robots-Tag "noindex" </Files>`; single file: `<Files "unicorn.pdf">` (htaccess in that directory).
  - NGINX: `location ~* \.pdf$ { add_header X-Robots-Tag "noindex, nofollow"; }`; images: `location ~* \.(png|jpe?g|gif)$ { add_header X-Robots-Tag "noindex"; }`; single file: `location = /secrets/unicorn.pdf { … }`.

### Valid indexing and serving rules (meta and header; case-insensitive; combine with commas or separate tags; other search engines may treat them differently)
- `all`: no restrictions; default, no effect if listed.
- `noindex`: do not show page, media or resource in results. Without it the item may be indexed.
- `nofollow`: do not follow links on the page; without it Google may use them to discover pages.
- `none`: equals `noindex, nofollow`.
- `nosnippet`: no text snippet or video preview. A static image thumbnail may still show if it improves UX. Applies to all result forms (web search, Google Images, Discover, AI Overviews, AI Mode) and prevents use of the content as direct input for AI Overviews and AI Mode. Use `data-nosnippet` to exclude only sections.
- `indexifembedded`: allows indexing of the content when embedded in another page via `iframe` or similar, despite `noindex`. Only has an effect together with `noindex`.
- `max-snippet:[number]`: max characters of text snippet (a URL can appear as several results). Does not affect image/video previews. Applies to all result forms incl. AI Overviews and AI Mode, limiting direct input. Not applied where the publisher separately granted permission (in-page structured data, license agreement). Ignored if number is unparseable. Special values: `0` = no snippet (same as `nosnippet`); `-1` = Google chooses length. Without it Google chooses.
- `max-image-preview:[setting]`: `none` (no preview), `standard` (default size), `large` (up to viewport width). Applies to web search, Google Images, Discover, Assistant. Does not override separately granted permission (in-page structured data such as AMP and canonical article versions, license deals). To stop larger thumbnails for AMP and canonical article versions in Search/Discover use `standard` or `none`. Without it a default-size preview may show.
- `max-video-preview:[number]`: max seconds of video snippet. `0` = at most a static image (per `max-image-preview`); `-1` = no limit. Applies to web search, Google Images, Google Videos, Discover, Assistant. Ignored if unparseable.
- `notranslate`: no translation offer for the page's title link and snippet (otherwise offered for results not in the query language; clicking leads into Google Translate for all further interaction).
- `noimageindex`: do not index images on the page.
- `unavailable_after:[date/time]`: no display in results after that date/time. Formats: RFC 822, RFC 850, ISO 8601 and similar widely adopted. Ignored if invalid. Default is no expiry. Googlebot sharply reduces crawl rate of the URL after the date.

### Historical or unused rules (ignored by Google Search)
- `noarchive`: no longer used; the cached link feature no longer exists.
- `nocache`: not used.
- `nositelinkssearchbox`: no longer used; feature gone.

### Combining rules
- Comma list: `noindex, nofollow`; or separate tags: `noindex` and `nofollow` each in its own `<meta name="robots">`.
- Example mix: `max-snippet:20, max-image-preview:large`.
- Different crawlers with different rules: the sum of the negative rules applies. `robots: nofollow` plus `googlebot: noindex` means `noindex, nofollow` for Googlebot.

### `data-nosnippet`
- Valid only on `span`, `div`, `section`. Boolean attribute: any value (even `"false"`) is ignored, so it always applies.
- HTML must be valid with all tags closed; an unclosed `div` swallows all following content. `<mytag data-nosnippet>` is invalid.
- Extraction may happen before and after rendering (rendering is not guaranteed). Don't add or remove `data-nosnippet` on existing nodes with JS; include it when JS first adds the element. For custom elements wrap them in `div`, `span` or `section`.

### Structured data interaction
- Robots meta limits don't restrict use of schema.org structured data, except `article.description` and `description` of other creative works, which `max-snippet` limits. Example: `recipe` markup stays eligible for the recipe carousel even if the text preview is limited.
- To control structured-data usage, edit the structured data itself. Structured data in a `data-nosnippet` element remains usable for search results.

### robots.txt interaction
- Meta tags and `X-Robots-Tag` are found only on crawl. A URL disallowed in robots.txt never reveals its rules, so they are ignored. URLs whose rules must be obeyed must not be disallowed.

## noindex
https://developers.google.com/search/docs/crawling-indexing/block-indexing · Last updated: 2025-12-10

### Core
- `noindex` via `<meta>` or HTTP response header; when Googlebot crawls and extracts it, the page is dropped from Search entirely, regardless of inbound links.
- Must be crawlable: not blocked by robots.txt and otherwise accessible, else Google never sees it and the page can still appear (for example via links from other pages).
- Useful without root server access (page-by-page control).
- `noindex` in robots.txt is not supported by Google.
- Can be combined with other rules, for example `<meta name="robots" content="noindex, nofollow" />`.

### Implementation
- All engines supporting it: `<meta name="robots" content="noindex">` in `<head>`. Google only: `<meta name="googlebot" content="noindex">`. Other engines may interpret differently and could still show the page.
- Header: `X-Robots-Tag: noindex` (or `none`); usable for PDFs, video, images.
- CMS users: use the CMS settings mechanism for meta tags.

### Debugging
- If a page still shows up, Google probably hasn't recrawled since the rule was added; for less important pages this can take months. Request recrawl in URL Inspection tool.
- For quick removal use the Removals tool.
- Check robots.txt isn't blocking the URL (edit it to unblock).
- Verify Googlebot sees the rule: URL Inspection tool shows the HTML Googlebot received. Page Indexing report lists pages where Googlebot extracted a `noindex`.

## rel attributes (Qualify your outbound links)
https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links · Last updated: 2025-12-10

- Normal links need no `rel`. Otherwise use on `<a>`:
  - `rel="sponsored"`: ads and paid placements (paid links). `nofollow` was previously recommended for these and is still acceptable, `sponsored` preferred.
  - `rel="ugc"`: recommended for user-generated content links (comments, forum posts). Optionally remove it for trusted contributors with consistently high-quality contributions.
  - `rel="nofollow"`: when other values don't fit and you prefer Google not associate your site with or crawl the target. For links within your own site use robots.txt `disallow`.
- Multiple values: space- or comma-separated (`rel="ugc nofollow"`, `rel="ugc,nofollow"`).
- Qualified links are generally not followed, but targets may still be crawled via sitemaps or other sites' links.
- `rel` values work only on `<a>` elements Google can crawl; `nofollow` additionally exists as a robots meta rule.
- To prevent indexing: allow crawling and use `noindex`.

## Page removals
https://developers.google.com/search/docs/crawling-indexing/remove-information · Last updated: 2025-12-10

- Not your page: use "Remove your personal information from Google".
- Quick removal: Removals tool removes a page from results within a day.
- Remove or protect all URL variations of the content (for example `example.com/puppies`, `example.com/PUPPIES`, `example.com/petchooser?pet=puppies`).
- Removals tool requests last about 6 months. For permanence:
  - Remove or update the content (most secure; also covers engines that ignore `noindex`).
  - Password-protect the page.
  - Add `noindex` (only blocks Google results; users and engines ignoring `noindex` can still access).
  - Don't use robots.txt to block the page.
- Images: see Image removals. Other properties (Google Shopping etc.: opt out per property; Business Profile: edit info; knowledge panel: update).

## Image removals
https://developers.google.com/search/docs/crawling-indexing/prevent-images-on-your-page · Last updated: 2025-12-10

- Emergency: Removals tool; images may reappear when the request expires unless also removed or blocked.
- Non-emergency, two equal methods (using both is pointless, because Googlebot must crawl the URL to see headers): robots.txt `disallow`, or `noindex` `X-Robots-Tag` header on the image URL.
- Without access to the host (for example a CDN) or without such options, delete the images.
- robots.txt: put in site root hosting the image. Slower than the Removals tool but flexible (wildcards, subpaths) and applies to all search engines.
  - Single: `User-agent: Googlebot-Image` + `Disallow: /images/dogs.jpg`.
  - Many: one `Disallow` each, or `*` wildcard, for example `Disallow: /images/animal-picture-*.jpg`.
  - All images: `Disallow: /`. By file type: `Disallow: /*.gif$`.
  - `Googlebot-Image` excludes from Google Images; `Googlebot` excludes from all Google searches.
- Header method: crawling of the image URLs must be allowed.
- `noimageindex` on a page blocks images embedded in that page only; if the image appears on other pages it may be indexed there. For a guaranteed block use `noindex` `X-Robots-Tag` on the image.
- Not your images: use the Search help article for removing an image from results.

## Redacted information
https://developers.google.com/search/docs/crawling-indexing/keep-redacted-information-out · Last updated: 2025-12-10

### Why
- Documents and images can carry invisible information (change history, uncropped originals, author/editor metadata) that survives export or conversion. Tiny font, background-colored text or covering text with an image does not redact: search engines still index it, and OCR and screen readers expose it.

### Before publishing
- Edit and export images before embedding: crop out unwanted areas (some tools keep the uncropped original), fully remove or obscure text (OCR makes it searchable), remove unwanted metadata. Export to flattened or non-vector formats such as PNG or WEBP.
- Remove unwanted text before generating the public file; use a format without change history.
- Use real redaction tools (black rectangles over text leave the text in the file); double-check metadata; follow format-specific redaction practice (PDF, image).
- Information in URLs and file names can be indexed even if the content is robots.txt-blocked; use hashes in URL parameters instead of emails or names.
- Consider authentication; serve the login page with a `noindex` robots `meta`.
- Verify the site in Search Console ahead of time for fast removals.

### If already indexed
- Remove the live document.
- Use the Removals tool on the verified site (URL prefix for many); generally under a day.
- Re-host the properly redacted version under a different URL (recrawl lag) and update links.
- Ask other sites hosting copies to remove them (their Removals tool) or use the Outdated Content tool.
- Let removal requests expire (when URLs are updated in the index, or after about 6 months).

## Redirects and Google Search
https://developers.google.com/search/docs/crawling-indexing/301-redirects · Last updated: 2026-04-14

### When to redirect
- New domain; multiple URLs reaching the same page (pick one preferred/canonical, redirect others); merging sites; removed page replaced by another. Platforms (Blogger, Shopify) may have built-in redirect tools.

### Types and how Google treats them (listed in order of how reliably Google interprets them)
- Permanent (Googlebot follows; the indexing pipeline treats it as a signal that the target should be canonical; the target shows in results; use only if sure it won't be reverted):
  - `HTTP 301` and `HTTP 308` (server-side).
  - `meta refresh` with 0 seconds.
  - HTTP `Refresh` header with 0 seconds.
  - JavaScript `location`: only if server-side or `meta refresh` is impossible.
  - Crypto redirect (plain link plus explanation): not a real redirect; may not be recognized by all engines; use only if no other option.
- Temporary (Googlebot follows but the pipeline does not use it as a canonical signal; the source page stays in results; the target may still be indexed given other canonicalization signals):
  - `HTTP 302`, `HTTP 303`, `HTTP 307`.
  - `meta refresh` with more than 0 seconds.
  - HTTP `Refresh` with more than 0 seconds.
- Users can't tell the types apart; choose by how long the redirect will last and which page should show in Search.

### Server-side
- Needs server config (for example `.htaccess`) or server scripts (PHP). Permanent `301`/`308` is the best way to change the URL shown in results. Temporary redirects keep the old URL in results (example: service temporarily unavailable, send users to an explanation page).
- PHP: headers must be sent before any output: `header('HTTP/1.1 301 Moved Permanently'); header('Location: …'); exit();`; temporary: `HTTP/1.1 302 Found`.
- Apache `mod_alias`: `Redirect permanent "/old" "https://example.com/new"`; `Redirect temp "/two-old" "…"`. `mod_rewrite`: `RewriteRule "^/service$" "/about/service" [R=301]` (permanent) or `[R]` (temporary, default 302).
- NGINX: `return 301 …;` permanent, `return 302 …;` temporary inside `location = /service`; `rewrite … permanent;` / `rewrite … redirect;` for complex rules.
- Other servers: ask host or manager.

### `meta refresh` and HTTP equivalent
- Instant (0 s, triggers on load): interpreted as permanent. Delayed (more than 0 s): interpreted as temporary.
- Syntax in `<head>`: `<meta http-equiv="refresh" content="0; url=https://example.com/newlocation">`; header: `Refresh: 0; url=https://www.example.com/newlocation`. Delayed: `content="5; url=…"`.

### JavaScript `location` redirects
- Executed by the Web Rendering Service after crawling; rendering can fail, so Google might never see the redirect. Last resort. Syntax: `window.location.href = "…"` in a head `<script>`.

### Crypto redirects
- Last resort when nothing else is possible: add a visible link to the new page with a short explanation (users find the content; Google may treat as a crypto redirect, existence "may be disputed"). Ask the host for real redirects first.

### Alternate versions of a URL
- Google tracks both source and target; one becomes canonical depending on signals (temporary vs permanent), the other an alternate name.
- Alternate names can appear in results when the query suggests users trust the old URL more. After a domain move, old URLs may occasionally still show though new ones are indexed; this is normal and fades without action.

## Move a site with URL changes
https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes · Last updated: 2026-08-20

### Scope
- Covers HTTP to HTTPS; domain changes (`example.com` to `example.net`, merging domains or hostnames); path changes (`page.php?id=1` to `/widget`, `page.html` to `page.htm`). Hosting-only change with unchanged URLs: use the hosting guide.
- Phases: general best practices, prepare new site, prepare URL mapping, start move (redirects), monitor.

### General best practices
- Split large sites into steps if possible: first move a piece that changes rarely and isn't hit by unpredictable events. A test section isn't fully representative; more pages bring more problems.
- Change one thing at a time (for example domain first, then CMS, then layout).
- Time the move for traffic dips (seasonal or weekday); also frees server resources for Googlebot.
- Expect temporary ranking fluctuation. Medium sites: a few weeks or more before new URLs replace old; larger sites longer. Speed depends on URL count and server speed. A sitemap helps; moving in sections is fine.
- No link-credit loss: `301` and other permanent redirects don't lose PageRank.
- Use Search Console; verify each property separately; use the Index Status report (broad view) and Sitemaps report (indexed counts of submitted URLs).
- Move completes only when Googlebot has visited every old and new URL at least once; there is no fixed crawl frequency; the move happens per URL.

### Checklist: prepare the new site
- [ ] Set up the CMS (preferably same as old) and import content.
- [ ] Transfer images and downloads (PDFs) too; they may have traffic and links.
- [ ] HTTPS move: obtain and configure TLS certificates.
- [ ] Prepare new robots.txt with the correct blocks. If crawling was blocked during development, prepare the post-move version. If `noindex` was used in development, prepare the list of URLs to strip it from.
- [ ] Content not moving (deleted or merged): make those URLs return `404` or `410` on the new site.
- [ ] Verify old and new sites in Search Console, all variants of both (`www`/non-`www`, HTTP/HTTPS).
- [ ] Ensure verification keeps working: tokens may differ per URL; carry over the HTML verification file; make sure the new CMS includes the meta tag or Analytics include used for verification.
- [ ] Copy over Search Console settings: crawl rate set to "Let Googlebot determine" for both old and new site; re-upload the disavow file under the new site's account.
- [ ] Bought domain: check for manual actions (fix and file reconsideration) and leftover URL removals (especially site-wide) from the previous owner.
- [ ] Set up web analytics on both sites (consider a new Google Analytics profile for clean separation).
- [ ] Ensure server capacity: Google temporarily crawls the new site more heavily since old-site crawls get redirected on top of normal crawling; warn the host if the site is very large.

### Checklist: prepare URL mapping
- [ ] List old URLs: start with important ones (sitemaps, server logs or analytics top traffic, Search Console "Links to your site" for pages with links); CMS URL listing; recent server-log URLs for a seasonally sensible period; include images, videos, JS, CSS files.
- [ ] (Simple domain-only moves can use a wildcard server-side redirect without a URL list.)
- [ ] Decide each old URL's target; store in a database or rewrite rules for patterns.
- [ ] On the new site: each URL gets a self-referencing `rel="canonical"` `<link>`; hreflang annotations updated to new URLs (HTML or sitemap); internal links changed to new URLs.
- [ ] Save for the move: a sitemap of new URLs from the mapping, and the list of sites linking to the old URLs (from Search Console).

### Redirect strategy
- Server-side permanent redirects (`301`/`308`, via `.htaccess` on Apache or CMS functions). Client-side redirects only as a last resort.
- Small and medium sites: move all URLs at once (better UX, faster detection by Google). Large sites: may move in sections for easier monitoring.
- Avoid chains: Googlebot follows up to 10 hops, but redirect directly to the final URL; if impossible keep the chain short, ideally at most 3 and fewer than 5. Chains add latency and not all clients handle long ones.

### Checklist: start the move
- [ ] Turn on the redirects (config push or CMS update).
- [ ] Avoid irrelevant redirects: don't send many old URLs to one irrelevant target like the new home page (confusing, may count as `soft 404`). Consolidating several pages into one new page and redirecting them there is fine.
- [ ] Check new-site `rel="canonical"` links point to new URLs; update or remove any `noindex` robots meta added to prevent early indexing.
- [ ] Test redirects: URL Inspection Tool for single URLs; command-line tools or scripts for volume.
- [ ] Domain or subdomain change only: submit Change of Address in Search Console for the old site (`example.com` to `example.net`, `a.example.com` to `b.example.com`). Not needed for HTTP to HTTPS, `www` to non-`www` on one domain, or path moves. For a new domain submit Change of Address for every verified old variant (for example `en.example.com`, `www.example.com`, `example.com`), even unused ones; all must be verified.
- [ ] Keep redirects as long as possible, generally at least 1 year, so Google transfers all signals including reassigning other sites' links. For users consider keeping indefinitely, but redirects are slow, so update own links and high-volume external links.
- [ ] Submit the new sitemap in Search Console; the old sitemap can then be removed (see note).
- [ ] Update links right after launch: internal links (per mapping), external links (ask linking sites, prioritize by inbound visits), social profile links (Facebook, Twitter, LinkedIn), ad campaign landing pages.

> Note: this page says the old sitemap can be removed after submitting the new one, yet the monitoring section says to submit both saved sitemaps and watch old-URL indexed count fall to zero. Both are stated.

### Monitor traffic
- Search Console: Sitemaps (new-URL sitemap starts at 0 indexed, old-URL sitemap many; old drops to zero over time; redirect warnings on the old-URL sitemap are normal and can be ignored); Index Coverage report (old URL counts fall, new rise; check for unexpected crawl errors); Search queries/performance (new URLs gain impressions and clicks).
- Other: server access and error logs (Googlebot crawling, unexpected HTTP errors, user traffic); analytics, especially Google Analytics real-time during the initial phase. Expect old-site traffic down and new-site traffic up.
- Typical duration: a few weeks for most pages of a small to medium site; longer for large ones; visibility may fluctuate temporarily.

> Note: "Index Status report" and "Index Coverage report" are older Search Console names; current naming elsewhere is Page indexing report.

### Troubleshooting common mistakes
- Leftover `noindex` or robots.txt blocks from migration: remove them. A missing robots.txt is fine but must return a real `404`. Test: inspect robots.txt on the HTTPS site; URL Inspection for pages missing from Google.
- Incorrect redirects, often to non-existent URLs on the new site: check for a high "Not found" count in Search Console or crawl with a tool such as Screaming Frog.
- Other crawl errors: look for spikes in the Index Coverage report.
- Insufficient server capacity (heavier Google crawl after migration).
- Sitemaps not updated with new URLs.

## Changing your hosting
https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes · Last updated: 2025-12-10

- Applies to switching hosting provider or moving to a CDN where user-visible URLs do not change. For URL changes use the site-move-with-URL-changes guide.
- Phases: prepare new infrastructure, start move (DNS change), monitor, shut down old.

### Checklist
- [ ] Copy the site to the new host (HTML files or database export/import) and test everything: pages, images, forms, downloads (PDFs). Use a test environment, possibly IP-restricted.
- [ ] Optionally allow public testing on a temporary hostname (for example `beta.example.com`) to check browser and Googlebot reachability. Prevent accidental indexing with `noindex` robots rule in HTML or HTTP headers.
- [ ] Have a Search Console account for the site; verify the temporary hostname property too; check Googlebot access with URL Inspection Tool.
- [ ] Check firewall or DoS protection doesn't block Googlebot from the DNS or hosting servers (verify Googlebot per docs).
- [ ] Lower DNS record TTL to a conservative low value (for example a few hours) at least a week before the move, so new settings propagate faster.
- [ ] Ensure Search Console verification survives: include the HTML verification file; include the meta tag or Analytics include in the new CMS templates.
- [ ] Start: remove temporary crawl blocks (robots.txt disallow-all, `noindex` meta or headers) from the new copy.
- [ ] Update DNS records to the new host; this is the actual move.
- [ ] Monitor: server logs on old and new (old traffic falls, new rises); check propagation with public DNS checking tools across ISPs/regions; watch Index coverage graphs in Search Console.
- [ ] Shut down old hosting once its logs show zero traffic.

### Googlebot crawl rate note
- A temporary drop in crawl rate right after launch is normal, followed by a steady rise over a few days, possibly above prior levels, because crawl-rate signals change with hosting. Without serious problems or slowdowns, Googlebot crawls as fast as necessary and possible.

## A/B testing
https://developers.google.com/search/docs/crawling-indexing/website-testing · Last updated: 2025-12-10

### Overview
- A/B testing compares two or more variations; multivariate testing changes several elements at once to find individual and combined effects.
- Tests can use separate URLs (users redirected from the original to variants) or inject variations on one URL via JS.
- Small changes (button size/color/placement, call-to-action text) often don't affect snippet or ranking, so crawling or indexing of variants may not matter. If Google crawls often enough to see the test, it will probably index the post-test update quickly.

### Best practices
- Don't cloak: never show different URLs or content to Googlebot than to humans; against spam policies (can demote or remove the site), whether by server logic, robots.txt or other means. Use links or redirects instead. Googlebot generally doesn't support cookies, so it sees the version served to cookie-less browsers.
- Multi-URL tests: put `rel="canonical"` on all variant URLs pointing to the original. Preferred over `noindex`, which can have unexpected bad effects (you want the original indexed, with variants grouped as duplicates).
- Use `302` (temporary), not `301`, for redirecting users to variants, so the original URL stays indexed. JS-based redirects are also fine.
- Run only as long as needed (depends on conversion rate and traffic; the tool tells when data suffices). After the test apply the winner and remove all test elements (alternate URLs, scripts, markup) promptly. A needlessly long experiment, especially with a variant served to a large share of users, may be treated as deception and acted upon.
- Further help: Google Analytics content experiments articles and forums.

## Temporarily pause or disable a website
https://developers.google.com/search/docs/crawling-indexing/pause-online-business · Last updated: 2025-12-10

### Recommended: limit functionality
- Keep the site online (people can still find products, read reviews, use wishlists).
- Disable the cart (simplest; no change to Search visibility).
- Show a banner or popup on all pages including the landing page with delays, shipping times, pick-up/delivery options. Mark it `data-nosnippet` so it doesn't appear in snippets; follow Google's popup and banner guidelines.
- Update structured data (`Product`, `Book`, `Event`, etc.): availability, events changed to cancelled, `LocalBusiness` opening hours.
- Check the Merchant Center feed and follow `availability` attribute best practices.
- Tell Google: Search Console recrawl request for a few pages (home page); sitemaps for many pages (all product pages).

### Not recommended: disabling the whole site
- Complete removal from the index is significant; recovery time is unfixed and cannot be sped up. Only for a very short period (a few days at most), even when done properly.
- Side effects: customers can't find the business or first-hand information (reviews, specs, repair guides, manuals; third-party info may be wrong); Knowledge Panels may lose phone numbers and logo; Search Console verification fails and reports lose data as pages drop; ramp-up needs reindexing with uncertain duration and outcome.
- Options if you must:
  - Urgent 1 to 2 day shutdown: informational error page with HTTP `503` instead of all content.
  - Longer: an indexable placeholder home page with `200`.
  - Quick hide while deciding: temporarily remove the site from Search (Removals tool).

### Best practices when disabling
- Titles, descriptions, metadata and structured data can't be refreshed while pages return `503`.
- Keep robots.txt crawlable; never return `503` for robots.txt (blocks all crawling).
- Verify `503` locally with `curl -I -X GET "https://www.example.com/"`.
- Minimize load of the `503` page: `Retry-After` header with best-effort date or duration; static HTML; inline CSS and base64 images.
- Give users guidance: links, expected return date or update date, customer-service contact.
- Don't disallow all crawling in robots.txt (can remove content and possibly URLs from Search).
- Don't return `403`, `404`, `410`, `noindex` robots meta or `X-Robots-Tag`: removes URLs from Search.
- Don't use the temporary-removal tool for closures (users can't learn the status; resellers/affiliates may still appear).

### FAQ
- Closing for just a few weeks still harms indexing; limit functionality instead.
- Excluding only non-essential products is fine; limit purchasing on them.
- Crawl rate can be reduced but is not recommended generally (slower reflection of unavailability); valid if Googlebot causes critical server load; set a reminder to reset it.
- Quick (re)indexing: Search Console for a limited number of pages; sitemaps for many.
- Region blocking: Google generally crawls from the US; blocking the US makes the site inaccessible to Search. Limit functionality for that region instead.
- Don't use the Removals tool for out-of-stock products; keep the page and mark it out of stock.
