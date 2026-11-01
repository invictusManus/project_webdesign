# DESIGN.md: [Brand]

The brand spec for people and AI agents (DES-01). Read it before any UI or copy work. Values live in `tokens.json` (DES-02): reference token names here, never raw values.

## Design intake (DES-13)

| Question | Answer |
|---|---|
| Color palette (or pick one of the suggested palettes) | |
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
| Muted text | `semantic.color.text.muted` | Secondary info, never for essential content |
| Primary action | `semantic.color.action.primary` | One primary call to action per view (UX-06) |
| Focus | `semantic.color.focus` | Focus ring, 2 px, offset 2 px |
| Status | `semantic.color.status.*` | Always with icon or text, never color alone (A11Y-07) |

## Typography

| Role | Token | Notes |
|---|---|---|
| Body | `semantic.text.body` | 1 rem (16–18 px), line-height 1.6, 45–75 characters per line |
| H1–H4 | `semantic.text.h1`…`h4` | Golden-ratio scale: H4 1.272, H3 1.618, H2 2.058, H1 2.618 rem (desktop), via `clamp()` |

Families: `primitive.font.family.sans`; weights: 400 body, 500–600 labels, 600–700 headings (DES-15).

## Layout & spacing

Breakpoints, max content width, grid columns, spacing scale (`primitive.space.*`), section rhythm (`semantic.space.section`).

## Components

| Component | States documented (DES-06) | Notes |
|---|---|---|
| Button | default · hover · focus-visible · active · disabled · loading | Min height 44 px |
| Form field | default · focus · error · disabled | Label always visible (A11Y-16) |
| Card | default · hover · focus-within | |

## Imagery & icons

Photo style, art direction, aspect ratios, focal points, illustration style, icon set and stroke width, alt-text rules (A11Y-06).

## Motion

Durations `primitive.duration.*`, easing `primitive.easing.standard`. Animate `transform`/`opacity` only. Reduced-motion fallback required (A11Y-10).

## Glossary

| Term we use | Not | Meaning |
|---|---|---|
| | | |
