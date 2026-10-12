---
version: 1
name: Ask-it × Endro — Frame (video / frame layer)
description: >
  Frame-scale design system for the Ask-it explainer (1920×1080, 30 fps, ~105 s). Two worlds
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

components:
  phone:
    description: >
      iPhone-style device. Body 470×1000 px at 1:1 (scale freely), radius {radii.phone-body}, body
      #111 with a 2px inner rim rgba(255,255,255,0.12), screen inset 14px, screen radius
      {radii.phone-screen}, dynamic island 120×34 pill #000 centered 20px from the top, status bar
      (time "9:41", signal/wifi/battery glyphs) 22px Lufga 600 ink. Screen content is either a real
      2x screenshot (390-pt wide = 780 px source) sized to the screen width, or rebuilt HTML.
      Shadow {shadows.phone}. In AVANT scenes the screen gets filter: grayscale(0.85) brightness(0.85).
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
  # Shared handoff constants — neighbouring frames must match these exactly at their seams.
  # All times in storyboard blocks are LOCAL to the frame (0 = frame start).
  PHONE: "body 470×1000 px, screen inset 14 px → screen 442×972 px. A real 2x screenshot (780 px wide) is drawn at width 442 px (scale 0.5667) under a 44 px iOS status bar ('9:41', signal/wifi/battery, ink on white). Pages scroll by translating the screenshot inside the screen (overflow hidden). Scroll amounts in the storyboard are in SCREEN px (after the 0.5667 scale)."
  PHONE_HERO: "light world: phone scaled 0.9 (423×900 rendered), center x=700 y=520, no tilt"
  PHONE_AVANT: "dark world (frame 1): phone scaled 0.9, center x=860 y=520"
  PILLS_ROW: "the three step pills on one row, vertically centered at y=540, pill height 88 px, centers x=520 (01 Diagnostic), x=960 (02 Recommandation), x=1400 (03 Dashboard)"
  GRID_100: "10×10 visitor dots, 26 px circles, 18 px gap (pitch 44 px), grid centered at x=520 y=520"
  BACKGROUNDS: "each frame paints its own full-duration class='clip' background layer: grid-bg (Ask-it world) or avant-bg (AVANT world)"
---

# Ask-it × Endro — Frame

## Overview

The film follows one real visitor on a real brand site. **Endro** (organic skincare) is the brand
whose site, diagnostic and products we show; **Ask-it** is the product that changes her visit.
Everything Ask-it-side uses the Ask-it identity (off-white grid canvas, warm ink, coral accent, pastel
mesh, Lufga). Everything brand-side (inside the phone) is the real Endro UI: real screenshots of the
Endro shop and of the Endro diagnostic, real product packshots, real Nuancier textures.

## The two worlds

- **AVANT (scenes 1–2):** the same Endro site drained of color (grayscale 85 %), anonymous visitor,
  dark warm-charcoal stage, vignette, slow heavy camera. Nobody guides her. Coral never appears here
  except as the single colored figure « 70 % ».
- **ASK-IT (scenes 3–9):** the switch happens on « Bon… ça, c'était avant » — color floods back from
  the center, the 44px grid draws itself, the brand mesh blooms. From here on the canvas is light.

## Composition rules

- One idea per shot. One focal element sharp; everything else under depth-of-field blur (6–14px).
- UI is shown BIG: a phone occupies 60–85 % of the frame height; a dashboard crop fills the frame.
  Any text the viewer must read is ≥ 28 px at 1080p.
- Device frames sit off-center (rule of thirds) with supporting cards/chips floating on the other side.
- Headlines: max 6 words, Lufga 600, one accent word in coral. Numbers in DM Sans 700, signs (+ ×) in coral.
- Keep the bottom band (y > 900 px) free of key content.
- Real faces humanize the data: persona portraits (assets/personas/*.webp) in circles with a white ring.

## Motion language (calibrated on the Agence 1600 references, measured frame by frame)

The reference films never hard-cut and never freeze: a new composition every ~1.25 s (median), about
one visual attack per second, and every hold carries a slow scale drift. Match that energy.

- **Lead the voice:** an element appears 150–300 ms BEFORE the word it illustrates is spoken.
- **Entrances (UI, cards, words):** 0.25–0.45 s, expo.out or back.out(1.6), combined transform
  (y 30–60 px + scale 0.9 → 1 + blur 10 px → 0). Groups stagger 20–60 ms (≤ 0.5 s total).
- **Number slam** (stats like 70 %, ×4, +36 %): fromTo yPercent −120 + blur 12 px → 0 in ~70 ms
  (power4.in), land with back.out(2) (slight undershoot, settle in ~270 ms), then 10–12 thin radial
  impact lines (SVG strokes) scale 1 → 1.6 and fade 1 → 0 in 250 ms. Then the digits may count.
- **Word slam** (interjection / pivot): scale 6 → 1 with blur 30 → 0 px, back.out(2), 0.47 s; the
  previous element is first sucked out (scale 0.8, blur 6 px, opacity 0 in ~70 ms).
- **UI rising in perspective:** perspective 1400 px; fromTo rotationX 35° → 10° (or rotationY 70° → 12°)
  + yPercent 60 → 0 in 0.45 s power3.out, then settles to 5–10° over 0.5 s (sine.out); the UI may be
  cropped by the frame edge. A giant keyword can sit BEHIND a tilted UI (lower z-index).
- **Inside-scene camera** (world wrapper translate/scale): 0.4–0.7 s power2.inOut with blur at peak
  speed; between moves a slow drift (scale −3 to +4 % per second-ish) keeps every frame alive.
- **Whip / zoom-through inside a frame** (when a frame changes its own layout): outgoing group
  translates 100–120 % of the width in 0.15–0.25 s (expo.in) with directional blur, or scales 1 → 1.3 with
  blur 0 → 20 px in 0.1–0.25 s; the next layout arrives calmly (0.3 s fade/typing) 0–1 frame later.
- **Persistent objects:** prefer re-arranging the same objects (FLIP-style position/scale moves,
  expo.out 0.35–0.6 s, stagger 20–40 ms) over replacing them.
- **Logo build:** mark drawn or popped in ~200 ms, letters staggered 33–50 ms, pale → brand color.
- **Taps:** cursor/touch travels power2.inOut 0.25 s, press scale 0.95 for 0.1 s, ring r 0 → 60 px with
  opacity 1 → 0 in 0.35 s; the tapped element reacts in the same beat.
- **Two-tone headlines:** hierarchy by color, not weight — main words ink, complement ink-soft.
- Counters roll in DM Sans tabular-nums and land exactly on the voice cue.
- No CSS transitions, no exits on non-final scenes (the assembler owns scene seams).

## Do / Don't

- Do use the real assets listed in each storyboard block (paths under assets/).
- Do keep Endro UI faithful (Archivo uppercase headings, forest green buttons) when rebuilding it.
- Don't put narration sentences on screen; use short labels, numbers and single accent words.
- Don't use pure black or pure white surfaces outside device screens; don't use gradient text.
- Don't invent claims or numbers: only those named in the storyboard.
