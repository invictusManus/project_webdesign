# Crawling & Google crawlers: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

> Note: Most crawling pages moved from `/search/docs/crawling-indexing/` to the shared `/crawling/docs/` site (Nov and Dec 2025) because the infrastructure serves many Google products, not only Search. Pages that still exist on both sites are marked below.

## About Google's web crawling
https://developers.google.com/crawling/docs/about-crawling · Last updated: 2026-03-03

### What crawling is
- Crawling = automated software discovering new pages and understanding them, so pages can appear in results. All search engines rely on it.
- Googlebot is the best-known crawler (keeps Search fresh); other crawlers serve other surfaces (Images, Shopping). Crawlers use identifiable user-agent names and known IP addresses so site owners can confirm legitimacy.

### Recrawling and freshness
- Recrawl frequency varies: news homepages may be recrawled every few minutes; pages unchanged for years may wait about a month.
- Site owners influence recrawl through sitemap files that announce new and updated pages.
- Frequent crawling is a good sign (fresh or in-demand content; ecommerce is crawled often for price, promotion and stock).
- Rendering loads a page fully like a person would. Pages got heavier (median mobile page 816 KB to 2.3 MB, 60+ files), so a page may need several crawls for a representative snapshot.

### Automatic optimization and limits
- Crawl rate adapts automatically: slower site or errors lead to a lower crawl rate. Crawled content is cached to avoid wasteful requests. Crawlers recognize low-value sections (example: calendars running to year 9999).
- Site owners help by marking content that need not be crawled (lowers their infrastructure cost).
- Crawlers never enter paywall or login content without permission. For subscription content: give crawlers explicit access, use structured data so human visitors still see a login screen without triggering spam rules, and use preview controls to keep subscription text out of previews.

### Site-owner controls
- Google honors robots.txt and robots meta tags; sitemaps announce content; crawl budget governs frequency.
- Crawled data may be reused, and robots.txt choices are still respected on reuse.
- `Google-Extended` in robots.txt controls (among other things) whether content helps train future Gemini models. It does not affect inclusion in Search and is not a ranking signal.
- Search Console (free) shows how much was crawled and why, and helps diagnose downtime or speed problems.

## List of Google crawlers
https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers · Last updated: 2026-06-12

