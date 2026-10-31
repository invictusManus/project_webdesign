# 04 · Content

**Why it matters:** Content is why people visit and why search engines and AI cite you. Pages that add original value from identifiable experts outperform generic text. Guide: Phase 3.

Detail: `reference/google-search/` notes.

Scope: content strategy, topic clusters, E-E-A-T, copywriting, media, AI-assisted content, governance. Per-page planning: [`content-brief.md`](../templates/content-brief.md).

Last verified: 2026-10

| ID | Level | Rule | Verify |
|---|---|---|---|
| CON-01 | MUST | Each indexable URL serves one primary intent and one query cluster (`url-map.csv`). No two URLs target the same intent. | `url-map.csv`; GSC queries per page |
| CON-02 | MUST | Every page gets a content brief before writing: intent, audience, primary query, questions to answer, unique angle or evidence, outline, internal links, call to action, schema type. | Brief per URL |
| CON-03 | SHOULD | Each core topic has a pillar page that links to cluster pages, each answering one specific sub-question (SEO-23). | Link graph |
| CON-04 | MUST | People-first: every page adds something not available elsewhere, such as first-hand experience, original data, expert insight, worked examples or tools. No rewritten commodity content. | Editorial review vs. top results |
| CON-05 | MUST | Trust (E-E-A-T): the site shows who is behind it (About, team, Impressum). Each article has a byline linking to an author page with credentials. Sources are cited for facts, figures and claims. No fabricated authors: no made-up names, AI-generated headshots or false credentials. | Page review |
| CON-06 | MUST | Articles show their published and updated dates, and `datePublished`/`dateModified` markup equals them (timezone included, no future dates). "Updated" changes only after a substantive edit, never for a date bump alone. | Version history vs. date |
| CON-07 | SHOULD | Answer first: lead with the direct answer or key takeaway, then the detail. One idea per paragraph. Subheadings mirror real user questions. Use lists and tables for comparable data. | Editorial review |
| CON-08 | SHOULD | Use plain, active language at the audience's reading level and the voice defined in `DESIGN.md`. No filler introductions. | Readability check |
| CON-09 | MUST | AI-assisted content gets expert review, a fact check of every claim and an original contribution. Disclose AI use where readers would expect it (and per PRV-13). Review also covers `<title>`, meta description, structured data and alt text. AI-generated images carry IPTC `DigitalSourceType` `TrainedAlgorithmicMedia`; AI-written product titles and descriptions are labeled as such in Merchant Center. Never publish at scale without review (SEO-33). | Editorial log |
| CON-10 | SHOULD | Prefer original images and diagrams to stock. Use captions where they add context. Videos get a transcript and chapter markers. Alt text follows A11Y-06. | Media review |
| CON-11 | SHOULD | Health, finance, legal and safety topics (YMYL) are written or reviewed by named, qualified experts. | Byline and reviewer |
| CON-12 | MUST | Each page has an owner and a review date. YMYL pages are reviewed every 6 months, all others at least yearly. Dated markup (events, offers, jobs) is kept current. | `url-map.csv` owner and review_date |
| CON-13 | SHOULD | Every quarter, pages with falling traffic or rankings are reviewed for usefulness. Improve them first; merge (301) or remove (410) only content that cannot be salvaged. Never add or delete content in bulk to look "fresh", and a drop after a core update alone is no reason to delete. No thin or outdated page stays indexable. | Decay report |
| CON-14 | SHOULD | An editorial calendar follows the clusters and business priorities. Every piece has a distribution plan (newsletter, social, outreach). | Calendar |
| CON-15 | SHOULD | Reviews, comparisons and best-of pages show first-hand evidence: own testing or measurements, benefits and drawbacks, why an item is best, alternatives or several sellers. No thin summaries or copied merchant text. | Editorial review |

## Sources

- [Google: Creating helpful, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google: Guidance on using generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [Google: Search Quality Rater Guidelines](https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf)
- [Google: Core updates](https://developers.google.com/search/docs/appearance/core-updates) · [Publication dates](https://developers.google.com/search/docs/appearance/publication-dates) · [Reviews system](https://developers.google.com/search/docs/appearance/reviews-system) · [Write high-quality reviews](https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews)
- [Google: Spam policies (scaled content abuse)](https://developers.google.com/search/docs/essentials/spam-policies)
