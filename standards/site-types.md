# Site types

Profiles adjust the standards per site type. **Raise** = SHOULD/COULD becomes MUST · **Relax** = rule applies in reduced form · **Add** = type-specific requirement. All rules not mentioned apply unchanged. Mixed sites (e.g. SaaS marketing site + blog) combine profiles.

## Corporate & service business

- **Goal / KPI:** qualified leads, calls, bookings.
- **Rendering:** static.
- **Schema:** Organization, LocalBusiness subtype per location, BreadcrumbList, JobPosting on career pages.
- **Raise:** SEO-31 (sites with several locations), UX-08, UX-12.
- **Add:** career pages with JobPosting markup. JobPosting is the one case where Google's Indexing API may be used.

## Landing page (campaign)

- **Goal / KPI:** conversion rate, cost per acquisition.
- **Rendering:** static, single page.
- **Schema:** WebPage plus Organization.
- **Raise:** PRF-04 (≤ 500 KB), UX-08.
- **Relax:** internal-linking rules (SEO-22 to SEO-24). Pages built only for paid traffic and their test variants are `noindex` (SEO-02, UX-16).
- **Add:** keep the ad promise and the landing page's message identical. Show ad-to-page relevance, transparency (who you are, price, terms) and an easy way to leave.

## Blog & publisher

- **Goal / KPI:** organic sessions, subscribers, assisted conversions.
- **Rendering:** static with incremental builds.
- **Schema:** BlogPosting or NewsArticle, Person (author), BreadcrumbList.
- **Raise:** CON-03, CON-13, GEO-07, GEO-08.
- **Add:**
  - RSS/Atom feed, author archives, paginated archives (SEO-14).
  - Large images ≥ 1200 px wide with `max-image-preview:large` for Discover.

## SaaS

- **Goal / KPI:** trials, sign-ups, demo requests, activation.
- **Rendering:** the marketing site is static. The app runs client-side behind login, on its own subdomain or path.
- **Schema:** SoftwareApplication, Organization.
- **Raise:** SEC-17, SEC-19, MSR-11 (for self-serve purchases), UX-14.
- **Add:**
  - App and account areas send `noindex` (SEO-02).
  - Transparent pricing page; indexable docs and help center; public changelog.
  - Status page on a separate domain (MSR-21).
  - Cancellation button for B2C subscriptions (PRV-12).

## E-commerce

- **Goal / KPI:** revenue, conversion rate, average order value.
- **Rendering:** category and product pages prerendered or server-rendered; cart and checkout dynamic.
- **Schema:** Product with Offer, shipping details and MerchantReturnPolicy; BreadcrumbList; Organization (`OnlineStore`).
- **Raise:** SEO-13, SEO-14, MSR-11, SEC-16, QA-06.
- **Add:**
  - Out of stock: keep the page and mark its availability. Discontinued for good: 301 to the successor, or 410.
  - Payments through hosted fields of a PCI DSS–compliant provider.
  - Product feed matches the page.
  - Accessibility law applies (A11Y-02), as do the e-commerce duties (PRV-12).

## Web application

- **Goal / KPI:** activation, retention, task success.
- **Rendering:** client- or server-rendered behind login; public pages static.
- **Raise:** SEC-16, SEC-17, SEC-19, QA-06, QA-13.
- **Relax:** SEO rules apply to public pages only. TEC-03: JavaScript may be required inside the app.
- **Add:**
  - Product analytics only with consent (PRV-01).
  - Session timeout warnings (WCAG 2.2.1).
  - Every core task is covered by E2E tests (QA-05).
