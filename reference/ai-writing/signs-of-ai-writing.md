# Signs of AI writing: main page notes

Source: Wikipedia, "Wikipedia:Signs of AI writing" (WikiProject AI Cleanup field guide). Retrieved 2026-11-01; revision 1383029935 (2026-10-31). Text © Wikipedia contributors, CC BY-SA 4.0. These notes are an adaptation (summarized, restructured) and are licensed CC BY-SA 4.0. Not an official Wikipedia policy. Indicator words and phrases are kept exact.

Structure: `###` = top-level section of the source page, `####` and `#####` = its subsections. The page is written for Wikipedia editors, so web-copy relevance is noted where a sign transfers. Related pages (Style, Markup, comments, user pages, buzzspeak) have their own files; see [`README.md`](README.md).

## Wikipedia:Signs of AI writing
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### Lead: purpose, scope and reading rules
- A field guide to writing and formatting conventions typical of AI chatbots such as ChatGPT, with real examples from Wikipedia articles, drafts, comments and other content. Aim: detect undisclosed AI-generated content on Wikipedia.
- Some signs apply broadly, some do not outside Wikipedia. The guide is less useful for non-informational writing. Fiction-specific tells (whispering woods, the name Elara Voss, etc.) are deliberately not listed.
- Not all text with these indicators is AI-generated. LLMs are trained on human writing, including Wikipedia. Many elements also appear in editorials, blogs and fan fiction.
- The list is descriptive, not prescriptive: observations, not rules. Style advice belongs to Wikipedia's policies and Manual of Style.
- The patterns are signs of a problem, not the problem itself. Easy fixes (excess boldface, broken markup, citation quirks) can point to deeper issues with serious policy risk (unverifiable claims, fabricated sources, neutrality). Instruction in the source, in bold: do not merely treat the signs as the problems to fix, because that can make detection harder. Address the deeper concerns.
- Speedy deletion criterion G15 (unambiguously LLM-generated pages) lists only the most objective signs. The rest of the signs here are not enough on their own for deletion.
- As of October 2026 the most common signs of newly AI-generated text on Wikipedia, besides the unambiguous ones: Markdown presence, AI edit summaries, hedging disclaimers about source availability and usage, vague expression of connection or association, canned emphasis on source attribution and media coverage.

### Caveats

#### AI detection tools
- Do not rely solely on tools such as GPTZero and Pangram. They beat random chance but have non-trivial error rates.
- Detectors are fragile: paraphrasing, markup changes, spacing changes and models unseen in training all reduce accuracy.
- A high detector percentage is not a valid criterion for G15 speedy deletion.

#### Your detection ability
- Do not over-trust personal judgment. A 2025 study found human ability to separate LLM text from human text no better than chance.
- A 2025 study on German theses: 57% recognition of AI texts, 64% of human texts.
- A 2025 preprint: expert annotators (heavy LLM users) correctly flagged 90% of AI text and wrongly flagged 3.3% of human text. Light LLM users did only slightly better than chance in both directions.
- Human speech and writing is being shaped by LLMs (evidence in 2024 podcast speech, academic writing, semantics, word choice), so the two converge. That process lags and is patchy. The reverse does not hold: LLM output is not becoming more like human writing.
- The page links a quiz (Wikipedia:AI or not quiz) for practice.

### Content
- Mechanism: LLMs predict the statistically likely continuation, so output regresses to the mean, toward what fits the widest range of cases. A second tuning round (reinforcement learning from human feedback) pushes output toward broadly palatable prose. Strength and tell at once.
- Training data describes famous people in positive, important-sounding language. The LLM drops specific, unusual, nuanced facts (statistically rare) and substitutes generic positive description (common). Example: "inventor of the first train-coupling device" becomes "a revolutionary titan of industry".
- Image analogy: the subject gets louder (more exaggerated) while the picture blurs (less specific), like image generators that make fine details blurry.
- Core tell: smoothing of specific facts into generic statements that would fit many topics.

#### Undue emphasis on significance, legacy, and broader trends
Words to watch: `stands/serves as`, `is a testament/reminder`, `a crucial/pivotal/vital/significant/key role/moment`, `underscores/highlights its importance/significance`, `reflects broader`, `symbolizing its ongoing/enduring/lasting`, `contributing to the`, `setting the stage for`, `marking/shaping the`, `represents/marks a shift`, `key turning point`, `evolving landscape`, `focal point`, `indelible mark`, `deeply rooted`, `distinction [matters/is important] because`.
- LLMs puff up a topic by stating that arbitrary aspects of it represent or contribute to a broader topic, using a distinct, recognizable repertoire.
- Examples from the source: `marking a pivotal moment`, `represented a significant shift`, `was part of a broader movement`, `an important center`, `solidify its role as a regional hub`, `This etymology highlights the enduring legacy`, `the transformative power of unity`, `contributes to the broader history`, `reflects the influence of`.
- Debate framing: subjects placed amid "debates" or said to have "participated in public discussions". Examples: `generated debate`, `shaped emerging policy discussions`, `prompted broader reflection`, `raising philosophical questions`.
- Appears even for mundane subjects (etymology, population data). Sometimes a hedging preamble admits low importance, then argues importance anyway (`Though it saw only limited application, it contributes to the broader history`).
- Biology pattern: over-emphasis on ties to the broader ecosystem, even when tenuous; belaboring conservation status and preservation efforts even when status is unknown and no efforts exist. Examples: `there is no specific conservation assessment ... crucial for the survival of this and other endemic species`, `plays a role in the ecosystem`, `contributes to Hawaii's rich cultural heritage`, `Preserving this endemic species is vital`.
- As of mid-2026, these often arrive together with hedging disclaimers, editorializing about why a distinction or nuance matters.

