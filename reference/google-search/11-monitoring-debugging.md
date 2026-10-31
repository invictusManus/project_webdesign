# Monitoring & debugging: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Get started with Search Console
https://developers.google.com/search/docs/monitor-debug/search-console-start · Last updated: 2025-12-10

### Purpose and cadence
- Free Google tool showing how Google crawls, indexes and serves a site; usable by anyone with a site.
- No daily sign-in needed: Google emails when it finds new issues on the site.
- Check about once a month, and after content changes, to confirm data is stable.

### Getting started steps
- Verify site ownership to unlock all data.
- Page indexing / Index coverage report: lists pages Google indexed or tried to index; fix errors and warnings.
- Sitemap submission is optional (pages are discovered anyway) but may speed discovery and enables Sitemaps report monitoring.
- Search performance report: traffic from Google Search by query, page, country; trends for impressions, clicks and other metrics. If traffic falls, debug the drop.

### Reports for SEO specialists, marketers, site admins
- Manual Actions report: shows manual actions, affected site sections and where to learn more; a manual action can hide some or all of the site from results.
- Removals tool: temporary hide from Search; a successful request lasts only about six months, giving time to fix or remove content permanently.
- Change of Address tool: use when moving to another domain or subdomain; helps migrate results to the new site.
- Rich result status reports: show structured data Google could or could not read, errors that block rich results, warnings, debugging info.

### Reports for web developers
- Index Coverage: site-wide errors, warnings, excluded pages; also impressions per page, to gauge organic impact.
- URL Inspection: page-level index status; test live URL, request crawling, view loaded resources and details.
- Security Issues report: warnings for suspected hacking or use that could harm visitors or devices.
- Core Web Vitals report: field (real-world usage) data on page performance.

## Debug drops in Search traffic
https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops · Last updated: 2025-12-10

### Overview
- Uses the Search Console Performance report plus Google Trends to find the cause of a drop.
- Graph shape hints at cause: large sudden drop = algorithmic update, site-wide security or spam issue; recurring shape = seasonality; site-wide step = technical issue or changing interests; also possible: reporting glitch.
- Check the Search Console Data Anomalies page first: drop may come from data processing or logging changes.

### Main causes
- **Algorithmic update**
  - Core and smaller updates change performance; check Google's ranking updates list for relevance.
  - Often nothing fundamentally wrong with content. Assess top pages in Search Console: small drop (e.g. position 2 to 4) vs large drop (e.g. 4 to 29).
  - Positions are not static; the web keeps changing, causing gains and drops.
  - Small drop: may show a noticeable traffic drop without a big impressions change; fluctuations occur anytime and may reverse unaided. Recommendation: avoid radical changes to a page that already performs well.
  - Large drop (out of top results for many terms, e.g. top 10 to 29): self-assess the whole site (not single pages) as helpful, reliable, people-first. Changes can take a few days to several months to take effect (e.g. months before systems conclude a site produces helpful content long term). Wait a few weeks before re-analyzing in Search Console. No guarantee that changes bring impact; more deserving content keeps ranking.
- **Technical issues**
  - Errors blocking crawl, index or serve: server availability, robots.txt fetching, "page not found", etc.
  - Can be site-wide (site down) or page-level (e.g. misplaced `noindex`, which depends on Google crawling the page so traffic falls more slowly).
  - Check Crawl stats report and Page indexing report for a matching spike in issues.
- **Security issues**: malware or phishing can trigger warnings or interstitials before users reach the site, lowering traffic. Check Security Issues report.
- **Spam issues**: automated detection plus human review (manual action). Non-compliance with spam policies can rank content lower or remove it. Review spam policies; check Manual Actions report.
- **Seasonality and changing interests**: demand shifts from trends or seasons. Filter Performance report to one top query at a time and compare on Google Trends to see whether the drop is site-specific or web-wide.
- **Site moves and migrations**: changing URLs causes ranking fluctuation during recrawl/reindex; medium sites take a few weeks to be noticed, larger sites longer. If no recovery, check the site move troubleshooting section for common migration mistakes.

