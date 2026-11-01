# Pre-publish checklist: AI-writing signs in website copy

Check every text written for a website against this list before publishing: pages, sections, blog posts, navigation labels, buttons, meta titles and descriptions. Each item names a pattern and its fix.

Derived only from the signs documented in this folder (see [`README.md`](README.md) for sources). Source: Wikipedia contributors, CC BY-SA 4.0; this checklist is an adaptation under the same license. The source guide is about Wikipedia, so items are adapted to web copy and some signs have no web equivalent (listed at the end). It describes patterns seen in AI output. It cannot detect AI and proves nothing in either direction.

## How to run it

1. Read the text top to bottom once, then scan each group below. Search the source text for the exact words and characters listed.
2. Weigh hits by kind. One unambiguous artifact (group M) means the text came from a chatbot unreviewed: fix it and re-verify every claim in the piece. Otherwise a single hit is weak evidence; several hits from different groups are strong. The guide's own heuristic: signs multiply, so one em dash means little and an em dash plus `pivotal` plus vague attribution means a lot.
3. Fix the cause, not the symptom. The guide warns that treating signs as the problem only makes detection harder. The real problems are generic or unverified content. Replace each flagged passage with a specific, checkable fact (who, what, when, how many, link), or delete it.
4. Do not swap in synonyms. Overuse of one word does not make its synonyms safe, and synonym swaps leave the generic content intact.
5. Check facts against sources. The guide calls this the most reliable test and the slowest: every claim, name, date, figure, quote and link must be traceable to a source you opened.
6. Re-run the checklist on the revised text. Replacements often reintroduce the same patterns.
7. Pass does not mean human or verified. The guide notes (August 2026) that the documented signs are partly outdated for the newest models, and that human judgment alone is near chance. A clean pass lowers risk. It does not replace fact-checking.

## Element map

| Element | Run these groups |
|---|---|
| Home, landing, service pages | V, T, S, P, C, M |
| About, team, bio pages | T9, T10, C5, C6, V7, C1, M |
| Blog posts and articles | all groups; S9 (summaries) and C7 (negative parallelisms) matter most |
| Headings and section titles | S1, S2, S3, S6, S8, V6 |
| Navigation labels | S1, S2, S6, V5, T9 |
| Buttons and calls to action | S6, T5, T9, P1, P3, V1, V5 |
| Meta titles and descriptions | V1, V5, V6, C1, S6, P1, P3 (straight quotes in attributes), M1, M3, M5 |
| Contact pages, forms, email templates | S13, T2, T4, T5, M3 |
| Notices, policy and error copy | T2, T3, T4, T7, T8 |
| Changelogs, release notes, commit messages | C12, T2, V1 |
| Outbound links and cited sources | C14, M6 |

## V. Vocabulary

