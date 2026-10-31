# Search Essentials & SEO fundamentals: Google Search documentation notes

Source: Google Search Central documentation (developers.google.com), retrieved 2026-10-31. © Google, licensed under CC BY 4.0. Summarized and restructured; not an official Google document.

## Google Search Essentials (overview)
https://developers.google.com/search/docs/essentials · Last updated: 2025-12-10

### Three parts of the Essentials
- Technical requirements: what a page needs to be eligible to show in Google Search.
- Spam policies: behaviors and tactics that can lead to lower ranking or complete omission from results.
- Key best practices: the main things that improve how a site appears.
- "Web-based content" = web pages, images, videos or other public material Google finds on the web.
- Appearing in Google Search costs nothing, whatever anyone claims.
- Meeting every requirement and best practice does not guarantee crawling, indexing or serving.
- Very few technical things need doing; most sites pass without noticing. Sites that focus on the best content and experience and uphold the spirit of the principles are more likely to do well.

### Key best practices (list on the page)
- Create helpful, reliable, people-first content.
- Use the words people would search for, in prominent spots: title, main heading, and descriptive locations such as alt text and link text.
- Make links crawlable so Google can find other pages through them.
- Tell people about the site; be active in communities relevant to what the site offers.
- Follow the specific best practices for other content types: images, videos, structured data, JavaScript.
- Enable search features (rich results etc.) that make sense for the site.
- Use the appropriate method to control appearance, or to opt out of Search, for content that should not be found.

## Google Search technical requirements
https://developers.google.com/search/docs/essentials/technical · Last updated: 2025-12-18

### The three requirements
- Googlebot is not blocked.
- The page works: Google receives HTTP `200 (success)`.
- The page has indexable content.
- Meeting them makes a page eligible for indexing only; indexing is not guaranteed.

### Googlebot isn't blocked
- Google indexes only publicly accessible pages that don't block Googlebot. A page behind a login is not crawled.
- Any of several mechanisms that block indexing keeps a page out of the index.
- Pages blocked by robots.txt are unlikely to show in results.
- To list inaccessible pages you want indexed: use both the Page Indexing report and the Crawl Stats report in Search Console (each shows different information about URLs).
- To test one page: URL Inspection tool.

### The page works
- Only pages served with HTTP `200` are indexed. Client and server error pages are not indexed.
- Check the status code with URL Inspection.

### The page has indexable content
- Textual content must be in a file type Google Search supports.
- Content must not violate the spam policies.
- robots.txt blocking prevents crawling, but the URL may still appear in results. To keep a page out of the index, use `noindex` and allow Google to crawl the URL.

## Spam policies for Google web search
https://developers.google.com/search/docs/essentials/spam-policies · Last updated: 2026-08-28

### Scope and enforcement
- Spam = techniques that deceive users or manipulate Search systems into featuring content prominently, including attempts to manipulate generative AI responses in Google Search.
- To be eligible for web search results, content (pages, images, videos, news content, other material) must not violate the overall Search policies or these spam policies.
- Applies to all web search results, including Google's own properties.
- Detection: automated systems plus, as needed, human review that can result in a manual action. Violators may rank lower or not appear at all.
- Reporting a spam site: search quality user report. Reports feed scalable, automated improvements rather than individual removals.
- The list covers common practices only; Google may act against any spam practice.

### Cloaking
- Definition: presenting different content to users and search engines with intent to manipulate rankings and mislead users.
- Examples: showing a travel-destinations page to search engines but a discount-drugs page to users; inserting text or keywords only when the requesting user agent is a search engine.
- Sites whose JavaScript or images are hard for search engines to access should use Google's accessibility recommendations, not cloaking.
- Hacked sites often get cloaking injected to hide the hack from the owner.
- Paywall or content gating is not cloaking if Google sees the full content behind the wall just like a person with access and the site follows Flexible Sampling guidance.

### Doorway abuse
- Definition: sites or pages created to rank for specific, similar queries, leading users to intermediate pages less useful than the final destination.
- Examples: multiple sites with slight URL/home-page variations to maximize reach for a query; multiple domains or pages aimed at specific regions or cities that funnel users to one page; pages generated to funnel visitors into the usable part of a site; substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy.

### Expired domain abuse
- Definition: buying an expired domain and repurposing it primarily to manipulate rankings by hosting content of little to no user value.
- Examples: affiliate content on a former government agency site; commercial medical products on a former non-profit medical charity site; casino content on a former elementary school site.

### Hacked content
- Definition: content placed on a site without permission through security vulnerabilities. Gives poor results and can install malicious content on user machines.
- Code injection: malicious code (often JavaScript, directly or in iframes) injected into existing pages.
- Page injection: new spammy or malicious pages added (manipulating search or phishing); existing pages may look clean while the new ones harm visitors and search performance.
- Content injection: subtle changes visible to search engines but hard for owner/users to spot: hidden links or hidden text via CSS/HTML, or cloaking.
- Redirects: injected code redirects some users to harmful or spammy pages, sometimes depending on referrer, user agent or device (for example, a redirect only when arriving from a Google result, none on direct visits).
- Google points to its guides on fixing hacked sites and avoiding being hacked.

### Hidden text and link abuse
- Definition: placing content on a page solely to manipulate search engines and not to be easily viewable by humans.
- Examples: white text on white background; text hidden behind an image; CSS positioning text off-screen; font size or opacity set to 0; hiding a link by linking a single small character (such as a hyphen mid-paragraph).
- Not violations (legitimate show/hide design): accordion or tabbed content; slideshow or slider cycling images or text; tooltips and similar text shown on interaction; text only for screen readers that improves their experience.