### Analyze the drop pattern in the Performance report
- Impressions and clicks both dropped: work through the causes above.
- Impressions stable but clicks dropped: titles/snippets may not communicate the content well, or competitors have more appealing rich results.
- Date filter: set Last 16 months to rule out yearly recurrence (festivity, trend). To keep more than 16 months, use the Search Analytics API or bulk data export and store the data.
- Compare tab: last 3 months vs previous period, or year over year. Check all tabs (queries, URLs, countries, devices, search appearances) to see if the change is specific.
- Search type filter: separate Web, Images, Video, News to locate the drop.
- Average position metric: do not focus on absolute position; impressions and clicks are the measure of success. Dramatic persistent position drop: self-assess content for helpfulness and reliability.
- Pages table: find whether the drop is site-wide, a group of pages, or one key page. Compare periods and sort by Clicks Difference (largest losers first). Site-wide: check Page indexing report. Group of pages: use URL Inspection on a few.

### Investigate industry trends (Google Trends)
- Trends gives a largely unfiltered, anonymized, categorized, aggregated sample of real Google searches, from global down to city level.
- Two drivers: changing interests (what/how people search, new products for the same queries, brand shifts) and seasonality (e.g. diets in January, turkey in November, champagne in December; industries differ).
- Example: turkey strongly seasonal (November peak), chicken mildly seasonal, coffee stable.
- Extra checks: compare top queries in your region with queries bringing you traffic; if topics are missing, verify you have content that is crawled and indexed. Check queries related to important topics for rising related queries and add related content.

## Improve SEO with a bubble chart
https://developers.google.com/search/docs/monitor-debug/bubble-chart-analysis · Last updated: 2025-12-10

### Purpose
- Visualizes many long-tail queries to show which perform well and which could improve; built in Looker Studio on the Search Console data source.
- Data source: Site Impression table (performance data aggregated by site and query).

### Chart setup
- Controls: data control (property), date range (default last 28 days), query include/exclude, country, device.
- Axes: x = site CTR, y = average position.
  - Reverse the y-axis so position 1 is at top (best = top right).
  - Log scale on both axes to show extremes.
  - Reference lines (average, median or percentile) split the chart into quadrants.
- Bubbles: one per query; size = clicks; color = device category (any dimension possible but more values hide patterns).

### Quadrant interpretation (quadrants depend on your own distribution)
- Top position, high CTR: nothing needed.
- Low position, high CTR: relevant queries; improving rank has big impact. Check for an existing page: none, create one centralizing info; exists, add content addressing the need.
- Low position, low CTR: look at bubble size for low-CTR but high-traffic queries. Related queries: prioritize over queries not appearing at all (easier to optimize). Unrelated queries: refine content or focus on queries bringing relevant traffic.
- Top position, low CTR: check largest bubbles for causes:
  - Competitors with structured data/rich results attract clicks; optimize for common visual elements.
  - Accidental ranking for queries users do not link to the site (ignorable; if undesirable e.g. offensive, remove mentions that read as synonyms or related queries).
  - Users already got the answer (hours, address, phone). Fine if goal is store visits; otherwise sharpen titles/descriptions.
- Device split is an extra signal (e.g. location queries strong on mobile, weak on desktop).

### Optimizing specific queries
- Create a query filter in Search Console, or a pivot table in Looker Studio, to see all pages receiving traffic for a query.
- Apply SEO starter guide tips: descriptive, specific, accurate `title` elements, description meta tags and `alt` attributes; headings for hierarchy; consider synonyms and related queries (Google Ads Keyword Planner for variations and approximate volume; Google Trends for rising topics).

## Using Search Console and Google Analytics data for SEO
https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console · Last updated: 2026-01-07

### Roles of each tool
- Search Console: pre-visit data (impressions, clicks, queries, etc.).
- Google Analytics: on-site behavior (pages, time, actions) and acquisition channels (email, referrals, social, paid, organic).
- Source of truth for Search performance: Search Console. Source of truth for on-site behavior: Google Analytics.
- Comparison helps attribute conversions (transactions, signups, leads) to Google Search. Numbers never match fully; compare Search Console Clicks to Google Analytics Sessions (most comparable). Trend shape matters, not totals.