- V1. AI vocabulary density. Look for: `Additionally` (especially opening a sentence), `align with`, `boasts` (meaning has), `bolstered`, `crucial`, `deep dive`, `delve`, `emphasizing`, `enduring`, `enhance`, `fostering`, `garner`, `highlight` (verb), `interplay`, `intricate`/`intricacies`, `landscape` (abstract), `meticulous`/`meticulously`, `pivotal`, `robust`, `showcase`, `tapestry` (abstract), `testament`, `underscore` (verb), `valuable`, `vibrant`, `key` as a filler adjective. One or two is coincidence; many in one text is one of the strongest tells. Fix: delete the phrase or rewrite with a plain verb and a concrete fact. Literal uses (a highlighted text, an underscore character, a robust test suite with evidence) are fine.
- V2. Newer-model words (mid-2026 onward). Look for clusters of: `challenge`, `clearer`, `dependable`, `echoed`, `foster`, `leverage`, `matters`, `multifaceted`, `practical`, `prioritize`, `quietly`, `steady`, `universally`. Weak alone (ordinary words). Fix: flag only when several co-occur; rewrite with specifics.
- V3. Pseudo-scientific words (Grok-style): `causal`, `empirical`, `correlate`, plus continued `underscore`. Fix: use only where a real analysis exists; otherwise plain words.
- V4. Copula avoidance. Look for: `serves as`, `stands as`, `marks`, `functions as`, `operates as`, `represents a`, `boasts a`, `features a`, `maintains a`, `offers a`, `refers to` (in a definition). Fix: `is`, `are`, `has`. Example: "X serves as the company's hub" becomes "X is the company's hub". Present perfect `has been featured` is not the sign.
- V5. Puffery and marketing buzzspeak. Look for: `boasts a`, `vibrant`, `rich`, `profound`, `enhancing`, `showcasing`, `exemplifies`, `commitment to`, `natural beauty`, `nestled`, `in the heart of`, `groundbreaking`, `renowned`, `featuring`, `diverse array`, `thought leader`, `trend-setter`, `cutting edge`, `award-winning`, `acts as the gateway`, `dependable, value-driven experiences`, `rich cultural heritage`, `diverse tapestry`. Fix: state the checkable fact. Replace `award-winning` with the award, year and awarding body (and a link). Replace "renowned" with who recognized it, when.
- V6. Significance words. Look for: `stands/serves as`, `is a testament/reminder`, `a crucial/pivotal/vital/significant/key role/moment`, `underscores/highlights its importance/significance`, `reflects broader`, `symbolizing its ongoing/enduring/lasting`, `contributing to the`, `setting the stage for`, `marking/shaping the`, `represents/marks a shift`, `key turning point`, `evolving landscape`, `focal point`, `indelible mark`, `deeply rooted`, `distinction matters because`. Fix: delete the sentence, or replace with the event, date and effect it names.
- V7. Vague connection verbs. Look for: `in connection with/to`, `connected with/to`, `in association with`, `associated with`, `particularly associated`, `widely associated`, `ventured into`, `began his/her career as` where "was" is meant. Fix: state the relationship directly ("was CEO of X from 2017 to 2021", "teaches science at X").
- V8. Elegant variation. Look for: one thing called by a new descriptive phrase each time ("the constraints", "the challenging climate", "the confines"; "the artists", "non-conformist artists", "like-minded artists"). Mostly older models. Fix: repeat the plain noun or use a pronoun. Non-native writers also vary words, so this is weak alone.
- V9. Plain words over stiff ones. The guide notes humans use `wrote`, `moved`, `used`, `tried`, `died` where AI text prefers `authored`, `relocated`, `utilized`, `attempted`, `passed away`; also simple `there is a`, `it has a`; `very`, `perhaps`, `tends to`; `as a result of`, `in order to`, `all of the`, `a part of`, `the fact that` in isolation. Fix: prefer the plain word. This is a human-writing trait: absence is not proof of AI.
- V10. Sentence-opening transitions. Look for: `Additionally,`, `Consequently,`, `Notably,`, `Overall`. Weak alone (accepted in essays). Fix: delete if the sentence connects without it.

## T. Tone

