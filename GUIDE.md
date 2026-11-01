# Website 101: from zero to launch to growth

This guide walks you through building a professional website, in the order a real project runs. Each step explains **why** it matters, **what to do**, and when it is **done**. "Done" points to rule IDs in [`standards/`](standards/); the rule itself holds the exact threshold and how to check it. For search topics, the rules follow Google's own documentation, condensed in [`reference/google-search/`](reference/google-search/README.md). Unfamiliar terms are explained in [`GLOSSARY.md`](GLOSSARY.md).

You don't need every step on day one. Make every **MUST** rule pass before launch, then work through the **SHOULD** rules, and add **COULD** rules once the basics hold. Small sites can treat several steps as a five-minute decision.

---

## 0 · How a website works (primer)

1. **A visitor types your domain.** DNS translates it into a server address. A CDN serves your pages from a location near the visitor.
2. **The server answers over HTTPS** with HTML (structure and content), CSS (looks) and JavaScript (behavior). The browser assembles the page.
3. **Search engines work the same way, at scale.** They *crawl* (fetch pages by following links), *render* (run the page like a browser), *index* (store what each page is about) and *rank* (order results for each search).
4. **AI assistants** (Google AI Overviews, ChatGPT, Perplexity, Copilot) mostly retrieve from these same indexes and cite the pages they use. A page that can't be crawled and indexed can't be cited either.
5. **A "good" website is**: useful to a defined audience, fast, usable by everyone, secure, findable, measurable and legally compliant. Each of these has its own standard.

---

## Phase 1 · Plan

Most website failures are planning failures: the wrong audience, an unclear offer, or pages nobody searches for. Fill in [`project-brief.md`](templates/project-brief.md) as you go.

**Step 1 · Define goals and the one action that matters.**
- Why: without a measurable goal you can't make design decisions or prove success.
- Do: write 1–3 business goals. Turn each into a KPI with a baseline and a target, and define the primary action per page type (call, quote request, purchase, sign-up).
- Done: STR-01, MSR-06.

**Step 2 · Understand your audience.**
- Why: visitors decide in seconds whether a page is for them. That only works if you speak to their real problem in their words.
- Do: talk to customers, read reviews and support tickets, look at search queries. For each audience, note the job they want done, what triggers the search, their objections and how they decide.
- Done: STR-02.

**Step 3 · Position the offer.**
- Why: a clear positioning statement becomes your homepage headline, your elevator pitch and how search engines and AI describe you.
- Do: complete the statement in the brief, and reuse the exact wording everywhere.
- Done: STR-03, GEO-05.

**Step 4 · Study competitors and the search results.**
- Why: you compete with whoever ranks for your topics, not only with your business rivals.
- Do: Google your core topics. List who ranks and what kind of page wins (guide, list, tool, product page, map pack), and whether an AI Overview appears. Note what each competitor does well and what they miss.
- Done: STR-04, STR-06, STR-07.

**Step 5 · Research keywords and map them to pages.**
- Why: each page should answer one clear need. Two pages chasing the same need compete with each other.
- Do: collect search queries with volume and intent, group them into topics, and assign each group to exactly one URL in [`url-map.csv`](templates/url-map.csv). Prioritize by business value and effort.
- Done: STR-05, STR-09, CON-01.

**Step 6 · Pick the site type.**
- Why: a shop, a SaaS product and a local service business need different things.
- Do: choose a profile in [`site-types.md`](standards/site-types.md) and apply its raised and relaxed rules.
- Done: STR-08.

**Step 7 · Plan structure and navigation.**
- Why: if people (and crawlers) can't find a page, it doesn't exist.
- Do: turn `url-map.csv` into a shallow tree. Use at most 7 top-level menu items, labelled in your visitors' words. Test the labels with a few real users.
- Done: UX-01, UX-02.

**Step 8 · Set up accounts, owned by the client.**
- Why: an agency or ex-employee holding the domain or analytics account is a common, expensive disaster.
- Do: register the domain, hosting, Git, CMS, Search Console, analytics and consent tool in the site owner's name. Turn on 2FA and store every login in a shared vault.
- Done: TEC-13, MSR-01, MSR-04 (see [`1-preflight.md`](checklists/1-preflight.md) § C).

