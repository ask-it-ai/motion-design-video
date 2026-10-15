---
version: 1
name: Ask-it × Endro — Frame (video / frame layer)
description: >
  Frame-scale design system for the Ask-it explainer v4 (1920×1080, 60 fps, 98 s). Two worlds
  share one canvas: the AVANT world (a brand site drained of color, anonymous, cold) and the ASK-IT
  world (off-white canvas, faint 44px grid, warm near-black ink, Ask-it coral as the one accent,
  pastel brand mesh). Real client UI (Endro diagnostic, Endro shop, Ask-it dashboard) is shown
  inside device frames at video scale. Atoms below are sacred; composition is free.
unit: the frame — 1920×1080
principle: atoms are sacred · composition is free · one idea per shot · the real product is the hero

colors:
  # ── Ask-it world (default) ──
  canvas: "#FDFCFC"          # off-white page ground (ask-it.ai --bg)
  surface: "#F5F5F7"         # secondary panels
  card: "#FFFFFF"
  ink: "#241F20"             # warm near-black: headlines, CTA pill
  ink-soft: "#6C6560"        # body / secondary text
  ink-mute: "#A39C95"        # captions, metadata
  line: "rgba(36,31,32,0.10)"
  grid: "rgba(36,31,32,0.05)" # 44px background grid lines
  coral: "#F8571F"           # THE accent (dashboard + site): one accent word, key numbers, active states
  coral-dark: "#D74B1B"
  coral-tint: "#FDEEE7"
  powder: "#ACCCE9"          # brand mesh only (soft glows), never text
  periwinkle: "#A7ABDD"      # brand mesh only
  greige: "#DDD7CD"
  good: "#1F8A4C"            # success states (added to cart, campaign active)
  good-tint: "#E9F5EE"
  ai: "#4A5FC1"              # Aski (AI assistant) accents only
  ai-tint: "#EEF0FA"
  # ── AVANT world (problem scenes) ──
  avant-bg: "#1B1718"
  avant-panel: "#2A2526"
  avant-line: "rgba(255,255,255,0.08)"
  avant-ink: "#F2EFEC"
  avant-mute: "#8C8580"
  # ── Endro (client brand, inside the phone and in brand moments only) ──
  endro-forest: "#173221"    # diagnostic panel, CONTINUER buttons
  endro-plum: "#2F095A"      # top banner "Magnifiques à tout âge"
  endro-corail: "#DF764C"    # profile CORAIL02 circle
  endro-orange: "#C9532B"    # product backgrounds (orange family)
  endro-navy: "#2C4A6E"      # product backgrounds (blue family)
  # ── Les Petits Prodiges (skin-swap moment only) ──
  lpp-cream: "#FBF6EF"
  lpp-ink: "#1A1A1A"

gradients:
  brand-mesh: "radial-gradient(60% 60% at 27% 23%, rgba(248,87,31,0.22) 0%, transparent 60%), radial-gradient(55% 55% at 78% 30%, rgba(172,204,233,0.55) 0%, transparent 62%), radial-gradient(60% 60% at 55% 85%, rgba(167,171,221,0.45) 0%, transparent 65%)"
  avant-vignette: "radial-gradient(ellipse 70% 70% at 50% 45%, rgba(0,0,0,0) 40%, rgba(0,0,0,0.55) 100%)"

radii:
  pill: "999px"
  card: "22px"
  card-sm: "14px"
  phone-body: "68px"
  phone-screen: "56px"
  window: "20px"
  avatar: "50%"

shadows:
  float: "0 40px 80px -24px rgba(36,31,32,0.22), 0 8px 24px -8px rgba(36,31,32,0.10)"
  card: "0 18px 40px -18px rgba(36,31,32,0.18), 0 2px 6px rgba(36,31,32,0.05)"
  phone: "0 60px 120px -30px rgba(36,31,32,0.35), 0 20px 40px -20px rgba(36,31,32,0.25)"
  avant-phone: "0 60px 120px -30px rgba(0,0,0,0.65)"

