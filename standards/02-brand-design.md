# 02 · Brand & design

**Why it matters:** Visitors judge credibility in seconds, mostly from visual quality and consistency. A documented brand plus design tokens keep every page consistent and make changes cheap. Guide: steps 11–13.

Detail: `reference/google-search/` notes.

Scope: corporate identity, design tokens, color, typography, layout, components, motion, imagery, brand assets. The brand spec lives in [`DESIGN.md`](../templates/DESIGN.md) and the values in [`tokens.json`](../templates/tokens.json).

Last verified: 2026-10

| ID | Level | Rule | Verify |
|---|---|---|---|
| DES-01 | MUST | `DESIGN.md` documents the brand for people and AI agents: positioning (STR-03), personality, voice and tone, logo use, color roles, typography, imagery, icons, motion and glossary. | File exists and is current |
| DES-02 | MUST | Design tokens live in `tokens.json` (W3C DTCG format) in three tiers: primitive → semantic → component. Components use only semantic or component tokens, and code consumes them as CSS custom properties (TEC-04). | Token build; grep CSS for raw hex values |
| DES-03 | MUST | Every text/background pairing defined in tokens meets A11Y-07. Hover, focus, error, success and warning states have their own tokens. Dark mode, if offered, overrides the same semantic tokens. | Contrast check of token pairs |
| DES-04 | MUST | Typography: at most 2 families, a defined type scale (ratio 1.2–1.25) with fluid sizes via `clamp()`, body text ≥ 16 px, body line-height about 1.5, line length 45–75 characters. | Computed styles at 360 and 1440 px |
| DES-05 | SHOULD | Spacing follows a 4/8 px scale. The layout grid has content-driven breakpoints and a maximum content width. | Token file; visual QA |
| DES-06 | MUST | Component inventory: every component documents its states (default, hover, focus-visible, active, disabled, loading, error, empty) and its responsive behavior. | Component library or `DESIGN.md` |
| DES-07 | SHOULD | Each component is built once and reused, in the design library and in code. No one-off variants without review. | Library usage report |
| DES-08 | SHOULD | Motion has a purpose: UI transitions take 150–300 ms and animate only `transform` and `opacity`, with a reduced-motion variant (A11Y-10). | Performance panel; OS setting |
| DES-09 | SHOULD | Prefer authentic imagery (own team, products, customers) over stock. Art direction, aspect ratios and focal points are defined; image licenses are recorded (TEC-27). | Asset register |
| DES-10 | MUST | Brand assets: SVG logo; favicon set declared on the home page, one per hostname, at a stable URL that Googlebot-Image may crawl: a square ICO containing ≥ 48 px images plus a 192 px PNG (Google recommends larger than 48×48 and lists BMP, GIF, ICO, PNG, JPEG, PPM, TIFF, not SVG; an SVG icon is an optional extra); 180 px apple-touch icon; manifest icons 192 and 512 px; and a default plus per-page Open Graph image (≥ 1200 px wide, 16:9: 1200×675, SEO-19). | [`head.html`](../templates/head.html) links resolve; URL Inspection on the home page |
| DES-11 | SHOULD | Before launch, production CSS is checked against `DESIGN.md`: no colors, font sizes or spacings outside the tokens. | CSS audit |
| DES-12 | COULD | Dark mode follows `prefers-color-scheme` and offers a user toggle. | Manual check |

## Sources

- [W3C DTCG: Design Tokens Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/)
- [MDN: Using CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) · [MDN: clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)
- [Google: Favicons in Search](https://developers.google.com/search/docs/appearance/favicon-in-search)
- [web.dev: Manifest](https://web.dev/learn/pwa/web-app-manifest) · [MDN: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
