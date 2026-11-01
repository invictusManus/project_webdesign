# Signs of AI writing: Markup subpage notes

Sources: Wikipedia, "Wikipedia:Signs of AI writing/Markup" (revision 1382923809, 2026-10-31) and its sub-subpage "Wikipedia:Signs of AI writing/Wikitext wrapped in Markdown code blocks from chatbots" (revision 1379493064, 2026-10-10). Retrieved 2026-11-01. Text © Wikipedia contributors, CC BY-SA 4.0. These notes are an adaptation (summarized, restructured) and are licensed CC BY-SA 4.0. Not an official Wikipedia policy.

Structure: one `##` per page, `###` = section, `####` = subsection. Web relevance is high for the chatbot-artifact items: stray Markdown, citation tokens and tracking parameters survive copy/paste into any CMS.

## Wikipedia:Signs of AI writing/Markup
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Markup

### Lead
- Markup errors typical of chatbots, with real examples. Wikipedia uses wikitext, a niche markup language.

### Use of Markdown
- Chatbots default to Markdown, far more common than wikitext. System prompts often tell them to format headings and lists in Markdown (the page quotes a 2024 Claude system prompt about `#` headers, asterisks or underscores for emphasis and list markers).
- Markdown versus wikitext: asterisks or underscores instead of single quotes for bold and italic; `#` instead of `=` for headings; parentheses instead of square brackets around URLs; `---`, `***` or `___` instead of `----` for thematic breaks.
- Asked to "generate an article", chatbots often output Markdown; copy buttons may preserve it. A chatbot may offer "turn this into actual Wikipedia markup format (`wikitext`)" and then produce rudimentary or broken wikitext, often inside a fenced code block with leading ```` ```wikitext ````.
- Faulty wikitext mixed with Markdown, especially a fenced code block, is a strong indicator. Markdown alone is not: developers, researchers, technical writers and experienced users write Markdown in Obsidian, GitHub, Reddit, Discord, Slack, iOS Notes, Google Docs, Windows Notepad. New editors may assume Wikipedia accepts Markdown.
#### Misuse of asterisks
- Text wrapped in `**double asterisks**` meant as bold, left visible. Example: `**summary rejection**`, `**speculation about motive**`.
#### Misuse of number signs
- `##` used for section headings. In wikitext it makes a numbered list. Example: `## Geography`, `## History`, `## Administration`, `## Population`.
#### Unusual link formatting
- External links as `[Example](example.com)` instead of `[example.com this]`. Seen in Gemini-style citation formatting. Examples: `[here](https://en.wikipedia.org/wiki/Special:Contributions/...)`, `[talk page](...)`, and URL-in-brackets followed by the URL in parentheses.
#### Thematic breaks between sections
- `----` or `---` between every section. Exception: AfC templates include a `---` separator by default.
- Examples: a draft with `----` after every section and level 1 headings.

### Broken wikitext
- Chatbots are weak at wikitext and templates and produce faulty syntax. Notable case: garbled code for the AfC submission template (a category string full of timestamp fragments).
#### Omission of colon-letter strings
- When pasting chatbot output with magic words or links to non-article pages, users lose the colon and the word right after it. `{{DEFAULTSORT:Doe, John}}` becomes `{{DEFAULTSORT, John}}`; `[[:Category:Living people]]` becomes `[[Category people]]`; `Draft:Name` loses `Draft`; `WP:SHORTCUT` becomes just `WP`. Colon-number strings are unaffected.
- Examples: `[[Category people]]`, `[[Category civil engineers]]`, `[[Category of Lagos alumni]]`, `I respectfully contest the proposed speedy deletion of Draft of Lives (2026 film)`.
#### Entire articles wrapped in nowiki tags
- Copying from certain ChatGPT UI blocks puts HTML on the clipboard too; VisualEditor parses the HTML first and escapes markup, so `<nowiki>` tags show up around the whole article. If the entire page is wrapped, it was almost certainly pasted whole, most likely from ChatGPT.

