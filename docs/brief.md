# Vidéo motion design Ask-it : mémoire du projet

Ce fichier garde tout ce qu'il faut pour reprendre le projet d'une session à l'autre.

> ⚠️ Le repo est **public**. Ne jamais y mettre de clé API, de mot de passe, ni le lien de partage
> Frame.io. Les clés vivent dans les secrets de l'environnement (`ELEVENLABS_API_KEY`).

## Objectif

Refaire la vidéo de présentation d'Ask-it (explainer motion design, 16:9) en version finale, ultra qualitative :

- plus réaliste : un vrai site de marque cliente au lieu de la marque fictive « VELYNE » ;
- les trois étapes (diagnostic, page de recommandation, dashboard) montrées concrètement, avec de vrais exemples ;
- animations plus abouties, synchronisées sur la voix off ;
- ajout du sound design (bruitages) et d'une musique de fond. La v2 n'a aucune piste audio.

## État au 12/10/2026

| Élément | Détail |
|---|---|
| Vidéo actuelle | `Ask-it_video_presentation_v2 (1).mp4`, 1920×1080, 30 i/s, **87,2 s**, sans piste audio |
| Voix off actuelle | `ElevenLabs_2026-10-05T12_54_15_Martin Dupont…_v4.mp3`, mono, **114,4 s**, les deux voix (visiteuse + narrateur) |
| Écart | La vidéo est ~24 % trop courte sur toute sa longueur : +27 s cumulés à la fin |
| Fabrication de la v2 | Code HTML/GSAP rendu avec HyperFrames (CLI Apache-2.0), sur un Mac local. Les sources ne sont pas dans GitHub |
| Hébergement | Dossier de partage Frame.io (2 fichiers, commentaires et téléchargement activés). Lien : demander à Pierre |

Synchronisation voix ↔ image de la v2 (début de chaque section) :

