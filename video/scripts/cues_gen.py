# Cue sheet: per-scene local times -> global cue list (cues.json). Times = the visual event the sound must hit.
import json, sys
START = {'f01':0.0,'f02':12.39,'f03':23.00,'f04':29.85,'f05':37.48,'f06':52.23,'f07':64.59,'f08':75.82,'f09':83.23,'f10':94.84}
G = {'ui_tap':-14,'ui_select':-18,'swipe':-20,'whoosh_soft':-20,'whoosh_fast':-17,'pop':-17,'chip_fly':-14,'tab_close':-15,
     'dots_fade':-16,'counter_tick':-22,'number_slam':-15,'ember_burn':-22,'muffle_drone':-16,'rewind':-18,'color_flood':-18,
     'logo_sting':-12,'success':-16,'paper_crumple':-14,'typing':-12,'notif':-16,'timer':-16,'sparkle':-20,'skin_swap':-17,'cart_add':-15}
S = {
 'f01': [(1.40,'swipe',{}),(3.21,'ui_tap',{}),(4.91,'ui_tap',{}),(6.40,'swipe',{}),
         (7.95,'whoosh_soft',{'gain':-19}),(8.05,'pop',{'gain':-22,'pitch':-2,'pan':-0.4}),(8.17,'pop',{'gain':-23,'pan':0.5}),
         (8.30,'pop',{'gain':-24,'pitch':2,'pan':-0.2}),(8.42,'pop',{'gain':-26,'pitch':3,'pan':0.3}),
         (8.6,'muffle_drone',{'gain':-20}),(11.55,'tab_close',{})],
 'f02': [(0.10,'number_slam',{'gain':-19}),(1.60,'dots_fade',{}),(2.29,'number_slam',{}),
         (3.95,'whoosh_soft',{}),(5.23,'pop',{}),
         (6.15,'pop',{'gain':-19,'pan':-0.5}),(6.27,'pop',{'gain':-20,'pitch':1,'pan':0.4}),(6.39,'pop',{'gain':-21,'pitch':2,'pan':-0.2}),(6.51,'pop',{'gain':-22,'pitch':3,'pan':0.3}),
         (8.55,'ui_select',{'pan':-0.5}),(8.73,'ui_select',{'pan':0.3,'pitch':1}),(8.91,'ui_select',{'pan':-0.1,'pitch':2}),(9.09,'ui_select',{'pan':0.5,'pitch':3})],
 'f03': [(1.67,'counter_tick',{'align':'start'}),(1.80,'ember_burn',{'align':'start'}),
         (2.88,'ui_select',{}),(3.30,'ui_select',{'pitch':1}),(3.70,'ui_select',{'pitch':2}),(4.10,'ui_select',{'pitch':3}),
         (4.95,'whoosh_soft',{'gain':-22}),(6.0,'muffle_drone',{})],
 'f04': [(0.15,'rewind',{'align':'start'}),(1.94,'color_flood',{}),(2.15,'logo_sting',{}),(4.63,'skin_swap',{}),
         (5.46,'pop',{'pan':-0.3}),(5.53,'pop',{'pitch':2,'pan':0.3}),(5.60,'pop',{'pitch':4,'pan':-0.1}),(5.67,'pop',{'pitch':5,'pan':0.4}),
         (6.05,'ui_select',{}),(6.13,'ui_select',{'pitch':2}),(6.21,'ui_select',{'pitch':4})],
 'f05': [(0.06,'ui_select',{}),(1.15,'whoosh_soft',{}),(2.30,'skin_swap',{}),(3.20,'skin_swap',{'pitch':-1}),
         (4.45,'swipe',{}),(4.60,'typing',{'trim':(0.0,0.55),'align':'start'}),
         (6.89,'ui_tap',{}),(7.44,'chip_fly',{}),(7.68,'ui_tap',{}),(8.23,'chip_fly',{'pitch':1}),(8.54,'ui_tap',{}),(9.09,'chip_fly',{'pitch':2}),
         (9.80,'timer',{'align':'start'}),(10.15,'ui_select',{}),(11.28,'pop',{}),(11.62,'success',{}),
         (12.30,'pop',{'pitch':1}),(13.52,'pop',{'pitch':-1})],
 'f06': [(0.05,'ui_select',{}),(0.80,'swipe',{}),(2.25,'whoosh_soft',{}),(2.73,'pop',{}),(3.50,'swipe',{'gain':-23}),
         (3.70,'pop',{}),(3.78,'pop',{'pitch':2}),(3.86,'pop',{'pitch':4}),(3.94,'pop',{'pitch':5}),
         (5.15,'sparkle',{}),(7.10,'whoosh_soft',{}),(7.30,'counter_tick',{'align':'start','trim':(0.0,0.7)}),(8.00,'number_slam',{}),
         (10.45,'counter_tick',{'align':'start','trim':(0.0,0.65)}),(11.10,'number_slam',{})],
 'f07': [(0.00,'whoosh_fast',{}),(2.00,'tab_close',{'gain':-16}),(2.95,'paper_crumple',{}),(3.85,'whoosh_soft',{}),
         (4.00,'counter_tick',{'align':'start','trim':(0.0,1.15)}),(5.17,'cart_add',{}),
         (5.95,'whoosh_soft',{}),(6.87,'ui_select',{}),(7.62,'whoosh_soft',{}),(8.34,'notif',{}),
         (8.90,'swipe',{}),(9.10,'typing',{'trim':(0.0,0.8),'align':'start'}),(10.23,'ui_tap',{}),(10.30,'success',{})],
 'f08': [(0.00,'whoosh_soft',{}),(0.60,'typing',{'trim':(0.0,0.4),'align':'start'}),(1.00,'typing',{'trim':(0.4,1.1),'align':'start'}),
         (1.86,'ui_select',{}),(2.74,'ui_tap',{}),(2.82,'success',{}),
         (3.60,'pop',{'gain':-19}),(3.85,'pop',{'gain':-19,'pitch':2}),(4.10,'pop',{'gain':-19,'pitch':4}),(4.35,'pop',{'gain':-19,'pitch':5}),
         (5.50,'notif',{}),(5.80,'notif',{'pitch':1}),(6.10,'notif',{'pitch':2})],
 'f09': [(0.00,'whoosh_fast',{}),(0.45,'pop',{}),(1.95,'ui_tap',{}),(2.10,'swipe',{}),
         (4.75,'ui_tap',{}),(5.87,'ui_tap',{'pitch':1}),(6.61,'ui_tap',{'pitch':2}),
         (7.69,'skin_swap',{}),(8.05,'sparkle',{}),(8.60,'swipe',{'gain':-22}),
         (10.49,'ui_tap',{}),(10.55,'cart_add',{}),(10.75,'pop',{'pitch':3})],
 'f10': [(0.00,'whoosh_soft',{}),(1.15,'success',{'gain':-18}),(2.35,'whoosh_soft',{'gain':-22}),
         (2.93,'dots_fade',{'rev':True,'align':'start'}),(4.41,'number_slam',{'gain':-17}),
         (5.47,'logo_sting',{}),(6.14,'pop',{}),(8.20,'ui_tap',{}),(8.26,'success',{'gain':-17})],
}
out = []
for sc, lst in S.items():
    for t, name, o in lst:
        c = dict(t=round(START[sc]+t, 3), sfx=name, gain=o.get('gain', G[name]), scene=sc)
        for k in ('pitch','pan','rev','align','trim'):
            if k in o: c[k] = o[k]
        out.append(c)
json.dump(out, open(sys.argv[1], 'w'), indent=1)
print(len(out), 'cues, density', round(len(out)/105.5, 2), '/s')