- T1. Ad-copy or travel-guide register in neutral content. Look for: superlatives and glowing adjectives in descriptions that should inform, press-release phrasing, text selling a subject the page only describes. Fix: neutral facts; let numbers, dates and named sources carry the praise. Newer models are subtler: also check for quiet positivity with no superlative.
- T2. Overassurance. Look for: `I am committed to ...`, `I assure you that ...`, `I have taken the time to ...`, `I understand the importance of ...`, `I recognize that ...`, `Going/Moving forward, I will ...`, `my aim/goal/intention is to ...`, `aligns with our values/mission`. Fix: name the concrete commitment (what, by when) or delete it.
- T3. Vague commitments to rules and standards. Look for: broad, abstract mentions of standards, guidelines or policies ("adheres to the highest standards", "in compliance with best practices") with no specific rule named. Fix: cite the specific standard, rule or document, or remove.
- T4. Hedged apology or claim. Look for: `I apologize for any ...`, `may have ...`, `could be interpreted/perceived as ...`. Fix: name the specific thing that happened and what changed.
- T5. Clerk or customer-service register. Look for: `Thank you for your time and consideration`, `Thank you for considering`, `I respectfully ...`, `I am happy to ...`, `please do not hesitate to ...`, `welcome any additional input`, `Your assistance would be invaluable`, `I look forward to collaborating`. Fix: a direct sentence with a specific next step (who to contact, how, by when).
- T6. Denial of intent. Look for: `my/our intention is not to ... but to ...`, `not created for promotional purposes`, `is not intended to promote`. Fix: delete; show the purpose through content.
- T7. Didactic disclaimers. Look for: `it's important to note`, `it is crucial to differentiate ... to prevent confusion`, `it's important to remember`, `may vary`. Fix: state the actual fact or caveat, specifically; drop the preamble.
- T8. Corrective framing (mid-2026 style). Look for: `should be treated as ... rather than ...`, `does not by itself establish`, `does not establish that`, `should not be confused with`, `undergoing testing and evaluation, rather than validated`. Fix: say what the source supports and what it does not, in plain terms with the source named.
- T9. Canned "about me" and "contact" copy. Look for: `Welcome to My ...!`, `About Me`, `My Interests`, `How I Contribute`, `Goals`, `Let's Connect!`, `Let's Collaborate!`, `I'm always open to learning`, `Feel free to reach out`, `I'd love to hear from you!`, a closing quotation, `Thank you for visiting`. Fix: write real biography facts (role, years, work, places), and a specific contact route.
- T10. Hedging about missing information. Look for: `While specific details are limited/scarce`, `not widely available/documented/disclosed`, `in the provided/available sources`, `based on available information`, `maintains a low profile`, `keeps personal details private`, `likely` guesses about unknown facts. Fix: delete. If information does not exist, leave the claim out. Never fill the gap with speculation.
- T11. Self-certification. Look for: `neutral`, `well-sourced`, `all claims verified`, `human-curated`, `written in a neutral, encyclopedic tone` about the text itself. Fix: delete; show sources instead.
- T12. Generic text. Look for: copy that would fit any company, product or person if the name were swapped. Fix: swap the name test: if the text stays true for a competitor, rewrite with details only this subject has.

## S. Structure and formatting

- S1. Title case in headings, navigation labels and buttons. Look for: every main word capitalized ("Impact of Technology and Digitalization"). Fix: sentence case unless the brand style guide says otherwise. If the site deliberately uses title case, apply it uniformly and note that it is a house choice.
- S2. "X and Y" and recognition-style headings. Look for: `Awards and Recognition`, `Recognition`, `Challenges and Legacy`, `Challenges and Future Directions`, `Future Outlook`, `Future Prospects`, `Conclusion`. Fix: name what the section contains. Remove a recognition section unless it lists real awards with year, body and source.
- S3. Outline-like challenges and future section. Look for: `Despite its ... faces several challenges ...`, `Despite these challenges`, then a positive or speculative closing line. Fix: either state specific challenges with facts and dates, or cut the section.
- S4. Inline-header vertical lists. Look for: list items starting with a bold label and a colon ("**Route Details**: ...", "1. Key Figures:"), or bullets with no punctuation after a bold title. Fix: rewrite as prose, or as a plain list where each item is a full statement. Use a definition list only when entries are true term and definition pairs.
- S5. Excess boldface. Look for: bold on many phrases per paragraph, every instance of a term bolded, "key takeaways" bolding. Fix: remove; keep bold only where a reader must not miss something.
- S6. Emoji as formatting. Look for: emoji before headings, list items, labels, menu items, button text, titles or descriptions (👋 ✨ 🚀 📌 🏆 💬 📬). Fix: remove.
- S7. Small tables. Look for: a two-column, three-to-five row table of simple facts or a two-item comparison table. Fix: prose or a short list; keep tables for real multi-dimension data.
- S8. Heading structure. Look for: more than one h1; page title repeated as a heading inside the body; skipped levels (h1 then h3); a heading containing only subheadings with no text. Fix: one h1, sequential levels, text under every heading.
- S9. Summaries and conclusions. Look for: `In summary`, `In conclusion`, `Overall`, a "Conclusion" section, a closing paragraph restating the opening. Fix: delete; end on the last new fact or the call to action.
- S10. Horizontal rule between every section. Look for: `---` or `<hr>` after each section. Fix: remove; use headings and spacing.
- S11. Short text cut into titled sections. Look for: a short message or small page split into many titled blocks. Fix: merge into continuous text.
- S12. Rule of three. Look for: triplets of adjectives or short phrases (`tiles, metals, and plastics`; `mythological image, magical weapons, and spirit of resistance`), especially in places that rarely carry such flourishes (meta descriptions, button text, headings, changelogs). Fix: keep only items that are true and distinct; use two or four or one if that matches the facts.
- S13. Letter or email format in web copy. Look for: `Subject:`, `Dear ...`, `Sincerely,`, `Best regards,` or a leftover signature block in page text, forms or templates. Fix: remove; write for the page.

