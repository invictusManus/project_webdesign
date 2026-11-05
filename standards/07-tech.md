# 07 · Technical foundation

**Why it matters:** The technical foundation decides speed, security, editability and how easily the site can change later. Most rules here are cheap at the start and expensive to retrofit. Guide: steps 9, 21 and 29.

Detail: `reference/google-search/` notes.

Scope: HTML/CSS/JS baseline, rendering, hosting, environments, domain, DNS, email, integrations (CMS, forms, APIs, third parties), installable web apps (PWA), CMS validation and editorial workflow, transactional and marketing email, maintenance and handover. Security headers and TLS: [`10-security-privacy.md`](10-security-privacy.md).

Last verified: 2026-11

## Markup, styles, scripts

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-01 | MUST | Every page starts with `<!doctype html>`, `<html lang="…">`, `<meta charset="utf-8">` within the first 1024 bytes, and `<meta name="viewport" content="width=device-width, initial-scale=1">`. Template: [`head.html`](../templates/head.html). | HTML validator |
| TEC-02 | MUST | HTML validates without errors, and every `id` is unique. `<head>` holds only `title`, `meta`, `link`, `script`, `style`, `base`, `noscript` and `template`: an `iframe` or `img` there makes Google ignore everything after it (canonical, hreflang). | Nu HTML Checker or html-validate in CI |
| TEC-03 | SHOULD | Reading, navigating and submitting forms work without JavaScript. Scripts only enhance. | Browser with JS disabled |
| TEC-04 | SHOULD | Styles use design tokens as CSS custom properties with low, flat specificity. No inline styles except critical CSS. | Code review; CSS linter |
| TEC-05 | MUST | Custom 404 and 500 pages return the correct status code and offer navigation plus links to key pages. | `curl -I` on a random URL |

## Rendering & architecture

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-06 | MUST | [house] Choose rendering per page type and document the choice in the site README. Default: static (prerendered). Server rendering only for per-request data. Client-only rendering only behind login. Dynamic rendering for bots is a discouraged workaround. | Site README; view source |
| TEC-28 | SHOULD | JavaScript-dependent content works in Google's renderer: feature-detect APIs (no WebGL, WebSockets or WebRTC without an HTTP fallback), no permission prompts, no reliance on cookies or Local/Session Storage across page loads. Light-DOM content in web components is projected with `<slot>`. | URL Inspection → rendered HTML and console |
| TEC-07 | SHOULD | Choose framework and CMS for editor needs, prerender/SSR support, team skills, hosting fit and long-term support. No page builder without clean code or content export. | Decision record in project brief |