#### Canned emphasis on notability, attribution, and media coverage
Words to watch: `independent coverage`, `local/regional/national/[country name] media outlets`, `music/business/tech outlets`, `trade publications`, `cited/featured/profiled in`, `written by a leading expert`, `active social media presence`, `was identified by`.
- LLMs try to prove notability by announcing it, listing the outlets that covered a subject and what type they are (trade publications, regional media). They often misattribute their own superficial analysis to the source. More common in tools released in 2025 or later.
- Narrow and distinct from human press releases: the focus is on characteristics of the sources themselves (content, public availability, classification in the media landscape), in idiosyncratic phrasing. Output can echo guideline wording such as "independent coverage", as if justification leaked into the text.
- `maintain an active social media presence` and similar: idiosyncratic to AI text, rare on Wikipedia before about 2024.
- Examples: `featured in Vogue, Wired, Toronto Star, and other media`; `other prominent media outlets`; `documented in archived school event programs and regional press coverage`; `maintains a strong digital presence`; `has also been mentioned in ABC News coverage relating to` (the cited reference did not exist); `profiled in multiple high-quality, independent, and widely-read outlets`; `significant, substantial, secondary coverage, not trivial mentions or press releases`; `Repeated national media coverage`; `reported by`; `highlighted by multiple independent reports`; `recognised by universities, specialist publications`; `Ongoing public presence in respected media`; `significant, sustained, and verifiable coverage`.

#### Superficial analyses
Words to watch: `highlighting/underscoring/emphasizing ...`, `ensuring ...`, `reflecting/symbolizing ...`, `contributing to ...`, `cultivating/fostering ...`, `encompassing ...`, `enhancing ...`, `valuable insights`, `align/resonate with`.
- Chatbots attach superficial analysis about significance, recognition or impact, usually as a trailing present-participle ("-ing") phrase at the end of a sentence, sometimes with vague attribution to third parties.
- On Wikipedia such comments are synthesis or unattributed opinion. Chatbots with web search may pin them on named sources ("Roger Ebert highlighted the lasting influence") whether or not the source says so.
- Source examples (participle tails): `creating a lively community within its borders`; `further enhancing its significance as a dynamic hub of activity and culture`; `offering a diverse range of experiences against the backdrop of`; `serving as a major railway hub with historical significance`; `facilitating the movement of passengers and goods`; `contributing to the socio-economic development of the region`; `reflecting its continued relevance in the regional and national transportation landscape`; `emphasizing the importance of solidarity and collective action`; `shaping their values, community structures`; `driving a commitment to empowerment and social change that echoes through generations`; `stands as a counter-symbol, emphasizing unity, togetherness, and transcendent faith`; `fosters a sense of connection and shared purpose`; `embodying the spirit of unity`; `underscores its role in bringing together`; `reflecting the rich culture and landscape`; `celebrate the area's agricultural roots`; `resonates with the region's natural beauty`; `evoke enduring faith and resilience`; `creating a space where the past and present come together`; `highlighting their historical and pedagogical significance`; `demonstrating the ongoing relevance of his research`; `confirming its relevance`; `illustrate Blois' lasting influence`; `a perspective that still fuels linguistic debates today`; `demonstrates the enduring relevance`.
- July 2026 case: a chatbot offering "neutral" paraphrases each ended with a participle clause (`reflecting the public image ...`, `underscoring the image ...`, `highlighting the image ...`).

#### Promotional and advertisement-like language
Words to watch: `boasts a`, `vibrant`, `rich`, `profound`, `enhancing`, `showcasing`, `exemplifies`, `commitment to`, `natural beauty`, `nestled`, `in the heart of`, `groundbreaking`, `renowned`, `featuring`, `diverse array`.
- LLMs struggle with neutral tone. Even when told to write encyclopedically they drift to ad copy or travel-guide prose, whether generating or rewriting. An edit summary can claim "removed promotional tone" while adding it. Happens without any intent to advertise.
- Caveat: not all promotional or spammy writing is AI. The tell is the same phrase set recurring regardless of topic. Older models (GPT-4) are blatantly positive; newer ones are subtly positive and avoid obvious superlatives like "the best".
##### Subtypes: cultural heritage
- LLMs keep reminding the reader of importance. Examples: `Nestled within the breathtaking region`; `stands as a vibrant town with a rich cultural heritage and a significant place`; `From its scenic landscapes to its historical landmarks`; `offers visitors a fascinating glimpse into the diverse tapestry`; `unique characteristics`; `a town worth visiting`; `celebrated for its resilience, cultural richness, and natural beauty`; `it has made remarkable strides in human development`; `make Bangladesh ecologically unique`; `deep-rooted tradition of literature, music, and art`; `a pivotal moment in its identity`; `offers a dynamic blend of tradition and progress that continues to inspire the world`; `acts as the gateway`; `diverse attractions`; `every traveller's journey`; `dependable, value-driven experiences`; `rich history, spiritual heritage, and natural beauty`.
##### Subtypes: people and companies
- Press-release or commercial tone. Examples: `align with KQ's goals of reducing its environmental footprint`; `emphasized the airline's commitment to sustainability, customer focus`; `communicates a powerful emotional presence, staying true to Cadillac's signature bold proportions`; `enhances accessibility`; `accentuate the vehicle's overall length`; `imparts a sense of refined dynamism`; `reinforcing the car's cohesive and elegant design`; `preserving the vehicle's clean and modern profile`; `thoughtfully revived`; `showcasing the brand's dedication to craftsmanship and historical reverence`.

