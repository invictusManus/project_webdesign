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

## Server code, APIs and accounts

Rules marked *(…)* apply only when the site has that feature.

| ID | Level | Rule | Verify |
|---|---|---|---|
| SEC-23 | MUST | *(server fetches)* Server-side fetches of user-influenced URLs (link previews, imports, webhook targets) allow only `https` to allowlisted hosts, block loopback, private and link-local ranges (incl. `169.254.169.254` and IPv6) after DNS resolution, re-check every redirect hop and cap time and size. | Submit `http://127.0.0.1`, the metadata IP, a name resolving to `10.0.0.1` and redirects to each: all rejected |
| SEC-24 | MUST | Redirect targets from `next`, `return` or `url` parameters are relative paths or exact allowlisted hosts; `//`, `\`, `javascript:` and foreign URLs are rejected. CR/LF from request data never reaches a response header. | `?next=//evil.example`, `/\evil.example`, `%0d%0aSet-Cookie:x`: no off-site `Location`, no injected header |
| SEC-25 | MUST | *(CORS)* `Access-Control-Allow-Origin` is an exact allowlist, never reflected from `Origin` and never `null`. Credentials only with one named origin; per-user responses never use `*`; dynamic values send `Vary: Origin`. | `curl -sI -H 'Origin: https://evil.example'` and `Origin: null` per API route: no ACAO |
| SEC-26 | MUST | *(files)* Paths built from request data are canonicalized and confined to a base directory; stored files get server-generated names; archive extraction rejects entries outside the target. | `?file=../../etc/passwd`, `%2e%2e%2f`, a zip with `../x`: rejected |
| SEC-27 | MUST | *(uploads)* Extends SEC-10: type is detected from the file's bytes, not its name or `Content-Type`. Uploads are served with `nosniff` and `Content-Disposition: attachment` or from a separate cookieless origin; images are re-encoded with pixel and decompressed-size limits. | Upload HTML renamed `.jpg`, `shell.php.jpg`, a 50,000 × 50,000 px PNG: none renders inline or runs, the large image is refused |
| SEC-28 | MUST | Request data never reaches a shell, template compiler, XML parser with external entities or a native deserializer (`unserialize`, `pickle`). Subprocesses take argument arrays; NoSQL and LDAP filters are built from typed fields. | SAST plus review; `;id`, `{{7*7}}` and an XXE document stay inert |
| SEC-29 | MUST | Absolute URLs in emails, redirects, canonicals and sitemaps come from a configured base URL, never from `Host`, `X-Forwarded-Host` or `Forwarded`. The app answers only for its own hostnames. | `curl -H 'Host: evil.example'` and `X-Forwarded-Host` on pages, redirects and the reset email: value absent or rejected |
| SEC-30 | MUST | *(accounts, personalized pages)* Per-user responses send `Cache-Control: private, no-store`. The CDN cache key includes every input that changes the response; static-asset rules never match dynamic paths (`/account/x.css`, `/account;a.js`). Public pages keep PRF-16. | Logged in, request those paths; fetch anonymously elsewhere: no private content, no cache HIT |
| SEC-31 | MUST | *(accounts)* A new session ID on login, privilege change and MFA; sessions invalidated server-side on logout, password change and account disable; IDs from a CSPRNG with ≥ 64 bits of entropy; idle and absolute timeouts; logout clears client-side private data. | Cookie changes after login; the old cookie returns 401 after logout or password change |
| SEC-32 | MUST | *(accounts)* Reset, invite, email-change and magic-link tokens are random, single-use, short-lived, bound to one account and action, and stored hashed. A reset revokes other sessions. Login, reset and sign-up answer identically, in content and timing, for known and unknown accounts. | Reuse, expiry and cross-account tests; compare responses for a known vs. unknown email |
| SEC-33 | MUST | *(JWT, OAuth, OIDC)* The server pins the JWT algorithm and key source and checks `iss`, `aud` and `exp`; header-chosen `jku`/`kid` are not trusted. Clients bind `state` and PKCE to the session and check the ID-token `nonce`; `redirect_uri` matches exactly. | `alg=none`, wrong `aud`, expired token, foreign `state`, `redirect_uri` variant: all rejected |
| SEC-34 | MUST | Extends SEC-11: every route that takes an object ID checks the caller's right to that object (read, update, delete, list, export, bulk, file download). Writes accept an allowlist of fields, so `role`, `owner`, `price` and `status` can't be set from the request. | As user A, request user B's IDs on every verb; send `role=admin`: 403/404, nothing changes |
| SEC-35 | MUST | *(webhooks)* Inbound webhooks verify the provider's signature over the raw body with a constant-time compare and a timestamp tolerance, reject replayed event IDs, and take account and event type only from the verified payload. | Unsigned, wrongly signed, stale and replayed posts: 4xx, no side effect |
| SEC-36 | MUST | Production has debug mode off with no switch via parameter or header. Unauthenticated `/debug`, `/phpinfo.php`, `/server-status`, `/actuator`, `/metrics`, GraphQL introspection (unless public) and CMS user-listing endpoints return 401, 403 or 404; seed and sample accounts are removed. | Probe the list on production; try `?debug=1` |
| SEC-37 | MUST | Extends SEC-09: user or CMS HTML is sanitized with an allowlist sanitizer on output (Trusted Types where supported). `href`, `src`, `location` and `window.open` values from requests, fragments or storage are `https:`, `mailto:` or relative, never `javascript:` or `data:`. | Submit `<img src=x onerror=…>` and a `javascript:` link: both render inert |
| SEC-38 | MUST | *(postMessage, WebSockets)* Message handlers check `event.origin` against an exact allowlist; sensitive messages never target `"*"`. WebSocket upgrades check `Origin`, authenticate with a per-connection token (not cookies alone) and re-authorize each message. | Post from an unlisted origin; connect with `Origin: https://evil.example`: ignored or 403 |
| SEC-39 | SHOULD | Recursive merge or path-assign on request data rejects `__proto__`, `constructor` and `prototype`, or uses `Map`/`Object.create(null)`. | Send `{"__proto__":{"x":1}}`; `({}).x` stays undefined |
| SEC-40 | SHOULD | *(service worker)* The worker is same-origin at the narrowest scope and never caches responses with `Authorization`, `Set-Cookie`, `private` or `no-store`; logout and account switches purge its caches. | DevTools → Application → Cache Storage after login, logout and switch |
| SEC-41 | SHOULD | Request body size is capped (≤ 1 MB by default, uploads per SEC-10), list endpoints cap `limit` and query depth, every server-side call has a timeout, user-supplied regexes never run, and limits apply before expensive work. | 10 MB body → 413; `?limit=100000` capped; a ReDoS probe stays fast |
| SEC-42 | SHOULD | CI hardening: workflows running pull-request code get `contents: read` and no secrets; no PR checkout under `pull_request_target` or `workflow_run` with secrets; third-party actions pinned to a full commit SHA; event fields (branch, title) never interpolated into `run:`; no unpinned `curl \| sh` or `npx` without a version. | Workflow review or linter |
| SEC-43 | SHOULD | Dependency confusion and install scripts: scoped internal package names, the registry pinned in a committed `.npmrc`, install scripts of new dependencies reviewed or CI on `npm ci --ignore-scripts`, lockfile integrity verified. Extends SEC-14. | Registry config and CI install step review |
| SEC-44 | COULD | *(accounts)* Fetch Metadata: authenticated apps reject non-navigation requests with `Sec-Fetch-Site: cross-site` as defense in depth against CSRF and cross-site leaks. | `curl -X POST -H 'Sec-Fetch-Site: cross-site'` → 403 |
| SEC-45 | MUST | Origin servers, databases, admin panels and management ports are unreachable from the internet except through the CDN or WAF, an allowlist or a VPN; requests that bypass the CDN are refused. | Port scan of the own origin (with approval): only 80/443; `curl --resolve host:443:<origin-ip>` refused |
| SEC-46 | MUST | *(shop, forms with prices)* The server recomputes price, discount, shipping, tax and totals from catalog data and ignores client-sent prices, roles and currencies; negative, zero or fractional quantities are rejected; orders, coupons and sign-ups are atomic, and steps can't be skipped. | Tamper price and `qty=-1`; 20 parallel coupon redeems → one success; open the confirmation URL directly |

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

- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): [SSRF](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) · [Unvalidated redirects](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) · [File upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) · [Injection](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html) · [Deserialization](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html) · [Session management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) · [Forgot password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) · [Mass assignment](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html) · [DOM XSS](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) · [Prototype pollution](https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html) · [Denial of service](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html) · [CI/CD security](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html) · [NPM security](https://cheatsheetseries.owasp.org/cheatsheets/NPM_Security_Cheat_Sheet.html) · [Secrets management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [OWASP API Security Top 10 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) · [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/) (CORS, Host header, web messaging, WebSockets, business logic)
- [RFC 8725: JWT best practices](https://www.rfc-editor.org/rfc/rfc8725) · [RFC 9700: OAuth 2.0 security BCP](https://www.rfc-editor.org/rfc/rfc9700) · [RFC 9111: HTTP caching](https://www.rfc-editor.org/rfc/rfc9111) · [RFC 6455: WebSocket](https://www.rfc-editor.org/rfc/rfc6455) · [W3C Fetch Metadata](https://www.w3.org/TR/fetch-metadata/) · [W3C Service Workers](https://www.w3.org/TR/service-workers/)
- [GitHub: Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) · [NIST SP 800-123: Server security](https://csrc.nist.gov/pubs/sp/800/123/final)

- [OWASP Top 10:2025](https://owasp.org/Top10/) · [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) · [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [MDN: HTTP security headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers) · [MDN HTTP Observatory](https://developer.mozilla.org/en-US/observatory)
- [BSI TR-02102-2 (TLS)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102-2.html) · [RFC 9116 security.txt](https://www.rfc-editor.org/rfc/rfc9116)
- [Google: Prevent malware](https://developers.google.com/search/docs/monitor-debug/security/prevent-malware) · [Social engineering](https://developers.google.com/search/docs/monitor-debug/security/social-engineering) · [Repeat Offenders](https://developers.google.com/search/docs/monitor-debug/security/safe-browsing-repeat-offenders) · [`site:` operator](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site)
- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [TDDDG §25](https://www.gesetze-im-internet.de/ttdsg/__25.html) · [DSK Orientierungshilfe Digitale Dienste](https://www.datenschutzkonferenz-online.de/media/oh/OH_Digitale_Dienste.pdf)
- [Google: Consent mode](https://developers.google.com/tag-platform/security/guides/consent) · [Google CMP partner program](https://cmppartnerprogram.withgoogle.com/)
- [DDG §5 Impressum](https://www.gesetze-im-internet.de/ddg/__5.html) · [§312j BGB](https://www.gesetze-im-internet.de/bgb/__312j.html) · [§312k BGB](https://www.gesetze-im-internet.de/bgb/__312k.html) · [VSBG §36](https://www.gesetze-im-internet.de/vsbg/__36.html)
- [Regulation (EU) 2024/1689 (AI Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) · [Regulation (EU) 2024/3228 (ODR repeal)](https://eur-lex.europa.eu/eli/reg/2024/3228/oj)
