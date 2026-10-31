# 09 · Accessibility

Scope: WCAG 2.2 AA, EU accessibility law, semantics, perception, operation, understanding, testing.

Last verified: 2026-10

## Target & law

| ID | Level | Rule | Verify |
|---|---|---|---|
| A11Y-01 | MUST | Conform to WCAG 2.2 Level AA. WCAG 2.2 is ISO/IEC 40500:2025, and the EU standard EN 301 549 is moving to it. WCAG 3 is a draft, not a target. | Audit per A11Y-23 and A11Y-24 |
| A11Y-02 | MUST | [EU] B2C e-commerce services (Germany: BFSG, in force since 28 Jun 2025) must comply and publish an accessibility statement with a feedback contact. Exempt: service providers with < 10 employees **and** ≤ €2 m annual turnover or balance sheet. Sites outside that scope SHOULD publish a statement too. | Statement linked in footer |

## Structure & semantics

| ID | Level | Rule | Verify |
|---|---|---|---|
| A11Y-03 | MUST | Use landmarks (`header`, `nav`, `main`, `footer`) with exactly one `main`. The first focusable element is a skip link to the main content. | Screen reader landmark list |
| A11Y-04 | MUST | Headings form a logical outline with no skipped levels. Lists, tables (`th` with `scope`), buttons and links use native elements. ARIA only where no native element exists, following the ARIA Authoring Practices. | axe; heading outline tool |
| A11Y-05 | MUST | `lang` is set on `<html>` and on inline passages in another language. | HTML source |

## Perceivable

| ID | Level | Rule | Verify |
|---|---|---|---|
| A11Y-06 | MUST | Informative images have meaningful `alt` text; decorative images have `alt=""`. Icon-only controls have accessible names. Charts and diagrams have a text equivalent. | axe; manual review |
| A11Y-07 | MUST | Contrast: text ≥ 4.5:1, large text ≥ 3:1, UI components and focus indicators ≥ 3:1. Color is never the only carrier of meaning. | Contrast checker on tokens and screens |
| A11Y-08 | MUST | Content reflows at 320 CSS px and 200 % zoom without loss or 2-D scrolling (data tables and maps excepted). Text-spacing overrides don't break the layout. Zoom is never disabled. | Browser zoom; text-spacing bookmarklet |
| A11Y-09 | MUST | Videos have captions and audio has transcripts. No audio autoplays. Anything that moves for more than 5 s can be paused. | Manual review |
| A11Y-10 | MUST | Animation respects `prefers-reduced-motion`. Nothing flashes more than 3 times per second. | OS reduced-motion setting |

## Operable

| ID | Level | Rule | Verify |
|---|---|---|---|
| A11Y-11 | MUST | Everything works by keyboard alone, in a logical order, with no keyboard traps. | Keyboard-only walkthrough |
| A11Y-12 | MUST | Every focusable element shows a visible focus indicator. Sticky headers, chat widgets and cookie banners never hide the focused element entirely (2.4.11). | Keyboard walkthrough |
| A11Y-13 | MUST | Targets are at least 24 × 24 CSS px or have enough spacing (2.5.8). Primary controls SHOULD be 44 × 44 px. | Target-size check on mobile viewport |
| A11Y-14 | MUST | Every drag interaction has a single-pointer alternative (2.5.7). | Manual review |
| A11Y-15 | MUST | Link and button text makes sense in context. No "click here" or "read more" without an accessible name that says what. | Screen reader links list |

## Understandable

| ID | Level | Rule | Verify |
|---|---|---|---|
| A11Y-16 | MUST | Form fields have visible labels that are programmatically associated. Required fields and formats are stated in text. Personal-data fields use `autocomplete`. | axe; manual |
| A11Y-17 | MUST | Errors are shown in text next to the field, with a suggestion for fixing them. Status messages are announced through live regions. | Screen reader test of failed submit |
| A11Y-18 | MUST | No redundant entry: data already given in a process is auto-filled or offered for selection (3.3.7). | Multi-step flow test |
| A11Y-19 | MUST | Help (contact, chat, FAQ) appears in the same relative place on every page (3.2.6). | Template review |
| A11Y-20 | MUST | Accessible authentication: no cognitive test (puzzle, character transcription) without an alternative. Pasting and password managers are allowed (3.3.8). | Login and form test |
| A11Y-21 | SHOULD | Use plain language. Expand abbreviations on first use. Keep labels and navigation consistent. | Content review |

## Testing

| ID | Level | Rule | Verify |
|---|---|---|---|
| A11Y-22 | SHOULD | Run accessibility checks in component tests and end-to-end tests, not only on finished pages. | CI configuration |
| A11Y-23 | MUST | An automated axe-based scan shows 0 violations on every template in CI. Automated tools catch only some issues, so A11Y-24 still applies. | axe / Lighthouse CI |
| A11Y-24 | MUST | Key flows are tested manually: keyboard only, a screen reader (NVDA + Chrome or Firefox; VoiceOver + Safari on macOS and iOS), 200 % zoom and the mobile screen reader. | Test protocol |
| A11Y-25 | SHOULD | People with disabilities take part in usability tests of core flows. | Research report |

## Sources

- [W3C: What's new in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) · [WCAG 2.2 as ISO/IEC 40500:2025](https://www.w3.org/WAI/news/2025-10-21/wcag22-iso/)
- [W3C: WCAG 3 introduction](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/) · [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [EU: European Accessibility Act](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en)
- [BFSG §2 definitions](https://www.gesetze-im-internet.de/bfsg/__2.html) · [§3 microenterprise exemption](https://www.gesetze-im-internet.de/bfsg/__3.html)
- [AccessibleEU: EN 301 549 update](https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en)