**Step 9 · Make the technical decisions.**
- Why: rendering and platform choices are hard to undo, and they decide speed and SEO.
- Do: render pages statically by default, render on the server only for per-request data, and render client-side only behind a login. Pick the framework or CMS your editors can actually use. Start a third-party inventory whose default answer is "no".
- Done: TEC-06, TEC-07, TEC-20.

**Step 10 · Clarify the legal side.**
- Why: in the EU, missing legal pages or a wrong cookie banner can lead to fines and warning letters.
- Do: decide who writes the privacy policy and Impressum. Check whether accessibility law applies (online shops usually), whether you sell online (extra duties) and whether you use AI features (disclosure).
- Done: PRV-04, PRV-10, PRV-12, PRV-13, A11Y-02.

---

## Phase 2 · Design

Design is how the site earns trust in the first seconds. Consistency comes from a system, not from individual pages.

**Step 11 · Write the brand spec.**
- Why: one written source keeps designers, developers, writers and AI agents consistent.
- Do: fill in [`DESIGN.md`](templates/DESIGN.md): personality, voice, logo use, color roles, type, imagery, glossary.
- Done: DES-01.

**Step 12 · Turn the brand into design tokens.**
- Why: tokens are named values (e.g. `color.action.primary`). Change one, and every button updates; nobody improvises a new blue.
- Do: start from [`tokens.json`](templates/tokens.json): primitive values, then semantic roles, then components. Check that every text color pair passes contrast.
- Done: DES-02, DES-03, DES-04.

**Step 13 · Design mobile first, with reusable components.**
- Why: most visits are on phones, and Google indexes the mobile version.
- Do: design at 360 px first, then scale up. Build each component once, with all its states (hover, focus, error, loading, empty).
- Done: UX-05, DES-05, DES-06, DES-07.

**Step 14 · Design the key pages.**
- Why: visitors decide fast. The first screen must answer "what is this, is it for me, what do I do next?"
- Do: give every page one primary call to action, put trust signals (reviews, logos, guarantees, real contact details) near decisions, and use no dark patterns.
- Done: UX-06, UX-07, UX-08, UX-11, UX-17 (no pop-ups hiding the content).

**Step 15 · Design forms and states.**
- Why: forms are where conversions happen, and where most of them get lost.
- Do: ask for as little as possible. Use visible labels, error messages that explain the fix, and a confirmation that says what happens next.
- Done: UX-09, UX-10, A11Y-16, A11Y-17.

**Step 16 · Build accessibility into the design.**
- Why: about one in six people lives with a significant disability (WHO). Accessible design is also clearer for everyone, and the law requires it for many sites.
- Do: check contrast, make touch targets large enough, design a visible focus style, and never use color as the only signal.
- Done: A11Y-07, A11Y-12, A11Y-13, DES-08.

---

## Phase 3 · Content

Content is why people come and why search engines and AI cite you.

**Step 17 · Brief every page before writing.**
- Why: a brief forces you to define the intent, the questions to answer and what makes the page better than what already exists.
- Do: use [`content-brief.md`](templates/content-brief.md) for every launch page.
- Done: CON-02.

**Step 18 · Write for people first.**
- Why: Google and AI systems reward pages with original value: real experience, data, examples. Rewritten generic text doesn't rank and doesn't get cited.
- Do: lead with the answer. Use one idea per paragraph and headings that match real questions. Add something only you can say. Have experts review AI-assisted drafts.
- Done: CON-04, CON-07, CON-08, CON-09.

**Step 19 · Show who is behind the site.**
- Why: trust is the core of E-E-A-T. Anonymous content is weaker for users, search and AI.
- Do: create About and team pages, put author bylines with credentials on articles, cite sources and show honest dates.
- Done: CON-05, CON-06, GEO-07. Pages with reviews or comparisons also need first-hand evidence (CON-15).

**Step 20 · Prepare media.**
- Why: images make pages understandable, but they are also the main cause of slow pages.
- Do: prefer original photos and diagrams, write alt text that conveys the image's purpose, and export to AVIF or WebP at display size.
- Done: CON-10, A11Y-06, PRF-06.