### Keyword stuffing
- Definition: filling a page with keywords or numbers to manipulate rankings; often unnatural lists or groups, or out of context.
- Examples: lists of phone numbers without substantial added value; blocks of text listing cities and regions the page tries to rank for; repeating words or phrases so often it sounds unnatural (the sample is a repetitive "unlimited app store credit" paragraph).

### Link spam
- Definition: creating links to or from a site primarily to manipulate rankings.
- Buying or selling links for ranking: money for links or for posts containing links; goods or services for links; sending someone a product in exchange for a written piece that includes a link.
- Excessive link exchanges ("link to me and I'll link to you") or partner pages solely for cross-linking.
- Using automated programs or services to create links to your site.
- Requiring a link in a Terms of Service, contract or similar arrangement without letting the third-party content owner qualify the outbound link.
- Text ads or text links that don't block ranking credit.
- Advertorials or native advertising where payment is received for articles with links that pass ranking credit, or links with optimized anchor text in articles, guest posts or press releases distributed on other sites.
- Low-quality directory or bookmark site links.
- Keyword-rich, hidden or low-quality links embedded in widgets distributed across sites.
- Widely distributed links in footers or templates of various sites.
- Forum comments with optimized links in the post or signature (example: signature "paul's pizza san diego pizza best pizza san diego").
- Low-value content created primarily to manipulate linking and ranking signals.
- Exception: buying and selling links for advertising or sponsorship is normal and not a violation if the links are qualified with `rel="nofollow"` or `rel="sponsored"` on the `<a>` tag.

### Machine-generated traffic
- Also called automated traffic: sending automated queries to Google, including scraping results for rank checking or other automated access to Google Search without express permission.
- Consumes resources and interferes with serving users; violates both the spam policies and the Google Terms of Service.

### Malicious practices
- Definition: practices that create a mismatch between user expectations and the actual outcome, causing a deceptive experience or compromised security or privacy.
- Malware: software or mobile apps designed to harm a computer, device, its software or users; includes installing software without consent and harmful software such as viruses. Owners may host such binaries inadvertently (downloadable files).
- Unwanted software: executables or mobile apps that are deceptive, unexpected or hurt the browsing or computing experience; examples: switching home page or other browser settings, apps leaking private data without disclosure. Owners must comply with the Unwanted Software Policy.
- Back button hijacking: interfering with browser navigation (manipulating history or other functionality) so users cannot use the back button to return immediately to the page they came from.

### Misleading functionality
- Definition: intentionally building sites that trick users into thinking they can access content or services they cannot.
- Examples: a fake generator claiming to provide app store credit that doesn't; a site claiming functionality (PDF merge, countdown timer, online dictionary) but leading users to deceptive ads instead.

### Scaled content abuse
- Definition: many pages generated primarily to manipulate rankings rather than help users; typically large amounts of unoriginal content with little to no value, regardless of how it is created.
- Examples: using generative AI or similar tools to generate many pages without adding user value; scraping feeds, search results or other content to generate many pages, including via automated transformations (synonymizing, translating, obfuscation), with little value; stitching or combining content from different pages without added value; creating multiple sites to hide the scaled nature of the content; many pages whose content makes little or no sense to a reader but contains search keywords.
- If such content is hosted on your site, exclude it from Search.

### Scraping
- Definition: taking content from other sites, often automatically, and hosting it to manipulate rankings.
- Examples: republishing others' content without original content or value or even citing the source; copying and only slightly modifying (synonym substitution, automated techniques) then republishing; reproducing feeds from other sites with no unique user benefit; sites dedicated to embedding or compiling videos, images or other media from other sites without substantial added value.

### Site reputation policy
- Applies where third-party content is published on a host site mainly because of the host's already-established ranking signals (earned mainly from first-party content), so the content ranks better than it could alone.
- Third-party content = created by an entity separate from the host: site users, freelancers, white-label services, people not employed directly by the host. Third-party content alone is not a violation; the problem is publishing it mainly to exploit the host's signals.
- Inconsistent examples: an educational site hosting a page of sponsored payday-loan reviews written by a third party who distributes the same page to other sites; a medical site hosting a low-quality, non-integrated third-party "best casinos" ad page placed to rank on the site's signals.
- Not inconsistent: wire or press-release service sites; news publications syndicating content from other news publications; sites built for user-generated content (forums, comment sections); columns, opinion pieces and other editorial work; advertorial or native-advertising pages whose purpose is to share content directly with readers (such as promotion within the publication) rather than to manipulate ranking; affiliate links used throughout a page with links treated appropriately, or embedded third-party ad units. Lists are non-exhaustive.
- Default presumption: individual pages (including new ones) match the overall quality of other pages on the domain. If a portion looks out of line, the site goes to human review.
- Consequences by region:
  - (region: outside EEA) relevant pages may get a manual action when shown to users outside the EEA.
  - (region: EEA) relevant pages may be categorized as separate from the main domain and rank independently on their own merits, with no manual-action impact.
- Notification: Manual actions report and Search Console message center. Sites can address the issue or appeal via reconsideration request; eligible EEA sites can also bring disputes to mediation.
- Review goal: whether the content has sufficient input, editorial oversight or contribution from the host to be fully integrated with the main site. Applies globally, using objective factors on how much control the host exercises. Factors, none necessary or sufficient alone: presentation (design, formatting, typography, UX consistent with host); quality (issues absent from the main domain); stated or implied authorship (explicit ownership or responsibility, or indications contesting it); whether identical or near-identical content appears on multiple other sites. Other evidence (such as third-party ranking-manipulation marketing material) may count.
- Worked examples:
  - Unlikely action: integrated coupons/deals section run with a specialist provider. Lesson: clear commercial disclosure, publisher named as editorially responsible, curated and cross-referenced in editorial content, reachable from main navigation, with an accessible reporting link.
  - Likely action (outside EEA): unauthored CBD-oil affiliate article on a business publication. Lesson: no author or responsible editor, no commercial disclaimers, no links from site sections, presentation and quality mismatch, content copied from a third-party marketplace.
  - Unlikely action: authored, original affiliate cooking content from a freelancer (celebrity chef interviews, affiliate links). Lesson: consistent branding, editorial-responsibility statements, named author and content specific to the host, even though the freelancer also works elsewhere and affiliate links may repeat.