fonts:
  # every family below ships as a file in assets/fonts/ — declare @font-face in each composition
  Lufga: { files: ["assets/fonts/Lufga-Regular.woff2 (400)", "assets/fonts/Lufga-Medium.woff2 (500)", "assets/fonts/Lufga-SemiBold.woff2 (600)", "assets/fonts/Lufga-Bold.woff2 (700)"], role: "Ask-it display + UI text" }
  DM Sans: { files: ["assets/fonts/DMSans-normal-latin.woff2 (variable 300–800)"], role: "ALL numerals and stats (Ask-it renders digits in DM Sans)" }
  Archivo: { files: ["assets/fonts/Archivo-normal-latin.woff2 (variable 400–900)"], role: "Endro diagnostic headings (uppercase, bold) when rebuilt in HTML" }
  Mulish: { files: ["assets/fonts/Mulish-normal-latin.woff2 (variable 300–800)"], role: "Endro body text when rebuilt in HTML" }

typography:
  hero:      { fontFamily: "Lufga", px: 128, weight: 600, lineHeight: 1.0, tracking: "-0.035em", color: "ink" }
  h1:        { fontFamily: "Lufga", px: 96, weight: 600, lineHeight: 1.04, tracking: "-0.03em", color: "ink" }
  h2:        { fontFamily: "Lufga", px: 64, weight: 600, lineHeight: 1.08, tracking: "-0.02em", color: "ink" }
  h3:        { fontFamily: "Lufga", px: 44, weight: 500, lineHeight: 1.15, tracking: "-0.01em", color: "ink" }
  body:      { fontFamily: "Lufga", px: 30, weight: 400, lineHeight: 1.35, color: "ink-soft" }
  label:     { fontFamily: "Lufga", px: 22, weight: 500, tracking: "0.02em", color: "ink-soft" }
  eyebrow:   { fontFamily: "Lufga", px: 22, weight: 600, tracking: "0.14em", upper: true, color: "coral" }
  stat-xl:   { fontFamily: "DM Sans", px: 260, weight: 700, lineHeight: 0.9, tracking: "-0.05em", color: "ink", note: "+ / × signs in coral" }
  stat:      { fontFamily: "DM Sans", px: 140, weight: 700, lineHeight: 0.95, tracking: "-0.04em", color: "ink" }
  ui-number: { fontFamily: "DM Sans", px: 56, weight: 600, tracking: "-0.02em", color: "ink", note: "tabular-nums" }
  endro-h:   { fontFamily: "Archivo", px: 30, weight: 800, upper: true, tracking: "-0.01em", color: "#1A1A1A", note: "inside the phone, at phone scale" }
  kinetic:   { fontFamily: "Lufga", px: 96–150, neutral: "weight 500, ink-soft (AVANT: avant-mute)", accent: "weight 700, coral (AVANT: avant-ink)", tracking: "-0.03em", note: "two weights only; MK.words" }

