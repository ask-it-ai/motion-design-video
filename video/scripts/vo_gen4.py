# Generate new takes for selected lines only (v4), STT-check them and measure the "pourcent" words.
# usage: python3 -I vo_gen4.py <workdir> <takes> L02 L08 ...
import base64, json, os, re, sys, time, urllib.request, urllib.error, subprocess
WORK, TAKES, IDS = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
KEY = os.environ.get('ELEVENLABS_API_KEY') or open(os.path.join(os.path.dirname(WORK), 'secrets', 'elevenlabs.key')).read().strip()
VOICES = {'N': 'a5n9pJUnAhX4fn7lx3uo', 'V': 'O31r762Gb3WFygrEOGh0'}
SETTINGS = {'N': {'stability': 0.5, 'similarity_boost': 0.75}, 'V': {'stability': 0.45, 'similarity_boost': 0.75}}
API = 'https://api.elevenlabs.io'
def post_json(path, payload):
    req = urllib.request.Request(API + path, data=json.dumps(payload).encode(), headers={'xi-api-key': KEY, 'Content-Type': 'application/json'})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=180) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:300]
            if e.code in (429, 500, 502, 503) and attempt < 3: time.sleep(2 ** attempt * 2); continue
            raise RuntimeError(f'{e.code} {body}')
def stt(path):
    out = subprocess.run(['curl', '-sS', '--max-time', '200', '-X', 'POST', API + '/v1/speech-to-text', '-H', f'xi-api-key: {KEY}',
                          '-F', 'model_id=scribe_v2', '-F', f'file=@{path}', '-F', 'language_code=fra', '-F', 'tag_audio_events=false',
                          '-F', 'timestamps_granularity=word'], capture_output=True, text=True)
    return json.loads(out.stdout)
lines = json.load(open(os.path.join(WORK, 'lines.json')))
idx = {l['id']: i for i, l in enumerate(lines)}
for lid in IDS:
    i = idx[lid]; ln = lines[i]
    prev_t = re.sub(r'\[[^\]]*\]\s*', '', lines[i - 1]['text'])[-280:] if i > 0 else None
    next_t = re.sub(r'\[[^\]]*\]\s*', '', lines[i + 1]['text'])[:280] if i + 1 < len(lines) else None
    for k in range(TAKES):
        base = os.path.join(WORK, 'takes', f"{lid}_t{k + 1}")
        if not os.path.exists(base + '.mp3'):
            payload = {'text': ln['text'], 'model_id': 'eleven_v4', 'language_code': 'fr', 'voice_settings': SETTINGS[ln['spk']], 'seed': 4000 + 31 * k + i}
            if prev_t: payload['previous_text'] = prev_t
            if next_t: payload['next_text'] = next_t
            res = post_json(f"/v1/text-to-speech/{VOICES[ln['spk']]}/with-timestamps?output_format=mp3_44100_192", payload)
            open(base + '.mp3', 'wb').write(base64.b64decode(res['audio_base64']))
            json.dump({'alignment': res.get('alignment'), 'normalized_alignment': res.get('normalized_alignment')}, open(base + '.align.json', 'w'))
        if not os.path.exists(base + '.stt.json'):
            json.dump(stt(base + '.mp3'), open(base + '.stt.json', 'w'))
        s = json.load(open(base + '.stt.json')); al = json.load(open(base + '.align.json'))['alignment']
        # character alignment: locate every "pourcent" and the word before it
        chars = al['characters']; st = al['character_start_times_seconds']; en = al['character_end_times_seconds']
        text = ''.join(chars); notes = []
        for m in re.finditer('pourcent', text):
            a, b = m.start(), m.end() - 1
            j = a - 1
            while j >= 0 and chars[j] == ' ': j -= 1
            gap = st[a] - en[j]
            notes.append(f"'{text[max(0, a - 14):a].strip()}'→pourcent: gap {gap * 1000:.0f} ms, dur {(en[b] - st[a]) * 1000:.0f} ms")
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base + '.mp3'], capture_output=True, text=True).stdout or 0)
        words = [w for w in s.get('words', []) if w.get('type') == 'word']
        pct = [f"{words[q-1]['text']}[{words[q-1]['end']:.2f}] {w['text']}[{w['start']:.2f}-{w['end']:.2f}]" for q, w in enumerate(words) if q and ('%' in w['text'] or 'cent' in w['text'].lower())]
        print(f"{lid} t{k + 1} {dur:.2f}s | STT: {s.get('text', '')[:120]}")
        print('    align:', '; '.join(notes)); print('    stt  :', '; '.join(pct))
