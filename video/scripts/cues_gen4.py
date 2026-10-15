# v4 cue sheet -> cues.json (GLOBAL film times, 60 fps picture). Each time is the visual event the sound must hit,
# taken from STORYBOARD.md v4 and checked against the built scenes' GSAP timelines; align='hit' puts the sound's own
# impact point on it, align='start' starts it there.
# Rules (docs/motion-avance.md): every click has its sound on the click frame; every slam gets a suction before and a
# boom on the impact frame (the music stops 0.28 s before and comes back on a kick at the same frame, see
# music_edit.py); accelerated exits get a whoosh peaking on the cut; series of pops are sounded one by one.
import json, sys

G = {'ui_tap': -14, 'ui_select': -19, 'swipe': -21, 'whoosh_soft': -21, 'whoosh_fast': -17, 'pop': -21, 'chip_fly': -17,
     'tab_close': -15, 'dots_fade': -17, 'counter_tick': -23, 'number_slam': -16, 'ember_burn': -21, 'muffle_drone': -19,
     'rewind': -19, 'color_flood': -18, 'logo_sting': -16, 'success': -18, 'paper_crumple': -14, 'typing': -18, 'notif': -17,
     'timer': -19, 'sparkle': -22, 'skin_swap': -18, 'cart_add': -16,
     'suck': -18, 'switch_light': -12, 'fall': -17, 'zoom_dive': -15, 'land': -19, 'slam_big': -15}

def pops(times, base=-23, pitches=(0, 2, 4, 5, 7), pans=(-0.3, 0.3, -0.1, 0.4, 0.0)):
    return [(t, 'pop', {'gain': base - 0.7 * (i % 3), 'pitch': pitches[i % len(pitches)], 'pan': pans[i % len(pans)]}) for i, t in enumerate(times)]

def slam(t, big=True, suck_gain=-17):
    # suction ending 2 frames before the impact, then the boom on the impact frame
    return [(t - 0.03, 'suck', {'gain': suck_gain}), (t, 'slam_big' if big else 'number_slam', {})]

C = []
add = C.extend
# ---------------- f01 Hésitation (0.00) — AVANT
add([(0.00, 'swipe', {'align': 'start', 'gain': -18}), (0.25, 'pop', {'gain': -25, 'pitch': -2}), (2.18, 'pop', {'gain': -22, 'pitch': 3}),
     (2.98, 'ui_tap', {}), (3.85, 'ui_select', {'pitch': -5, 'gain': -20}), (4.22, 'whoosh_fast', {'gain': -20}),
     (4.63, 'ui_tap', {'pitch': 1}), (5.57, 'whoosh_soft', {'gain': -18})])
add(pops([5.58, 5.62, 5.67, 5.73], base=-24))
add(pops([6.68, 6.93, 7.03], base=-22, pitches=(2, 4, 6)))
add([(8.25, 'suck', {'gain': -19}), (8.40, 'ui_tap', {'gain': -20, 'pitch': -2}), (8.52, 'swipe', {'align': 'start', 'gain': -21}),
     (8.82, 'fall', {'align': 'start', 'gain': -15})])
# ---------------- f02 Soixante-dix (9.25)
add([(9.30, 'whoosh_fast', {'gain': -20}), (9.58, 'pop', {'pitch': -6, 'gain': -21})])
add(slam(11.30))
add([(11.32, 'dots_fade', {'align': 'start', 'gain': -18}), (12.97, 'whoosh_fast', {'gain': -18})])
# ---------------- f03 Problème (13.00)
add([(13.05, 'whoosh_soft', {'gain': -21}), (15.10, 'success', {'gain': -20}), (15.46, 'whoosh_fast', {'gain': -18})])
add(pops([15.52, 15.69, 15.86, 16.03, 16.22], base=-25))
add([(17.05, 'swipe', {'gain': -20})])
add([(t, 'ui_select', {'gain': -24 - (i % 2), 'pitch': [0, 2, 4, 5, 7][i], 'pan': [-0.4, 0.3, -0.1, 0.4, 0][i]}) for i, t in enumerate([17.95, 18.15, 18.35, 18.55, 18.75])])
add([(19.88, 'zoom_dive', {'rev': True, 'gain': -15})])
# ---------------- f04 Budget + c'était avant (19.90)
add([(19.90, 'number_slam', {'gain': -19}), (21.13, 'whoosh_soft', {'gain': -22}),
     (21.13, 'counter_tick', {'align': 'start', 'trim': (0.0, 0.92), 'gain': -22}), (21.13, 'ember_burn', {'align': 'start', 'gain': -21}),
     (22.05, 'notif', {'pitch': 3, 'gain': -20}), (22.25, 'whoosh_soft', {'gain': -22}), (22.45, 'chip_fly', {'gain': -20})])
