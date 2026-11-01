# Signs of AI writing: Style subpage notes

Source: Wikipedia, "Wikipedia:Signs of AI writing/Style" (WikiProject AI Cleanup). Retrieved 2026-11-01; revision 1382924605 (2026-10-31). Text © Wikipedia contributors, CC BY-SA 4.0. These notes are an adaptation (summarized, restructured) and are licensed CC BY-SA 4.0. Not an official Wikipedia policy.

Structure: `###` = section of the source page, `####` = its subsections. Page summary in the main page's "Style" section: see [`signs-of-ai-writing.md`](signs-of-ai-writing.md).

## Wikipedia:Signs of AI writing/Style
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style

### Lead
- A list of style errors typical of AI chatbots, with real examples from Wikipedia pages. Wikipedia-specific advice is linked to the Manual of Style, not given here.

### Title case
- In section headings, chatbots strongly tend to capitalize all main words (title case) instead of sentence case.
- Examples: `Impact of Technology and Digitalization`, `Sustainable Development and Environmental Law`, `Human Rights and Economic Law`.
- Web relevance: headings, navigation labels and button text capitalized word by word.

### Overuse of boldface
- Chatbots bold phrases mechanically and excessively. The habit comes from readmes, fan wikis, how-tos, sales pitches, slide decks, listicles and similar material. They tend to emphasize every instance of a chosen word or phrase, often in a "key takeaways" style.
- Some newer models and apps are instructed to avoid it, so absence proves nothing.
- Examples: a finance definition with bold on `leveraged buyout (LBO)`, `debt financing`, `private equity firms`, `financial sponsors`, `assets and future cash flows`; a list description bolding `Productive Years`, `P(doom)`, `one-sentence summary of their contribution to AI Safety`.

### Inline-header vertical lists
- A bulleted or numbered list where each marker is followed by a bold header, a colon, then descriptive text.
- When copied as screen text the formatting breaks: the marker may become a bullet character (•), hyphen, en dash, hash (#), emoji or similar; ordered lists keep literal numbers (`1.`); line breaks may disappear.
- Examples: `Conflict of Interest (COI)/Autobiography:`, `Notability (GNG and NPOLITICIAN):`; `1. Historical Context Post-WWII Era:` through `10. Questions to Consider`; `Key highlights:` followed by `Route Details`, `Bypasses and Improvements`, `Timeline and Impact`; a run-together paragraph of bold headers (`Mass Content Removal:`, `Disruptive Tagging:`, `Refusal to engage`, `Context:`); `SEO (Search Engine Optimization):`, `AEO (Answer Engine Optimization):`, `GEO (Generative Engine Optimization):`.
- Variant: no punctuation after the entry title, only the title in bold or on its own line (`Durability`, `Portability and the "Pocket Meal"`, `The Fire Hazard`). Do not confuse with how people bold Keep or Delete in deletion discussions.
- Web relevance: feature lists, benefit lists and FAQ-style blocks built as "Bold label: sentence".

### Heading errors
#### Title heading
- Chatbots put a heading with the article name before the content, not imagining that the title already exists. Example: a level 1 heading holding the page name.
#### Skipping heading levels
- Chatbots skip level 2 and start sections at level 3. This breaks accessibility and style conventions, so a manually formatted page rarely has it.
#### Overuse of level 1 headings
- Level 1 headings are normally reserved for the page title. Chatbots may use several (possibly from translating Markdown `#` to wikitext). Example: `= History =`, `= Programming =`, `= Main Characters =`, `= Educational Goals =`, `= Style =`, `= Target Audience =`, `= External Links =`.
- Web relevance: more than one `h1`, or heading levels skipped (`h1` then `h3`).
#### Headings only containing other headings
- A heading that holds only subheadings and no text of its own. Example: level 1 `Programming` directly followed by level 2 `Pixy's Adventure Club`.

### Emoji as formatting
- Chatbots have put emoji in front of section headings and bullet points. Mostly seen in talk comments and edit summaries; rarer now but still occurring.
- Examples: `👋 Welcome to ...`, `🧑‍💻 About Me`, `🌏 My Interests`, `🎯 What I'm Working On`, `📬 Let's Connect!`, `🙏 Gratitude`; analysis blocks starting `🧠 Cognitive Dissonance Pattern:`, `🧱 Structural Gatekeeping:`, `🚨 Underlying Motivation:`, `🧭 What You're Actually Dealing With:`; numbered history sections with a different emoji each; `🌍 My Mission:`, `📚 My Interests:`, `🤝 My Goals on Wikipedia:`.

### Unusual use of tables
- Small, minimally formatted tables that would read better as prose or an infobox. Examples: a two-column "Key Statistics" table with three rows; a two-column name and designation table; side-by-side comparison tables (Feature, Material, Use, Transmission) for two items.
- Chatbots sometimes insert Markdown table syntax inside wikitables, producing garbled output.

### Curly quotation marks and apostrophes
- ChatGPT and DeepSeek typically use curly quotation marks (“...” or ‘...’) and the curly apostrophe (’) instead of straight ones (" ' and the typewriter apostrophe), including in contractions and possessives. They may mix curly and straight inconsistently within one response.
- Curly quotes alone do not prove LLM use. Causes of human curly quotes: Chicago Manual of Style typography; Microsoft Word smart quotes; the default system-wide setting on macOS and iOS (except some apps or when disabled, as programmers do); grammar tools such as LanguageTool; citation tools copying titles from web pages; professionally typeset newspapers. Some fonts show curly apostrophes as straight, making the difference invisible.
- Gemini and Claude models typically do not use curly quotes.
- Web relevance: mixed curly and straight quotes in one text, or curly apostrophes pasted into code, URLs or attributes.

### See also
- Main page, the Markup subpage and the comments page (see [`README.md`](README.md)).