| Section | Début voix | Début image | Décalage |
|---|---|---|---|
| A. Visiteuse hésite | 0,1 s | 0,0 s | 0 |
| B. Problème (70 %, trafic, budget, à l'aveugle) | 10,8 s | 8,5 s | +2,3 s |
| C. « Bon, ça, c'était avant » + logo + 3 étapes | 31,7 s | 24,0 s | +7,7 s |
| D. Diagnostic | 41,0 s | 30,5 s | +10,5 s |
| E. Page de recommandation + ×4 / +36 % | 58,0 s | 42,5 s | +15,5 s |
| F. Dashboard + « un formulaire » | 74,4 s | 55,5 s | +18,9 s |
| G. La visiteuse revient | 94,3 s | 71,5 s | +22,8 s |
| H. Outro + CTA | 105,6 s | 79,5 s | +26,1 s |

La voix off contient 41 silences de plus de 0,45 s, soit 23 s cumulés.

## Script (version de base, avec les tags ElevenLabs)

Visiteuse (Victoria) :
> [thoughtful] Hmm… c'est lequel pour ma peau ? Celui-là ? [short pause] Ah non… Celui-là ! [sighs] Ah bah non pas lui non plus… Oh la la... Y a vraiment trop de choix. Bon. [exhales sharply] Je verrai plus tard.

Narrateur :
> [serious] Non. Elle ne reviendra pas... Comme 70 % de vos visiteurs ! [clears throat] Soyons honnêtes. Le problème, c'est pas votre trafic. Sur votre site, tous vos visiteurs voient la même chose, et personne n'est là pour les guider. [annoyed] Résultat : vous brûlez votre budget sur un trafic dont vous ne savez rien. Et vous optimisez… à l'aveugle. [short pause] Bon, ça, c'était avant... [excited] Ask-it, c'est la solution qui transforme vos visiteurs anonymes en clients et en data, en trois petites étapes. D'abord, le diagnostic. Intégré à votre site, et à votre image. Il pose à chaque visiteuse les questions qui la concernent : problématiques, besoin, routine, habitudes. En trente secondes, vous savez qui elle est, ce qu'elle cherche, et ce qui la fait hésiter. Ensuite, sa page de recommandation. 100 % personnalisée, générée automatiquement après ses questions. Sa routine sur mesure et les arguments qui la rassurent. Résultat : quatre fois plus de conversions en moyenne, et des paniers 36 % plus élevés. Et enfin, votre dashboard. Adieu le tableau Excel : Ask-it vous dit combien ça vous rapporte, qui sont vos meilleurs personas, où votre tunnel bloque, et quelle publicité lancer ensuite. Le mieux ? Vous n'avez presque rien à faire. Un formulaire, et notre équipe s'occupe du reste. Et vous ? Bah vous profitez !

Visiteuse :
> [surprised] Tiens, c'est quoi ça ? Un diagnostic personnalisé… [thoughtful] Alors moi, c'est ça… hop, hop… [happy] Oh, c'est exactement ce qu'il me fallait. Allez, au panier !

Narrateur :
> [happy] Cette fois, elle est restée. Vous aussi, ne laissez plus partir 70 % de vos visiteurs. [excited] Réservez votre démo avec Ask-it !

Pierre aime ces tags d'expression, mais ils sont à réajuster pour sonner vraiment authentiques.

## Voix (ElevenLabs)

- Compte : offre Creator. Quota mensuel de 143 564 caractères, remis à zéro le 05/11/2026.
- Modèle : `eleven_v4` (le plus récent). Réglages disponibles : stabilité et similarité uniquement (pas de vitesse ni de style). Les pauses se gèrent par la ponctuation et les tags.
- Visiteuse : **Victoria – Content Creator** (`O31r762Gb3WFygrEOGh0`), choix validé par Pierre.
- Narrateur : Pierre veut une voix d'homme **posée, douce, grave, envoûtante**. Pas encore tranché :
  - actuel : Martin Dupont – Deep, Warm and Aged (`a5n9pJUnAhX4fn7lx3uo`) ;
  - déjà dans le compte : Paul K – Deep Engaging Storyteller (`MBIQRZjHPU6xEjGuB3b8`), François Louis – Deep, Warm and Poised (`UBXZKOKbt62aLQHhc1Jm`) ;
  - bibliothèque, à tester : Adrien – Deep, Comforting and Warm (`TTtB1x9U8PF0Vgf20IAP`), Marcel – Warm, Soft and Intimate (`YV28ox2c5Cuh5rim0LrW`), Guillaume – Narrator (`ohItIVrXTBI80RrUECOD`), Charles Pestel – Calm and Professional (`592QbnMQfByEAOJe8maw`), Nicolas – Narrator (`aQROLel5sQbj1vuIVi6B`).
  - Un comparatif audio de ces 8 voix sur le même extrait a été généré le 12/10.

## Références de style (Agence 1600, Vimeo)

| Vidéo | Durée | Lien |
|---|---|---|
| Gojiberry | 71 s | https://vimeo.com/1171069888 |
| Trellis | 63 s | https://vimeo.com/1228532891 |
| Notion | 13 s | https://vimeo.com/1116887083 |
| Lemlist | 52 s | https://vimeo.com/1201492792 |
| Slack | 67 s | https://vimeo.com/900238637 |
| Taapit (sans paroles) | 77 s | https://vimeo.com/1101854162 |

Vimeo bloque les téléchargements automatisés (captcha Cloudflare). Pour les analyser image par image, il faut les MP4 (à déposer dans le dossier Frame.io ou Google Drive).

## Sources produit

- Direction artistique : https://ask-it.ai/
- Maquette du dashboard : URL et mot de passe fournis par Pierre, non versionnés. Espace client d'exemple : Endro.
- Diagnostics clients en ligne :
  - Endro : https://www.endro-cosmetiques.com/pages/diagnostic-peau
  - Les Petits Prodiges : https://lespetitsprodiges.com/pages/diagnostic-1?view=diagnostic
  - Sova : https://sova-diag.ask-it.ai/
- Connecteur Motion disponible pour des plans très avancés. Compte Motion à 0 crédit au 12/10.

## Constats du 12/10 (analyse complète)

Rapport détaillé avec visuels : artefact privé « Revue vidéo Ask-it » (lien dans la conversation du 12/10).

- **DA Ask-it (site)** : fond blanc cassé avec grille fine, noir profond, typo géométrique (Lufga sur le site), boutons pilules noirs. L'orange/corail vient du dashboard et des signes « + » / « × » des chiffres du site.
- **Dashboard (maquette)** : accueil « CA généré par le diagnostic » (78 343 €), courbe corail, KPI, personas avec photos (Claire « la peau qui tiraille », Julie, Inès), parcours du diagnostic avec « Frein détecté : l'écran de contact », Aski Chat (IA), segment Klaviyo. « Alice » y est l'utilisatrice côté marque : la visiteuse de la vidéo s'appellera **Claire**.
- **Endro** (marque à privilégier, déjà en vitrine sur ask-it.ai) : panneau vert profond, Nuancier de Peau (36 profils = textures naturelles × 3 teintes), questions au prénom, choix en photos, curseur, offre −15 % contre l'e-mail, révélation « Votre profil CORAIL02 », routine en 4 étapes (72,50 €), « Vous êtes comme 6 % des endroïstes ».
- **Les Petits Prodiges** : même moteur, habillage opposé (beige, photos lifestyle, mot des fondatrices). Idéal pour « à votre image ».
- **Sova** : la page du site « Camille ≠ Sarah » (même diagnostic, deux pages différentes) illustre « 100 % personnalisée ».
- **Chiffres à harmoniser** : script ×4 / +36 % ; site ×6,4 / +33 % (« mesuré sur l'ensemble de nos clients ») ; maquette Endro ×4,7 / +18 %. Le « 70 % » figure aussi sur le site.
- **Références** : langage commun = univers couleur de la marque cliente, titre gras avec un mot mis en valeur, interface réelle en très grand avec profondeur de champ, cartes flottantes, visages réels. MP4 à fournir pour analyser le mouvement et le son.

## Direction recommandée (résumé)

- Master d'environ 95 s (voix resserrée, script ajusté pour Eleven v4) + déclinaison 30 s pour les publicités.
- Deux mondes : « avant » gris froid désaturé, « après » univers Ask-it ; bascule sur « Bon, ça, c'était avant ».
- Une idée par plan, interface zoomée (texte ≥ 28 px en 1080p), caméra continue avec raccords de forme, typo cinétique calée au mot.
- Son : musique Eleven Music en sections (avant / après), bruitages UI ElevenLabs, ducking −12 dB, −14 LUFS réseaux / −16 LUFS site.
- Structure : hésitation (9 s) · problème (16 s) · bascule (7 s) · diagnostic Endro + CORAIL02 (14 s) · recommandation (13 s) · dashboard (16 s) · zéro effort (6 s) · elle revient (9 s) · fin (6 s).

## Chaîne de fabrication

- HyperFrames 0.8.150 (Apache-2.0), HTML/CSS/GSAP. Rendu validé dans l'environnement cloud avec
  `HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell`.
- Voix : `eleven_v4`, phrase par phrase, puis alignement mot à mot (`/v1/speech-to-text`, `scribe_v2`) pour piloter les animations.
- Bruitages : 40 crédits par seconde. Musique : Eleven Music, autorisée pour un usage publicitaire.
- Motion (connecteur) : à réserver à un ou deux plans très avancés ; compte à 0 crédit au 12/10.

## Process convenu

1. Analyse de toutes les sources et recommandations (12/10).
2. Pierre commente la vidéo sur Frame.io. Je lis les commentaires depuis le lien de partage.
3. Production : reconstruction en code, voix calée au mot près, bruitages et musique ElevenLabs, mixage.
4. Rendu MP4, nouvelle version sur Frame.io, puis itérations jusqu'à la version finale.

## v3 livrée le 12/10 (sans commentaires Frame, sans musique)

- **Demande** : Pierre a ajouté les 6 références en MP4 sur Frame. Il garde Martin Dupont. Il demande une v3 sans attendre ses commentaires Frame (il les ajoutera ensuite), avec la voix et les bruitages ; la musique viendra après.
- **Analyse des 6 références** (Trellis, Slack, Taapit, Notion, Gojiberry, lemlist) :
  - pas de coupe sèche ; transitions dans les pauses de la voix ;
  - impacts réservés aux chiffres ;
  - un son par geste, calé sur le pic du mouvement ;
  - court silence avant les bascules ;
  - interface en très grand, caméra toujours en mouvement.
- **Projet** :
  - `video/` (HyperFrames) : 10 scènes `compositions/f01…f10`, assemblage dans `index.html`, piste son unique `assets/audio/mix.wav` (hors git).
  - Transitions : f02→f03 fondu, f06→f07 et f08→f09 poussée, f07→f08 et f09→f10 flou. Les autres raccords sont des raccords d'image.
  - `fit_slot.py` ajuste les scènes à ces transitions sans décaler les repères voix.
- **Son** :
  - 176 repères (`video/scripts/cues_gen.py`) mesurés sur les timelines GSAP réelles ;
  - bruitages 14 LU sous la voix et atténués de 4 dB quand elle parle ;
  - master −14 LUFS / −1 dBTP.
- **Rendu** : 105,5 s, 1080p30.
  - Master de 57,7 Mo (trop lourd pour l'envoi direct).
  - Copie de 27,2 Mo envoyée à Pierre (SSIM 0,997 par rapport au master).
- **Écarts assumés** :
  - chiffres du script (×4, +36 %) ;
  - total de la routine 72,50 € pour 5 produits (4 cartes affichées) ;
  - « Peau sensible 3/10 » d'après la capture réelle ;
  - chiffres du dashboard repris de la maquette.
- **Suite** : commentaires Frame de Pierre, puis musique Eleven Music (deux sections avant/après), puis déclinaison 30 s.

## Analyse image par image du 13/10

Pierre l'a demandée avant de donner ses retours sur la v3. Elle compare les 5 références et la v3 avec les mêmes mesures. Détail dans `docs/motion-avance.md`.

Constat principal : la v3 est plus statique que les références et que la v2 :
- 36 % d'images figées, contre 5 à 12 % ;
- 14,8 pauses de 0,5 s par minute, contre environ 1 ;
- une interface trop petite à l'écran.

## v4 en cours (15/10) : refonte du mouvement d'après l'analyse

Demande de Pierre : nouvelle version de 100 s maximum, construite sur l'analyse image par image, et « pourcent » prononcé en entier par la voix.

- **Voix** : `assets/audio/vo_v4.wav` (96,2 s, hors git) et sa timeline mot à mot.
  - « % » est écrit « pourcent » dans le script.
  - Les jetons « % » et la ponctuation de la transcription sont rattachés au mot précédent. Plus aucune coupe ne tombe dans un mot.
  - Scripts : `scripts/vo_gen4.py`, `scripts/vo_assemble4.py`, textes dans `audio-src/vo_lines_v4.json`.
- **Durée** : 98,0 s, 60 i/s.
- **Langage de mouvement** : `frame.md` → « Motion language v4 ». Les recettes mesurées sont codées dans `lib/motionkit.js` (`window.MK`) :
  - dérive caméra continue ;
  - pop à ressort, slam précédé d'une aspiration, clic à 4 réponses ;
  - sortie accélérée puis entrée lancée, traversée par zoom, gravité ;
  - texte cinétique, compteur avec retenue, vol en arc.
  - La dérive seule garde 0 % d'images figées sur un plan d'interface, avec la même mesure que pour les références.
- **Storyboard** : `STORYBOARD.md` v4, 14 scènes de f01 à f14, chaque geste calé sur la voix.
  - Les raccords sont dans les scènes : coupe franche sur l'image la plus rapide. Il n'y a plus de transitions dans `index.html`.
  - Les scènes ont été construites par 7 agents, 2 scènes chacun, à partir de `.hyperframes/frame-packets-v4/` (hors git).
  - Outil de contrôle des scènes : `scene_snap.mjs` dans le scratchpad. Il produit des captures et mesure la part d'images figées.
- **Flou de mouvement** : composant registre `motion-blur`, chargé une fois via `lib/motion-blur.js`. Il s'applique aux éléments qui portent `data-hf-motion-blur`.
- **Musique** : Eleven Music `music_v2_5`, avec un plan de composition aux durées imposées.
  - Lit AVANT de 26 s, sombre et minimal, à 100 BPM.
  - Lit APRÈS de 71,4 s, lumineux, à 112 BPM.
  - Aucune voix détectée par la transcription.
  - `scripts/music_edit.py` cale la musique sur l'image :
    - silence de 0,28 s avant chaque slam, puis reprise sur un coup de grosse caisse à l'image d'impact (écart de 0 à 20 ms) ;
    - chute de 30 dB après « à l'aveugle » ;
    - le premier coup du lit APRÈS tombe sur « It » de « Ask-it ».
- **Bruitages** : 6 sons ajoutés au fichier `audio-src/sfx_library.json` : `suck`, `switch_light`, `fall`, `zoom_dive`, `land`, `slam_big`.
  - `scripts/cues_gen4.py` produit la feuille de 249 repères, en temps global.
- **Mixage** : `scripts/mix4.py` (voix, bruitages, musique).
  - Musique à −9 LU de la voix et atténuée de 6 dB quand la voix parle, soit environ 15 dB sous la voix.
  - Creux de −3 dB vers 2,5 kHz dans la musique.
  - Master à −14 LUFS et −1 dBTP.