add(pops([22.88, 22.95, 23.02, 23.08], base=-24))
add([(23.60, 'pop', {'pitch': -3, 'gain': -20}), (23.62, 'ui_select', {'pitch': -5, 'gain': -22}),
     (24.05, 'whoosh_soft', {'gain': -22}), (24.28, 'swipe', {'align': 'start', 'gain': -24}), (24.52, 'ui_tap', {'gain': -18}),
     (24.65, 'swipe', {'align': 'start', 'gain': -25, 'pitch': 2}), (24.85, 'ui_tap', {'gain': -18, 'pitch': 1}),
     (25.00, 'muffle_drone', {'align': 'start', 'trim': (0.0, 1.5), 'gain': -19}),
     (26.75, 'suck', {'gain': -18}), (26.76, 'land', {'gain': -22}), (26.89, 'swipe', {'align': 'start', 'gain': -22}),
     (27.19, 'fall', {'align': 'start', 'gain': -15})])
# ---------------- f05 Ask-it (27.62) — the world switch
add([(27.62, 'switch_light', {}), (28.20, 'logo_sting', {}), (29.07, 'whoosh_soft', {'gain': -22}),
     (30.02, 'typing', {'align': 'start', 'trim': (0.0, 0.3), 'gain': -21}), (30.79, 'success', {'gain': -18}), (30.80, 'pop', {'gain': -20}),
     (30.86, 'cart_add', {'gain': -21}), (31.60, 'whoosh_soft', {'gain': -21})])
add(pops([31.95, 32.02, 32.08], base=-24, pitches=(3, 5, 7)))
add([(32.20, 'suck', {'gain': -17}), (32.23, 'number_slam', {'gain': -16}), (32.33, 'number_slam', {'gain': -18, 'pitch': 2}),
     (32.43, 'number_slam', {'gain': -19, 'pitch': 4}), (32.87, 'ui_select', {'gain': -18}), (33.44, 'zoom_dive', {'rev': True, 'gain': -15})])
# ---------------- f06 Diagnostic (33.45)
add([(33.65, 'pop', {'gain': -23}), (34.39, 'sparkle', {'gain': -22}),
     (35.56, 'whoosh_fast', {'gain': -18}), (35.56, 'skin_swap', {}), (36.38, 'whoosh_fast', {'gain': -19}), (36.38, 'skin_swap', {'pitch': -1}),
     (36.93, 'pop', {'gain': -20}), (37.85, 'whoosh_soft', {'gain': -22}), (37.88, 'swipe', {'gain': -24})])
add([(37.90 + i * 0.034, 'typing', {'trim': (0.056, 0.11), 'align': 'start', 'gain': -19 - (i % 3)}) for i in range(6)])
add([(38.46, 'ui_tap', {}), (40.27, 'ui_tap', {'pitch': 1}), (40.76, 'chip_fly', {}), (40.78, 'ui_select', {'pitch': 3, 'gain': -23}),
     (40.97, 'whoosh_fast', {'gain': -20}), (41.07, 'ui_tap', {'pitch': 2}), (41.54, 'chip_fly', {'pitch': 1}), (41.56, 'ui_select', {'pitch': 5, 'gain': -23}),
     (41.75, 'whoosh_fast', {'gain': -21}), (41.85, 'swipe', {'align': 'start', 'pitch': 3, 'gain': -22}), (42.05, 'ui_select', {'gain': -21}),
     (42.37, 'chip_fly', {'pitch': 2, 'gain': -19}), (42.40, 'success', {'gain': -22}), (42.66, 'whoosh_fast', {'gain': -18})])