### Looker Studio dashboard (template provided)
- Setup: open template, "Use my own data", connect Search Console (choose URL Impression table) and Google Analytics, then reconnect each chart.
- Colors: orange = Google Analytics, blue = Search Console.
- GA data pre-filtered to `Session source = google` and `Session medium = organic`.
- Per-query blending is best done in BigQuery (Search Console bulk export + GA BigQuery export); Looker Studio blending also possible via country, device, landing page dimensions.
- Controls: property selection, country and device (use the same filters on both sources), date range (default 28 days; Search Console data can lag a couple of days).
- Five metrics: Sessions (GA); Engagement rate (GA; engaged session = key event, or over 10 seconds, or 2+ page views); Returning users (GA); Clicks (SC); CTR (SC = clicks / impressions).
- Charts and reading:
  - Organic sessions + engagement rate over time: big traffic change, go to Search Console and follow the traffic-drop guide. Engagement drop, make content more closely related to the queries that bring users.
  - Share of organic traffic over time: no good or bad value; if it shifts while sessions/engagement did not, check GA Traffic acquisition report for other channels changing.
  - Clicks and CTR over time: volume and snippet persuasiveness; on pattern change, check which queries and pages dropped or spiked.
  - Top pages and queries by clicks and CTR, with change versus previous period; top countries tables (filter by country in GA or SC for multi-country sites).
- Dashboard is for spotting changes quickly, not for debugging.

### Deeper investigation
- GA: Traffic acquisition report (channel "Organic Search", source "Google"; actions and purchases); Landing page report filtered to google organic sessions (engagement and conversions per page).
- SC: Performance reports for fluctuations.

### Data discrepancies
- Small discrepancy: ignore, expected. Big discrepancy: check reasons (more than one may apply; some cannot be debugged).
- GA implementation: tag may be missing on pages; depends on configuration. Search Console processes all properties uniformly.
- Cookies/tracking: users opting out of tracking skew GA data (consent management).
- Timezone: GA configurable; Search Console fixed to Pacific Time (PT). Big offset (e.g. Australia) makes this visible.
- Attribution: GA has three attribution models; Search Console counts every Search click. Closest is GA's default model.
- Canonical URLs: Search Console reports only the Google Search canonical URL; GA reports any URL with the tag, so more URLs.
- Traffic breakdowns: Search Console splits web, image, video, news, Discover; GA categories differ.
- Non-HTML pages (e.g. PDFs): Search Console includes them if shown or clicked; GA may not measure them (turn on enhanced measurement events).
- Bot traffic: GA excludes known bots and spiders; Search Console does not necessarily filter them.

### Other resources
- Link Search Console to Google Analytics (exposes some SC reports in GA).
- Site Kit plugin for WordPress (both datasets in one dashboard).
- Recommended for most detail and fewest discrepancies: Search Console bulk data export plus GA BigQuery export, merged.

## Analyze social and video platform content
https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content · Last updated: 2026-07-29

### Platform properties
- Content from TikTok, Instagram, X and YouTube can appear in Google Search (e.g. short video carousel, latest posts carousel, "what people are saying" carousel).
- Add and verify each account separately as a platform property in Search Console. If the Search profile is already claimed, verified accounts are added automatically as properties.

### Reports
- Insights report: traffic trends (clicks over last 28 days across Search parts), top-performing content, search queries bringing people to channel/profile/posts/videos, audience countries.
- Performance reports: filter by country, dates, search terms; answers e.g. country success, mobile vs desktop, expected or surprising queries.
- Insights card of query groups: top, trending up, trending down themes, for planning content.

