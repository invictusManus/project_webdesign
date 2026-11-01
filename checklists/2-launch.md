# Launch checklist

Release gate for new sites and relaunches. On an existing site it doubles as the audit sheet ([`audit-report.md`](../templates/audit-report.md)).

Every MUST passes, or has a documented exception with an owner and a due date. Rule details and verify methods are in [`standards/`](../standards/). Conditional items: *(local)*, *(shop)*, *(accounts)*, *(multilingual)*, *(EU)*.

## A · Release gate

### Design, UX & content
- [ ] DES-03 Token color pairs pass contrast
- [ ] DES-04 Typography rules
- [ ] DES-06 Component states documented
- [ ] DES-10 Logo, favicons, OG images
- [ ] DES-05 φ spacing scale · DES-14 palette structure · DES-16 golden-ratio layout
- [ ] DES-17 shape system · DES-18 button tiers · DES-19 link styling
- [ ] DES-21 No generic AI look
- [ ] CON-16 Every text passed the AI-writing checklist
- [ ] PSY-01 Reviewed against UX psychology · PSY-14 heuristic evaluation done, no open P0/P1
- [ ] PSY-02 Gestalt · PSY-03 hierarchy · PSY-04 Hick · PSY-05 Fitts · PSY-06 Jakob
- [ ] PSY-07 · PSY-08 Nielsen heuristics · PSY-09 cognitive load · PSY-13 ethical conversion
- [ ] UX-02 Consistent navigation and footer
- [ ] UX-05 No overflow from 360 to 1440 px, no hover-only functions
- [ ] UX-06 One primary call to action per page
- [ ] UX-07 Clear first screen
- [ ] UX-09 Lean forms with confirmation
- [ ] UX-10 Empty, loading and error states
- [ ] UX-11 No dark patterns
- [ ] CON-04 Every page adds original value
- [ ] CON-05 About, bylines, sources
- [ ] CON-06 Honest dates
- [ ] CON-09 AI-assisted content reviewed
- [ ] CON-12 Owner and review date per page

### AI search
- [ ] GEO-01 SEO gate passed first
- [ ] GEO-02 No snippet restrictions on key pages
- [ ] GEO-03 AI crawler policy live; CDN doesn't block allowed bots
- [ ] GEO-05 Consistent entity name and description
- [ ] GEO-06 Organization graph with `sameAs`
- [ ] GEO-17 · GEO-18 · GEO-19 isitagentready: Discoverability, Content, Bot Access Control 100 %

### Technical & SEO
- [ ] TEC-01 Document head basics
- [ ] TEC-02 Valid HTML, unique IDs
- [ ] TEC-05 Custom 404/500 with correct status
- [ ] TEC-06 Rendering choice documented
- [ ] TEC-08 CDN, HTTP/2+, compression, auto-TLS
- [ ] TEC-09 Rollback tested
- [ ] TEC-10 Staging protected and noindexed
- [ ] TEC-11 No secrets in repo or bundle
- [ ] TEC-12 Backup and tested restore
- [ ] TEC-13 Domain owned by client, 2FA, auto-renew
- [ ] TEC-15 SPF, DKIM, DMARC
- [ ] TEC-17 Every form tested end to end
- [ ] TEC-18 Tracking-free spam protection
- [ ] TEC-19 CMS fields incl. required alt text
- [ ] TEC-20 Third-party inventory complete
- [ ] TEC-25 No end-of-life software
- [ ] TEC-29 CDN, WAF and firewall let Googlebot through
- [ ] SEO-01 Indexable URLs return 200 with content in HTML
- [ ] SEO-02 Noindex, not robots.txt, for exclusions
- [ ] SEO-03 robots.txt valid, lists sitemap
- [ ] SEO-38 robots.txt served with 200 on every host
- [ ] SEO-04 No staging leftovers on production
- [ ] SEO-05 One canonical host, single 301s
- [ ] SEO-06 Self-referencing canonicals
- [ ] SEO-41 Canonical signals agree on one HTTPS URL
- [ ] SEO-07 Clean XML sitemap
- [ ] SEO-08 No soft 404s
- [ ] SEO-09 Redirects one hop
- [ ] SEO-10 Content and directives server-rendered
- [ ] SEO-11 Crawlable links
- [ ] SEO-39 Mobile content parity
- [ ] SEO-40 Lazy content loads without interaction
- [ ] SEO-15 Unique titles
- [ ] SEO-16 Unique meta descriptions
- [ ] SEO-17 One H1
- [ ] SEO-21 Structured data valid and visible
- [ ] SEO-46 Markup on crawlable pages, required properties, crawlable images
- [ ] SEO-47 Honest review and rating markup
- [ ] SEO-48 *(shop)* Product and Offer markup complete and matching the page
- [ ] SEO-51 *(job pages)* JobPosting on leaf pages, expired jobs handled
- [ ] SEO-52 *(paywalls)* Googlebot sees full content, paywall markup
- [ ] SEO-22 No orphan pages
- [ ] SEO-25 Zero broken internal links
- [ ] SEO-27 No link schemes
- [ ] SEO-33 Spam policies respected
- [ ] SEO-57 Third-party and affiliate content integrated with original value
- [ ] SEO-29 *(local)* Business Profile verified and clean
- [ ] SEO-30 *(local)* NAP identical everywhere

### Performance
- [ ] PRF-03 PageSpeed Insights ≥ 90 in all categories, mobile and desktop
- [ ] PRF-02 Lab gate on every key template
- [ ] PRF-06 Modern, responsive images
- [ ] PRF-07 Media dimensions reserved
- [ ] PRF-08 LCP image eager and high priority
- [ ] PRF-10 Self-hosted, subset WOFF2
- [ ] PRF-11 Font display and fallback metrics
- [ ] PRF-12 No render-blocking scripts
- [ ] PRF-13 Third parties after consent or interaction
- [ ] PRF-17 Immutable asset caching
- [ ] PRF-22 No HTML, CSS or JS file over 2 MB

