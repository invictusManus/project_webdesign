# DESIGN.md: [Brand]

The brand spec for people and AI agents (DES-01). Read it before any UI or copy work. Values live in `tokens.json` (DES-02): reference token names here, never raw values.

## Design intake (DES-13)

| Question | Answer |
|---|---|
| Color palette, 60-30-10 (DES-14): primary 60 % · secondary 30 % · accent 10 % (hex), plus neutrals; or pick a suggested palette | |
| Font family: category (sans-serif · serif · mono · display) and family name, max 2 (DES-04) | |
| Style direction: minimal/simple · modern translucent · bold/expressive · editorial · classic/corporate · playful | |
| Light, dark or both | |
| Density: airy or compact | |

## Brand

- **Positioning:** [statement from project brief, STR-03]
- **Personality:** [3 adjectives, e.g. precise · warm · calm]
- **Voice:** [how we sound] · **Tone shifts:** [e.g. error messages calmer, marketing bolder]

| Do | Don't |
|---|---|
| | |

## Logo

Files, clear space, minimum size, allowed backgrounds, forbidden uses.

## Color roles

| Role | Token | Use |
|---|---|---|
| Text | `semantic.color.text.default` | Body copy |
| Secondary text | `semantic.color.text.secondary` | Lead, meta, captions |
| Muted text | `semantic.color.text.muted` | Secondary info, never for essential content |
| Disabled text | `semantic.color.text.disabled` | Inactive controls only |
| Text on accent | `semantic.color.text.on-accent` | Labels on primary buttons |
| Primary (60 %) | `primitive.color.primary.*`, `semantic.color.bg.brand` | Brand color and tints on large surfaces (DES-14) |
| Secondary (30 %) | `primitive.color.secondary.*`, `semantic.color.bg.secondary` | Sections, cards, illustrations |
| Accent (10 %) | `semantic.color.action.primary` | Primary call to action and key highlights only, one per view (UX-06) |
| States | `semantic.color.action.*-hover`, `*-pressed`, `disabled` | Every interactive color has its states (DES-36) |
| Surfaces | `semantic.color.surface.*` | Raised, sunken, overlay, skeleton |
| Focus | `semantic.color.focus` | Focus ring, 2 px, offset 2 px |
| Status | `semantic.color.status.*` | Always with icon or text, never color alone (A11Y-07) |

## Typography

| Role | Token | Notes |
|---|---|---|
| Body | `semantic.text.body` | 1 rem (16–18 px), line-height 1.6, 45–75 characters per line |
| Display | `semantic.text.display` | Hero only, 3.33 rem desktop |
| H1–H4 | `semantic.text.h1`…`h4` | Golden-ratio scale: H4 1.272, H3 1.618, H2 2.058, H1 2.618 rem (desktop), via `clamp()` |
| H5 · H6 | `semantic.text.h5` · `h6` | 1 rem/600 · 0.786 rem/600 (DES-24) |
| Eyebrow | `semantic.text.eyebrow` | 0.786 rem/600, +0.08 em, ≤ 3 words, not a heading |
| Lead | `semantic.text.lead` | 1.272 rem/400, line-height 1.5, first paragraph only |
| Small · caption | `semantic.text.small` · `caption` | 0.786 rem, never smaller |
| Footer · legal | `semantic.text.footer` | 0.875 rem |

Vertical rhythm (DES-25): space above a heading ≥ φ × space below it.

Families: `primitive.font.family.sans`; weights: 400 body, 500–600 labels, 600–700 headings (DES-15).

## Elevation, borders, states

| Use | Token | Rule |
|---|---|---|
| Card · dropdown · dialog | `semantic.elevation.card` · `dropdown` · `dialog` | Three levels only (DES-37) |
| Borders | `semantic.border.*` (input, input-hover, input-focus, input-error, divider) | Composite border tokens (DES-38) |
| Focus outline | `semantic.border.focus`, offset `semantic.focus.offset` | 2 px, ≥ 3:1 on every surface |
| Hover | `semantic.state.*`, `semantic.transition.hover` | At most two hover effects at once (DES-36) |

Themes: `tokens.dark.json` overrides semantic tokens only (DES-40). Forced-colors mapping: buttons → `ButtonText`/`ButtonFace`, links → `LinkText`, focus → `Highlight`.

## Token change log (DES-41)

| Date | Token | Change | Reason |
|---|---|---|---|
| | | | |

## Layout & spacing

| Tier | Width | Columns | Gutter | Margin | Section padding |
|---|---|---|---|---|---|
| Mobile | 0–599 px | 4 | 16 | 16 | 42 |
| Tablet | 600–1023 px | 8 | 26 | 26 | 68 |
| Desktop | 1024–1439 px | 12 | 26 | 42 | 68–110 |
| Wide | ≥ 1440 px | 12, capped | 26 | auto | 110 |

Tokens: `primitive.breakpoint.*`, `semantic.width.*` (prose · wide), spacing `primitive.space.*`. Rules: LAY-01 to LAY-13.

### Page types and section order (LAY-14)

| Page type | Sections in order |
|---|---|
| Home / landing | hero → problem and value → proof → offer or how it works → FAQ → final call to action |
| | |

Header (LAY-15): [logo · nav items · utilities · call to action]. Footer (LAY-19): [columns · legal row].

## Components

| Component | States documented (DES-06) | Notes |
|---|---|---|
| Button | default · hover · focus-visible · active · disabled · loading | Min height 44 px |
| Form field | default · focus · error · disabled | Label always visible (A11Y-16) |
| Card | default · hover · focus-within | One link stretched over the card (CMP-02) |
| Dialog | open · closing | Full screen below 600 px (CMP-11) |
| [more from `16-components`] | | |

Every component lists anatomy, variants, tokens, states, behavior per tier and its keyboard/ARIA pattern (CMP-01): use [`component-spec.md`](component-spec.md). Page types: [`page-blueprint.md`](page-blueprint.md).

## Imagery & icons

Photo style, art direction, aspect ratios, focal points, illustration style, alt-text rules (A11Y-06).

| Item | Choice | License |
|---|---|---|
| Icon library (DES-42; default Lucide) | | |
| Illustration source (DES-44) | | |

Usage: [`icon.md`](icon.md). Sources: [`reference/assets/`](../reference/assets/README.md).

## Motion

Durations `primitive.duration.*`, easings `primitive.easing.*`, transitions `semantic.transition.*`. Animate `transform`/`opacity` only. Reduced-motion fallback required (A11Y-10). Start from [`motion.css`](motion.css); a JavaScript library only per DES-43 (record which and why):

## Style guide (CON-17)

| Topic | Our rule |
|---|---|
| Spelling variant | e.g. en-US |
| Capitalization | Sentence case for headings, buttons and navigation |
| Numbers | e.g. one to nine in words, 10 and up as numerals |
| Dates, times | e.g. 4 March 2026 · 14:30 CET (per locale, I18N-08) |
| Units, currency | e.g. 5 km · €1,200 (non-breaking space per DES-26) |
| Brand and product names | Exact spelling (GEO-05) |
| Inclusive language | Per language (CON-20) |
| Readability target | Flesch ≥ 60 / Amstad ≥ 60 (CON-18) |

## Glossary

| Term we use | Not | Meaning |
|---|---|---|
| | | |
