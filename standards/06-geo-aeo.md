# 06 · GEO & AEO (AI search)

Scope: visibility and citations in AI answers (Google AI Overviews and AI Mode, ChatGPT, Perplexity, Copilot, Gemini, Claude): eligibility, crawler policy, entities, citable content, off-site signals, measurement. Google's position: optimizing for generative AI search is SEO, and no special files or markup are needed. Clean SEO ([`05-seo.md`](05-seo.md)) comes first.

Last verified: 2026-10

## Eligibility & crawler policy

| ID | Level | Rule | Verify |
|---|---|---|---|
| GEO-01 | MUST | AI search work starts only once the SEO MUST rules pass. AI features draw on indexable, snippet-eligible pages. No separate AI versions of pages, and no splitting text into chunks just for AI. | Launch gate status |
| GEO-02 | MUST | Key pages carry no `nosnippet`, `max-snippet:0` or `data-nosnippet` on core content; these also limit use in AI Overviews and AI Mode. | Source review; URL Inspection |
| GEO-03 | MUST | AI crawler policy is decided and set in robots.txt. Search and user-initiated bots are allowed: OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot. Training bots (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot) are allowed or blocked by explicit decision. CDN bot protection must not block the allowed bots. Template: [`robots.txt`](../templates/robots.txt). | robots.txt; CDN bot logs |
| GEO-04 | SHOULD | Leave Search Console's generative-AI control at its default (included) unless there is a documented business reason to opt out. Opting out is not a ranking signal, but it removes the site from AI Overviews and AI Mode. | GSC settings |

## Entities & structured data

| ID | Level | Rule | Verify |
|---|---|---|---|
| GEO-05 | MUST | One canonical brand name, one-sentence description and category, used identically on the site, in structured data, the Business Profile, social profiles and directories. | Profile audit |
| GEO-06 | MUST | Organization (or Person) markup with a stable `@id`, logo, contact details and `sameAs` links to every official profile (Wikidata, LinkedIn, Business Profile …). Pages connect to it through the `@id` graph. Template: [`site-graph.jsonld`](../templates/schema/site-graph.jsonld). | Schema Markup Validator |
| GEO-07 | SHOULD | Authors are entities: author pages carry `Person` markup with credentials and `sameAs`, and bylines link to them (CON-05). | Validator; page review |

## Citable content

| ID | Level | Rule | Verify |
|---|---|---|---|
| GEO-08 | SHOULD | Write content that AI answers can cite: precise definitions, statistics with source and date, original data or research, step lists, comparison tables, and claims attributed to named experts. | Editorial review |
| GEO-09 | SHOULD | Pages answer the topic's follow-up questions (People Also Ask, sales and support questions, related prompts) under descriptive headings, written for people. | Content brief questions covered |
| GEO-10 | SHOULD | Off-site presence: the brand is mentioned and described accurately in authoritative third-party sources: press, industry lists, review platforms, Wikipedia/Wikidata where notable, and communities where the audience asks questions. | Mention monitoring |
| GEO-11 | SHOULD | Bing Webmaster Tools and IndexNow are set up (MSR-04). Bing's index powers Microsoft Copilot answers. | Bing WMT |
| GEO-12 | SHOULD | Merchant Center and Business Profile data are complete and current, because AI shopping and local answers draw on them (MSR-20, SEO-29). | Diagnostics |

## Measurement

| ID | Level | Rule | Verify |
|---|---|---|---|
| GEO-13 | SHOULD | Measure AI visibility monthly with three sources: Search Console's generative-AI report, Bing's AI Performance report, and a fixed set of 20–50 prompts run across the major assistants. Record mentions, citations, accuracy and sentiment vs. competitors. | Monthly report |
| GEO-14 | SHOULD | When AI answers describe the brand wrongly, trace the error to its source (an outdated page or third-party profile) and fix it there. | Issue log |

## Experimental

| ID | Level | Rule | Verify |
|---|---|---|---|
| GEO-15 | COULD | ⚗ `/llms.txt`: a curated Markdown index of key pages. It is an unofficial proposal that Google does not use, and its effect is unproven, but it is cheap. | File reachable |
| GEO-16 | COULD | ⚗ Content-usage signals (`Content-Signal` in robots.txt) and agent-discovery files. Unofficial; follow IETF AIPREF standardization before relying on them. | Watch list |

## Sources

- [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) · [Optimizing for generative AI search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google: Generative AI performance reports](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) · [Search generative AI control](https://support.google.com/webmasters/answer/16908024)
- [Google: Common crawlers incl. Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) · [Organization markup](https://developers.google.com/search/docs/appearance/structured-data/organization)
- [OpenAI crawlers](https://developers.openai.com/api/docs/bots) · [Anthropic crawlers](https://support.claude.com/en/articles/8896518) · [Perplexity crawlers](https://docs.perplexity.ai/guides/bots) · [Applebot-Extended](https://support.apple.com/en-us/119829)
- [IndexNow](https://www.indexnow.org/faq) · [llms.txt proposal](https://llmstxt.org/) · [IETF AIPREF](https://datatracker.ietf.org/wg/aipref/about/)