### Analyses
- 24-hour filter in Performance report: spot a term suddenly driving traffic to a new post; use for cross-promotion. Also monitor Google Trends.
- Page filter on a keyword, e.g. `playlist` for YouTube playlists; compare CTR and average position scorecards. Shows the playlist page, not its videos.
- Format comparison via comparison mode with URL contains: YouTube `/watch` vs `/shorts/`; Instagram `/p/` vs `/reels/`.
- Cross-platform comparison: open each platform property, click the URL to analyze (filters the report), Export, repeat per property; compare countries, devices, top queries; adjust strategy (e.g. repackage long-form content, more vertical short video if audience is mobile).
- Content strategy: watch for sudden spikes on older content; extend lifecycle (pin, cross-promote, sequel); after rewriting a title or caption add a Search Console annotation (bookmark on a date) and compare performance afterwards.

## Search operators overview
https://developers.google.com/search/docs/monitor-debug/search-operators · Last updated: 2025-12-10

- Operators help debug a site (e.g. `site:` for comment spam, `imagesize:` for small images).
- Bound by indexing and retrieval limits; URL Inspection tool is more reliable for debugging.
- `filetype:` results of a type per `content-type` HTTP header or file extension, e.g. `filetype:rtf galway`.
- `imagesize:` pages with images of given dimensions; Google Images only.
- `site:` results from a domain, URL or URL prefix.
- `src:` pages referencing an image URL in `src` attribute; Google Images only.

## `site:` search operator
https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site · Last updated: 2025-12-10

- Syntax: `site:example.com` returns results from the domain and its subdomains (e.g. `www.`, `recipes.`); `site:https://www.example.com/ramen tsukemen` returns URLs with that prefix relevant to the term.
- Available on all Google Search properties.
- Indexed URL may show for related `site:` queries but not guaranteed. If missing, use URL Inspection to check indexability and submit for indexing. Check query precision: `site:https://www.example.com` differs from `site:https://example.com/`.
- Uses: list indexed and serving URLs (not exhaustive; large sites will not see all; a more specific prefix may yield more); check one URL's index status; find spam with e.g. `site:example.com viagra casino`; see URLs matching a term; check a URL for a term.
- Limitations: does not necessarily return all URLs under the prefix, so unsuitable for counting indexed URLs. Without a query it does not rank results: shortest URL generally first, otherwise relatively random.

## Google Images search operators
https://developers.google.com/search/docs/monitor-debug/search-operators/image-search · Last updated: 2025-12-10

- `src:` and `imagesize:` work only on Google Images; no effect elsewhere.
- `src:https://example.com/media/carrot.jpg` returns pages from any domain that reference that image URL in `src`; useful to find hotlinking by other sites.
- `imagesize:WIDTHxHEIGHT` (width `x` height format required), e.g. `imagesize:1500x1000`.
- Combine: `src:… imagesize:500x1200`; `site:https://example.com/ imagesize:500x1200` for exact-size images indexed on your site.
- Limitation: indexing and retrieval limits mean not all results appear.

## Preventing and monitoring abuse on your site (overview)
https://developers.google.com/search/docs/monitor-debug/security · Last updated: 2025-12-10

- Hub page listing: user-generated spam prevention, malware and unwanted software, preventing malware infection, social engineering (phishing and deceptive sites), Safe Browsing Repeat Offenders Policy.

## Prevent user-generated spam on your site and platform
https://developers.google.com/search/docs/monitor-debug/prevent-abuse · Last updated: 2026-10-26

### Context
- Spammers exploit open comment forms and other user-generated content inputs. Platforms letting users publish shared pages, generated content or web apps can be abused to create many policy-violating, low-value pages or sites.
- Prevention is usually not hard; even a simple unusual challenge can deter.

### Measures
- Publish an abuse policy and communicate it (e.g. at sign-up); let trusted users report spammy content.
- Identify spammy accounts: log signups and interactions; look at form completion time, requests per IP range, user agents at signup, chosen user names/form values. Build a user reputation system.
- Add robots `meta` `noindex` to posts from new users without reputation; allow indexing after reputation is earned (demotivates spammers).
- Add `rel="nofollow"` or `rel="ugc"` to all links in untrusted content.
- Index only content meant for Search: for user-created shareable pages, generated output or interactive tools meant for direct sharing, collaboration or utility, apply `noindex` (robots `meta` or `X-Robots-Tag` header) or block crawling in `robots.txt` by default.
- Manual approval (moderation) for suspicious interactions: effective, adds overhead; built into most CMSes for comments.
- Blocklist: once one spam profile is found, remove others easily; ban repeat IP addresses permanently (firewall deny list or plugins like Akismet).
- Block automated account creation: reCAPTCHA or similar verification on sign-up forms.