## Hosting & delivery

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-08 | MUST | Hosting provides a CDN, HTTP/2 or HTTP/3, Brotli/gzip compression and automatically renewed TLS certificates. | `curl -I --http3`; response headers |
| TEC-09 | MUST | Deploys are atomic and can be rolled back in one step. Every change gets a preview deployment. | Run one rollback before launch |
| TEC-10 | MUST | [house] Environments are local → preview/staging → production. Staging requires authentication and sends `X-Robots-Tag: noindex`. It is never linked publicly. | `curl -I` on staging |
| TEC-11 | MUST | Secrets live in environment variables or a secret store, never in the repository or the client bundle. `.env*` is git-ignored. | Secret scan; inspect bundle |
| TEC-41 | MUST | The secret scan covers git history and build output. A secret that was committed, bundled, logged or put in a URL is rotated, not just deleted. Keys are scoped to least privilege. Credentials, session IDs and reset tokens never appear in URLs, logs, analytics or `Referer`. | History scan; grep logs and analytics URLs for `token=` and `key=` |
| TEC-12 | MUST | Content, database and uploads are backed up daily and kept ≥ 30 days off-site. A restore is tested before launch and once a year. | Restore protocol |
| TEC-42 | SHOULD | Backups and database exports are encrypted at rest, stored outside the web root with a named access list, and deletion requests and retention (PRV-06) reach them within the backup rotation. | Access-list review; restore test |
| TEC-29 | MUST | CDN, WAF and firewall let Google's crawlers through: no blocked Google IPs, DNS answers over UDP and TCP. Network timeouts, resets and DNS errors count as `5xx`, and URLs drop from the index within days. Claimed Googlebot traffic is verified by reverse+forward DNS or Google's published IP ranges, never by user agent alone. | URL Inspection live test; GSC Crawl stats; WAF logs |
| TEC-30 | SHOULD | Crawlers are throttled only with `503` or `429` (plus `Retry-After`) and for at most 1–2 days. A `4xx` other than `429` never reduces crawl rate, and `crawl-delay` is ignored. For a crawl spike, check access logs for facets and calendars first. | Access logs; GSC Crawl stats |
| TEC-31 | SHOULD | Planned downtime or closure keeps pages online and indexable: disable the cart, add a banner with `data-nosnippet`, update availability and opening-hours markup. A full shutdown of 1–2 days returns a static `503` with `Retry-After` (robots.txt stays `200`); never `403`/`404`/`410`, `noindex` or `Disallow: /`. Longer closures keep an indexable `200` placeholder. | `curl -I` during a drill |
| TEC-32 | SHOULD | A host or CDN change without URL changes is tested on a temporary hostname with `noindex`, checked with URL Inspection, keeps Search Console verification, drops temporary blocks, and keeps the old host until its traffic is zero. | Old vs. new server logs |
| TEC-33 | SHOULD | Responses send `ETag` (preferred by Google) or a valid HTTP-date `Last-Modified` and answer `If-None-Match`/`If-Modified-Since` with `304`. | `curl -I` twice |

## Domain, DNS, email

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-13 | MUST | The domain is registered in the site owner's name and account, with 2FA, auto-renew and registrar lock. Credentials live in a shared password vault. | Registrar account; WHOIS/RDAP |
| TEC-14 | SHOULD | A CAA record limits certificate issuers. DNSSEC is on where the registrar supports it. All name servers return the right A/CNAME records (changes take up to 72 h). Lower TTLs to a few hours or less at least 7 days before a DNS migration. | `dig CAA`; `dig` per name server; DNSSEC analyzer |
| TEC-15 | MUST | Every domain that sends email has SPF, DKIM and DMARC. Start DMARC at `p=none` with reports, then move to `quarantine` and `reject`. | MXToolbox; DMARC reports |
| TEC-16 | SHOULD | Transactional email (forms, orders) goes through a dedicated provider on its own subdomain, with aligned SPF/DKIM. | Header check of a test email |
| TEC-38 | SHOULD | Transactional emails (confirmations, orders, password resets): HTML plus a plain-text part, one column ≤ 600 px, live text instead of images, `lang` set, layout tables with `role="presentation"`, alt text, body text ≥ 16 px, absolute links with descriptive text, token colors that pass A11Y-07, and a logo that works in dark mode. The sender name is consistent and replies reach a monitored inbox. No marketing content or tracking without a legal basis (PRV-01). Tested in Gmail, Outlook and Apple Mail, light and dark. | Test sends; email client previews |
| TEC-39 | SHOULD | Marketing email follows Gmail's sender guidelines: aligned SPF, DKIM and DMARC (TEC-15), valid forward and reverse DNS, TLS, one-click unsubscribe (`List-Unsubscribe` with an HTTPS URI plus `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, both covered by DKIM, RFC 8058) and a visible unsubscribe link in the body, honored within 48 hours, and a user-reported spam rate below 0.3 % in Postmaster Tools (aim below 0.1 %). Gmail enforces the unsubscribe and DMARC parts for bulk senders (about 5,000 messages a day to Gmail); follow them at any volume. Consent per PRV-11. | Message headers; Postmaster Tools |