#### Vague expression of connection or association
Words to watch: `in connection with/to ...`, `connected with/to`, `in association with ...`, `associated with`.
- Instead of stating a relationship directly ("In 2017, John Doe was the CEO of ExampleCorp"), LLMs allude to it ("sources identified John Doe as being associated with leadership of ExampleCorp"; "Professor Jane Doe was connected with science education at Example University").
- Often mixed with promotional buzzspeak and generic AI vocabulary (`particularly associated`, `widely associated`), sometimes repeated within one draft.
- Source examples: `in connection with the "Grammaire Blois"`; `has been associated with residential water management applications`; `referenced the inventor in connection with environmental award recognition`; `Uses associated with the patented method`; `associated principally with`; `is associated with the Rajhans Orchestra`; `became associated with musical education`; `Contemporary material associated with the ensemble`; `organised in connection with celebrations of`.
- Very frequent as of 2026 (named among the five most common signs).

#### Vague attributions and overgeneralization of opinions
Words to watch: `Industry reports`, `Observers have cited`, `Experts argue`, `Some critics argue`, `several sources/publications` (when only a few are cited), `such as` (before exhaustive word lists).
- Weasel wording: opinions credited to a vague authority. Source count is inflated: one or two sources presented as widely held; "reviewers" or "scholars" in the plural with one person cited; lists framed as non-exhaustive when sources show no other examples.
- Source examples: `of interest to researchers and conservationists`; `according to Indian sources`; `described in scholarship`; `modern researchers treat`; `Toy industry publications such as`.

#### Outline-like conclusions about challenges and future prospects
Words to watch: `Despite its... faces several challenges...`, `Despite these challenges`, `Challenges and Legacy`, `Future Outlook`.
- Many LLM articles end with a "Challenges" section opening "Despite its [positive words], [subject] faces challenges..." and closing with a vaguely positive verdict or speculation about initiatives that could help. Often part of a rigid outline that also has "Future Prospects".
- Caveat: the sign is the rigid formula, not any mention of challenges.
- Source examples: `Challenges and Future Directions`; `faces new challenges and opportunities`; `adapt to these emerging trends`; `faces several challenges, including`; `continues to thrive`; `Despite these challenges`; `continue to provide a vital service`; `positions them as critical components for sustainable energy solutions`; `Future investments in technology ... could enhance the canal's efficiency`; `continues to evolve in response to these challenges`; `future challenges`; `main contemporary challenge`; `for the coming decades`.

#### "Awards and recognition" section
- Headers shaped "X and Y" are common (not exclusive) in AI text. "Awards and recognition" (and bare "Recognition") is near-ubiquitous in AI articles and far more common than in human writing, even versus articles tagged promotional.
- It reflects AI focus on legacy and trends and its vague allusion to "coverage" or "recognition" by outlets.

### Language and grammar
- AI text shows consistent syntax, word-choice and sentence-construction patterns that human writing does not show to the same degree, and struggles to match some human patterns. Models differ: GPT-4o (ChatGPT May 2024 to August 2025) deviates from human writing more than contemporaries.
- The patterns are topic-independent, which gives AI text an identifiable "voice".

#### High density of "AI vocabulary" words
Words to watch: `Additionally` (especially starting a sentence), `align with`, `boasts` (meaning "has"), `bolstered`, `crucial`, `deep dive`, `delve`, `emphasizing`, `enduring`, `enhance`, `fostering`, `garner`, `highlight` (as a verb), `interplay`, `intricate/intricacies`, `landscape` (as an abstract noun), `meticulous/meticulously`, `pivotal`, `robust`, `showcase`, `tapestry` (as an abstract noun), `testament`, `underscore` (as a verb), `valuable`, `vibrant`.
- Studies show overuse of specific words in text after 2022 (public chatbot era). They co-occur: where there is one, expect others. Also seen in LLM encyclopedias such as Grokipedia.
- One or two such words in an edit may be coincidence. An edit (post-2022) with many of them, many times, is one of the strongest tells.
- Words change over time: `delve` peaked in 2023 and early 2024, fell later in 2024, dropped sharply in 2025.
##### Words by LLM era (approximate, not hard cutoffs)
- 2023 to mid-2024 (GPT-4): `Additionally`, `boasts`, `bolstered`, `crucial`, `delve`, `emphasizing`, `enduring`, `garner`, `intricate/intricacies`, `interplay`, `key`, `landscape`, `meticulously`, `pivotal`, `underscore`, `tapestry`, `testament`, `valuable`, `vibrant`.
- Mid-2024 to mid-2025 (GPT-4o): `align with`, `bolstered`, `crucial`, `emphasizing`, `enhance`, `enduring`, `fostering`, `highlighting`, `pivotal`, `showcasing`, `underscore`, `vibrant`.
- Mid-2025 to mid-2026 (GPT-5): `emphasizing`, `enhance`, `highlighting`, `showcasing`, plus the vocabulary of canned notability and attribution emphasis.
- Mid-2026 onward (GPT-6): `challenge`, `clearer`, `dependable`, `echoed`, `foster`, `leverage`, `matters`, `multifaceted`, `practical`, `prioritize`, `quietly`, `steady`, `universally`. Accompanied by more period and comma use and shorter sentences held to a strict 8 to 20 word range. (Backed by a single review-site source in the page.)
- Chatbot differences: Grok overuses pseudo-scientific words such as `causal`, `empirical`, `correlate` and still overuses `underscore` as of 2026.
##### Reading rules for the word list
- Take the list literally. A word being overused does not mean its synonyms are. Mind context: `underscore` can mean a literal underline mark or incidental music.
##### Examples (words flagged in source examples)
- Howdy Modi revision: `showcasing`, `highlighted`, `emphasizing`, `fostering`, `underscored`.
- Mosque inscriptions revision: `valuable`, `key`, `highlight`, `emphasize`, `highlights`, `underscores`, `enduring`.
- Somali cuisine revision: `intricate`, `tapestry` (three times), `vibrant`, `Additionally,` (twice), `enduring testament`, `landscape`, `showcasing`, `pivotal`.

