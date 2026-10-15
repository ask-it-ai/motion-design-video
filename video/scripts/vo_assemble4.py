# Assemble the chosen takes into one VO track with controlled gaps and build a word-level timeline.
# Usage: python3 -P vo_assemble.py <workdir> <out_wav> <out_json> L01=2 L02=2 ...
import json, os, subprocess, sys
import numpy as np

work, out_wav, out_json = sys.argv[1:4]
picks = dict(a.split('=') for a in sys.argv[4:])
lines = json.load(open(os.path.join(work, 'lines.json')))
SR = 48000

TEMPO = {'N': 1.06, 'V': 1.03}  # v4: tighter delivery to stay under 100 s, pitch and formants preserved

def load(path, tempo=1.0):
    af = ['-af', f'rubberband=tempo={tempo}:formant=preserved:pitchq=quality'] if tempo != 1.0 else []
    raw = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', path, *af, '-ac', '1', '-ar', str(SR),
                          '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()

def trim_bounds(x):
    fr = int(0.01 * SR); n = len(x) // fr
    db = 20 * np.log10(np.sqrt(np.mean(x[:n * fr].reshape(n, fr) ** 2, axis=1)) + 1e-9)
    thr = db.max() - 42
    on = np.where(db > thr)[0]
    a = max(0, (on[0] - 4) * fr)            # 40 ms before first energy
    b = min(len(x), (on[-1] + 12) * fr)     # 120 ms natural tail
    return a, b

def compress_pauses(seg, words, spk):
    """Shorten silences between words: cut the quietest stretch inside each long gap (10 ms crossfades).
    Returns the new segment and the word list with shifted times."""
    xf = int(0.010 * SR)
    fr = int(0.005 * SR)
    out = []; cursor = 0; shift = 0.0; new_words = []
    for i, w in enumerate(words):
        ws, we = w['start'] - shift, w['end'] - shift
        new_words.append(dict(w, start=ws, end=we))
        if i + 1 == len(words): break
        gap = words[i + 1]['start'] - w['end']
        txt = w['text']
        end_sent = txt.endswith(('.', '?', '!', ':')) or txt in ('?', '!', ':')
        if spk == 'V':
            target = 0.50 if end_sent else 0.28
        else:
            target = 0.34 if end_sent else 0.17
        excess = gap - target
        if excess < 0.06: continue
        g0 = int((w['end'] + 0.06) * SR); g1 = int((words[i + 1]['start'] - 0.06) * SR)
        cut = int(excess * SR)
        if g1 - g0 <= cut + 2 * xf: cut = max(0, g1 - g0 - 2 * xf)
        if cut <= 0: continue
        # quietest window of length `cut` inside [g0, g1]
        region = seg[g0:g1]
        n = len(region) // fr
        e = np.convolve((region[:n * fr].reshape(n, fr) ** 2).mean(axis=1), np.ones(max(1, cut // fr)), 'valid')
        c0 = g0 + int(np.argmin(e)) * fr
        c1 = c0 + cut
        out.append(seg[cursor:c0 + xf].copy())
        # crossfade tail of kept part with head after the cut
        a_ = out[-1][-xf:]; b_ = seg[c1:c1 + xf]
        ramp = np.linspace(0, 1, xf, dtype=np.float32)
        out[-1][-xf:] = a_ * (1 - ramp) + b_ * ramp
        cursor = c1 + xf
        shift += (c1 - c0) / SR
    out.append(seg[cursor:])
    return np.concatenate(out), new_words

track = []; t = 0.0; timeline = {'sample_rate': SR, 'lines': [], 'words': []}
for ln in lines:
    k = picks[ln['id']]
    base = os.path.join(work, 'takes', f"{ln['id']}_t{k}")
    tempo = TEMPO[ln['spk']]
    x = load(base + '.mp3', tempo)
    a, b = trim_bounds(x)
    seg = x[a:b]
    stt = json.load(open(base + '.stt.json'))
    rel = []
    for w in stt.get('words', []):
        if w.get('type') != 'word': continue
        ws, we = w['start'] / tempo - a / SR, w['end'] / tempo - a / SR
        if rel and (w['text'].strip() in ('%', '?', '!', ':', ';', '…') or w['text'].startswith('%')):
            rel[-1]['end'] = max(rel[-1]['end'], we); rel[-1]['text'] += ' ' + w['text']; continue
        if we > 0: rel.append(dict(text=w['text'], start=ws, end=we))
    # explicit cuts (take-time seconds) before pause compression: drop the span, crossfade 30 ms, shift later words
    for c0, c1 in sorted(ln.get('cuts', []), reverse=True):
        i0, i1 = int((c0 / tempo) * SR) - a, int((c1 / tempo) * SR) - a
        xf2 = int(0.03 * SR)
        head, tail = seg[:i0 + xf2].copy(), seg[i1:]
        ramp = np.linspace(0, 1, xf2, dtype=np.float32)
        head[-xf2:] = head[-xf2:] * (1 - ramp) + tail[:xf2] * ramp
        seg = np.concatenate([head, tail[xf2:]])
        span = (i1 - i0) / SR
        rel = [w for w in rel if w['end'] <= i0 / SR or w['start'] >= i1 / SR]
        rel = [dict(w, start=w['start'] - span, end=w['end'] - span) if w['start'] >= i1 / SR else w for w in rel]
    before = len(seg) / SR
    seg, rel = compress_pauses(seg, rel, ln['spk'])
    fade = int(0.008 * SR)
    seg[:fade] *= np.linspace(0, 1, fade); seg[-fade:] *= np.linspace(1, 0, fade)
    start = t; dur = len(seg) / SR
    print(f"  {ln['id']}: {before:5.2f}s -> {dur:5.2f}s")
    for w in rel:
        if w['end'] < 0 or w['start'] > dur: continue
        timeline['words'].append({'line': ln['id'], 'spk': ln['spk'], 'w': w['text'],
                                  'start': round(start + max(0, w['start']), 3), 'end': round(start + min(dur, w['end']), 3)})
    timeline['lines'].append({'id': ln['id'], 'spk': ln['spk'], 'sec': ln['sec'], 'take': int(k),
                              'start': round(start, 3), 'end': round(start + dur, 3), 'text': ln['text']})
    track.append(seg)
    gap = ln['gap_after']
    if gap > 0: track.append(np.zeros(int(gap * SR), dtype=np.float32))
    t = start + dur + gap

y = np.concatenate(track)
y = y / max(1e-6, np.abs(y).max()) * 0.89          # headroom before loudness pass
lead = np.zeros(int(0.4 * SR), dtype=np.float32)    # 0.4 s pre-roll for the opening shot
y = np.concatenate([lead, y, np.zeros(int(0.3 * SR), dtype=np.float32)])
for l in timeline['lines']: l['start'] = round(l['start'] + 0.4, 3); l['end'] = round(l['end'] + 0.4, 3)
for w in timeline['words']: w['start'] = round(w['start'] + 0.4, 3); w['end'] = round(w['end'] + 0.4, 3)
timeline['duration'] = round(len(y) / SR, 3)
raw = out_wav + '.raw.f32'
y.astype(np.float32).tofile(raw)
subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', raw,
                '-c:a', 'pcm_s24le', out_wav], check=True)
os.remove(raw)
json.dump(timeline, open(out_json, 'w'), ensure_ascii=False, indent=1)
print('duration', timeline['duration'], 's;', len(timeline['words']), 'words')
for l in timeline['lines']: print(f"{l['id']} {l['spk']} {l['sec']} {l['start']:7.2f} -> {l['end']:7.2f}")
