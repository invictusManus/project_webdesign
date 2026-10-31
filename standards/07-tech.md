# 07 · Technical foundation

Scope: HTML/CSS/JS baseline, rendering, hosting, environments, domain, DNS, email, integrations (CMS, forms, APIs, third parties), maintenance and handover. Security headers and TLS: [`10-security-privacy.md`](10-security-privacy.md).

Last verified: 2026-10

## Markup, styles, scripts

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-01 | MUST | Every page starts with `<!doctype html>`, `<html lang="…">`, `<meta charset="utf-8">` within the first 1024 bytes, and `<meta name="viewport" content="width=device-width, initial-scale=1">`. Template: [`head.html`](../templates/head.html). | HTML validator |
| TEC-02 | MUST | HTML validates without errors, and every `id` is unique. | Nu HTML Checker or html-validate in CI |
| TEC-03 | SHOULD | Reading, navigating and submitting forms work without JavaScript. Scripts only enhance. | Browser with JS disabled |
| TEC-04 | SHOULD | Styles use design tokens as CSS custom properties with low, flat specificity. No inline styles except critical CSS. | Code review; CSS linter |
| TEC-05 | MUST | Custom 404 and 500 pages return the correct status code and offer navigation plus links to key pages. | `curl -I` on a random URL |

## Rendering & architecture

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-06 | MUST | Choose rendering per page type and document the choice in the site README. Default: static (prerendered). Server rendering only for per-request data. Client-only rendering only behind login. | Site README; view source |
| TEC-07 | SHOULD | Choose framework and CMS for editor needs, prerender/SSR support, team skills, hosting fit and long-term support. No page builder without clean code or content export. | Decision record in project brief |

## Hosting & delivery

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-08 | MUST | Hosting provides a CDN, HTTP/2 or HTTP/3, Brotli/gzip compression and automatically renewed TLS certificates. | `curl -I --http3`; response headers |
| TEC-09 | MUST | Deploys are atomic and can be rolled back in one step. Every change gets a preview deployment. | Run one rollback before launch |
| TEC-10 | MUST | Environments are local → preview/staging → production. Staging requires authentication and sends `X-Robots-Tag: noindex`. It is never linked publicly. | `curl -I` on staging |
| TEC-11 | MUST | Secrets live in environment variables or a secret store, never in the repository or the client bundle. `.env*` is git-ignored. | Secret scan; inspect bundle |
| TEC-12 | MUST | Content, database and uploads are backed up daily and kept ≥ 30 days off-site. A restore is tested before launch and once a year. | Restore protocol |

## Domain, DNS, email

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-13 | MUST | The domain is registered in the site owner's name and account, with 2FA, auto-renew and registrar lock. Credentials live in a shared password vault. | Registrar account; WHOIS/RDAP |
| TEC-14 | SHOULD | A CAA record limits certificate issuers. DNSSEC is on where the registrar supports it. Lower TTLs to ≤ 300 s 48 h before a DNS migration. | `dig CAA`; DNSSEC analyzer |
| TEC-15 | MUST | Every domain that sends email has SPF, DKIM and DMARC. Start DMARC at `p=none` with reports, then move to `quarantine` and `reject`. | MXToolbox; DMARC reports |
| TEC-16 | SHOULD | Transactional email (forms, orders) goes through a dedicated provider on its own subdomain, with aligned SPF/DKIM. | Header check of a test email |

## Integrations

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-17 | MUST | Forms validate on the server and show clear success and error states. Delivery is confirmed by a test submission. | Test submission per form |
| TEC-18 | MUST | Spam protection without tracking: honeypot, time trap and rate limit first; a privacy-friendly challenge only if spam persists. Never a puzzle-only CAPTCHA (see A11Y-20). | Bot test; a11y review |
| TEC-19 | MUST | The CMS content model has structured fields for title, meta description, slug, social image, alt text (required), author and dates, plus drafts, preview, versions and roles. | CMS schema review |
| TEC-20 | MUST | Every external script, embed, font or pixel is listed in the third-party inventory in [`project-brief.md`](../templates/project-brief.md): purpose, owner, consent category, data shared, performance cost, CSP origins. The default answer is no. | Inventory vs. network requests |
| TEC-21 | SHOULD | Video, map and social embeds load as click-to-load placeholders until the user interacts or consents. | Network panel before interaction |
| TEC-22 | SHOULD | API calls run on the server with timeouts, retries with backoff, a fallback UI and failure monitoring. | Fault-injection test |

## Code quality, maintenance, handover

| ID | Level | Rule | Verify |
|---|---|---|---|
| TEC-23 | SHOULD | Code is in version control with a protected main branch, reviewed pull requests and CI on every pull request ([`ci/quality.yml`](../templates/ci/quality.yml)). | Repository settings |
| TEC-24 | SHOULD | Use a formatter and a linter with default settings, one package manager, a lockfile (SEC-14) and `.editorconfig`. | CI lint step |
| TEC-25 | MUST | No end-of-life runtime, framework, CMS or plugin in production. Dependency updates are automated and merged at least monthly. | Update bot dashboard; endoflife.date |
| TEC-26 | SHOULD | The site repository has a README (run, build, deploy, rollback, owners) and an `AGENTS.md` ([template](../templates/AGENTS.md)). | Repository |
| TEC-27 | SHOULD | Handover package: who has access to what, credentials in the vault, runbook, and licenses for fonts, images and code. | Handover sign-off |

## Sources

- [MDN: Webpage metadata](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Webpage_metadata) · [WHATWG HTML](https://html.spec.whatwg.org/)
- [web.dev: Rendering on the web](https://web.dev/articles/rendering-on-the-web)
- [Google: Email sender guidelines](https://support.google.com/a/answer/81126) · [RFC 7489 DMARC](https://www.rfc-editor.org/rfc/rfc7489)
- [RFC 8659 CAA](https://www.rfc-editor.org/rfc/rfc8659)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