#### Avoidance of basic copulatives ("is"/"are" phrases)
Words to watch: `serves as/stands as/marks/functions as/operates as/represents [a]`, `boasts/features/maintains/offers [a]`, `refers to`.
- LLMs replace plain "is"/"are" with `serves as a`, `mark the` and similar. Seen in GPT and Gemini models. One study found a drop of more than 10% in "is"/"are" in academic writing in 2023, with no earlier change.
- They also prefer marketing-flavored verbs (`features`, `offers`) to the neutral `has`. Do not confuse with present perfect (`has been featured`).
- Newer output links this to vague connection: `ventured into politics as a candidate` versus `was a candidate`; `began his career as` versus `was`.
- Wikipedia shows the same decline, after controlling for lead sentences. AI copyedits "improve" text this way. In a test, GPT-3.5 asked to "Revise the following sentence" used "is"/"are" less often.
- In leads, `refers to` treats the article as being about the word instead of the subject.
- Source diffs: `is LAAA's exhibition arm` became `serves as LAAA's exhibition space`; `There are four individual gallery spaces` became `The gallery features four separate spaces`; `is the first and oldest Malay-language tabloid` became `holds the distinction of being the first and oldest`.

#### Negative parallelisms
- LLM output often reads as correcting a misconception or an incomplete conclusion, retroactively adding a trait alongside or instead of one already mentioned. Humans use it too (myth-busting listicles) but it is a stereotypical AI sign.
##### Not just X, but also Y
- Constructions with "not", "but", "however": `Not only ... but ...`, `It is not just ..., it's ...`.
- Source examples: `not only dismissive but also unnecessarily harsh`; `doesn't just undermine the editor's argument; it questions their very right`; `should be encouraged, not belittled`; `not just dismissive, they're outright disrespectful`; `not only discourage participation but also damage`; `not only a work of self-representation, but a visual document`; `isn't just sourcing, it's framing`; `doesn't mean it doesn't exist`; `Movements evolve before they're neatly labelled`; `That's not just a sourcing issue, it's a systemic bias`; `Rather than simply retelling a classical legend, the film adapts`; `not only from its digital animation and visual spectacle, but also from its ability`.
- Can span sentences: `He hailed from the esteemed Duse family ... Eugenio's life, however, took a path that intertwined both personal ambition and familial complexities.`
##### Not X, but Y
- States the item lacks the first trait entirely: `It's not ..., it's ...`, `no ..., no ..., just ...`.
- Source examples: `is not grounded in visual mastery, but in`; `This dispersal is not dissolution. Rather, it constitutes`; `not a mirror but a portal`; `not a representation of self, but a mechanism`; `This isn't WP:NBIO, it's WP:1EVENT in disguise`; `Not a career, not a body of work, not sustained relevance, just an algorithmic moment`; `the topic is not who ..., it's whether`; `This ain't bludgeoning, it's surgical teardown`.
##### Y rather than X
- Reversed form, particularly common in recent output. Examples: `prioritizing empirical consolidation of power amid fragmented loyalties rather than ideological purity`; `Rather than introducing a new decompiler, REA acts as an interface`; `a bridge between AI coding agents and existing reverse-engineering tools rather than a replacement for conventional disassemblers`.

#### Leads treating Wikipedia lists or broad article titles as proper nouns
- First sentence introduces the title as a real-world entity when it is a list or generic title. Wikipedia style permits the title in the first sentence "in a natural way", but AI leads are unnatural.
- Examples: `Catchment area (health) refers to`; `EuroGames editions is the chronological list of`; `The "List of songs about Mexico" is a curated compilation of`.
- Web relevance: low (encyclopedia lead convention).

#### Rule of three
- LLMs overuse triplets: "adjective, adjective, adjective" or "short phrase, short phrase, and short phrase". Used to make superficial analyses look comprehensive.
- Stronger when it shows up where nobody bothers with flourishes, such as edit summaries.
- Source examples: `tiles, metals, and plastics`; `drywall, plywood, and other construction materials`; `electrical outlets, switches, and plumbing fixtures`; `model making, woodworking, and other craft projects`; `mythological image, magical weapons, and spirit of resistance`; `contemporary values, modern aesthetics, and digital animation technology`. Several of those sat inside canned-format Markdown lists.

