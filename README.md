# Website Foundation

A complete, practical handbook for planning, designing, building, launching and running professional websites. It works for any tech stack, and both people and AI coding agents can follow it.

## What you get

- **A step-by-step guide.** [`GUIDE.md`](GUIDE.md) takes you from the first idea to launch and growth in 41 steps and explains why each step matters. [`GLOSSARY.md`](GLOSSARY.md) explains every technical term in plain words.
- **About 500 testable rules.** Each rule has an ID, a level and a way to check it, so "done" never means "looks fine to me".
- **Checklists** for before the project, launch day, Search Console and day-to-day running.
- **Ready-made templates:** project brief, design spec, design tokens, page and component plans, audit report, legal and technical files.
- **Reference material:** Google's full Search documentation in condensed notes, a checklist for spotting AI-written copy, and a vetted list of free icon, animation and illustration sources.

## Who it is for

- **Beginners** who want to learn how a professional website is made.
- **Designers, developers and agencies** who want one consistent quality bar for every project.
- **Site owners** who want to audit, fix or relaunch an existing site.
- **AI coding agents** that build or edit websites (see [Working with AI agents](#working-with-ai-agents)).

## Start here

| I want to… | Open |
|---|---|
| Learn web design from scratch | [`GUIDE.md`](GUIDE.md) and [`GLOSSARY.md`](GLOSSARY.md) |
| Build a new website | [`checklists/1-preflight.md`](checklists/1-preflight.md), then the standards, then [`checklists/2-launch.md`](checklists/2-launch.md) |
| Audit or improve an existing site | [`checklists/2-launch.md`](checklists/2-launch.md) as the audit sheet, written up in [`templates/audit-report.md`](templates/audit-report.md) |
| Relaunch or move a site | [`checklists/2-launch.md`](checklists/2-launch.md) section D and [`templates/url-map.csv`](templates/url-map.csv) |
| Set up and use Google Search Console | [`checklists/4-search-console.md`](checklists/4-search-console.md) |
| Run and grow a live site | [`checklists/3-monitoring.md`](checklists/3-monitoring.md) |
| Look up what Google says about an SEO topic | [`reference/google-search/`](reference/google-search/README.md) |
| Pick tools | [`TOOLS.md`](TOOLS.md) |

## How a project runs

The work follows the web development life cycle. Each phase has its own files.

| Phase | What happens | Main files |
|---|---|---|
| 1. Discovery | Goals, audience, offer, competitors, search demand, scope and estimate | `standards/01-strategy.md`, `standards/17-project.md`, `templates/project-brief.md`, `templates/project-plan.md` |
| 2. Planning | Site type, pages and keywords, features, legal duties, accounts | `checklists/1-preflight.md`, `standards/site-types.md`, `templates/url-map.csv` |
| 3. Design | Brand, design system, layout, components, UX, accessibility | standards 02, 03, 09, 14, 15, 16; `templates/DESIGN.md`, `templates/tokens.json` |
| 4. Development | Content, code, SEO, performance, security, measurement | standards 04–08, 10–12; code templates |
| 5. Testing | Automated checks, real devices, accessibility, security review | `standards/13-qa.md`, `templates/ci/` |
| 6. Deployment | Launch gate (every MUST rule), go-live, first 14 days | `checklists/2-launch.md` |
| 7. Maintenance | Handover, monitoring, updates, Search Console, content upkeep | `templates/handover.md`, `templates/maintenance-agreement.md`, `checklists/3-monitoring.md`, `checklists/4-search-console.md` |

## What it covers

| Area | In short | Where |
|---|---|---|
| Project and client | Scope, estimate, timeline, roles, change requests, handover, maintenance agreement | `17-project` |
| Strategy | Goals, audiences, positioning, competitors, keyword research | `01-strategy` |
| Brand and design system | Design intake, 60-30-10 color palette (primary, secondary, accent), golden-ratio type and spacing, full design tokens incl. hover, shadows, borders and dark mode, icons and animation | `02-brand-design`, `templates/DESIGN.md`, `templates/tokens.json` |
| Layout and responsive | Mobile, tablet, desktop and wide screens, grid, page structure, header, navigation, hero, footer | `15-layout-responsive` |
| Components | Cards, tables, forms, dialogs, tabs, accordions, loading and empty states | `16-components` |
| UX and conversion | Navigation, forms, product pages, cart, checkout, site search, chatbots, onboarding | `03-ux` |
| UX psychology | How people perceive and decide; honest persuasion, no dark patterns | `14-ux-psychology` |
| Content | Content plans, trust signals, style guide, readability, AI-writing review | `04-content`, `reference/ai-writing/` |
| SEO | Crawling, indexing, titles, alt text, structured data, links, local SEO, migrations | `05-seo`, `reference/google-search/` |
| AI search | Being found and cited in AI answers (Google AI Overviews, ChatGPT and others) | `06-geo-aeo` |
| Tech | HTML and CSS basics, hosting, domains, email, CMS and editors, installable web apps (PWA) | `07-tech` |
| Performance | Core Web Vitals, images, fonts, JavaScript, energy use | `08-performance` |
| Accessibility | WCAG 2.2 AA, keyboard, screen readers, motion, EU accessibility law | `09-accessibility` |
| Security and privacy | HTTPS, headers, OWASP, accounts, APIs, consent, GDPR, legal pages | `10-security-privacy` |
| Measurement | Search Console, Bing, GA4, tag manager, monitoring | `11-measurement` |
| Multiple languages | URLs, hreflang, translation, formats, right-to-left | `12-i18n` |
| Quality assurance | Devices, automated tests, audits, definition of done | `13-qa` |
| Site types | What changes for business sites, landing pages, blogs, SaaS, shops and web apps | `site-types` |

## How the rules work

Every rule lives in exactly one place in `standards/` and looks like this:

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRF-08 | MUST | The main hero image is in the first HTML, never lazy-loaded, and has high priority. | Lighthouse "LCP request discovery" |

- **MUST:** required. It blocks launch unless an exception is written down with an owner and a date.
- **SHOULD:** the professional default. Skip it only for a written reason.
- **COULD:** extra polish once MUST and SHOULD hold.
- **[EU]:** a legal duty in the EU or Germany. It describes the law; it is not legal advice.
- **[house]:** our own stricter choice. It never contradicts Google or another primary source.
- **⚗:** experimental and unofficial, but cheap to try.
- **Sources:** official ones only (Google, W3C, OWASP, MDN, EU law and similar). For search, Google's documentation always wins.
- **IDs never change.** A removed rule stays in place, marked `RETIRED`. Checklists point to IDs, and [`rules.csv`](rules.csv) lists every rule in one file.

## Quality checks

`scripts/check.sh` must pass before any change is merged. It checks that:

- every rule ID exists once, is used correctly and appears in a checklist if it is a MUST;
- every link inside the repository works and every standard stays short;
- the design tokens are valid and every color pair passes the contrast checks, in light and dark mode;
- the generated files (`rules.csv`, `templates/tokens.css`) are up to date.

GitHub runs the same check on every change. A weekly job reports changed Google documentation and broken external links.

## Working with AI agents

- Copy [`templates/AGENTS.md`](templates/AGENTS.md) into a website's repository, and the agent follows these rules.
- [`AGENTS.md`](AGENTS.md) explains how agents apply and edit this handbook.
- Rule IDs are cited in commits and reports, e.g. `fix(PRF-08): eager-load hero image`, so every change is traceable.

## Keeping it current

Each standard shows when its rules were last checked against their sources (`Last verified`). Re-check them every quarter, and always when a file changes, against:

[Google Search Central](https://developers.google.com/search/updates) · [web.dev](https://web.dev/blog) · [Chrome UX Report](https://developer.chrome.com/docs/crux/release-notes) · [W3C WAI](https://www.w3.org/WAI/news/) · [OWASP Top 10](https://owasp.org/Top10/) · [Schema.org](https://schema.org/docs/releases.html) · [Datenschutzkonferenz](https://www.datenschutzkonferenz-online.de/) · [EUR-Lex](https://eur-lex.europa.eu/)

## Contributing

1. Create a branch for one task.
2. Make the change, run `scripts/check.sh`, and commit with the rule IDs in the message.
3. Open a pull request. It is merged once the checks are green and it has been reviewed.

## Folder map

```
README.md · GUIDE.md · GLOSSARY.md · AGENTS.md · TOOLS.md · rules.csv
standards/   01-strategy · 02-brand-design · 03-ux · 04-content · 05-seo · 06-geo-aeo · 07-tech
             08-performance · 09-accessibility · 10-security-privacy · 11-measurement · 12-i18n · 13-qa
             14-ux-psychology · 15-layout-responsive · 16-components · 17-project · site-types
checklists/  1-preflight · 2-launch · 3-monitoring · 4-search-console
templates/   project-brief · content-brief · url-map.csv · audit-report · AGENTS · DESIGN
             tokens.json · tokens.dark.json · tokens.css (generated) · motion.css · icon
             component-spec · page-blueprint · accessibility-statement
             project-plan · handover · maintenance-agreement
             head.html · robots.txt · _headers · security.txt · consent-default.html
             schema/ (structured data examples) · ci/ (quality workflow, Lighthouse CI)
reference/   google-search/ (all 184 Google Search documentation pages, condensed)
             ai-writing/ (signs of AI writing and a pre-publish checklist)
             assets/ (free icon, animation and illustration sources with licenses)
scripts/     check.sh · rules_index.py · check_tokens.py · tokens_to_css.py
```

## License

[MIT](LICENSE)
