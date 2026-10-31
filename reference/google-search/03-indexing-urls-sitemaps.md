# Indexing: file types, URL structure, links, sitemaps, canonicalization, mobile-first indexing, AMP: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Overview of crawling and indexing topics
https://developers.google.com/search/docs/crawling-indexing · Last updated: 2025-12-10

### Purpose
- Section covers how to control Google's ability to find and parse content for Search and other Google properties, and how to stop Google crawling specific content.

### Topic map
- File types indexable by Google.
- URL structure: logical, human-intelligible URLs.
- Sitemaps: tell Google about new or updated pages.
- Crawler management: ask for recrawl, faceted-navigation crawling, crawl budget for large sites, HTTP status/network/DNS error effects, Google crawlers.
- robots.txt: tells crawlers which pages or files they may request.
- Canonicalization: how Google auto-detects and treats duplicates and assigns a canonical to each duplicate group; how to tell Google about duplicates to avoid excessive crawling.
- Mobile sites: optimize and ensure correct crawling and indexing.
- AMP: how AMP works in Search.
- JavaScript: differences and limits of how crawlers access and render content.
- Page and content metadata: valid HTML for metadata, supported `meta` tags, robots `meta`/`data-nosnippet`/`X-Robots-Tag`, `noindex` meta tag, crawlable links, `rel` attributes for outbound links.
- Removals: control what you share, remove a hosted page, remove hosted images, keep redacted information out.
- Site moves and changes: redirects, site moves, A/B testing impact, temporarily pausing a site.

## File types Google can index
https://developers.google.com/search/docs/crawling-indexing/indexable-file-types · Last updated: 2026-02-03

### How the type is determined
- Google can index most text-based files and certain encoded document formats.
- File type is determined by the `Content-Type` HTTP header received at crawl time.
- If `Content-Type` is missing or wrong, Google may fall back to the file extension or re-parse with a different parser.

### Supported flat file types (plain, unencoded text, may use markup)
- `.csv`
- `.kml`, `.kmz` (Google Earth)
- `.gpx` (GPS eXchange Format)
- `.htm`, `.html`, and other extensions (HTML)
- `.svg`
- `.tex` (TeX/LaTeX)
- Text: `.txt`, `.text`, other extensions, including source code: `.bas`; `.c`, `.cc`, `.cpp`, `.cxx`, `.h`, `.hpp`; `.cs`; `.java`; `.pl`; `.py`
- `.wml`, `.wap` (Wireless Markup Language)
- `.xml`

### Supported encoded file types (need a parser to extract text)
- `.pdf`, `.ps` (PostScript), `.epub`, `.hwp` (Hancom Hanword)
- Microsoft: `.xls`, `.xlsx`; `.ppt`, `.pptx`; `.doc`, `.docx`
- OpenOffice: `.odp`, `.ods`, `.odt`
- `.rtf`

### Supported media formats
- Images: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF.
- Video: 3GP, 3G2, ASF, AVI, DivX, M2V, M3U, M3U8, M4V, MKV, MOV, MP4, MPEG, OGV, QVT, RAM, RM, VOB, WebM, WMV, XAP.

### Search by file type
- `filetype:` operator limits results to a file type or extension; example `filetype:rtf galway` matches RTF files and URLs ending in `.rtf` containing the term.

## URL structure best practices for Google Search
https://developers.google.com/search/docs/crawling-indexing/url-structure · Last updated: 2026-10-21

### Requirements for a crawlable URL structure
- Failing these means Google will likely crawl inefficiently (including extremely high crawl rates) or not at all.
- Follow IETF STD 66: characters the standard defines as reserved must be percent-encoded.
- Don't use URL fragments to change page content (e.g. `https://example.com/#/potatoes`); Google generally doesn't support fragments. When JavaScript changes content, use the History API.
- Common parameter encoding: `=` between key and value, `&` between parameters. Multiple values for one key may use any character not conflicting with STD 66, such as `,` (e.g. `color=purple,pink,salmon`).
- Not recommended: `:` for key-value with brackets `[ ]` between parameters (`?[category:dresses][sort:price-low-to-high]`); single `,` for key-value with `,,` between parameters (`?category,dresses,,sort,lowtohigh`).

### Make URLs easy to understand
- Descriptive: readable words rather than long ID numbers (`/wiki/Aviation` over `index.php?topic=42&area=3a5ebc944f41daa6f849f730f1`).
- Use the audience's language (and transliterated words where relevant): e.g. German words for German searchers (`/lebensmittel/pfefferminz`); Japanese characters are shown in an example.
- Percent-encode as necessary in `href` attributes: unreserved ASCII may stay unencoded; non-ASCII characters (Arabic, Chinese, umlauts, emoji) should be percent-encoded (`/gem%C3%BCse` recommended over `/gemüse`).
- Separate words with hyphens `-`, not underscores `_` (underscores conventionally join concepts, e.g. `format_date`; hyphens signal word boundaries). Joined words (`/greendress`) are also not recommended.
- Use as few parameters as possible; trim parameters that don't change content.
- URLs are case sensitive: `/APPLE` and `/apple` are distinct URLs. If the server treats cases the same, convert all URL text to one case so Google can see they are the same page.
- Multi-regional sites: choose a structure that makes geotargeting easy. Recommended: country-specific domain (`https://example.de`) or country subdirectory on a gTLD (`https://example.com/de/`).