### Monitoring
- Verify the site or subdomain in Search Console for email alerts on manual actions and security issues; regularly check Page Indexing and Search performance reports for unexpected spikes in indexed pages, impressions or off-purpose queries.
- Track platform-level creation and indexing metrics; alert on spikes in new public pages or few users producing a large share of indexable URLs.
- Watch for spam signals: redirects, many ad sections, spammy keywords, large encoded JavaScript blocks; `site:` operator or Google Alerts can help.
- Watch webserver logs for sudden traffic spikes.
- Test URLs for phishing and malware regularly, e.g. with the Google Safe Browsing API.
- Confidence checks, e.g. thousands of interactions from an unexpected country overnight; language detection libraries or Google Translate API v2 can detect language of new sites.

## Malware and unwanted software
https://developers.google.com/search/docs/monitor-debug/security/malware · Last updated: 2025-12-10

### Definitions
- Malware: software or mobile app designed to harm a device, its software or users (e.g. installing software without consent, viruses). Owners may host such binaries unknowingly.
- Unwanted software: executable or mobile app with deceptive, unexpected behavior or that harms browsing/computing experience (e.g. changes home page or browser settings, leaks private data without disclosure).
- Security Issues report: "Malware" = web-based malware running without explicit user action; "Harmful downloads" = malware/unwanted software the user must explicitly download. Lists suspected files on the site.

### Fixing
- Make the site/app follow the guidelines, then request a review in the Security Issues report. Mobile apps showing warnings: file an appeal.
- Persistent or unfixable issues: Search Console users can use "Report a security issue".

### Guidelines (not exhaustive; violations cause warnings on download and visit)
- **Don't misrepresent yourself**
  - Inform users accurately of purpose; download must be intentional via an accurate ad. Deceptive: ad with only "Download" or "Play" without naming the software, a "Play" button leading to a download, an ad mimicking the publisher site and offering content (e.g. a movie) but leading to unrelated software.
  - Behave as advertised; describe data collection or ad injection in clear language, not as minor features.
  - Clearly explain browser/system changes; users review and approve significant options; main UI discloses bundled components and offers an easy skip; hidden options or barely visible text is not disclosure.
  - Use endorsements only when authorized; no unauthorized third-party or government logos.
  - Don't scare users: no false claims of critical security state or infection; no false service claims (e.g. "speed up your PC"); "free" cleaners must not be advertised as free unless services need no payment.
- **Software guidelines**
  - Use the Chrome Settings Override API (via a Chrome extension with compliant install flow) to change default search, startup page or new tab page.
  - Do not suppress browser or OS dialogues alerting users to changes.
  - Code signing recommended (valid, verified signature with verifiable publisher info); unsigned alone is not a reason to flag.
  - Don't degrade TLS/SSL: no installing root CA certificates; no intercepting TLS connections unless the tool is for expert debugging.
  - Protect user data: only transmit private data as needed for functionality, disclosed and encrypted.
  - Do no harm: don't break the browser reset function; don't bypass settings UI controls; use an extension (not DLL ad injection, intercepting proxies, Layered Service Provider, or patching the Chrome binary); no scary or false descriptions (registry cleaners); easy, findable, non-threatening uninstall that removes all components and restores settings.
  - Bundled components: the bundler is responsible for all of them.
- **Chrome extension guidelines**
  - Extensions must be disclosed, hosted in the Chrome Web Store, disabled by default, compliant with Web Store policies (including single-purpose); installed via the authorized flow; must not suppress Chrome alerts.
  - Uninstall flow must tell users how to disable and delete the extension.
  - Binaries that install an extension in violation of the Chrome Alternative Extension Distribution Options policy are identified as malware.
