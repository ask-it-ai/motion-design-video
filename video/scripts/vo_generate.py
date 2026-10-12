# Generate the v3 voice-over line by line with Eleven v4 (with timestamps),
# QC each take with speech-to-text, keep the best take per line.
# Usage: python3 -I vo_generate.py <workdir> <takes>
import base64, json, os, re, sys, time, unicodedata, urllib.request, urllib.error, subprocess

WORK = sys.argv[1]
TAKES = int(sys.argv[2]) if len(sys.argv) > 2 else 2
# API key: env ELEVENLABS_API_KEY, else a local secrets file next to the work dir (never committed)
KEY = os.environ.get('ELEVENLABS_API_KEY') or open(os.path.join(os.path.dirname(WORK), 'secrets', 'elevenlabs.key')).read().strip()
VOICES = {'N': 'a5n9pJUnAhX4fn7lx3uo',   # Martin Dupont - Deep, Warm and Aged
          'V': 'O31r762Gb3WFygrEOGh0'}   # Victoria - Content Creator
SETTINGS = {'N': {'stability': 0.5, 'similarity_boost': 0.75},
            'V': {'stability': 0.45, 'similarity_boost': 0.75}}
API = 'https://api.elevenlabs.io'

def post_json(path, payload):
    req = urllib.request.Request(API + path, data=json.dumps(payload).encode(),
                                 headers={'xi-api-key': KEY, 'Content-Type': 'application/json'})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:400]
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 ** attempt * 2); continue
            raise RuntimeError(f'{e.code} {body}')

def stt(path):
    out = subprocess.run(['curl', '-sS', '--max-time', '200', '-X', 'POST', API + '/v1/speech-to-text',
                          '-H', f'xi-api-key: {KEY}', '-F', 'model_id=scribe_v2', '-F', f'file=@{path}',
                          '-F', 'language_code=fra', '-F', 'tag_audio_events=false',
                          '-F', 'timestamps_granularity=word'], capture_output=True, text=True)
    return json.loads(out.stdout)

def norm_words(t):
    t = re.sub(r'\[[^\]]*\]', ' ', t)
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = t.replace("'", ' ').replace('’', ' ').replace('-', ' ')
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    # spoken numbers that STT may write as digits
    t = t.replace('70', 'soixante dix').replace('36', 'trente six').replace('30', 'trente')
    t = re.sub(r'\bpour cent\b', 'pourcent', t).replace('%', ' pourcent ')
    t = re.sub(r'\b(hmm+|mh+|hum+|euh+)\b', ' ', t)
    return t.split()

def wer(ref, hyp):
    d = list(range(len(hyp) + 1))
    for i in range(1, len(ref) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(hyp) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (ref[i - 1] != hyp[j - 1]))
            prev = cur
    return d[len(hyp)] / max(1, len(ref))

lines = json.load(open(os.path.join(WORK, 'lines.json')))
os.makedirs(os.path.join(WORK, 'takes'), exist_ok=True)
report = []
for i, ln in enumerate(lines):
    prev_t = re.sub(r'\[[^\]]*\]\s*', '', lines[i - 1]['text'])[-280:] if i > 0 else None
    next_t = re.sub(r'\[[^\]]*\]\s*', '', lines[i + 1]['text'])[:280] if i + 1 < len(lines) else None
    ref = norm_words(ln['text'])
    takes = []
    for k in range(TAKES):
        base = os.path.join(WORK, 'takes', f"{ln['id']}_t{k + 1}")
        if not os.path.exists(base + '.mp3'):
            payload = {'text': ln['text'], 'model_id': 'eleven_v4', 'language_code': 'fr',
                       'voice_settings': SETTINGS[ln['spk']], 'seed': 1000 + 17 * k + i}
            if prev_t: payload['previous_text'] = prev_t
            if next_t: payload['next_text'] = next_t
            try:
                res = post_json(f"/v1/text-to-speech/{VOICES[ln['spk']]}/with-timestamps?output_format=mp3_44100_192", payload)
            except RuntimeError as e:
                if 'previous_text' in str(e) or 'next_text' in str(e) or 'not supported' in str(e).lower():
                    payload.pop('previous_text', None); payload.pop('next_text', None)
                    res = post_json(f"/v1/text-to-speech/{VOICES[ln['spk']]}/with-timestamps?output_format=mp3_44100_192", payload)
                else:
                    raise
            open(base + '.mp3', 'wb').write(base64.b64decode(res['audio_base64']))
            json.dump({'alignment': res.get('alignment'), 'normalized_alignment': res.get('normalized_alignment')},
                      open(base + '.align.json', 'w'))
        if not os.path.exists(base + '.stt.json'):
            json.dump(stt(base + '.mp3'), open(base + '.stt.json', 'w'))
        s = json.load(open(base + '.stt.json'))
        hyp = norm_words(s.get('text', ''))
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                    base + '.mp3'], capture_output=True, text=True).stdout.strip() or 0)
        takes.append({'take': k + 1, 'wer': round(wer(ref, hyp), 3), 'dur': round(dur, 2), 'stt': s.get('text', '')})
    best = sorted(takes, key=lambda t: (t['wer'] > 0.08, t['wer'], t['dur']))[0]
    report.append({'id': ln['id'], 'spk': ln['spk'], 'best': best['take'], 'takes': takes})
    print(ln['id'], ln['spk'], ' | '.join(f"t{t['take']}: wer={t['wer']} dur={t['dur']}s" for t in takes), '-> best t%d' % best['take'], flush=True)
json.dump(report, open(os.path.join(WORK, 'takes_report.json'), 'w'), ensure_ascii=False, indent=1)