- FAQ:
  - Manual action outside the EEA does not affect ranking in the EEA and is not used as an EEA ranking signal. No `noindex` obligation for content under non-EEA action; not applying it is not counted as circumvention or repeat violation, or in EEA ranking.
  - Previous EEA manual actions under this policy are lifted for EEA results; pages are no longer demoted. They may be categorized as separate and ranked on their own merits, but not automatically. Prior action is not used as a ranking signal.
  - "Separate from main domain" categorization means the presumption that pages match domain quality no longer applies. The section doesn't immediately lose main-site signals; ranking systems learn over time to rank parts independently. The categorization itself is not a ranking signal.
  - Disagreement: EEA sites have a new reconsideration process with commitment to answer within a short timeframe and with more detailed reasoning; alternative dispute resolution is available in the EEA.

### Sneaky redirects
- Definition: maliciously sending a visitor to a different URL than requested, either to show users and search engines different content or to show users unexpected content that doesn't meet their needs.
- Examples: showing search engines one kind of content while redirecting users to something significantly different; showing desktop users a normal page while redirecting mobile users to a spam domain.
- Legitimate redirects: moving a site to a new address; consolidating several pages into one; sending logged-in users to an internal page.
- Test: is the redirect intended to deceive users or search engines?

### Thin affiliation
- Definition: publishing pages with product affiliate links where descriptions and reviews are copied from the merchant with no original content or added value.
- Thin if part of a program distributing the same content across an affiliate network without added value; often cookie-cutter sites or templates replicating the same or similar content within a site or across domains or languages.
- Not every affiliate is thin. Good affiliate pages add price information, original product reviews, rigorous testing and ratings, navigation of products or categories, and product comparisons.

### User-generated spam
- Definition: spammy content added by users through a channel intended for user content; owners are often unaware.
- Examples: spammy accounts on hosting services anyone can register for; spammy forum posts; blog comment spam; spammy files uploaded to file hosting platforms.
- Google points to tips for preventing abuse of public areas and for fixing hacked sites.

### Other practices that can lead to demotion or removal
- Legal removals: a significant volume of valid copyright removal requests against a site can demote other content from it. Similar demotion signals apply to complaints about defamation, counterfeit goods and court-ordered removals. CSAM is always removed when identified, and all content from sites with a significant proportion of CSAM is demoted.
- Personal information removals: a significant volume of removals against a site with exploitative removal practices demotes its other content; the pattern is checked on other sites too. Similar demotions may apply to sites with many removals involving doxxing, explicit personal imagery created or shared without consent, or explicit non-consensual fake content.
- Policy circumvention: continuing to bypass spam or content policies can lead to restricted or removed eligibility for search features (for example Top Stories, Discover) and broader action (such as removing more site sections). Circumvention includes using existing or new subdomains, subdirectories or sites to keep violating, or other methods to continue distributing violating content or behavior.
- Scam and fraud: impersonating an official business or service via imposter sites, intentionally showing false business information, or attracting users on false pretenses. Automated systems try to keep such pages out of results. Examples: impersonating a well-known business or provider to trick users into paying the wrong party; deceptive sites posing as official customer support for a legitimate business, or giving fake contact information for it.

## How Google Search works
https://developers.google.com/search/docs/fundamentals/how-search-works · Last updated: 2025-12-18

### Ground rules
- Fully automated search engine; crawlers explore the web regularly. Most listed pages are found automatically, not submitted.
- Google does not accept payment to crawl more often or rank higher; ranking is programmatic.
- Google doesn't guarantee crawling, indexing or serving, even for pages following the Essentials.

### Three stages (not every page passes each)
- Crawling: downloading text, images, video from discovered pages.
- Indexing: analyzing and storing that information in the Google index.
- Serving: returning results relevant to the user's query.

### Crawling
- No central registry of pages; Google continuously performs URL discovery: known pages, links extracted from known pages (for example a category page linking to a new post), and submitted sitemaps.
- Googlebot (also crawler, robot, bot, spider) uses an algorithmic process to decide which sites to crawl, how often, and how many pages. It avoids crawling too fast, adapting to site responses (HTTP 500 errors mean slow down).
- Not every discovered page is crawled: some are disallowed, others require login.
- Google renders pages and runs JavaScript using a recent Chrome, because sites rely on JavaScript for content.
- Common access problems: server problems, network issues, robots.txt rules blocking Googlebot.

### Indexing
- Processes textual content and key tags/attributes such as `<title>` elements and alt attributes, images, videos.
- Canonicalization: clusters pages with similar content, picks the most representative as canonical (the one that may be shown); others are alternates that may serve in other contexts (for example mobile, or a very specific page request).
- Signals collected for the canonical and its cluster include page language, country the content is local to, and usability.
- Stored in the Google index (a large database across thousands of computers). Indexing isn't guaranteed.
- Common indexing issues: low content quality; robots `meta` rules disallowing indexing; site design that makes indexing difficult.

### Serving search results
- Relevance is determined by hundreds of factors, including location, language and device. Example: "bicycle repair shops" returns different results in Paris than in Hong Kong.
- SERP features depend on the query: "bicycle repair shops" likely shows local results and no images; "modern bicycle" more likely shows images but not local results. Visual Element gallery documents common UI elements.
- Indexed in Search Console but not in results can mean: irrelevant content for queries, low content quality, robots `meta` rules preventing serving.
- Follow the Google Search Central blog for algorithm changes.

