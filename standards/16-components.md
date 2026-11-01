# 16 · Components

**Why it matters:** Users learn a site through its components. A card, a dialog or a tab that looks and behaves the same everywhere, on every device and for every input method, makes pages faster to build and easier to use. Standard patterns also make them accessible by default. Guide: steps 13–15.

Scope: component specification, cards, lists, tables, badges, avatars, choice controls, selects, date and file inputs, form layout, search, dialogs, drawers, toasts, alerts, tooltips, popovers, tabs, accordions, carousels, pagination, steppers, loading, empty and error states, media players, maps, pricing tables, testimonials, breadcrumbs, consent banner layout. Buttons, links and inputs: DES-18 to DES-20. Tokens: [`02-brand-design.md`](02-brand-design.md). Tiers and page regions: [`15-layout-responsive.md`](15-layout-responsive.md).

Last verified: 2026-11

## Specification

| ID | Level | Rule | Verify |
|---|---|---|---|
| CMP-01 | MUST | Every component is specified in the library or `DESIGN.md`: anatomy, variants (≤ 3 sizes), tokens used, states (DES-06), behavior per tier (LAY-01), keyboard and ARIA behavior following the WAI-ARIA APG pattern where one exists, and content limits (e.g. title ≤ 2 lines). | Library docs review |

## Content elements

| ID | Level | Rule | Verify |
|---|---|---|---|
| CMP-02 | MUST | Cards: one card shows one object. A clickable card has one real link (usually the title), stretched over the card with a pseudo-element, and no nested interactive elements inside that link. Fixed anatomy order: media → eyebrow → title (a heading at the right outline level) → text (≤ 3 lines) → meta → action. Cards in a row share equal height. Padding is 16 px on mobile and 26 px from tablet up, radius per DES-17, hover lift only under LAY-08, and a `:focus-within` ring. | Component audit; keyboard and screen reader test |
| CMP-03 | SHOULD | Lists use native `ul`, `ol` or `dl` with hanging markers aligned to the text and item spacing per DES-25. Link lists keep rows ≥ 24 px (44 px on touch, LAY-08). Visible lists longer than 7 items are grouped under subheadings. | Markup review |
| CMP-04 | MUST | Tables hold data only, never layout. They have a `<caption>` or label and `th` with `scope` (A11Y-04). Text aligns to the start, numbers to the end with tabular numerals (DES-26). Long tables keep the header row sticky, use zebra stripes or dividers (not both), and rows ≥ 44 px on touch. Sortable headers are buttons with `aria-sort`. Below 600 px, use a scroll container with a sticky first column, or stack rows into label–value cards (LAY-13). | Markup review; 360 px test |
| CMP-05 | SHOULD | Badges and tags: labels of ≤ 2 words, pill radius, ≤ 3 per item. Status badges carry text, not just color (A11Y-07). Interactive chips are buttons of ≥ 24 px (44 px on touch), and removable chips have a "Remove [label]" button. | Component audit |
| CMP-06 | SHOULD | Avatars use the sizes 24, 32, 42 and 68 px with an initials fallback. `alt` is the person's name, or empty when the name is shown next to it (A11Y-06). | Component audit |

## Forms and search

