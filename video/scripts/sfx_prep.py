# Decode chosen SFX variants -> 48 kHz stereo float32 .npy + 24-bit WAV, trimmed and peak-normalized.
# Also writes a waveform/spectrogram contact sheet for visual QC.
import sys, os, json, subprocess, numpy as np
from PIL import Image, ImageDraw
SP = sys.argv[1]
RAW = os.path.join(SP, 'sfx', 'raw'); OUT = os.path.join(SP, 'sfx', 'prep')
SR = 48000
# chosen variant per sound, plus highpass (Hz) to keep the low end for the voice; 0 = none
PICK = {
 'ui_tap': ('v1', 120), 'ui_select': ('v1', 200), 'swipe': ('v1', 150), 'whoosh_soft': ('v2', 60),
 'whoosh_fast': ('v2', 80), 'pop': ('v2', 100), 'chip_fly': ('v1', 120), 'tab_close': ('v2', 60),
 'dots_fade': ('v2', 80), 'counter_tick': ('v2', 300), 'number_slam': ('v2', 0), 'ember_burn': ('v1', 80),
 'muffle_drone': ('v1', 0), 'rewind': ('v1', 100), 'color_flood': ('v1', 80), 'logo_sting': ('v2', 80),
 'success': ('v2', 120), 'paper_crumple': ('v1', 150), 'typing': ('v1', 200), 'notif': ('v1', 200),
 'timer': ('v1', 200), 'sparkle': ('v1', 400), 'skin_swap': ('v1', 120), 'cart_add': ('v1', 120),
}
def decode(f, hp):
    af = [f'aresample={SR}']
    if hp: af.append(f'highpass=f={hp}:poles=2')
    raw = subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',f,'-af',','.join(af),'-ac','2','-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()
def env_db(x, fr=240):
    m = np.abs(x).max(axis=1); n = len(m)//fr
    return 20*np.log10(m[:n*fr].reshape(n, fr).max(axis=1) + 1e-9), fr
meta = {}
sheet = []
for name, (var, hp) in PICK.items():
    x = decode(os.path.join(RAW, f'{name}_{var}.mp3'), hp)
    db, fr = env_db(x)
    pk = db.max()
    on = np.where(db > pk - 40)[0]
    a = max(0, on[0]*fr - int(0.004*SR))
    # tail: last block above peak-50 dB, plus 40 ms
    b = min(len(x), (on[-1]+1)*fr + int(0.04*SR))
    y = x[a:b].copy()
    fi = min(len(y), int(0.003*SR)); y[:fi] *= np.linspace(0, 1, fi)[:, None]
    fo = min(len(y), int(0.03*SR)); y[-fo:] *= np.linspace(1, 0, fo)[:, None]
    g = 10**(-1/20) / (np.abs(y).max() + 1e-12)
    y *= g
    np.save(os.path.join(OUT, f'{name}.npy'), y.astype(np.float32))
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-','-c:a','pcm_s24le',os.path.join(OUT, f'{name}.wav')], input=y.astype(np.float32).tobytes())
    rms = 20*np.log10(np.sqrt(np.mean(y**2)) + 1e-9)
    e2, fr2 = env_db(y, 240)
    hit = float(np.argmax(e2)*fr2/SR)
    meta[name] = dict(var=var, hp=hp, dur=round(len(y)/SR, 3), gain_db=round(float(20*np.log10(g)), 1), rms_db=round(float(rms), 1),
                      lead_trim=round(float(a/SR), 3), hit=round(hit, 3))
    # waveform strip
    W, H = 600, 70
    im = Image.new('RGB', (W+160, H), (20, 20, 20)); d = ImageDraw.Draw(im)
    mono = np.abs(y).max(axis=1); step = max(1, len(mono)//W)
    for i in range(min(W, len(mono)//step)):
        v = mono[i*step:(i+1)*step].max(); h = int(v*(H/2-2))
        d.line([(160+i, H//2-h), (160+i, H//2+h)], fill=(240, 120, 70))
    d.text((4, 4), f'{name} {var}', fill=(255, 255, 255)); d.text((4, 24), f'{len(y)/SR:.2f}s g{20*np.log10(g):+.0f}dB', fill=(180, 180, 180))
    d.text((4, 44), f'rms {rms:.0f}dB', fill=(180, 180, 180))
    sheet.append(im)
H = sum(i.height for i in sheet); S = Image.new('RGB', (760, H)); yy = 0
for i in sheet: S.paste(i, (0, yy)); yy += i.height
S.save(os.path.join(SP, 'sfx', 'contact.png'))
json.dump(meta, open(os.path.join(OUT, 'meta.json'), 'w'), indent=1)
for k, v in meta.items(): print(f'{k:14s} {v}')
