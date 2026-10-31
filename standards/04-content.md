# 04 · Content

**Why it matters:** Content is why people visit and why search engines and AI cite you. Pages that add original value from identifiable experts outperform generic text. Guide: Phase 3.

Scope: content strategy, topic clusters, E-E-A-T, copywriting, media, AI-assisted content, governance. Per-page planning: [`content-brief.md`](../templates/content-brief.md).

Last verified: 2026-10

| ID | Level | Rule | Verify |
|---|---|---|---|
| CON-01 | MUST | Each indexable URL serves one primary intent and one query cluster (`url-map.csv`). No two URLs target the same intent. | `url-map.csv`; GSC queries per page |
| CON-02 | MUST | Every page gets a content brief before writing: intent, audience, primary query, questions to answer, unique angle or evidence, outline, internal links, call to action, schema type. | Brief per URL |
| CON-03 | SHOULD | Each core topic has a pillar page that links to cluster pages, each answering one specific sub-question (SEO-23). | Link graph |
| CON-04 | MUST | People-first: every page adds something not available elsewhere, such as first-hand experience, original data, expert insight, worked examples or tools. No rewritten commodity content. | Editorial review vs. top results |
| CON-05 | MUST | Trust (E-E-A-T): the site shows who is behind it (About, team, Impressum). Each article has a byline linking to an author page with credentials. Sources are cited for facts, figures and claims. | Page review |
| CON-06 | MUST | Articles show their published and updated dates. "Updated" changes only after a substantive edit, never for a date bump alone. | Version history vs. date |
| CON-07 | SHOULD | Answer first: lead with the direct answer or key takeaway, then the detail. One idea per paragraph. Subheadings mirror real user questions. Use lists and tables for comparable data. | Editorial review |
| CON-08 | SHOULD | Use plain, active language at the audience's reading level and the voice defined in `DESIGN.md`. No filler introductions. | Readability check |
| CON-09 | MUST | AI-assisted content gets expert review, a fact check of every claim and an original contribution. Disclose AI use where readers would expect it (and per PRV-13). Never publish at scale without review (SEO-33). | Editorial log |
| CON-10 | SHOULD | Prefer original images and diagrams to stock. Use captions where they add context. Videos get a transcript and chapter markers. Alt text follows A11Y-06. | Media review |
| CON-11 | SHOULD | Health, finance, legal and safety topics (YMYL) are written or reviewed by named, qualified experts. | Byline and reviewer |
| CON-12 | MUST | Each page has an owner and a review date. YMYL pages are reviewed every 6 months, all others at least yearly. | `url-map.csv` owner and review_date |
| CON-13 | SHOULD | Every quarter, pages with falling traffic or rankings are updated, merged (301) or removed (410). No thin or outdated page stays indexable. | Decay report |
| CON-14 | SHOULD | An editorial calendar follows the clusters and business priorities. Every piece has a distribution plan (newsletter, social, outreach). | Calendar |

## Sources

- [Google: Creating helpful, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google: Guidance on using generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [Google: Search Quality Rater Guidelines](https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf)
- [Google: Spam policies (scaled content abuse)](https://developers.google.com/search/docs/essentials/spam-policies)
