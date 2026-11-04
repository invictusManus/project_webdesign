# 04 · Content

**Why it matters:** Content is why people visit and why search engines and AI cite you. Pages that add original value from identifiable experts outperform generic text. Guide: Phase 3.

Detail: `reference/google-search/` notes.

Scope: content strategy, topic clusters, E-E-A-T, copywriting, media, AI-assisted content, governance. Per-page planning: [`content-brief.md`](../templates/content-brief.md).

Last verified: 2026-11

| ID | Level | Rule | Verify |
|---|---|---|---|
| CON-01 | MUST | [house] Each indexable URL serves one primary intent and one query cluster (`url-map.csv`). No two URLs target the same intent. | `url-map.csv`; GSC queries per page |
| CON-02 | MUST | Every page gets a content brief before writing: intent, audience, primary query, questions to answer, unique angle or evidence, outline, internal links, call to action, schema type. | Brief per URL |
| CON-03 | SHOULD | [house] Each core topic has a pillar page that links to cluster pages, each answering one specific sub-question (SEO-23). | Link graph |
| CON-04 | MUST | [house] People-first: every page adds something not available elsewhere, such as first-hand experience, original data, expert insight, worked examples or tools. No rewritten commodity content. | Editorial review vs. top results |
| CON-05 | MUST | [house] Trust (E-E-A-T): the site shows who is behind it (About, team, Impressum). Each article has a byline linking to an author page with credentials. Sources are cited for facts, figures and claims. No fabricated authors: no made-up names, AI-generated headshots or false credentials. | Page review |
| CON-06 | MUST | Articles show their published and updated dates, and `datePublished`/`dateModified` markup equals them (timezone included, no future dates). "Updated" changes only after a substantive edit, never for a date bump alone. | Version history vs. date |
| CON-07 | SHOULD | Answer first: lead with the direct answer or key takeaway, then the detail. One idea per paragraph. Subheadings mirror real user questions. Use lists and tables for comparable data. | Editorial review |
| CON-08 | SHOULD | Use plain, active language at the audience's reading level and the voice defined in `DESIGN.md`. No filler introductions. Objective, not promotional: every claim carries a fact, and the hype words in the AI-writing checklist are absent (NN/g measured objective copy as more usable). | Readability check |
| CON-09 | MUST | AI-assisted content gets expert review, a fact check of every claim and an original contribution. Disclose AI use where readers would expect it (and per PRV-13). Review also covers `<title>`, meta description, structured data and alt text. In Merchant Center feeds, AI-generated images carry IPTC `DigitalSourceType` `TrainedAlgorithmicMedia`; AI-written product titles and descriptions are labeled as such in Merchant Center. Never publish at scale without review (SEO-33). | Editorial log |
| CON-10 | SHOULD | Prefer original images and diagrams to stock. Use captions where they add context. Videos get a transcript and chapter markers. Alt text follows A11Y-06. | Media review |
| CON-11 | SHOULD | Health, finance, legal and safety topics (YMYL) are written or reviewed by named, qualified experts. | Byline and reviewer |
| CON-12 | MUST | Each page has an owner and a review date. YMYL pages are reviewed every 6 months, all others at least yearly. Dated markup (events, offers, jobs) is kept current. | `url-map.csv` owner and review_date |
| CON-13 | SHOULD | Every quarter, pages with falling traffic or rankings are reviewed for usefulness. Improve them first; merge (301) or remove (410) only content that cannot be salvaged. Never add or delete content in bulk to look "fresh", and a drop after a core update alone is no reason to delete. No thin or outdated page stays indexable. | Decay report |
| CON-14 | SHOULD | An editorial calendar follows the clusters and business priorities. Every piece has a distribution plan (newsletter, social, outreach). | Calendar |
| CON-15 | SHOULD | Reviews, comparisons and best-of pages show first-hand evidence: own testing or measurements, benefits and drawbacks, why an item is best, alternatives or several sellers. No thin summaries or copied merchant text. | Editorial review |
| CON-16 | MUST | Before any website text is added or changed (pages, sections, blog posts, navigation, buttons, titles, meta descriptions), it is checked line by line against [`reference/ai-writing/checklist.md`](../reference/ai-writing/checklist.md) (Wikipedia: Signs of AI writing). Every match is rewritten. | Checklist pass noted in the commit or PR |