### Three categories of clients
| Category | What | robots.txt |
|---|---|---|
| Common crawlers | Used for Google's products (for example Googlebot) | Always respected for automatic crawls |
| Special-case crawlers | Specific products with an agreement between crawled site and product (example: `AdsBot` ignores the global `*` group with the ad publisher's permission) | May ignore it |
| User-triggered fetchers | End user triggers a fetch (example: Site Verifier) | Generally ignored (fetch is user-requested) |

### Technical properties
- Crawlers run on thousands of machines across many datacenters, so logs show many IPs. Egress is primarily from US IPs; if Google detects a site blocking US requests it may crawl from IPs in other countries.
- Protocols: HTTP/1.1 (default) and HTTP/2. Crawlers choose what gives best performance and may switch between sessions. HTTP/2 can save CPU/RAM for site and Googlebot but gives no product benefit (no ranking boost). Opt out of HTTP/2 crawling by answering `421` to HTTP/2 requests from Google (if not feasible, message the Crawling team; temporary solution). FTP (RFC959) and FTPS (RFC4217) are supported but rare.
- Content encodings: gzip, deflate, Brotli (`br`); advertised per request in `Accept-Encoding` (example `gzip, deflate, br`).
- File size limit: by default only the first 15 MB of a file is crawled; the rest is ignored. Individual products may set other limits per crawler and file type (Googlebot may use a smaller limit such as 2 MB, or a larger one for PDF than HTML).
- Crawl rate: goal is to crawl as many pages per visit as possible without overloading the server; the rate can be reduced on request. Wrong HTTP response codes can affect how the site appears in Google products.

### HTTP caching
- Supported: heuristic caching via `ETag` response header with `If-None-Match` request header, and `Last-Modified` response header with `If-Modified-Since` request header. Other HTTP caching directives are not supported.
- If both `ETag` and `Last-Modified` are present, `ETag` is used (per HTTP standard). Google recommends `ETag` for its crawlers because it has no date-format issues. Still set both (CMSes and other tools use them).
- `Last-Modified` must be a valid HTTP date; recommended format `Weekday, DD Mon YYYY HH:MM:SS Timezone` (example `Fri, 4 Sep 1998 19:15:56 GMT`).
- Optional: `Cache-Control: max-age=<seconds the content stays unchanged>` (example `max-age=94043`) helps crawlers decide when to recrawl.
- Use of caching differs per crawler: `Googlebot` supports caching when recrawling for Search; `Storebot-Google` only under certain conditions. Implementation goes through hosting or CMS provider.

### Verification
- Crawlers identify via: HTTP `user-agent` header, source IP, reverse DNS hostname of the IP. See "Verify requests from Google".

## Googlebot
https://developers.google.com/search/docs/crawling-indexing/googlebot · Last updated: 2026-02-03

### What it is
- Generic name for two Search crawlers: Googlebot Smartphone (simulates mobile user) and Googlebot Desktop (simulates desktop user). Tell them apart via the `user-agent` request header.
- Both obey the same robots.txt token (`Googlebot`), so you can't target one subtype in robots.txt.
- For most sites Search primarily indexes the mobile version, so most crawl requests come from the mobile crawler and a minority from desktop.

### How Googlebot accesses your site
- Most sites: no more than about one request every few seconds on average (short bursts can look higher). Crawl rate can be reduced if the site struggles.
- File size limits when crawling for Search: first 2 MB of a supported file type, first 64 MB of a PDF. Each resource referenced in HTML (CSS, JS) is fetched separately with the same limit (except PDF). At the cutoff Googlebot stops the fetch and sends only the downloaded part to indexing. The limit applies to uncompressed data. Googlebot Video, Googlebot Image and others may have different limits.
- When crawling from US IPs, Googlebot's timezone is Pacific Time.
- Other technical properties: see overview of Google's crawlers.

> Note: Default limit for all Google crawlers is 15 MB (overview page); Googlebot for Search uses the smaller 2 MB (64 MB PDF). The 2026-02-03 changelog entry moved the generic file-size text from this page to the crawling site.

### Blocking Googlebot
- Googlebot finds URLs mainly via links on crawled pages; keeping a site secret by not publishing links is almost impossible (referrer logs can leak the URL).
- Crawling is not indexing; blocking crawling does not stop a URL appearing in results.
- Stop crawling: robots.txt. Keep out of the index: `noindex`. Make inaccessible to crawlers and users: password protection or similar.
- Blocking Googlebot affects Search (including Discover and all Search features) plus Google Images, Google Video, Google News.

### Verifying Googlebot
- The `user-agent` header is often spoofed. Verify via reverse DNS lookup of the source IP or by matching the IP against published Googlebot ranges.

## Common crawlers
https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers · Last updated: 2026-10-30

### General properties
- Used for building search indexes, other product-specific crawls and analysis. They always obey robots.txt for automatic crawling.
- IPs from `common-crawlers.json`; reverse DNS matches `crawl-***-***-***-***.googlebot.com` or `geo-crawl-***-***-***-***.geo.googlebot.com`.
- A crawler may have several tokens; matching one token is enough for a rule to apply. List is not exhaustive. UA strings can be spoofed.
- `Chrome/W.X.Y.Z` in UA strings is a placeholder for the Chrome version (example `41.0.2272.96`) that rises over time; use wildcards for the version when filtering logs.

### Crawler table
| Crawler | UA in HTTP requests | robots.txt token(s) | Affected by robots.txt rules / products | Respects robots.txt |
|---|---|---|---|---|
| Googlebot Smartphone | `Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)` | `Googlebot` | Google Search (incl. Discover and all Search features), Google Images, Video mode, Google News, Discover | Yes |
| Googlebot Desktop | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36` (rarely `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)` or `Googlebot/2.1 (+http://www.google.com/bot.html)`) | `Googlebot` | same as above | Yes |
| Googlebot Image | `Googlebot-Image/1.0` | `Googlebot-Image`, `Googlebot` | Google Images, Discover, Video mode, all Search features that show images, logos, favicons | Yes |
| Googlebot Video | `Googlebot-Video/1.0` | `Googlebot-Video`, `Googlebot` | Video-related Search features and other video-dependent products | Yes |
| Googlebot News | no separate UA string; crawls with various Googlebot UAs | `Googlebot-News`, `Googlebot` | Google News product (news.google.com and the Google News app) | Yes |
| Google StoreBot (`Storebot-Google`) | Desktop `Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Safari/537.36`; mobile `Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36` | `Storebot-Google` | All Google Shopping surfaces (Shopping tab in Search, Google Shopping) | Yes |
| Google-InspectionTool | Desktop `Mozilla/5.0 (compatible; Google-InspectionTool/1.0)`; mobile = Android Chrome UA ending `(compatible; Google-InspectionTool/1.0)` | `Google-InspectionTool`, `Googlebot` | Search testing tools (Rich Results Test, URL Inspection in Search Console); no effect on Search or other products | Yes |
| GoogleOther | `... (compatible; GoogleOther)` (mobile Android Chrome form and desktop `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GoogleOther) Chrome/W.X.Y.Z Safari/537.36`) | `GoogleOther` | No specific product; generic crawler for product teams fetching public content (example: one-off internal R&D crawls) | Yes |
| GoogleOther-Image | `GoogleOther-Image/1.0` | `GoogleOther-Image`, `GoogleOther` | No specific product; GoogleOther optimized for public image URLs | Yes |
| GoogleOther-Video | `GoogleOther-Video/1.0` | `GoogleOther-Video`, `GoogleOther` | No specific product; GoogleOther optimized for public video URLs | Yes |
| Google-CloudVertexBot | UA substring `Google-CloudVertexBot` | `Google-CloudVertexBot`, `Googlebot` | Crawls requested by site owners to build Vertex AI Agents; no effect on Search or other products | Yes |
| Google-Extended | no separate UA string; uses existing Google UAs; token is control-only | `Google-Extended` | Standalone product token: whether crawled content may train future Gemini models (Gemini Apps, Vertex AI API for Gemini) and be used for grounding in Gemini Apps and Grounding with Google Search on Vertex AI. Does not affect Search inclusion or ranking | Yes (control token) |

### Key points
- Example groups per crawler in the page all use the pattern `user-agent: <token>` + `allow` + `disallow`. Image/Video/CloudVertex/InspectionTool list `Googlebot` as an additional token, so a `Googlebot` group also governs them when no more specific group exists.
- Google intends to support the AIPREF shared machine-readable training preference (`user-agent: __usage_ai-training`) in early 2027 (note added 2026-10-30).

## Special case crawlers
https://developers.google.com/crawling/docs/crawlers-fetchers/google-special-case-crawlers · Last updated: 2026-09-17

### General properties
- Used where the crawled site and the product have an agreement about crawling. They may ignore robots.txt rules, so they use different IPs than common crawlers (`special-crawlers.json`). Reverse DNS matches `rate-limited-proxy-***-***-***-***.google.com`.
- General crawler properties apply. List not exhaustive. UA can be spoofed.

### Active crawlers
| Crawler | UA in HTTP requests | robots.txt token | Affected products | Respects robots.txt |
|---|---|---|---|---|
| APIs-Google | `APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)` | `APIs-Google` | Delivery of push notification messages by Google APIs | Own token honored; global `*` ignored |
| AdsBot Mobile Web | Android Chrome UA ending `(compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)` | `AdsBot-Google-Mobile` | Google Ads checking ad quality of web pages | Own token; `*` ignored |
| AdsBot | `AdsBot-Google (+http://www.google.com/adsbot.html)` | `AdsBot-Google` | Google Ads checking ad quality of web pages | Own token; `*` ignored |
| Google-Safety | `Google-Safety` | none | Abuse-specific crawling, such as malware discovery for publicly posted links on Google properties | Ignores robots.txt entirely (unaffected by crawling preferences) |
| Mediapartners-Google | Desktop `Mediapartners-Google`; mobile `(Various mobile device types) (compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html)` | `Mediapartners-Google` | Visits participating sites to provide relevant ads; affects various ad products (for example AdSense, Ad Manager). Generalized 2026-09-17 | Own token; `*` ignored |

### Retired special-case crawlers (historical only)
| Crawler | UA / token | Notes |
|---|---|---|
| AdsBot Mobile Web (iPhone) | iPhone Safari UA with `(compatible; AdsBot-Google-Mobile; ...)`; token `AdsBot-Google-Mobile` | Checked iPhone page ad quality; `*` ignored |
| Duplex on the web | `DuplexWeb-Google/1.0` in Android UA; token `DuplexWeb-Google` | Supported Duplex on the web; may ignore `*` |
| Google Favicon | UA ends `Google Favicon`; tokens `Googlebot-Image`, `Googlebot` | Favicon fetches |
| Mobile Apps Android | `AdsBot-Google-Mobile-Apps`; token `AdsBot-Google-Mobile-Apps` | Obeyed `AdsBot-Google` rules but ignored `*`; Android app page ad quality |
| Web Light | `googleweblight` in UA; token `googleweblight` | Explicit human browse requests only, so ignored robots.txt; checked `no-transform` header when a user clicked a Search result |

### Key points
- All AdsBot crawlers must be named explicitly; `User-agent: *` does not match them (also stated in the robots.txt create/useful-rules pages).
- AdsBot demand rises with Dynamic Search Ad targets (see crawl budget, reduce crawl rate).

## User-triggered fetchers
https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers · Last updated: 2026-08-19

### General properties
- Started by a user inside a Google product (example: Site Verifier; a site on Google Cloud that lets its users fetch an external RSS feed). Because a user requested the fetch, they generally ignore robots.txt.
- IP ranges: `user-triggered-fetchers.json`, `user-triggered-fetchers-google.json`, `user-triggered-agents.json`. Reverse DNS: `***-***-***-***.gae.googleusercontent.com` (user-owned/GCP) or `google-proxy-***-***-***-***.google.com` (Google-owned).
- List not exhaustive. UA can be spoofed.

### Fetchers
| Fetcher | UA in HTTP requests | Purpose | Respects robots.txt |
|---|---|---|---|
| Chrome Web Store (`Google-CWS`) | `Mozilla/5.0 (compatible; Google-CWS)` | Requests URLs developers put in Chrome extension and theme metadata | Generally no |
| Feedfetcher | `FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)` | Crawls RSS/Atom feeds for Google News and WebSub | No |
| Gemini Notebook | Mobile and desktop UAs with `(compatible; Google-GeminiNotebook; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-gemininotebook)`; former agent `Google-NotebookLM` "supported until August 2026" | Fetches individual URLs users give as sources for their Gemini Notebook projects | Generally no |
| Google-Agent | Mobile and desktop UAs containing `(compatible; Google-Agent; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-agent)`; IPs from `user-triggered-agents.json` | Agents hosted on Google infrastructure that navigate the web and act on user request | Generally no |
| Google Messages | `GoogleMessages` | Link previews for URLs sent in chat messages | Generally no |
| Google Pinpoint | `Google-Pinpoint` | Fetches individual URLs users specified as sources for their personal document collections | Generally no |
| Google Publisher Center | `GoogleProducer; (+https://developers.google.com/search/docs/crawling-indexing/google-producer)` | Fetches and processes feeds publishers explicitly supplied for Google News landing pages | Generally no |
| Google Read Aloud | Mobile and desktop UAs with `(compatible; Google-Read-Aloud; +https://support.google.com/webmasters/answer/1061943)`; former agent `google-speakr` (deprecated) | Fetches and reads pages aloud via text-to-speech on user request | No (opt out via meta tag) |
| Google Site Verifier | `Mozilla/5.0 (compatible; Google-Site-Verification/1.0)` | Fetches Search Console verification tokens | Generally no |

### Notes
- Google-Agent: Google is experimenting with Web Bot Auth using identity `https://agent.bot.goog` (see Web Bot Auth page).

> Note: The page says the former agent `Google-NotebookLM` was supported "until August 2026"; the changelog (2026-07-16) says the old value continues to be supported for a smooth transition. As of 2026-10-31 that window has passed; use `Google-GeminiNotebook` in any filters.

## APIs-Google
https://developers.google.com/crawling/docs/crawlers-fetchers/apis-user-agent · Last updated: 2025-11-21

- User agent used by Google APIs to deliver push notifications (so developers need not poll). Google requires developers to prove domain ownership before registering a URL on that domain to receive messages.
- Access pattern: each notification is an HTTPS `POST`. On possibly temporary errors it resends, then retries on an exponential backoff schedule for up to several days. Rate depends on number of push registrations, how fast resources change and retries, so traffic can be steady, sporadic or spiky.
- Requirements: valid SSL certificate (self-signed, untrusted-issuer or revoked certificates are invalid). Respond within seconds to avoid needless retries.
- Prevent calls: unregister for notifications (if subdomains or URL spaces are run by others, ask them to disable their app), or use robots.txt with token `APIs-Google` (it does not follow `Googlebot` rules). There may be a short delay before it sees the change; if messages continue several days after blocking, check robots.txt location.
- Verify: reverse DNS of IPs using the UA shows `googlebot.com` or `google.com`.

## Feedfetcher
https://developers.google.com/crawling/docs/crawlers-fetchers/feedfetcher · Last updated: 2026-02-11

- Fetches RSS/Atom feeds for Google News and WebSub; stores and periodically refreshes feeds requested by app/service users. Only podcast feeds get indexed in Search (a feed not following Atom/RSS spec may still be indexed).
- robots.txt is ignored (requests come from explicit human action). To stop it, serve `404`, `410` or another error status to the `Feedfetcher-Google` user agent. For hosted feeds (blog/site hosts), work with the host.
- Frequency: on average no more than once per hour per site (frequently updated sites more; delays can make it look more frequent). Common RSS/Atom feeds are fetched once for all users who subscribed.
- Requests come from many machines near the target site; IPs are in `user-triggered-fetchers-google.json`.
- Downloads one copy of each file per retrieval (restarts may cause re-fetches). Crawls only the single URL a user supplied; does not discover links. Wrong/non-existent or "secret" URLs hit by it come from a user typing or knowing them.
- Support: Search Central forum.

## Google Read Aloud
https://developers.google.com/crawling/docs/crawlers-fetchers/read-aloud-user-agent · Last updated: 2025-12-02

- User agent `Google-Read-Aloud` for the text-to-speech service; triggered when an end user has TTS on and visits a page. Used by Google Go, Google Read it, Read Aloud in the Google app and other Google TTS services.
- Behavior: user-triggered, caches page results (multiple requests still possible), not a crawler (does not follow links). Uses stateless rendering (like a user, but no user cookies). A listen request may or may not cause a visit depending on whether the page was fetched recently.
- Opt out: robots.txt does not work. Use `<meta name="google" content="nopagereadaloud">`. It may proactively fetch and render the page (with embedded resources) to see the meta tag; once recognized, future requests drop automatically.
- Paywalled content: use paywalled-content structured data with `isAccessibleForFree` set to `False`.
- `google-speakr` is the old deprecated name.

## Verify requests from Google
https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests · Last updated: 2026-03-20

### Crawler categories and identifiers
| Type | Reverse DNS mask | IP ranges file |
|---|---|---|
| Common crawlers | `crawl-***-***-***-***.googlebot.com` or `geo-crawl-***-***-***-***.geo.googlebot.com` | `common-crawlers.json` |
| Special-case crawlers (may or may not respect robots.txt) | `rate-limited-proxy-***-***-***-***.google.com` | `special-crawlers.json` |
| User-triggered fetchers (ignore robots.txt) | `***-***-***-***.gae.googleusercontent.com` or `google-proxy-***-***-***-***.google.com` | `user-triggered-fetchers.json`, `user-triggered-fetchers-google.json`, `user-triggered-agents.json` |

- Google-controlled fetchers use IPs in `user-triggered-fetchers-google.json` and resolve to `google.com`; IPs in `user-triggered-fetchers.json` resolve to `gae.googleusercontent.com` (for example a GCP-hosted site fetching external RSS feeds for its users).

### Methods
- Manual (enough for most cases): (1) reverse DNS the IP with `host`; (2) check the domain is `googlebot.com`, `google.com` or `googleusercontent.com`; (3) forward DNS that hostname; (4) confirm it returns the original IP. Examples in the page cover `66.249.66.1` (googlebot.com), `35.247.243.240` (geo.googlebot.com), `66.249.90.77` (rate-limited-proxy google.com).
- Automatic (large scale): match IPs against the published JSON lists (CIDR notation): common crawlers, special crawlers, user-triggered fetchers (users), user-triggered fetchers (Google), user-triggered agents. For other Google IPs (for example Apps Script) match against Google's general IP list.

## Verifying Googlebot and other Google crawlers
https://developers.google.com/crawling/docs/crawlers-fetchers/verifying-googlebot · Last updated: 2026-03-20

> Note: Body is identical to "Verify requests from Google" above (same headline, table, steps, examples); only title/URL differ. Treat as one document; the 2026-03-20 changelog entry added user-triggered agents IP ranges to it.

## Authenticate requests with Web Bot Auth (experimental)
https://developers.google.com/crawling/docs/crawlers-fetchers/web-bot-auth · Last updated: 2026-10-13

### What and status `(experimental)`
- Web Bot Auth: IETF internet-draft cryptographic protocol where bots sign requests, so identity does not rest on spoofable headers and IPs. Benefits: cryptographic certainty (identity decoupled from IP), better observability, future-proofing.
- Experimental because it is a draft (IETF WBA Working Group, may change) and UA/IP verification remains the de facto standard. Currently tested with some AI agents on Google infrastructure; not all Google user agents use it, and not every request of a participating agent is signed.
- Keep relying on IP addresses, reverse DNS and UA strings in addition.

### Allowlisting Google AI agents
- Option 1: use a bot-detection service, CDN or WAF that supports Web Bot Auth. Some let you look up and allowlist the `Google-Agent` UA. A subset of `Google-Agent` requests are signed and authenticated as `https://agent.bot.goog`.
- Option 2: verify yourself (HTTP Message Signatures for automated traffic; RFC 9421):
  - Fetch the key set from `https://agent.bot.goog/.well-known/http-message-signatures-directory`; cache per its `Cache-Control`; delete cached keys missing from the file (expired/revoked).
  - Participating requests carry `Signature-Agent` header `g="https://agent.bot.goog"` (note the `g=` label).
  - Verify the `Signature` header against `Signature-Input` using the headers labelled `g`.
  - Fall back to IP verification for unsigned requests.
  - For latency-sensitive requests you may respond first and validate within the signature's expiry window (sanction applies to later requests). A signature's expiry window is not the key set's `Cache-Control` lifetime; validate each separately.
- Next steps: ask your host/security provider about support; follow the Working Group and IETF list; send feedback via Google's form.

## Reduce the Google crawl rate
https://developers.google.com/crawling/docs/crawlers-fetchers/reduce-crawl-rate · Last updated: 2026-10-06

### Find the cause first
- Common causes of sharp crawl increases: inefficient URL configuration (faceted navigation, sorting/filtering, calendars with many date URLs) and Dynamic Search Ad targets. Check hosting company and recent access logs, then apply the faceted-navigation and crawl-efficiency guides.

### Emergency reduction
- Side effects warning: Search discovers fewer new pages, refreshes existing pages less often (prices and availability lag), removed pages may stay indexed longer; Google Ads campaigns may be cancelled or paused and ads may not serve.
- To reduce urgently for a short time (a couple of hours, 1-2 days): return `500`, `503` or `429` instead of `200`.
- When a significant number of URLs return those codes, Google cuts the crawl rate for the whole hostname (error URLs and content URLs alike) and raises it again automatically as errors drop.
- On `503` or `429` you may add `Retry-After` (RFC 9110): delay in seconds (example `Retry-After: 120`) or absolute UTC HTTP-date (example `Retry-After: Wed, 21 Oct 2026 07:28:00 GMT`).
- Do not do this longer than 1-2 days: if Googlebot sees these codes on the same URL for multiple days the URL may be dropped from the index.

### Exceptional requests
- If serving errors is not feasible, file a special request reporting unusually high crawl rate and state the optimal rate. You cannot request a higher crawl rate; evaluation can take several days.

## Optimize your crawl budget
https://developers.google.com/crawling/docs/crawl-budget · Last updated: 2026-07-22

### Who it is for
- Advanced guide for: sites with 1M+ unique pages with weekly changes; 10,000+ unique pages with daily changes; sites with a large share of URLs in Search Console "Discovered - currently not indexed". Numbers are rough estimates, not thresholds.
- Other sites: keep sitemap current and check the Page Indexing report; pages crawled the same day they publish need no tuning.

### Theory
- Crawl budget = set of URLs Google can and wants to crawl; set by crawl capacity limit and crawl demand. A "site" is a unique hostname (`www.example.com` and `code.example.com` have separate budgets). Crawled does not mean indexed (pages are evaluated and consolidated afterwards).
- Crawl capacity limit (hostload): caps total time the server spends holding connections open for Google (parallel connections and duration). All sites start with the same conservative default and Google adjusts it if demand exists and the site is healthy.
  - Goes up when responses are consistent and latency/TTFB stable or improving; goes down on slowdowns, `5xx` or rate-limit signals such as `429`. Google's own finite resources also cap it.
- Crawl demand: per crawler (AdsBot demand rises with dynamic ad targets; Google Shopping with merchant-feed products). For Googlebot it depends on site size, update frequency, page quality and relevance vs. other sites. Levers: perceived inventory (best lever: duplicate or unwanted URLs waste time), popularity (popular URLs crawled more), staleness. Site moves can temporarily raise demand.
- Capacity limit is shared across all crawlers: high demand from one lowers capacity for others. Low demand means less crawling even when capacity is free.

### Best practices
- Manage URL inventory: tell Google what to crawl and not crawl.
- Consolidate duplicate content (focus crawling on unique content, not unique URLs).
- Block crawling with robots.txt for pages users need but Google need not process (infinite scroll duplicates, differently sorted versions) when they can't be consolidated. This makes processing by other systems (indexing) much less likely.
  - Don't use `noindex` for this: Google still requests the page, then drops it, wasting crawl time.
  - Don't use robots.txt to temporarily shift crawl budget; Google won't reallocate freed budget unless already at its capacity limit.
- Return `404`/`410` for permanently removed pages (strong signal not to recrawl; Google does not forget a known URL). Blocked URLs stay in the crawl queue much longer and are recrawled when the block is lifted.
- Eliminate `soft 404` errors (they keep being crawled); check the Page Indexing report.
- Keep sitemaps current; include `<lastmod>` for updated content.
- Avoid long redirect chains.
- Make pages efficient to load/render: faster responses and resources; support HTTP caching with `304 (Not Modified)`.
- Debug: check availability issues during crawling and look for efficiency gains.

### Getting more budget
- Add server resources if blocked by your server capacity (symptom: "Hostload exceeded" in URL Inspection).
- Improve content quality for the targeted product (for Search: popularity, overall user value, uniqueness, serving capacity).

## Improve crawling of faceted navigation URLs
https://developers.google.com/crawling/docs/faceted-navigation · Last updated: 2025-12-18

### Problem
- Parameter-based facets (example `?products=fish&color=radioactive_green&size=tiny`) create near-infinite URL spaces: overcrawling (crawlers can't know URLs are useless before fetching them) and slower discovery of new useful URLs. Crawling facets also costs rendering/computation.
- Choose: prevent crawling if facets need not be indexed, or follow best practices if they must be.

### Prevent crawling
- robots.txt: disallow facet parameters; allow only individual item pages and one dedicated unfiltered listing. Pattern: `disallow: /*?*products=`, `disallow: /*?*color=`, `disallow: /*?*size=`, with `allow: /*?products=all$` for the unfiltered listing.
- URL fragments for filters (`#products=fish&color=...`): Search generally ignores fragments for crawling and indexing, so there is no crawl effect either way.
- Weaker, long-term options:
  - `rel="canonical"` to the unfiltered/base URL may reduce crawl volume of non-canonical versions over time.
  - `rel="nofollow"` on links to filtered pages helps only if every anchor to that URL carries it.

### If facet URLs must be crawlable and indexable
- Use `&` as the parameter separator; `,`, `;`, `[`, `]` are hard for crawlers to recognize as separators.
- For facets in the path (`/products/fish/green/tiny`), keep filter order constant and prevent duplicate filters.
- Return `404` when a filter combination has no results, has duplicate filters, is otherwise nonsensical, or is a non-existent pagination URL. Serve the `404` at the URL requested; do not redirect to a generic not-found page. For single-page apps, follow SPA best practices.
- Expect higher server load and possibly slower discovery of new URLs.

## Myths about crawling
https://developers.google.com/crawling/docs/myths-about-crawling · Last updated: 2025-12-18

- Compressing sitemaps raises crawl budget: false (zipped sitemaps must still be fetched).
- Tweak pages to look fresh: false for Search (quality counts regardless of age; no value in trivial changes or date bumps).
- Old content outweighs fresh: false (useful is useful).
- Google dislikes query parameters: false (it can crawl parameters).
- Faster load and render means more crawling: true, because resources are limited by time and number of bots; rendering time counts as much as request time. Google may spend more time on important slow sites. Prioritize user speed over crawl coverage.
- Small sites are crawled less often: false (important, frequently changing content is crawled often regardless of size).
- Closer to home page means more important: partly true (pages linked from the home page may be crawled more; not ranked higher for that).
- URL versioning encourages recrawl: partly true (probably works but often unnecessary and wastes crawl resources if content didn't change; change the URL only for meaningful changes).
- Site speed and errors affect crawl budget: true. Speed lets Google fetch more over the same connections; many `5xx` or timeouts slow crawling. Watch the Crawl Stats report in Search Console and keep server errors low.
- Crawling is a ranking factor: false (necessary for appearing, not a ranking signal; better crawl rate does not raise rankings).
- Alternate URLs and embedded content count against budget: true (any crawled URL counts, including AMP/hreflang alternates, CSS, JavaScript, XHR fetches).
- `crawl-delay` controls Google's crawlers: false (non-standard rule is not processed).
- `nofollow` affects crawl budget: partly true (a nofollow link can still be crawled via other links elsewhere on the site or web).
- `noindex` controls crawl budget: partly true (Google must crawl the page to see `noindex`; use it to keep pages out of the index and don't worry about budget; removing URLs from the index can indirectly free budget over time).
- `4xx` pages waste crawl budget: false for `4xx` except `429` (Google got a status and no content).

## Introduction to robots.txt
https://developers.google.com/search/docs/crawling-indexing/robots/intro · Last updated: 2025-12-10

### Purpose
- robots.txt tells crawlers which URLs they may access, mainly to avoid overloading the site. It is not a way to keep a page out of Google; use `noindex` or password protection.
- On hosted platforms (Wix, Blogger) you may not be able to edit robots.txt; use the platform's search-visibility settings.

### Effect by file type
- Web pages (HTML, PDF, other readable non-media): use to manage crawl traffic or skip unimportant/similar pages. Don't use it to hide pages from results: a blocked URL can still be indexed from links with descriptive text but shows no description. Embedded images, video, PDFs and other non-HTML files on a blocked page are excluded from crawling unless referenced by allowed pages. To fix a descriptionless result, remove the block; to hide completely use another method.
- Media files (image/video/audio): robots.txt manages crawl traffic and keeps media out of Google results, but other pages and users can still link to the files.
- Resource files (scripts, styles, images): can be blocked if the page isn't significantly affected without them. Don't block them if they help Google understand the page, or analysis suffers.

### Limitations
- Not all search engines support every rule; rules cannot force crawlers (Googlebot and respectable crawlers obey; others may not). Use password protection for secrets.
- Crawlers interpret syntax differently; learn the syntax per crawler.
- A disallowed URL can still be indexed if linked elsewhere; URL and anchor text may show. To prevent it: password protection, `noindex` meta tag or response header, or remove the page.
- Caution: combined crawling and indexing rules can counteract each other.

## Create and submit a robots.txt file
https://developers.google.com/crawling/docs/robots-txt/create-robots-txt · Last updated: 2025-11-21

### Basics
- Steps: create `robots.txt`, add rules, upload to site root, test. All files are implicitly allowed unless a rule says otherwise.
- Minimal example: `User-agent: Googlebot` + `Disallow: /nogooglebot/`; `User-agent: *` + `Allow: /`; `Sitemap: https://www.example.com/sitemap.xml`.

### Format and location
- Plain text, UTF-8 (ASCII included), created in a plain-text editor (not a word processor; curly quotes and proprietary formats cause problems). Characters outside UTF-8 may be ignored, invalidating rules.
- Named exactly `robots.txt`; one per site; at the root of the host it applies to (not in a subdirectory). If you can't reach the root, use another method such as meta tags.
- Valid on subdomains and non-standard ports (example `https://example.com:8181/robots.txt`). Applies only to its own protocol, host and port: `https://example.com/robots.txt` does not cover `https://m.example.com/` or `http://example.com/`.

### Rules
- File = one or more groups; each group starts with `User-agent` and lists rules, one per line. Groups are processed top to bottom; a user agent matches one group (first, most specific); multiple groups for the same agent are merged.
- Default: anything not disallowed is crawlable. Paths are case-sensitive (`disallow: /file.asp` does not block `/FILE.asp`). `#` starts a comment.
- Supported fields:
  - `user-agent` (required, one or more per group): `*` matches all crawlers except AdsBot crawlers, which must be named explicitly. Examples: block only Googlebot; block Googlebot and `AdsBot-Google` with two `User-agent` lines in one group; block all except AdsBot with `*`.
  - `disallow` / `allow` (at least one per group): path relative to root; must start with `/`; a directory must end with `/`; a page uses its full name as shown in the browser. `allow` overrides `disallow` for a subpath.
  - `sitemap` (optional, 0 or more): fully qualified URL; Google does not assume or check http/https/www/non-www alternates.
- All rules except `sitemap` support the `*` wildcard for prefix, suffix or whole string. Unrecognized lines are ignored.

### Test and submit
- Check public accessibility in a private browser window at the robots.txt URL.
- Validate markup with the Search Console robots.txt report (only for files already live) or Google's open-source robots.txt library (local testing, same code as Search).
- After upload, Google finds and uses the file automatically. To refresh the cache sooner see the update page.

## Update your robots.txt file
https://developers.google.com/crawling/docs/robots-txt/submit-updated-robots-txt · Last updated: 2025-11-21

- Download the current file: open the URL and copy, `curl https://example.com/robots.txt -o robots.txt`, or copy from the Search Console robots.txt report. Keep format rules (UTF-8).
- Edit with correct syntax and UTF-8, then upload to site root as `robots.txt` (method is platform dependent). Without root permission, contact the domain manager (example: a site under `subdomain.example.com/site/example/` generally cannot change `subdomain.example.com/robots.txt`).
- Hosted platforms may expose their own search-visibility settings instead.
- Cache: Google notices changes and refreshes its cached copy about every 24 hours. For faster refresh use "Request a recrawl" in the robots.txt report.

## List of useful robots.txt rules
https://developers.google.com/crawling/docs/robots-txt/useful-robots-txt-rules · Last updated: 2026-06-12

- Disallow whole site: `User-agent: *` + `Disallow: /`. URLs may still be indexed without being crawled; AdsBot crawlers are not matched by `*`.
- Allow whole site: empty `Disallow:` (equivalent to no robots.txt or `Allow: /`).
- Disallow a directory: append `/` (`Disallow: /calendar/`). Caution: robots.txt is not for private content (use authentication); disallowed URLs can still be indexed, and the file is public and may reveal where private content lives.
- Disallow single pages: `Disallow: /useless_file.html`, `Disallow: /junk/other_useless_file.html`.
- Whole site except a subdirectory: `Disallow: /` + `Allow: /public/`.
- One crawler only allowed: `Googlebot-News` group `Allow: /`, then `*` group `Disallow: /`.
- Everyone but one crawler: named group `Disallow: /` for it, `*` group `Allow: /`.
- Block whole site but allow Shopping: `*` `Disallow: /`, `Storebot-Google` `Allow: /` (hidden from Search results, still analyzable for Google Shopping).
- Block all images from Google (Images, Discover and other places): `Googlebot-Image` `Disallow: /` (images and videos can't be indexed without crawling). Block one image: `Disallow: /images/dogs.jpg`.
- File type: `User-agent: Googlebot` + `Disallow: /*.gif$`. `$` marks end of URL, so `cats.xls?personality=loki` is NOT blocked by `/*.xls$`.
- Combine user agents in one group (example `Googlebot` + `Storebot-Google` with `Allow: /cats` / `Disallow: /`); same as repeating the rules per agent.

## How Google interprets the robots.txt specification
https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec · Last updated: 2026-10-23

### Scope
- Automated crawlers follow the Robots Exclusion Protocol (RFC 9309): they download and parse robots.txt before crawling. REP does not apply to user-controlled fetchers (feed subscriptions) or user-safety crawlers (malware analysis).

### Location and validity
- Top-level directory of the host, supported protocols for Search: HTTP, HTTPS, FTP. HTTP(S): non-conditional `GET`; FTP: `RETR` with anonymous login. URL is case-sensitive.
- Valid only for the host, protocol and port where it lives:
  - `https://example.com/robots.txt`: valid for that host/protocol/port and all subdirectories; not for `https://other.example.com/`, `http://example.com/`, `https://example.com:8181/`.
  - `https://www.example.com/robots.txt`: only that subdomain (not `example.com`, `shop.www.example.com`, `www.shop.example.com`).
  - `https://example.com/folder/robots.txt`: invalid; subdirectories are never checked.
  - IDN `https://www.exämple.com/robots.txt` equals its punycode (`xn--exmple-cua.com`).
  - `ftp://example.com/robots.txt`: only `ftp://example.com/`.
  - IP host `https://212.96.82.21/robots.txt`: only that IP as hostname, not sites hosted on it.
  - Default ports are equivalent (`:443` = HTTPS default); `:444` and `:8181` are separate scopes.

### Errors and HTTP status codes (fetching robots.txt)
- `2xx`: process the file as served.
- `3xx`: follows at least five redirect hops (RFC 1945), then treats it as `404` (also for disallowed URLs in the chain, because rules could not be fetched). Logical redirects (frames, JavaScript, meta refresh) are not followed.
- `4xx` except `429`: treated as if no valid robots.txt exists, so no crawl restrictions. Don't use `401`/`403` to limit crawl rate; `4xx` (except `429`) have no effect on crawl rate.
- `5xx` (file exists but can't be fetched): for the first 12 hours Google stops crawling the site and keeps trying to fetch it. If still failing, for the next 30 days it uses the last good cached version while retrying (`503` retried fairly often); with no cached copy it assumes no restrictions. After 30 days: if the site is generally available, behaves as if no robots.txt exists (still checks); if the site has general availability problems, stops crawling while periodically requesting robots.txt.
- Other errors (DNS or network issues: timeouts, invalid responses, resets, interrupted connections, HTTP chunking errors) are treated as a server error.

### Caching
- Cached up to about 24 hours, longer when refresh is impossible (timeouts or `5xx`). Cache may be shared across crawlers; lifetime may shift with `max-age` in `Cache-Control`.

### File format
- UTF-8 plain text, lines separated by `CR`, `CR/LF` or `LF`. Invalid lines are ignored, including a Unicode BOM at the start; if HTML is served instead, Google parses what it can and ignores the rest. Non-UTF-8 characters may be ignored.
- Size limit: 500 KiB; content beyond is ignored. Reduce size by consolidating rules (for example place excluded material in a separate directory).

### Syntax
- Line = `<field>:<value><#optional-comment>`. Field names case-insensitive; spaces optional (leading/trailing ignored); `#` comments to end of line.
- Supported fields: `user-agent`, `allow`, `disallow`, `sitemap`. Others (example `crawl-delay`) are unsupported.
- `allow`/`disallow` are written `rule: [path]`; a rule without a path is ignored; default is no restriction. Path is relative to the host root, must start with `/`, case-sensitive.
- `user-agent`: name and value case-insensitive.
- `disallow`: values case-sensitive. Google can't index content of disallowed pages but may index the URL and show it with no snippet.
- `allow`: ignored without a path.
- `sitemap`: supported by Google, Bing and others (sitemaps.org). Value is an absolute URL with protocol and host (no URL-encoding required), may be on a different host, multiple lines allowed with no limit, not tied to any user agent, honored by all crawlers unless the sitemap URL is disallowed. Case-insensitive field, case-sensitive value.

### Grouping and user-agent precedence
- Repeat `user-agent` lines to share rules (example: `e` and `f` share a group; `h` has an empty group).
- Only one group applies per crawler: the one with the most specific matching user agent; group order is irrelevant. Non-matching text is ignored (`googlebot/1.2` and `googlebot*` equal `googlebot`).
- Several groups for the same agent are merged internally. Specific groups and the `*` group are never combined.
- Example (groups `googlebot-news`, `*`, `googlebot`): Googlebot News (and when crawling images) follows `googlebot-news`; Googlebot web follows `googlebot`; `Storebot-Google` and other Google crawlers (even news-related ones not identifying as `googlebot-news`) follow `*`, because a related entry is valid only on exact match.
- Lines other than `allow`, `disallow`, `user-agent` are ignored by the parser, so a `sitemap` line between two `user-agent` lines does not separate groups: `user-agent: a`, `sitemap:`, `user-agent: b`, `disallow: /` yields one group for both `a` and `b`.

### URL path matching
- Rule paths may be raw UTF-8 or percent-encoded (RFC 3986); Google compares percent-encoded forms (RFC 9309 section 2.2.2) and canonicalizes raw UTF-8 automatically (`/foo/bar/ツ` equals `/foo/bar/%E3%83%84`). Percent-encoding is recommended for easier third-party processing (added 2026-10-23).
- Wildcards: `*` = 0 or more of any character; `$` = end of URL.
- Pattern table (case-sensitive):
  - `/` matches root and everything; `/*` equals `/`.
  - `/$` matches only the root.
  - `/fish` and `/fish*` match any path starting `/fish` (`/fish.html`, `/fishheads/yummy.html`, `/fish.php?id=anything`); not `/Fish.asp`, `/catfish`, `/?id=fish`, `/desert/fish`.
  - `/fish/` matches things in that folder (`/fish/`, `/fish/?id=anything`, `/fish/salmon.htm`); not `/fish`, `/fish.html`, `/animals/fish/`, `/Fish/Salmon.asp`.
  - `/*.php` matches any path containing `.php` (including `/filename.php/`, `/folder/filename.php?parameters`); not `/` even if it maps to index.php; not `/windows.PHP`.
  - `/*.php$` matches paths ending `.php`; not `/filename.php?parameters`, `/filename.php/`, `/filename.php5`.
  - `/fish*.php` matches `/fish` then `.php` in order (`/fish.php`, `/fishheads/catfish.php?parameters`); not `/Fish.PHP`.

### Precedence among rules
- Most specific rule wins by rule-path length; among conflicting rules (including wildcards) the least restrictive wins.
- Examples: `allow: /p` beats `disallow: /` on `/page`; `allow: /folder` vs `disallow: /folder` gives allow; `disallow: /*.htm` beats `allow: /page` for `/page.htm` (longer match); `allow: /page` vs `disallow: /*.ph` on `/page.php5` gives allow; `allow: /$` beats `disallow: /` on `/`, but `/page.htm` is disallowed (the allow applies only to root).

## HTTP status codes
https://developers.google.com/crawling/docs/troubleshooting/http-status-codes · Last updated: 2026-02-04

### Scope
- Covers the top 20 status codes Google sees; exotic codes (for example `418`) are not covered. Experimental features of HTTP and FTP are unsupported unless stated.
- Search Console reports errors for `4xx`-`5xx` and for failed redirects (`3xx`). A `2xx` is not a guarantee of indexing.

### Handling per code
| Code | How Google handles it |
|---|---|
| `2xx` (general) | Content considered for processing (for Search: indexing). If the content looks like an error or empty page, Search Console shows `soft 404`. |
| `200` | Passes what it received to the next system (Search: indexing pipeline; may index, not guaranteed). |
| `201` | Same as `200`. |
| `202` | Waits a limited time for content, then passes on whatever it got. Timeout depends on the user agent (Googlebot Smartphone may differ from Googlebot Image). |
| `204` | No content received, so nothing to process. |
| `3xx` (general) | By default follows up to 10 redirect hops; specific products may differ (Googlebot generally 10 for web content; Google Inspection Tools doesn't follow redirects). Content from the redirecting URL is ignored; the target's content is used. For robots.txt see its own redirect rules (5 hops). |
| `301` | Followed; strong signal that the target should be processed. |
| `302` | Followed by default; weak signal that the target should be processed. Other products may differ. |
| `303` | Treated like `302`. |
| `304` | Tells the next system the content is unchanged since the last crawl. Search: indexing may recompute signals but otherwise no effect on indexing. |
| `307` | Equivalent to `302`. |
| `308` | Equivalent to `301`. Google treats the pairs the same but they differ semantically; use the right code so other clients (e-readers, other search engines) benefit. |
| `4xx` (general) | Content ignored and never used. Previously used URLs that return `4xx` are phased out. Search doesn't index `4xx` URLs and removes already indexed ones. |
| `400`, `401`, `403`, `404`, `410`, `411` | All treated the same: signals "content doesn't exist". Indexed URLs are removed; newly found `404` pages are not processed; crawl frequency gradually drops. |
| `429` | Treated as a server-overload signal, i.e. a server error (not a content-gone signal). |
| `5xx` and `429` (general) | Crawlers temporarily slow down. Search keeps already indexed URLs but eventually drops them. Content is ignored. Once `2xx` returns, crawl rate rises gradually. For robots.txt see its own `5xx` handling. |
| `500`, `502`, `503` | Crawl rate is reduced in proportion to how many URLs return a server error. Search removes URLs that persistently return server errors. |

- `401` and `403` must not be used to limit crawl rate: `4xx` (except `429`) don't affect it.

## Network and DNS errors
https://developers.google.com/crawling/docs/troubleshooting/dns-network-errors · Last updated: 2025-12-18

### Effects
- Timeouts, connection resets and DNS errors are treated like `5xx`: crawling slows immediately (the server may not handle load) and no content is received.
- Search can't index such URLs; already indexed unreachable URLs drop from the index within days. Search Console may log an error per type. With third-party hosting/CDN, ask the provider for help.

### Debug network errors (timeouts, connection resets)
- Occur before or during crawling, often with no status code to hint at the cause.
- Check firewall settings and logs for overly broad blocking; make sure Google IPs are not blocked.
- Capture traffic (`tcpdump`, Wireshark) to find anomalies pointing to a component or server module.
- Otherwise contact the hosting company. Causes can be in any component handling traffic (example: overloaded network interfaces drop packets causing timeouts; mistaken closed ports send `RST`).

### Debug DNS errors
- Mostly misconfiguration; a firewall blocking Google DNS queries is another cause.
- Check firewall rules: no Google IPs blocked; both `UDP` and `TCP` allowed.
- Verify `A` and `CNAME` records with `dig` (`dig +nocmd example.com a +noall +answer`, `dig +nocmd www.example.com cname +noall +answer`).
- Verify every name server returns the correct site IPs (`dig ... ns`, then query each name server directly).
- DNS changes within 72 hours may still be propagating; flush Google's Public DNS cache to speed up.
- If you run your own DNS server, make sure it is healthy and not overloaded.

## Troubleshoot crawl errors
https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors · Last updated: 2025-12-18

> Note: Search-specific guide that overlaps the crawling-site pages on crawl budget, status codes and crawl rate. Differences are flagged inline.

### Overview steps
- Check availability issues; find pages that should be crawled but aren't; find parts needing faster crawling; improve crawl efficiency; handle overcrawling.

### Availability issues
- Better availability does not necessarily raise crawl budget (crawl demand sets it), but availability issues stop Google crawling as much as it wants.
- Diagnose: Crawl Stats report shows crawl history and availability issues; in Host availability graphs look for Googlebot requests above the red limit line, drill into failing URLs and correlate with site problems. URL Inspection returning "Hostload exceeded" means Googlebot can't crawl as many URLs as it discovered.
- Treat: read Crawl Stats docs; block pages you don't want crawled; speed up loading and rendering; add server capacity. If Google keeps hitting its serving-capacity limit while important URLs go uncrawled, raise capacity for a month and see whether crawl requests rise.

### Pages not crawled but should be
- Causes: Google doesn't know the page, it is blocked, availability throttling, or budget exhausted. Crawling is not indexing; crawled pages may still not show if value or demand is low.
- Diagnose: Search Console has no per-URL/path crawl history; use server logs. New pages normally take several days at minimum; same-day crawling isn't expected except for time-sensitive sites like news.
- Treat: update sitemaps, check robots.txt for accidental blocks, review crawl priorities, verify serving capacity.

### Updates not crawled fast enough
- Google aims for timely indexing; for most sites that's three days or more. Don't expect same-day indexing unless a news site or similarly time-sensitive.
- Diagnose: logs for crawl time; URL Inspection or a search for the indexing date.
- Do: news sitemap for news content; `<lastmod>` for updated URLs; crawlable URL structure; standard crawlable `<a>` links; with separate mobile HTML, give the mobile version the same links as desktop, or list them in a sitemap (Google indexes only the mobile version).
- Avoid: resubmitting an unchanged sitemap several times a day; expecting everything in a sitemap to be crawled immediately (sitemaps are suggestions); including URLs in sitemaps that shouldn't appear in Search (wastes budget).

### Crawl efficiency
- Page loading speed: crawling is limited by bandwidth, time and Googlebot instance availability. Faster server responses may allow more pages, but speeding up low-quality pages won't make Google crawl more; if it believes high-quality content is missing it will likely raise the budget. Block large unimportant, non-critical resources via robots.txt (never resources needed to understand the page); keep pages fast; avoid long redirect chains; both response time and render time (including embedded images and scripts) matter.
- Content changes via status codes: Google generally supports `If-Modified-Since` and `If-None-Match` but doesn't send them on every crawl (AdsBot is more likely to). `If-Modified-Since` carries the last crawl date/time; the server may return `304` with no body (Google reuses its copy) or `200` with a body if newer. You may also send `304` with no body for any Googlebot request if the content is unchanged since the last visit, saving server resources.

### Hide URLs you don't want in Search
- Categories of wasteful URLs: faceted navigation and session IDs; duplicate content; `soft 404` pages; hacked pages (check Security Issues report); infinite spaces and proxies (block in robots.txt); low-quality/spam content; shopping cart, infinite scroll and action pages ("sign up", "buy now").
- Warning: blocking or hiding already-crawled pages won't shift budget elsewhere unless Google is at its serving limit.
- Do: robots.txt for resources/pages Google should not crawl at all; reference shared resources (images, JS) from one identical URL on every page so Google can cache and reuse them.
- Avoid: regularly adding/removing robots.txt entries to reallocate budget (use it for long-term exclusions only); rotating sitemaps or other temporary hiding.

### `soft 404` errors
- Definition: URL returns `200` while showing a not-found/error message, or an empty page/no main content. Causes: missing server-side include, broken database connection, empty internal search result page, missing JavaScript file. Such pages are excluded from Search; Search Console shows `soft 404` in the Page Indexing report when detected by content.
- Fix by situation:
  - Gone with no replacement: `404` or `410`. Custom `404` pages are allowed and should match site look and navigation, tell visitors clearly the page is missing in friendly language, link popular content and the home page, optionally offer a broken-link report; the server must still return `404`.
  - Moved or clear replacement: `301` redirect; verify with URL Inspection.
  - Still exists but flagged: probably failed to load properly for Googlebot (missing critical resources, prominent error during rendering). Use URL Inspection to see rendered content and returned code. A blank or error-looking render often comes from resources that can't be loaded (blocked by robots.txt, too many resources, server errors, slow or very large resources).

### Overcrawling emergencies
- Googlebot has built-in protections, but if it overwhelms the site: return `503` or `429` temporarily for Googlebot requests; Googlebot retries those URLs for about 2 days. Returning "no availability" codes for more than a few days causes Google to permanently slow or stop crawling.
- Once the rate drops, stop sending `503`/`429`; sending them for more than 2 days makes Google drop those URLs from the index. Keep monitoring crawl rate and host capacity.
- If the culprit is an AdsBot crawler, it is likely Dynamic Search Ad targets; that crawl recurs every 3 weeks. Limit ad targets or add capacity.

> Note: This page says retry window is about 2 days and dropping starts after more than 2 days; "Reduce the Google crawl rate" says to avoid it beyond 1-2 days. Treat 1-2 days as the safe maximum.

## Ask Google to recrawl your URLs
https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl · Last updated: 2025-12-10

- On hosted platforms (Blogger, WordPress) the platform usually submits new content automatically; check platform docs.
- You can request (re)indexing only for URLs you manage. Crawling takes a few days to a few weeks; monitor via the Index Status report or URL Inspection tool. A request guarantees neither fast nor any inclusion.
- URL Inspection tool (a few URLs): requires owner or full user of the Search Console property. There is a quota for individual URL submissions; repeat requests for the same URL do not speed it up.
- Sitemap (many URLs): best for large numbers, new launches or site moves. A sitemap can carry metadata for alternate languages, video, image, news.

## Crawling changelog
https://developers.google.com/crawling/docs/changelog · Last updated: 2026-10-30

Updates feed: `https://developers.google.com/crawling/docs/changelog/crawling_docs_updates.rss`. Newest first.

- 2026-10-30: Common crawlers page notes Google's intent to support the shared machine-readable AI training preference signal.
- 2026-10-23: robots.txt spec: added recommendation to percent-encode rule paths.
- 2026-10-06: Reduce crawl rate: restructured emergency section and added `Retry-After` header details and examples (support not new; already in "Temporarily pause or disable a website").
- 2026-09-17: `Mediapartners-Google` documentation generalized to cover several ad products (AdSense, Ad Manager); heading renamed.
- 2026-07-22: Crawl budget guide polished for clarity and consistent terms (for example crawl capacity limit).
- 2026-07-16: NotebookLM user agent renamed `Google-GeminiNotebook` (now Gemini Notebook); old value still supported for transition; update hardcoded strings.
- 2026-07-14: Corrected `Google-InspectionTool` UA string (had a stray semicolon that production does not use).
- 2026-05-04: Added Web Bot Auth documentation (experimental; some Google agents start using it).
- 2026-03-20: Added `Google-Agent` UA (rolling out over following weeks; Google-hosted agents acting on user request) and IP ranges for user-triggered agents in the verification docs.
- 2026-03-03: Added overview page about how Google's crawling works.
- 2026-02-11: IP range files for common crawlers, special crawlers, user-triggered fetchers moved to `/crawling/ipranges` (old `/search/apis/ipranges` still works for now; update links).
- 2026-02-03: Default file size limits for crawlers and fetchers moved from the Googlebot docs to the crawling docs.
- 2026-01-21: Added Google Messages to user-triggered fetchers (link previews in chat).
- 2025-12-18: Migrated faceted navigation, crawl budget, HTTP status codes and DNS/network error docs to the crawling site (no functional change; wording notes that guidance spans products).
- 2025-12-02: Google Read Aloud page expanded (stateless rendering, needs page access to see meta tags).
- 2025-11-20: Migrated crawlers overview, verification, reduce crawl rate, common crawlers, robots.txt spec to the new crawling site (content unchanged).
- 2025-11-12: Added `Google-Pinpoint` fetcher.
- 2025-11-03: Added `Google-CWS` fetcher.
- 2025-10-15: Updated list of Google products using the Read Aloud service.
- 2025-10-09: Added `Google-NotebookLM` to user-triggered fetchers.
- 2025-07-01: Google Read Aloud UA updated with newer browser versions (for sites that reject old ones).
- 2025-04-25: `Google-Extended` token description clarified.
- 2025-04-25: Corrected `Googlebot-News` description: its preferences do not affect the News tab on Google (only the News product).