## SEO Starter Guide
https://developers.google.com/search/docs/fundamentals/seo-starter-guide · Last updated: 2025-12-10

### Purpose and framing
- SEO = helping search engines understand content and helping users find the site and decide whether to visit.
- Following the Essentials makes appearing more likely; no guarantee of indexing. SEO is the next step to improve presence.
- No secrets that automatically rank first; some suggestions may not apply. Best practices make it easier for search engines (not only Google) to crawl, index and understand content.

### How does Google Search work?
- Usually nothing is needed except publishing the site; most sites are found automatically.
- Option to hire a professional (see "Do you need an SEO?").

### How long until I see impact?
- Changes take hours to several months. Wait a few weeks before assessing; not every change has noticeable impact. If unsatisfied, iterate.

### Help Google find your content
- First check whether the site is already indexed with the `site:` search operator (example `site:wikipedia.org`). If absent, review the technical requirements.
- Google mostly finds pages via links from already-crawled pages; inbound links accumulate over time and promotion encourages them.
- Sitemap: optional file listing the URLs you care about; some CMSes generate one. Not required; first make sure people know about the site.

### Check if Google can see your page the same way a user does
- Google needs access to the same resources as the browser (CSS, JavaScript). Hiding them can prevent understanding and ranking.
- For location-dependent content, check what Google sees from its crawler location, generally the US.
- Check with the URL Inspection Tool in Search Console.

### Don't want a page in Google's search results?
- Google supports several ways to opt out of crawling and indexing for files, directories or the whole site; see the guide on preventing content from appearing in search results.

### Organize your site
- Logical organization helps users and search engines see how pages relate. Not urgent: engines will likely understand pages as they are. Most valuable for larger sites and long-term.

#### Use descriptive URLs
- URL parts can appear as breadcrumbs in results (domain + breadcrumb). Google learns breadcrumbs from URL words; structured data can influence them.
- Use words useful to users, for example `https://www.example.com/pets/cats.html`; a random-identifier URL (`/2/6772756D707920636174`) is less helpful.

#### Group topically similar pages in directories
- Matters mainly above a few thousand URLs: directories let Google learn how often each directory's URLs change (for example `/policies/` rarely, `/promotions/` often) and crawl at different frequencies.
- Google has a separate ecommerce site-structure guide; good URL structure matters more for large ecommerce sites.

#### Reduce duplicate content
- Same content under multiple URLs is duplicate content; engines pick one canonical URL per piece of content.
- Not a spam violation, but can be poor UX and waste crawl resources on unwanted URLs. If you don't canonicalize, Google does it automatically.
- Aim for one URL per piece of content. Prefer a redirect from non-preferred URLs to the best URL; if redirecting isn't possible, use `rel="canonical"` `link` element. Don't worry too much; engines usually work it out.

### Make your site interesting and useful
- Compelling, useful content likely affects search presence more than any other suggestion in the guide. Common attributes:
  - Easy to read and well organized: natural writing, no spelling or grammar mistakes, paragraphs, sections and headings.
  - Unique: don't copy others in part or whole; don't just rehash what's published.
  - Up to date: update or delete outdated content.
  - Helpful, reliable, people-first: for example, expert or experienced sources show expertise.

#### Expect your readers' search terms
- Anticipate vocabulary differences between experts and newcomers (example: "charcuterie" vs "cheese board"). Don't worry about covering every variation; Google's language matching understands pages without exact terms.

#### Avoid distracting advertisements
- Ads are fine but must not distract or prevent reading. Problem examples: ads or interstitials (pages shown before or after expected content) that make the site hard to use.

#### Link to relevant resources
- The vast majority of new pages Google finds daily come via links. Links also corroborate what you write.
- Write good link text: anchor text tells users and Google about the target before visiting.
- Link when you need to:
  - Links give context and may demonstrate topical knowledge.
  - For pages you don't control, link only to resources you trust; otherwise add `nofollow` or a similar annotation to avoid association and possible ranking harm.
  - For user-generated content (forum posts, comments), have the CMS automatically add `nofollow` or similar to every user-posted link; this also discourages spammers.

### Influence how your site looks in Google Search
- Focus on the two most visible elements: title link and snippet.

#### Influence your title links
- Sources include the `<title>` element (title text, also used in browsers and bookmarks) and other on-page headings.
- CMS users usually just need to write good titles; most CMSes output `<title>` automatically.
- Good title: unique to the page, clear and concise, accurately describes the content. May include site/business name, physical location, and what the page offers. See the title links documentation for details.

#### Control your snippets
- Snippet is sourced from the page's own content (you control the available words). Occasionally it comes from the meta description tag.
- Good meta description: short, unique to the page, one or two sentences covering the page's most relevant points.

