#!/usr/bin/env python3
"""Fit a scene to its host slot in index.html: optional lead-in pad and tail hold.

pad  — the scene's own timeline is nested, unchanged, in a wrapper at +pad seconds, so a root-level
       transition can show the scene during the voice pause before its first cue.
tail — the scene's clips stay visible `tail` seconds after the scene's nominal end, holding the final
       frame while the root transition hands over to the next scene.
Timed elements are re-windowed (a clip starting at 0 still starts at 0; any later clip shifts by pad;
a clip that ran to the end now runs to the end of the slot). Original values are kept in data-fit-*
attributes, so the script is idempotent: re-running restores the originals first.

usage: fit_slot.py compositions/f07-dashboard.html --pad 0.35 --tail 0.20
"""
import argparse, re

ap = argparse.ArgumentParser()
ap.add_argument("path"); ap.add_argument("--pad", type=float, default=0.0); ap.add_argument("--tail", type=float, default=0.0)
a = ap.parse_args()
src = open(a.path, encoding="utf-8").read()
MARK = "/* fit_slot lead-in */"
fmt = lambda v: f"{round(v, 3):g}"

# 1. restore a previous fit
src = re.sub(r'data-start="[^"]*" data-fit-start="([^"]*)"', r'data-start="\1"', src)
src = re.sub(r'data-duration="[^"]*" data-fit-duration="([^"]*)"', r'data-duration="\1"', src)
m = re.search(r"\n[ \t]*" + re.escape(MARK) + r"\n.*?__lead\.add\((\w+)\.paused\(false\), [\d.]+\);\n[ \t]*window\.__timelines\[([^\]]+)\]\s*=\s*__lead;", src, re.S)
if m:
    src = src.replace(m.group(0), f"\n      window.__timelines[{m.group(2)}] = {m.group(1)};")

# 2. scene duration from the template root
root = re.search(r'<div[^>]*\bid="root"[^>]*>', src) or re.search(r'<[a-z]+[^>]*data-composition-id="[^"]+"[^>]*>', src)
D = float(re.search(r'data-duration="([\d.]+)"', root.group(0)).group(1))
P, T = a.pad, a.tail
if P == 0 and T == 0:
    open(a.path, "w", encoding="utf-8").write(src); print(f"{a.path}: restored (D={fmt(D)})"); raise SystemExit

# 3. re-window every timed element (root included)
def rewin(tag):
    s = re.search(r'data-start="([\d.]+)"', tag); d = re.search(r'data-duration="([\d.]+)"', tag)
    if not s or not d: return tag
    s0, d0 = float(s.group(1)), float(d.group(1)); e0 = s0 + d0
    s1 = 0.0 if s0 < 1e-6 else s0 + P
    e1 = P + D + T if e0 >= D - 1e-3 else e0 + P
    tag = tag.replace(s.group(0), f'data-start="{fmt(s1)}" data-fit-start="{s.group(1)}"', 1)
    return tag.replace(d.group(0), f'data-duration="{fmt(e1 - s1)}" data-fit-duration="{d.group(1)}"', 1)
src = re.sub(r'<[a-z][a-z0-9-]*\b[^>]*data-start="[\d.]+"[^>]*>', lambda mm: rewin(mm.group(0)), src)

# 4. lead-in wrapper around the registered timeline
if P > 0:
    reg = list(re.finditer(r"window\.__timelines\[([^\]]+)\]\s*=\s*(\w+)\s*;", src))
    assert len(reg) == 1, f"expected one timeline registration, found {len(reg)}"
    r = reg[0]
    wrapped = (f"{MARK}\n      var __lead = gsap.timeline({{ paused: true }});\n"
               f"      __lead.add({r.group(2)}.paused(false), {fmt(P)});\n"
               f"      window.__timelines[{r.group(1)}] = __lead;")
    src = src[: r.start()] + wrapped + src[r.end():]
open(a.path, "w", encoding="utf-8").write(src)
print(f"{a.path}: D={fmt(D)} pad={fmt(P)} tail={fmt(T)} -> slot {fmt(P + D + T)}")