### Style
- Short summary of the Style subpage (full notes in [`signs-style.md`](signs-style.md)): title case instead of sentence case in headings; overuse of boldface, sometimes with misused asterisks; inline-header vertical lists; wrong heading levels (a level 1 heading with the title, multiple level 1 headings); emoji at the start of headings or list entries; curly quotation marks and apostrophes instead of straight ones.

### Communication intended for the user

#### Collaborative communication
Words to watch: `a Wikipedia-style article`, `I hope this helps`, `Of course!`, `Certainly!`, `You're absolutely right!`, `Would you like...`, `is there anything else`, `let me know`, `more detailed breakdown`, `here is a`, and phrases like `..., [check/verify/confirm]... ...before [publishing/publication/submitting]`.
- Editors paste chatbot correspondence, prewriting or advice as if it were article content, in text or in hidden comments.
- Source examples: report-style scaffolding (`In this section, we will discuss the background information related to the topic of the report`); advice to the user (`ensure that the content is presented in a neutral tone, supported by reliable sources`); `Here's a template for your wiki user page. You can copy and paste this`; advice on adding photos and maps phrased as suggestions; an answer cut off mid-sentence (`Final important tip: The ~~~~ at the very end is Wikipedia markup that automatically`); `List the areas you want to contribute to. Example: ...`; `Delete this section before submission`; HTML comments with submission notes and conflict-of-interest instructions; `Before creating a real Wikipedia page ... your channel should ideally have: Over 100,000 subscribers`.

#### Hedging disclaimers about source availability and recommended usage
Words to watch: `While specific details are limited/scarce...`, `not widely available/documented/disclosed`, `...in the provided/available sources / search results...`, `[claim] should be [treated/presented] as... rather than...`, `based on available information`, `...does not by itself establish...`.
- Chatbots fill perceived gaps by pointing at the gap or adding cautionary disclaimers.
##### 2023-24: didactic disclaimers
- Older LLMs (~2023) added didactic "important to note" disclaimers: advice to an imagined reader on safety or controversial topics, or on locale-dependent topics. They appear as "partial refusals" in the GPT-4 system card.
- Examples: `However, it's important to note ... may vary`; `It is crucial to differentiate ... to prevent confusion`; `It's important to remember that what's free in one country might not be free in another, so always check before you use something`.
##### 2024-25: missing-source statements
- Chatbots with web search fail to find sources or information in provided sources and say the information is not public. They may add what it "likely" is and why it matters. All speculative, including the claim it is "not documented", and may be fabricated. For personal life: `maintains a low profile`, `keeps personal details private` (also speculative).
- Examples: `aren't widely documented`; `is limited in the provided search results ... the mountain likely supports`; `are not extensively documented in readily available sources`; `Below is a detailed overview based on available information`; `not widely transcribed on major sites like Genius or AZLyrics`; `My analysis is based on available track titles`; `I've inferred common motifs from similar trap tracks`; `lyrics and production details aren't fully documented in public sources`.
##### Mid-2026-present: corrective framings
- Chatbots often add disclaimers on how sources should be used. Three known patterns:
  - Negative parallelism, usually with "rather than": a claim or source should be treated as something speculative, subjective or symbolic rather than definitive or verified.
  - Cautioning that available information does not establish some firm conclusion.
  - Saying a topic "should not be confused" with another (less reliable pattern).
- Extremely uncommon before mid-2026 (roughly the July release of GPT-5.6). Text with these disclaimers dated before July 2026 is far less likely to be AI.
- Examples: `should be treated as religious tradition rather than as an archaeological explanation`; `undergoing testing and evaluation, rather than validated production or clinical systems`; `It does not establish that Benjakitti has a particular contamination problem`.

#### Phrasal templates and placeholder text
- Mad Libs-style fill-in templates left unfilled. Real article-creation templates exist and are not AI.
- Source examples: `[Describe the specific section or content that needs editing ...]`; `[Article Title 1]`, `[Your Email Address]`, `[brief reason]`, `[Join Date]`; `[link to the revised article]`, `[Your Name]`; `[Entertainer's Name]`; `(Add your channel URL here)`, `(If available)`.
- Infobox edits may carry comments like `<!-- Add if available with citation -->`. Check first whether the comment belongs to the infobox template itself (boilerplate exists, such as "Add spouse if reliably sourced").
##### Date placeholders
- Placeholder dates like `2025-XX-XX` in citation access-date (rarely date) fields.
##### URL placeholders
- Strings such as `INSERT_SOURCE_URL_##`, `INSERT_WEBSITE_URL_HERE`, `PASTE_SPOTIFY_TRACK_URL_HERE`, `PASTE_YOUTUBE_VIDEO_URL_HERE`, `SOURCE_PUBLISHER`, `[Year]`, `[Founder Names]`.
- `example.com` is a normal placeholder in templates, but links to subpages of it (`example.com/source1`, `example.com/article`, `example.com/news`) may indicate LLM use.

### Markup irregularities
- Summary of the Markup subpage (full notes in [`signs-markup.md`](signs-markup.md)).
- Markdown in place of wikitext: asterisks for bold, number signs for headings, `---` or `----` section dividers, Markdown link format `[url](text)`; most unambiguous: output in triple-backtick code blocks, often prefixed `wikitext`.
- Exposed internal data structure or styling, an unambiguous indicator. Example: ChatGPT `contentReference[oaicite:1]`.
- Other bugs: nonexistent categories, nonexistent templates.

