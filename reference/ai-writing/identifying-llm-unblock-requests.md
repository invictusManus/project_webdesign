# Identifying LLM unblock requests: notes

Source: Wikipedia, "Wikipedia:Identifying LLM unblock requests" (information page, shortcuts WP:LLMUR, WP:IDLLM). Linked from the Wikipedia AI directory and from the comments page. Retrieved 2026-11-01; revision 1381430804 (2026-10-22). Text © Wikipedia contributors, CC BY-SA 4.0. These notes are an adaptation (summarized, restructured) and are licensed CC BY-SA 4.0. Not an official Wikipedia policy.

Scope: one genre, appeals written by people who were blocked. The signs are the genre-neutral ones: letter formatting, placeholders, generic wording, stock closers. Included because the traits are the same ones that show up in form letters, contact replies and "about us" copy.

## Wikipedia:Identifying LLM unblock requests
https://en.wikipedia.org/wiki/Wikipedia:Identifying_LLM_unblock_requests

### Lead
- Using an LLM for an unblock request is not inherently bad faith (newcomers, non-fluent English speakers). A minority are AI-assisted and may be taken at face value. A truly AI-generated request should almost always be declined because it does not show the user understands why they were blocked.
- Detector sites (GPTZero, a no-limit GPTZero for Wikipedia, ZeroGPT, Copyleaks, QuillBot, Leap AI, Illuminarty, Pangram) have varying success. A result is good evidence for or against, never sufficient alone in either direction. User scripts exist to copy plain text or wikitext into detectors.

### General signs
- Unfilled placeholder text: for example `I was blocked because [reason for block here]`.
- Leftover prompts or metadata: lines such as `Write me a Wikipedia unblock request` or `Here is a Wikipedia unblock request` at the start.
- Written like a letter: ChatGPT often adds subject lines, which do not fit the interface and which a human is unlikely to add. Salutations and valedictions are also a tell, though occasionally seen in human requests.
- Markdown: humans rarely format a whole post in Markdown, and more rarely use advanced Markdown such as `#Headings` and `[links](https://...)`.
- Generalities and hallucinations: referencing the block only in general terms (`I understand that my edits went against Wikipedia's policy on promotional editing`) or misstating the reason (`My username was too promotional` when the username was not an issue) is a strong sign.
- Marked difference in writing style: sudden fluent or more formal English. Caveat: context can push people to formality, and tools like Grammarly can do the same.
- Phrases: `I am committed to ...`, `I respectfully request ...`, `I have taken the time to carefully ...`.
- Lists: ChatGPT really likes bulleted and numbered lists (humans do too, but less).
- Closing statements: `Thank you for your time` or `Thank you for considering my request`, often merged in longer appeals. Not conclusive alone; repeated use with other signs points the right way.

### Examples
- Five ChatGPT outputs, shown to illustrate: a template with `Subject: Request for Unblock - [Your Username or IP Address]`, `Dear Wikipedia Administrators,`, `I am writing to respectfully request a review of the block`, `I regret any actions that may have contributed to the block`, `I apologize for any inconvenience caused`, `I am committed to contributing positively`, `Thank you for considering my request. If any further clarification is needed, I am happy to provide it.`, `Sincerely, [Your Username]`; a promotional-edits version that adds `Feel free to personalize it further, especially by mentioning any specific guidelines you've read` after the draft; a version using numbered sections (`1. Acknowledgment and Explanation`, `2. Commitment to Policy Compliance`, `3. Request for Review`) and `I pledge to follow the rules and use my account responsibly`.
- The page notes a factual slip in one output: it listed the core content policies as "neutrality, verifiability, and reliability", where the real ones are verifiability, neutrality and no original research.
- Prompt variant: when asked for a less letter-like style, the output becomes conversational but still keeps vague references to policies while sidestepping the specifics of the block (`I understand why my account was blocked and appreciate the opportunity to address it`; `I'd like to improve as a contributor and would welcome any guidance`; `Let me know if you'd like to adjust this further!`).

### See also
- The main Signs of AI writing page and the AI resources directory (see [`README.md`](README.md)).
