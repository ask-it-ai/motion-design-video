---
format: 1920x1080
fps: 60
duration: 98.0s
message: "Ask-it transforme vos visiteurs anonymes en clients… et en data."
arc: Hook (visiteuse perdue) → 70 % → Problème → Budget à l'aveugle → Bascule → Ask-it → Diagnostic → Profil → Recommandation → Chiffres → Dashboard → Insights → Zéro effort → Elle revient → CTA
audience: fondateurs et responsables e-commerce de marques beauté / DNVB françaises
mode: autonomous
voice: assets/audio/vo_v4.wav (Martin Dupont narrateur + Victoria visiteuse) — word timings in assets/audio/vo_v4_timeline.json
motion: frame.md → "Motion language v4" + lib/motionkit.js (window.MK). Measured on Trellis, Gojiberry, lemlist, Taapit, Slack (docs/motion-avance.md).
---

v4 rules that override everything older:

- 60 fps. Every composition root carries `data-fps="60"`. Times below are LOCAL seconds (0 = scene start); "N frames" = N/60 s.
- **Seams are authored inside the scenes.** Each scene ENDS with its own accelerating exit whose fastest frame is the scene's last frame, and STARTS already moving (launched entry in the same direction, or oversized entry that brakes). The assembler hard-cuts between scenes: no root transitions, no fades.
- **Never frozen**: `MK.drift` on the `.drift` wrapper for the whole scene; a burst of action at least every 0.5 s; after a result, lock 14–17 frames, then drift.
- Shared layouts (PHONE_MACRO, PILLS_ROW, GRID_100, STEP_CHIP) and every token live in frame.md.
- On-screen text: only the short key phrases written below in « » — never a full narration sentence.

---

## Frame 1 — Hésitation

