# Compare momentary loudness (400 ms, every 100 ms) of the VO and SFX stems; flag SFX that crowd the voice.
import sys, os, subprocess, re, json, numpy as np
D = sys.argv[1]
def mom(path):
    e = subprocess.run(['ffmpeg','-hide_banner','-nostats','-v','verbose','-i',path,'-af','ebur128=framelog=verbose','-f','null','-'],capture_output=True,text=True).stderr
    t, M = [], []
    for m in re.finditer(r't:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+|-inf)', e):
        t.append(float(m.group(1))); M.append(float(m.group(2)) if m.group(2) != '-inf' else -120.0)
    return np.array(t), np.array(M)
tv, Mv = mom(os.path.join(D, 'stem_vo.wav')); ts, Ms = mom(os.path.join(D, 'stem_sfx.wav'))
n = min(len(Mv), len(Ms)); Mv, Ms, t = Mv[:n], Ms[:n], tv[:n]
speech = Mv > -35
diff = Ms - Mv
print('SFX vs VO during speech: median %.1f dB, p90 %.1f dB, max %.1f dB' % (np.median(diff[speech]), np.percentile(diff[speech], 90), diff[speech].max()))
placed = json.load(open(os.path.join(D, 'placed.json')))
bad = np.where(speech & (diff > -8))[0]
print('windows where SFX within 8 dB of the voice:', len(bad))
seen = set()
for i in bad:
    tt = t[i]
    near = [p for p in placed if p['start'] - 0.1 <= tt <= p['start'] + 1.0]
    key = tuple(sorted(set(p['sfx']+'@'+str(p['t']) for p in near)))
    if key in seen: continue
    seen.add(key)
    print(f'  t={tt:6.2f}  VO {Mv[i]:6.1f}  SFX {Ms[i]:6.1f}  ->', ', '.join(key))
gaps = (~speech) & (Ms > -60)
print('SFX in voice gaps: max momentary %.1f LUFS' % (Ms[gaps].max() if gaps.any() else -120))
