# Cue sheet -> cues.json. Each time is the VISUAL EVENT the sound must hit (scene-local, measured on the
# built compositions' GSAP timelines); align='hit' puts the sound's own impact point on it.
# Rules (from the reference analyses): one sound per gesture template, hits on the motion peak, transitions
# get a whoosh, numbers get a slam, a short silence before the world switch, keys sounded one by one.
import json, sys
START = {'f01':0.0,'f02':12.39,'f03':23.00,'f04':29.85,'f05':37.48,'f06':52.23,'f07':64.59,'f08':75.82,'f09':83.23,'f10':94.84}
G = {'ui_tap':-14,'ui_select':-19,'swipe':-21,'whoosh_soft':-21,'whoosh_fast':-17,'pop':-19,'chip_fly':-15,'tab_close':-15,
     'dots_fade':-16,'counter_tick':-24,'number_slam':-16,'ember_burn':-22,'muffle_drone':-17,'rewind':-19,'color_flood':-18,
     'logo_sting':-15,'success':-18,'paper_crumple':-14,'typing':-13,'notif':-17,'timer':-17,'sparkle':-21,'skin_swap':-17,'cart_add':-16}
# single keystrokes cut from the typing take: (start, end) in the prepared file, onset ~6 ms in
KEYS = [(0.056, 0.11), (0.208, 0.262), (0.330, 0.386), (0.408, 0.46), (0.736, 0.80), (0.938, 1.0)]
def keys(times, gain=-15, pan=0.0):
    out = []
    for i, t in enumerate(times):
        a, b = KEYS[(i * 4 + 1) % len(KEYS)]
        out.append((t - 0.006, 'typing', {'trim': (a, b), 'align': 'start', 'gain': gain + (i % 3) * -1.5, 'pan': pan}))
    return out