### Accessibility
- [ ] A11Y-01 WCAG 2.2 AA target met
- [ ] A11Y-02 *(EU)* Accessibility statement if in scope
- [ ] A11Y-03 Landmarks and skip link
- [ ] A11Y-04 Heading outline, native elements
- [ ] A11Y-05 Language attributes
- [ ] A11Y-06 Text alternatives
- [ ] A11Y-07 Contrast
- [ ] A11Y-08 Reflow and zoom
- [ ] A11Y-09 Captions, transcripts, no autoplay audio
- [ ] A11Y-10 Reduced motion, no flashing
- [ ] A11Y-11 Full keyboard operation
- [ ] A11Y-12 Visible, unobscured focus
- [ ] A11Y-13 Target size
- [ ] A11Y-14 Drag alternatives
- [ ] A11Y-15 Meaningful link text
- [ ] A11Y-16 Labelled form fields
- [ ] A11Y-17 Clear error messages
- [ ] A11Y-18 No redundant entry
- [ ] A11Y-19 Consistent help
- [ ] A11Y-20 Accessible authentication
- [ ] A11Y-23 Automated scan: 0 violations
- [ ] A11Y-24 Manual keyboard and screen reader test

### Security
- [ ] SEC-01 TLS configuration
- [ ] SEC-02 HSTS
- [ ] SEC-03 Baseline headers
- [ ] SEC-04 CSP header (enforced, or report-only with a dated plan)
- [ ] SEC-08 Cookie flags
- [ ] SEC-09 No unsafe DOM sinks
- [ ] SEC-10 Server-side validation, safe uploads
- [ ] SEC-11 Server-side access control, MFA on admin
- [ ] SEC-12 CSRF protection and rate limits
- [ ] SEC-13 *(accounts)* Password and MFA policy
- [ ] SEC-14 Supply-chain controls
- [ ] SEC-15 Patch SLAs agreed

### Privacy & legal
- [ ] PRV-01 *(EU)* Nothing non-essential before consent
- [ ] PRV-02 *(EU)* Fair consent banner
- [ ] PRV-03 Consent Mode v2 defaults
- [ ] PRV-04 *(EU)* Complete privacy policy
- [ ] PRV-05 *(EU)* Processing agreements and transfers
- [ ] PRV-06 Data minimization and retention
- [ ] PRV-10 *(EU)* Impressum
- [ ] PRV-11 Newsletter double opt-in
- [ ] PRV-12 *(shop, EU)* E-commerce duties
- [ ] PRV-13 *(EU)* AI disclosure and labels

### Measurement
- [ ] MSR-01 Search Console domain property
- [ ] MSR-06 Measurement plan
- [ ] MSR-07 GA4 configured
- [ ] MSR-08 Key events tested
- [ ] MSR-14 One owned tag container
- [ ] MSR-15 Consent settings on every tag, tested
- [ ] MSR-20 *(shop)* Merchant feed via Merchant API
- [ ] MSR-21 Uptime monitoring with alerts
- [ ] MSR-22 Expiry alerts

### Internationalization *(multilingual)*
- [ ] I18N-01 One URL per language or market
- [ ] I18N-02 No forced geo or language redirects
- [ ] I18N-03 Complete, reciprocal hreflang
- [ ] I18N-04 Self-canonical per language
- [ ] I18N-05 Correct `lang` and `og:locale`
- [ ] I18N-06 Fully localized templates
- [ ] I18N-10 RTL support *(RTL languages)*

### Quality assurance
- [ ] QA-01 Browser matrix tested
- [ ] QA-02 Viewports tested
- [ ] QA-03 Static checks in CI
- [ ] QA-04 Lighthouse CI assertions pass
- [ ] QA-05 E2E tests for critical flows
- [ ] QA-07 Real-device test
- [ ] QA-08 Full pre-launch crawl
- [ ] QA-09 No placeholders or test pages
- [ ] QA-10 No open P0/P1 defects

## B · Launch day

- [ ] Lower DNS TTL at least 7 days before (TEC-14), switch DNS, then confirm HTTPS and host redirects (SEO-05)
- [ ] Production has no `noindex`, no `Disallow: /` and no password (SEO-04)
- [ ] Submit the sitemap (MSR-02); inspect key pages and request indexing (MSR-03)
- [ ] Set up Bing Webmaster Tools and IndexNow (MSR-04)
- [ ] Fresh browser profile: no cookies or tags before consent (PRV-01, MSR-15)
- [ ] Submit every form once and confirm delivery (TEC-17)
- [ ] Uptime and expiry monitors are live (MSR-21, MSR-22)
- [ ] Take a backup of the launch state (TEC-12)

## C · First 14 days

- [ ] Daily: error tracking, server 404 log, uptime alerts
- [ ] Day 2: Search Console Page indexing and Crawl stats show no unexpected errors (MSR-02)
- [ ] Day 3: key events arrive in GA4 with plausible counts (MSR-08)
- [ ] Day 7: 404s from old or external links are redirected (SEO-08, SEO-35)
- [ ] Day 14: first ranking and traffic snapshot vs. baseline; open issues triaged
- [ ] Day 28+: field Core Web Vitals pass (PRF-01)

## D · Relaunch add-on

- [ ] SEO-34 URL inventory complete
- [ ] SEO-35 1:1 redirect map deployed and crawled
- [ ] SEO-36 Content, title and markup parity checked
- [ ] SEO-37 Change of address (domain move); weekly checks for 8 weeks
