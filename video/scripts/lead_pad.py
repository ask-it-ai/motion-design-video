#!/usr/bin/env python3
"""Give a scene a lead-in pad so a root-level transition can show it before its first cue.

The scene's own timeline is nested, unchanged, inside a wrapper timeline at +PAD seconds, and the
template root's data-duration grows by PAD. Idempotent: a file that already carries a pad is
re-padded from its original timeline, never stacked.

usage: lead_pad.py compositions/f07-dashboard.html 0.35
"""
import re, sys

path, pad = sys.argv[1], float(sys.argv[2])
src = open(path, encoding="utf-8").read()
MARK = "/* orchestrator lead-in pad */"

if MARK in src:  # undo a previous pad first
    m = re.search(r"\n[ \t]*" + re.escape(MARK) + r".*?window\.__timelines\[(['\"])(.+?)\1\]\s*=\s*__lead;", src, re.S)
    orig = re.search(r"__lead\.add\((\w+)\.paused\(false\), ([\d.]+)\);", m.group(0))
    var, old = orig.group(1), float(orig.group(2))
    src = src.replace(m.group(0), f'\n      window.__timelines["{m.group(2)}"] = {var};')
    src = re.sub(r'(data-composition-id="[^"]+"[^>]*?data-duration=")([\d.]+)(")',
                 lambda d: f"{d.group(1)}{round(float(d.group(2)) - old, 3):g}{d.group(3)}", src, count=1)

reg = list(re.finditer(r"window\.__timelines\[(['\"])(.+?)\1\]\s*=\s*(\w+)\s*;", src))
assert len(reg) == 1, f"expected one timeline registration, found {len(reg)}"
r = reg[0]
comp_id, var = r.group(2), r.group(3)
wrapped = (f"{MARK}\n      const __lead = gsap.timeline({{ paused: true }});\n"
           f"      __lead.add({var}.paused(false), {pad:g});\n"
           f'      window.__timelines["{comp_id}"] = __lead;')
src = src[: r.start()] + wrapped + src[r.end():]

root = re.search(r'(<[^>]*data-composition-id="' + re.escape(comp_id) + r'"[^>]*>)', src)
tag = root.group(1)
dm = re.search(r'data-duration="([\d.]+)"', tag)
if dm:
    new_tag = tag.replace(dm.group(0), f'data-duration="{round(float(dm.group(1)) + pad, 3):g}"')
    src = src.replace(tag, new_tag, 1)
open(path, "w", encoding="utf-8").write(src)
print(f"{path}: {comp_id} padded {pad:g}s (timeline var {var})" + (f", root duration -> {round(float(dm.group(1)) + pad, 3):g}" if dm else ", root has no data-duration"))