## P. Punctuation

- P1. Em dashes. Look for: em dashes (—) used where a comma, parentheses, colon or period would work, especially for punched-up contrasts or parallelisms and with spaces around them. Fix: rewrite the sentence with the simpler mark. Check every one; keep only where nothing else reads correctly. Do not search-and-replace blindly. Frequency alone is not proof (human writers use them).
- P2. Dash-free overcorrection. Look for (since September 2026): no dashes at all plus uniformly comma-and-period sentences, short and of even length (the guide cites a strict 8 to 20 word band). Fix: vary sentence length and punctuation by what the meaning needs (colon, parentheses, semicolon, dash) and read aloud.
- P3. Curly quotes and apostrophes. Look for: curly “ ” ‘ ’ mixed with straight " ' in one text, or a different style than the rest of the site; curly apostrophes in contractions and possessives. Fix: pick one style for the whole site. Always use straight quotes inside code, URLs, HTML attributes, JSON-LD, meta tag values and CSS. Curly quotes alone are not proof of AI (Word, macOS and iOS create them), so look for inconsistency.
- P4. Wrong dash or hyphen. Look for: hyphen, en dash or em dash swapped for each other (hyphen where an em dash or en dash belongs, em dash where a comma belongs). Fix: hyphen for compounds, en dash for ranges, em dash only when needed.
- P5. Pasted bullet characters. Look for: `•`, `-`, `–`, `#`, or emoji at line starts as text, literal `1.` numbering with lost line breaks. Fix: rebuild with real list markup.

## C. Content patterns