components:
  phone:
    description: >
      iPhone-style device at MACRO scale (layout PHONE_MACRO): screen 780 px wide showing a real 2x
      screenshot (780 px source) at 1:1, so its text reads 26–30 px on screen; body = screen + 28 px rim
      (#111 with a 2 px inner rim rgba(255,255,255,0.12)), outer radius 96 px, screen radius 78 px, dynamic
      island 200×56 #000 pill 26 px from the top. The 2x screenshots already contain the status bar area:
      do not draw a second one. Shadow {shadows.phone} (AVANT: {shadows.avant-phone}). In AVANT scenes the
      screenshot gets filter: grayscale(0.75) brightness(0.88) contrast(1.05). Overlays (typed text, selection
      rings, the Ask-it entry pill, buttons turning green) are HTML drawn in screenshot pixels inside the screen.
  browser-window:
    description: >
      Desktop window for the dashboard: radius {radii.window}, white, 1.5px {colors.line} border,
      top bar 52px with three 12px dots (#FF5F57 #FEBC2E #28C840) and a centered URL pill
      "app.ask-it.ai" in ink-mute. Shadow {shadows.float}.
  card:
    backgroundColor: "{colors.card}"
    border: "1.5px solid {colors.line}"
    rounded: "{radii.card}"
    shadow: "{shadows.card}"
    description: "Floating UI cards (profile card, KPI tile, persona row, chat bubble)."
  answer-chip:
    description: >
      Pill chip that flies out of a tapped answer into the profile card: white, 1.5px line border,
      radius pill, 10px coral dot + label in Lufga 500 26px ink. On landing it settles into the
      profile card's chip row.
  profile-card:
    description: >
      White card 520 px wide: avatar 88px (persona photo assets/personas/claire.webp, white 4px ring),
      name "Claire" Lufga 600 40px, sub-label "Profil Endro · CORAIL02" Lufga 500 22px coral, a chip row
      that fills as answers land, and a thin progress bar (coral fill) labelled "Profil complété".
  pill-cta:
    backgroundColor: "{colors.ink}"
    textColor: "#FFFFFF"
    rounded: "{radii.pill}"
    typography: "Lufga 600 34px"
    description: "The one solid CTA: « Réserver une démo → ». Same as the ask-it.ai header button."
  step-pill:
    description: >
      The three steps « 01 Diagnostic · 02 Recommandation · 03 Dashboard »: white pills, 1.5px line
      border, number in a 40px coral circle (white DM Sans 600), label Lufga 500 30px ink. Active step:
      coral-tint fill + coral border.
  visitor-tag:
    description: >
      Small pill following the visitor's thumb/cursor: 36px avatar circle (grey silhouette in AVANT,
      Claire's photo after) + « Visiteuse anonyme » (AVANT) / « Claire » (after), Lufga 500 22px.
  touch:
    description: >
      Mobile touch indicator: 54px circle rgba(255,255,255,0.55) with 2px rgba(36,31,32,0.25) ring and
      soft shadow; on tap it scales 1 → 0.85 → 1 and emits a ripple ring (scale 1 → 2.2, opacity 0.5 → 0).
  grid-bg:
    description: >
      Ask-it background: {colors.canvas} + 44px square grid of 1px {colors.grid} lines + the brand-mesh
      gradient drifting slowly (scale 1 → 1.06 and ±40px over the scene). Shared by every Ask-it scene.
  avant-bg:
    description: >
      AVANT background: {colors.avant-bg} + 44px grid of 1px {colors.avant-line} + avant-vignette.
      No brand mesh, no coral.

spacing:
  safe-x: "120px"
  safe-top: "90px"
  keep-out-bottom: "y > 900px stays empty of key content"
  gap: "32px"

layout:
  # Shared constants (v4). All times inside a storyboard block are LOCAL to that scene (0 = scene start), at 60 fps.
  PHONE_MACRO: "the v4 default. Phone drawn at 1:1 of the 2x screenshots: screen 780 px wide (a 780×1688 screenshot fills it 1:1, so body text reads 26–30 px), body = screen + 28 px rim (836 px wide, radius 96 px outer / 78 px screen), dynamic island 200×56. The phone is taller than the frame: the camera (.rig) frames the part that matters. Pages scroll by translating the screenshot inside the screen (overflow hidden). Text the viewer must read is ≥ 26 px ON SCREEN."
  PHONE_WIDE: "when the whole phone must be seen (≤ 1.5 s per scene): PHONE_MACRO under a rig scale of 0.52–0.6."
  PILLS_ROW: "the three step pills on one row, vertically centred at y=540, pill height 120 px, label Lufga 600 44 px, number in a 64 px coral circle (DM Sans 700 34 px white); centres x=430 (01 Diagnostic), x=960 (02 Recommandation), x=1490 (03 Dashboard)"
  GRID_100: "10×10 visitor dots, 40 px circles, pitch 62 px (grid box 598×598), grid centred at x=600 y=540; the visitor 'Claire' is row 4 / col 6 (0-based: r=3, c=5)"
  STEP_CHIP: "small active step marker for steps 01–03: white pill 64 px tall at top-left (left 96 px, top 72 px), coral number circle 44 px + label Lufga 600 28 px ink"
  BACKGROUNDS: "each scene paints its own full-duration class='clip' background layer: grid-bg (Ask-it world, f05–f14) or avant-bg (AVANT world, f01–f04)"
---

# Ask-it × Endro — Frame

## Overview

The film follows one real visitor on a real brand site. **Endro** (organic skincare) is the brand
whose site, diagnostic and products we show; **Ask-it** is the product that changes her visit.
Everything Ask-it-side uses the Ask-it identity (off-white grid canvas, warm ink, coral accent, pastel
mesh, Lufga). Everything brand-side (inside the phone) is the real Endro UI: real screenshots of the
Endro shop and of the Endro diagnostic, real product packshots, real Nuancier textures.

## The two worlds

- **AVANT (scenes f01–f04):** the same Endro site drained of color (grayscale 75 %), anonymous visitor,
  dark warm-charcoal stage, vignette. The camera is just as alive as in the Ask-it world (v4: nothing
  freezes) but colder. Coral never appears here except as the single colored figure « 70 % ».
- **ASK-IT (scenes f05–f14):** the switch happens on « Bon… ça, c'était avant »: the dark world is sucked
  into a card and tossed away; f05 opens on the light canvas (44 px grid, brand mesh blooming). From here
  on the canvas is light.

## Composition rules

- One idea per shot. One focal element sharp; everything else under depth-of-field blur (6–14px).
- UI is shown BIG: a phone occupies 60–85 % of the frame height; a dashboard crop fills the frame.
  Any text the viewer must read is ≥ 28 px at 1080p.
- Device frames sit off-center (rule of thirds) with supporting cards/chips floating on the other side.
- Headlines: max 6 words, Lufga 600, one accent word in coral. Numbers in DM Sans 700, signs (+ ×) in coral.
- Keep the bottom band (y > 900 px) free of key content.
- Real faces humanize the data: persona portraits (assets/personas/*.webp) in circles with a white ring.

## Motion language v4 (measured frame by frame on Trellis, Gojiberry, lemlist, Taapit, Slack)

v3 froze 36 % of its frames; the references freeze 5–12 %. v4 is built so that **nothing ever stops**.
Every recipe below exists as a builder in `lib/motionkit.js` (`window.MK`) — use the builder, do not
re-invent the curve. Times in frames are at **60 fps** (`MK.F` = 1/60 s).

### Scene skeleton (every composition)

`#root` (data-fps="60") › background `.clip` (static ground) › `.shake` (tremor only) › `.rig` (the camera:
pans, snaps, zooms, dives) › `.drift` (`MK.drift` for the WHOLE scene, never off) › content layers.
One transform channel per wrapper — never tween the same property of one element from two places.

### The 10 laws

1. **Never frozen.** Action comes in bursts of ~0.2 s separated by slow drift. After a result lands, a
   lock of 14–17 frames, then drift again. No more than 0.5 s without a burst. Budget: ≤ 1 still frame in 10.
2. **UI in macro, filmed by a camera.** PHONE_MACRO (screen text 26–34 px on screen). The rig snaps and
   pans between targets; the secondary is cropped by the frame edge. The camera has a slight 3D attitude
   (rotateY/rotateX drifting −4° → +7° over a shot, perspective 1800–2400 px).
3. **A click is an event** — `MK.click`: touch pressed 3 frames before; on the click frame the UI state
   changes INSTANTLY (`tl.set`), the component pulses (0.97 → 1.025 → 1), the frame trembles (−8/+4 px),
   3 coral dashes radiate (17 frames) and the camera snaps +10–20 % toward the target (65 % in 1 frame).
4. **Exits accelerate, the cut lands on the fastest frame, the next scene arrives launched.** Each scene
   ENDS with its own exit (last 18 frames, `MK.exit` / `MK.zoomThrough` / `MK.suck` / `MK.toss`) whose fastest
   frame is the scene's last frame. Each scene STARTS in motion: launched entry in the same direction
   (`MK.enter`, circ.out, half the way in 6 frames) or oversized entry that brakes (`MK.enterBig` 1.36–1.48 → 1).
   Never an empty background for more than 1 frame. There are NO root transitions in v4.
5. **Real motion blur.** `data-hf-motion-blur='{"shutterAngle":360,"samplesPerFrame":12}'` on compact
   movers (numbers, words, chips, cards, icons, tossed objects) — never on an element that contains a
   large image. Large layers (phone, screenshots, panels, the whole stage) get the directional SVG blur
   from `MK.blurFilter` during their exits/entries/pans. Never both on the same element.
6. **Slam for every key number** (`MK.slam` after `MK.suck`): the previous content is sucked 100 → 55 %
   accelerating over 18 frames; the number arrives at ×6.5 and reaches 100 % in 9 frames without braking;
   −16.5 % undershoot 2 frames later; back in 14 frames; ±25 px frame shake on the impact frame. The impact
   frame sits on the stressed syllable (± 1 frame).
7. **Anticipation, overshoot, gravity.** Before every expansion, contract to 45–70 % over the 8 frames before
   (`MK.anticipate`). Pops (`MK.pop`): full size in 4 frames, +20–25 % at frames 7–8, back to 1 by frame ~26,
   never below 1. Tossed objects rise, hang, fall accelerating with a lagging rotation (`MK.toss`).
8. **Overlap.** A layer starts at the speed peak of the previous one, never after it ends. Offsets:
   1 frame (icons/dots), 3–5 frames (letters), 4 frames (a series of cards/chips/pills), 6–8 frames (words).
9. **Text carries the rhythm** (`MK.words`). Only the short key phrase named in the storyboard is written —
   never a full narration sentence. Neutral words: Lufga 500, land 0.1 s ahead of the voice, rise 40 px.
   Accent words: Lufga 700 (or DM Sans 700 for numbers), build letter by letter ON their syllable
   (cadence 3/4/5/6/10 frames), coral in the Ask-it world, avant-ink in the AVANT world.
10. **Depth and matter.** Planes tilted at rotateX 58–64° with rotateZ ±12° for the recommendation and the
    dashboard flights; floating cards drift ×1.4 faster than the plane (parallax); the background goes out of
    focus 5 frames BEFORE a foreground gesture (depth-of-field 6–14 px), never after.

### MK builders (signatures, times in seconds, scene-local)

- `MK.drift(tl, el, t0, dur, {zoom=.03, float=14, period=2.6, seed})` — continuous camera life
- `MK.pop(tl, el, t, {over=.22, from=0, inner})` · `MK.anticipate(tl, el, t, {to=.7, frames=8})`
- `MK.shake(tl, shakeEl, t, {px=8})` · `MK.slam(tl, el, t, {from=6.5, shakeEl, shakePx=25})` → impact time = t + 9 frames
- `MK.suck(tl, el, t, {to=.55, frames=18})` → end time
- `MK.click(tl, {t, x, y, layer, component, shakeEl, touch, rig, snap, rigScale})` (x/y in `layer` px)
- `MK.blurFilter(scopeEl, uniqueId)` → handle `{ramp, clear}` for directional blur on big layers
- `MK.exit(tl, el, t, {dir, dist=1400, frames=18, blur})` → cut time · `MK.enter(tl, el, t, {dir, dist=900, frames=38, blur})`
- `MK.enterBig(tl, el, t, {from=1.4, frames=40})` · `MK.zoomThrough(tl, rig, t, {origin:"x y", to=8, frames=18, blur})` → cut time
- `MK.snapZoom(tl, el, t, {from, to, origin, tail=16})` (S-curve: 5 % / 65 % in 2 frames / tail)
- `MK.pan(tl, el, t, {x, y, scale, frames=24, blur, axis})` (camera travel, blur at the speed peak)
- `MK.toss(tl, el, t, {rise=120, fall=1500, rotation=24, fallFrames=26, x})` → end of fall (= cut when it exits)
- `MK.words(tl, container, [{w, t, accent, letters}], {lead=.1})` → spans
- `MK.count(tl, t, {from, to, dur, penultimate, holdFrames=10, render})` → time of the final value
- `MK.type(tl, el, text, t, {cps=40})` · `MK.fly(tl, el, t, {dx, dy, arc=-140, frames=30})` → landing time
- `MK.ring(tl, layer, t, {x, y, r1=120, color})` · `MK.each(list, t, frames, fn)` · `MK.hash(n)` (deterministic 0–1)

Load it in every composition right after GSAP: `<script src="lib/motionkit.js"></script>` (inside the template).

## Do / Don't

- Do use the real assets listed in each storyboard block (paths under assets/).
- Do keep Endro UI faithful (Archivo uppercase headings, forest green buttons) when rebuilding it.
- Don't put narration sentences on screen; use short labels, numbers and the short key phrases the storyboard names (kinetic text).
- Don't fade between scenes, don't start a scene from rest, don't end a scene at rest (except the very last one).
- Don't use CSS transitions, Math.random, Date or timers; derive every pseudo-random value from MK.hash(index).
- Don't use pure black or pure white surfaces outside device screens; don't use gradient text.
- Don't invent claims or numbers: only those named in the storyboard.