---

## Phase 4 · Build

Build on a solid, boring foundation. Every shortcut here shows up later as a ranking, speed or security problem.

**Step 21 · Set up the project and environments.**
- Why: preview deploys and one-click rollback make every change safe. Staging that leaks into Google makes it unsafe.
- Do: use Git with reviewed pull requests, CI on every change ([`ci/quality.yml`](templates/ci/quality.yml)), a password-protected staging site, and secrets kept out of the code.
- Done: TEC-09, TEC-10, TEC-11, TEC-23, QA-03.

**Step 22 · Lay the HTML foundation.**
- Why: valid, semantic HTML is what browsers, screen readers, crawlers and AI all read first.
- Do: start from [`head.html`](templates/head.html). Use landmarks (`header`, `nav`, `main`, `footer`), one H1, logical headings and native buttons and links.
- Done: TEC-01, TEC-02, A11Y-03, A11Y-04, A11Y-05, SEO-17.

**Step 23 · Make every page crawlable.**
- Why: if the content only appears after JavaScript runs, or links aren't real links, search engines may never see it.
- Do: render content and metadata into the HTML on the server or at build time. Use real `<a href>` links. Give phones the same content as desktops. Load lazy content when it scrolls into view, never only on click.
- Done: SEO-01, SEO-10, SEO-11, SEO-39, SEO-40, TEC-28.

**Step 24 · Get the SEO basics right.**
- Why: these are the rules that decide whether a page can rank at all.
- Do:
  - Pick one host: https plus www or non-www.
  - Set a self-referencing canonical, a unique title and a meta description on every page.
  - Clean up the sitemap and set up [`robots.txt`](templates/robots.txt).
  - Make 404s real 404s and redirects single 301s.
  - Give every host its own `robots.txt`, and make canonical tags, sitemap, internal links and redirects all point to the same URL.
- Done: SEO-02 to SEO-09, SEO-15, SEO-16, SEO-38, SEO-41.

**Step 25 · Add structured data.**
- Why: structured data tells machines what a page is about (your organization, an article, a product, a location). It powers rich results and helps AI identify you as an entity.
- Do: adapt the [`schema/`](templates/schema/) templates, link profiles via `sameAs`, and mark up only what is visible on the page.
- Done: SEO-21, SEO-46, GEO-06. Reviews, products, jobs, articles and local businesses have their own markup rules (SEO-47 to SEO-56); every property is listed in [`reference/google-search/`](reference/google-search/README.md).

**Step 26 · Hit the performance budget.**
- Why: slow pages lose visitors and conversions, and Core Web Vitals are part of Google's page experience signals.
- Do:
  - Responsive modern images with fixed dimensions; the main hero image loads eagerly with high priority.
  - Self-hosted, subset fonts; deferred scripts; long caching for hashed files.
- Done: PRF-02, PRF-06 to PRF-13, PRF-17, PRF-22 (no file over 2 MB).

**Step 27 · Secure the site.**
- Why: even a brochure site can be hijacked for spam or used to attack visitors.
- Do: HTTPS only, the header baseline from [`_headers`](templates/_headers), server-side validation, spam protection without tracking, MFA on admin logins, and automatic dependency updates.
- Also make sure your CDN or firewall doesn't block Google's crawlers. To slow them down, answer with `503` or `429`, never other errors.
- Done: SEC-01 to SEC-04, SEC-08 to SEC-12, SEC-14, TEC-18, TEC-25, TEC-29, TEC-30.

**Step 28 · Set up consent and measurement.**
- Why: in the EU, nothing non-essential may run before consent. Without measurement you're guessing.
- Do: install a consent tool with an equally visible "reject" option. Load Google tags only after consent ([`consent-default.html`](templates/consent-default.html)). Configure analytics and track your key events.
- Done: PRV-01, PRV-02, PRV-03, MSR-07, MSR-08, MSR-14, MSR-15.

