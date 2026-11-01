# 02 · Brand & design

**Why it matters:** Visitors judge credibility in seconds, mostly from visual quality and consistency. A documented brand, a golden-ratio design system and tokens keep every page consistent, handcrafted rather than generic, and cheap to change. Guide: steps 11–13.

Detail: `reference/google-search/` notes.

Scope: design intake, identity, tokens, color, typography, spacing, layout, shape, buttons, links, inputs, motion, imagery, brand assets. The brand spec lives in [`DESIGN.md`](../templates/DESIGN.md), the values in [`tokens.json`](../templates/tokens.json). Perception and usability principles: [`14-ux-psychology.md`](14-ux-psychology.md).

Last verified: 2026-11

## Golden-ratio system (φ ≈ 1.618)

| Scale | Values (base 16 px) |
|---|---|
| Type, step √φ ≈ 1.272 | 12.6 small · **16 body** · 20.4 H4 · 25.9 H3 · 32.9 H2 · 41.9 H1 · 53.3 display |
| Space, step φ | 4 · 6 · 10 · 16 · 26 · 42 · 68 · 110 · 178 px |
| Radius, step φ | 6 · 10 · 16 · 26 px · pill |
| Layout split | 61.8 % / 38.2 % (content/aside, text/image, hero columns) |
| Line height | body 1.6 · headings 1.1–1.25 |

## Intake, identity, color

| ID | Level | Rule | Verify |
|---|---|---|---|
| DES-13 | MUST | Before any UI work, ask the client and record the answers in `DESIGN.md`: color palette (or offer 2–3 suggested palettes derived from brand, industry and audience, each contrast-checked), style direction (e.g. minimal/simple, modern translucent, bold/expressive, editorial, classic/corporate, playful), light, dark or both, and density (airy or compact). Building starts only once answered or explicitly delegated. | `DESIGN.md` intake filled |
| DES-01 | MUST | `DESIGN.md` documents the brand for people and AI agents: intake answers (DES-13), positioning (STR-03), personality, voice and tone, logo use, color roles, typography, imagery, icons, motion and glossary. | File exists and is current |
| DES-02 | MUST | Design tokens live in `tokens.json` (W3C DTCG format) in three tiers: primitive → semantic → component. Components use only semantic or component tokens, and code consumes them as CSS custom properties (TEC-04). | Token build; grep CSS for raw hex values |
| DES-14 | MUST | Palette structure: one brand color, one accent reserved for the primary call to action, a 9–10 step neutral scale and semantic status colors. Roughly 60 % dominant (neutral), 30 % secondary, 10 % accent. No second accent competing for attention. | Token review; screenshot color audit |
| DES-03 | MUST | Every text/background pairing defined in tokens meets A11Y-07. Hover, focus, error, success and warning states have their own tokens. Dark mode, if offered, overrides the same semantic tokens. | Contrast check of token pairs |

## Typography, spacing, layout

| ID | Level | Rule | Verify |
|---|---|---|---|
| DES-04 | MUST | Typography follows the golden-ratio scale: body 1 rem (16–18 px), H4 1.272 rem, H3 1.618 rem, H2 2.058 rem, H1 2.618 rem on desktop, one step smaller on mobile, fluid via `clamp()`. At most 2 families. Body line-height ≈ 1.6, headings 1.1–1.25, 45–75 characters per line (aim for ≈ 66). One H1 per page, no skipped heading levels (A11Y-04). | Computed styles at 360 and 1440 px |
| DES-15 | SHOULD | Headings use weight 600–700, body 400, labels 500–600. Large headings get −0.01 to −0.02 em letter-spacing. Sentence case; no all-caps beyond short labels. `text-wrap: balance` for headings, `pretty` for body. | Computed styles |
| DES-05 | MUST | Spacing uses only the φ scale. Space inside a group is at least one φ step smaller than space between groups (PSY-02). | Token file; spacing audit |
| DES-16 | MUST | Layout: 12-column grid with content-driven breakpoints, container max 1200–1280 px, text column ≈ 66 ch, asymmetric splits at 61.8/38.2, section padding 68–110 px on desktop and 42–68 px on mobile, shared alignment lines, whitespace instead of decoration. | Grid overlay at 390 and 1440 px |

## Shape, buttons, links, inputs