- **Mobile application guidelines**
  - Inform users and get agreement before collecting data (third-party accounts, email, phone number, installed apps, files); transmit with modern cryptography (HTTPS); non-Play apps disclose in-app, Play apps follow Play policy; don't collect beyond published use.
  - Don't impersonate another brand or app.
  - Keep all content within app context; no ads or content outside the app without informed consent and clear attribution.
  - Deliver advertised functionality; don't download additional apps without informed consent.
  - Transparent behavior: don't uninstall or replace other apps or shortcuts (unless that is the stated purpose); clear, complete uninstall; don't mimic OS or other-app prompts.
  - Google Play apps must also follow Developer Program Policies and Developer Distribution Agreement.

## Prevent a malware infection
https://developers.google.com/search/docs/monitor-debug/security/prevent-malware · Last updated: 2025-12-10

### Monitoring site health
- Periodically run `site:` on your domain to spot unexpected pages or topics you did not write (sign of hacking).
- Security Issues report: lists hacked pages Google identified, with fix instructions.
- Malware detection shows in the Search Console message panel; forward messages to email for speed.

### Security checklist, all website owners
- Choose good passwords (Google account guidelines).
- Choose third-party content providers carefully: third-party apps and ads must come from trusted, legitimate sources that publish support and contact information.
- Contact hosting company or publishing platform for support; follow their security page or RSS feed.
- Keep workstations safe: current software, virus/trojan-free, updated anti-virus.

### Security checklist, owners with server access
- Check server configuration (Apache and IIS security guidance: directory permissions, server-side includes, authentication, encryption).
- Keep a backup of `.htaccess` (or equivalent access control) for recovery; delete the backup when finished.
- Keep all software and plug-ins patched; keep a list with versions; forgotten forums and blogs are a common pitfall; host OS patches also matter (even banks, sports teams, government sites have been warned).
- Watch log files: unfamiliar URL parameters (like `=http:` or `=//`) or spikes to redirect URLs may signal open-redirect exploitation. Hackers often alter logs, so protect them (e.g. move from default location).
- Check for common vulnerabilities: no directories with open permissions; test for XSS and SQL injection.
- Use SSH and SFTP rather than plain-text telnet or FTP.
- Follow security news (Google Security Blog, US-CERT).
- Persistent or unfixable issues: "Report a security issue" in Search Console.

## Social engineering (phishing and deceptive sites)
https://developers.google.com/search/docs/monitor-debug/security/social-engineering · Last updated: 2025-12-10

### Definition and effect
- Content that tricks visitors into dangerous actions (revealing confidential info, downloading software). If detected, Chrome may show a "Deceptive site ahead" warning. Check pages in the Security Issues report (reported as "deceptive content").
- Types:
  - Phishing: tricks users into revealing personal information (passwords, phone numbers, SSNs) by posing as, or looking like, a trusted entity (browser, OS, bank, government).
  - Deceptive content: tricks users into things they would do only for a trusted entity (share a password, call tech support, download software), including ads falsely claiming device software is out of date.
  - Insufficiently labeled third-party services: a third party operating a site on behalf of a first party without making the relationship clear (e.g. a donation platform handling collections for a charity site must identify itself as a third-party platform acting for that charity).
- Safe Browsing warns users before they visit pages that consistently engage in social engineering. A page counts if it pretends to be a trusted entity (device, browser, the site itself) or tricks users into trusted-entity actions.
- Embedded content (usually ads) with social engineering is a policy violation for the host page, whether visible ads or pop-ups, pop-unders or redirects.
- Sites can be flagged without intent: embedded images, third-party components or ads; hackers can take over sites to host or distribute such content (e.g. to collect card numbers). See Help for Hacked Sites if hacked.
- Examples: install-malware pop-up, fake browser update pop-up, fake Google login page (check URL and `https://`), fake software-update ads, ads posing as installers or page buttons.

