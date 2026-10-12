# Objective SFX metrics: true duration, onset delay, peak dBFS, integrated loudness-ish RMS, tail, spectral centroid.
import sys, glob, os, subprocess, numpy as np, json
d = sys.argv[1]; rows = {}
for f in sorted(glob.glob(os.path.join(d, 'raw', '*.mp3'))):
    raw = subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',f,'-ac','1','-ar','48000','-f','f32le','-'],capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    if len(x) == 0: continue
    fr = 480; n = len(x)//fr
    rms = np.sqrt(np.mean(x[:n*fr].reshape(n,fr)**2, axis=1)) + 1e-9
    db = 20*np.log10(rms); thr = db.max() - 30
    on = np.where(db > thr)[0]
    onset = on[0]*0.01 if len(on) else 0; last = on[-1]*0.01 if len(on) else 0
    spec = np.abs(np.fft.rfft(x[:min(len(x), 48000)] * np.hanning(min(len(x), 48000))))
    freqs = np.fft.rfftfreq(min(len(x),48000), 1/48000); cent = float((spec*freqs).sum()/(spec.sum()+1e-9))
    rows[os.path.basename(f)[:-4]] = dict(dur=round(len(x)/48000,2), onset=round(onset,2), active=round(last-onset,2),
        peak_db=round(float(20*np.log10(np.abs(x).max()+1e-9)),1), rms_db=round(float(20*np.log10(np.sqrt(np.mean(x**2))+1e-9)),1), centroid=int(cent))
for k,v in rows.items(): print(f"{k:22s} {v}")
json.dump(rows, open(os.path.join(d,'metrics.json'),'w'), indent=1)