### Avoid common URL problems
- Overly complex URLs, especially with many parameters, create excessive numbers of URLs for identical or similar content. Result: Googlebot may use excess bandwidth or be unable to index all content.
- Additive filtering: combinable filters (beach + fitness center) make URL counts explode; Googlebot only needs a small number of lists from which it can reach each item page.
- Irrelevant parameters: referral parameters (`click=`, `referrerid=`, `ref=`), sort parameters, and session IDs (`sessionid=`). Avoid session IDs in URLs; use cookies. Consider blocking problematic URLs with robots.txt.
- Calendar issues: dynamically generated calendars linking to unlimited past or future dates (`calendar.php?d=13&m=8&y=2011`). Add `nofollow` to links to dynamically created future calendar pages if the calendar is infinite.
- Broken relative links: a parent-relative link (`../../category/stuff`) on the wrong page can create infinite spaces if the server doesn't return the right HTTP status for nonexistent pages. Fix: use root-relative URLs instead of parent-relative.

### Fixing crawling-related URL problems
- Consider blocking Googlebot with robots.txt for dynamic URLs that generate search results, and for URLs that create infinite spaces: calendars, ordering and filtering functions.
- Sites with faceted navigation: follow the guidance on managing crawling of faceted navigation URLs.

## Link best practices for Google
https://developers.google.com/search/docs/crawling-indexing/links-crawlable · Last updated: 2025-12-10

### Role of links
- Google uses links as a signal of page relevancy and to discover new pages to crawl.

### Make links crawlable
- Generally only `<a>` elements with an `href` attribute are crawled. Most other formats aren't parsed; Google can't reliably extract URLs from `<a>` without `href` or from other tags acting as links via script events.
- Parseable (recommended): `<a href="https://example.com">`, `<a href="/products/category/shoes">`, `<a href="./products/category/shoes">`, `<a href="..." onclick="...">` (valid `href` plus handler), `<a href="..." class="pretty">`.
- Links inserted dynamically with JavaScript are crawlable if they use the same `<a href>` markup.
- Not recommended (Google may still try): `<a routerLink="...">`, `<span href="...">`, `<a onclick="goto('...')">`.
- `href` must resolve to a real web address (URI-like) Google can request: `https://example.com/stuff`, `/products`, `/products.php?id=123` are fine.
- Not recommended (Google may still try): `<a href="javascript:goTo('products')">`, `<a href="javascript:window.location.href='/products'">`.

### Anchor text placement
- Anchor text is the visible link text; put it between `<a>` tags that Google can crawl. Empty link text is bad.
- Fallback: if the `<a>` is empty, Google can use the `title` attribute as anchor text.
- Image links: Google uses the `img` `alt` attribute as anchor text; empty `alt` plus empty link text is bad.
- If JavaScript inserts anchor text, check it is present in rendered HTML with the URL Inspection tool.

### Write good anchor text
- Descriptive, reasonably concise, relevant to both the host page and the target page.
- Bad (generic): "click here", "read more", "website", "article". Tip: read only the anchors out of context; if you can't tell what the targets are about, improve them.
- Bad (excessively long): anchor spanning a whole clause; shorten to the key phrase.
- Don't stuff keywords into anchors (keyword stuffing violates spam policies). Test: does the reader need the keywords to understand the next page?
- Context matters: words before and after the link count. Don't chain several links next to each other (e.g. five single-word links in a row); space them with surrounding text.

### Internal links
- Every page you care about should be linked from at least one other page on the site.
- Link to helpful related resources in context.
- No ideal link count per page; if it feels like too many, it probably is.

### External links
- Linking out is fine and can help establish trustworthiness (e.g. citing sources); give readers context on what to expect.
- Use `nofollow` only for sources you don't trust, not on every external link (example: responding to an article badmouthing your product without passing your reputation).
- Paid links: qualify with `sponsored` or `nofollow`.
- User-generated links (forums, Q&A): add `ugc` or `nofollow`.

## Learn about sitemaps
https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview · Last updated: 2025-12-10

### What a sitemap is
- A file listing pages, videos and other files and the relationships between them; search engines read it to crawl more efficiently.
- Signals which URLs you consider important and metadata such as last update and alternate language versions.
- Can carry type-specific data: video (running time, rating, age-appropriateness), image (image locations on a page), news (article title, publication date).
- CMSes such as WordPress, Wix, Blogger usually already provide a sitemap.

### Do you need one
- If pages are properly linked (all important pages reachable via navigation or in-page links), Google can usually discover most of the site.
- A sitemap helps discovery but does not guarantee every listed URL is crawled or indexed. In most cases a site benefits from having one.
- Likely needed: large site (harder to ensure every page is linked); new site with few external links; lots of rich media (video, images) or presence in Google News.
- Likely not needed: "small" site (about 500 pages or fewer, counting only pages meant for search results); comprehensive internal linking from the home page; few media or news pages to surface.

## Build and submit a sitemap
https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap · Last updated: 2026-07-08

