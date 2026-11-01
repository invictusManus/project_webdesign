# 10 · Security, privacy & legal

**Why it matters:** Security protects visitors and the site from abuse; privacy law decides what you may collect and how. In the EU, mistakes here lead to fines and warning letters. Guide: steps 10, 27 and 28.

Detail: `reference/google-search/` notes.

Scope: transport security, headers, application security (OWASP Top 10:2025), supply chain, privacy (GDPR, TDDDG), consent, legal pages, AI transparency. Rules tagged [EU] are requirements, not legal advice.

Last verified: 2026-10

## Transport & headers

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEC-01 | MUST | HTTPS only. TLS 1.3 is enabled, TLS 1.2 (ECDHE suites) is the minimum, and SSL, TLS 1.0 and TLS 1.1 are off. | SSL Labs grade A |
| SEC-02 | MUST | `Strict-Transport-Security: max-age=63072000; includeSubDomains`, once every subdomain serves HTTPS. | `curl -I` |
| SEC-03 | MUST | Baseline headers: `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, a `Permissions-Policy` that denies unused features, `Cross-Origin-Opener-Policy: same-origin`, and `X-Frame-Options: DENY` for legacy browsers. Template: [`_headers`](../templates/_headers). | MDN HTTP Observatory (target A) |
| SEC-04 | MUST | Send `Content-Security-Policy` as an HTTP header, not `<meta>`. Minimum: `default-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'; upgrade-insecure-requests`. Roll it out with `Content-Security-Policy-Report-Only` first. | Observatory; browser console |
| SEC-05 | SHOULD | Strict script CSP: nonces or hashes plus `'strict-dynamic'`. No `'unsafe-inline'` or `'unsafe-eval'` for scripts. Violations are reported via `report-to`. | CSP Evaluator |
| SEC-06 | SHOULD | Hide server version and `X-Powered-By`. Don't send `X-XSS-Protection` (obsolete). No public directory listings, `.git`, `.env`, backups or private source maps. | Observatory; probe the paths |
| SEC-07 | COULD | Add the domain to the HSTS preload list. Use COEP `require-corp` and CORP `same-origin` where no cross-origin embeds are needed. | hstspreload.org |

## Application

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEC-08 | MUST | Cookies are `Secure`, `HttpOnly` unless scripts must read them, and `SameSite=Lax` or `Strict`. Session cookies use the `__Host-` prefix and a short lifetime. | DevTools → Application → Cookies |
| SEC-09 | MUST | No `eval` or `new Function`. Untrusted data never goes into `innerHTML` or `document.write`. Output is encoded for its context with the framework's escaping. | Code review; linter |
| SEC-10 | MUST | Every form and API validates input on the server and uses parameterized queries. Uploads are checked against an allowlist of type and size, stored outside the web root, and SVG is denied by default. | Code review; DAST scan |
| SEC-11 | MUST | Access control runs on the server for every request and action. Admin and CMS logins require MFA and are rate-limited. No default credentials. | Manual test; DAST |
| SEC-12 | MUST | State-changing requests are protected against CSRF (SameSite cookies plus a token for authenticated actions) and are rate-limited. | DAST; manual |
| SEC-13 | MUST | If the site has user accounts, follow NIST SP 800-63B-4: passwords ≥ 15 characters without MFA or ≥ 8 with MFA, maximum ≥ 64, no composition rules, no forced rotation. Check against breached-password lists, hash with Argon2id, give generic login errors and offer MFA. | Auth review |
| SEC-14 | MUST | Supply chain (OWASP A03): committed lockfile, frozen installs in CI, dependency vulnerability scan and secret scan in CI, 2FA on Git, registry, hosting and DNS accounts. | CI logs; account settings |
| SEC-15 | MUST | Critical security patches for CMS, plugins and runtime ship within 48 hours, all others within 7 days. Every CMS, plugin, forum and blog (even forgotten ones) is inventoried with its version. Servers are reached by SSH/SFTP, never FTP or telnet. | Patch log; software inventory |
| SEC-16 | SHOULD | Third-party scripts are self-hosted or pinned with Subresource Integrity. | Source review |
| SEC-17 | SHOULD | Errors fail closed and never expose stack traces. Security events (logins, admin changes) are logged without unnecessary personal data and alert on anomalies. | Error page test; log review |
| SEC-18 | SHOULD | Publish `/.well-known/security.txt` (RFC 9116) with `Contact` and an `Expires` date less than a year ahead. Template: [`security.txt`](../templates/security.txt). | Fetch the file |
| SEC-19 | SHOULD | Before launch, a DAST baseline scan (e.g. ZAP) shows no high-risk findings. | Scan report |
| SEC-20 | SHOULD | Hack detection: Search Console messages are forwarded to a monitored mailbox, the Security issues and Manual actions reports stay clean, and `site:example.com` plus spam terms (e.g. `casino`) is checked monthly for injected pages. Logs are watched for open-redirect abuse (`=http:` or `=//` parameters, spikes on redirect URLs). | GSC Security issues; `site:` query; log review |
| SEC-21 | SHOULD | Incident runbook for a flagged site: review the Search Console owner list for unknown owners, open the flagged sample URLs from a machine outside the site's network and refresh several times, fix every cause, then request one review. Never toggle between clean and compromised states (Safe Browsing Repeat Offenders get no review requests for 30 days). | Tabletop exercise; GSC Security issues |
| SEC-22 | SHOULD | Embedded ads and third-party components are vetted: deceptive ads or pop-up redirects count against the host page. Hosted payment, booking or login pages run by a third party show that party's brand on every page and state the relationship (social-engineering flag). | Security issues report; page review |