### Add images to your site, and optimize them
- Many people search visually; images can be a first entry point (example "fruit tart recipes").
- Add high-quality images near relevant text: sharp and clear, placed by relevant text, which helps Google understand context (example: yarn shop photo in that shop's section of a London yarn-shops review).
- Add descriptive alt text: short, describes the image's relationship to the content; via the `alt` attribute of `img` or a CMS field.

### Optimize your videos
- Pages primarily about individual videos can surface in video results.
- Create high-quality video; embed on a standalone page near relevant text.
- Write descriptive text in the video title and description fields (apply title best practices).
- Video-focused sites should read the dedicated video optimization docs.

### Promote your website
- Channels: social media, community engagement, online and offline advertising, word of mouth.
- Word of mouth is among the most lasting methods but takes time and prior effort such as community engagement. Google for Creators has audience-building resources.
- Offline: URL on business cards, letterhead, posters; permission-based recurring newsletters.
- Overpromotion can backfire: audience fatigue, and engines may see some practices as manipulation.

### Things we believe you shouldn't focus on
- Meta keywords: Google Search doesn't use the keywords meta tag.
- Keyword stuffing: excessive repetition (even in variations) tires users and violates spam policies.
- Keywords in domain name or URL path: choose the name that is best for the business. For ranking, keywords in the domain or path have hardly any effect beyond appearing in breadcrumbs.
- TLD: matters only when targeting a specific country, and even then is a low-impact signal (example: `.ch` for selling Dutch cheese to searchers in Switzerland). Otherwise Google doesn't care whether it's `.com`, `.org` or `.asia`.
- Minimum or maximum content length: length alone doesn't matter; no word-count target. Varied natural wording gives more chances to match queries.
- Subdomains vs subdirectories: choose what suits the business and site management.
- PageRank: uses links and is fundamental, but only one of many ranking signals.
- Duplicate content "penalty": content on multiple URLs is fine, inefficient, and won't cause a manual action. Copying others' content is different.
- Number and order of headings: semantic order is great for screen readers, but out-of-order headings don't matter to Google Search (the web isn't valid HTML generally). No ideal number of headings; "if you think it's too much, then it probably is".
- E-E-A-T as a ranking factor: stated as "No, it's not."

### Next steps and resources
- Set up Search Console to monitor and optimize performance; learn which reports to check first.
- Maintain SEO over time (site moves, multilingual sites).
- Structured data makes pages eligible for features such as review stars and carousels; see the search gallery.
- Resources: Google Search Central blog; Search Central on LinkedIn and X; Search Central Help Forum (Product Experts, occasionally Googlers); Search Central YouTube channel.

## Developer's guide to Search
https://developers.google.com/search/docs/fundamentals/get-started-developers · Last updated: 2025-12-10

### Framing
- Goal of SEO: more relevant users viewing content; if Google can't understand a page, traffic may be lost.
- Also ensure the site is secure, fast, accessible to all and works on all devices.

### Find out how Google sees your site
- Test in the URL Inspection tool or Rich Results Test.
- Googlebot doesn't always see what browsers show. Example: images invisible to Google because the page uses an unsupported JavaScript feature (Google sees loading icons).

### Check your links
- Googlebot navigates via links, sitemaps and redirects and treats each URL as the first and only one seen from the site.
- Use crawlable `<a>` elements; every page reachable by a link from another findable page.
- Referring link has relevant text or, for image links, a relevant `alt` attribute.
- Build and submit a sitemap (file describing pages, videos, other files and relationships).
- Single-HTML-page JavaScript apps: each screen or piece of content needs its own URL.

### Check how you're using JavaScript
- Google runs JavaScript but with differences and limitations to design around; see JavaScript SEO basics and the fix-JavaScript-problems guide.

### Keep Google updated when content changes
- Submit sitemaps; ask Google to recrawl URLs.
- If pages still aren't indexed, check server logs for errors.

### Don't forget about the words on the page
- Googlebot finds only textually visible content (text inside videos is invisible).
- Express visual content in text (example: a category page of shirt images with no text per item is suboptimal).
- Every page needs a descriptive title and meta description; unique ones help show relevance and can raise traffic.
- Use semantic HTML. Google indexes HTML, PDF, images and video but not content requiring plugins (Java, Silverlight) or rendered in a canvas.
- Text must be accessible in the DOM. Content added through the CSS `content` property is not in the DOM and is currently ignored by Google Search. Fine for decorative content; Google may not index it.

### Tell Google about other versions of your content
- Google doesn't automatically know about mobile/desktop or international versions. Consolidate duplicate URLs, tell Google about localized versions, make AMP pages discoverable.

### Control what content Google sees
- Block finding: restrict to logged-in users (login page or password).
- Block crawling: robots.txt (not a mechanism for keeping a page out of Google; use `noindex` robots rules or password protection).
- Block indexing but allow crawling: `noindex` tag. Mixing crawl and index rules can make rules counteract each other (see Combining crawling with indexing/serving rules).
- Content missing from Search: check access with URL Inspection; test robots.txt for accidental blocking; check HTML `meta` tags for `noindex`.

### Enable rich results
- Rich results = styling, images or interactive features. Provide explicit structured data clues; see the features gallery.

## Maintaining your site's SEO
https://developers.google.com/search/docs/fundamentals/get-started · Last updated: 2025-12-18

### Control how Google crawls and indexes your site
- Understand the crawl, index, serve pipeline to debug and anticipate behavior.
- Duplicate content: understand canonical pages and their effect on crawling and indexing.
- Resources: images, CSS and crawlable pages must be reachable by Google (not blocked by robots.txt, reachable by an anonymous user). Inaccessible pages don't appear in the Page Indexing report and show as not crawled in URL Inspection. Blocked resources appear only per URL in URL Inspection; render the live page there to verify.
- robots.txt: use it to prevent crawling and sitemaps to encourage crawling. Block duplicate content and unimportant resources (such as small frequently used icons or logos) that might overload the server. Never use robots.txt to prevent indexing; use `noindex` or login requirements.
- Sitemaps: tell Google which pages matter and can include extra information such as update frequency; important for non-text content (images, video). Google doesn't restrict crawling to sitemap pages but prioritizes them; most useful for fast-changing content or pages not discoverable by links.

### Internationalized or multi-lingual sites
- Read multi-regional and multilingual guidance; use hreflang for language variants; read how locale-adaptive content affects crawling.

### Migrating a page or a site
- Single URL moved permanently: `301` redirect. Temporary move: `302` so Google keeps crawling the original.
- Removed pages: custom `404` page for UX but the response must be a true `404`, not a `soft 404`.
- Whole site: implement all `301` redirects and sitemap changes, then tell Google about the move so it crawls the new site and forwards signals.