- scene: Macro on her phone in the dark AVANT world: she flings through the Endro serums page, taps one serum, rejects it, taps another, drowns in a swarm of products (« trop de choix ») and tosses the tab away.
- duration: 9.25s (global 0.00–9.25)
- world: AVANT
- entry: first frame already moving — the page is mid-fling (scrolling up fast, vertical blur)
- exit: the page card falls out of the bottom of the frame with gravity (down, ~3500 px/s at the last frame)
- status: outline
- voiceover: "Hmm… c'est lequel pour ma peau ? Celui-là ?… Ah non. Celui-là ! Ah bah non, pas lui non plus… Oh là là… y a vraiment trop de choix. Bon. Je verrai plus tard."
- src: compositions/f01-hesitation.html
- blueprint: compose
- rules: MK.drift, MK.click, MK.pan, MK.snapZoom, MK.pop, MK.words, MK.suck, MK.toss, MK.blurFilter
- focal: the product tiles of the Endro serums page (macro), then the swarm, then the tossed page
- roles: phone (PHONE_MACRO, AVANT filter) = her screen · touch = her thumb · visitor-tag « Visiteuse anonyme » (grey silhouette) = her · packshot swarm = overwhelm · page card = the tab she closes
- assets: assets/screens/endro-shop/collection-serums.png (780×9978) · assets/endro/products/*.jpg (11 packshots, 1000×1000) · assets/fonts/Lufga-*.woff2
- sfx: orchestrator

Voice cues (local s): Hmm 0.45–0.93 · c'est 1.21 · lequel 1.35–1.75 · pour 1.79 · ma 1.95 · peau ? 2.18–2.49 · Celui-là ? 2.98–3.33 · Ah 3.85 · non. 3.95–4.11 · Celui-là. 4.63–5.00 · Oh 5.50 · là 5.62 · là, 5.74–5.85 · y 6.13 · a 6.21 · vraiment 6.31–6.62 · trop 6.68–6.89 · de 6.93–6.99 · choix. 7.03–7.28 · Bon, 7.78–7.89 · je 8.17 · verrai 8.25–8.45 · plus 8.48–8.58 · tard 8.64–8.83

Geometry: phone body centred x=900; the rig frames TWO product rows of the page at a time (tiles ≈ 340 px wide on screen). Measure the tile boxes on the PNG yourself (source px; rows of tiles start around y≈580, 1200, 1820, 2420 in the 780-px-wide source; left column x≈40–380, right column x≈400–740). Visitor-tag: avant-panel pill, 52 px grey silhouette + « Visiteuse anonyme » Lufga 500 30 px avant-ink, floating right of the phone at the thumb's height (x≈1390).

Scene 1 (0.00–1.20s): ENTRY. The page is already flung: its scroll goes 300 → 1450 source px over 1.0 s (expo.out) with vertical SVG blur 16 → 0 over the first 10 frames. The touch indicator finishes the flick (up 260 px in 8 frames, then fades 50 %). Visitor-tag pops at 0.25 (MK.pop). On « Hmm » (0.45) the scroll overshoots and settles back 60 px (sine.inOut 0.5 s): hesitation.
Scene 2 (1.20–2.90s): « c'est lequel pour ma peau ? » — slow camera travel across the two visible rows (rig x −120 over 1.2 s, sine.inOut) while the thumb hovers from tile to tile (touch moves, 3 legs of 0.35 s power2.inOut). At 2.18 a « ? » bubble (avant-panel circle 84 px, « ? » Lufga 700 54 px avant-ink) pops on the visitor-tag (MK.pop over .25).
Scene 3 (2.98–4.40s): « Celui-là ? » — CLICK at 2.98 on the left tile of the upper row: MK.click with all 4 responses (touch press, tile pulse, frame tremble −8/+4, 3 dashes in avant-ink, rig snap +18 % toward the tile). On the click frame (tl.set) a 4 px white ring (radius 16) appears around the tile and the tile lifts (shadow). « Ah non. » (3.85–4.11): the ring shakes x −10/+8/−6/+4/−2/0 (3 frames per leg) and dims; at 4.11 ring off (instant). 4.10–4.33: WHIP to the neighbour tile (rig x −390, 14 frames power3.inOut, horizontal SVG blur peaking 10 px at the speed peak).
Scene 4 (4.63–5.40s): « Celui-là. » — CLICK at 4.63 on the right tile (same 4 responses, snap +10 %), ring + lift on the click frame.
Scene 5 (5.42–7.70s): « Oh là là… y a vraiment trop de choix. » — MK.snapZoom OUT on the rig from its current scale to 0.5 (start 5.42, the 65 % jump lands at 5.57) revealing the whole phone; at 5.58 the swarm bursts from behind the phone: 12 packshots (rounded 26 px, 180–240 px squares, grayscale 0.75, avant shadow) fly radially to their spots (20 frames expo.out) and pop (MK.pop), 1-frame offsets; three depth rings — near (scale 1.25, blur 6 px, frame edges, drift ×1.4), mid (sharp), far (scale 0.7, blur 4 px, 70 % opacity, drift ×0.6). Kinetic text centred over the phone (MK.words): « trop de » neutral (Lufga 500 120 px avant-mute, lead 0.1) and « choix » accent (Lufga 700 150 px avant-ink) built letter by letter from 7.03. With each word more products pop in: +4 at 6.68, +4 at 6.93, +6 at 7.03 (1-frame offsets, positions from MK.hash, repeats of the 11 images allowed, rotations ±12°).
Scene 6 (7.78–8.40s): « Bon, » — LOCK 14 frames (only drift). 7.92–8.25: the swarm is sucked back behind the phone (each packshot x/y → phone centre, scale 0.3, fade, 18 frames power2.in, 1-frame offsets in reverse order); the words exit up (12 frames expo.in); the rig snap-zooms back to 0.8 on the phone (MK.snapZoom start 7.95).
Scene 7 (8.40–9.25s): « je verrai plus tard » — EXIT. The thumb presses the page at 8.40; at 8.46 the page becomes a card (screenshot container: scale 0.86, radius 40 px, shadow; 6 frames power2.out) and is TOSSED: MK.toss(page, 8.52, {rise 110, fall 1500, rotation 16, fallFrames 26}) → its fall ends at 9.25. Behind it the phone screen is an empty avant-panel. The visitor-tag and its « ? » drop with it (MK.toss, 4 frames later, smaller). Rig follows the fall over the last 12 frames (y −160, power2.in). Vertical SVG blur ramp 0 → 20 px on the page card over the last 8 frames. Last frame = fastest frame of the fall.

## Frame 2 — Soixante-dix

- scene: 100 visitor dots fall in; hers drops out of the grid; « 70 % » slams and 69 more dots fall away; then everything shoots up.
- duration: 3.75s (global 9.25–13.00)
- world: AVANT
- entry: launched DOWN — the grid arrives from above still falling (same direction as frame 1's toss), brakes
- exit: everything accelerates UP out of frame (~3500 px/s at the last frame)
- status: outline
- voiceover: "Non. Elle ne reviendra pas. Comme soixante-dix pourcent de vos visiteurs."
- src: compositions/f02-soixante-dix.html
- blueprint: compose
- rules: MK.enter, MK.toss, MK.anticipate, MK.slam, MK.pop, MK.words, MK.exit
- focal: her dot, then the « 70 % » stat and the falling dots
- roles: GRID_100 dots = visitors (avant-ink 70 %) · her dot (r3,c5) with a white 3 px ring = Claire · « 70 % » = the stat (DM Sans 700 300 px avant-ink, « % » coral — the only coral of the AVANT world)
- assets: assets/fonts/DMSans-normal-latin.woff2 · assets/fonts/Lufga-*.woff2
- sfx: orchestrator

Voice cues (local s): Non, 0.33–0.48 · elle 0.65 · ne 0.79 · reviendra 0.90–1.31 · pas, 1.35–1.52 · comme 1.69–1.88 · 70 % 2.05–2.65 · de 2.69 · vos 2.79 · visiteurs 2.92–3.50

Scene 1 (0.00–0.63s): ENTRY. GRID_100 launched down: MK.enter(grid, 0, {dir:"down", dist:900, frames:38, blur}) — vertical blur 16 → 0 in 6 frames. Her ring pops at 0.12 (MK.pop over .25).
Scene 2 (0.25–1.60s): « Non, elle ne reviendra pas » — MK.anticipate her dot (to 0.6) then at 0.33 she drops: MK.toss(herDot, 0.33, {rise 18, fall 900, rotation 0, fallFrames 30}) out of the bottom; a faint dashed ring stays in the empty slot (fades in at 0.45, 50 %). Rig pushes toward the slot (scale 1 → 1.12 over 1.0 s, sine.inOut, origin on the slot); at 1.35 the dashed ring pulses (×1.15) and dims to 25 %.
Scene 3 (1.69–2.70s): « comme 70 % » — the grid contracts (MK.anticipate to 0.86 over the 8 frames before 2.05) while « 70 % » SLAMS on the right: MK.slam(stat, 1.90, {shakeEl}) → impact 2.05 (stat block x 1080–1720, baseline y≈600, data-hf-motion-blur). On the impact frame the grid springs back (MK.pop from 0.86, over .12) and 69 more dots fall: MK.toss each (rise 6–14 px, fall 700–1000 px, fallFrames 22–30, from MK.hash), 1-frame offsets in a MK.hash-shuffled order (2.05 → ~3.2). The 30 dots that remain brighten to 90 %.
Scene 4 (2.69–3.45s): « de vos visiteurs » — MK.words under the stat (x≈1090, y≈700): « de vos » neutral (Lufga 500 64 px avant-mute), « visiteurs » accent (Lufga 700 64 px avant-ink, letters from 2.92).
Scene 5 (3.45–3.75s): EXIT — MK.exit(rig, 3.45, {dir:"up", dist:1400, frames:18, blur}); last frame = fastest.

## Frame 3 — Le problème

- scene: Kinetic text over a traffic chart that keeps climbing (traffic is fine), then a whip down onto a tilted wall of identical phones that all scroll in sync, each with a « ? » nobody answers; the camera dives into one « ? ».
- duration: 6.90s (global 13.00–19.90)
- world: AVANT
- entry: launched UP (continues frame 2's exit) — the traffic card and the first words rise from below and brake
- exit: zoom-through into the central « ? » bubble (expo.in, ~×9, the last frame is the fastest)
- status: outline
- voiceover: "Le problème, ce n'est pas votre trafic. Sur votre site, tout le monde voit la même chose… et personne n'est là pour guider."
- src: compositions/f03-probleme.html
- blueprint: compose
- rules: MK.enter, MK.words, MK.pop, MK.pan, MK.drift, MK.zoomThrough, MK.blurFilter
- focal: the word « trafic » + the climbing line, then the wall of phones, then the « ? »
- roles: traffic card = traffic is not the problem · identical phones = same site for everyone · « ? » bubbles = nobody guides
- assets: assets/screens/endro-shop/collection-serums.png · assets/fonts/Lufga-*.woff2 · assets/fonts/DMSans-normal-latin.woff2
- sfx: orchestrator

Voice cues (local s): Le 0.24 · problème, 0.35–0.74 · ce 0.91 · n'est 1.03 · pas 1.20 · votre 1.35 · trafic. 1.63–2.10 · Sur 2.44 · votre 2.60 · site, 2.92–3.14 · tout 3.31 · le 3.43 · monde 3.54–3.77 · voit 3.82 · la 3.95 · même 4.05–4.22 · chose 4.25–4.58 · et 4.75 · personne 4.95–5.41 · n'est 5.44 · là 5.59 · pour 5.80 · guider 6.01–6.33

Scene 1 (0.00–2.30s): ENTRY + « Le problème, ce n'est pas votre trafic. » — a traffic card (avant-panel 1200×520, radius 28, centre x=960 y=620) launched up: MK.enter(card, 0, {dir:"up", dist:900, frames:38, blur}). Inside: « Trafic » (Lufga 600 40 px avant-ink), « Visites / mois » (Lufga 500 26 px avant-mute) and a line chart (SVG, 5 px avant-ink stroke, 12 points rising with small dips) drawing left → right from 0.05 to 2.10 (stroke-dashoffset), its last segment steep on « trafic » (1.63–2.10); at 2.10 a green check badge (#4CC27F circle 72 px, white check) pops at the line's end (MK.pop over .25). Kinetic text above the card (y≈190, centred): line A « Le problème, » (MK.words, Lufga 500 84 px avant-mute) from 0.14; at 0.85 line A exits up (12 frames expo.in) while line B builds: « ce n'est pas votre » neutral + « trafic. » accent (Lufga 700 96 px avant-ink, letters from 1.63).
Scene 2 (2.30–2.62s): WHIP DOWN inside the scene — MK.pan(rig, 2.30, {y:-1080, frames:18, blur, axis:"y"}) to the phone wall below.
Scene 3 (2.44–4.70s): « Sur votre site, tout le monde voit la même chose » — the wall: 15 phones (5 × 3, each ≈ 300×650: PHONE_MACRO scaled 0.36, grayscale screens = collection-serums.png at the same scroll) on a plane tilted rotateX 60°, rotateZ −12° (perspective 2000 px); a tiny grey visitor avatar on each phone's top-right corner. Phones pop in a diagonal order with 4-frame offsets from 2.50 (MK.pop over .2). The camera flies over the plane (plane x −120, y +300 over 2.5 s, sine.inOut) and ends with the CENTRAL phone at frame centre (960, 520). At « même chose » (4.05) every screen scrolls in perfect sync (−420 source px, 24 frames power3.inOut): identical.
Scene 4 (4.75–6.60s): « et personne n'est là pour guider » — a « ? » bubble (avant-panel circle 72 px, « ? » Lufga 700 44 px avant-ink) pops above each phone, 4-frame offsets from 4.95 (MK.pop over .25), each wobbling (rotation ±6°, drift). Plane slowly pushes in (scale 1 → 1.1). Lock 14 frames after « guider » (6.33–6.56) with drift only.
Scene 5 (6.60–6.90s): EXIT — MK.zoomThrough(rig, 6.60, {origin:"960px 470px" (the central « ? »), to:9, frames:18, blur}); last frame = fastest.

## Frame 4 — Le budget brûle (et c'était avant)

- scene: The ad budget counter burns upward, the visitor profile is all question marks, campaign settings are poked at random, everything goes blind — then the whole dark world is sucked into a card and tossed away.
- duration: 7.72s (global 19.90–27.62)
- world: AVANT
- entry: oversized entry that brakes (the camera arrives from the « ? » dive)
- exit: the dark card falls out of the bottom with gravity (down, ~3500 px/s)
- status: outline
- voiceover: "Résultat : vous brûlez votre budget sur des visiteurs dont vous ne savez rien. Et vous optimisez… à l'aveugle. Bon… ça, c'était avant."
- src: compositions/f04-budget.html
- blueprint: compose
- rules: MK.enterBig, MK.words, MK.snapZoom, MK.count, MK.pan, MK.pop, MK.anticipate, MK.enter, MK.click, MK.suck, MK.toss
- focal: the counter, then the profile card, then the settings card, then the card of the past
- roles: spend card = budget · embers = money burning · profile card with « ? » = unknown visitor · settings card = blind optimisation · card + toss = « c'était avant »
- assets: assets/fonts/DMSans-normal-latin.woff2 · assets/fonts/Lufga-*.woff2
- sfx: orchestrator

Voice cues (local s): Résultat : 0.25–0.74 · vous 1.08 · brûlez 1.23–1.47 · votre 1.49 · budget 1.76–2.08 · sur 2.15 · des 2.29 · visiteurs 2.42–2.95 · dont 2.98 · vous 3.13 · ne 3.23 · savez 3.38 · rien 3.70–3.95 · et 4.12 · vous 4.19 · optimisez 4.38–5.02 · à 5.19 · l'aveugle 5.27–5.68 · Bon, 6.61–6.78 · ça, 6.95–7.10 · c'était 7.27–7.53 · avant 7.61–7.83

Scene 1 (0.00–1.05s): ENTRY — MK.enterBig(stage, 0, {from:1.45, frames:40}). Spend card (avant-panel 980×460, radius 28, centre x=820 y=520): « Budget publicitaire · ce mois » (Lufga 500 34 px avant-mute), counter « 8 240 € » (DM Sans 700 150 px avant-ink, tabular-nums), a thin sparkline at the bottom. Kinetic « Résultat : » (Lufga 700 72 px avant-ink, letters from 0.25) above the card's left edge (y≈190).
Scene 2 (1.08–2.15s): « vous brûlez votre budget » — MK.snapZoom(rig, 1.08, {from:1, to:1.3, origin: the counter}); MK.count(1.23 → 8 240 → 24 960 €, dur 0.75, penultimate 24 950, holdFrames 10) — final value on its own frame ≈ 2.15. Embers: 24 particles (6–10 px circles, #E0763A at 70 %) rise from the card's bottom edge (y −200…−420, x ±40 from MK.hash, fade out, 0.8–1.2 s, 2-frame offsets) from 1.23; the bottom edge glows warm (inset orange shadow 0 → 0.8 over 1.23–1.6).
Scene 3 (2.15–3.95s): « sur des visiteurs dont vous ne savez rien » — MK.pan(rig, 2.15, {x:-760, scale:1, frames:22, blur}) to the profile card (avant-panel 620×580): it swings in (rotationY 35° → 0, back.out(1.4), 30 frames from 2.30). Grey silhouette avatar 120 px + « Visiteuse anonyme »; rows « Âge » « Type de peau » « Besoin » « Frein », each ending with a grey « ? » pill that pops (MK.pop over .25) with 4-frame offsets from 2.98. « rien » (3.70): MK.anticipate the avatar (to 0.7) then MK.pop at 3.70; all « ? » pills tremble ±6 px (3 legs).
Scene 4 (4.12–5.10s): « et vous optimisez » — the campaign settings card (avant-panel 900×520, « Réglages campagne », sliders « Âge ciblé », « Centres d'intérêt », « Budget / jour », toggles « Lookalike », « Retargeting ») is launched up in front: MK.enter(settings, 4.05, {dir:"up", dist:900, frames:30, blur}). The touch pokes at random: slider 1 knob +140 then −60 (4.38–4.62), toggle 1 MK.click at 4.62 (snap 0.06), slider 2 −120 (4.75–4.90), toggle 2 MK.click at 4.95.
Scene 5 (5.10–6.55s): « à l'aveugle » + silence — at 5.10 (5 frames before « à ») the stage goes blind: CSS blur 0 → 18 px and brightness 1 → 0.55 (power2.in 0.45 s), a dark vignette closes in from the edges (opacity 0 → 0.8), the rig keeps pushing in (+6 % then +3 % slower until 6.55). Still alive: drift continues.
Scene 6 (6.55–6.99s): « Bon, » — the whole blind stage is sucked into a card: scale 1 → 0.42 (power2.in, 18 frames from 6.55) while its corners round to 28 px and a 2 px rgba(255,255,255,0.14) border + avant-phone shadow appear; the avant grid behind is sharp again. Lock 8 frames, card tilts −2°.
Scene 7 (6.99–7.72s): « ça, c'était avant » — EXIT. MK.toss(card, 6.99, {rise:90, fall:1500, rotation:-16, fallFrames:26}) → fall ends 7.72; vertical SVG blur ramp 0 → 20 px over the last 8 frames. Last frame = fastest.

## Frame 5 — Ask-it

- scene: The light world opens; the ask-it lockup builds letter by letter; an anonymous visitor becomes Claire, a client, and bursts into data; three step pills slam; the camera dives into « 01 ».
- duration: 5.83s (global 27.62–33.45)
- world: ASK-IT
- entry: oversized entry that brakes — the light grid rushes in at ×1.4 while the brand mesh blooms
- exit: zoom-through into pill 01 (expo.in, ~×9)
- status: outline
- voiceover: "Ask-it transforme vos visiteurs anonymes en clients… et en data. En trois étapes."
- src: compositions/f05-askit.html
- blueprint: compose
- rules: MK.enterBig, MK.ring, MK.pop, MK.words, MK.pan, MK.enter, MK.type, MK.anticipate, MK.fly, MK.suck, MK.slam, MK.zoomThrough
- focal: the lockup, then the avatar morph, then the step pills
- roles: lockup = Ask-it · grey silhouette → Claire photo = anonymous visitor becomes a client · chips = data · PILLS_ROW = the 3 steps
- assets: assets/askit/askit-logo-mark.svg · assets/askit/askit-logo-lockup-dark-on-transparent.png (reference for the lockup look only) · assets/personas/claire.webp · assets/fonts/Lufga-*.woff2 · assets/fonts/DMSans-normal-latin.woff2
- sfx: orchestrator

Voice cues (local s): (avant ends 0.11) · Ask 0.74–0.93 · It 0.98–1.11 · transforme 1.21–1.68 · vos 1.77 · visiteurs 1.93–2.36 · anonymes 2.40–2.95 · en 3.00 · clients 3.17–3.55 · et 3.72 · en 3.83 · data 3.96–4.29 · en 4.46 · trois 4.61–4.81 · étapes 4.87–5.21

Scene 1 (0.00–0.40s): ENTRY — grid-bg; MK.enterBig(stage, 0, {from:1.4, frames:40}); brand mesh blooms (opacity 0.3 → 1, scale 0.7 → 1, power2.out 0.8 s); MK.ring at the centre (r1 1100, coral, alpha 0.3, 30 frames).
Scene 2 (0.40–1.25s): « Ask-it » — the lockup builds at the centre: the mark (askit-logo-mark.svg, 150 px) MK.pop at 0.42; the wordmark « ask-it.ai » (as in askit-logo-lockup-dark-on-transparent.png: « ask-it » Lufga 600 170 px ink, « .ai » Lufga 400 ink, tracking −0.03em) builds letter by letter with 4-frame offsets from 0.52 (each letter y 60 → 0, scaleY .2 → 1, colour pale coral → ink in 5 frames), complete on « It » (0.98). Lock 14 frames.
Scene 3 (1.25–2.95s): « transforme vos visiteurs anonymes » — overlap: the lockup flies up to y=150 and scales 0.45 (24 frames power3.inOut from 1.25); at its speed peak (≈1.45) the visitor avatar is launched up into place (MK.enter dir up, 600 px, 30 frames): grey silhouette in a 220 px circle (white 6 px ring) at x=640 y=560 with a « ? » (Lufga 700 90 px ink-mute) and the visitor-tag pill under it whose text types « Visiteuse anonyme » (MK.type 60 cps from 2.40).
Scene 4 (3.04–3.70s): « clients » — MK.anticipate the avatar (to 0.6, from 3.04), at 3.17 the content swaps instantly to Claire's photo, MK.pop(from 0.6, over .22) + MK.ring (coral, r1 260); the tag text becomes « Claire » (tl.set) and a green « Cliente » badge (good, bag icon) pops 4 frames later.
Scene 5 (3.83–4.45s): « et en data » — MK.anticipate the avatar (to 0.85, before 3.96); at 3.96 four data chips burst out of her (MK.fly from the avatar centre into a 2×2 cluster on the right, x 1000–1600, y 470–640; 22 frames, arc −80, 4-frame offsets; data-hf-motion-blur): « 35 ans », « Peau mixte », « Teint terne », « Routine essentielle » (white pills 64 px, coral dot, Lufga 500 30 px ink).
Scene 6 (4.30–5.25s): « en trois étapes » — MK.suck(avatar + chips + lockup, 4.30) (18 frames to 0.55 + fade); the three pills of PILLS_ROW SLAM (MK.slam from 3.0, 9 frames, shake 12 px, data-hf-motion-blur): starts 4.46 / 4.56 / 4.66 → impacts 4.61 / 4.71 / 4.81. Lock 14 frames; at 5.25 pill 01 turns active (coral-tint fill + coral border, instant) with a component pulse.
Scene 7 (5.53–5.83s): EXIT — MK.zoomThrough(rig, 5.53, {origin:"430px 540px", to:9, frames:18, blur}); last frame = fastest.

## Frame 6 — Le diagnostic

- scene: Macro on the real Endro diagnostic: the skin swaps Endro → Les Petits Prodiges → Endro on whip pans, the name is typed, then three questions are answered in rhythm and each answer flies as a chip into Claire's profile card.
- duration: 9.25s (global 33.45–42.70)
- world: ASK-IT
- entry: oversized entry that brakes (the phone emerges from the pill dive at ×1.45)
- exit: whip left — the whole stage accelerates out to the left
- status: outline
- voiceover: "D'abord, le diagnostic. Intégré à votre site, à votre image. Il pose à chaque visiteuse les bonnes questions : ses besoins, sa routine, ses habitudes."
- src: compositions/f06-diagnostic.html
- blueprint: compose
- rules: MK.enterBig, MK.pop, MK.pan, MK.type, MK.click, MK.fly, MK.enter, MK.exit, MK.blurFilter
- focal: the phone screen (macro), then the chips landing in the profile card
- roles: phone = the Endro diagnostic · brand badge = the client's brand · profile card = what Ask-it learns · chips = answers
- assets: assets/screens/endro-diag/00-intro.png · assets/screens/lpp-diag/00-intro-mobile.png · assets/screens/endro-diag/01-prenom.png · assets/screens/endro-diag/04-claire-actuellement-comment-se-comporte-votre-pe.png · assets/screens/endro-diag/04-claire-actuellement-comment-se-comporte-votre-pe-choix.png · assets/screens/endro-diag/12-claire-quel-type-de-routine-recherchez-vous.png · assets/screens/endro-diag/12-claire-quel-type-de-routine-recherchez-vous-choix.png · assets/screens/endro-diag/05-claire-votre-peau-est-elle-sensible.png · assets/screens/endro-diag/05-claire-votre-peau-est-elle-sensible-choix.png · assets/endro/logo-noir.png · assets/lpp/logo-lpp.png · assets/personas/claire.webp · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): D'abord, 0.20–0.63 · le 0.80 · diagnostic. 0.94–1.60 · Intégré 1.94–2.30 · à 2.33 · votre 2.39 · site, 2.75–3.01 · à 3.18 · votre 3.26 · image. 3.48–3.90 · Il 4.24 · pose 4.41–4.58 · à 4.65 · chaque 4.79 · visiteuse 5.01–5.56 · les 5.62 · bonnes 5.81 · questions, 6.05–6.50 · ses 6.67 · besoins, 6.82–7.26 · sa 7.43 · routine, 7.58–8.07 · ses 8.24 · habitudes. 8.39–8.98

Geometry: PHONE_MACRO centred x=700 inside a 3D wrapper (perspective 2200 px, rotateY drifting −6° → +4° over the scene). Profile card (frame.md profile-card, 560 px wide) on the right, x 1220–1780, y 170–620. STEP_CHIP « 01 Diagnostic ».

Scene 1 (0.00–1.90s): ENTRY — MK.enterBig(rig, 0, {from:1.45, frames:40}); screen = 00-intro.png (Nuancier, full colour). STEP_CHIP pops at 0.20. « D'abord, le diagnostic » — the camera glides down the Nuancier (rig y −220, 1.2 s sine.inOut); a white shimmer band sweeps diagonally across the screen at 0.94–1.40.
Scene 2 (1.94–3.95s): « Intégré à votre site, à votre image » — whip A: MK.pan(rig, 1.98, {x:+240, frames:16, blur}); at its speed peak (2.11) the screen swaps INSTANTLY to lpp-diag/00-intro-mobile.png and the brand badge (white pill outside the screen's top-right: logo 34 px tall) swaps Endro → Les Petits Prodiges (MK.pop). Whip B: MK.pan(rig, 2.80, {x:-240, frames:16, blur}); at 2.93 back to Endro (screen + badge). « image » (3.48): MK.anticipate the badge (to 0.6) then MK.pop + MK.ring (coral).
Scene 3 (4.24–6.60s): « Il pose à chaque visiteuse les bonnes questions » — the profile card is launched in from the right (MK.enter dir left, 700 px, 38 frames from 4.24) with a 3D swing (rotationY 28° → 0, back.out(1.4)): Claire photo 96 px, « Claire », « Profil Endro », empty chip row, progress « Profil complété » 0 %. 4.41: the camera snaps down to the first-name field (rig y to frame the field + CTA, snap S-curve); the field overlay types « Claire » (MK.type 30 cps, 4.45 → 4.65) then the screen becomes 01-prenom.png (identical, tl.set). CLICK at 5.01 on « COMMENCER MON DIAGNOSTIC » (MK.click, snap 0.12) → screen swaps instantly to 04-…-pe.png (question + skin photos) as the camera snaps back up to frame the question and the three photos. 5.62–6.50: slow travel across the photos (rig x −80) while the touch moves to « PEAU MIXTE/NORMALE ».
Scene 4 (6.82–7.40s): « ses besoins » — CLICK at 6.82 on that photo → 04-…-choix.png (instant). Chip « Peau mixte » flies from the tap point into the card's chip row: MK.fly(chip, 6.84, {dx, dy computed from the tap point, arc:-160, frames:28}) → lands 7.31; on landing the progress bar steps 0 → 33 % (10 frames) and the card pulses.
Scene 5 (7.43–8.15s): « sa routine » — whip (MK.pan rig y, 14 frames from 7.40); at its peak (7.52) the screen swaps to 12-…-vous.png; CLICK at 7.62 on « Essentielle » → 12-…-choix.png; chip « Routine essentielle » flies → lands ≈ 8.09; progress → 66 %.
Scene 6 (8.20–8.95s): « ses habitudes » — whip at 8.20; at its peak (8.30) the screen swaps to 05-…-sensible.png; the touch drags the slider knob 0 → 3/10 (8.40–8.58, overlay knob) then 05-…-choix.png (tl.set at 8.60); chip « Peau sensible · 3/10 » flies → lands ≈ 8.92; progress → 100 % with a check pop.
Scene 7 (8.95–9.25s): EXIT — MK.exit(rig, 8.95, {dir:"left", dist:1500, frames:18, blur}); last frame = fastest.

## Frame 7 — Le profil en 30 secondes

- scene: A 30-second timer slams and runs; Claire's complete profile arrives big with her CORAIL02 swatch; what she is looking for and what makes her hesitate pop as chips.
- duration: 4.70s (global 42.70–47.40)
- world: ASK-IT
- entry: launched LEFT (continues the whip) — the timer ring slides in from the right and brakes while « 30 s » slams
- exit: push left — the stage accelerates out to the left
- status: outline
- voiceover: "En trente secondes, vous savez qui elle est, ce qu'elle cherche… et ce qui la fait hésiter."
- src: compositions/f07-profil.html
- blueprint: compose
- rules: MK.enter, MK.slam, MK.suck, MK.enterBig, MK.anticipate, MK.pop, MK.ring, MK.pan, MK.snapZoom, MK.exit
- focal: « 30 s », then the profile card, then the two chips
- roles: timer = speed · profile card = who she is · CORAIL02 swatch = her profile · « Cherche » chip = what she wants · « Frein » chip = what makes her hesitate
- assets: assets/personas/claire.webp · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): En 0.07 · trente 0.22–0.41 · secondes, 0.48–0.88 · vous 1.05 · savez 1.20 · qui 1.56 · elle 1.75 · est, 1.90–2.01 · ce 2.18 · qu'elle 2.29 · cherche 2.54–2.90 · et 3.07 · ce 3.31 · qui 3.45 · la 3.56 · fait 3.71 · hésiter 3.86–4.35

Scene 1 (0.00–1.00s): ENTRY — a timer ring (coral 12 px stroke, 380 px diameter, track rgba(36,31,32,.08)) centred (960, 520), launched left: MK.enter(ring, 0, {dir:"left", dist:1100, frames:30, blur}). « 30 s » slams inside it: MK.slam(timerText, 0.07, {shakeEl}) → impact 0.22 (« 30 » DM Sans 700 220 px ink, « s » coral 120 px, data-hf-motion-blur). The ring stroke fills 0 → 100 % from 0.22 to 0.88 (power1.inOut). Lock 10 frames.
Scene 2 (1.00–2.10s): « vous savez qui elle est » — MK.suck(timer, 1.00); the profile card arrives big: MK.enterBig(card, 1.30, {from:1.45, frames:40}). Card (white, 1000×560, centre 960/520, radius 28): Claire photo 180 px (white ring) left; « Claire » (Lufga 600 64 px), « Profil CORAIL02 » (Lufga 600 34 px coral); the three chips from frame 6 (« Peau mixte », « Routine essentielle », « Peau sensible · 3/10 ») and « Profil complété 100 % ». The CORAIL02 swatch (200 px circle #DF764C, « CORAIL02 » Archivo 800 30 px white) overlapping the card's right edge: MK.anticipate (to 0.6) then MK.pop at 1.56 + MK.ring (coral).
Scene 3 (2.18–2.95s): « ce qu'elle cherche » — MK.pan(rig, 2.36, {x:-120, y:-60, scale:1.08, frames:20}); chip « Cherche · un teint lumineux » (coral-tint fill, coral text Lufga 600 30 px, 72 px tall) pops at 2.54 under the card, linked by a connector line drawing from the card (stroke-dashoffset, 10 frames).
Scene 4 (3.07–4.40s): « et ce qui la fait hésiter » — MK.snapZoom(rig, 3.62, {from:1.08, to:1.3, origin: the new chip}); chip « Frein · peur des réactions » (amber tint #FFF3E0, amber « ! » dot #E8A23B, Lufga 600 30 px ink) pops at 3.71; the « ! » pulses ×1.4 twice from 3.86 (0.25 s each).
Scene 5 (4.40–4.70s): EXIT — MK.exit(rig, 4.40, {dir:"left", dist:1600, frames:18, blur}); last frame = fastest.

## Frame 8 — La recommandation

- scene: Flight over Claire's real result page on a tilted plane that straightens onto CORAIL02; « 100 % » slams; three different profile pages fan out (each visitor has her own); her routine bursts out of the page as cards with a running total; reassurance badges pop; everything is sucked away.
- duration: 6.80s (global 47.40–54.20)
- world: ASK-IT
- entry: launched LEFT on a tilted plane (rotateX 58°, rotateZ −12°)
- exit: SUCTION — the whole stage shrinks to 55 % accelerating (Trellis « Stop » prelude to frame 9's slam)
- status: outline
- voiceover: "Ensuite, sa page de recommandation, cent pourcent personnalisée : sa routine sur mesure, et les arguments qui la rassurent."
- src: compositions/f08-recommandation.html
- blueprint: compose
- rules: MK.enter, MK.pop, MK.slam, MK.suck, MK.snapZoom, MK.anticipate, MK.fly, MK.count, MK.blurFilter
- focal: the result page, « 100 % », the routine cards and the total
- roles: page = Claire's own recommendation page · OCÉAN01 / AMBRE02 pages = other visitors get other pages · routine cards = her routine · total pill = basket · badges = reassurance
- assets: assets/screens/endro-diag/17-resultat-full.png (780×18528) · assets/screens/endro-diag/17-resultat.png · assets/endro/diag/ocean.webp · assets/endro/diag/ambre.webp · assets/endro/products/gelee-nettoyante.jpg · assets/endro/products/gommage-visage-eclat.jpg · assets/endro/products/serum-bonne-mine.jpg · assets/endro/products/creme-bonne-mine.jpg · assets/endro/diag/meilleur-pharma-2026.png · assets/fonts/* (Archivo for the rebuilt Endro headers)
- sfx: orchestrator

Voice cues (local s): Ensuite, 0.22–0.65 · sa 0.82 · page 0.99 · de 1.24 · recommandation 1.33–2.09 · 100 % 2.26–2.88 · personnalisée, 2.90–3.59 · sa 3.77 · routine 3.90–4.29 · sur 4.37 · mesure 4.56–5.03 · et 5.20 · les 5.27 · arguments 5.46–5.86 · qui 5.90 · la 6.01 · rassurent. 6.12–6.61

Scene 1 (0.00–1.05s): ENTRY — the page (17-resultat-full.png in a rounded 40 px container, shadow) on a plane rotateX 58°, rotateZ −12°, scale 1.3, perspective 2200 px, launched left: MK.enter(plane, 0, {dir:"left", dist:1000, frames:38, blur}); the page scrolls continuously (−1400 source px over 0–1.05 s) — flying over her routine. STEP_CHIP « 02 Recommandation » pops at 0.22.
Scene 2 (1.05–2.05s): « page de recommandation » — the plane straightens (rotateX → 0, rotateZ → 0, scale → 1, 30 frames power3.inOut from 1.05) while the page scrolls back to its top: lands at 1.55 on the CORAIL02 header in macro (page at 1:1, centred x=700). Drift.
Scene 3 (2.03–2.90s): « 100 % » — the page goes out of focus 5 frames before the impact (blur 0 → 10 px from 2.03); MK.slam(stat100, 2.11, {shakeEl}) → impact 2.26 (« 100 » DM Sans 700 280 px ink + « % » coral, centred x=1220 y=520, data-hf-motion-blur).
Scene 4 (2.85–3.70s): « personnalisée » — MK.suck(stat100, 2.85); the page refocuses (2.95) and the rig pulls back (MK.snapZoom to 0.7, start 2.92): two other result pages slide out from behind hers (4-frame offsets, 22 frames expo.out from 3.00) — left « OCÉAN01 » (ocean.webp header, 220 px circle #2C4A6E, « VOTRE PROFIL OCÉAN01 » Archivo 800 white) at x≈520 rotationY 18°, right « AMBRE02 » (ambre.webp, circle #B8732E) at x≈1400 rotationY −18°, both behind and smaller (0.85). Hers stays in front, centred.
Scene 5 (3.70–5.10s): « sa routine sur mesure » — the side pages fly out left/right (14 frames expo.in from 3.70); MK.snapZoom back to 1.0 on her page (3.75); the page scrolls to the routine section (20 frames power3.inOut from 3.80); MK.anticipate the page (to 0.94) then at 3.90 four routine cards burst out of it into a 2×2 grid on the right (MK.fly, 26 frames, 4-frame offsets, data-hf-motion-blur): card 300×380 white, packshot 220 px, « Étape 1 · Nettoyer » / « Étape 2 · Exfolier » / « Étape 3 · Traiter » / « Étape 4 · Hydrater » (Lufga 600 26 px) with gelee-nettoyante, gommage-visage-eclat, serum-bonne-mine, creme-bonne-mine (names only — NO per-card prices). Total pill « Total routine » under the grid: MK.count 0 → 72,50 € (from 4.40, dur 0.5, penultimate 72,40, holdFrames 10) — final on « mesure » ≈ 5.07.
Scene 6 (5.20–6.50s): « et les arguments qui la rassurent » — reassurance badges pop around the cluster (MK.pop, 4-frame offsets from 5.46, drift ×1.4): « ★ 4,7/5 · 3 158 avis », « Validé par un dermatologue » (check icon), the Meilleur produit pharma 2026 seal (image, 150 px), « Comme 6 % des Endroïstes ». At 6.12 (« rassurent ») all of them pulse together (+4 %).
Scene 7 (6.50–6.80s): EXIT — MK.suck(rig, 6.50, {to:0.55, frames:18}) with fade; last frame = smallest & fastest.

## Frame 9 — Les chiffres

- scene: « À la clé » — « ×4 » slams with a 1-vs-4 bar; the basket fills with products and « +36 % » slams.
- duration: 5.25s (global 54.20–59.45)
- world: ASK-IT
- entry: oversized entry — « À la clé » arrives at ×1.4 and brakes (right after frame 8's suction)
- exit: push left
- status: outline
- voiceover: "À la clé : quatre fois plus de conversions en moyenne… et des paniers trente-six pourcent plus élevés."
- src: compositions/f09-chiffres.html
- blueprint: compose
- rules: MK.enterBig, MK.words, MK.pop, MK.slam, MK.suck, MK.toss, MK.exit
- focal: « ×4 », then « +36 % »
- roles: ×4 = conversions · bars = 1 vs 4 · cart + falling packshots = bigger baskets · +36 % = basket size
- assets: assets/endro/products/serum-bonne-mine.jpg · assets/endro/products/creme-bonne-mine.jpg · assets/endro/products/gelee-nettoyante.jpg · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): À 0.15 · la 0.23 · clé, 0.36–0.55 · quatre 0.72–0.93 · fois 1.08–1.27 · plus 1.30 · de 1.51 · conversions 1.64–2.13 · en 2.17 · moyenne 2.29–2.74 · et 2.91 · des 3.00 · paniers 3.13–3.44 · 36 % 3.61–4.32 · plus 4.36 · élevés 4.57–4.87

Scene 1 (0.00–0.57s): ENTRY — MK.enterBig(stage, 0, {from:1.4, frames:40}); a key badge (coral circle 90 px, white key glyph SVG) pops at 0.0 (MK.pop over .25) and « À la clé : » builds beside it (MK.words, lead 0.15, Lufga 600 84 px ink-soft, y≈250).
Scene 2 (0.57–2.80s): « quatre fois plus de conversions en moyenne » — MK.slam(x4, 0.57, {shakeEl}) → impact 0.72 (« ×4 », DM Sans 700 340 px, « × » coral, centre x=720 y=580, data-hf-motion-blur). Kinetic words right of it (x from 1100): « plus de » neutral (Lufga 500 64 px ink-soft), « conversions » accent (Lufga 700 76 px coral, letters from 1.64), « en moyenne » neutral (Lufga 500 44 px ink-mute) at 2.29. A mini bar chart under the words: « Sans » (grey bar, 60 px) and « Avec Ask-it » (coral bar, 240 px) — the coral bar grows from 1.64 with overshoot (scaleY 0 → 1.08 → 1).
Scene 3 (2.91–3.55s): « et des paniers » — MK.suck(x4 group, 2.95); at 3.13 a cart icon (SVG, ink, 200 px, x=620 y=600) pops and three mini packshots (90 px rounded) drop into it with gravity (1-frame offsets from 3.14, accelerating fall from y −500, squash on landing).
Scene 4 (3.46–4.95s): « 36 % plus élevés » — MK.slam(p36, 3.46, {shakeEl}) → impact 3.61 (« +36 % », DM Sans 700 300 px, « + » and « % » coral, centre x=1260 y=540, data-hf-motion-blur). « plus élevés » accent (Lufga 700 64 px ink) under it from 4.36; a coral up-arrow grows with overshoot at 4.57 and the cart squashes once (scaleY 0.9 → 1).
Scene 5 (4.95–5.25s): EXIT — MK.exit(rig, 4.95, {dir:"left", dist:1600, frames:18, blur}); last frame = fastest.

## Frame 10 — Le dashboard

- scene: The Ask-it dashboard flies in on a tilted plane and lands; an Excel sheet slams, crumples and is tossed away; the camera snaps onto the revenue card where 78 343 € counts with restraint.
- duration: 6.50s (global 59.45–65.95)
- world: ASK-IT
- entry: launched LEFT on a tilted plane (rotateX 62°, rotateZ −12°)
- exit: the camera scrolls DOWN the dashboard — content accelerates UP out of frame
- status: outline
- voiceover: "Et enfin, votre dashboard. Adieu le tableau Excel. Ask-it vous dit combien ça vous rapporte…"
- src: compositions/f10-dashboard.html
- blueprint: compose
- rules: MK.enter, MK.pop, MK.slam, MK.anticipate, MK.toss, MK.snapZoom, MK.count, MK.ring, MK.exit
- focal: the dashboard, the Excel sheet, then the revenue counter
- roles: browser-window = app.ask-it.ai · Excel sheet = the old way · revenue card = « combien ça vous rapporte »
- assets: assets/askit/askit-logo-mark.svg · assets/personas/claire.webp · assets/personas/julie.webp · assets/personas/ines.webp · assets/fonts/* · REUSE the v3 dashboard markup, CSS and data from compositions/f07-dashboard.html (browser window, dark sidebar, « Espace Endro », KPI tiles, revenue card with coral area chart, personas, funnel, Aski) so frames 10 and 11 show the same product
- sfx: orchestrator

Voice cues (local s): Et 0.16 · enfin, 0.28–0.60 · votre 0.77 · dashboard. 1.07–1.65 · Adieu 1.99–2.33 · le 2.37 · tableau 2.54 · Excel. 2.86–3.32 · Ask 3.66 · It 3.90 · vous 4.09 · dit 4.22 · combien 4.39–4.75 · ça 4.81 · vous 4.92 · rapporte, 5.05–5.54 · qui 5.71 · sont 5.92 · vos 6.15 · meilleurs 6.34–

Scene 1 (0.00–1.30s): ENTRY — the browser window (1640×960, URL pill « app.ask-it.ai ») on a plane rotateX 62°, rotateZ −12°, scale 1.25, perspective 2200 px, launched left: MK.enter(plane, 0, {dir:"left", dist:1000, frames:38, blur}). STEP_CHIP « 03 Dashboard » pops at 0.17. « votre dashboard »: the plane straightens (rotateX 62 → 4°, rotateZ → 0, scale → 0.92, 30 frames power3.inOut from 0.80), landing ≈ 1.30 on the top of the dashboard (sidebar, « Espace Endro », KPI tiles, revenue card).
Scene 2 (1.84–3.60s): « Adieu le tableau Excel » — the dashboard blurs 6 px from 1.90; an Excel-like sheet (green header #1D6F42 with « Excel », 10×14 grey cell grid with numbers, 900×600, rotated 4°, centre x=1180 y=560) SLAMS: MK.slam(sheet, 1.84, {from:3, shakeEl, shakePx:14}) → impact 1.99. « Excel » (2.86): crumple anticipation (8 frames before: scale 0.55, rotation −12°, scaleY 0.5, radius 60 px) then MK.toss(sheet, 2.86, {rise:90, fall:1400, rotation:-40, fallFrames:24, x:300}); the dashboard refocuses (6 → 0 px, 12 frames from 2.95).
Scene 3 (3.55–5.70s): « Ask-it vous dit combien ça vous rapporte » — MK.snapZoom(rig, 3.55, {from:1, to:1.75, origin: the revenue card}); MK.count(3.95, 0 → 78 343 €, dur 0.95, penultimate 78 290, holdFrames 10) — final ≈ 5.07 on « rapporte »: the number pulses (+4 %), a coin icon pops, MK.ring (coral). The coral area chart draws under the counter 4.00–4.90 (stroke-dashoffset + area fade) and its tooltip « Record · 8 250 € » pops at 4.95. Lock 10 frames, then drift.
Scene 4 (6.20–6.50s): EXIT — MK.exit(rig, 6.20, {dir:"up", dist:1400, frames:18, blur}); last frame = fastest.

## Frame 11 — Personas, tunnel, publicité

- scene: Scrolling down the dashboard: best personas with Claire on top, the diagnostic funnel with a slammed friction alert, then Aski types the next ad campaign which is switched on with a click.
- duration: 4.30s (global 65.95–70.25)
- world: ASK-IT
- entry: launched UP (continues frame 10's scroll) — the personas card rises and brakes
- exit: push left
- status: outline
- voiceover: "…qui sont vos meilleurs personas… où votre tunnel bloque… et quelle publicité lancer ensuite."
- src: compositions/f11-insights.html
- blueprint: compose
- rules: MK.enter, MK.ring, MK.snapZoom, MK.pan, MK.slam, MK.type, MK.pop, MK.click, MK.exit
- focal: Claire's persona row, the friction alert, the campaign toggle
- roles: persona rows = « meilleurs personas » · funnel + alert = « où votre tunnel bloque » · Aski + campaign card = « quelle publicité lancer »
- assets: assets/personas/claire.webp · assets/personas/julie.webp · assets/personas/ines.webp · assets/askit/askit-logo-mark.svg · assets/fonts/* · REUSE the v3 dashboard markup, CSS and data from compositions/f07-dashboard.html (same look as frame 10)
- sfx: orchestrator

Voice cues (local s): (meilleurs −0.16–0.16) · personas, 0.19–0.67 · où 0.84 · votre 0.97 · tunnel 1.25–1.55 · bloque 1.61–1.89 · et 2.06 · quelle 2.25 · publicité 2.50–3.04 · lancer 3.08–3.38 · ensuite 3.44–3.89

Scene 1 (0.00–0.80s): ENTRY — the « Vos meilleurs personas » card (1300×520, macro) launched up: MK.enter(card, 0, {dir:"up", dist:900, frames:38, blur}). Rows (avatar 96 px, name, descriptor, share bar, revenue): Claire « Teint terne · peau mixte » 36 % · 28 203 €; Julie « Peau sèche » 24 % · 18 802 €; Inès « Peau sensible » 19 % · 14 885 €. Bars grow (scaleX 0 → 1.04 → 1) with 4-frame offsets from 0.05. « personas » (0.19): Claire's row turns coral-tint, MK.ring around her avatar, rig snaps +10 % toward her row (MK.snapZoom start 0.12).
Scene 2 (0.80–2.00s): « où votre tunnel bloque » — MK.pan(rig, 0.80, {y:-700, frames:20, blur, axis:"y"}) to « Parcours du diagnostic »: 4 bars « Commencés 11 395 », « Arrivées au contact 10 617 », « Terminés 9 705 », « Achats 1 347 » grow (scaleY with overshoot, 4-frame offsets from 1.00). MK.slam(alert, 1.46, {from:2.2, shakeEl, shakePx:10}) → impact 1.61: dark pill « Frein détecté : l'écran de contact » above the drop between bars 1 and 2, coral dot pulsing; the drop zone gets a coral hatched highlight.
Scene 3 (2.06–3.40s): « et quelle publicité lancer » — the Aski panel is launched in from the right (MK.enter dir left, 800 px, 30 frames from 2.06): blue gradient orb 40 px « Aski », ai-tint bubble typing (MK.type 70 cps from 2.25) « Lancez une campagne Meta sur l'audience « Teint terne · 30–44 ans » »; the campaign card « Campagne · Teint terne » with an OFF toggle pops at 3.10.
Scene 4 (3.44–4.00s): « ensuite » — MK.click on the toggle at 3.44 (rig snap 0.15, shake, dashes, touch) → instant state: toggle ON (good green), « Campagne activée ✓ ». Lock 14 frames, drift.
Scene 5 (4.00–4.30s): EXIT — MK.exit(rig, 4.00, {dir:"left", dist:1600, frames:18, blur}); last frame = fastest.

## Frame 12 — Zéro effort

- scene: « Le mieux ? » — « presque rien à faire »; a form fills itself at high speed and is sent; the Ask-it team checklist ticks itself; then order notifications drop in with gravity.
- duration: 7.15s (global 70.25–77.40)
- world: ASK-IT
- entry: launched LEFT — « Le mieux ? » slides in from the right and brakes
- exit: everything accelerates UP
- status: outline
- voiceover: "Le mieux ? Vous n'avez presque rien à faire. Un formulaire… et notre équipe s'occupe du reste. Et vous ? Vous profitez."
- src: compositions/f12-zero-effort.html
- blueprint: compose
- rules: MK.enter, MK.words, MK.exit, MK.type, MK.pop, MK.click, MK.blurFilter
- focal: the kinetic words, the form, the checklist, the notifications
- roles: form = « un formulaire » · checklist = « notre équipe s'occupe du reste » · notifications = « vous profitez »
- assets: assets/askit/askit-logo-mark.svg · assets/endro/logo-noir.png · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): Le 0.17 · mieux ? 0.30–0.89 · Vous 0.93 · n'avez 1.02 · presque 1.34–1.70 · rien 1.74–1.91 · à 1.96 · faire. 2.10–2.40 · Un 2.74 · formulaire 2.89–3.47 · et 3.64 · notre 3.72 · équipe 3.94–4.19 · s'occupe 4.25 · du 4.59 · reste. 4.70–5.02 · Et 5.40 · vous, 5.51–5.64 · vous 5.81 · profitez 6.02–6.61

Scene 1 (0.00–0.95s): ENTRY — the text container is launched left (MK.enter dir left, 900 px, 38 frames, blur): « Le » neutral (Lufga 500 150 px ink-soft, from 0.07) + « mieux ? » accent (Lufga 700 150 px coral, letters from 0.30), centred y=480.
Scene 2 (0.95–2.65s): « presque rien à faire » — overlap: « Le mieux ? » flies up and shrinks (y −260, scale 0.55, 20 frames from 0.95) as the second line builds: « presque rien » accent (Lufga 700 120 px ink, letters from 1.34; « rien » coral) + « à faire. » neutral (Lufga 500 120 px ink-soft) from 2.00. 2.40–2.65: the text block exits up (14 frames expo.in).
Scene 3 (2.55–3.60s): « Un formulaire » — the form card is launched up (MK.enter dir up, 900 px, 30 frames from 2.55): 900×560, centre x=760, « Lancez votre diagnostic » (h3) and three fields filled at high speed: « Endro » (MK.type 60 cps from 2.80), « endro-cosmetiques.com » (90 cps from 2.92), chip « Plus de conversions » pops at 3.20; the touch reaches « Envoyer → » (3.25–3.40) and clicks at 3.47 (MK.click, snap 0.15) → instant: the button turns good-green « Demande envoyée ✓ ».
Scene 4 (3.55–5.05s): « et notre équipe s'occupe du reste » — the checklist panel (560×520, x≈1420) is launched in from the right (MK.enter dir left, 700 px, 30 frames from 3.55): « L'équipe Ask-it s'en occupe »; three initials avatars pop with 1-frame offsets at 3.72; four rows tick (spinner → green check MK.pop) at 3.94 / 4.19 / 4.45 / 4.70: « Catalogue importé », « Diagnostic construit », « Page de résultat générée », « Installé sur votre site ».
Scene 5 (5.10–6.85s): « Et vous ? Vous profitez. » — 5 frames before the first drop the form + checklist go out of focus (blur 8 px, scale 0.94 from 5.10); three order notifications (white 640×104, radius 22, small Endro logo, « Nouvelle commande » Lufga 600 30 px, amount DM Sans 700 34 px, « à l'instant » ink-mute) drop from above with gravity (power2.in fall 16 frames, squash scaleY 0.9 for 3 frames, settle 8 frames) and stack at y=300 / 420 / 540 (centre x=960), landing at 5.55 / 5.80 / 6.05: « 72,50 € », « 58,00 € », « 91,30 € ». Drift after.
Scene 6 (6.85–7.15s): EXIT — MK.exit(rig, 6.85, {dir:"up", dist:1400, frames:18, blur}); last frame = fastest.

## Frame 13 — Elle revient

- scene: Back on the Endro serums page — in full colour. The Ask-it pill invites her; she taps it, answers in a flash with a whip between every answer, gets her CORAIL02 routine and adds it to her basket.
- duration: 11.10s (global 77.40–88.50)
- world: ASK-IT
- entry: launched UP (continues frame 12's exit) — the phone and its page rise and brake
- exit: zoom-through into the basket icon
- status: outline
- voiceover: "Tiens… c'est quoi, ça ? Un diagnostic personnalisé ? Alors moi… c'est ça… hop… et ça. Oh, c'est exactement ce qu'il me fallait ! Allez, au panier."
- src: compositions/f13-elle-revient.html
- blueprint: compose
- rules: MK.enter, MK.pop, MK.snapZoom, MK.click, MK.type, MK.pan, MK.ring, MK.anticipate, MK.fly, MK.zoomThrough, MK.blurFilter
- focal: the phone screen in macro
- roles: phone = Endro site then diagnostic · entry pill = the Ask-it widget · visitor-tag « Claire » (photo) = her, now known · basket icon = conversion
- assets: assets/screens/endro-shop/collection-serums.png · assets/screens/endro-diag/00-intro.png · assets/screens/endro-diag/04-claire-actuellement-comment-se-comporte-votre-pe.png · assets/screens/endro-diag/04-claire-actuellement-comment-se-comporte-votre-pe-choix.png · assets/screens/endro-diag/05-claire-votre-peau-est-elle-sensible.png · assets/screens/endro-diag/05-claire-votre-peau-est-elle-sensible-choix.png · assets/screens/endro-diag/07-claire-quelles-sont-vos-pre-occupations-pour-vot.png · assets/screens/endro-diag/07-claire-quelles-sont-vos-pre-occupations-pour-vot-choix.png · assets/screens/endro-diag/16-chargement.png · assets/screens/endro-diag/17-resultat.png · assets/endro/products/serum-bonne-mine.jpg · assets/personas/claire.webp · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): Tiens, 0.20–0.53 · c'est 0.86 · quoi 1.04 · ça ? 1.31–1.48 · Un 1.95 · diagnostic 2.09–2.59 · personnalisé ? 2.65–3.27 · Alors 3.81–4.11 · moi, 4.20–4.42 · c'est 4.70 · ça. 5.12–5.51 · Hop. 5.78–6.17 · Et 6.50 · ça. 6.81–7.08 · Oh, 7.55–7.75 · c'est 7.88 · exactement 8.15–8.85 · ce 8.89 · qu'il 8.95 · me 9.10 · fallait. 9.26–9.49 · Allez, 9.88–10.04 · au 10.27 · panier 10.39–10.64

Geometry: PHONE_MACRO centred x=760, full colour; visitor-tag « Claire » (photo 52 px + « Claire » Lufga 600 30 px) right of the phone (x≈1300); a floating basket icon (SVG bag 110 px, ink, white circle 160 px, shadow) appears top-right of the frame (x≈1560, y≈200) at 9.95.

Scene 1 (0.00–1.50s): ENTRY — MK.enter(phone, 0, {dir:"up", dist:900, frames:38, blur}) while the page scrolls 400 → 900 source px (expo.out 1.0 s). Tag pops at 0.15. « Tiens… c'est quoi, ça ? » — the Ask-it entry pill (HTML inside the screen: white pill 640×96 at screen-bottom, coral dot, « Trouvez votre routine en 30 s → » Lufga 600 30 px ink, shadow) slides up 200 px with MK.pop overshoot at 0.30; MK.snapZoom(rig, 0.86, {from:1, to:1.3, origin: the pill}); a « ? » bubble pops on the tag at 1.31.
Scene 2 (1.95–3.70s): « Un diagnostic personnalisé ? » — the touch travels to the pill (2.30–2.62); CLICK at 2.65 (MK.click, snap 0.12) → instant: screen = 00-intro.png, pill gone; the camera snaps to the name field; « Claire » typed (MK.type 30 cps from 2.95).
Scene 3 (3.81–7.20s): « Alors moi… c'est ça… hop… et ça. » — rapid fire, every answer is a click with 4 responses + MK.ring (coral, r1 60), every new screen arrives on the speed peak of a whip (MK.pan 14 frames with blur, screen swap by tl.set at its peak): CLICK 4.70 « COMMENCER MON DIAGNOSTIC » → 04-…-pe.png · CLICK 5.12 on « PEAU MIXTE/NORMALE » → 04-…-choix.png · whip 5.40 → 05-…-sensible.png · « Hop » 5.78–5.98 slider drag (overlay knob 0 → 30 %) → 05-…-choix.png · whip 6.30 → 07-…-vot.png · CLICK 6.81 on a concern → 07-…-choix.png.
Scene 4 (7.10–9.50s): « Oh, c'est exactement ce qu'il me fallait ! » — whip at 7.10 → 16-chargement.png at its peak; a coral selection square hops across 4 swatches (instant moves every 4 frames, 7.20–7.45) and lands on CORAIL. MK.anticipate the screen content (to 0.92, before 7.55); at 7.55 the screen becomes 17-resultat.png with MK.pop (over .12); 6 small four-point sparkles pop around the phone (1-frame offsets) and twinkle. Camera: MK.pan to the CORAIL02 chips (y, 20 frames from 7.90), then to the bottom bar « TOTAL DE LA ROUTINE 72,50 € / AJOUTER AU PANIER » (24 frames from 8.60) → arrives ≈ 9.00; at « fallait » (9.26) the total pulses (+6 %).
Scene 5 (9.88–10.80s): « Allez, au panier » — basket icon pops (top-right) at 9.95; the touch reaches the button (9.88–10.30); CLICK at 10.39 (MK.click, snap 0.2, shake 8) → instant: the button overlay turns good-green « Ajoutée ✓ »; a packshot (serum-bonne-mine, 120 px rounded) flies into the basket icon (MK.fly 18 frames, arc −200, data-hf-motion-blur) → lands 10.72: badge « 4 » pops on the icon (MK.pop) + MK.ring.
Scene 6 (10.80–11.10s): EXIT — MK.zoomThrough(rig, 10.80, {origin: the basket icon centre, to:9, frames:18, blur}); last frame = fastest.

## Frame 14 — Elle est restée

- scene: Claire arrives big — she stayed; the camera snaps back and she becomes one dot of the 100-visitor grid; 70 dots light up coral as « 70 % » slams; the ask-it lockup builds and the « Réserver une démo » pill is clicked; calm living end frame.
- duration: 9.50s (global 88.50–98.00)
- world: ASK-IT
- entry: oversized entry that brakes (out of the basket dive)
- exit: none — final scene: ends on a calm, still-drifting end card (no fade to black)
- status: outline
- voiceover: "Cette fois… elle est restée. Ne laissez plus partir soixante-dix pour cent de vos visiteurs. Réservez votre démo avec Ask-it."
- src: compositions/f14-fin.html
- blueprint: compose
- rules: MK.enterBig, MK.anticipate, MK.pop, MK.ring, MK.snapZoom, MK.pan, MK.slam, MK.words, MK.suck, MK.click, MK.drift
- focal: Claire, then the coral grid + « 70 % », then the CTA pill
- roles: Claire avatar = she stayed · GRID_100 (light: dots ink 15 %) = callback to frame 2 · coral dots = visitors you keep · lockup = Ask-it · pill-cta = « Réserver une démo »
- assets: assets/personas/claire.webp · assets/askit/askit-logo-mark.svg · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): Cette 0.29 · fois, 0.56–0.82 · elle 0.99 · est 1.12 · restée 1.24–1.71 · Ne 2.32 · laissez 2.43 · plus 2.75 · partir 2.94–3.28 · soixante-dix 3.34–3.83 · pour 3.86 · cent 4.05–4.17 · de 4.19 · vos 4.26 · visiteurs. 4.39–5.00 · Réservez 5.34–5.69 · votre 5.73 · démo 6.00–6.36 · avec 6.43 · Ask 6.81–7.02 · It 7.07–7.24

Scene 1 (0.00–2.25s): ENTRY — Claire's avatar (260 px, white 8 px ring, green check badge 64 px) at (960, 500): MK.enterBig(avatar group, 0, {from:1.5, frames:40}); brand-mesh glow behind. « Cette fois… elle est restée » — slow push (rig 1 → 1.06); MK.anticipate (to 0.75, before 1.24) then MK.pop at 1.24 + MK.ring (coral, r1 300) + coral radial glow 0.2 → 0.6. Lock 14 frames, drift.
Scene 2 (2.30–3.30s): « Ne laissez plus partir » — MK.snapZoom(rig, 2.30, {from:1.06, to:0.2, origin: the avatar}): she becomes one dot of GRID_100 (lay the grid out in rig space around her so that at rig 0.2 it reads as GRID_100 dots, 40 px, ink 15 %, her dot = r3,c5 in coral with a white ring); then MK.pan so that the grid sits at x=600 and the right half is free (≈2.75–3.10).
Scene 3 (3.19–5.00s): « soixante-dix pour cent de vos visiteurs » — MK.slam(stat70, 3.19, {shakeEl}) → impact 3.34 (« 70 % » DM Sans 700 300 px coral, centre x=1340 y=500, data-hf-motion-blur); from 3.34, 69 more dots light up coral in a cascade spreading from her dot (1-frame offsets, MK.pop over .25 each, ink 15 % → coral); « de vos visiteurs » (MK.words, Lufga 500 56 px ink-soft, under the stat) from 4.19.
Scene 4 (5.00–6.40s): « Réservez votre démo » — MK.suck(grid + stat + words, 5.00); the lockup builds at the centre (y≈420): mark MK.pop at 5.32, « ask-it.ai » letters with 4-frame offsets (« ask-it » Lufga 600 150 px ink, « .ai » Lufga 400) complete by 5.75; the pill-cta « Réserver une démo → » (ink pill 120 px tall, Lufga 600 44 px white) pops at 5.95 (MK.pop over .2) at y≈640.
Scene 5 (6.30–7.40s): « avec Ask-it » — an arrow cursor (ink, 56 px) glides in from the bottom-right (power2.inOut 0.4 s from 6.30); MK.click at 6.81 (component: the pill, shake 6 px, coral dashes, rig snap 0.05) → instant: the pill turns coral; « ask-it.ai » (label, ink-mute) pops under it at 6.95.
Scene 6 (7.40–9.50s): END CARD — no exit: drift only (rig scale +2 % over 2.1 s, mesh drifting); the last 0.5 s keep a very slow drift (never frozen, no fade to black).