| ID | Level | Rule | Verify |
|---|---|---|---|
| CMP-07 | MUST | Choice controls are native inputs (restyled with `appearance: none`, or visually hidden with a styled label). The visible box is ≥ 20 px, and the label is part of a hit area ≥ 44 px tall on touch. Radios serve 2–6 visible options; more options use a select. Groups use `fieldset` and `legend`. Toggle switches only for settings that take effect immediately (`role="switch"`), with a label naming the setting. | Keyboard and screen reader test; touch test |
| CMP-08 | MUST | Native `<select>` by default; custom comboboxes follow the APG combobox pattern. Known dates (e.g. birthday) are typed with the format shown; scheduling uses a picker that also accepts typing. File upload uses a native input, with drag and drop as an optional extra (A11Y-14). Accepted types and size limits are stated before upload, with progress and a remove option per file. `type`, `inputmode`, `autocomplete` and `enterkeyhint` bring up the right mobile keyboard (A11Y-16). | Device test on iOS and Android; keyboard test |
| CMP-09 | MUST | Form layout: one column on every tier. Two short, related fields may sit side by side from 600 px (postcode and city). Field width hints at the expected input length, labels sit above (DES-20) with help text below, and the required-field marker is explained. The submit button aligns with the field column and is full width on mobile. Never disable the submit button to signal errors; validate on blur and on submit. Long forms show an error summary that links to each field, plus inline errors (A11Y-17). | Form review per tier; failed-submit test |
| CMP-10 | SHOULD | Search: a `<search>` element or `role="search"`, `type="search"`, a visible label or a labelled icon button, and height ≥ 44 px. Suggestions follow the APG combobox pattern; Esc clears. Results pages show the query and the result count. Position: top-right on desktop (PSY-06), in the header or menu panel on mobile. | Keyboard and screen reader test |

## Overlays and feedback

| ID | Level | Rule | Verify |
|---|---|---|---|
| CMP-11 | MUST | Dialogs use `<dialog>` with `showModal()` or the APG modal dialog pattern. Focus moves into the dialog and stays there, Esc closes it, and focus returns to the trigger. The dialog is labelled by its title and has a visible close button (≥ 44 px); the background is inert and does not scroll. Widths: 400, 560 or 800 px on desktop; full screen below 600 px with safe-area padding (LAY-09). Dialogs never open on page load, except mandatory gates (UX-17). Destructive confirmations name the action ("Delete project", not "OK"). | Keyboard and screen reader test per tier |
| CMP-12 | SHOULD | Drawers are ≤ 400 px wide: navigation slides in from the start, filters and cart from the end. On mobile, bottom sheets have a drag handle plus a close button (A11Y-14). Modal drawers follow CMP-11. | Keyboard and touch test |
| CMP-13 | MUST | Toasts only confirm non-critical events (`role="status"`). Blocking errors appear inline or in an alert (`role="alert"`, A11Y-17). Toasts stay ≥ 5 s, pause on hover and focus, and persist until dismissed if they contain an action (WCAG 2.2.1). At most 3 stack at once: bottom-center on mobile (above bottom bars and safe areas), bottom-end on desktop, never covering the primary action or the focused element. Inline alerts span their container with an icon, text and an optional action; non-critical alerts can be dismissed. | Screen reader test; timing check |
| CMP-14 | MUST | Tooltips hold short supplemental text only: no interactive content and nothing essential. They show on both hover and focus, can be dismissed with Esc, can be hovered and stay open while hovered (WCAG 1.4.13). On touch devices use a toggletip button or inline text instead. Popovers with interactive content use the `popover` attribute or an APG disclosure or dialog pattern, stay inside the viewport and flip at its edges. | Keyboard, pointer and touch test |

## Navigation and disclosure