# ---------------- f07 Profil (42.70)
add([(42.92, 'slam_big', {'gain': -15}), (43.58, 'timer', {'gain': -20}), (44.00, 'suck', {'gain': -19}), (44.05, 'land', {'gain': -18}),
     (44.26, 'pop', {'gain': -18}), (44.27, 'sparkle', {'gain': -22}), (45.20, 'whoosh_soft', {'gain': -24}), (45.24, 'pop', {'gain': -20, 'pitch': 2}),
     (46.47, 'whoosh_soft', {'gain': -22}), (46.41, 'pop', {'gain': -19, 'pitch': -2}), (46.56, 'ui_select', {'pitch': -4, 'gain': -22}),
     (46.81, 'ui_select', {'pitch': -4, 'gain': -23}), (47.36, 'whoosh_fast', {'gain': -16})])
# ---------------- f08 Recommandation (47.40)
add([(47.45, 'swipe', {'gain': -22}), (47.62, 'pop', {'gain': -22}), (48.70, 'whoosh_soft', {'gain': -20})])
add(slam(49.66))
add([(50.40, 'whoosh_soft', {'gain': -22}), (50.40, 'swipe', {'gain': -24}), (50.47, 'swipe', {'gain': -25, 'pitch': 2}),
     (51.28, 'whoosh_fast', {'gain': -20}), (51.22, 'swipe', {'align': 'start', 'gain': -22})])
add([(t, 'chip_fly', {'gain': -19 - (i % 2), 'pitch': i, 'pan': [-0.2, 0.3, -0.3, 0.2][i]}) for i, t in enumerate([51.73, 51.80, 51.86, 51.93])])
add([(51.80, 'counter_tick', {'align': 'start', 'trim': (0.0, 0.6), 'gain': -24}), (52.47, 'cart_add', {'gain': -19})])
add(pops([52.86, 52.93, 53.00, 53.06], base=-23, pitches=(2, 4, 5, 7)))
add([(53.52, 'sparkle', {'gain': -22}), (54.18, 'suck', {'gain': -14})])
# ---------------- f09 Chiffres (54.20)
add([(54.21, 'pop', {'gain': -20})])
add(slam(54.92))
add([(55.84, 'pop', {'pitch': 2, 'gain': -22}), (57.33, 'pop', {'gain': -20}),
     (57.45, 'land', {'gain': -18}), (57.52, 'land', {'gain': -19, 'pitch': 2}), (57.60, 'land', {'gain': -20, 'pitch': 4})])
add(slam(57.81))
add([(58.77, 'whoosh_soft', {'pitch': 3, 'gain': -24}), (58.77, 'land', {'gain': -20}), (59.41, 'whoosh_fast', {'gain': -16})])
# ---------------- f10 Dashboard (59.45)
add([(59.62, 'pop', {'gain': -22}), (60.50, 'whoosh_soft', {'gain': -20}), (61.42, 'suck', {'gain': -22}), (61.44, 'number_slam', {}),
     (62.31, 'paper_crumple', {}), (62.61, 'fall', {'align': 'start', 'gain': -18}), (63.15, 'whoosh_soft', {'gain': -20}),
     (63.40, 'counter_tick', {'align': 'start', 'trim': (0.0, 1.0), 'gain': -22}), (64.40, 'pop', {'gain': -23}), (64.52, 'cart_add', {}),
     (65.91, 'whoosh_fast', {'gain': -17})])
# ---------------- f11 Insights (65.95)
add([(66.00, 'swipe', {'gain': -24}), (66.14, 'ui_select', {'gain': -18}), (66.15, 'sparkle', {'gain': -24}), (66.93, 'whoosh_soft', {'gain': -21})])
add(pops([66.95, 67.02, 67.08, 67.15], base=-24))
add([(67.54, 'suck', {'gain': -22}), (67.56, 'number_slam', {}), (68.15, 'whoosh_soft', {'gain': -20}),
     (68.20, 'typing', {'align': 'start', 'trim': (0.0, 0.85), 'gain': -20}), (69.05, 'pop', {'gain': -20}), (69.39, 'ui_tap', {}),
     (69.42, 'success', {'gain': -22}), (70.21, 'whoosh_fast', {'gain': -16})])