## Privacy & consent

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRV-01 | MUST | [EU] Before consent, nothing non-essential is stored on or read from the device (cookies, storage, fingerprinting), and no third-party request sends personal data (TDDDG §25, GDPR). | Fresh profile: network and storage before consent |
| PRV-02 | MUST | [EU] The consent banner shows accept and reject with equal prominence on the first layer. Purposes are granular, nothing is pre-ticked, there is no consent wall, withdrawal is as easy as consent (persistent link), and consent is logged. | Banner review against the DSK guidance |
| PRV-03 | MUST | Google tags run only with Consent Mode v2: `ad_storage`, `analytics_storage`, `ad_user_data` and `ad_personalization` default to `denied` before any tag fires, and the CMP updates them. Sites showing Google ads need a Google-certified CMP. Template: [`consent-default.html`](../templates/consent-default.html). | Tag Assistant; network before consent |
| PRV-04 | MUST | [EU] A privacy policy is linked from every page. It names the controller, the DPO if required, purposes and legal bases, every recipient, third-country transfers and their safeguards, retention periods, data subject rights and the right to complain. | Policy vs. third-party inventory (TEC-20) |
| PRV-05 | MUST | [EU] Every processor (hosting, analytics, forms, email, CMP) has a data processing agreement (Art. 28 GDPR). US recipients must be certified under the EU-US Data Privacy Framework or covered by standard contractual clauses plus a transfer impact assessment. | Contract register |
| PRV-06 | MUST | Collect only the data each purpose needs. Retention periods are defined and enforced automatically. Logs are anonymized or short-lived. | Retention config |
| PRV-07 | SHOULD | Privacy-friendly defaults: fonts per PRF-10, click-to-load embeds (TEC-21), and cookieless analytics where it suffices. Whether consent is still needed is assessed legally. | Network panel |
| PRV-08 | SHOULD | [EU] Keep a record of processing activities (Art. 30). Run a DPIA where required. Have a breach process that can notify within 72 hours. | Documentation |
| PRV-09 | COULD | Outside the EU: honor Global Privacy Control. Add a CCPA/CPRA "Do Not Sell or Share" link if in scope. UK GDPR/PECR mirror the EU rules. Check local law for each target market. | Legal review per market |

## Legal pages & duties

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRV-10 | MUST | [EU] Germany: an Impressum per DDG §5, labelled "Impressum" and reachable from every page. It gives name and address, legal form and representatives, email plus another fast contact, register and number, VAT ID, and the supervisory authority, chamber and professional rules for regulated professions. | Footer link; content check |
| PRV-11 | MUST | Newsletters use double opt-in, keep a consent record (time and text version) and include an unsubscribe link in every email. | Test subscription |
| PRV-12 | MUST | [EU] E-commerce must provide: pre-contract information, withdrawal policy, total prices including VAT and shipping (PAngV), an order button labelled "zahlungspflichtig bestellen" or equivalent (§312j BGB), a cancellation button for B2C subscriptions (§312k BGB) and a consumer-arbitration statement (VSBG §36). The EU ODR-platform link is no longer required since 20 Jul 2025. | Checkout review |
| PRV-13 | MUST | [EU] AI Act Art. 50 (applies since 2 Aug 2026): tell users when they are talking to an AI system. Label AI-generated or manipulated images, audio and video (deepfakes), and AI-generated text published to inform the public unless it was human-reviewed under editorial responsibility. | Chatbot UI; media labels |

## Sources

- [OWASP Top 10:2025](https://owasp.org/Top10/) · [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) · [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [MDN: HTTP security headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers) · [MDN HTTP Observatory](https://developer.mozilla.org/en-US/observatory)
- [BSI TR-02102-2 (TLS)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102-2.html) · [RFC 9116 security.txt](https://www.rfc-editor.org/rfc/rfc9116)
- [Google: Prevent malware](https://developers.google.com/search/docs/monitor-debug/security/prevent-malware) · [Social engineering](https://developers.google.com/search/docs/monitor-debug/security/social-engineering) · [Repeat Offenders](https://developers.google.com/search/docs/monitor-debug/security/safe-browsing-repeat-offenders) · [`site:` operator](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site)
- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [TDDDG §25](https://www.gesetze-im-internet.de/ttdsg/__25.html) · [DSK Orientierungshilfe Digitale Dienste](https://www.datenschutzkonferenz-online.de/media/oh/OH_Digitale_Dienste.pdf)
- [Google: Consent mode](https://developers.google.com/tag-platform/security/guides/consent) · [Google CMP partner program](https://cmppartnerprogram.withgoogle.com/)
- [DDG §5 Impressum](https://www.gesetze-im-internet.de/ddg/__5.html) · [§312j BGB](https://www.gesetze-im-internet.de/bgb/__312j.html) · [§312k BGB](https://www.gesetze-im-internet.de/bgb/__312k.html) · [VSBG §36](https://www.gesetze-im-internet.de/vsbg/__36.html)
- [Regulation (EU) 2024/1689 (AI Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) · [Regulation (EU) 2024/3228 (ODR repeal)](https://eur-lex.europa.eu/eli/reg/2024/3228/oj)