- C1. Generic positive description in place of facts. Look for: stock praise ("a rich tapestry", "a vibrant community", "remarkable strides", "dependable experiences"), specific facts blurred into "a revolutionary titan of industry". Fix: restore the specific, unusual detail (what exactly, when, how many). Delete the sentence if no specific fact exists.
- C2. Undue emphasis on significance, legacy and trends. Look for: statements that an ordinary detail reflects, symbolizes or contributes to a broader topic; `was part of a broader movement`; `generated debate`; `shaped emerging policy discussions`; `prompted broader reflection`; `raising philosophical questions`; ecosystem or heritage ties that are tenuous; preambles that admit low importance and then argue importance. Fix: delete unless a source states the fact.
- C3. Superficial analysis via trailing participle phrases. Look for: a sentence ending in `, highlighting ...`, `, underscoring ...`, `, emphasizing ...`, `, ensuring ...`, `, reflecting ...`, `, symbolizing ...`, `, contributing to ...`, `, fostering ...`, `, showcasing ...`, `, enhancing ...`, `, encompassing ...`, `valuable insights`, `align/resonate with`. Fix: end the sentence at the fact. If analysis is needed, give it its own sentence, attributed to a named source, or delete.
- C4. Vague attributions. Look for: `Industry reports`, `Observers have cited`, `Experts argue`, `Some critics argue`, `several sources/publications` when few are cited, `according to [vague group] sources`, `described in scholarship`, `such as` before a short list that implies others. Fix: name the source, date and link; say "one study" if one; make lists exact.
- C5. Canned notability and media-coverage claims. Look for: `independent coverage`, `local/regional/national media outlets`, `trade publications`, `featured in X, Y and other media`, `cited/featured/profiled in`, `written by a leading expert`, `active social media presence`, `maintains a strong digital presence`, `was identified by`, `has also been mentioned in`, `significant, substantial, secondary coverage`. Fix: link each mention with outlet, title and date and say what it reported; delete descriptions of source type or prestige; delete social-presence claims.
- C6. Vague connection claims. See V7. Also check people and organization relationships: state role, dates and organization.
- C7. Negative parallelism. Look for: `not only ... but also ...`, `It is not just ..., it's ...`, `It's not ..., it's ...`, `no ..., no ..., just ...`, `not X but Y`, `rather than ...` closers, `Rather than simply ..., ...`, `not a mirror but a portal`, `doesn't just ...; it ...`, and the multi-sentence version ("... however, took a path that intertwined both ..."). Fix: state the positive claim directly. Keep a contrast only when a real misconception exists and you can say who holds it.
- C8. Outline-like challenge formula and speculation about the future. See S3. Also delete vague forward-looking closers (`continues to thrive`, `positions it as a critical component`, `could enhance its relevance`).
- C9. Claims of coverage, quality or sourcing without content. Look for: edit-summary or changelog style text that stresses "sourced", "verified", "independent sources" instead of saying what was added. Fix: say what was added or changed in concrete terms.
- C10. Fabricated or unverifiable references. Look for: dead links (404, nonexistent domains), unresolvable DOIs, invalid ISBNs (checksum), DOIs that open an unrelated paper, book citations with no page number or URL, generic textbook cited for a specific claim, a cited page that does not contain the claim. Fix: open every link and DOI; confirm the source says what the text says; remove anything you cannot verify. Link failures can be innocent (paywalls, login walls, mangled URLs), so check before concluding.
- C11. Unsupported specifics. Look for: names, dates, quotes, statistics, awards and prices with no source you opened. Fix: verify against a primary source or remove. This is the most reliable test in the guide.
- C12. Changelog, release-note and commit-message boilerplate. Look for: `ensured that ... adheres to`, `refined`, `enhanced`, `enriched`, `streamlined`, `improved`, `in compliance/complies with`, `clarity`, `flow`, `neutral tone`; `preserved/preserving`, `retained/retaining`, `avoided/avoiding`, `ensured/ensuring`, `aimed/aiming to`; mentions of unchanged material; `addressed reviewer/client feedback`; itemized parameter names. Fix: one specific sentence on what changed.
- C13. Lead sentence treating a generic title as a proper noun. Look for: `[Page title] refers to`, `[Page title] is a curated compilation of`, `The "[List name]" is ...`. Fix: begin with the subject itself in a natural sentence.

## M. Markup and chat artifacts

Any hit here is unambiguous. Fix the text, then re-verify all claims and links in the piece.