### Citations
Relevance: web copy that cites sources or links out.
#### Broken external links
- Several broken links (nonexistent sites, 404s) in a new article or draft, especially absent from web archives, is a strong sign of AI generation. Links rot over time, but these factors make it unlikely the link ever worked.
- False-positive checks: links that work for others but not you (paywalls, university library access); links mangled by bots or scripts; links missing a start or end from human copy/paste.
#### Invalid DOI and ISBNs
- ISBN checksums catch bad ISBNs. DOIs resist link rot. Unresolvable DOIs and invalid ISBNs can indicate hallucinated references.
#### DOIs that lead to unrelated articles
- An LLM may invent scholarly references with valid-looking DOIs that point to unrelated papers. Example: invented IEEE Proceedings citations on Ohm's law, one by an author dead for 30+ years before the stated date.
- Not always AI: from 2018 to 2023 a VisualEditor UX issue made editors insert PubMed references with low IDs by accident (PMID 9 on rat livers), which can resemble hallucination.
#### Book citations without page numbers or URLs
- LLM book citations often lack page numbers, so they cannot verify the claim (example: a real circuits textbook cited for Ohm's law with no page).
- Some include pages and a real book, but the cited pages do not support the text. Watch for: a general or frequently-cited book, and no URL. Example: a Goldwater book cited for a Burke claim; searching the book for "Burke" gives nothing.
#### Incorrect or unconventional use of references
- References attempted in Wikipedia style but with wrong details. Examples: faulty reference-reuse syntax after every full stop; a third source assumed from `pubmed.ncbi.nlm.nih.gov/3` (PMID 3) that is irrelevant; the `↩` return character around footnotes; chatbot offers left in the references (`Would you like help formatting and submitting this to Wikipedia`).
#### utm_source=
- ChatGPT may append `utm_source=openai` or `utm_source=chatgpt.com` to source URLs. Microsoft Copilot may add `utm_source=copilot.com`. Grok uses `referrer=grok.com`. Gemini and Claude use UTM parameters less often.
- Near-definitive proof of ChatGPT involvement, but not that ChatGPT wrote the prose (people use AI to find citations for existing text; the edit history shows this). Extremely rare exceptions exist (Google has indexed URLs with the parameter).
#### Named references declared in references section but unused in article body
- Sources listed in a `<references>` block but not cited in the body; also named references that are never defined (can also come from copy/paste between articles). Wikipedia-specific.

### Comment-specific indicators
- Summary of the comments page (full notes in [`signs-comments.md`](signs-comments.md)). LLM-written comments often: misquote policies and cite made-up shortcuts (or just "WP"); transclude maintenance banners; have titled sections or subheadings; downplay LLM use by claiming human effort; request input from critics or other editors to learn what to fix; call concerns unsubstantiated speculation; urge critics to refocus on improving content.
- The tone resembles a clerk or customer-service agent: users claim to have "carefully reviewed" the work, apologize for any inconvenience they "may have" caused, and write along the lines of `If there are specific issues that need to be resolved, please point them out to me, and I will try to resolve them.`
- Opening patterns cited from searches: `I understand your concerns regarding AI-generated...`, `Dear Wikipedia Editorial Team`, `I am writing to`, `I hope/trust this message finds you well`.

### Edit summaries
- AI edit summaries follow rigid templates uncommon before 2023. Their presence strongly suggests the edits are AI-written too, since few would use AI for a summary but not the longer writing task. The more a summary deviates from the pattern, the less likely it is AI. Common abbreviations such as "ce" point to humans.
- Older AI summaries are first-person with older-LLM signs (AI vocabulary, emoji, list formatting, Markdown). Newer ones are exhaustively procedural about the process and policy compliance.
- Web relevance: the same traits show up in commit messages, changelogs, release notes and meta descriptions.
#### General examples
- Examples: a first-person ChatGPT-labelled summary explaining it "revised the content to provide a neutral and informative description"; `**Concise edit summary:** Improved clarity, flow, and readability ...`; a long itemized reorganization note; a summary that still contains a chatbot preamble (`Claude responded: ...`).
#### Canned assurance of adherence to Wikipedia policies and guidelines
Words to watch: `ensured that... adheres to`, `refined`, `enhanced`, `enriched`, `streamlined`, `improved`, `in compliance/complies with`, `Wikipedia [guidelines/style/standards]`, `revised`, `verifiability`, `neutrality`, `neutral tone`, `encyclopedic tone`, `clarity`, `flow`.
- Summaries reassure, nearly self-consciously, that the edit follows policy. They often say outright that these are Wikipedia's guidelines (humans rarely state the obvious that edits on Wikipedia are for Wikipedia).
- Humans do cite policy but briefly and specifically with a link (`removed excessive links per MOS:OVERLINK`). AI versions are wordier and vaguer ("ensure neutrality", "improve attribution", "comply with the manual of style"). More assurances stacked, across more kinds of "improvement", means a stronger sign.
- Examples: `clarity and compliance with the Manual of Style`; `corrected promotional wording`; `improved sourcing and neutrality`; `for a more neutral tone. Removed promotional`; `Improve citations`.
#### Specific mentions of "preserved" or "retained" information, "avoided" mistakes, and other procedural statements
Words to watch: `preserved/preserving`, `retained/retaining`, `avoided/avoiding`, `ensured/ensuring`, `aimed/aiming to`.
- Humans rarely mention what they did not change. An AI told to change X and Y while preserving Z does. Typical format: "Revised [section] to [improve/ensure] [neutrality/verifiability] while preserving [whatever]".
- Examples: `while preserving the original meaning and technical details`; `preserved existing structure and lead emphasis`; `preserved references and categories`; `while preserving sourced criticisms`.
#### Overemphasis on presence/reliability of citations
Words to watch: `added sourced [information/content/infobox/section]`, `added verified [information/content/infobox/section]`, `added [coverage/citations/references]`, `improved attribution`, `with [independent/secondary/third-party/peer-reviewed] sources`.
- Mirrors the body-text habit of alluding to coverage without summarizing it. Humans say what they added (`Added info about the artist's debut`), not only that it is sourced.
- Examples: `with sourced content`; `with ESSA citations`; `added sourced information, references`; `Add sourced Military culture section`.
#### Overemphasis on parameter/template names and markup idiosyncracies
- Summaries itemize parameter and template names with original markup and say "inline citations" or "internal links". New editors rarely give that granularity. Example: `Corrected infobox parameters (image_size)`.
#### Reference to AfC review
- Summaries mention the edit addresses reviewer feedback, which is too obvious to state. Examples: `Addressing reviewer feedback by integrating independent secondary coverage`; `per reviewer feedback. All claims verified`; `Addressed reviewer feedback by improving sourcing, formatting, and neutrality`.

### Miscellaneous
#### Pronounced shift in writing style
- A sudden change in an editor's style (unexpectedly flawless grammar versus their earlier talk comments), especially if the earlier writing predates November 2022. An AI-using editor's style tracks the contemporary LLM era (2023 edits resemble 2023 output).
- The reverse: a user whose pre-chatbot edits show the same style (frequent boldface, lists) is less likely to be using AI now.
#### "Submission statements" in AfC drafts
- At least one LLM inserts reviewer-facing notes asserting notability and guideline compliance (`Reviewer note (for AfC): This draft is a neutral and well-sourced biography ... meets WP:RS and WP:BLP standards`; an AI-use disclosure that says the text was reworked to "ensure full compliance with Wikipedia guidelines"). It mainly reveals LLM use.
#### Pre-placed maintenance templates
- New editors' drafts containing an AfC review template pre-set to "declined" with no reasoning (the LLM offers to add an AfC template and outputs `{{AfC submission|d}}`) are a strong indicator. The creator then asks why it was declined with no feedback.
- LLMs also create pages that already contain maintenance or protection templates that cannot plausibly belong (`Short description`, `Use American English`, `Use mdy dates`, `BLP sources` with dates).
#### Canned user pages
- Rigid formats with inline-header vertical lists and headings such as `Welcome To My User Page!`, `About Me`, `My Interests`, `Let's Connect!`; emoji, bold text, or attempted Markdown bold. Full notes in [`canned-user-pages.md`](canned-user-pages.md). Example heading style: `✨ About Me`, `🏆 My Contributions`, `💬 Let's Connect!`, `Happy Editing! 🚀`.
#### Permissions gaming
- Throwaway AI rewrites or additions across dozens of unrelated articles to inflate edit count and gain user rights. Use the sign in one direction only: someone adding much AI text is not necessarily gaming; a suspected permissions gamer who added much text probably used AI.
#### Differences between LLMs
- Each model and version has its own idiolect; GPT-5 traits differ from GPT-4 or Gemini. ChatGPT (GPT-4o-2024-08-06) and Grok (Grok-Beta, late 2024/early 2025) focus on broader context more than Gemini (1.5 Pro) and Claude (3.5 Sonnet). Gemini and Claude are more concise; ChatGPT and Grok, longer (Grokipedia articles are very long). ChatGPT has been the most-used chatbot for Wikipedia edits.
#### Biases in content
##### Pro-authoritarian bias
- As of 2026, leading American models show pro-authoritarian bias on some prompts (training on state-media propaganda; safety reasoning for users in repressive countries). Chinese-language answers are more authoritarian than English ones. Models were more likely to criticize governments in freer countries.

### Signs of human writing
#### Age of text relative to ChatGPT launch
- Text added before 30 November 2022 (ChatGPT public launch) can be treated as not AI-written. Paid earlier LLMs were not widely accessible. Older text with AI-like features is coincidence given the size of Wikipedia. Tools such as Who Wrote That and WikiBlame date text.
#### Ability to explain one's own editorial choices
- Real editors can explain an edit or mistake. A suspicious fabricated-looking URL can be probed: a human can give the right link, name the typo, or quote the real passage.
#### Syntax
- LLMs aiming for "formal, neutral, encyclopedic tone" avoid constructions humans use and style guides often prefer. Over 25 years of Wikipedia writing these are more common in human text than AI text:
  - simple is/has phrases: `there is a`, `it has a`.
  - plain words over stiff or euphemistic synonyms: `wrote` (not authored), `moved` (relocated), `used` (utilized), `tried` (attempted), `died` (passed away).
  - superlative or definitive statements: `one of the best`, `is the only`, `was the first`.
  - qualifiers and intensifiers: `very`, `perhaps`, `tends to`.
  - isolated wordy constructions: `as a result of`, `in order to`, `all of the`, `a part of`, `the fact that`.

### Ineffective indicators
- False accusations drive newcomers away. Check for confirmation bias and the Dunning-Kruger effect. Style-only detection is not easy. These popular indicators are ineffective and can point the other way:
  - Perfect grammar: many skilled writers and professionals exist.
  - Mixed casual and formal registers, or language that sounds both clinical and emotional: can be a tech worker, youth, playfulness, neurodivergence, or several editors on one page.
  - "Bland" or "robotic" prose: AI traits are specific; they skew positive and verbose, and may not look robotic to the unfamiliar.
  - "Fancy", "academic" or "formal" prose: AI favors specific words, not formal register in general.
  - Transition words in isolation: older AI overused `Additionally,`, `Consequently,`, `Notably,` at sentence starts, but only a few transitions are overused and human essays use them. Not a strong tell.
  - Unsourced content: over 570,000 articles are tagged for citations, mostly pre-LLM. Modern chatbots with search often include citations (not necessarily accurate ones).
  - Bizarre wikitext: odd stray HTML tags (`<span>`) point to browser extensions or a known translation-tool bug; misplaced syntax like `''Catch-22 i''s` points to VisualEditor mistakes.
  - Correct wikitext: normal with the visual editor or preview.
- The page also points to a "Sudden shift in English variety use" section that does not exist in the retrieved revision (broken anchor). Treat as undocumented.

### Historical indicators
- Common in older models, rarer in newer ones, still useful for finding old undetected edits. Dates approximate.
#### Statements about knowledge cutoffs (2022-2023)
Words to watch: `Up to my last training update`, `as of my last knowledge update`.
- Older fixed-cutoff models (GPT-3.5, GPT-4) warned that information is accurate only up to a date. Example: `As of my last knowledge update in January 2022, I don't have specific information about the current status`.
#### Section summaries
Words to watch: `In summary`, `In conclusion`, `Overall`.
- Older LLMs, told to write longer pieces, added "Conclusion" sections and ended paragraphs or sections by restating the core idea. Examples: `In summary, the educational and training trajectory ... This structured pathway ensures that ...`; repeated `In summary,` and `Conclusion:` blocks in long comments.
#### Prompt refusal
Words to watch: `as an AI language model`, `as a large language model`, `I cannot offer medical advice, but I can...`, `I'm sorry`.
- Older chatbots declined requests with apologies, then offered alternatives. Outright refusals are now rare. Example: `As an AI language model, I can't directly add content to Wikipedia for you, but I can help you draft your bibliography.`
#### Overuse of em dashes (2022-September 2026)
- LLM output uses em dashes (—) more than nonprofessional human text of the same genre, in places where humans use commas, parentheses, colons, (misused) hyphens or en dashes. Often formulaic, mimicking punched-up sales writing by stressing clauses or parallelisms. AI em dashes are usually surrounded by spaces, against typographic convention.
- Most useful combined with other signs, not alone. Far more common on discussion pages than in articles. Some companies suppress the habit (notably OpenAI's GPT-5.1). A July 2026 study found only Claude, among contemporary models, used em dashes more than professional writers; ChatGPT used them less.
- From September 2026, the newest models are increasingly hard-coded to avoid em dashes. Side effect: less punctuation variety overall. Commas and periods become more likely than in human text (flagged as needing a citation in the source), and that is now its own sign of AI writing.
- Examples show dash-heavy contrasts: `— something that was reported by the user`; `e.g., "Curaçao, Dutch Caribbean" — but this only adds confusion`; `you're right about one thing — we do seem to have`.
#### Abrupt cut offs
- Older ChatGPT stopped when a response hit the token limit, requiring "continue generating". Not foolproof: a bad copy/paste or a copyright violation can look similar.
#### Outdated access-date parameters
- Citations with default access dates far older than the edit (e.g., `access-date=12 December 2024` in an article created December 2025). Newer chatbots seldom do this and legitimate causes exist (copied citations, offline work, merges).
#### Lexical diversity/elegant variation
- Older models may carry a repetition penalty, so they avoid reusing a word and substitute synonyms. Observed on Wikipedia before-versus-after 2023 and against generated articles (GPT-4o-mini, Gemini-1.5-Flash).
- Caveat: if separate pieces of AI text were added in separate edits, the tell may not apply. Non-native speakers (for example Italian schooling teaches avoiding repetition) also vary words.
- Example pattern: one referent renamed again and again (`the constraints of socialist realism` / `the challenging climate of Soviet artistic constraints` / `the confines of state-imposed artistic norms`; `non-conformist artists` / `these artists` / `like-minded artists`; `their creativity` / `their artistic aspirations` / `his distinctive artistic vision`).

### See also
- Template "Looks AI-generated" (a maintenance tag).
- Wikipedia:Artificial intelligence resources (directory page).
- Wikipedia:Artificial intelligence (overview).
- A user essay, "AI Slop Detection" (user page, not retrieved).

### External links and further reading (as listed)
- CanYouPasstheTuringTest.com and the Tropes AI Writing Pattern Directory (tropes.fyi): external sites, not retrieved.
- Further reading: Sam Kriss, "Why Does A.I. Write Like ... That?", The New York Times Magazine, 2025-12-03 (subscription). Not retrieved.