## Integrations

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-17 | MUST | Forms validate on the server and show clear success and error states. Delivery is confirmed by a test submission. | Test submission per form |
| TEC-18 | MUST | Spam protection without tracking: honeypot, time trap and rate limit first; a privacy-friendly challenge if spam persists, and from the start on open sign-up forms (accounts, user content). Never a puzzle-only CAPTCHA (see A11Y-20). | Bot test; a11y review |
| TEC-19 | MUST | The CMS content model has structured fields for title, meta description, slug, social image, alt text (required), author and dates, plus drafts, preview, versions and roles. | CMS schema review |
| TEC-20 | MUST | Every external script, embed, font or pixel is listed in the third-party inventory in [`project-brief.md`](../templates/project-brief.md): purpose, owner, consent category, data shared, performance cost, CSP origins. The default answer is no. | Inventory vs. network requests |
| TEC-21 | SHOULD | Map, social and secondary video embeds load as click-to-load placeholders until the user interacts or consents. Videos meant to rank (SEO-45) keep their player element in the HTML without user action (a click or consent gate is a user action): self-host with `<video>`, `poster` and `preload="none"`, or use an iframe with `loading="lazy"`. | Network panel before interaction; URL Inspection for ranking videos |
| TEC-22 | SHOULD | API calls run on the server with timeouts, retries with backoff, a fallback UI and failure monitoring. | Fault-injection test |

## CMS and editors

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-34 | MUST | The CMS enforces on publish: title, meta description and alt text, or an explicit "decorative" flag (SEO-58); slug rules (SEO-12); minimum image sizes (SEO-19). A slug change creates a 301 automatically (SEO-09). Rich text allows only semantic elements (H2–H4, lists, links, tables with headers); no raw HTML, inline styles or colors outside the tokens (DES-11). | Try to publish an incomplete page; change a slug |
| TEC-35 | SHOULD | Editorial workflow: roles with least privilege (author, editor, publisher, admin), an approval step for YMYL and legal pages (CON-11), scheduled publishing, and revision history with restore. Publishes feed the change log (MSR-26). | CMS roles review |
| TEC-36 | SHOULD | Editors build pages from library blocks (CMP-01) within constraints: section order per page type (LAY-14), one hero, one primary call to action (UX-06). Each block has help text and character limits that match its component's content limits. | Build a test page in the CMS |
| TEC-37 | SHOULD | Handover includes editor training (TEC-27): a short guide per content type, the style guide (CON-17), the AI-writing checklist (CON-16), and image preparation (formats, sizes, alt text). | Training record |
| TEC-40 | MUST | *(CMS)* Unpublished, scheduled, private and deleted content is absent from sitemaps, feeds, site search and CMS REST or GraphQL listings. A preview link opens one item only and needs login or an expiring unguessable token. Exports and backups download only for named roles. | Search sitemap, RSS, API (`?status=draft`) and site search for a known draft slug unauthenticated; reuse item A's preview token on item B |

## Installable web apps (PWA)

