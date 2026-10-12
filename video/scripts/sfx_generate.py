# Generate the SFX library with ElevenLabs text-to-sound (v2). Usage: python3 -I sfx_generate.py <sfx_dir>
import json, os, sys, urllib.request, urllib.error, time, concurrent.futures as cf
D = sys.argv[1]
# API key: env ELEVENLABS_API_KEY, else a local secrets file next to the work dir (never committed)
KEY = os.environ.get('ELEVENLABS_API_KEY') or open(os.path.join(os.path.dirname(D), 'secrets', 'elevenlabs.key')).read().strip()
lib = json.load(open(os.path.join(D, 'library.json')))
os.makedirs(os.path.join(D, 'raw'), exist_ok=True)
jobs = [(s, k) for s in lib for k in range(1, s['n'] + 1)]
def gen(job):
    s, k = job
    out = os.path.join(D, 'raw', f"{s['id']}_v{k}.mp3")
    if os.path.exists(out) and os.path.getsize(out) > 1000: return out, 'cached'
    body = json.dumps({'text': s['text'], 'duration_seconds': s['d'], 'prompt_influence': s['pi'], 'model_id': 'eleven_text_to_sound_v2'}).encode()
    req = urllib.request.Request('https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_192', data=body,
                                 headers={'xi-api-key': KEY, 'Content-Type': 'application/json'})
    for a in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                open(out, 'wb').write(r.read()); return out, 'ok'
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:200]
            if e.code in (429, 500, 502, 503) and a < 3: time.sleep(3 * (a + 1)); continue
            return out, f'ERR {e.code} {msg}'
with cf.ThreadPoolExecutor(4) as ex:
    for out, st in ex.map(gen, jobs): print(os.path.basename(out), st, flush=True)