| ID | Level | Rule | Verify |
|---|---|---|---|
| DES-17 | MUST | Shape: one radius family from the φ scale applied by role (controls 10, cards 16, large panels 26, tags pill); nested radius = outer radius − padding. One elevation system (≤ 3 shadow levels, or borders), not mixed at random. One icon set with one stroke width, sized 1–1.272 em of the adjacent text. | Component audit |
| DES-18 | MUST | Buttons come in three tiers only: primary (filled accent), secondary (outline or tonal), tertiary (text). Min height 44 px, horizontal padding 16–26 px from the φ scale, verb label (UX-15) at 1 rem/600, all states (DES-06) and a visible focus ring. At most one primary per view (UX-06). Icon-only buttons have an accessible name. | Component audit; keyboard test |
| DES-19 | MUST | Links in running text are underlined (or carry another non-color cue) and differ from body text in color. They have hover and focus-visible states, and say when they open a new tab. Link text names the target (A11Y-15). Links navigate; buttons act. | Page review |
| DES-20 | SHOULD | Inputs: label above the field, 44 px height, one border style, focus ring in the focus token, error state with icon and text (A11Y-17). A placeholder never replaces the label. | Form review |
| DES-06 | MUST | Component inventory: every component documents its states (default, hover, focus-visible, active, disabled, loading, error, empty) and its responsive behavior. | Component library or `DESIGN.md` |
| DES-07 | SHOULD | Each component is built once and reused, in the design library and in code. No one-off variants without review. | Library usage report |

## Handcrafted look, style directions, motion

| ID | Level | Rule | Verify |
|---|---|---|---|
| DES-21 | MUST | No generic AI look: no unchanged default component-library styling, decorative purple-blue gradients or glows, emoji used as icons, everything centered, identical icon-card grids, stock 3D illustrations, mixed radii and shadows, random accent colors or filler copy. Every visual choice traces back to `DESIGN.md` and real content. | Design review against this list |
| DES-22 | SHOULD | Translucent style (if chosen): translucency only for navigation, overlays and floating surfaces, never behind long text. `backdrop-filter` gets an opaque `@supports` fallback, contrast is measured against the worst-case background (A11Y-07), blur ≤ 20 px. | Contrast check; low-end device test |
| DES-08 | SHOULD | Motion has a purpose (feedback, state change, orientation): UI transitions 150–300 ms, large elements ≤ 500 ms, one standard easing, only `transform` and `opacity` animated, plus a reduced-motion variant (A11Y-10). | Performance panel; OS setting |
| DES-23 | SHOULD | Micro-animations make the interface feel alive without distracting: hover and press feedback on interactive elements, smooth state changes, reveal on scroll once (≤ 400 ms, stagger ≤ 60 ms). Never animate the LCP element in, no scroll-jacking, no looping motion near text, nothing that delays content or input (PRF-01). Prefer CSS and the Web Animations API; reuse a small set of animated components. | Performance trace; reduced-motion check |

## Imagery, assets, QA

| ID | Level | Rule | Verify |
|---|---|---|---|
| DES-09 | SHOULD | Prefer authentic imagery (own team, products, customers) over stock. Art direction, aspect ratios and focal points are defined; image licenses are recorded (TEC-27). | Asset register |
| DES-10 | MUST | [house] Brand assets: SVG logo; favicon set declared on the home page, one per hostname, at a stable URL that Googlebot-Image may crawl: a square ICO containing ≥ 48 px images plus a 192 px PNG (Google recommends larger than 48×48 and lists BMP, GIF, ICO, PNG, JPEG, PPM, TIFF, not SVG; an SVG icon is an optional extra); 180 px apple-touch icon; manifest icons 192 and 512 px; and a default plus per-page Open Graph image (≥ 1200 px wide, 16:9: 1200×675, SEO-19). | [`head.html`](../templates/head.html) links resolve; URL Inspection on the home page |
| DES-11 | SHOULD | Before launch, production CSS is checked against `DESIGN.md`: no colors, font sizes, spacings or radii outside the tokens. | CSS audit |
| DES-12 | COULD | Dark mode follows `prefers-color-scheme` and offers a user toggle. | Manual check |

## Sources

- [W3C DTCG: Design Tokens Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/)
- [MDN: Using CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) · [MDN: clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp) · [MDN: text-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap)
- [MDN: backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter) · [MDN: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
- [Google: Favicons in Search](https://developers.google.com/search/docs/appearance/favicon-in-search) · [web.dev: Manifest](https://web.dev/learn/pwa/web-app-manifest)
