# Glossary

Plain-language definitions of the terms used in this blueprint, in alphabetical order.

| Term | Meaning |
|---|---|
| **301 / 302 / 410** | HTTP status codes. 301 = moved permanently (passes ranking signals), 302 = moved temporarily, 410 = gone for good. |
| **404 / soft 404** | 404 = page not found. A *soft 404* is an error or empty page that wrongly answers "200 OK", which wastes crawling and confuses search engines. |
| **A/B test** | Showing two versions of a page to different visitors to see which converts better. |
| **AEO / GEO** | Answer / Generative Engine Optimization: making content findable and citable in AI answers. Google treats it as part of SEO. |
| **AI Overview / AI Mode** | Google's AI-generated answers above or instead of the classic result list. They cite source pages. |
| **Alt text** | Text alternative for an image, read by screen readers and used by search engines. |
| **ARIA** | Attributes that add accessibility meaning to custom widgets. Only needed when no native HTML element fits. |
| **Baseline** | web.dev label for web features that work in all major browsers. "Widely available" = safe to use without fallbacks. |
| **bfcache** | Back/forward cache: the browser keeps a page in memory so the back button is instant. |
| **Breadcrumb** | Trail like *Home › Services › Consulting* that shows where a page sits. |
| **Canonical URL** | The one preferred URL for a piece of content, declared with `rel=canonical` so duplicates don't compete. |
| **CDN** | Content Delivery Network: servers worldwide that deliver your files from near the visitor. |
| **CLS** | Cumulative Layout Shift: how much the page jumps around while loading. Good: ≤ 0.1. |
| **CMP** | Consent Management Platform: the tool behind the cookie banner that records and enforces choices. |
| **CMS** | Content Management System: where editors create and change content without code. |
| **Consent Mode** | Google's mechanism that tells its tags what the visitor agreed to (ads, analytics …). |
| **Core Web Vitals (CWV)** | Google's three user-experience metrics: LCP (loading), INP (responsiveness), CLS (visual stability). |
| **Crawl / render / index / rank** | How search works: fetch pages by following links, run them like a browser, store what they're about, order them per query. |
| **CSP** | Content Security Policy: a header that tells the browser which scripts and sources may run. Blocks most injection attacks. |
| **CTA** | Call to action: the button or link for the step you want visitors to take. |
| **Design tokens** | Named design values (colors, sizes, spacing) shared by design tools and code. |
| **DNS** | The internet's phone book: turns a domain into a server address. |
| **E-E-A-T** | Experience, Expertise, Authoritativeness, Trust. Google's framework for judging content quality; trust matters most. |
| **Entity** | A uniquely identifiable thing (your company, a person, a product) that search engines and AI recognize across the web. |
| **GA4** | Google Analytics 4, Google's analytics product. |
| **GTM** | Google Tag Manager: a container for adding and controlling tracking tags without code changes. |
| **hreflang** | Annotation telling search engines which language/region version of a page to show to whom. |
| **HSTS** | Header that forces browsers to use HTTPS for your domain. |
| **Hydration** | JavaScript taking over server-rendered HTML to make it interactive. Less hydration = faster pages. |
| **Impressum** | Legal notice with provider details, mandatory for commercial websites in Germany (DDG §5). |
| **INP** | Interaction to Next Paint: how quickly the page responds to clicks and taps. Good: ≤ 200 ms. |
| **IndexNow** | Protocol to notify Bing and other engines instantly about new or changed URLs. |
| **Intent** | What the searcher actually wants: information, comparison, purchase or a specific site. |
| **JSON-LD** | The recommended format for structured data: a script block describing the page in Schema.org terms. |
| **Key event** | A GA4 event marked as important (formerly "conversion"), e.g. a completed form. |
| **Landmarks** | HTML regions (`header`, `nav`, `main`, `footer`) that let screen-reader users jump around a page. |
| **LCP** | Largest Contentful Paint: when the main content (often the hero image) has loaded. Good: ≤ 2.5 s. |
| **Lighthouse** | Google's automated lab audit for performance, accessibility, SEO and best practices. |
| **llms.txt** | Unofficial proposal for a Markdown index of a site for AI tools. Not used by Google. |
| **noindex** | Directive that keeps a page out of search results. |
| **Open Graph** | Meta tags that control the preview (title, image) when a page is shared on social media or in messengers. |
| **Orphan page** | A page no other page links to; hard for users and crawlers to find. |
| **p75** | 75th percentile: the value that 75 % of real visits meet or beat. Core Web Vitals are judged at p75. |
| **Pillar / cluster** | A broad overview page (pillar) linking to detailed pages (cluster) on sub-topics, and back. |
| **Prerender / SSG / SSR / CSR** | Ways to produce HTML: at build time (prerender / static site generation), per request on the server (SSR), or in the browser (CSR). |
| **robots.txt** | File at the site root that tells crawlers which paths they may fetch. Controls crawling, not indexing. |
| **RTL** | Right-to-left scripts such as Arabic or Hebrew. |
| **RUM** | Real User Monitoring: performance measured on actual visitors' devices (field data), as opposed to lab tests. |
| **Schema.org / structured data** | Shared vocabulary for describing content to machines (Organization, Product, Article …). |
| **Search Console** | Google's free tool showing how your site performs in Search, with indexing reports and alerts. |
| **SERP** | Search Engine Results Page. |
| **Sitemap (XML)** | File listing the URLs you want indexed, with last-modified dates. |
| **SPF / DKIM / DMARC** | DNS records that prove email from your domain is genuine and stop spoofing. |
| **TBT** | Total Blocking Time: lab metric for how long scripts block the page. Proxy for INP in lab tests. |
| **TLS / HTTPS** | Encryption between browser and server. |
| **TTFB** | Time to First Byte: how fast the server starts answering. Good: ≤ 0.8 s. |
| **UTM parameters** | Tags added to campaign links (`utm_source`, `utm_medium`, `utm_campaign`) so analytics can attribute visits. |
| **WCAG** | Web Content Accessibility Guidelines (W3C). Level AA of version 2.2 is the target in this blueprint. |
| **YMYL** | "Your Money or Your Life": topics (health, finance, legal, safety) where bad information can cause real harm, judged more strictly. |
