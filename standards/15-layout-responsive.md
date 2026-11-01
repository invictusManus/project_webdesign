# 15 · Layout & responsive design

**Why it matters:** The same page is used on a 360 px phone, a tablet in either orientation and a 1920 px monitor, by touch, mouse and keyboard. Fixed breakpoints, grids and page regions make every template predictable on every device, and they keep content, focus and calls to action visible where users expect them. Guide: steps 13–14.

Scope: breakpoints, grid, content widths, responsive type and spacing, reflow, input modality, viewport and device behavior, tablets, content parity, responsive media, wide content, page anatomy, header, navigation, hero, sections, footer, fixed elements, print, responsive QA. Tokens and type scale: [`02-brand-design.md`](02-brand-design.md). Components: [`16-components.md`](16-components.md).

Last verified: 2026-11

## Device tiers

| Tier | Width (CSS px) | Columns | Gutter | Outer margin | Section padding |
|---|---|---|---|---|---|
| Mobile | 0–599 | 4 | 16 | 16 | 42 |
| Tablet | 600–1023 | 8 | 26 | 26 | 68 |
| Desktop | 1024–1439 | 12 | 26 | 42 | 68–110 |
| Wide | ≥ 1440 | 12, container capped (LAY-03) | 26 | auto | 110 |

## Grid and spacing

| ID | Level | Rule | Verify |
|---|---|---|---|
| LAY-01 | MUST | Breakpoints are tokens for the four tiers above, written as mobile-first `min-width` media queries in `em` so they also follow the user's default font size (tokens hold px; the build emits `em`). Extra breakpoints only where content breaks (DES-16), never per device model. | Token file; CSS review |
| LAY-02 | MUST | Each tier uses the columns, gutters and outer margins from the table. Content never touches the viewport edge (≥ 16 px margin). Elements span whole columns and share alignment lines across sections (PSY-02). | Grid overlay at 360, 768, 1024, 1440 px |
| LAY-03 | MUST | Three content widths: prose ≤ 66 ch (≈ 680–720 px), wide 1200–1280 px (DES-16) and full-bleed for media and background bands only. Text never runs to full width on tablet, desktop or wide screens, and no line exceeds 75 ch at 1920 px. | Measure at 768, 1440, 1920 px |
| LAY-04 | MUST | Type scales per tier with `clamp()` built from `rem` plus `vw`, so text still enlarges at 200 % zoom (WCAG 1.4.4). Body never drops below 16 px on any tier and may rise to 18 px on desktop. Headings step down per DES-04, tablets interpolate. Mobile keeps ≥ 35 ch per line. | Computed styles at 360, 768, 1440 px; 200 % zoom |
| LAY-05 | MUST | Section padding follows the tier table. Card and grid gaps are 16 px on mobile and 26 px from tablet up. Control heights and component padding stay the same on every tier. | Computed styles per tier |

## Reflow and adaptation

| ID | Level | Rule | Verify |
|---|---|---|---|
| LAY-06 | MUST | Layouts collapse in a predictable order: 61.8/38.2 splits stack once a column would fall below 320 px; card grids show 1 column on mobile, 2 on tablet, 3–4 on desktop (`repeat(auto-fit, minmax(min(100%, 280px), 1fr))`). Visual order equals DOM order on every tier; no `order` or `row-reverse` that breaks reading or focus order (WCAG 1.3.2, 2.4.3). | Resize test; keyboard walkthrough per tier |
| LAY-07 | SHOULD | Reusable components (card, media object, teaser, widget) adapt to their container with container queries (`@container`); viewport media queries handle page layout only. | CSS review; component in narrow and wide slot |
| LAY-08 | MUST | Input modality: hover effects only under `@media (any-hover: hover) and (any-pointer: fine)` (so trackpad tablets get them), sizing for touch under `(pointer: coarse)`, and every hover reveal has a tap and focus equivalent (UX-05). On coarse pointers, primary controls are ≥ 44 × 44 px with ≥ 8 px between adjacent targets (A11Y-13). Swipe and other path-based gestures always have a single-pointer button alternative (WCAG 2.5.1; drag: A11Y-14). Pinch zoom is never blocked by `touch-action` or the viewport tag (TEC-01, A11Y-08). | Touch device test; DevTools pointer emulation |
| LAY-09 | MUST | Viewport and device: full-height areas use `svh`/`dvh` with a `vh` fallback; fixed and sticky bars respect `env(safe-area-inset-*)` (set `viewport-fit=cover` only when insets are handled). Portrait and landscape both work, with no orientation lock (WCAG 1.3.4). The on-screen keyboard never hides the focused field (no fixed bottom bar over inputs). | iOS and Android device test in both orientations |
| LAY-10 | SHOULD | Tablets: test portrait 768–834 px and landscape 1024–1180 px. Don't infer touch from width: tablets with keyboard and trackpad get hover and focus styles too (LAY-08). Two-column layouts hold only while each column is ≥ 320 px. | Device test in both orientations |
| LAY-11 | MUST | Content parity: every tier carries the same content and functions (SEO-39). Smaller screens reorder (mobile-first DOM order) and condense (accordions, scrollable rows with a visible overflow cue) but never remove. At 360 × 640 the first screen shows the H1, the value proposition and the primary call to action (UX-07). | Compare mobile and desktop DOM; screenshot at 360 × 640 |
| LAY-12 | MUST | Responsive media: `srcset`/`sizes` match the layout width per tier (PRF-06); `<picture>` art direction when the subject would be too small on mobile; focal points kept with `object-position`; aspect-ratio tokens reserve space (PRF-07). No text baked into images; background images never carry content. | Network panel per tier; screenshot review |
| LAY-13 | MUST | Tables, code blocks, charts and maps never cause page-level horizontal scrolling (UX-05, A11Y-08): they sit in a labelled, keyboard-focusable scroll container (`role="region"`, `aria-label`, `tabindex="0"`) or switch to a stacked layout below 600 px (CMP-04, WCAG 1.4.10). | 320 and 360 px test; keyboard scroll |

