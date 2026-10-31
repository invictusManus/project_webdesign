# Tools

One tool per job, chosen from official or well-established tools. "Free" covers most sites; "Pro" is for when depth, history or scale is needed. Prices and plans change, so check the vendor before buying. Last verified: 2026-10.

## Research & strategy (preflight)

| Job | Free | Pro |
|---|---|---|
| Own search data | Google Search Console, Bing Webmaster Tools | — |
| Keyword volume & ideas | Google Keyword Planner | Ahrefs **or** Semrush (pick one) |
| Competitors & visibility | Ahrefs Webmaster Tools (own site) | Same suite; Sistrix for DACH visibility; Similarweb for market sizing |
| SERP, keyword, backlink & AI-answer data for agents | — | treg.io (pay per call, see below) |
| Local | Google Business Profile | BrightLocal |
| UX research | Microsoft Clarity (heatmaps, replays) | Maze or Lyssna (prototype tests) |

## Design

| Job | Free | Pro |
|---|---|---|
| UI design & prototyping | Penpot | Figma |
| Design tokens | `tokens.json` (W3C DTCG) | Tokens Studio, Figma variables |
| Contrast | WebAIM Contrast Checker | Stark |

## Build & QA

| Job | Free | Pro |
|---|---|---|
| Technical SEO crawl | Screaming Frog (≤ 500 URLs) | Screaming Frog licence, Sitebulb |
| Performance (lab + field) | PageSpeed Insights, Lighthouse, CrUX Vis, WebPageTest | DebugBear or SpeedCurve (RUM + monitoring) |
| Accessibility | axe DevTools, Accessibility Insights, WAVE, NVDA, VoiceOver | axe DevTools Pro |
| E2E & cross-browser | Playwright | BrowserStack (real devices) |
| HTML validation | Nu HTML Checker, html-validate | — |
| Structured data | Rich Results Test, Schema Markup Validator | — |
| Security | MDN HTTP Observatory, SSL Labs, ZAP, Dependabot | Snyk |
| Email/DNS | MXToolbox, Google Postmaster Tools, internet.nl | EasyDMARC or dmarcian |

## Measure & operate

| Job | Free | Pro |
|---|---|---|
| Analytics | GA4 (needed for Google Ads) | Plausible, Fathom or Matomo (privacy-friendly) |
| Tag management | Google Tag Manager | Server-side GTM |
| Consent | Google-certified CMP free tier | Usercentrics/Cookiebot, OneTrust, Didomi |
| Rank tracking | Search Console | Suite tracker, AccuRanker |
| AI visibility | Search Console generative-AI report, Bing AI Performance report | Peec AI, Otterly.AI, suite AI add-ons |
| Uptime | Uptime Kuma (self-hosted) | Better Stack |
| Errors | Sentry (free tier) | Sentry Team |
| Synthetic checks | Playwright in CI | Checkly |

## treg.io

**What it is:** a registry and proxy that gives AI agents one key, via MCP, CLI or REST, for 4,000+ API endpoints from about 120 providers.

**What it covers:**
- SEO: SERP, keywords, backlinks and on-page audits (DataForSEO, SE Ranking, Serpstat and others).
- AI answer sampling (ChatGPT, Perplexity, Gemini, AI Mode, Claude).
- The site's own Search Console, GA4 and Business Profile data, via OAuth.
- Generative media models.

**Pricing:** prepaid credit, priced per call, with the price shown before each call. No subscription.

**Use it for** one-off, agent-driven research in preflight and audits: keyword volumes, SERP and AI Overview snapshots, backlink pulls, prompt sampling. A typical call costs fractions of a cent to a few cents.

**Not a replacement** for an SEO suite: no dashboards, history or scheduled tracking. Ahrefs, Similarweb and Sistrix are not available, and Semrush works only with your own key.

**Alternative:** at steady high volume, go to the data providers (e.g. DataForSEO) directly.
