# Component: [Name]

Spec per CMP-01. One file or library page per component. Reference token names, never raw values (DES-02).

## Purpose

What it is for, and when not to use it (name the alternative component).

## Anatomy

| Part | Element | Token(s) | Required |
|---|---|---|---|
| e.g. title | `h3` (level fits the outline) | `semantic.text.h4` | yes |

## Variants and sizes

≤ 3 sizes (sm · md · lg) and the variants (e.g. primary, secondary). Each with its use case.

## States (DES-06)

| State | Visual change | Token(s) |
|---|---|---|
| default | | |
| hover (pointer only, LAY-08) | | |
| focus-visible | focus ring (DES-30) | `semantic.color.focus` |
| active | | |
| disabled | | |
| loading | | |
| error | | |
| empty | | |

## Behavior per tier (LAY-01)

| Tier | Layout and behavior |
|---|---|
| Mobile (< 600 px) | |
| Tablet (600–1023 px) | |
| Desktop (≥ 1024 px) | |

Container query breakpoints, if any (LAY-07):

## Accessibility

- WAI-ARIA APG pattern: [link or "native element"]
- Keyboard: Tab · Enter · Space · Esc · arrows
- Accessible name and role:
- Screen reader announcement for changes (A11Y-17):
- Target size on touch (LAY-08):

## Content limits

e.g. title ≤ 2 lines, text ≤ 3 lines, label ≤ 2 words. CMS block help text uses these (TEC-36).

## Do and don't

| Do | Don't |
|---|---|
| | |
