# v4 mix: VO + SFX cue sheet + music stem (music_edit.py) -> stereo 48 kHz master.
# The SFX bus ducks 4 dB under the voice; the music bus is carved (-3 dB presence dip) and ducks 6 dB under the
# voice, its base level sitting MUSIC_REL dB under the voice's loudness, so it plays ~15 dB under speech.
# usage: mix4.py <scratchpad> <vo.wav> <cues.json> <music.wav> <out_dir> [--total 98.0] [--lufs -14]
import sys, os, json, subprocess, numpy as np
SP, VO, CUES, MUSIC, OUT = sys.argv[1:6]
args = sys.argv[6:]
TOTAL = float(args[args.index('--total')+1]) if '--total' in args else 98.0
LUFS = float(args[args.index('--lufs')+1]) if '--lufs' in args else -14.0
SR = 48000
PREP = os.path.join(SP, 'sfx', 'prep')
meta = json.load(open(os.path.join(PREP, 'meta.json')))
os.makedirs(OUT, exist_ok=True)

def ff_decode(path, ch):
    raw = subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',path,'-ac',str(ch),'-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, ch).copy()
def ff_write(path, x):
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','f32le','-ar',str(SR),'-ac',str(x.shape[1]),'-i','-','-c:a','pcm_s24le',path], input=np.ascontiguousarray(x, dtype=np.float32).tobytes(), check=True)
def ff_filter(x, af):
    p = subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-f','f32le','-ar',str(SR),'-ac',str(x.shape[1]),'-i','-','-af',af,'-f','f32le','-'], input=np.ascontiguousarray(x, dtype=np.float32).tobytes(), capture_output=True, check=True)
    return np.frombuffer(p.stdout, dtype=np.float32).reshape(-1, x.shape[1]).copy()

N = int(round(TOTAL*SR))
# --- voice: HPF + gentle compression, placed at 0 (vo.wav already carries its pre-roll)
vo = ff_decode(VO, 1)
vo = ff_filter(vo, 'highpass=f=70:poles=2,acompressor=threshold=0.1:ratio=2:attack=10:release=150:knee=3:makeup=1')
vo_bus = np.zeros((N, 2), np.float32)
L = min(N, len(vo)); vo_bus[:L] = vo[:L] * np.float32(1.0)

# --- sfx bus
def load_sfx(name, pitch=0.0, rev=False, trim=None):
    y = np.load(os.path.join(PREP, f'{name}.npy'))
    hit = meta[name]['hit']
    if trim:  # keep [a, b] seconds of the prepared file
        a, b = trim; y = y[int(a*SR):int(b*SR)].copy(); hit = max(0.0, hit - a)
        fo = min(len(y), int(0.02*SR)); y[-fo:] *= np.linspace(1, 0, fo)[:, None]
    if rev:
        y = y[::-1].copy(); hit = len(y)/SR - hit
    if pitch:
        r = 2**(pitch/12)  # resample: higher pitch -> shorter
        n2 = int(len(y)/r); idx = np.arange(n2)*r
        y = np.stack([np.interp(idx, np.arange(len(y)), y[:, c]) for c in range(2)], 1).astype(np.float32)
        hit = hit / r
    return y, hit
cues = json.load(open(CUES))
sfx_bus = np.zeros((N, 2), np.float32)
placed = []
for c in cues:
    y, hit = load_sfx(c['sfx'], c.get('pitch', 0), c.get('rev', False), c.get('trim'))
    t0 = c['t'] - (hit if c.get('align', 'hit') == 'hit' else 0.0)
    g = 10**(c['gain']/20)
    pan = c.get('pan', 0.0)  # -1..1 equal-power
    gl, gr = np.cos((pan+1)*np.pi/4)*np.sqrt(2), np.sin((pan+1)*np.pi/4)*np.sqrt(2)
    i0 = int(round(t0*SR)); j0 = max(0, -i0); i0 = max(0, i0)
    seg = y[j0:]; L = min(len(seg), N - i0)
    if L <= 0: continue
    sfx_bus[i0:i0+L, 0] += seg[:L, 0]*g*gl; sfx_bus[i0:i0+L, 1] += seg[:L, 1]*g*gr
    placed.append(dict(c, start=round(t0, 3)))