## Page structure

| ID | Level | Rule | Verify |
|---|---|---|---|
| LAY-14 | MUST | Every template is built from fixed regions in this order: skip link → `header` → optional breadcrumbs (UX-03) → `main` with the H1 as its first heading → `footer` (A11Y-03). Each page type documents its section order in `DESIGN.md`, e.g. landing page: hero → problem and value → proof → offer or how it works → FAQ → final call to action. One section holds one idea under one H2. | Template review; heading outline |
| LAY-15 | MUST | Header: logo at the start linking home (PSY-06), primary navigation, utilities (search, language, account, cart), at most one call to action at the end, in the same order on every page (UX-02). Height ≤ 72 px on desktop, ≤ 64 px on mobile. If sticky, it hides on scroll down and returns on scroll up on mobile, and `scroll-padding-top` equals its height so anchors and focus stay visible (A11Y-12). | Template review per tier; keyboard and anchor test |
| LAY-16 | MUST | Navigation per tier: from 1024 px, inline primary navigation; dropdowns and mega menus open on click, Enter and Space (hover optional) and follow the WAI-ARIA disclosure pattern. Below 1024 px, a labelled menu button (≥ 44 px, `aria-expanded`) opens a panel listing items in the desktop order. A modal drawer traps focus, closes with Esc and returns focus to the button. The current page has `aria-current="page"`. Apps may add a bottom tab bar of ≤ 5 items, each with icon and label. | Keyboard and screen reader test per tier |
| LAY-17 | MUST | Hero: H1, a one-sentence value proposition and the primary call to action (secondary optional) are visible without scrolling on every tier (UX-07). Height is content-driven and never above 100 svh. Text over images passes A11Y-07 against the worst-case area (use a scrim). The hero image follows PRF-08. | Screenshots at 360 × 640, 768 × 1024, 1440 × 900 |
| LAY-18 | SHOULD | Section rhythm: text/media splits alternate sides on desktop; on mobile, heading and text come before media unless the media is the content. Background bands use ≤ 2 surface tones, with no two full-bleed image bands in a row. Sections separate by spacing or a surface change, not both plus rules and shadows. | Full-page screenshot per tier |
| LAY-19 | MUST | Footer: brand and short claim, key navigation (UX-02), contact (UX-12) and a legal row that is never collapsed: Impressum (PRV-10), privacy policy (PRV-04), cookie settings (PRV-02), terms where applicable, copyright, plus language switch (I18N) and social links where they exist. 4–5 columns on desktop, 2 on tablet, 1 on mobile (link groups may collapse into disclosures). Footer links meet LAY-08 on touch. | Template review per tier |
| LAY-20 | MUST | On mobile, all fixed and sticky elements together (header, call-to-action bar, chat launcher, banners) cover ≤ 25 % of the viewport height, and at most one sticky call-to-action bar exists. None hides the focused element (A11Y-12). | Screenshot at 360 × 640 with all elements active |
| LAY-21 | SHOULD | Content pages (articles, docs, recipes, invoices) have a print stylesheet: navigation, banners and video hidden; dark text on white; external link URLs printed after the link; `break-inside: avoid` on figures and tables; `break-after: avoid` on headings. | Print preview |
| LAY-22 | SHOULD | Responsive QA: every template is checked at the QA-02 widths plus 320 px (WCAG 1.4.10), 844 × 390 (phone landscape) and 1180 × 820 (tablet landscape), and at 200 % zoom. Visual regression snapshots (QA-06) cover mobile, tablet and desktop. | Screenshot set; snapshot diff |

## Sources

- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/): [1.3.2 Meaningful sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html) · [1.3.4 Orientation](https://www.w3.org/WAI/WCAG22/Understanding/orientation.html) · [1.4.4 Resize text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) · [1.4.10 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) · [2.4.3 Focus order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) · [2.5.1 Pointer gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html)
- [W3C WAI-ARIA APG: Disclosure navigation menu](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/) · [Dialog (modal)](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- [MDN: Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries) · [MDN: hover and pointer media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover) · [MDN: env()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env) · [MDN: length units (svh, dvh)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length) · [MDN: Printing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing)
- [Material Design 3: Breakpoints](https://m3.material.io/foundations/layout/breakpoints/overview) · [Material Design 3: Accessibility, touch targets](https://m3.material.io/foundations/designing/structure) · [Apple HIG: Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Google: Mobile-first indexing best practices](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
