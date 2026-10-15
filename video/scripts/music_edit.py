# Cut the two Eleven Music beds to picture (v4) -> one 48 kHz stereo music stem.
# The beds are not looped or stretched: they are re-seeked at each key impact so that a kick of the music
# lands exactly on the visual impact (the "chopped music" of the reference films), with a short silence
# before it, and the AVANT bed plunges ~30 dB after « à l'aveugle » before the world switch.
# usage: music_edit.py <avant.wav> <apres.wav> <out.wav> [--total 98.0]
import sys, json, subprocess, numpy as np
from scipy.signal import find_peaks

AVANT, APRES, OUT = sys.argv[1:4]
args = sys.argv[4:]
TOTAL = float(args[args.index('--total') + 1]) if '--total' in args else 98.0
SR = 48000

def decode(path):
    raw = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', path, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()

def kicks(x):
    """Kick / sub-drop attack times (s): coarse low-band (< 150 Hz) flux peaks, refined to the steepest rise
    of the low-passed envelope (± 2 ms)."""
    from scipy.signal import butter, sosfiltfilt
    m = x.mean(axis=1)
    hop, n = 256, 2048
    frames = np.lib.stride_tricks.sliding_window_view(np.pad(m, (n // 2, n)), n)[::hop]
    spec = np.abs(np.fft.rfft(frames * np.hanning(n), axis=1))
    low = spec[:, np.fft.rfftfreq(n, 1 / SR) < 150].sum(axis=1)
    flux = np.maximum(0, np.diff(low, prepend=low[0]))
    pk, _ = find_peaks(flux, height=flux.max() * 0.25, distance=int(0.2 * SR / hop))
    coarse = pk * hop / SR                                   # frames are centred
    env = np.abs(sosfiltfilt(butter(4, 150, 'low', fs=SR, output='sos'), m))
    w = int(0.004 * SR); env = np.convolve(env, np.ones(w) / w, 'same')
    d = np.diff(env, prepend=env[0])
    out = []
    for c in coarse:
        a, b = int(max(0, c - 0.06) * SR), int(min(len(m) / SR, c + 0.06) * SR)
        out.append((a + int(np.argmax(d[a:b]))) / SR if b > a else c)
    return np.array(out)

beds = {'avant': decode(AVANT), 'apres': decode(APRES)}
K = {k: kicks(v) for k, v in beds.items()}

# Placement plan. Each segment plays `bed` from src to src + (t1 - t0) at film [t0, t1).
# 'chop' events re-seek the bed at film time T so a kick lands exactly on T, after `pre` s of silence.
PLAN = [
    # bed, film start, source start
    ('avant', 0.0, 0.19),            # the bed's first sub drop (9.77 s) lands on « Non » (9.58)
    ('apres', 27.62, 0.04),          # bright world from the cut; its first kick lands on « It » (28.72)
]
CHOPS = [  # (film T, pre-silence s, source kick: None = nearest kick, float = snapped to the nearest kick, {'exact': s})
    (11.30, 0.28, {'exact': 9.772}),   # « 70 % » slam replays the bed's first sub drop (stutter edit)
    (19.90, 0.30, {'exact': 19.377}),  # f04 entry = the AVANT bed's third-section drop
    (32.23, 0.26, None),      # step pills slam
    (42.92, 0.28, None),      # « 30 s »
    (49.66, 0.28, None),      # « 100 % »
    (54.92, 0.30, None),      # « ×4 »
    (57.81, 0.30, None),      # « +36 % »
    (61.44, 0.22, None),      # Excel slam
    (91.84, 0.32, None),      # final « 70 % »
    (95.31, 0.26, 68.603),    # CTA click = the APRÈS bed's final hit, then its tail
]
DIPS = [  # (film T, depth dB, s before, s after) — breathing without re-seek
    (67.56, -9.0, 0.22, 0.05),   # friction alert
]
PLUNGE = (25.62, 0.12, -30.0)    # after « à l'aveugle »: -30 dB in 120 ms, held until the switch
FADE_OUT = (97.2, 98.0)

N = int(round(TOTAL * SR))
out = np.zeros((N, 2), np.float32)
log = []

BED_GAIN = {'avant': 10 ** (4 / 20), 'apres': 1.0}   # the AVANT bed is mixed ~10 dB softer by the model

def place(bed, t0, t1, src, fin=0.004, fout=0.012):
    x = beds[bed] * np.float32(BED_GAIN[bed])
    i0, i1 = int(round(t0 * SR)), min(N, int(round(t1 * SR)))
    s0 = int(round(src * SR))
    L = min(i1 - i0, len(x) - s0)
    if L <= 0:
        return
    seg = x[s0:s0 + L].copy()
    a = min(L, int(fin * SR)); seg[:a] *= np.linspace(0, 1, a)[:, None]
    b = min(L, int(fout * SR)); seg[-b:] *= np.linspace(1, 0, b)[:, None]
    out[i0:i0 + L] += seg
    log.append(dict(bed=bed, t0=round(t0, 3), t1=round(t0 + L / SR, 3), src=round(src, 3)))

# walk the timeline: per bed, segments are split at chop points
events = sorted(CHOPS)
for bi, (bed, start, src0) in enumerate(PLAN):
    end = PLAN[bi + 1][1] if bi + 1 < len(PLAN) else TOTAL
    t, offset = start, start - src0   # film = source + offset
    for T, pre, explicit in events:
        if not (start < T < end):
            continue
        place(bed, t, T - pre, t - offset)               # play up to the silence
        src_now = T - offset
        if isinstance(explicit, dict):
            k = explicit['exact']
        else:
            ref = explicit if explicit is not None else src_now   # a float = a section drop, snapped to its refined attack
            k = K[bed][np.argmin(np.abs(K[bed] - ref))]
        offset = T - k
        log.append(dict(chop=T, bed=bed, kick=round(float(k), 3), shift=round(float(k - src_now), 3)))
        t = T
    place(bed, t, end, t - offset, fout=0.02)

# gain automation: dips, plunge, fade
g = np.ones(N, np.float32)
tt = np.arange(N) / SR
for T, db, before, after in DIPS:
    lo = 10 ** (db / 20)
    m = (tt >= T - before) & (tt < T)
    g[m] = np.minimum(g[m], 1 + (lo - 1) * np.clip((tt[m] - (T - before)) / 0.04, 0, 1))
    m2 = (tt >= T) & (tt < T + after)
    g[m2] = np.minimum(g[m2], lo + (1 - lo) * (tt[m2] - T) / after)
p0, pd, pdb = PLUNGE
lo = 10 ** (pdb / 20)
m = (tt >= p0) & (tt < 27.62)
g[m] = np.minimum(g[m], 1 + (lo - 1) * np.clip((tt[m] - p0) / pd, 0, 1))
f0, f1 = FADE_OUT
m = tt >= f0
g[m] *= np.clip(1 - (tt[m] - f0) / (f1 - f0), 0, 1) ** 2
out *= g[:, None]

subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-',
                '-c:a', 'pcm_s24le', OUT], input=np.ascontiguousarray(out).tobytes(), check=True)
json.dump(log, open(OUT.rsplit('.', 1)[0] + '_edit.json', 'w'), indent=1)
for e in log:
    print(e)