# ---------------- f12 Zéro effort (70.25)
add([(71.40, 'whoosh_soft', {'gain': -22}), (72.85, 'whoosh_soft', {'gain': -22}), (73.05, 'typing', {'align': 'start', 'trim': (0.0, 0.4), 'gain': -18}),
     (73.45, 'pop', {'gain': -22}), (73.72, 'ui_tap', {}), (73.75, 'success', {}), (73.92, 'whoosh_soft', {'gain': -22}), (73.97, 'pop', {'gain': -24, 'pitch': 3})])
add([(t, 'ui_select', {'gain': -20, 'pitch': p}) for t, p in [(74.19, 0), (74.44, 2), (74.70, 4), (74.95, 7)]])
add([(t, 'notif', {'gain': -17 - i, 'pitch': i}) for i, t in enumerate([75.80, 76.05, 76.30])])
add([(t, 'land', {'gain': -21}) for t in [75.80, 76.05, 76.30]])
add([(77.36, 'whoosh_fast', {'gain': -17})])
# ---------------- f13 Elle revient (77.40)
add([(77.45, 'swipe', {'gain': -24}), (77.55, 'pop', {'gain': -23}), (77.70, 'pop', {'gain': -19}), (77.72, 'sparkle', {'gain': -24}),
     (78.41, 'whoosh_soft', {'gain': -21}), (78.71, 'pop', {'pitch': -2, 'gain': -22}), (80.05, 'ui_tap', {'gain': -13}),
     (80.06, 'skin_swap', {}), (80.35, 'typing', {'align': 'start', 'trim': (0.0, 0.2), 'gain': -20}),
     (82.10, 'ui_tap', {'gain': -16}), (82.52, 'ui_tap', {'pitch': 1, 'gain': -16}), (82.92, 'whoosh_fast', {'gain': -20}),
     (83.18, 'swipe', {'align': 'start', 'pitch': 3, 'gain': -20}), (83.38, 'ui_select', {'gain': -20}), (83.82, 'whoosh_fast', {'gain': -20}),
     (84.21, 'ui_tap', {'pitch': 2, 'gain': -16}), (84.62, 'whoosh_fast', {'gain': -21})])
add([(84.60 + i * 0.067, 'ui_select', {'gain': -26, 'pitch': 2 * i}) for i in range(4)])
add([(84.95, 'success', {'gain': -16}), (84.96, 'sparkle', {'gain': -20}), (85.47, 'whoosh_soft', {'gain': -24}),
     (86.22, 'whoosh_soft', {'gain': -24}), (86.66, 'pop', {'gain': -22}), (87.35, 'pop', {'gain': -20}),
     (87.79, 'ui_tap', {'gain': -13}), (88.12, 'cart_add', {'gain': -15}), (88.49, 'zoom_dive', {'rev': True, 'gain': -15})])
# ---------------- f14 Fin (88.50)
add([(88.55, 'land', {'gain': -19}), (88.56, 'sparkle', {'gain': -22}), (89.74, 'success', {'gain': -21}), (89.76, 'sparkle', {'gain': -24}),
     (90.96, 'whoosh_soft', {'gain': -18}), (91.40, 'whoosh_soft', {'gain': -25})])
add(slam(91.84, suck_gain=-16))
add([(91.86, 'dots_fade', {'rev': True, 'align': 'start', 'gain': -21}), (93.80, 'suck', {'gain': -20}), (94.00, 'logo_sting', {'gain': -14}),
     (94.45, 'pop', {'gain': -18}), (94.80, 'swipe', {'align': 'start', 'gain': -26}), (95.31, 'ui_tap', {'gain': -12}),
     (95.33, 'sparkle', {'gain': -20}), (95.45, 'pop', {'gain': -24, 'pitch': 4})])

out = []
for t, name, o in C:
    c = dict(t=round(t, 3), sfx=name, gain=o.get('gain', G[name]))
    for k in ('pitch', 'pan', 'rev', 'align', 'trim'):
        if k in o:
            c[k] = o[k]
    out.append(c)
out.sort(key=lambda c: c['t'])
json.dump(out, open(sys.argv[1], 'w'), indent=1)
print(len(out), 'cues')
