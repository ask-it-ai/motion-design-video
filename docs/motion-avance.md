# Motion avancé vs basique : analyse image par image (13/10/2026)

Pierre a demandé une analyse image par image des 5 références du dossier Frame : Trellis, Slack, lemlist, Gojiberry et Taapit. Ce sont les mêmes fichiers que lors de la première analyse.

La v3 et la v2 ont été passées dans les mêmes mesures, avec l'outil `video/scripts/fbf.py`.

Synthèse illustrée (page privée) : https://claude.ai/artifact/RGqT8o2XcambcD7EVEfEzu

## Mesures comparées

Échantillonnage commun à 30 i/s (Taapit à 25 i/s). Slack est mesuré sur sa partie image seule (0–52 s).

| Film | Images figées | Pauses ≥ 0,5 s/min | Surface en mouvement (médiane) | Zoom caméra | Éléments qui bougent seuls | Rafales de flou/min |
| --- | --- | --- | --- | --- | --- | --- |
| Trellis | 4,9 % | 0,9 | 4,5 % | 22,6 % | 54,6 % | 25,6 |
| Gojiberry | 4,8 % | 0,8 | 2,9 % | 27,4 % | 44,0 % | 30,5 |
| lemlist | 12,1 % | 1,2 | 2,0 % | 23,7 % | 38,7 % | 34,9 |
| Taapit | 11,1 % | 1,5 | 1,6 % | 18,9 % | 29,5 % | 37,2 |
| Slack | 22,6 % | 9,2 | 1,2 % | 14,8 % | 27,7 % | 20,7 |
| v2 | 21,8 % | 11,0 | 2,4 % | 22,8 % | 35,1 % | 26,8 |
| **v3** | **35,7 %** | **14,8** | **0,4 %** | **7,4 %** | **15,7 %** | **12,5** |
| **v4 (15/10)** | **4,9 %** | **0,6** | **2,7 %** | **28,5 %** | **37,1 %** | **28,8** |

- **Slack** : ses pauses sont des noirs et des cartons comiques voulus. Hors noirs, moins de 4 % de ses images sont figées.
- **v3, par scène** : 40 à 47 % d'images figées, sauf le dashboard (9 %).
- **v4, par scène** : de 0 à 9 %, sauf les chiffres f09 (21 %, gros textes sur fond clair, plus longue pause 0,40 s) et le carton final f14 (18 %, pause voulue de 0,67 s).

## Les 10 écarts

1. **Rien ne s'arrête.**
   - L'action vient par rafales de 0,2 s séparées par une dérive lente.
   - L'immobilité ne vient qu'en verrou court, 14–17 images après un résultat.
   - Jamais plus de 0,4–0,6 s figé.
2. **L'interface est filmée de près par une caméra.**
   - Gojiberry : formulaire à 81 % de la largeur.
   - Taapit : UI agrandie ×2–2,6 au clic, texte de 26–34 px à l'écran.
   - Slack : caméra 3D de −4° à +7°, ×1,15.
   - Le secondaire est remplacé par des barres grises.
   - v3 : téléphone entier, texte courant ≈ 14 px.
3. **Le clic est un événement.**
   - Bascule en 1 image et tressaillement du cadre (−8/+4 px sur 6 images).
   - 3 traits pendant 7 images et pulsation de +2,5 %.
   - Son sur l'image même, saut caméra de +20 %.
4. **Les sorties accélèrent et l'élan traverse la coupe.**
   - Vitesse ×1,2–1,3 par image, coupe sur l'image la plus rapide.
   - Entrée trop grande (×1,3–1,5) qui freine en 6–14 images.
   - Jamais de fond vide prolongé.
5. **60 i/s et vrai flou de mouvement.**
   - Flou de 0,35–0,5 × le déplacement par image.
   - « Stop » de Trellis :
     - aspiration de 18 images ;
     - arrivée à ×6,55 et taille atteinte en 9 images ;
     - écrasement de −16,5 %, retour en 14 images, secousse de ±25 px.
6. **Anticipation, dépassement, gravité.**
   - Contraction de 30–55 % commencée 8 images avant une expansion.
   - Dépassement de 20–25 % sans rebond.
   - Chute qui accélère.
7. **Les actions se chevauchent.**
   - Chaque calque part au pic de vitesse du précédent.
   - Décalages de 1 (icônes), 3–5 (lettres), 4 (série), 6–8 (mots) images.
8. **Le texte porte le rythme.**
   - Mots neutres en avance sur la voix, à 5–8 images par mot.
   - Mots-clés construits sur leur syllabe.
   - Deux graisses.
9. **Profondeur et matière.**
   - Plans inclinés à 60–68° et parallaxe ×1,4.
   - Fond flouté 5 images avant le geste.
   - Lettres éclairées, grain.
10. **Le son tombe à l'image et sait se taire.**
    - Creux avant chaque impact.
    - Montée 4–5 images avant, impact à 0–2 images près.
    - Chute d'environ 30 dB à la bascule de monde.

## Plan proposé pour la v4

À ajuster avec les retours de Pierre sur la v3.

- Rendu à 60 i/s avec flou de mouvement.
- Budget d'immobilité : au plus 1 pause de 0,5 s par minute.
- Interface en macro, filmée par une caméra.
- Clics à 4 réponses.
- Une seule grammaire de transition : sortie accélérée, puis entrée lancée.
- Slams des chiffres : 70 %, ×4, +36 %, 78 343 €.
- Actions qui se chevauchent.
- Texte animé sur les phrases clés.
- Anticipation et ressort.
- Plans inclinés pour la recommandation et le dashboard.
- Son avec creux et silences, puis musique hachée calée sur les mouvements clés.