# --- duck the sfx bus under the voice (envelope follower, 4 dB when the voice speaks)
env = np.abs(vo_bus[:, 0]); fr = 480
blocks = env[:len(env)//fr*fr].reshape(-1, fr).max(axis=1)
active = (20*np.log10(blocks+1e-9) > -38).astype(np.float32)
# attack 30 ms, release 250 ms on the block grid (10 ms)
g = np.ones_like(active); duck = 10**(-float(os.environ.get('DUCK_DB', '4'))/20); cur = 1.0
for i, a in enumerate(active):
    tgt = duck if a else 1.0
    k = 0.33 if tgt < cur else 0.04
    cur += (tgt - cur)*k; g[i] = cur
gs = np.repeat(g, fr); gs = np.concatenate([gs, np.full(N-len(gs), gs[-1] if len(gs) else 1.0)])[:N]
sfx_bus *= gs[:, None].astype(np.float32)
# --- music bus: presence carve + duck under the voice, base level relative to the voice loudness
def lufs_of(x):
    p = subprocess.run(['ffmpeg','-hide_banner','-nostats','-f','f32le','-ar',str(SR),'-ac',str(x.shape[1]),'-i','-','-af','ebur128','-f','null','-'],
                       input=np.ascontiguousarray(x, dtype=np.float32).tobytes(), capture_output=True)
    e = p.stderr.decode(); tail = e[e.rindex('Summary:'):]
    return float(tail.split('I:')[1].split('LUFS')[0])
mu = ff_decode(MUSIC, 2)
mu = ff_filter(mu, 'equalizer=f=2500:t=q:w=1.0:g=-3,equalizer=f=250:t=q:w=1.2:g=-1.5')
mus_bus = np.zeros((N, 2), np.float32); L = min(N, len(mu)); mus_bus[:L] = mu[:L]
rel = float(os.environ.get('MUSIC_REL', '-9'))
vo_l, mu_l = lufs_of(vo_bus), lufs_of(mus_bus)
mus_bus *= np.float32(10**((vo_l + rel - mu_l)/20))
g2 = np.ones_like(active); duck2 = 10**(-float(os.environ.get('MUSIC_DUCK_DB', '6'))/20); cur = 1.0
for i, a in enumerate(active):
    tgt = duck2 if a else 1.0
    k = 0.25 if tgt < cur else 0.03          # attack ~40 ms, release ~350 ms on the 10 ms grid
    cur += (tgt - cur)*k; g2[i] = cur
gm = np.repeat(g2, fr); gm = np.concatenate([gm, np.full(N-len(gm), gm[-1] if len(gm) else 1.0)])[:N]
mus_bus *= gm[:, None].astype(np.float32)
print(f'voice {vo_l:.1f} LUFS, music raw {mu_l:.1f} LUFS -> placed {rel:+.0f} LU under the voice, ducked {os.environ.get("MUSIC_DUCK_DB", "6")} dB under speech')
mix = vo_bus + sfx_bus + mus_bus
ff_write(os.path.join(OUT, 'stem_vo.wav'), vo_bus); ff_write(os.path.join(OUT, 'stem_sfx.wav'), sfx_bus); ff_write(os.path.join(OUT, 'stem_music.wav'), mus_bus)
pre = os.path.join(OUT, 'premaster.wav'); ff_write(pre, mix)
# --- master: static gain to target, oversampled peak limiter at -1.2 dBFS, verify integrated + true peak
def measure(path):
    e = subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',path,'-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    tail = e[e.rindex('Summary:'):]
    I = float(tail.split('I:')[1].split('LUFS')[0]); TP = float(tail.split('Peak:')[1].split('dBFS')[0])
    LRA = float(tail.split('LRA:')[1].split('LU')[0])
    return I, TP, LRA
I0, TP0, LRA0 = measure(pre); print('premaster', I0, 'LUFS', TP0, 'dBTP', 'LRA', LRA0)
gain = LUFS - I0
for it in range(3):
    af = f'volume={gain:.2f}dB,aresample=192000,alimiter=limit=0.87:attack=1.5:release=60:level=false,aresample={SR}'
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',pre,'-af',af,'-c:a','pcm_s24le',os.path.join(OUT,'master.wav')],check=True)
    I, TP, LRA = measure(os.path.join(OUT,'master.wav'))
    print(f'  iter {it}: gain {gain:+.2f} dB -> {I} LUFS, TP {TP} dBTP, LRA {LRA}')
    if abs(I - LUFS) < 0.15: break
    gain += LUFS - I
json.dump(placed, open(os.path.join(OUT, 'placed.json'), 'w'), indent=1)
print('cues placed:', len(placed))
