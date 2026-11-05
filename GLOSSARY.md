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
| **Breakpoint tier** | One of the four width ranges a layout is designed for: mobile, tablet, desktop, wide (LAY-01). |
| **Canonical URL** | The one preferred URL for a piece of content, declared with `rel=canonical` so duplicates don't compete. |
| **CDN** | Content Delivery Network: servers worldwide that deliver your files from near the visitor. |
| **CLS** | Cumulative Layout Shift: how much the page jumps around while loading. Good: ≤ 0.1. |
| **CMP** | Consent Management Platform: the tool behind the cookie banner that records and enforces choices. |
| **CMS** | Content Management System: where editors create and change content without code. |
| **Consent Mode** | Google's mechanism that tells its tags what the visitor agreed to (ads, analytics …). |
| **Container query** | CSS that adapts a component to the width of its container instead of the whole viewport (`@container`). |
| **Core Web Vitals (CWV)** | Google's three user-experience metrics: LCP (loading), INP (responsiveness), CLS (visual stability). |
| **CORS** | Cross-Origin Resource Sharing: HTTP headers that decide which other websites may read responses from your server. |
| **Crawl / render / index / rank** | How search works: fetch pages by following links, run them like a browser, store what they're about, order them per query. |
| **CSP** | Content Security Policy: a header that tells the browser which scripts and sources may run. Blocks most injection attacks. |
| **CTA** | Call to action: the button or link for the step you want visitors to take. |
| **CTR** | Click-through rate: clicks divided by impressions, e.g. in the Search Console Performance report. |
| **Design tokens** | Named design values (colors, sizes, spacing) shared by design tools and code. |
| **DNS** | The internet's phone book: turns a domain into a server address. |
| **E-E-A-T** | Experience, Expertise, Authoritativeness, Trust. Google's framework for judging content quality; trust matters most. |
| **Entity** | A uniquely identifiable thing (your company, a person, a product) that search engines and AI recognize across the web. |
| **Eyebrow** | A short label above a heading (e.g. "Case study"). Styled small and often uppercase; not a heading in the outline. |
| **Fetch Metadata** | Browser request headers (`Sec-Fetch-Site` and others) that tell the server where a request came from, so cross-site requests can be refused. |
| **Forced colors** | An OS mode (e.g. Windows contrast themes) that replaces site colors with a user-chosen palette. |
| **GA4** | Google Analytics 4, Google's analytics product. |
| **GTM** | Google Tag Manager: a container for adding and controlling tracking tags without code changes. |
| **hreflang** | Annotation telling search engines which language/region version of a page to show to whom. |
| **HSTS** | Header that forces browsers to use HTTPS for your domain. |
| **Hydration** | JavaScript taking over server-rendered HTML to make it interactive. Less hydration = faster pages. |
| **Idempotency** | Doing the same request twice has the same effect as doing it once, e.g. a double-clicked "Pay" creates one order. |
| **Impressum** | Legal notice with provider details, mandatory for commercial websites in Germany (DDG §5). |
| **IndexNow** | Protocol to notify Bing and other engines instantly about new or changed URLs. |
| **INP** | Interaction to Next Paint: how quickly the page responds to clicks and taps. Good: ≤ 200 ms. |
| **Intent** | What the searcher actually wants: information, comparison, purchase or a specific site. |
| **JSON-LD** | The recommended format for structured data: a script block describing the page in Schema.org terms. |
| **JWT / OAuth** | JWT: a signed token that carries login information. OAuth: the standard behind "Sign in with …" and delegated access. |
| **Key event** | A GA4 event marked as important (formerly "conversion"), e.g. a completed form. |
| **Landmarks** | HTML regions (`header`, `nav`, `main`, `footer`) that let screen-reader users jump around a page. |
| **LCP** | Largest Contentful Paint: when the main content (often the hero image) has loaded. Good: ≤ 2.5 s. |
| **Lighthouse** | Google's automated lab audit for performance, accessibility, SEO and best practices. |
| **llms.txt** | Unofficial proposal for a Markdown index of a site for AI tools. Not used by Google. |
| **noindex** | Directive that keeps a page out of search results. |
| **OKLCH** | A color space that matches how people perceive lightness, used to build even color scales. |
| **Open Graph** | Meta tags that control the preview (title, image) when a page is shared on social media or in messengers. |
| **Orphan page** | A page no other page links to; hard for users and crawlers to find. |
| **Owner / Full / Restricted** | Search Console permission levels: owners manage users and settings, full users see all data and act, restricted users mostly view. |
| **p75** | 75th percentile: the value that 75 % of real visits meet or beat. Core Web Vitals are judged at p75. |
| **Pillar / cluster** | A broad overview page (pillar) linking to detailed pages (cluster) on sub-topics, and back. |
| **Prerender / SSG / SSR / CSR** | Ways to produce HTML: at build time (prerender / static site generation), per request on the server (SSR), or in the browser (CSR). |
| **PWA (progressive web app)** | A website that can be installed to the home screen or desktop and opens like an app, without an app store. |
| **robots.txt** | File at the site root that tells crawlers which paths they may fetch. Controls crawling, not indexing. |
| **RTL** | Right-to-left scripts such as Arabic or Hebrew. |
| **RUM** | Real User Monitoring: performance measured on actual visitors' devices (field data), as opposed to lab tests. |
| **Safe area** | The part of a phone screen not covered by notches, rounded corners or the home indicator (`env(safe-area-inset-*)`). |
| **Schema.org / structured data** | Shared vocabulary for describing content to machines (Organization, Product, Article …). |
| **Search Console** | Google's free tool showing how your site performs in Search, with indexing reports and alerts. |
| **SERP** | Search Engine Results Page. |
| **Server Components** | React components that run only on the server and send finished HTML, so the browser downloads less JavaScript and search engines see the content directly. |
| **Service worker** | A small script the browser runs in the background; it caches files so a site works offline and can receive push messages. |
| **Sitemap (XML)** | File listing the URLs you want indexed, with last-modified dates. |
| **Skeleton** | A grey placeholder in the shape of the coming content, shown while it loads. |
| **SPF / DKIM / DMARC** | DNS records that prove email from your domain is genuine and stop spoofing. |
| **SSRF** | Server-Side Request Forgery: tricking a server into fetching internal or private addresses on the attacker's behalf. |
| **Stress fixture** | Test content at the extremes (empty, very long, unbroken strings, RTL, many items) used to check that layouts don't break. |
| **svh / dvh** | Viewport-height units that account for mobile browser toolbars: small (svh) and dynamic (dvh) viewport height. |
| **Tabular numerals** | Digits of equal width, so numbers line up in columns (`font-variant-numeric: tabular-nums`). |
| **Tailwind CSS** | A styling tool where short class names (e.g. `p-4`, `bg-action-primary`) apply design values; here it is limited to the design tokens. |
| **TBT** | Total Blocking Time: lab metric for how long scripts block the page. Proxy for INP in lab tests. |
| **TLS / HTTPS** | Encryption between browser and server. |
| **Toast** | A short, temporary message (e.g. "Saved") that appears at the edge of the screen and disappears on its own. |
| **TTFB** | Time to First Byte: how fast the server starts answering. Good: ≤ 0.8 s. |
| **UTM parameters** | Tags added to campaign links (`utm_source`, `utm_medium`, `utm_campaign`) so analytics can attribute visits. |
| **Validate Fix** | A Search Console button that asks Google to recrawl the affected URLs after you fixed an indexing or enhancement issue. |
| **WCAG** | Web Content Accessibility Guidelines (W3C). Level AA of version 2.2 is the target in this blueprint. |
| **Web app manifest** | A JSON file that tells the browser an app's name, icons, colors and how it opens when installed. |
| **YMYL** | "Your Money or Your Life": topics (health, finance, legal, safety) where bad information can cause real harm, judged more strictly. |