### Internal formatting and reference markup bugs
- Chatbots leak internal formatting metadata, an unambiguous AI indicator. Patterns differ per tool.
#### ChatGPT: contentReference, oaicite/oai_citation, +1, turn0search0, attributableIndex
- `:contentReference[oaicite:0]{index=0}` in place of reference links; `Example+1` style tails; `oai_citation` (for example `[oai_citation:0‡wellington.scoop.co.nz](...)`); combined source name lists such as `IT Governance+3ISO+3ISO+3`, `Wikipedia+1`, `Ignyte+3Microsoft Learn+3Google Cloud+3`.
- `citeturn0search0` (wrapped in Private Use Area Unicode) at sentence ends, with the number after "search" rising through the text; a shorter form with only a number in PUA characters; image sets as `iturn0image0turn0image1...`; rarer `citeturn0news0`, `citeturn1file0`, `cite` plus a generated identifier. First seen February 2025. Occasionally appears as a ref name such as `0search12`.
- JSON tails: `({"attribution":{"attributableIndex":"X-Y"}})` with rising indices, often with caret-bracket sentence wrappers (`^[...]`).
- Also `utm_source=chatgpt.com` inside URLs (see the main page's utm_source section).
#### Gemini: `[cite: 1]`, `[span_1](start_span)`, HTML mark tags
- Reference markers `[1, 2]` or `[3, 12, 13]`, sometimes `[cite: 2, 6]`, and `[span_1](start_span)` ... `[span_1](end_span)`. In VisualEditor, URLs may appear inside the brackets with the number.
##### Unusual text highlighting
- Text pasted from Gemini into VisualEditor may be wrapped in `<mark>...</mark>` and render highlighted: a remnant of Gemini's "Double-check response" highlighting. Examples show whole descriptive phrases wrapped (`<mark>prominent Australian nun and educator</mark>`, `<mark>celebrated Pakistani Punjabi folk singer</mark>`).
#### Grok: grok_card, grok_render_citation_card_json
- XML-like `<grok-card data-id="..." data-type="citation_card">` tags after citations, and `[](grok_render_citation_card_json={"cardIds":["..."]})` in place of links.
#### DeepSeek: lenticular brackets, dagger symbols
- As of June 2025, citation markers like `【85†L261-269】` (lenticular brackets, dagger, line ranges), specific to DeepSeek and derivatives. The page's examples also show source names run into the text with no space (`medway.gov.ukmedway.gov.uk`) and non-breaking hyphens in compounds (`singer‑songwriter`); the page does not call these signs, so treat them as observations only.
#### Perplexity: attached_file, ppl-ai-file-upload
- As of fall 2025, tags such as `[attached_file:1]` and `[web:1]` at sentence ends; citations to an Amazon S3 bucket with `ppl-ai-file-upload` in the URL.
#### Unclassified: :::writing
- As of 1 June 2026, markup like `:::writing{variant="document" id="[NUMBER]"}` (random 5-digit number), with closing `:::`, possibly in other languages (for example `:::écriture{variante="document" ...}`).

### Non-existent or out-of-place categories
- LLMs hallucinate plausible-sounding categories (like SEO keywords) or use obsolete ones, producing red links; recent models may drop words (`[[Category people]]`).
- Not proof alone: humans make similar mistakes. It corroborates other AI signs. The dropped-words form is a strong AI tell, since humans rarely make it.

### Non-existent templates
- Hallucinated templates (especially plausible infobox types) and parameters. Red links; unknown parameters in real templates do nothing. Templates deleted after the model's knowledge cutoff also appear. Example: `Infobox ancient population` where the real one is `Infobox archaeological culture`. Non-infobox example: an `Update submission` template with an invented `reasons` parameter.

### See also
- Main page, Style subpage, comments page.

## Wikipedia:Signs of AI writing/Wikitext wrapped in Markdown code blocks from chatbots
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Wikitext_wrapped_in_Markdown_code_blocks_from_chatbots

### Lead
- Chatbots wrap a block of text in a Markdown code fence of three backticks with a language label (here, wikitext). Users copy the leading ```` ```wiki ````, the trailing ```` ``` ````, or both.
- Typical surrounding chatter: `Certainly! Here is your Wikipedia-style draft, formatted in wikitext and ready to copied and pasted into Wikipedia!` and `Would you like me to add some fictional references for you?`
- The leading marker may carry an extra parameter (```` ```wiki id=deadbeef00 ````), may omit the language label, or use another (`mediawiki`, `wikitext`).
- The trailing marker is seen more often, probably because users miss it more easily.

### Common objections
- Excuses reported (paraphrased): "It is a spell checker/grammar checker"; "I wrote it in a code editor".

### Examples
- The page lists revisions of real pages that carried the leading and trailing markers, and some with only the trailing marker. Not reproduced here.

### See also
- The Markdown section above.