### Follow crawling and indexing best practices
- Make links crawlable.
- Use `rel=nofollow` for paid links, login-required links and untrusted content such as user-submitted content, to avoid passing quality signals or inheriting bad quality.
- Crawl budget: relevant for very large sites (hundreds of millions of periodically changing pages, or tens of millions changing frequently). Best current mechanism: list most recently updated or most important pages in sitemaps and hide less important pages with robots.txt rules.
- JavaScript: follow Google's JavaScript recommendations.
- Multi-page articles: prominent crawlable next/previous links are sufficient.
- Infinite scroll: Google can have trouble; offer a paginated version if you want it crawled.
- Block URLs that change state (posting comments, creating accounts, adding to cart) with robots.txt.
- Review which file types are indexable.
- If Google crawls too much (rare), the site crawl rate can be reduced.
- Migrate HTTP sites to HTTPS for user and site security.

### Help Google understand your site
- Put key information in text, not graphics; text is the safest bet.
- Add structured data for non-text content or extra guidance (can enable rich results). By hand per developer guidelines, or with the WYSIWYG Structured Data Markup helper.
- Data Highlighter: lets you highlight page portions and label them (event, date, price); simple but breaks when layout changes.
> Note: Data Highlighter and the Structured Data Markup helper are mentioned here as options; this page is dated 2025-12-18 and no deprecation is stated on it. Treat as legacy and verify availability before relying on them.

### Follow our guidelines
- Search Essentials contain recommendations and also rules whose violation can lead to removal from the index.
- Content-specific guidance:
  - Video: follow video best practices so Google can find, crawl and show video results.
  - Images: follow image best practices; supply image metadata on the host page for extra information in Google Images; to block an image from indexing use a robots.txt `Disallow` rule.
  - Children: content specifically for children should be tagged child-directed for COPPA compliance.
  - Adult content: consider tagging adult-only pages or sites so they are filtered in SafeSearch.
  - News sites: Google Publisher Center help; News sitemap for faster discovery; prevent site abuse; flexible sampling for limited free views; indicate subscription/paywalled content while allowing crawling; use `meta` tags to limit text or image use in snippets; consider AMP or Web Stories for fast-loading content.
  - Other types (businesses, books, apps, scholarly works): other Google services exist for posting information. Specialized Search features exist for recipes, events, job postings and others.

### Manage the user experience
- Good user experience should be the top goal and is stated to be a ranking factor.
- HTTPS recommended; HTTP sites can be marked "not secure" in Chrome.
- Fast pages usually beat slow ones in user satisfaction. Core Web Vitals report for site-wide numbers; PageSpeed Insights for individual pages; web.dev for guidance. AMP also suggested for fast pages.
- Mobile: page cites over 60 percent of the global internet population using mobile; Google uses a mobile crawler as the default crawler; make the site mobile-friendly.
> Note: the 60 percent figure and AMP/Web Stories recommendations come from the page as written and may be dated; no later figure is given.

### Control your search appearance
- Many result features exist (review stars, events, recipes); implement the appropriate ones.
- Provide a favicon and an article date for results.
- Read title link and snippet guidance; snippet length can be restricted or omitted; use `meta` tags to limit text or image use.

### Using Search Console
- Broad set of reports to monitor and optimize Search performance.

## Creating helpful, reliable, people-first content
https://developers.google.com/search/docs/fundamentals/creating-helpful-content · Last updated: 2026-10-05

### Principle
- Google's automated ranking systems prioritize helpful, reliable information created to benefit people, not to manipulate rankings.

### Self-assess your content
- Have trusted, unaffiliated people give honest assessments. After traffic drops, audit most-impacted pages and the searches they lost, then check them against the questions below.
- Content and quality questions:
  - Original information, reporting, research or analysis?
  - Substantial, complete or comprehensive treatment of the topic?
  - Insightful analysis beyond the obvious?
  - If drawing on other sources, adds substantial value and originality rather than copying or rewriting?
  - Main heading or page title is a descriptive, helpful summary and avoids exaggeration or shock?
  - Bookmark-, share- or recommendation-worthy?
  - Would it be expected in or referenced by a printed magazine, encyclopedia or book?
  - Substantial value compared with other result pages?
  - Spelling or stylistic issues? Sloppy or hastily produced?
  - Mass-produced or outsourced to many creators, or spread over a large site network, so individual pages get less care?
- Expertise questions:
  - Presentation builds trust (clear sourcing, evidence of expertise, author or site background via author page or About page links)?
  - Would a researcher conclude the site is well-trusted or a recognized authority?
  - Written or reviewed by a demonstrable expert or enthusiast?
  - Easily-verified factual errors?

### Provide a great page experience
- Core ranking systems reward good page experience; don't focus on one or two aspects, aim for overall quality across many aspects. See the page experience documentation.

### Focus on people-first content (yes answers = on track)
- Existing or intended audience that would find the content useful coming directly to you?
- Demonstrates first-hand expertise and depth (for example from actually using a product or visiting a place)?
- Site has a primary purpose or focus?
- Readers leave feeling they learned enough to reach their goal?
- Readers leave with a satisfying experience?

