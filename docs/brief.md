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

## Process convenu

1. Analyse de toutes les sources et recommandations (12/10).
2. Pierre commente la vidéo sur Frame.io. Je lis les commentaires depuis le lien de partage.
3. Production : reconstruction en code, voix calée au mot près, bruitages et musique ElevenLabs, mixage.
4. Rendu MP4, nouvelle version sur Frame.io, puis itérations jusqu'à la version finale.