### Fixing
- Ensure the pages engage in none of these practices, then:
  - Check Search Console: verify ownership and that no new, suspicious owners were added.
  - Check the Security Issues report; visit sample flagged URLs from a computer outside the network serving the site (hackers may hide attacks from site-owner networks).
  - No sample URLs and confident the site is clean: request a security review.
  - Remove deceptive content; report a false classification to Safe Browsing.
  - Check third-party resources (ads, images, embeds): ad networks rotate ads so refresh several times; ads differ on mobile and desktop (URL Inspection shows both views); follow third-party service guidelines for services such as payments.
  - Request a review in the Security Issues report after cleanup; a review can take several days.
- Persistent or unfixable issues: "Report a security issue".

### Third-party service guidelines
- Every page clearly shows the third-party brand (e.g. top of page) so users know who operates the site.
- Every page with first-party branding states the first/third-party relationship with a link for more info, e.g. "hosted by [third party] on behalf of [first party]".
- Usability test: a user seeing the page alone should understand which site they are on and the relationship.
- Best practice: for basic support services, use an industry-standard third party (e.g. OAuth for authentication rather than self-managed).

## Google Safe Browsing Repeat Offenders Policy
https://developers.google.com/search/docs/monitor-debug/security/safe-browsing-repeat-offenders · Last updated: 2025-12-10

- Safe Browsing warns users on dangerous sites or download files and notifies owners of compromised sites.
- Sites that repeatedly switch between compliant and noncompliant behavior in a short window are classified Repeat Offenders.
- Owner is emailed at the registered Search Console email address.
- While designated, the owner cannot request further reviews in Search Console.
- Status lasts 30 days, after which reviews can be requested again.

## Get started with Google Trends
https://developers.google.com/search/docs/monitor-debug/trends-start · Last updated: 2025-12-10

### About
- Trends provides a random sample of aggregated, anonymized, categorized Google and YouTube searches; analysis worldwide or at city level.
- Use trends to inform strategy; do not write about something merely because it trends; topic must fit the business and users (see helpful, reliable, people-first content).
- Tools: Explore (custom terms/topics, regional interest, related topics over time); Trending now (what is trending, approximate search volume, timeline, related news).

### Monitoring rising trends
- Use Trending now for recent trends; Explore for rising/top terms by location, date range, category and property.
- Evaluate relevance to your industry and audience and whether you can add value; review existing content first.
- General trends: Explore with empty search box shows top trending terms/topics (filters: country, date, category, property); Trending now with filters and related news/terms for context.
- Specific trends: list your own terms and search them in Explore (e.g. cheese types for a cheese store). Topics aggregate across languages and include misspellings, variations and acronyms. Example takeaways: one term rising, one highly seasonal, one sustained, one negligible; use for product availability, inventory and content planning.

### Keyword research
- Keyword research = identifying words and phrases the audience uses. Trends shows which of your terms are rising, possibly less known and less competitive. If unsure where to start, use the Search Console Performance report Queries tab.
- Steps: Explore, add up to 5 terms and read the timeline; for multi-country targeting a card shows where terms are most popular; check related topics and related queries (Top for most interest, Rising for recent attention) and pick only terms tied to the business and your expertise; look for related terms in other languages (to decide on translation; verify with Performance reports for those languages/countries).
- Then optimize using SEO best practices for terms matching your audience, site and first-hand experience.

### Content calendar
- Find seasonal trends and publish high-quality content a little before demand peaks.
- Analyze markets separately: trends differ by country (example: Brie spikes twice a year in the US, once in the UK, so UK content should publish before Christmas).

### Benchmarking against industry
- Determine whether a traffic change for a term follows an industry-wide change or is site-specific (see the traffic-drop page).
- Use a category filter to focus on a vertical (e.g. travel insurance).
- Add competitor names to see related topics/terms and, for multi-region operators, searches by subregion, metro, city.

### Brand awareness and sentiment
- Enter the brand name in Explore, set the range to the past 30 or 90 days, review both "Rising" and "Top" related terms (paginate with arrows).
- Use findings to address audience concerns (e.g. clarify an incident, explain coupons).
- Download data monthly, weekly or daily to track sentiment shifts and correlate with other data (other engines, social networks); at larger volumes consider an advanced tool such as Natural Language AI.
