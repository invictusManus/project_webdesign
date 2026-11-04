#!/usr/bin/env python3
"""Validate templates/tokens.json (+ tokens.dark.json): DTCG types, units, references, theme coverage, contrast pairs (DES-03, DES-41)."""
import json, re, sys

TYPES = {"color", "dimension", "fontFamily", "fontWeight", "duration", "cubicBezier", "number",
         "strokeStyle", "border", "transition", "shadow", "gradient", "typography"}
REF = re.compile(r"^\{([^}]+)\}$")
errors = []

def flatten(node, path=(), out=None):
    out = {} if out is None else out
    if isinstance(node, dict) and "$value" in node:
        out[".".join(path)] = node
    elif isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                flatten(v, path + (k,), out)
    return out

def refs(value):
    if isinstance(value, str):
        m = REF.match(value)
        return [m.group(1)] if m else []
    if isinstance(value, dict):
        return [r for v in value.values() for r in refs(v)]
    if isinstance(value, list):
        return [r for v in value for r in refs(v)]
    return []

def units(value):
    if isinstance(value, dict):
        if "unit" in value and "value" in value and isinstance(value["value"], (int, float)):
            yield value["unit"]
        for v in value.values():
            yield from units(v)
    elif isinstance(value, list):
        for v in value:
            yield from units(v)

def resolve(tokens, path, seen=()):
    if path in seen:
        errors.append(f"reference cycle at {path}")
        return None
    tok = tokens.get(path)
    if tok is None:
        return None
    m = REF.match(tok["$value"]) if isinstance(tok["$value"], str) else None
    return resolve(tokens, m.group(1), seen + (path,)) if m else tok["$value"]

def luminance(hexs):
    c = [int(hexs[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def check(tokens, theme):
    for path, tok in tokens.items():
        if tok.get("$type") not in TYPES:
            errors.append(f"{theme}: {path} has no valid $type")
        for u in units(tok["$value"]):
            if u not in ("px", "rem", "ms", "s"):
                errors.append(f"{theme}: {path} uses unit '{u}' (DTCG allows px, rem; ms, s for durations)")
        for r in refs(tok["$value"]):
            if r not in tokens:
                errors.append(f"{theme}: {path} references missing {r}")
    sc = "semantic.color."
    pairs = [("text.default", "bg.default", 4.5), ("text.secondary", "bg.default", 4.5), ("text.muted", "bg.default", 4.5),
             ("text.link", "bg.default", 4.5), ("text.link-hover", "bg.default", 4.5), ("text.default", "surface.raised", 4.5),
             ("text.default", "bg.subtle", 4.5), ("text.default", "surface.card", 4.5), ("text.on-footer", "bg.footer", 4.5), ("action.secondary", "surface.card", 4.5), ("text.default", "bg.secondary", 4.5), ("text.inverse", "bg.inverse", 4.5),
             ("action.on-primary", "action.primary", 4.5), ("action.on-primary", "action.primary-hover", 4.5),
             ("action.on-primary", "action.primary-pressed", 4.5), ("action.secondary", "bg.default", 4.5),
             ("action.secondary", "action.secondary-hover-bg", 4.5), ("focus", "bg.default", 3), ("focus", "surface.raised", 3),
             ("border.input", "bg.default", 3), ("border.input-error", "bg.default", 3)]
    pairs += [(f"status.{s}.text", f"status.{s}.bg", 4.5) for s in ("success", "warning", "danger")]
    pairs += [(f"dataviz.{i}", "bg.default", 3) for i in range(1, 9) if f"{sc}dataviz.{i}" in tokens]
    for fg, bg, minimum in pairs:
        a, b = resolve(tokens, sc + fg), resolve(tokens, sc + bg)
        if not (a and b):
            errors.append(f"{theme}: contrast pair {fg} / {bg} not resolvable")
            continue
        ratio = contrast(a["hex"], b["hex"])
        if ratio < minimum:
            errors.append(f"{theme}: {fg} on {bg} is {ratio:.2f}:1, needs {minimum}:1")

base = flatten(json.load(open("templates/tokens.json", encoding="utf-8")))
check(base, "light")
dark_overrides = flatten(json.load(open("templates/tokens.dark.json", encoding="utf-8")))
for path in dark_overrides:
    if not path.startswith("semantic.") or path not in base:
        errors.append(f"dark: {path} overrides nothing in tokens.json semantic tier (DES-40)")
for path in base:
    if path.startswith("semantic.color.") and path not in dark_overrides and not path.startswith("semantic.color.dataviz."):
        errors.append(f"dark: {path} has no dark value (DES-40)")
check({**base, **dark_overrides}, "dark")

for e in errors:
    print(e)
sys.exit(1 if errors else 0)