- M1. Chatbot correspondence. Look for: `Certainly!`, `Of course!`, `You're absolutely right!`, `I hope this helps`, `Would you like ...`, `is there anything else`, `let me know`, `more detailed breakdown`, `here is a ...`, `Feel free to personalize/customize it`, `Here's a template/draft you can use`, `Delete this section before submission`, advice addressed to the user ("ensure the content is presented in a neutral tone"), `... [check/verify/confirm] ... before [publishing/submitting]`, `a [site/article]-style ...`. Fix: delete the passage; rewrite what remains as the page's own text.
- M2. Chat logs, refusals and cutoffs. Look for: `You said:`, `ChatGPT said:`, `as an AI language model`, `as a large language model`, `I cannot ... but I can ...`, `I'm sorry`, `Up to my last training update`, `as of my last knowledge update`, a text that stops mid-sentence. Fix: delete; restore or rewrite the missing part, with sources.
- M3. Placeholders. Look for: `[Your Name]`, `[Company Name]`, `[Describe ...]`, `[brief reason]`, `[Year]`, `(Add your channel URL here)`, `(If available)`, `INSERT_SOURCE_URL_##`, `INSERT_WEBSITE_URL_HERE`, `PASTE_..._URL_HERE`, `SOURCE_PUBLISHER`, dates like `2025-XX-XX`, links to subpages of `example.com` (`example.com/source1`, `/article`, `/news`). Fix: fill with real values or remove. Search the rendered page and the source for square brackets, `XX`, `INSERT`, `PASTE`, `example.com`.
- M4. Markdown leftovers in a CMS or HTML. Look for: `**bold**` with visible asterisks, `## Heading` shown as text, `---` or `----` lines, `[text](url)` shown literally, triple backticks (often followed by a language label such as `wikitext`), `:::` fences. Fix: convert to real markup or remove; check that no code-fence or escape wrapper surrounds the whole text.
- M5. Chatbot citation and metadata tokens. Look for: `contentReference[oaicite:N]{index=N}`, `oai_citation`, source-name tails like `Wikipedia+1` and `IT Governance+3ISO+3`, `citeturn0search0`, `turn0image0`, `turn0news0`, `({"attribution":{"attributableIndex":"X-Y"}})`, `[cite: 1]`, `[span_1](start_span)`, `<mark>` wrapping phrases, `grok_card` or `<grok-card ...>`, `grok_render_citation_card_json`, `【85†L261-269】`, `[attached_file:1]`, `[web:1]`, `ppl-ai-file-upload`, `:::writing{variant="document" id="..."}`, `↩` footnote return characters, strange Private Use Area characters at sentence ends. Fix: delete the token, then find or add a real source for the claim it stood for.
- M6. AI-tool tracking parameters in URLs. Look for: `utm_source=openai`, `utm_source=chatgpt.com`, `utm_source=copilot.com`, `referrer=grok.com` in any link or reference. Fix: remove the parameter and check that the link works and supports the claim. The parameter proves the link came from an AI tool, not that the prose did.
- M7. Hidden comments. Look for: HTML comments (`<!-- ... -->`) that contain instructions, notes, TODOs or submission notes from a chatbot. Fix: strip all hidden comments from the source before publishing.
- M8. Email or form leftovers. Look for: `Subject:` lines, signature blocks, `Dear ...`. See S13.

## False-positive guards

Each of these alone does not indicate AI. Do not rewrite good copy because of one.

- Perfect grammar, formal register, "fancy" or academic words that are not on the lists, a mix of casual and formal tone, bland prose.
- Transition words in isolation (`Additionally`, `Consequently`, `Notably`).
- Unsourced content (older sites, pre-2023 text).
- Curly quotes alone (typographic software and operating systems create them); em dashes alone.
- Markdown syntax in developer documentation, READMEs and notes. Markdown shown inside rendered web copy is the problem.
- Salutations and sign-offs in genuine letters or emails.
- Repeated word avoidance by non-native writers.
- `highlight`, `underscore`, `landscape`, `concrete`, `robust`, `key` used in their literal senses; `has been featured`; `refers to` in a real glossary entry.
- Standard boilerplate placeholders in a CMS template or an `example.com` shown intentionally in documentation.
- Dead links from paywalls, logins or link rot on real sources.
- Text written before 30 November 2022 (ChatGPT public launch) is very unlikely to be AI-written.

## Signs documented but not transferable to web copy

Wikipedia-specific: broken categories and templates, nowiki wrapping, named-reference errors, DefaultSort and colon-letter loss, shortcut citations (`WP`), AfC submission notes, user-page userboxes, permissions gaming, edit-filter and noticeboard material. They remain in the notes for completeness.