### Supported formats (Google has no preference; all defined by the sitemaps protocol)
- XML sitemap: most versatile and extensible; carries image, video, news and localized-version data; provides the most URL information. Cons: cumbersome, hard to maintain on large or frequently changing sites. Most CMSes generate it or have plugins.
- RSS 2.0, mRSS and Atom 1.0: often easiest because CMSes generate feeds. Beyond HTML/indexable text pages it can only describe videos (not images or news). Feeds usually include only recent URLs.
- Text sitemap: simplest; lists only HTML and other indexable text-content URLs; easy to maintain on large sites.

### Best practices and limits
- Size limit for every format: 50MB uncompressed or 50,000 URLs per sitemap. Larger: split into multiple sitemaps (must).
- Optional sitemap index file; submit that single index. Multiple sitemaps and index files may be submitted; useful for per-sitemap performance tracking in Search Console.
- Encoding: UTF-8.
- Location: anywhere on the site, but unless submitted via Search Console a sitemap affects only descendants of its parent directory. Root placement covers all files and is recommended.
- URLs: fully qualified absolute (e.g. `https://www.example.com/mypage.html`, not `/mypage.html`); Google crawls them exactly as listed.
- Include URLs you want in search results (canonicals). For separate mobile and desktop URLs, point to one version only; to list both, annotate desktop and mobile versions.
- URL order doesn't matter.

### XML sitemap specifics
- Root `urlset` with namespace `http://www.sitemaps.org/schemas/sitemap/0.9`; each `url` has `loc` and optional `lastmod` (example date format `2022-06-04`).
- All tag values must be entity-escaped.
- Google ignores `<priority>` and `<changefreq>`.
- `<lastmod>` is used only if consistently and verifiably accurate (e.g. compared against actual page modification). It should reflect the last significant update (main content, structured data, links = significant; copyright date = not).

### RSS, mRSS, Atom 1.0 specifics
- Google accepts RSS 2.0 and Atom 1.0; mRSS (media RSS) conveys video details.
- Entity-escape tag values.
- Submit the feed URL as a sitemap.

### Text sitemap specifics
- One URL per line; nothing but URLs in the file.
- Any filename, `.txt` extension required (e.g. `sitemap.txt`).

### Creating a sitemap
- Sitemaps declare which URLs you prefer in results (canonicals); if content is reachable under several URLs, list only your preferred one.
- Options: CMS generation; manual for fewer than a few dozen URLs (any text editor, filename must use URL-legal characters); generated for more than a few dozen URLs (best done by the site software, e.g. exporting URLs from the database). Third-party generator collection is old and unmaintained.

### Submitting to Google
- Submission is only a hint; no guarantee Google downloads or uses it.
- Methods: Search Console Sitemaps report (shows last access and processing errors); Search Console API; `Sitemap: https://example.com/my_sitemap.xml` line anywhere in robots.txt (found at next robots.txt crawl; multiple lines allowed, no limit on count); WebSub for Atom/RSS feeds.

### Cross-submission for multiple sites
- One sitemap can list URLs of multiple sites, including different domains (e.g. `host1.example.com/sitemap.xml` covering `host2.example.com`, `host1.example1.com`, `host1.example.ch`), or one sitemap per site all hosted in one location.
- Via Search Console: verify ownership of all included sites, create sitemap(s) (optionally in an index), submit them.
- Via robots.txt: build per-site sitemaps containing only that site's URLs; upload all to one site you control (e.g. `https://sitemaps.example.com`); each site's robots.txt references its own sitemap with a `sitemap:` line.

### Troubleshooting
- Investigate errors in Search Console; see its sitemaps troubleshooting guide.

## Manage your sitemaps with a sitemap index file
https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps · Last updated: 2025-12-10

### Sitemap index best practices
- Use when a sitemap exceeds size limits: split so each file is under the limit, then list them in an index.
- Index XML is like sitemap XML (Sitemap Protocol); all sitemap requirements also apply to index files.
- Referenced sitemaps must be on the same site as the index (waived with cross-site submission).
- Referenced sitemaps must be in the index's directory or deeper (index at `https://example.com/public/sitemap_index.xml` may list only `https://example.com/public/...` and below).
- Up to 500 sitemap index files per site in a Search Console account.

### Sitemap index reference
- Namespace: `http://www.sitemaps.org/schemas/sitemap/0.9`.
- Required tags: `sitemapindex` (root); `sitemap` (parent for each listed sitemap; only direct child of `sitemapindex`); `loc` (sitemap URL, child of `sitemap`; up to 50,000 `loc` tags per index).
- Optional: `lastmod` (child of `sitemap`; when the sitemap file was modified; W3C Datetime format).
- Entries may point to `.xml.gz` files (example).

## How to combine sitemap extensions
https://developers.google.com/search/docs/crawling-indexing/sitemaps/combine-sitemap-extensions · Last updated: 2025-12-10

### Namespaces (declare each via `xmlns` on `urlset`)
- `image:` → `http://www.google.com/schemas/sitemap-image/1.1`
- `news:` → `http://www.google.com/schemas/sitemap-news/0.9`
- `video:` → `http://www.google.com/schemas/sitemap-video/1.1`
- `xhtml:` (for `hreflang`) → `http://www.w3.org/1999/xhtml`
- Base sitemap namespace: `http://www.sitemaps.org/schemas/sitemap/0.9`.

