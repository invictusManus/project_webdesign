# Icons: how to use them

For DES-17, DES-33 and DES-42. Library choice: [`reference/assets/`](../reference/assets/README.md). Default: Lucide.

## Install one library

```bash
npm i lucide-react        # React · vanilla JS: lucide · Vue: lucide-vue-next
```

Import single icons, never the whole set. The bundler ships only what you import.

## Use

```jsx
import { Menu, ArrowRight } from "lucide-react";

// Decorative: next to visible text. Hidden from screen readers.
<a href="/pricing">See pricing <ArrowRight size="1em" strokeWidth={1.5} aria-hidden="true" /></a>

// Standalone: the button needs an accessible name (A11Y-06).
<button type="button" aria-label="Open menu" aria-expanded="false">
  <Menu size={24} strokeWidth={1.5} aria-hidden="true" />
</button>
```

Vanilla JS: `import { createIcons, Menu } from "lucide"; createIcons({ icons: { Menu } });` with `<i data-lucide="menu" aria-hidden="true"></i>`.

## Rules in practice

| Do | Why |
|---|---|
| Size from `primitive.iconSize.*` (16, 20, 24, 32) or `1em`–`1.272em` next to text | DES-17, DES-33 |
| Stroke from `primitive.iconStroke` on every icon | One stroke width per site (DES-17) |
| Color through `currentColor` (the default); never hard-code a fill | Themes and forced colors work (DES-31, DES-40) |
| Label standalone icons; `aria-hidden="true"` on decorative ones | A11Y-06 |
| Text label next to anything but search, menu, close, home, cart | DES-33 |
| Mirror directional icons in RTL: `[dir="rtl"] .icon-directional { transform: scaleX(-1); }` | I18N-10 |
| Touch targets ≥ 44 px around icon buttons, even when the icon is 24 px | LAY-08 |

## Handover

Add to the third-party inventory (TEC-20) and the handover (TEC-27): library, version, license (e.g. "Lucide 1.x, ISC"). An Iconify set needs its own license line; CC BY sets need visible attribution.