**Step 29 · Connect the CMS, forms and third parties.**
- Why: editors need structured fields so every page ships with a title, description and alt text. Every external script costs speed and privacy.
- Do: model content with required SEO and alt fields. Test every form end to end. Load embeds only on click.
- Done: TEC-17, TEC-19, TEC-20, TEC-21.

**Step 30 · Going multilingual? Do it properly.**
- Why: wrong language setup confuses search engines and shows visitors the wrong version.
- Do: give each language its own URL folder and full hreflang annotations. Localize everything, including metadata and legal pages. Never redirect automatically by IP address.
- Done: I18N-01 to I18N-06.

---

## Phase 5 · Test

Test like a visitor, a crawler and an attacker, on real devices.

**Step 31 · Let the machines check first.**
- Why: automated checks catch regressions on every change, for free.
- Do: run HTML validation, a link check, Lighthouse CI and an automated accessibility scan in CI ([`lighthouserc.json`](templates/ci/lighthouserc.json)).
- Done: QA-03, QA-04, A11Y-23.

**Step 32 · Test by hand.**
- Why: tools find only part of the problems, especially accessibility ones.
- Do: use real iPhone and Android devices, all viewports, keyboard only and a screen reader. Run end-to-end tests on every critical flow.
- Done: QA-01, QA-02, QA-05, QA-07, A11Y-24.

**Step 33 · Crawl the whole site and proofread.**
- Why: launch day is the worst time to discover 40 missing titles or a "lorem ipsum".
- Do: run a full crawl, search for placeholder text, and click every link, phone number and email address.
- Done: QA-08, QA-09.

**Step 34 · Pass the launch gate.**
- Why: one explicit go/no-go list prevents "we'll fix it after launch" from becoming permanent.
- Do: work through [`2-launch.md`](checklists/2-launch.md) § A. No open P0 or P1 defects may remain.
- Done: QA-10.

---

## Phase 6 · Launch

**Step 35 · Launch day.**
- Why: most launch disasters are a forgotten `noindex`, a broken redirect or a form nobody receives.
- Do: follow [`2-launch.md`](checklists/2-launch.md) § B: switch DNS, check redirects and indexability, submit the sitemap, request indexing of key pages, and test consent and forms on the live site.

**Step 36 · Watch the first 14 days.**
- Why: problems show up in Search Console and logs within days. Catch them before rankings are affected.
- Do: follow § C. Relaunching an existing site? § D (redirect map, content parity) is mandatory.
- Done: SEO-34 to SEO-37 (relaunch).

---

## Phase 7 · Grow

A website is never finished. The routine in [`3-monitoring.md`](checklists/3-monitoring.md) keeps it healthy and growing.

**Step 37 · Measure monthly.**
- Why: one dashboard and a fixed review rhythm turn data into decisions.
- Do: review traffic by channel, conversions, rankings, Core Web Vitals and AI visibility.
- Done: MSR-24, MSR-25, MSR-26. If traffic drops, triage before changing anything (MSR-30).

**Step 38 · Improve conversions.**
- Why: doubling the conversion rate is often cheaper than doubling traffic.
- Do: find where visitors drop off, form a hypothesis, and test one change at a time.
- Done: UX-14, UX-16.

**Step 39 · Build content and authority.**
- Why: rankings and AI citations grow with topical depth and with other sites referencing you.
- Do: expand topic clusters, refresh or merge decaying pages, and earn links and mentions with original data and digital PR.
- Done: CON-03, CON-13, SEO-26, GEO-10.

**Step 40 · Get cited by AI assistants.**
- Why: a growing share of searches end in an AI answer. Being the cited source keeps you visible.
- Do: write clear definitions and sourced facts, keep your entity consistent everywhere, set up Bing Webmaster Tools, track a fixed prompt set monthly, and fix wrong AI descriptions at their source.
- Done: GEO-08, GEO-09, GEO-11, GEO-13, GEO-14.

**Step 41 · Keep it safe and current.**
- Why: outdated plugins and expired certificates or domains are the most common avoidable outages.
- Do: patch on schedule, review access every quarter, renew `security.txt` and legal texts every year, and re-check this blueprint every quarter.
- Done: SEC-15, TEC-25, MSR-21, MSR-22.