### Combining
- Declare several namespaces on one `urlset`; place each extension's tags one after another inside the relevant `<url>`.
- Order of extension blocks after `<loc>` is irrelevant.
- `hreflang` entries are `<xhtml:link rel="alternate" hreflang="…" href="…"/>`; the example lists each language version including the page itself (`en`, `de`, `de-ch`).
- Combining extensions increases file size significantly; the standard size limits still apply.

## Image sitemaps
https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps · Last updated: 2025-12-10

### Purpose and form
- Tell Google about images it might not find otherwise (e.g. images reached via JavaScript).
- Either a separate image sitemap or image tags in an existing sitemap; equally fine. General sitemap and image publishing best practices apply.

### Reference
- Namespace: `http://www.google.com/schemas/sitemap-image/1.1`.
- Required `<image:image>`: encloses one image; up to 1,000 per `<url>`.
- Required `<image:loc>`: image URL. May be on another domain if both domains are verified in Search Console (e.g. a CDN host must be verified). robots.txt must not disallow crawling of images you want indexed.
- Skeleton: `<url><loc>page</loc><image:image><image:loc>img</image:loc></image:image></url>`.

### Deprecated tags
- Removed from documentation: `<image:caption>`, `<image:geo_location>`, `<image:title>`, `<image:license>` (deprecation announcement referenced; date not stated on the page).

## News sitemaps
https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap · Last updated: 2025-12-10

### Best practices
- For news publishers: extend an existing sitemap or create a dedicated news sitemap (dedicated may give better tracking in Search Console).
- Update the same sitemap with fresh articles; don't create a new sitemap per update. Google News crawls news sitemaps as often as the rest of the site.
- Include only URLs of articles created in the last two days; after that remove the URLs or just the `<news:news>` metadata.
- Removing old URLs may leave the sitemap empty; Search Console may show an "Empty Sitemap" warning, which is only a check of intent and harmless to Search.

### Reference (namespace `http://www.google.com/schemas/sitemap-news/0.9`)
- `<news:news>` (required): parent of other `news:` tags. One per `url`; up to 1,000 per sitemap, beyond that split the sitemap.
- `<news:publication>` (required): parent of name and language; one per `news:news`.
- `<news:name>` (required): publication name, exactly as on articles at news.google.com, omitting parenthesized text.
- `<news:language>` (required): ISO 639 code, 2 or 3 letters; exceptions `zh-cn` (Simplified Chinese) and `zh-tw` (Traditional Chinese).
- `<news:publication_date>` (required): W3C format, original first-publication date/time, not when added to the sitemap. Accepted: `YYYY-MM-DD`; `YYYY-MM-DDThh:mmTZD`; `YYYY-MM-DDThh:mm:ssTZD`; `YYYY-MM-DDThh:mm:ss.sTZD`.
- `<news:title>` (required): article title as on the site; Google may shorten it. Don't include author, publication name or date.

## Video sitemaps and alternatives
https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps · Last updated: 2026-05-20

### Best practices
- Google recommends video sitemaps; mRSS feeds also supported. Separate sitemap/mRSS or tags in an existing sitemap.
- Don't list videos unrelated to the host page's content (e.g. minor addendum).
- Every URL referenced must be accessible to Googlebot: not disallowed in robots.txt, accessible without metafiles and without login, not blocked by a firewall, and on a supported protocol: HTTP and FTP (streaming protocols unsupported).
- To keep spammers from the `<player_loc>`/`<content_loc>` URLs, verify that bots are really Googlebot.
- Each tag may appear once per video unless noted.

### Video sitemap reference (namespace `http://www.google.com/schemas/sitemap-video/1.1`)
- Required:
  - `<video:video>`: parent for one video; multiple allowed per `<loc>`, one per video on the host page.
  - `<video:thumbnail_loc>`: thumbnail image URL; follow video thumbnail requirements.
  - `<video:title>`: escape HTML entities or use `CDATA`; should match the on-page title.
  - `<video:description>`: max 2048 characters; escape entities or `CDATA`; must match the on-page description but not word for word.
  - One of `<video:content_loc>` or `<video:player_loc>` is required:
    - `content_loc`: URL of the actual media file in a supported format; recommended when possible as the most effective way to fetch content; HTML and Flash unsupported; must differ from parent `<loc>`; equals `VideoObject.contentUrl`.
    - `player_loc`: player URL (usually the `src` of an `<embed>`); must differ from `<loc>`; used instead of `content_loc` for iframe-embed hosts like YouTube and Vimeo; equals `VideoObject.embedUrl`.
    - If access should be restricted but crawlable, let Googlebot in by verifying it.
- Optional:
  - `<video:duration>`: seconds, `1` to `28800` (8 hours).
  - `<video:expiration_date>`: W3C format (`YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ss+TZD`); omit if no expiry; Search stops showing the video after this date; update for recurring videos at the same URL.
  - `<video:rating>`: float `0.0` to `5.0`.
  - `<video:view_count>`: number of views.
  - `<video:publication_date>`: first-published date, W3C format as above.
  - `<video:family_friendly>`: `yes` (available with SafeSearch on; default if tag omitted) or `no` (only with SafeSearch off).
  - `<video:restriction>`: space-delimited ISO 3166 country codes; required attribute `relationship` = `allow` (listed allowed, others denied) or `deny` (listed denied, others allowed). No tag = shown everywhere. Affects search results only.
  - `<video:platform>`: space-delimited values `web`, `mobile`, `tv`; required attribute `relationship` = `allow` (omitted platforms denied) or `deny` (omitted allowed). No tag = all platforms. Affects search results only.
  - `<video:requires_subscription>`: `yes` or `no` (paid or free subscription).
  - `<video:uploader>`: name, max 255 characters; optional attribute `info` = URL of a page about the uploader, must be on the same domain as `<loc>`.
  - `<video:live>`: `yes` or `no`.
  - `<video:tag>`: one element per tag; max 32 tags per video; short keywords (a video may have several tags but belong to one category).