### Avoid search engine-first content (yes answers = warning sign)
- Made primarily to attract search visits?
- Lots of content on many topics hoping some ranks?
- Extensive automation across many topics?
- Mainly summarizing others without added value?
- Writing about trends only because trending, not for your audience?
- Readers need to search again for better information?
- Writing to a word count because Google supposedly prefers one (stated: no preferred word count)?
- Entering a niche without expertise just for search traffic?
- Promising an answer that doesn't exist (for example a release date for an unconfirmed product, film or show)?
- Changing page dates to look fresh without substantial change?
- Adding or removing lots of content mainly to seem "fresh" (stated: it won't help rankings)?

### What about SEO?
- SEO means things that help engines discover and understand content; useful when applied to people-first content, not search engine-first content.

### E-E-A-T and quality rater guidelines
- Systems use many factors to find content showing experience, expertise, authoritativeness and trustworthiness (E-E-A-T). Trust is most important; the others contribute, and content needn't show all four.
- E-E-A-T itself isn't a specific ranking factor, but a mix of factors identifying good E-E-A-T is used. More weight goes to content with strong E-E-A-T on topics that could significantly affect health, financial stability, safety, or society's welfare (YMYL, "Your Money or Your Life").
- Search quality raters give feedback on whether systems are working (like diner feedback cards); they don't control rankings and rater data is not used directly in ranking algorithms. Raters are trained to judge E-E-A-T using the search quality rater guidelines; reading them helps self-assessment.
- The guidelines emphasize main-content quality (how effectively it lets the page achieve its purpose and satisfy users) as among the most critical page-quality factors.

### Main content
- Main content = any part of the page that directly helps it achieve its purpose, which can include: primary text and media; interactive features (calculators, tools, games, search); user-generated contributions (forum discussions, reviews, comments, uploads) when they directly serve the page's purpose; tabbed or expanded sections (specs, safety notes, reviews); visible page titles and headings that summarize the topic.
- Raters evaluate four attributes:
  - Effort: human work put into the content or the systems powering it. High: original analysis, manual poem translation, custom interactive game map. Little or none: pages auto-generated from feeds, or large volumes of generative-AI text without manual oversight or curation. Attribution or crediting sources does not replace original effort.
  - Originality: unique information or perspectives not already on other sites.
  - Talent or skill: skill needed for a satisfying experience (clear writing, well-produced video, functional tools). Not all content needs specialized expertise (example: a personal snow-clearing tip).
  - Accuracy: informational pages should be factually accurate; YMYL topics must be highly accurate and consistent with established expert consensus.

### Who, How and Why
- Who: make authorship evident; add bylines where readers expect them; bylines should lead to author background and topic areas. Strongly encouraged to add accurate authorship information. Don't use deceptive authorship (AI-generated headshots, invented names, false credentials): it makes pages untrustworthy and is a low-quality signal.
- How: explaining how content was produced helps readers. Product reviews: number of products tested, results, how tests were done, with evidence such as photos (see the high-quality product reviews page). For substantially automated or AI content ask: is automation use evident through disclosure or otherwise; is background on how it was used provided; is the reason for using it explained. Add disclosures where readers would reasonably expect them to ask "how was this created?".
- Why: the most important question. Content should primarily help people and be useful to visitors who come directly. Content made primarily to attract search visits isn't what systems reward. Using automation, including AI, to produce content mainly to manipulate rankings violates spam policies.

## Guidance on using generative AI content
https://developers.google.com/search/docs/fundamentals/using-gen-ai-content · Last updated: 2026-10-01

- Generative AI is useful for researching and structuring original content, but using it (or similar tools) to produce many pages without added value may violate the scaled content abuse policy. Content must meet the Essentials and spam policies.
- Rater guideline references: scaled content abuse (section 4.6.5) and main content with little to no effort, originality or added value (section 4.6.6). The guidelines are not a ranking guide; ratings don't directly influence ranking.
- Accuracy, quality, relevance:
  - Generative models predict likely word sequences rather than retrieve facts, so outputs can contain inaccuracies (hallucinations).
  - Manually fact-check and review all AI-generated content before publishing, including `<title>` elements, meta descriptions, structured data and image alt text.
  - Structured data must meet the general guidelines, the feature-specific policies and be validated for eligibility.
- Give users context: explain how content was created where it suits the audience (background on how automation was used; image metadata).
- Merchant Center (ecommerce): has its own AI-content policies. AI-generated images must carry IPTC `DigitalSourceType` `TrainedAlgorithmicMedia` metadata. AI-generated product data (title and description attributes) must be specified separately and labeled as AI-generated.

## Optimizing your website for generative AI features on Google Search
https://developers.google.com/search/docs/fundamentals/ai-optimization-guide · Last updated: 2026-07-10

### Is SEO still relevant for generative AI search?
- Yes. Generative features (AI Overviews, AI Mode) are rooted in core ranking and quality systems.
- RAG (grounding): retrieves relevant, current pages from the Search index via core ranking systems, reviews them to generate the response, and shows clickable supporting links.
- Query fan-out: concurrent related queries generated by the model to fetch more results (example: "how to fix a lawn that's full of weeds" fans out to herbicides, chemical-free weed removal, weed prevention).
- AEO (answer engine optimization) and GEO (generative engine optimization): from Google's perspective, optimizing for generative AI search is optimizing for the search experience, so still SEO.

### Create valuable, non-commodity content
- Likely the biggest long-run influence on presence in generative AI search.
- Unique point of view: first-hand review vs a summary that restates what's available; don't recycle what others said or what a model could easily produce.
- Non-commodity vs commodity: commodity content (example "7 Tips for First-Time Homebuyers") is common knowledge; non-commodity (example "Why We Waived the Inspection & Saved Money: A Look Inside the Sewer Line") gives unique expert or experienced takes.
- Organize for readers: paragraphs, sections, headings.
- Add high-quality images and video: generative features can include images and video; following image and video SEO already covers this.
- Don't overdo variations: creating separate content for every query variation (including fan-out queries) primarily to manipulate rankings or AI responses violates the scaled content abuse policy and is ineffective long term; more pages don't make a site better. Google's systems understand relevance even without exact query-to-content match.
- AI-assisted content must meet the Essentials and spam policies.
- Core principle: would visitors find it satisfying?

### Build and maintain a clear technical structure
- Meet technical requirements: to appear in generative AI features a page must be indexed and eligible to show in Google Search with a snippet. Additionally, a site must be included in Search generative AI features in Search Console to be eligible for display there. Indexing and serving are never guaranteed.
- Crawling best practices: generative models use publicly accessible, crawlable content; large frequently updated sites should review crawl budget guidance.
- Semantic HTML: not required to be perfect (the web isn't valid HTML), but helps screen readers and other users.
- JavaScript: Google can process JavaScript content if it isn't blocked, but JS-framework sites are generally more complex; follow JavaScript SEO best practices.
- Page experience: displays well across devices, low latency, main content easily distinguishable from other elements.
- Reduce duplicate content (UX and crawl waste).
- Verify the site in Search Console to find technical issues.

### Optimize local business and ecommerce details
- Responses can include product listings, product info and local business info. Merchant Center (including feeds) and Google Business Profiles support visibility in AI responses and other results.
- Other merchant experiences such as Business Agent (conversational experience on Google Search) may be worth considering.

### Mythbusting: what you don't need to do
- LLMS.txt and other "special" machine-readable files, AI text files, markup or Markdown: Google Search doesn't use them. Creating them for other services is fine; neither helps nor harms Google visibility. Google may crawl and index many file types, which doesn't mean special treatment.
- "Chunking" content into tiny pieces: not required; systems handle multiple topics on a page. No ideal page length.
- Rewriting content just for AI: not needed; systems understand synonyms and meaning, so no need to capture every long-tail variation.
- Inauthentic "mentions": seeking them isn't as helpful as it seems; core ranking systems favor quality and other systems block spam.
- Overfocusing on structured data: not required for generative AI search and no special schema.org markup exists for it; still useful for rich result eligibility.

### Measure visibility
- Generative AI performance report in Search Console covers generative AI features on Google Search and Discover.
- Third-party tools have no access to internal ranking or AI systems; evaluate their advice against official guidance.

### Explore agentic experiences
- AI agents perform tasks (booking, comparing specs). Browser agents may analyze screenshots/visual renderings, the DOM structure, and the accessibility tree.
- If relevant, see agentic experiences and the agent-friendly website best-practices guide. Protocols like Universal Commerce Protocol (UCP) are emerging to let Search agents do more (page frames this as emerging).

### Next steps recap
- Apply foundational SEO; create non-commodity people-first content; prefer effective SEO over AEO/GEO hacks (chunking, llms.txt, inauthentic mentions); monitor in Search Console; explore agentic experiences.
- Plenty of content succeeds in Google Search, including generative experiences, without overt SEO; not everything in the guide is necessary.

## Do you need an SEO?
https://developers.google.com/search/docs/fundamentals/do-i-need-seo · Last updated: 2026-06-05

### What SEOs offer
- Services: content or structure review; technical advice (hosting, redirects, error pages, JavaScript); content development; online business development campaigns; keyword research; SEO training; expertise in specific markets and geographies; optimizing for generative AI.
- Google ads have no effect on organic presence. Google never accepts money to include or rank sites; appearing organically is free.

### Deciding
- Small local businesses can often do much themselves; start with the SEO Starter Guide. Knowing the techniques helps spot discouraged tactics if an SEO is hired.
- Best time to hire: during redesign (the earlier the better) or new site launch; also helpful for existing sites.

### Hiring checklist
- Interview: examples of past work, whether they follow the Search Essentials (previously Webmaster Guidelines), expected results and timeframe and how success is measured, experience in your industry, country/city and international sites, years in business, communication and transparency about changes and reasoning.
- Check that they are interested in your business, competitors and customer discovery.
- Check business references.
- Audit: grant read-only Search Console access at this stage (no write access). An audit should give realistic improvement and effort estimates. Guaranteed first place means find someone else.
- Third-party tools: Google doesn't evaluate or endorse them and they lack Google's internal ranking data; be wary of "acceptable" or "approved by Google" claims. Check recommendations against official guidance before big changes; ask whether they cite official Google documentation, whether AI-experience ("AEO"/"GEO") advice matches Google's guidance, and whether their tools align with Google's guidance.
- Be wary of unsolicited emails from SEO firms.
- Red flags: guaranteed #1 rankings, claimed "special relationship" with Google, "priority submit".
- Be wary of secrecy. If an SEO creates deceptive content on your behalf, the site can be removed from the index; you are responsible for hired companies' actions. An SEO with FTP access should explain all changes.
- You should never have to link to an SEO. Avoid link popularity schemes and submission to thousands of search engines.
- Warning: unethical SEOs using spam-policy-violating techniques can lower presence or cause removal from the index.

### Reporting issues
- US: FTC (website or 1-877-FTC-HELP). Outside the US: https://www.econsumer.gov/.

## Guidance on third-party SEO tools and advice
https://developers.google.com/search/docs/fundamentals/third-party-seo · Last updated: 2026-06-05

- Verify external SEO, listing and AI-experience (AEO/GEO) advice against official guidance. Good advice either marks claims as opinion backed by data/experience or cites official Google guidance. Misattributed "Google says" claims are common.
- Tool and service categories to evaluate: sitemap generation; indexing directives; "SEO-optimized" content generation; ranking-improvement advice; AEO/GEO tools.
- Google doesn't evaluate third-party services; be wary of claims of being "acceptable" or "approved" by Google Search. Using a tool doesn't guarantee ranking.
- Third-party data may be misread as coming from Google. Tools lack Google's internal ranking data and cannot guarantee performance; predictions are their own.
- Google strongly encourages using Search Console regardless, as the first-party source of data.
