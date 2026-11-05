# Reference stack starter

Baseline for STK-01 to STK-16. Versions checked 2026-11 on npm; install the current versions and let the update bot keep them fresh (STK-02).

## Packages

| Purpose | Package (version checked) |
|---|---|
| Runtime | Node.js 26 LTS |
| Framework and UI | `next` 16.4 · `react` and `react-dom` 19.3 · `typescript` 7 |
| Styling | `tailwindcss` 4.3 |
| Components and icons | `radix-ui` 1.8 · `lucide-react` 1.69 |
| Motion (gestures only) | `motion` 14 |
| Forms | `react-hook-form` 7 · `zod` 4 |
| Content (pick one) | `payload` 3 · `sanity` 6 · MDX |
| Database (only if needed) | `drizzle-orm` with Postgres |
| Multilingual | `next-intl` 4 |
| Testing | `vitest` 5 · `@playwright/test` 1.64 · `@axe-core/playwright` 4 · `@lhci/cli` |
| Code quality | `@biomejs/biome` 2 · pnpm |

## Styles: load order

```css
/* app/globals.css */
@import "tailwindcss";
@import "./tokens.css";          /* from scripts/tokens_to_css.py */
@import "./tailwind-theme.css";  /* also from scripts/tokens_to_css.py: token-only utilities (STK-07) */
@import "./motion.css";          /* templates/motion.css */
```

Utilities then follow the tokens: `bg-action-primary`, `text-text-muted`, `p-4` (16 px, `space.4`), `rounded-md`, `shadow-card`, `text-h2`, `ease-enter`, and the `tablet:`, `desktop:`, `wide:` breakpoints (LAY-01).

## `next.config.ts` essentials

```ts
const config = {
  poweredByHeader: false,                    // SEC-06
  images: { remotePatterns: [] },            // STK-06: allowlist only
  async headers() {
    return [{ source: "/(.*)", headers: [    // SEC-03; CSP with nonces in proxy.ts (SEC-04, SEC-05)
      { key: "X-Content-Type-Options", value: "nosniff" },
      { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
    ] }];
  },
};
export default config;
```

## Project layout

```
app/            routes (Server Components by default, STK-03); sitemap.ts, robots.ts (STK-05)
components/     one folder per component from the catalogue (CMP-01)
lib/            schemas (zod), data access (server only)
styles/         globals.css, tokens.css, tailwind-theme.css, motion.css
tests/          vitest unit tests, playwright e2e + axe
```
