# 08 · Performance

**Why it matters:** Faster pages keep more visitors and convert better. Core Web Vitals measure what real users experience, and Google's ranking systems use them. Guide: step 26.

Detail: `reference/google-search/` notes.

Scope: Core Web Vitals, budgets, images, fonts, JavaScript, network and caching.

Last verified: 2026-10

## Targets

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRF-01 | MUST | [house] Core Web Vitals are "good" at the 75th percentile of real users, on mobile and on desktop: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. | PageSpeed Insights field data; GSC Core Web Vitals (≈ 28 days after launch) |
| PRF-02 | MUST | Before launch, every key template passes in the lab: Lighthouse mobile, median of ≥ 3 runs, LCP ≤ 2.5 s, TBT ≤ 200 ms, CLS ≤ 0.1. | Lighthouse CI ([`lighthouserc.json`](../templates/ci/lighthouserc.json)) |
| PRF-03 | SHOULD | Key templates score ≥ 90 for Lighthouse mobile performance. | Lighthouse CI |
| PRF-04 | SHOULD | Budgets per page: ≤ 1.5 MB transferred (landing pages ≤ 500 KB), ≤ 170 KB compressed JavaScript on content pages, TTFB ≤ 0.8 s at p75. | Lighthouse; WebPageTest |
| PRF-05 | SHOULD | Real-user Core Web Vitals are collected per template (web-vitals library → analytics or RUM tool). | RUM dashboard |
| PRF-22 | MUST | No HTML, CSS or JS file exceeds 2 MB uncompressed: Googlebot reads only the first 2 MB of each file (64 MB for PDFs) and ignores the rest. | Crawler file-size report; DevTools uncompressed size |

## Images & media

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRF-06 | MUST | Images are AVIF or WebP (`<picture>` fallback if needed), resized to their display size with `srcset`/`sizes`, and compressed. | Lighthouse image audits |
| PRF-07 | MUST | Every `<img>`, `<video>` and `<iframe>` reserves its space with `width`/`height` or CSS `aspect-ratio`. | Lighthouse CLS diagnostics |
| PRF-08 | MUST | The LCP image is in the initial HTML, never lazy-loaded, with `fetchpriority="high"`. Below-the-fold images use `loading="lazy"` (SEO-40). | Lighthouse "LCP request discovery" |
| PRF-09 | SHOULD | No autoplaying hero video on mobile. Videos use a poster image and `preload="none"`. Secondary third-party players load as placeholders (TEC-21); videos meant to rank do not wait for a click (SEO-45). | Network panel |

## Fonts

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRF-10 | MUST | Fonts are self-hosted WOFF2, subset to the scripts in use, and limited to the weights in use (one variable font beats several static files). | Network panel |
| PRF-11 | MUST | `font-display: swap` or `optional`, with a metric-matched fallback (`size-adjust`, `ascent-override`). Preload at most the 1–2 fonts used above the fold. | Lighthouse; CLS on font swap |

## JavaScript & CSS

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRF-12 | MUST | Scripts use `defer` or `type="module"`. No render-blocking third-party scripts in `<head>`. | Lighthouse "render-blocking requests" |
| PRF-13 | MUST | Third-party scripts load only after consent or on interaction, and only those listed in the inventory (TEC-20). | Network panel before consent |
| PRF-14 | SHOULD | JavaScript is split per route. Only interactive components hydrate. Unused JS and CSS are removed. | Coverage tool; bundle analyzer |
| PRF-15 | SHOULD | Interactions run no long tasks over 50 ms. Long work is split and yields to the main thread. | Performance panel; INP attribution |
| PRF-16 | SHOULD | Pages qualify for the back/forward cache: no `unload` handlers and no `Cache-Control: no-store` on public pages. | Lighthouse bfcache audit |

## Network & caching

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRF-17 | MUST | Fingerprinted static assets send `Cache-Control: public, max-age=31536000, immutable`. HTML is revalidated (`no-cache` or short `max-age`). | `curl -I` |
| PRF-18 | SHOULD | `preconnect` only to critical third-party origins (≤ 3). No unused preloads. | Lighthouse warnings |
| PRF-19 | COULD | Multi-page sites prerender likely next pages with Speculation Rules (`moderate` eagerness). | DevTools → Speculative loads |
| PRF-20 | COULD | Cross-document View Transitions are added as progressive enhancement and respect `prefers-reduced-motion`. | Manual check |
| PRF-21 | COULD | Page weight and request count are tracked as a proxy for energy use. Static, cached delivery is preferred. | Monthly budget report |

## Sources

- [web.dev: Web Vitals](https://web.dev/articles/vitals) · [INP](https://web.dev/articles/inp) · [LCP](https://web.dev/articles/lcp) · [CLS](https://web.dev/articles/cls) · [TTFB](https://web.dev/articles/ttfb)
- [web.dev: LCP and INP now Baseline](https://web.dev/blog/lcp-and-inp-are-now-baseline-newly-available)
- [web.dev: Font best practices](https://web.dev/articles/font-best-practices) · [Fetch priority](https://web.dev/articles/fetch-priority) · [bfcache](https://web.dev/articles/bfcache)
- [Chrome: Prerender pages](https://developer.chrome.com/docs/web-platform/prerender-pages)
- [Google: Googlebot file size limits](https://developers.google.com/search/docs/crawling-indexing/googlebot) · [Video best practices](https://developers.google.com/search/docs/appearance/video)
- [Chrome: Lighthouse overview](https://developer.chrome.com/docs/lighthouse/overview)