## Editorial style

| ID | Level | Rule | Verify |
|---|---|---|---|
| CON-17 | MUST | A written style guide in `DESIGN.md` fixes: spelling variant (e.g. en-US or en-GB), capitalization (sentence case, DES-15), numbers, dates, times, units and currency per locale (I18N-08), abbreviations, brand and product names (GEO-05), terminology (UX-15), link text (A11Y-15), inclusive language (CON-20) and UI punctuation: no exclamation marks in headings, buttons, labels, navigation or errors, no trailing period on headings, buttons and labels, no all-caps for emphasis. All copy follows it. | Style guide exists; copy review |
| CON-18 | SHOULD | [house] Readability for general audiences: sentences average ≤ 20 words, paragraphs ≤ 4 sentences, Flesch reading ease ≥ 60 for English (Amstad ≥ 60 for German). The brief may set another level for specialist audiences. Complements A11Y-21. | Readability tool on key pages |
| CON-19 | SHOULD | Every recurring content type has a fixed structure in `content-brief.md`: article (answer first, sections, sources, author box), case study (client, problem, approach, measured result, quote), product description (benefit first, specifications, use and care, own text instead of manufacturer copy), service page, location page (SEO-31), landing page (ad promise, value, proof, offer, call to action, FAQ). | Sample per type |
| CON-20 | SHOULD | Inclusive language: gender-inclusive forms as defined per language in the style guide, people-first wording, no ableist idioms, imagery that represents the audience authentically. Instructions never rely on color, shape or position alone ("the green button", "on the right", WCAG 1.3.3). | Copy review |
| CON-21 | SHOULD | [EU] Claims are provable: statements about prices, test results, awards and certifications must not mislead (UWG §5 Abs. 2 Nr. 1–3; Directive 2005/29/EC Art. 6), price reductions must be provable (UWG §5 Abs. 5), and superlatives ("best", "No. 1") need evidence under case law on §5. Security, compliance, uptime and speed claims ("ISO 27001", "99.9 % uptime", "3× faster") name the certificate, scope and date or the measurement method, or are removed. [house] Every such claim and statistic carries a source, date and baseline ("vs. Oct 2025"). Flag for legal review. | Claims register |
| CON-22 | SHOULD | FAQ questions come from real sources (support tickets, site search, sales calls), logged in the content brief; no template questions that fit any product. Answers are specific and link to detail. | Question-to-source map |

## Sources

- [NN/g: Concise, scannable and objective](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/) · [NN/g: FAQs still deliver value](https://www.nngroup.com/articles/faqs-deliver-value/) · [Microsoft style guide: Periods](https://learn.microsoft.com/en-us/style-guide/punctuation/periods) · [Exclamation points](https://learn.microsoft.com/en-us/style-guide/punctuation/exclamation-points)
- [Google: Creating helpful, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google: Guidance on using generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [Google: Search Quality Rater Guidelines](https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf)
- [Google: Core updates](https://developers.google.com/search/docs/appearance/core-updates) · [Publication dates](https://developers.google.com/search/docs/appearance/publication-dates) · [Reviews system](https://developers.google.com/search/docs/appearance/reviews-system) · [Write high-quality reviews](https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews)
- [W3C: WCAG 2.2, 1.3.3 Sensory characteristics](https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html) · [UWG §5 (misleading commercial practices)](https://www.gesetze-im-internet.de/uwg_2004/__5.html) · [Directive 2005/29/EC (Unfair Commercial Practices)](https://eur-lex.europa.eu/eli/dir/2005/29/oj)
- [Google: Spam policies (scaled content abuse)](https://developers.google.com/search/docs/essentials/spam-policies)