### Deprecated tags and attributes
- Removed from documentation: `<video:category>`, `<video:gallery_loc>`, the `autoplay` and `allow_embed` attributes of `<video:player_loc>`, `<video:price>` and its attributes, `<video:tvshow>` and its attributes.

### mRSS alternative
- mRSS is an RSS 2.0 module for multimedia with richer descriptions; tested, submitted and updated like sitemaps. Example declares `xmlns:media="http://search.yahoo.com/mrss/"` and `xmlns:dcterms="http://purl.org/dc/terms/"`.
- Required:
  - `<media:content>`: attributes `medium` (set to `video`), `url` (direct media URL; if absent `<media:player>` is required), `duration` (optional, recommended, seconds).
  - `<media:player>`: player URL; at least one of this or `media:content@url` required; must not equal `<loc>` or the item `<link>` (link = host page, player = player).
  - `<media:title>`: max 100 characters; escape entities or `CDATA`.
  - `<media:description>`: max 2048 characters; escape or `CDATA`.
  - `<media:thumbnail>`: preview image URL; follow thumbnail requirements.
- Optional:
  - `<dcterms:valid>`: publication and expiration, e.g. `start=…; end=…; scheme=W3C-DTF`.
  - `<media:restriction>`: space-delimited ISO 3166 countries; required attributes `type="country"` (only country restrictions supported) and `relationship` = `allow`/`deny`.
  - `<media:price>`: only for paid videos; repeatable; required attributes `currency` (ISO 4217) and `type` = `rent`, `purchase`, `package`, `subscription`.
- Full mRSS spec has more optional tags.

> Note: the mRSS example shows an `.flv` file and a `.swf` player and a `<media:price>` without a `type` attribute, although the sitemap tag docs say Flash isn't a supported format and `type` is required for `media:price`; treat the example as illustrative only.

## What is canonicalization
https://developers.google.com/search/docs/crawling-indexing/canonicalization · Last updated: 2026-08-20

### Definition
- Canonicalization selects the representative (canonical) URL from a set of duplicate pages; also called deduplication; lets Search show one version of duplicate content.

### Why duplicates exist
- Region variants (e.g. US and UK URLs with `hreflang` but the same-language content); device variants (mobile and desktop versions); protocol variants (HTTP and HTTPS); site functions (sort and filter results); accidental variants (demo site left crawlable).
- Some duplication is normal and not a spam violation, but many URLs for one content confuse users and make tracking performance harder.