S = {
 'f01': [(1.70,'swipe',{}),(2.96,'ui_tap',{}),(4.76,'ui_tap',{'pitch':1}),(6.30,'swipe',{'gain':-22}),
         (7.92,'whoosh_soft',{'gain':-20}),(7.86,'pop',{'gain':-24,'pan':-0.4}),(8.00,'pop',{'gain':-25,'pitch':2,'pan':0.4}),
         (9.00,'pop',{'gain':-25,'pitch':3,'pan':0.3}),(9.12,'pop',{'gain':-26,'pitch':5,'pan':-0.3}),
         (9.40,'muffle_drone',{'gain':-21}),(11.78,'tab_close',{})],
 'f04': [(0.10,'rewind',{'align':'start'}),(1.78,'color_flood',{}),(1.90,'logo_sting',{}),(3.16,'pop',{'gain':-23}),
         (4.62,'skin_swap',{}),(4.92,'success',{'gain':-20}),
         (5.29,'pop',{'gain':-21,'pan':-0.3}),(5.36,'pop',{'gain':-21,'pitch':2,'pan':0.3}),(5.43,'pop',{'gain':-22,'pitch':4,'pan':-0.1}),(5.50,'pop',{'gain':-22,'pitch':5,'pan':0.4}),
         (5.92,'whoosh_soft',{'gain':-24}),(6.03,'ui_select',{}),(6.11,'ui_select',{'pitch':2}),(6.19,'ui_select',{'pitch':4})],
 'f06': [(0.95,'swipe',{}),(1.10,'ui_select',{}),(2.10,'whoosh_soft',{}),(2.62,'pop',{}),(3.52,'swipe',{'gain':-23}),
         (3.66,'pop',{'gain':-20}),(3.74,'pop',{'gain':-20,'pitch':2}),(3.82,'pop',{'gain':-21,'pitch':4}),(3.90,'pop',{'gain':-21,'pitch':5}),
         (4.05,'counter_tick',{'align':'start','trim':(0.0,1.0)}),(5.20,'sparkle',{'gain':-22}),(5.95,'pop',{'gain':-21,'pitch':-2}),
         (7.21,'whoosh_soft',{}),(7.48,'number_slam',{}),(7.50,'counter_tick',{'align':'start','trim':(0.0,0.45)}),
         (9.80,'whoosh_soft',{'gain':-23}),(9.90,'number_slam',{}),(9.92,'counter_tick',{'align':'start','trim':(0.0,1.1)}),(11.02,'pop',{})],
 'f08': keys([0.60,0.67,0.75,0.84,0.93]) + keys([1.04,1.10,1.16,1.22,1.28,1.35,1.41,1.47,1.60], gain=-16) +
        [(1.72,'ui_select',{}),(2.70,'ui_tap',{}),(2.86,'success',{}),(3.55,'whoosh_soft',{'gain':-23}),
         (4.10,'ui_select',{}),(4.35,'ui_select',{'pitch':2}),(4.60,'ui_select',{'pitch':4}),(4.85,'ui_select',{'pitch':5}),
         (5.55,'notif',{}),(5.85,'notif',{'pitch':1}),(6.15,'notif',{'pitch':2,'gain':-16})],
 'f09': [(0.45,'pop',{}),(1.97,'ui_tap',{}),(2.10,'swipe',{'gain':-22}),(2.54,'ui_tap',{'gain':-17,'pitch':-1}),
         (3.38,'swipe',{'gain':-24}),(4.72,'ui_tap',{}),(5.05,'swipe',{'gain':-25}),(5.82,'swipe',{'pitch':3,'gain':-21}),
         (6.05,'ui_tap',{'pitch':1}),(6.58,'ui_tap',{'pitch':2}),(7.12,'skin_swap',{}),(7.55,'sparkle',{'gain':-20}),
         (8.75,'swipe',{'gain':-22}),(9.25,'sparkle',{'gain':-24}),(10.44,'ui_tap',{}),(10.53,'cart_add',{}),(10.99,'pop',{'pitch':3})],
 # provisional until the scene lands
 'f02': [(0.06,'dots_fade',{'trim':(0.0,0.16),'align':'start','pitch':-2,'gain':-20}),
         (1.22,'dots_fade',{'align':'start','gain':-17}),(1.22,'counter_tick',{'align':'start','trim':(0.0,1.0),'gain':-25}),
         (2.21,'number_slam',{}),(3.95,'whoosh_soft',{}),(5.10,'ui_select',{}),(5.98,'whoosh_soft',{'gain':-23}),
         (6.00,'pop',{'gain':-22,'pan':-0.4}),(6.24,'pop',{'gain':-23,'pitch':2,'pan':0.4}),(7.70,'swipe',{'gain':-24}),
         (8.55,'ui_select',{'pan':-0.5}),(8.73,'ui_select',{'pan':0.4,'gain':-20}),(8.91,'ui_select',{'pan':-0.2,'gain':-21}),(9.09,'ui_select',{'pan':0.5,'gain':-22})],
 'f03': [(1.67,'counter_tick',{'align':'start'}),(1.80,'ember_burn',{'align':'start'}),(2.88,'ui_select',{}),(4.10,'ui_select',{'pitch':3}),
         (6.0,'muffle_drone',{'trim':(0.0,1.9)})],
 'f05': [(0.06,'ui_select',{}),(1.15,'whoosh_soft',{}),(2.30,'skin_swap',{}),(3.20,'skin_swap',{'pitch':-1}),
         (4.45,'swipe',{}),(6.89,'ui_tap',{}),(7.44,'chip_fly',{}),(7.68,'ui_tap',{}),(8.23,'chip_fly',{'pitch':1}),(8.54,'ui_tap',{}),(9.09,'chip_fly',{'pitch':2}),
         (9.80,'timer',{'align':'start'}),(11.62,'success',{}),(12.30,'pop',{'pitch':1}),(13.52,'pop',{'pitch':-1})],
 'f07': [(0.86,'ui_select',{}),(1.86,'tab_close',{'gain':-16}),(2.80,'paper_crumple',{}),(3.22,'whoosh_soft',{'gain':-23}),
         (3.95,'whoosh_soft',{}),(3.97,'counter_tick',{'align':'start','trim':(0.0,0.9),'gain':-25}),(5.17,'cart_add',{}),
         (4.98,'pop',{'gain':-23}),(6.02,'whoosh_soft',{'gain':-22}),(6.68,'ui_select',{}),(7.62,'whoosh_soft',{'gain':-22}),
         (8.20,'notif',{}),(8.85,'swipe',{'gain':-22})] +
        keys([9.34,9.40,9.46,9.53,9.60,9.66,9.73,9.80,9.86], gain=-21, pan=0.3) +
        [(9.96,'pop',{'gain':-21}),(10.06,'ui_tap',{}),(10.22,'success',{})],
 'f10': [(0.40,'ui_select',{'gain':-21}),(1.00,'success',{'gain':-19}),(2.45,'whoosh_soft',{'gain':-22}),
         (2.95,'dots_fade',{'rev':True,'align':'start','gain':-16}),(3.15,'number_slam',{'gain':-18}),
         (5.34,'logo_sting',{'gain':-16}),(6.02,'pop',{}),(8.20,'ui_tap',{}),(8.27,'success',{'gain':-18})],
}
# root-level transitions (global times = middle of the move)
T = [(23.15,'whoosh_soft',{'gain':-25}), (64.465,'whoosh_fast',{}), (75.75,'whoosh_soft',{'gain':-20}),
     (83.055,'whoosh_fast',{}), (94.72,'whoosh_soft',{'gain':-21})]
out = []
for sc, lst in S.items():
    for t, name, o in lst:
        c = dict(t=round(START[sc] + t, 3), sfx=name, gain=o.get('gain', G[name]), scene=sc)
        for k in ('pitch','pan','rev','align','trim'):
            if k in o: c[k] = o[k]
        out.append(c)
for t, name, o in T:
    out.append(dict(t=t, sfx=name, gain=o.get('gain', G[name]), scene='transition'))
out.sort(key=lambda c: c['t'])
json.dump(out, open(sys.argv[1], 'w'), indent=1)
print(len(out), 'cues')
