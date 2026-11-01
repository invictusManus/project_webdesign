# WikiProject AI Cleanup guide: notes

Sources: Wikipedia, "Wikipedia:WikiProject AI Cleanup/Guide and resources" (WP:AICGUIDE; revision 1382195891, 2026-10-27; "Guide" is a redirect to it) and the "Editing advice" part of "Wikipedia:WikiProject AI Cleanup" (the project hub). Both are linked from the main page. Retrieved 2026-11-01. Text © Wikipedia contributors, CC BY-SA 4.0. These notes are an adaptation (summarized, restructured) and are licensed CC BY-SA 4.0. Not an official Wikipedia policy.

Scope: only the parts about judging whether text is AI-written and how reliable the evidence is. The cleanup workflow (tagging, warning, speedy deletion, presumptive removal, noticeboard routines, user warning templates) is Wikipedia process and is not documented here.

Structure: one `##` per page, `###` = section, `####` = subsection.

## Wikipedia:WikiProject AI Cleanup/Guide and resources
https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide_and_resources

### Determining whether content is LLM-generated
- Main method: spot stylistic or linguistic signs common in LLM text and rare in human text; the main page is the one to study. Evidence is either one obvious sign (Markdown, chatbot communication) or a combination of less obvious signs.
- Combination logic: a sign like em dashes (often in human text too) rapidly loses force alone but, together with several others, makes human authorship unlikely. The page's worked illustration: if em dashes, the words `pivotal` plus `interplay`, and over-attribution appear in human text with probabilities of 20%, 15% and 25%, all three together are about 0.75% likely in human writing. Treat as a heuristic: the methods are probabilistic, so watch for false positives and alternative explanations.
- Detection is a skill: a 2025 study found human ability no better than chance; another found heavy LLM users correct about 90% of the time.
- Caveat dated August 2026: much of what the signs page documents has become outdated for the most recent models, making detection harder for now.
- Most reliable but slowest test: check whether the cited sources support the text (hallucination check). Prioritize sentences that show AI signs.
- Checking the author's other edits from the same period helps, since LLM use is habitual. Content added before 30 November 2022 is extremely unlikely to be LLM-generated.
#### LLM detection software
- Many detectors (GPTZero and others) give false positives, especially free ones, and must never be the only evidence in an accusation. They have false negatives and opaque scoring; "humanizer" sites try to fool them; some human styles or writing plugins trigger them; algorithms change; free tiers cover small amounts of text.
- The best (usually non-free) have over 95% accuracy in one study, and can triage dozens of edits. A consistently high score warrants further checks. Mixed scores are low signal (other editors may have changed text; wiki markup throws tools off).
#### Useful tools (as listed)
- Link checker for 404s (dead links can mean hallucinated links; confirm with a site search); ISBN existence checker; edit-filter logs; GPTZero for Wikipedia (not that reliable, but consistently high scores count); Pangram (one of the most reliable automated detectors despite high false negatives; use as a sanity check, not a substitute for judgment).
#### Examples of AI chat transcripts
- A table of shared ChatGPT links tied to drafts (autobiography, company, place), used to study how people prompt LLMs to create articles. Not reproduced. AfC (Articles for Creation) submit wizard asks for AI use disclosure as of 29 September 2026.

### Engaging with editors suspected of LLM use
- Process advice for Wikipedia editors: many users are good-faith newcomers or non-native speakers; be patient; ask rather than accuse; seek a commitment not to use LLMs instead of a confession; do not insist on perfect English.
- One point on detection hygiene: it is usually best to be vague about how content was judged to be LLM-generated; naming the signs may lead to masking or superficial fixes.

### Doing the cleanup, Patrolling the wiki, Templates related to AI cleanup
- Wikipedia workflow only (revert, stubbify or rewrite from scratch; draftify and tag; speedy deletion G15; presumptive removal; patrol searches; tracking categories; warning and deletion templates). Not documented.

## Wikipedia:WikiProject AI Cleanup
https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup

### Goals and Editing advice (relevant bullets only)
- Project goals: identify and remove AI-written text, find AI-generated images, track editors who may not know AI's deficiencies, educate editors, protect against AI agents.
- AI-assisted edits are hard to identify in most cases since text is often indistinguishable from human text; the signs page lists characteristics associated with chatbot text. Text present before 30 November 2022 is very unlikely to be AI.
- Most AI content is not "unsourced". It may carry real but unrelated sources, invented ("fake") sources, or legitimate sources used to build the AI content. When cleaning, check the sources. Examples given: an article with fake Russian and Hungarian sources found by no search; a beetle article with real German and French sources that were off-topic.
- As of 2026, recent models usually cite real sources but do not verify the content they cite them for. The existence of sources is not by itself evidence the text is human-written.
- Fully AI-written pages: check that the topic is legitimate and notable; hoaxes have entered through AI-made fake citations that look real (an example hoax stayed up for most of a year).

### Remaining sections
- Open tasks, participants, resources and see-also lists: project administration. Not documented.