### How Google picks the canonical
- At indexing Google identifies each page's primary content (centerpiece). Pages with the same or very similar primary content are clustered; Google picks the one its collected signals show as most complete and useful and marks it canonical.
- The canonical is crawled most regularly; duplicates less often, to reduce crawl load.
- Factors: HTTP vs HTTPS, redirects, presence in a sitemap, `rel="canonical"` link annotations. Your preference is a hint, not a rule; Google may choose differently.
- Language versions are duplicates only if the primary (body) content is in the same language (translating only header/footer/non-critical text doesn't make them distinct). For same-language regional variants use both canonicalization and `hreflang`.
- Google uses the canonical page as the main source to evaluate content and quality. Search results usually link the canonical, unless a duplicate is better suited to the user (e.g. the mobile page for a mobile user even if the desktop page is canonical).

## How to specify a canonical URL with rel="canonical" and other methods
https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls · Last updated: 2026-07-10

### Signals and their strength (strongest first)
- Redirects: strong signal that the redirect target should be canonical.
- `rel="canonical"` link annotations (HTML element or HTTP header): strong signal.
- Sitemap inclusion: weak signal.
- Other signals (page section below): HTTPS preference and `hreflang` cluster membership.
- Signals stack; combining two or more raises the odds your preferred URL is shown.
- None is required; if you specify nothing Google picks the objectively best version.
- In a CMS (WordPress, Wix, Blogger) look for an SEO settings page or `<head>` editing instructions.

### Reasons to specify a canonical
- Control which URL users see (e.g. a clean product URL over a `?gclid=` URL).
- Consolidate signals such as inbound links onto one URL.
- Simplify metrics tracking for a piece of content.
- Avoid wasting crawl time on duplicates.

### Best practices (all methods)
- Don't use robots.txt for canonicalization: disallowed URLs may still be indexed without content.
- Don't use the URL removal tool for canonicalization: it hides all versions of the URL.
- Don't give different canonicals for one page via different techniques (e.g. sitemap says one URL, `rel="canonical"` another).
- Don't specify a URL fragment as canonical.
- Put a self-referential `rel="canonical"` on the canonical page itself.
- Don't use `noindex` to steer canonical selection within one site: it blocks the page from Search entirely; `rel="canonical"` is preferred.
- With `hreflang`, the canonical must be in the same language, or best available substitute language.
- Link internally to the canonical URL, not to duplicates.
- Client-side rendering: best is to put the canonical in the HTML source and make sure JavaScript doesn't change it; if it can't be in the source, omit it there and set it only with JavaScript.

### Method comparison
- `rel="canonical"` link element: maps unlimited duplicates; hard to maintain on large or URL-churning sites; HTML pages only.
- `rel="canonical"` HTTP header: doesn't add page size; maps unlimited duplicates; same maintenance issue; works for non-HTML such as PDF.
- Sitemap: simple on large sites; Google must still work out duplicates for declared canonicals; weaker signal than `rel="canonical"`.
- Redirects: permanent redirects say the redirected URL is the worse version; use only when retiring a duplicate.
- AMP variant: follow AMP guidelines for canonical and AMP variant.

### `rel="canonical"` link annotations
- Supported per RFC 6596. Annotations that suggest alternate versions are ignored: `rel="canonical"` with `hreflang`, `lang`, `media` or `type` attributes is not used for canonicalization (use `rel="alternate" hreflang` etc.).
- Deliver via HTML element or HTTP `Link` header; choose one, since using both is more error-prone (conflicting URLs).
- Link element: in `<head>` of duplicates, pointing to the canonical; also add the same self-referential element on the canonical page. Only accepted inside `<head>`, so the `<head>` must be valid HTML. If JavaScript adds it, inject it properly.
- If the canonical page has a separate mobile URL, add `<link rel="alternate" media="only screen and (max-width: 640px)" href="mobile-URL">` next to the canonical element; add `hreflang` or other elements as appropriate.
- Use absolute URLs, not relative (relative is supported but risky, e.g. if a test site gets crawled).
- HTTP header: a `Link` header with `rel="canonical"` (RFC5988), usable for any document Search supports including PDFs; web search results only. Example: the `.docx` response sends `Link: <https://www.example.com/downloads/white-paper.pdf>; rel="canonical"` to make the PDF canonical. Use absolute URLs.

### Use a sitemap
- Submit the canonical URL of each page; every listed page is suggested as canonical and Google decides which are duplicates by content similarity. Easy way to define canonicals on large sites.

### Use redirects
- To eliminate duplicate pages. All permanent redirect methods have the same effect on Search, but discovery speed may differ; HTTP server-side redirects are quickest.
- Example: `https://example.com/home`, `https://home.example.com`, `https://www.example.com` → pick one, redirect others.

### Other signals: prefer HTTPS over HTTP
- Google prefers HTTPS as canonical unless: invalid SSL certificate; insecure dependencies (other than images); HTTPS page redirects users to or through an HTTP page; HTTPS page has `rel="canonical"` to the HTTP page.
- To reinforce: redirect HTTP to HTTPS; `rel="canonical"` from HTTP to HTTPS; implement HSTS.
- Avoid: bad TLS/SSL certificates and HTTPS→HTTP redirects (cause a very strong preference for HTTP that HSTS can't override); listing HTTP versions in the sitemap or `hreflang` instead of HTTPS; a certificate for the wrong host variant (must match the full site URL or be a wildcard covering the subdomains).

### Other signals: prefer URLs in `hreflang` clusters
- URLs belonging to reciprocal `hreflang` clusters are preferred as canonical. Example: `/de-de/cats` and `/de-ch/cats` reference each other but not `/de-at/cats` → the first two are preferred over `/de-at/`.

## Fix canonicalization issues
https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting · Last updated: 2026-08-21

### Troubleshooting steps
- Google may pick a different canonical than you designate (content quality, technical signals).
- Check which page Google considers canonical with the URL Inspection tool and judge whether it serves users from Search better. Important: if the canonical URL is in a Search Console property you don't own, you can't see traffic for your duplicate page.
- Look for technical misconfigurations signaling an unexpected preference (table below).
- Ensure clustered pages are sufficiently different: fixing is about making the clustered pages distinct. Re-evaluation takes time: Google may hold pages in a duplicate cluster for up to two weeks after content fixes. Pages split faster when the difference from the others is clear and significant.
- After fixing, use "Request Indexing" in URL Inspection; it is quota-limited, so reserve it for the most important URLs.

### Common canonicalization issues
- Language variants without localized annotations: same content for different regions (e.g. US, UK, Australia English sites) needs `hreflang` so the right page surfaces per region.
- Incorrect canonical elements: CMSes or plugins may point canonicals (or `3xx` redirects) at undesired URLs; inspect HTML in browser dev tools and report to the CMS provider.
- Misconfigured servers: hosting errors cause cross-domain selection, e.g. a server returning `example.com` content for a request to `other.example`, or unrelated servers returning identical `soft 404` pages Google fails to detect. Contact the host.
- Malicious hacking: injected code returning `3xx` redirects or cross-domain `rel="canonical"` (HTML head or HTTP header) to spammy or malicious URLs; Google may select the malicious URL over the compromised site's own.
- Syndicated content: canonical element isn't recommended to prevent duplication by syndication partners because the pages often differ a lot. Most effective: partners block indexing of your content (see the Google News article-duplication guidance).
- Copycat website: rarely Google may choose an external URL hosting your content without permission. Ask the host to remove it if it violates copyright, and/or file a Digital Millennium Copyright Act request with Google.

## Mobile site and mobile-first indexing best practices
https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing · Last updated: 2025-12-10

### Principle
- Google uses the mobile version of content, crawled with the smartphone agent, for indexing and ranking (mobile-first indexing).
- A mobile version isn't required for inclusion but is very strongly recommended.

### Mobile configurations
- Responsive design: same HTML on the same URL for all devices, display varies by screen size; Google recommends it (easiest to implement and maintain).
- Dynamic serving: same URL, different HTML per device via user-agent sniffing and the `Vary: user-agent` response header.
- Separate URLs: different HTML on separate URLs; relies on user-agent and `Vary` headers to redirect users to the right version.
- This guide's specifics apply to dynamic serving and separate URLs; with responsive design content and metadata are identical.
- CMS users may need a new mobile-friendly theme.

### Access and render
- Use the same robots `meta` tags on mobile and desktop; a different tag on mobile (especially `noindex` or `nofollow`) may stop crawling or indexing under mobile-first indexing.
- Don't lazy-load primary content on user interaction (swiping, clicking, typing); Google won't trigger it. Ensure lazy-loaded content is visible to Google.
- Don't block mobile resource URLs with `disallow`, especially where mobile resource URLs differ from desktop.

### Content parity
- Mobile must contain the same primary content as desktop; differing DOM or layout can change how Google understands content. Same content lets both versions rank for the same keywords.
- Mobile design may differ (accordions, tabs) provided content is equivalent. Intentionally having less on mobile means expecting traffic loss; prefer moving content into accordions or tabs over removing it.
- Use the same clear, meaningful headings.

### Structured data
- Same structured data on both versions. If prioritizing, start with `Breadcrumb`, `Product`, `VideoObject`.
- URLs in mobile structured data must be mobile URLs.
- If using Data Highlighter, train it on the mobile site and check its dashboard for extraction errors.

### Metadata
- `title` element and meta description equivalent on both.

### Ads
- Follow the Better Ads Standard; e.g. ads at the top can take up too much room on mobile.

### Images
- High-quality, not too small or low resolution.
- Supported formats and tags only (SVG is supported, but a `.jpg` in an `<image>` tag inside inline SVG can't be indexed).
- No image URLs that change on every page load.
- Same alt text as desktop.
- Same titles, captions, filenames and image-related text as desktop.
- Using different image URLs on mobile can cause temporary image-traffic loss while the new URLs build history; use the same image URLs on both to avoid it.

### Videos
- No URLs that change on every page load.
- Supported formats in supported tags (`<video>`, `<embed>`, `<object>`).
- Same video structured data on both.
- Place the video where it's easy to find on mobile (excess scrolling can hurt ranking).

### Extra practices for separate URLs (m-dot)
- Same error-page status on both versions (a normal desktop page with an error mobile counterpart drops from the index).
- No URL fragments on mobile URLs (generally not indexable; pages go missing).
- Different desktop pages need equivalent mobile pages; if distinct URLs redirect to one mobile URL (e.g. mobile home page), all of them drop from the index.
- Verify both versions in Search Console (data shift when mobile-first indexing starts).
- `hreflang`: link mobile to mobile and desktop to desktop. Example mobile (`https://m.example.com/`): `rel="canonical"` to desktop `https://example.com/`; `hreflang` alternates to `https://m.example.com/es/` and so on. Desktop: self canonical, `rel="alternate" media="only screen and (max-width: 640px)"` to the mobile URL, and `hreflang` alternates to desktop URLs.
- Mobile site needs capacity for a possible crawl-rate increase.
- robots.txt rules must work for both; usually keep them the same.
- Desktop URL is always canonical; mobile is the `alternate` (mobile page: `rel="canonical"` to desktop; desktop page: self canonical plus `rel="alternate"` with the `media` attribute).

### Troubleshooting (errors that block enablement or cause drops)
- Missing structured data (mobile lacks desktop's markup): same markup on both, correct mobile URLs, check Data Highlighter errors, check rendered content with URL Inspection.
- `noindex` tag on pages: use the same robots meta on both; no `noindex` on mobile.
- Missing image: same content as desktop; same robots meta (no `nofollow` on mobile); supported format and tag; no interaction-dependent lazy loading. Only content shown on mobile is used for indexing.
- Blocked image: robots.txt disallows an important image; allow crawling of mobile image URLs.
- Low quality image: too small or low resolution; provide high quality.
- Missing alt text: use the same alt text as desktop.
- Missing page title; missing meta description: make titles and descriptions equivalent.
- Mobile URL is an error page: same error status on both.
- Mobile URL has anchor fragment: Google can't index URLs with fragments; remove them.
- Mobile page blocked by robots.txt: verify robots.txt rules and robots meta work on both; use the same rules.
- Duplicate mobile page target: multiple desktop pages redirect to one mobile page; give each equivalent mobile versions.
- Desktop site redirects to the mobile home page: ensure an equivalent mobile page for each desktop page.
- Page quality issues (ads, missing content, titles, image descriptors): Better Ads Standard, same content and headings, same titles/captions/filenames/image text.
- Video issues (unsupported format, hard-to-find position, missing descriptions, slow load): supported tags and formats, no interaction-dependent lazy loading, prominent placement.
- Hostload issues: insufficient host capacity for mobile crawl; raise capacity.

## About AMP on Google Search
https://developers.google.com/search/docs/crawling-indexing/amp · Last updated: 2026-07-01

### Position
- Google indexes AMP pages like any page and applies the same standard regardless of technology.
- AMP pages can appear as rich results (structured data helps understanding; no guarantee) and as Web Stories.

### Guidelines
- All general Google-friendly practices apply.
- AMP page must follow the AMP HTML specification and be valid.
- Users must get the same content and actions as on the canonical page, where possible.
- AMP URL scheme must make sense to users: e.g. canonical `example.com/giraffes` → AMP at `amp.example.com/giraffes` or `example.com/amp/giraffes`, not `test.com/giraffes` (users see the AMP URL in the browser).
- Structured data must follow structured data policies.

### FAQs
- AMP pages aren't mobile-only; build them responsively.
- On desktop AMP displays well; standalone AMP can serve both mobile and desktop, but AMP on desktop gets no search-specific features in results.

## Enhance AMP content in Google Search
https://developers.google.com/search/docs/crawling-indexing/amp/enhance-amp · Last updated: 2026-07-01

### Create a basic AMP page
- For crawling and indexing, an AMP page must link to a canonical page, which may be a non-AMP version or the AMP page itself.
- Same content and actions as the canonical; same structured data on both; validate with the AMP Test Tool.
- robots.txt must not block the AMP page; use robots `meta`, `data-nosnippet`, `X-Robots-Tag` where appropriate.
- Follow `hreflang` guidance for language/regional URLs.

### Using a CMS
- Use a CMS plugin (WordPress, Drupal, Joomla) or custom code.
- Recommended URL schemes when generating AMP alongside a canonical page: `https://www.example.com/myarticle/amp` or `https://www.example.com/myarticle.amp.html`.
- Build a structured data template per content type (AMP Project metadata examples: recipes, articles, videos, reviews).

### Optimize for rich results
- Structured data lets AMP pages appear as rich results (e.g. Top stories carousel, host carousel); verify with the Rich Results Test and the AMP Test Tool.

### Monitor
- AMP status report: site-wide templating and implementation issues across many AMP pages.
- Rich result status reports: structured data problems and opportunities.
- To stop serving AMP, follow the removal guide.
- Codelabs and resources (AMP ad units, monetization, Tag Manager, built-in Google Analytics support) are listed.

## Validate your AMP content
https://developers.google.com/search/docs/crawling-indexing/amp/validate-amp · Last updated: 2026-07-01

### Validation tools
- AMP Test Tool (validity); Rich Results Test (structured data parse, for applicable content types); AMP status report (site-wide monitoring).

### If an AMP page doesn't appear in Search (indexing can take time)
- Make pages discoverable by links. Check `rel="amphtml"` on the canonical page; whether `rel="amphtml"` was wrongly added to other non-AMP pages (e.g. mobile); whether the AMP page has `rel="canonical"`.
- Follow the AMP guidelines for Search.
- Let Googlebot crawl: robots.txt must allow the canonical page, AMP page and links in structured data; remove all robots `meta` tags and `X-Robots-Tag` headers from canonical and AMP content.
- Structured data must follow guidelines for the feature type.
- Other reasons: some Search features unavailable in your country; site not indexed yet.
- Debugging resources: ampproject.org validation errors and fix guide.

## Remove your AMP pages from Google Search
https://developers.google.com/search/docs/crawling-indexing/amp/remove-amp · Last updated: 2026-07-01

### Setups
- Canonical AMP: one version, the AMP page is canonical. Canonical non-AMP: two versions (AMP page plus non-AMP canonical).
- Three removal options: remove all versions fast; remove only AMP while keeping the canonical non-AMP page; remove via CMS.

### Remove all versions (fastest; may show users an error)
- Delete AMP and non-AMP pages from the server or CMS.
- Request removal with the Remove outdated content tool for both URLs.
- Verify via Search; for many pages use the Search Console AMP status report and watch the "indexed AMP pages" graph trend down.
- Delay before Googlebot notices deletion; users see an error in the meantime.

### Remove only the AMP version (keep non-AMP canonical)
- Don't "remove" by emptying the file: empty/markup-less documents are invalid and Google keeps serving the oldest valid version.
- Remove the `rel="amphtml"` link from the canonical non-AMP page.
- Return `HTTP 301 Moved Permanently` or `302 Found` for the removed AMP URL, redirecting it to the canonical non-AMP page.
- To also remove it from non-Google platforms: return `HTTP 404 Not Found` for the AMP URL; verify via Search/AMP status report. To keep permalinks alive instead, send `HTTP 301` to the canonical non-AMP page.

> Note: the page lists a `301` or `302` redirect for Google removal but a `301` when keeping permalinks, and a `404` for non-Google removal; these target different goals.

### Remove with a CMS
- Unpublishing/deleting a page in the CMS normally removes both AMP and non-AMP versions (WordPress.com, Drupal, Squarespace help linked).
- Disabling AMP in the CMS removes all AMP pages site-wide; CMS-hosted domains may redirect users to non-AMP pages automatically, otherwise contact the CMS provider.
