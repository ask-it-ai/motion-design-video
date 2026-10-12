---
format: 1920x1080
duration: 105.5s
message: "Ask-it transforme vos visiteurs anonymes en clients… et en data."
arc: Hook (visiteuse perdue) → Problème (70 %, budget, à l'aveugle) → Bascule → Diagnostic → Recommandation → Dashboard → Zéro effort → Elle revient → CTA
audience: fondateurs et responsables e-commerce de marques beauté / DNVB françaises
mode: autonomous
fps: 30
voice: assets/audio/vo.wav (Martin Dupont narrateur + Victoria visiteuse) — word timings in assets/audio/vo_timeline.json
---

Shared layout constants (PHONE, PHONE_HERO, PHONE_AVANT, PILLS_ROW, GRID_100) and backgrounds live in frame.md → `layout`. All times inside a frame block are LOCAL to that frame.

## Frame 1 — Hésitation

- scene: In the dark AVANT world a phone shows the Endro serums page; an anonymous visitor scrolls, taps one serum, then another, gets overwhelmed and closes the tab.
- duration: 12.39s
- transition_in: cut
- status: outline
- voiceover: "Hmm… c'est lequel pour ma peau ? Celui-là ?… Ah non. Celui-là ! Ah bah non, pas lui non plus… Oh là là… y a vraiment trop de choix. Bon. Je verrai plus tard."
- src: compositions/f01-hesitation.html
- blueprint: device-surface-showcase (Adapt)
- rules: cursor-click-ripple, depth-of-field-blur, center-outward-expansion
- focal: the phone screen (Endro serums collection page)
- roles: phone = hero device · touch indicator = the visitor's thumb · visitor-tag = « Visiteuse anonyme » · floating packshots = overwhelm
- assets: assets/screens/endro-shop/collection-serums.png (780×9978, 2x full page) · assets/endro/products/*.jpg (packshots for the overwhelm) · assets/fonts/Lufga-*.woff2
- sfx: orchestrator

Voice cues (local s): Hmm 0.55 · lequel 1.53 · peau 2.39 · Celui-là? 3.21 · Ah non 4.11 · Celui-là! 4.91 · Ah bah non 5.91 · plus 7.01 · Oh là là 7.91 · trop de choix 9.17–9.53 · Bon 10.41 · plus tard 11.19–11.35.

Scene 1 (0.0–1.4s): AVANT background (avant-bg + grid + vignette). PHONE_AVANT rises in from y+60 with blur 12px → 0 (expo.out 0.9 s) and a slow continuous drift (scale 0.9 → 0.93 over the frame). Screen = collection-serums.png at scroll 0, filtered grayscale(0.6) brightness(0.9). The touch indicator fades in on the screen at 0.55 s with the visitor-tag (grey silhouette avatar + « Visiteuse anonyme ») hanging 70 px to its right, outside the phone.
Scene 2 (1.4–3.1s): the thumb drags up: the page scrolls from 0 to 300 px (screen px) with a smooth power2.inOut ease, landing so the 2nd product row (Sérum Bonne Mine / Sérum Anti-Taches) is mid-screen.
Scene 3 (3.21–4.4s): cursor-click-ripple tap on the top-left product tile of the visible row (« Celui-là ? »): the tile gets a 3 px white highlight ring that pops in (back.out). At 4.11 (« Ah non ») the ring shakes (x ±6 px, 3 cycles) and fades.
Scene 4 (4.91–7.2s): tap on the neighbour tile (« Celui-là ! »), same ring; at 5.91–7.01 (« pas lui non plus ») it fades and the page scrolls another 280 px.
Scene 5 (7.91–10.3s): « trop de choix »: the camera pulls back (scene wrapper scale 1 → 0.86) and 10–12 Endro packshots (assets/endro/products/*.jpg, 150–220 px squares, radius 14, grayscale(0.6)) burst outward from behind the phone with center-outward-expansion, settling at mixed depths around it; the ones farther away get depth-of-field-blur (6–12 px) so the phone stays the sharp focal point. A slight wobble keeps them alive.
Scene 6 (10.41–12.39s): « Bon… je verrai plus tard »: the packshots drift back and dim to 35 %; at 11.35 the phone screen performs an iOS « close tab » move — the page card shrinks to 0.82 and slides up out of the screen (power3.in 0.45 s) leaving a plain dark grey screen; the visitor-tag fades out at 11.6. Final frame: dark stage, empty dark phone (this is the hard cut into frame 2).

## Frame 2 — Elle ne reviendra pas

- scene: A grid of 100 visitors; 70 fade away while « 70 % » counts up in coral; then the same Endro page multiplied into identical phones, each visitor with a « ? » above them.
- duration: 10.61s
- transition_in: cut
- status: outline
- voiceover: "Non. Elle ne reviendra pas. Comme soixante-dix pour cent de vos visiteurs. Le problème, ce n'est pas votre trafic. Sur votre site, tout le monde voit la même chose… et personne n'est là pour guider."
- src: compositions/f02-soixante-dix.html
- blueprint: dataviz-countup (Adapt)
- rules: counting-dynamic-scale, spring-pop-entrance
- focal: the « 70 % » number, then the wall of identical phones
- roles: GRID_100 dots = visitors · « 70 % » = the stat (DM Sans 260 px, % sign coral) · phone wall = identical site for everyone
- assets: assets/screens/endro-shop/collection-serums.png · assets/fonts/DMSans-normal-latin.woff2 · assets/fonts/Lufga-*.woff2
- sfx: orchestrator

Voice cues (local s): Non 0.12 · reviendra pas 0.73–1.19 · comme 1.54 · 70 % 1.91–2.29 · visiteurs 2.62 · Le problème 3.78–3.89 · votre trafic 4.94–5.23 · Sur votre site 6.11–6.59 · même chose 7.77–7.98 · personne 8.72 · guider 9.80.

Scene 1 (0.0–1.4s): AVANT background. GRID_100 appears at once on the cut (all dots avant-ink at 80 %), the dot at row 4/col 5 has a thin ring (« her ») — on « Non » (0.12) her dot dims to 15 % with a small downward drop (y +8).
Scene 2 (1.54–3.4s): « comme 70 % »: 69 more dots fade to 12 % in a fast pseudo-random cascade (index-derived order, 1.2 s total) while on the right (left edge x=980, baseline y=600) the stat counts 0 → 70 with counting-dynamic-scale, landing exactly at 2.29; the « % » sign in coral; a label under it « ne reviennent jamais » (Lufga 500 34 px, avant-mute).
Scene 3 (3.78–5.6s): « Le problème, ce n'est pas votre trafic »: the grid and stat slide left and blur (exit is not needed: replace by a camera move — the whole world wrapper pans left 700 px, power3.inOut 0.9 s) revealing a traffic line chart card (avant-panel, radius 22) whose line draws upward with a small label « Trafic » and a green tick that spring-pops at 5.23 (traffic is fine).
Scene 4 (6.11–8.4s): « tout le monde voit la même chose »: a wall of 12 identical phones (4×3, each 0.34 scale, screens = collection-serums.png grayscale) assembles with spring-pop-entrance (stagger 0.04 s, ≤ 0.5 s) filling the frame; every phone shows exactly the same scroll position; a tiny grey visitor avatar sits on the top-right corner of each.
Scene 5 (8.51–10.61s): « et personne n'est là pour guider »: a small « ? » bubble (avant-panel pill, 44 px) pops above each phone one after the other (stagger 0.06 s); nothing answers. Slow push-in on the wall (scale 1 → 1.05). Hold.

## Frame 3 — Le budget brûle

- scene: An ad-spend counter burns upward while the visitor profile card stays full of question marks, then the whole dashboard blurs out: optimizing blind.
- duration: 6.85s
- transition_in: crossfade
- status: outline
- voiceover: "Résultat : vous brûlez votre budget sur des visiteurs dont vous ne savez rien. Et vous optimisez… à l'aveugle."
- src: compositions/f03-budget.html
- blueprint: compose
- rules: counting-dynamic-scale, particle-burst, depth-of-field-blur
- focal: the ad-spend counter, then the blurred optimization panel
- roles: spend card = budget · profile card with « ? » = unknown visitor · optimization panel = blind decisions
- assets: assets/fonts/DMSans-normal-latin.woff2 · assets/fonts/Lufga-*.woff2
- sfx: orchestrator

Voice cues (local s): Résultat 0.61 · brûlez 1.67 · budget 2.20 · visiteurs 2.88 · rien 4.18 · optimisez 4.90 · à l'aveugle 5.76–5.83.

Scene 1 (0.0–1.6s): AVANT background. Centered-left, a spend card (avant-panel, 620×300, radius 22) titled « Budget publicitaire · ce mois » with a DM Sans 120 px counter starting at 8 240 €.
Scene 2 (1.67–3.2s): « vous brûlez votre budget »: the counter rolls fast 8 240 → 24 960 € (counting-dynamic-scale, digits slightly scaling up as they climb) and the card's bottom edge glows warm while ember particles rise from it (particle-burst, ≤ 30 particles, warm orange at 60 % opacity — the only warm color here).
Scene 3 (2.88–4.3s): « sur des visiteurs dont vous ne savez rien »: on the right a visitor profile card slides in (avant-panel, grey silhouette avatar, 4 rows « Âge ? », « Peau ? », « Besoin ? », « Frein ? » each ending with a grey « ? » pill) — the « ? » pills pop one by one on 2.88 / 3.3 / 3.7 / 4.1.
Scene 4 (4.9–6.85s): « et vous optimisez… à l'aveugle »: a third card (campaign settings: three sliders and two toggles) rises in the middle; at 5.76 the whole stage gets depth-of-field-blur ramping to 22 px and brightness to 0.6 while the camera pushes in (scale 1 → 1.08). The final frame is a dark, heavily blurred stage — frame 4 starts from that exact look.

## Frame 4 — C'était avant

- scene: The blurred dark stage rewinds, color floods from the center into the Ask-it world, the ask-it.ai logo assembles, an anonymous visitor turns into a client with data, and three step pills land.
- duration: 7.63s
- transition_in: cut
- status: outline
- voiceover: "Bon… ça, c'était avant. Ask-it transforme vos visiteurs anonymes en clients… et en data. En trois étapes."
- src: compositions/f04-bascule.html
- blueprint: compose
- rules: chromatic-glitch, ambient-glow-bloom, spring-pop-entrance, card-morph-anchor
- focal: the color flood, then the ask-it.ai logo, then the step pills
- roles: rewind glitch = « c'était avant » · color flood = switch of worlds · logo = brand · silhouette→Claire = visitor becomes client · chips = data · pills = the 3 steps
- assets: assets/askit/askit-logo-mark.svg · assets/personas/claire.webp · assets/fonts/Lufga-*.woff2 · assets/fonts/DMSans-normal-latin.woff2
- sfx: orchestrator

Voice cues (local s): Bon 0.17 · ça 0.54 · c'était 0.89 · avant 1.24 · Ask-it 2.15–2.40 · transforme 2.63 · visiteurs anonymes 3.36–3.84 · clients 4.63 · data 5.46 · trois étapes 6.14–6.41.

Scene 1 (0.0–1.2s): starts as a dark blurred stage (avant-bg + a blurred grey panel at 22 px blur, brightness 0.6, matching frame 3's end). At 0.17–0.9 a short « rewind » chromatic-glitch: horizontal slice bands jitter and the blurred panel scrubs backwards (x −40 px, then +60 px) twice.
Scene 2 (1.24–2.1s): « avant »: a circular color flood opens from the frame center (radius 0 → 1400 px, power3.inOut 0.7 s) revealing the Ask-it grid-bg (canvas + 44 px grid + brand-mesh); the grid lines draw outward from the center; ambient-glow-bloom of the coral/powder mesh behind center.
Scene 3 (2.15–3.0s): « Ask-it »: the ask-it.ai lockup assembles at center (mark SVG 120 px spring-pops, then the wordmark « ask-it.ai » in Lufga 600 120 px slides in from x −30 with a mask reveal). At 2.63 the lockup moves up to y=230 and scales to 0.7.
Scene 4 (3.36–5.9s): below the logo, left at x=560: a grey visitor silhouette in a 140 px circle with the visitor-tag « Visiteuse anonyme ». At 4.63 (« clients ») card-morph-anchor: the silhouette circle morphs into Claire's photo (assets/personas/claire.webp) with a white 6 px ring and a green « Cliente » badge with a bag icon. At 5.46 (« data ») four answer-chips (« 35 ans », « Peau mixte », « Teint terne », « Routine essentielle ») spring-pop out to her right in a 2×2 cluster (stagger 0.07 s).
Scene 5 (5.99–7.63s): « en trois étapes »: logo, avatar and chips scale down 0.9 and fade to 0 while the three step pills spring-pop into PILLS_ROW (stagger 0.08 s, back.out(1.6)) — « 01 Diagnostic », « 02 Recommandation », « 03 Dashboard » with coral number circles. Hold on PILLS_ROW with a slow drift (frame 5 starts from this exact layout).

## Frame 5 — Le diagnostic

- scene: Pill 01 activates and opens onto a phone running the real Endro diagnostic; the skin swaps Endro → Les Petits Prodiges → Endro; questions are answered and chips fly into Claire's profile card; the Nuancier narrows to CORAIL02.
- duration: 14.75s
- transition_in: cut
- status: outline
- voiceover: "D'abord, le diagnostic. Intégré à votre site, à votre image. Il pose à chaque visiteuse les bonnes questions : ses besoins, sa routine, ses habitudes. En trente secondes, vous savez qui elle est, ce qu'elle cherche… et ce qui la fait hésiter."
- src: compositions/f05-diagnostic.html
- blueprint: device-surface-showcase (Adapt)
- rules: theme-crossfade-morph, card-morph-anchor
- focal: the phone (PHONE_HERO), then the profile card on the right
- roles: phone = Endro diagnostic · skin swap = « à votre image » · answer-chips = needs/routine/habits · profile card = what you now know · 30 s ring = speed · CORAIL02 = the identified profile
- assets: assets/screens/endro-diag/00-intro.png · assets/screens/lpp-diag/00-intro-mobile.png · assets/screens/endro-diag/01-prenom.png · assets/screens/endro-diag/04-claire-actuellement-comment-se-comporte-votre-pe-choix.png · assets/screens/endro-diag/05-claire-votre-peau-est-elle-sensible-choix.png · assets/screens/endro-diag/12-claire-quel-type-de-routine-recherchez-vous-choix.png · assets/screens/endro-diag/16-chargement.png · assets/screens/endro-diag/17-resultat.png · assets/endro/logo-noir.png · assets/lpp/logo-lpp.png · assets/personas/claire.webp · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): D'abord 0.06 · diagnostic 0.84 · Intégré 1.91 · site 2.74 · image 3.51 · pose 4.55 · visiteuse 5.17 · questions 6.23 · besoins 7.04 · routine 7.84 · habitudes 8.69 · trente secondes 9.88–10.15 · qui elle est 11.28–11.62 · cherche 12.30 · hésiter 13.68.

Scene 1 (0.0–1.5s): starts on PILLS_ROW (identical to frame 4's end). At 0.06 pill 01 turns active (coral-tint fill, coral border), pills 02/03 fade to 30 %. At 0.84 the camera pushes into pill 01 (scale 1 → 2.6 centered on it, power3.inOut 0.7 s) and the PHONE_HERO rises into place out of it, screen = 00-intro.png (Endro Nuancier, full color). The Ask-it grid-bg stays behind.
Scene 2 (1.91–3.9s): « Intégré à votre site, à votre image »: theme-crossfade-morph on the phone screen with the phone frame as the fixed anchor: Endro 00-intro.png → LPP 00-intro-mobile.png at 2.3 → back to Endro at 3.2 (each swap 0.3 s crossfade). A brand label pill floats at the phone's top-right corner and swaps with the skin: Endro logo (logo-noir.png, 28 px tall) ↔ Les Petits Prodiges logo (logo-lpp.png).
Scene 3 (4.38–6.4s): « Il pose à chaque visiteuse les bonnes questions »: on the right (x 1020–1600) the profile card (frame.md profile-card) slides in from x+60 with blur 10 → 0: avatar = Claire, name « Claire », empty chip row, progress bar at 0 %. The phone screen cuts to 01-prenom.png (first name « Claire » typed) at 4.55, then to 04-…-choix.png (skin photos) at 5.6.
Scene 4 (6.89–9.2s): three taps in rhythm (touch indicator with ripple, as frame.md touch): at 6.89 on the selected skin photo → an answer-chip « Peau mixte » flies along an arc from the tap point into the profile card's chip row (card-morph-anchor style landing, 0.55 s); screen → 05-…-choix.png; at 7.68 tap → chip « Peau sensible 4/10 » (« sa routine » → screen 12-…-choix.png); at 8.54 tap → chip « Routine essentielle ». The profile progress bar steps 0 → 35 → 70 → 100 %.
Scene 5 (9.73–11.7s): « En trente secondes »: a small timer badge (ring 64 px, coral stroke) next to the card fills its ring and shows « 30 s » at 10.15. At 10.76 the phone shows 16-chargement.png (Nuancier « nous identifions votre profil »); over it an HTML overlay of the 36 swatches is not needed — instead dim the screenshot to 50 % except a coral highlight square that lands on the CORAIL swatch at 11.28. The profile card gains the line « Profil CORAIL02 » (coral) at 11.62.
Scene 6 (11.94–14.75s): « ce qu'elle cherche » → chip « Préoccupation : teint terne » pops in coral-tint at 12.30; « ce qui la fait hésiter » → chip « Frein : peur des réactions » pops at 13.52 with a small amber « ! » dot. At 13.9 the phone screen crossfades to 17-resultat.png (CORAIL02 header, scroll 0). Hold: PHONE_HERO showing the CORAIL02 header — frame 6 starts from this exact state (profile card may stay on the right).

## Frame 6 — La recommandation

- scene: The real CORAIL02 result page scrolls; a second phone shows a different profile (≠); the routine products fly out as step cards with a running total; reassurance badges pop; then ×4 and +36 % land big.
- duration: 12.36s
- transition_in: cut
- status: outline
- voiceover: "Ensuite, sa page de recommandation, cent pour cent personnalisée : sa routine sur mesure, et les arguments qui la rassurent. À la clé : quatre fois plus de conversions en moyenne… et des paniers trente-six pour cent plus élevés."
- src: compositions/f06-recommandation.html
- blueprint: video-text-pivot (Adapt)
- rules: split-tilt-cards, spring-pop-entrance, counting-dynamic-scale
- focal: the result page, then the step cards, then the two stats
- roles: phone = Claire's page · second phone = another visitor's page (OCÉAN01) · step cards = routine · badges = reassurance · ×4 / +36 % = proof
- assets: assets/screens/endro-diag/17-resultat.png · assets/screens/endro-diag/17-resultat-full.png (780×18528) · assets/endro/diag/ocean.webp · assets/endro/products/gelee-nettoyante.jpg · assets/endro/products/gommage-visage-eclat.jpg · assets/endro/products/serum-bonne-mine.jpg · assets/endro/products/serum-hydratant.jpg · assets/endro/products/creme-bonne-mine.jpg · assets/endro/products/masque-creme.jpg · assets/endro/diag/meilleur-pharma-2026.png · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): Ensuite 0.10 · recommandation 1.24 · 100 % 2.17–2.60 · personnalisée 2.73 · routine 3.82 · sur mesure 4.28–4.47 · arguments 5.42 · rassurent 6.13 · À la clé 7.03–7.25 · quatre fois 7.66–8.00 · conversions 8.54 · moyenne 9.14 · paniers 10.05 · 36 % 10.53–11.10 · élevés 11.40.

Scene 1 (0.0–1.9s): starts exactly as frame 5 ended (PHONE_HERO with 17-resultat.png). A small step-pill « 02 Recommandation » (active) drops in at top-left (x=120, y=90). At 0.72–1.9 the page scrolls (use 17-resultat-full.png) from 0 to the « Étape 1 : Nettoyer » routine list (≈ source y 1700 → screen scroll ≈ 960 px), power2.inOut.
Scene 2 (2.17–3.6s): « cent pour cent personnalisée »: split-tilt-cards — a second phone slides in from the right (x=1240) showing a rebuilt HTML result header in the Endro style: full-bleed ocean texture (ocean.webp), a 220 px circle in #2C4A6E with « OCÉAN01 » (Archivo 800), title « VOTRE PROFIL OCÉAN01 » (Archivo 800 uppercase white), two chips « Type de peau : Sèche » « Préoccupation : Sécheresse », and below three blue product thumbnails (gelee-nettoyante, serum-hydratant, masque-creme). Both phones tilt toward each other (±8° rotationY); a coral « ≠ » sign (DM Sans 120 px) spring-pops between them at 2.73. At 3.5 the second phone slides back out to the right and the first phone recenters.
Scene 3 (3.68–6.3s): « sa routine sur mesure »: four step cards (card component, 260×330, product packshot on top, « Étape 1 · Nettoyer » / « Étape 2 · Exfolier » / « Étape 3 · Traiter » / « Étape 4 · Hydrater », product name, price) spring-pop out of the phone into an arc on the right (stagger 0.08 s) using gelee-nettoyante 10,90 €, gommage-visage-eclat 14,90 €, serum-bonne-mine 16,90 €, creme-bonne-mine 16,90 €; a total pill « Total routine 72,50 € » counts up under them. At 5.15–6.13 reassurance badges pop around (white pills): « ★ 4,7/5 · 3 158 avis », « Validé par un dermatologue », « Vous êtes comme 6 % des endroïstes », plus the Meilleur Produit Pharma 2026 seal image (90 px).
Scene 4 (7.03–12.36s): « À la clé »: video-text-pivot — the phone + cards slide aside (left, scale 0.8, depth-of-field blur 8 px) to hand the center to the stats: « ×4 » (stat-xl, × in coral) lands with counting-dynamic-scale 1 → 4 at 7.66–8.0, label « de conversions en moyenne » (h3, ink-soft) at 8.54; then « +36 % » (stat-xl, + and % in coral) counts 0 → 36 landing at 11.10, label « de panier moyen » at 11.4. Layout: the two stats side by side centered (x 560 and 1300, baseline y 560). Hold to the end.

## Frame 7 — Le dashboard

- scene: An Excel sheet crumples away; the Ask-it dashboard (Endro space) opens: revenue counter and coral chart, persona rows with Claire on top, the diagnostic funnel with the detected friction, and Aski proposing the next ad campaign which gets activated.
- duration: 11.23s
- transition_in: push
- status: outline
- voiceover: "Et enfin, votre dashboard. Adieu le tableau Excel. Ask-it vous dit combien ça vous rapporte… qui sont vos meilleurs personas… où votre tunnel bloque… et quelle publicité lancer ensuite."
- src: compositions/f07-dashboard.html
- blueprint: camera-journey (Adapt)
- rules: counting-dynamic-scale, svg-path-draw, stat-bars-and-fills
- focal: each dashboard panel in turn (revenue → personas → funnel → Aski campaign)
- roles: Excel grid = the old way · browser-window = app.ask-it.ai · revenue card = « combien ça vous rapporte » · persona rows = « meilleurs personas » · funnel = « où votre tunnel bloque » · Aski + campaign card = « quelle publicité lancer »
- assets: assets/personas/claire.webp · assets/personas/julie.webp · assets/personas/ines.webp · assets/endro/products/serum-bonne-mine.jpg · assets/endro/products/creme-bonne-mine.jpg · assets/endro/products/gelee-nettoyante.jpg · assets/askit/askit-logo-mark.svg · assets/fonts/* · the dashboard is rebuilt in HTML from frame.md tokens (white cards, 14 px radius, coral #F8571F accent, Lufga text, DM Sans digits)
- sfx: orchestrator

Voice cues (local s): Et enfin 0.05–0.17 · dashboard 1.00 · Adieu 2.00 · Excel 2.89 · Ask-it 3.75 · combien 4.50 · rapporte 5.17 · personas 6.87 · tunnel 7.97 · bloque 8.34 · publicité 9.27 · lancer 9.87 · ensuite 10.23.

Scene 1 (0.0–1.9s): Ask-it grid-bg. A step-pill « 03 Dashboard » (active) at top-left (x=120, y=90). A browser-window (1500×860, center x=960 y=560, URL pill « app.ask-it.ai ») rises in with blur 10 → 0 by 1.0. Inside: a left sidebar (dark #161616, 220 px: ask-it.ai mark + menu « Accueil · Questionnaire · Persona · Revenu · Conversion · Aski Chat ») and the content area titled « Espace Endro » (Lufga 600 34 px) with the sub-label « 30 derniers jours » (label, ink-mute).
Scene 2 (2.0–3.6s): « Adieu le tableau Excel »: in front of the window an Excel-like sheet (green header bar #1D6F42, grey cell grid 9×14, a few numbers) slams in at 2.0 (scale 1.15 → 1, 0.25 s), then at 2.89 crumples away: scale 1 → 0.15, rotation −28°, x +700, y −250, blur 0 → 8 px, power3.in 0.55 s.
Scene 3 (3.75–5.6s): camera-journey leg 1: the camera dives onto the revenue card (top-left of content): « Chiffre d'affaires généré par le diagnostic » (label 26 px) and the counter 0 → 78 343 € (DM Sans 120 px, counting-dynamic-scale) landing at 5.17, with a coral area chart drawing underneath (svg-path-draw, 30 days, a peak tooltip « Record · 8 250 € »).
Scene 4 (5.87–7.3s): leg 2: camera travels right to « Vos meilleurs personas »: three persona rows (avatar 72 px with white ring, name, descriptor, share bar, revenue): Claire « Teint terne · peau mixte » 36 % · 28 203 €; Julie « Peau sèche » 24 % · 18 802 €; Inès « Peau sensible » 19 % · 14 885 €. Rows slide in with stagger 0.08 s; Claire's row gets a coral-tint highlight at 6.87 (she is our visitor).
Scene 5 (7.55–8.7s): leg 3: camera down to « Parcours du diagnostic »: four funnel bars grow (stat-bars-and-fills, scaleY) « Commencés 11 395 » « Arrivées au contact 10 617 » « Terminés 9 705 » « Achats 1 347 »; at 8.34 a dark pill « Frein détecté : l'écran de contact » pops above the drop between bars 1 and 2 with a pulsing coral dot.
Scene 6 (8.83–11.23s): leg 4 / landing: an Aski chat panel slides in from the right edge of the window (ai-tint bubble with a 40 px blue gradient orb avatar « Aski »): the message types in (« Lancez une campagne Meta sur l'audience Teint terne · 30–44 ans ») by 9.9; under it a campaign card « Campagne · Teint terne » with a toggle; at 10.23 the toggle flips on and the card shows « Campagne activée » in good-green with a check. Hold.

## Frame 8 — Zéro effort

- scene: A three-field onboarding form fills itself and is sent; the Ask-it team checklist completes on its own; then order notifications stack up while « vous profitez ».
- duration: 7.41s
- transition_in: blur
- status: outline
- voiceover: "Le mieux ? Vous n'avez presque rien à faire. Un formulaire… et notre équipe s'occupe du reste. Et vous ? Vous profitez."
- src: compositions/f08-zero-effort.html
- blueprint: agent-progress-theater (Adapt)
- rules: discrete-text-sequence, physics-press-reaction, spring-pop-entrance
- focal: the form card, then the checklist, then the notifications
- roles: form = « un formulaire » · checklist = « notre équipe s'occupe du reste » · notifications = « vous profitez »
- assets: assets/askit/askit-logo-mark.svg · assets/endro/logo-noir.png · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): Le mieux 0.10–0.23 · presque rien 1.09–1.49 · faire 1.86 · Un formulaire 2.59–2.74 · équipe 3.84 · reste 4.61 · Et vous 5.33–5.44 · profitez 5.99.

Scene 1 (0.0–2.5s): Ask-it grid-bg. A form card (card component, 760×520, center x=760) « Lancez votre diagnostic » (h3) with three fields that fill via discrete-text-sequence typing: « Nom de la boutique » → « Endro » (0.6–1.0), « Site » → « endro-cosmetiques.com » (1.0–1.7), « Objectif » → a selected chip « Plus de conversions » (1.86).
Scene 2 (2.59–3.5s): « Un formulaire »: the dark pill button « Envoyer → » gets a physics-press-reaction click (cursor arrow lands on it) at 2.74 and turns good-green « Demande envoyée ✓ ».
Scene 3 (3.54–5.1s): « notre équipe s'occupe du reste »: to the right (x 1220–1700) a checklist panel « L'équipe Ask-it s'en occupe » with 4 rows that tick one by one (spinner → green check, 0.25 s apart): « Catalogue importé », « Diagnostic construit », « Page de résultat générée », « Installé sur votre site ». Small initials avatars (« AR », « BL », « PC ») sit next to the panel title.
Scene 4 (5.33–7.41s): « Et vous ? Vous profitez »: the form and checklist dim and drift back (scale 0.94, blur 6 px) while three order notifications spring-pop down from the top center, stacking (white rounded cards 560×96, Endro logo icon, « Nouvelle commande » + amounts « 72,50 € », « 58,00 € », « 91,30 € »), at 5.5 / 5.8 / 6.1. Light, playful bounce.

## Frame 9 — Elle revient

- scene: The same visitor is back on the Endro page, now in full color; an Ask-it entry pill invites her; she taps it, answers three questions in a flash, gets her CORAIL02 routine and adds it to the cart.
- duration: 11.61s
- transition_in: push
- status: outline
- voiceover: "Tiens… c'est quoi, ça ? Un diagnostic personnalisé ? Alors moi… c'est ça… hop… et ça. Oh, c'est exactement ce qu'il me fallait ! Allez, au panier."
- src: compositions/f09-elle-revient.html
- blueprint: device-surface-showcase (Adapt)
- rules: cursor-click-ripple, physics-press-reaction
- focal: the phone (PHONE_HERO) in full color
- roles: phone = Endro site + diagnostic · entry pill = Ask-it widget · visitor-tag = « Claire » with photo · cart = conversion
- assets: assets/screens/endro-shop/collection-serums.png · assets/screens/endro-diag/00-intro.png · assets/screens/endro-diag/04-claire-actuellement-comment-se-comporte-votre-pe-choix.png · assets/screens/endro-diag/05-claire-votre-peau-est-elle-sensible-choix.png · assets/screens/endro-diag/07-claire-quelles-sont-vos-pre-occupations-pour-vot-choix.png · assets/screens/endro-diag/16-chargement.png · assets/screens/endro-diag/17-resultat-full.png · assets/personas/claire.webp · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): Tiens 0.07 · c'est quoi ça 0.75–1.21 · Un diagnostic personnalisé 1.87–2.59 · Alors moi 3.79–4.19 · c'est ça 4.75–5.19 · Hop 5.87 · Et ça 6.61–6.93 · Oh 7.69 · exactement 8.31 · fallait 9.45 · Allez 10.09 · au panier 10.49–10.61.

Scene 1 (0.0–1.8s): Ask-it grid-bg; PHONE_HERO in full color showing collection-serums.png at scroll ≈ 300 px. The visitor-tag now reads « Claire » with her photo. At 0.4 an Ask-it entry pill slides up inside the screen bottom (white pill, coral dot, « Trouvez votre routine en 30 s → », Lufga 500 22 px at phone scale) with a soft bounce.
Scene 2 (1.87–3.4s): the touch taps the pill (cursor-click-ripple) at 1.95; the screen pushes to 00-intro.png (Nuancier) by 2.4; first-name field shows « Claire ».
Scene 3 (3.79–7.2s): quick-fire answers, one tap per beat with the screen cutting on each tap: 4.75 tap on the skin photo (04-…-choix.png), 5.87 slider « hop » (05-…-choix.png, the touch drags right 60 px), 6.61 tap (07-…-choix.png). Each tap emits a tiny coral spark.
Scene 4 (7.69–9.9s): « Oh, c'est exactement ce qu'il me fallait »: 16-chargement.png flashes for 0.35 s, then 17-resultat-full.png appears at scroll 0 (CORAIL02 header) and scrolls to the « AJOUTER AU PANIER · 72.50 € » button area (≈ source y 1500) by 9.6; a few sparkles around the phone.
Scene 5 (10.09–11.61s): « Allez, au panier »: physics-press-reaction tap on the add-to-cart button at 10.49; an HTML overlay of the button turns good-green « Ajoutée ✓ »; a cart badge « 4 » spring-pops on the phone's top-right header icon; the visitor-tag gets a small green check. Hold.

## Frame 10 — Elle est restée

- scene: Claire's avatar joins the 100-visitor grid, which re-lights in coral; then the ask-it.ai lockup and the « Réserver une démo » CTA pill, clicked once, hold to the end.
- duration: 10.66s
- transition_in: blur
- status: outline
- voiceover: "Cette fois… elle est restée. Ne laissez plus partir soixante-dix pour cent de vos visiteurs. Réservez votre démo avec Ask-it."
- src: compositions/f10-fin.html
- blueprint: cta-morph-press (Adapt)
- rules: spring-pop-entrance, cursor-click-ripple, ambient-glow-bloom
- focal: the re-lit grid, then the CTA pill
- roles: GRID_100 = callback to frame 2, now kept · lockup = Ask-it · pill-cta = « Réserver une démo »
- assets: assets/askit/askit-logo-mark.svg · assets/personas/claire.webp · assets/fonts/*
- sfx: orchestrator

Voice cues (local s): Cette fois 0.16–0.43 · restée 1.15 · laissez 2.41 · partir 2.93 · soixante-dix 3.33 · visiteurs 4.41 · Réservez 5.47 · démo 6.14 · Ask-it 6.97–7.24.

Scene 1 (0.0–1.9s): Ask-it grid-bg with brand-mesh glow. Claire's avatar (100 px, white ring, small green check) sits at center; at 1.15 (« restée ») a soft ambient-glow-bloom behind her.
Scene 2 (2.29–4.6s): « Ne laissez plus partir 70 % »: the camera pulls back and her avatar shrinks into one dot of GRID_100 (same layout as frame 2, but on the light canvas: dots ink at 15 %); from 2.93 to 4.41, 70 dots light up coral in a fast index-derived cascade (spring-pop-entrance scale 0.6 → 1, stagger capped to fit 1.4 s); on the right « 70 % » (stat, coral) appears with label « restent » in ink-soft.
Scene 3 (5.47–7.6s): « Réservez votre démo avec Ask-it »: grid and stat fade to 0 and scale 0.95 (final frame: exits allowed) while the ask-it.ai lockup (mark + wordmark, Lufga 600 110 px) builds at center y=440, then at 6.14 the pill-cta « Réserver une démo → » spring-pops under it (y=600) with a small « ask-it.ai » (label) beneath.
Scene 4 (7.6–10.66s): cta-morph-press landing: an arrow cursor glides in and clicks the pill at 8.2 (press 0.95, ripple ring coral 0 → 1.6 opacity 0.5 → 0); hold; gentle brand-mesh drift; from 10.1 everything eases to a calm still frame (no fade to black).