| ID | Level | Rule | Verify |
|---|---|---|---|
| CMP-15 | MUST | Tabs follow the APG tabs pattern (arrow keys move between tabs, Tab moves into the panel, `aria-selected`), with ≤ 6 tabs. Tabs switch views within one page; navigation between pages uses links. On mobile, tabs scroll horizontally with a visible overflow cue or become an accordion. | Keyboard and screen reader test; 360 px test |
| CMP-16 | MUST | Accordions use `<details>`/`<summary>` or the APG accordion pattern (a button inside a heading, `aria-expanded`). The whole header row is clickable and ≥ 44 px tall, the chevron reflects the state, and several panels may be open at once. Collapsed content stays findable with find-in-page (`<details>` or `hidden="until-found"`). Price, legal and safety information is never collapsed on desktop. | Keyboard test; find-in-page test |
| CMP-17 | SHOULD | Avoid carousels for key content. If used: visible previous/next buttons and slide indicators (≥ 44 px on touch), "Slide x of y" labels, no autoplay, or autoplay with a pause button that also stops on hover and focus (WCAG 2.2.2). Swiping is never the only control (A11Y-14). Use CSS scroll snap, with the next slide peeking on mobile. | Keyboard, screen reader and touch test |
| CMP-18 | MUST | Lists of more than 24 items paginate with real links (`<a href="?page=2">`, SEO-14), "Page x of y" and previous/next controls of ≥ 44 px on touch; mobile shows previous, current and next. "Load more" and infinite scroll keep paginated URLs, move focus to the first new item and leave the footer reachable. | Crawl test; keyboard test |
| CMP-19 | SHOULD | Multi-step flows show "Step x of y" with step names (≤ 7 steps; mobile shows only the current step's name) and allow going back without losing data (A11Y-18). Progress bars use `<progress>` or `role="progressbar"` with a value. | Flow test |
| CMP-20 | SHOULD | Breadcrumbs (UX-03): `nav` labelled "Breadcrumb" containing an `ol`, separators drawn in CSS, and the current page as plain text with `aria-current="page"`. On mobile, show only the parent link ("← Parent") or let the trail scroll horizontally. | Markup review; 360 px test |

## States

| ID | Level | Rule | Verify |
|---|---|---|---|
| CMP-21 | MUST | State components (UX-10): skeletons match the final layout's dimensions (no layout shift, PRF-01), appear only when loading takes > 300 ms, and drop the shimmer under reduced motion (A11Y-10). A loading button keeps its width and sets `aria-busy`. Empty states say why there is no content and offer one action. Error states say what happened and how to fix it, and offer a retry. Changes are announced through a live region (A11Y-17). | State inventory; screen reader test |

## Patterns

| ID | Level | Rule | Verify |
|---|---|---|---|
| CMP-22 | SHOULD | Video and audio players: native controls or a keyboard-operable player with captions (A11Y-09), a poster image (PRF-09), reserved aspect ratio (PRF-07), full container width, and no autoplay with sound. | Keyboard test; caption check |
| CMP-23 | SHOULD | Maps load behind a click-to-load placeholder (TEC-21), never trap keyboard or scroll focus, and come with the address as text plus a directions link. | Keyboard test; text check |
| CMP-24 | SHOULD | Pricing tables: ≤ 4 plans (PSY-04), one recommended plan marked with a text label (not just color), feature rows in the same order in every plan, and price with billing period and tax status (PSY-13). On mobile, plans stack with the recommended one first, or sit in a scroll-snap row; the full comparison follows CMP-04. | Review per tier |
| CMP-25 | SHOULD | Testimonials (PSY-12): quotes of ≤ 50 words with name, role and photo. Logo walls use one treatment (monochrome or original colors) and are sized by optical area; at most 2 rows on mobile. | Review per tier |
| CMP-26 | MUST | Consent banner layout (PRV-02): accept and reject share one button tier and size, both reachable by keyboard before any other control. The banner never hides the focused element (A11Y-12). It sits at the bottom of the screen on mobile within the LAY-20 budget; a full-screen sheet only if it carries no non-essential tracking before choice (PRV-01). The footer link reopens it (LAY-19). | Keyboard test; screenshot at 360 × 640 |

## Sources

- [W3C WAI-ARIA Authoring Practices Guide: Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/) (accordion, breadcrumb, combobox, dialog, disclosure, tabs, carousel, switch, table)
- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/): [1.4.13 Content on hover or focus](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html) · [2.2.1 Timing adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html) · [2.2.2 Pause, stop, hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- [MDN: `<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog) · [MDN: popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API) · [MDN: `<search>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search) · [MDN: inputmode](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode) · [MDN: hidden="until-found"](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden)
- [Google: Pagination and incremental page loading](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)