Rules marked *(PWA)* apply when the site should install to the home screen or desktop.

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-44 | MUST | *(PWA)* A web app manifest, linked from every page over HTTPS, sets `name`, `short_name`, `id`, `start_url`, `scope`, `display: standalone` (`fullscreen` only for games and kiosks, since it hides the status bar), `theme_color` and `background_color` from the tokens, and PNG icons at 192 and 512 px plus a 512 px `maskable` icon with its artwork inside the safe zone (DES-10). | DevTools → Application → Manifest: no errors or installability warnings |
| TEC-45 | MUST | *(PWA)* A service worker precaches the app shell and an offline fallback page, so the main screens open offline. HTML is network-first, hashed assets cache-first (PRF-17); private responses are never cached (SEC-40). Old caches are removed on activation, and a new version asks the user to reload instead of switching mid-session. | DevTools offline mode: main screens and the offline page load; Application → Service workers |
| TEC-46 | SHOULD | *(PWA)* Install prompt: an "Install app" button appears only where `beforeinstallprompt` fires (Chromium on Android and desktop), after the user has engaged, never on first load (UX-17). On iPhone and iPad, Safari shows short "Share → Add to Home Screen" instructions instead (Chrome and Edge on iOS can't install). All install UI is hidden when `display-mode` is `standalone`. | Test on Android Chrome, iOS Safari and desktop Chrome |
| TEC-47 | SHOULD | *(PWA)* In standalone mode the app replaces the missing browser bar: visible back navigation, share where useful, safe-area padding (LAY-09). Android builds the splash screen from `name`, `background_color` and the icon; iOS uses the apple-touch icon (DES-10). Push notifications are asked for only after a user action, in context (on iOS only for apps added to the home screen). | Device test in standalone mode on iOS and Android |
| TEC-48 | SHOULD | *(PWA)* Installability is tested in Chrome DevTools (Application panel) and on real devices. Lighthouse no longer audits PWAs: its PWA category was removed in version 12. | DevTools Application panel; device test |

## Code quality, maintenance, handover

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-23 | SHOULD | Code is in version control with a protected main branch, reviewed pull requests and CI on every pull request ([`ci/quality.yml`](../templates/ci/quality.yml)). | Repository settings |
| TEC-24 | SHOULD | Use a formatter and a linter with default settings, one package manager, a lockfile (SEC-14) and `.editorconfig`. | CI lint step |
| TEC-43 | SHOULD | Code comments explain why, not what: no banner or separator comments, step narration (`// Step 1`), end-of-block markers, doc blocks that only repeat the signature, or emoji; every `TODO` names an owner or issue. | Grep; lint step (TEC-24) |
| TEC-25 | MUST | No end-of-life runtime, framework, CMS or plugin in production. Dependency updates are automated and merged at least monthly. | Update bot dashboard; endoflife.date |
| TEC-26 | SHOULD | The site repository has a README (run, build, deploy, rollback, owners) and an `AGENTS.md` ([template](../templates/AGENTS.md)). | Repository |
| TEC-27 | SHOULD | Handover package: who has access to what, credentials in the vault, runbook, and licenses for fonts, images and code. | Handover sign-off |

## Sources

- [web.dev: Install criteria](https://web.dev/articles/install-criteria) · [Installation prompt](https://web.dev/learn/pwa/installation-prompt) · [Maskable icons](https://web.dev/articles/maskable-icon) · [MDN: Making PWAs installable](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable) · [MDN: display](https://developer.mozilla.org/en-US/docs/Web/Manifest/Reference/display)
- [Chrome: Updated install criteria](https://developer.chrome.com/blog/update-install-criteria) · [DevTools: Debug PWAs](https://developer.chrome.com/docs/devtools/progressive-web-apps) · [Lighthouse 12.0 release notes](https://github.com/GoogleChrome/lighthouse/releases/tag/v12.0.0) · [WebKit: Web Push for web apps on iOS](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/)
- [PEP 8: Comments](https://peps.python.org/pep-0008/#comments) · [Google Python Style Guide: Comments](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Google: Email sender guidelines](https://support.google.com/mail/answer/81126) · [Sender guidelines FAQ](https://support.google.com/a/answer/14229414) · [RFC 8058: One-click unsubscribe](https://www.rfc-editor.org/rfc/rfc8058)
- [MDN: Webpage metadata](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Webpage_metadata) · [WHATWG HTML](https://html.spec.whatwg.org/)
- [web.dev: Rendering on the web](https://web.dev/articles/rendering-on-the-web)
- [RFC 9989 DMARC](https://www.rfc-editor.org/rfc/rfc9989) (obsoletes RFC 7489) · [Google: Video best practices](https://developers.google.com/search/docs/appearance/video)
- [RFC 8659 CAA](https://www.rfc-editor.org/rfc/rfc8659)
- [Google: Valid page metadata](https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata) · [Fix JavaScript issues](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript) · [Dynamic rendering](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering)
- [Google: Reduce crawl rate](https://developers.google.com/crawling/docs/crawlers-fetchers/reduce-crawl-rate) · [Verify Google requests](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests) · [DNS and network errors](https://developers.google.com/crawling/docs/troubleshooting/dns-network-errors) · [Crawler overview (caching)](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers)
- [Google: Pause an online business](https://developers.google.com/search/docs/crawling-indexing/pause-online-business) · [Site move without URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
