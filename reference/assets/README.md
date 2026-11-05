# Asset sources: icons, animation, illustrations

A vetted list of free sources for DES-42 to DES-44. Reference only: nothing is copied into this repository. Sites install the chosen package from npm and ship only what they use. Licenses and counts verified 2026-11 against npm, jsDelivr and each source's license page; re-check before relying on a count. The weekly maintenance job (`scripts/asset-check.py`) reports license changes and deprecated packages.

## Icons (DES-42)

Pick one library per site. Default: Lucide.

| Library | License | Size | Package | Use when |
|---|---|---|---|---|
| [Lucide](https://lucide.dev) | ISC | 2,313 icons, 24 px grid, adjustable stroke | `lucide`, `lucide-react`, `lucide-vue-next`, `lucide-static` | Default: consistent outline style, tree-shakable per icon |
| [Tabler Icons](https://tabler.io/icons) | MIT | 5,203 outline + 1,054 filled, 24 px grid | `@tabler/icons`, `@tabler/icons-react` | Lucide lacks the icon, or filled variants are needed |
| [Phosphor](https://phosphoricons.com) | MIT | 1,512 icons × 6 weights (9,072) | `@phosphor-icons/core`, `@phosphor-icons/react` | The brand needs weight variety (thin to duotone) |
| [Iconify](https://iconify.design) | Per set: 144 MIT, 53 CC BY 4.0, 31 Apache 2.0, 13 OFL, 10 CC0, some CC BY-SA and GPL | 276 sets, ≈ 474,000 icons | `@iconify/json`, `@iconify-json/<set>` | A specialist icon no other library has. Check the set's license first: CC BY needs attribution, GPL and CC BY-SA are excluded by default. |
| [Simple Icons](https://simpleicons.org) | CC0 1.0 | 3,467 brand logos | `simple-icons` | Social, payment and tool logos. Each brand's own trademark rules still apply. |

## Animation (DES-43)

Use the first option that does the job.

| Option | License | Package | Use when |
|---|---|---|---|
| CSS transitions, `@keyframes`, `@starting-style`, scroll-driven animations, View Transitions, Web Animations API | Web standard | none | Default: hover, press, reveal, enter/exit, page transitions. Template: [`motion.css`](../../templates/motion.css) |
| [AutoAnimate](https://auto-animate.formkit.com) | MIT | `@formkit/auto-animate` | Lists and layouts that add, remove or reorder items (≈ 2 KB) |
| [Motion](https://motion.dev) | MIT | `motion` | Gestures, drag, spring physics, shared layout in React, Vue or vanilla JS |
| [GSAP](https://gsap.com) | Free "standard no-charge" license, not OSI open source ([terms](https://gsap.com/standard-license)) | `gsap` | Complex timelines and scroll storytelling. Record the license decision in the third-party inventory (TEC-20). |
| [lottie-web](https://github.com/airbnb/lottie-web) · [dotLottie](https://docs.lottiefiles.com/) | MIT | `lottie-web`, `@lottiefiles/dotlottie-web` | Designer-made illustrative animation (After Effects export). Prefer `.lottie` (compressed). |

## Illustrations (DES-44)

| Source | License | Use when |
|---|---|---|
| [Open Peeps](https://www.openpeeps.com) | CC0 | Hand-drawn people, mix-and-match |
| [unDraw](https://undraw.co/license) | Own free license: no attribution needed; no redistribution in packs, no AI training, no replicating the service | Flat illustrations recolored to the brand; use inside the site only |

Own or commissioned illustrations beat both (DES-09, DES-21).

## Design intake inspiration (⚗)

| Source | License | What it offers | Caveats |
|---|---|---|---|
| [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) data CSVs (checked 2026-11) | MIT | ~50 active style names, palettes for 192 product types, 34 landing section orders, font-pairing names | Unofficial and "derived" by its own provenance file. Palettes must be re-derived into 60-30-10 (DES-14) and contrast-checked (12 accents fail 3:1). Font pairings load Google Fonts from a CDN, which conflicts with PRF-10 and PRV-07: use the names only. Its motion presets (glow, parallax) conflict with DES-21 and DES-43. |
