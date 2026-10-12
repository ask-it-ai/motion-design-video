# Ask-it — explainer v3 (HyperFrames)

1920×1080, 30 fps, 105.5 s. Voice-over by Martin Dupont (narrator) and Victoria (the visitor), on Endro as the showcase brand.

- `frame.md`: design truth, covering the palette, type, components and layout constants.
- `STORYBOARD.md`: the 10 scenes, with local voice cues for each one.
- `compositions/fNN-*.html`: one sub-composition per scene, mounted by `index.html` at the voice-over line starts.
- `index.html`: the scene slots, the root-level transitions (placed in the voice pauses) and the soundtrack.

## Not in git

The `assets/` folder stays local: brand captures and packshots, personas, licensed fonts, and the generated audio. It is ignored on purpose because the repository is public.

## Audio pipeline

Scripts are in `scripts/` and their inputs in `audio-src/`. The ElevenLabs key is read from `ELEVENLABS_API_KEY`.

1. `vo_generate.py` → `vo_assemble.py`
   - Line-by-line Eleven v4 takes, checked with speech-to-text.
   - Pause compression, then the narrator at a tempo of 1.04.
   - Output: `assets/audio/vo.wav` and `vo_timeline.json`.
2. `sfx_generate.py` → `sfx_prep.py`
   - The sound-effect library (`audio-src/sfx_library.json`).
   - The chosen variants are trimmed, high-passed and peak-normalized.
   - The hit offset of each sound is stored in `audio-src/sfx_prep_meta.json`.
3. `cues_gen.py` → `mix.py` → `mix_qc.py`
   - The cue sheet sets each cue on the visual event its sound must hit.
   - The effects bus is ducked by 4 dB under the voice.
   - Master: −14 LUFS integrated, −1 dBTP.
   - QC measures how far the effects sit under the voice.

## Transitions with a lead-in

`scripts/lead_pad.py compositions/<scene>.html <seconds>` delays a scene's own timeline inside a wrapper. A root push or blur can then show the scene during the pause before its first cue, without moving any cue against the voice.

Current pads:

| Scene | Pad |
| --- | --- |
| f07 | 0.35 s |
| f08 | 0.30 s |
| f09 | 0.40 s |
| f10 | 0.40 s |

## Render

```bash
HYPERFRAMES_BROWSER_PATH=/path/to/chrome-headless-shell npx hyperframes check
npx hyperframes render . -q delivery -o renders/ask-it-v3.mp4
```
