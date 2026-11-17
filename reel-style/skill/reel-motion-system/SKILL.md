---
name: reel-motion-system
description: Approved house style and motion system for 9:16 Instagram/short-form reel motion graphics (1080x1920) - grey halftone canvas, single blue accent, Inter Display two-tier type, rounded cards, eased camera moves, connected transitions, and text motion curves measured from a reference edit. Use for ANY request to design still frames, animate a beat, plan motion graphics for a script, edit or extend reel graphics, render reel animations, or review whether a reel frame follows the style - including real-estate/property reels, brand-documentary edits, and Hinglish voiceover scripts. Includes ready templates, a frame-accurate renderer with real motion blur, reference-analysis tools, and a QA checklist.
---

# Reel motion system

This skill is the user's **approved** style. Follow it exactly; don't improvise a new look. The full rules are in `references/RULEBOOK.md`: **read it before designing or animating anything.** `references/CONVERSATION.md` is the session where every rule was agreed; check it when you need the reason behind a rule.

## Non-negotiables (summary; RULEBOOK.md has the detail)
1. **Look:** light grey vignette canvas + halftone dot grain, one accent (`#1f5fff` → `#22b8f0`), Inter Display, rounded cards, fixed corner brackets.
2. **Two-tier contrast on every line:** setup words light (300), grey and smaller; the **key word** extra-bold (800), large and in the blue gradient.
3. **Layout:** text only in y 220–1440 and x 80–940. Footer and right edge clear. One focal point per frame, chosen per script line (top, middle or bottom). **No text overlaps anything.** Small labels become icons.
4. **Motion:** nothing linear; no dead frames; transitions connect (whip, carried element, match cut, zoom-through); consistent direction; anticipation, follow-through and arcs.
5. **Text motion (measured):** words rise 36px over 0.45 s on `cubic-bezier(.2,.3,0,.8)`, blur/opacity clear first in 0.2 s; key word 0.75 s on `cubic-bezier(.3,.65,.45,.85)`, then breathes +2.5%; stagger 0.17 s. **No bounce or squash on text.** Squash and stretch are for shapes only.
6. **Sound:** none. Sound is not approved until the user provides their sound guide.
7. Real footage or photos over generated images; generated images are placeholders only.

## Workflow
1. Read `references/RULEBOOK.md`. For a script, pick the 3–4 moments where a graphic explains something better than footage, and propose them before building.
2. **Start from a template** in `templates/` (`balcony.html`, `location.html`, `pricing.html`). Each one already has the canvas, grain, brackets, self-hosted fonts (`templates/assets/fonts.css`) and ease tokens. Copy the closest one; keep new beats inside `templates/` so the relative `assets/` paths keep working.
3. If the beat follows another beat, make its first frame match the previous beat's last frame (a carried element or the same frame).
4. Preview, check, then final render (below). Run the QA checklist (RULEBOOK §9) before sending anything.
5. Deliver silent MP4s; say what's open (real assets, facts to confirm).

## Rendering (needs Node + Playwright Chromium + ffmpeg, as in Claude Code cloud sessions)
```bash
SK=<path to this skill>
# 10 fps preview -> contact sheet
node $SK/scripts/render.js $SK/templates/location.html /tmp/pv 6 10 1
ffmpeg -framerate 10 -i /tmp/pv/f%05d.jpg -vf "scale=180:-1,tile=12x5" sheet.png
# final: 30 fps x 8 shutter samples = real motion blur
node $SK/scripts/render.js $SK/templates/location.html /tmp/fr 6 30 8
ffmpeg -framerate 240 -i /tmp/fr/f%05d.jpg \
  -vf "tmix=frames=8:weights='1 1 1 1 1 1 1 1',select='eq(mod(n\,8)\,7)',setpts=N/30/TB" \
  -r 30 -an -c:v libx264 -pix_fmt yuv420p -crf 17 -movflags +faststart out.mp4
# exact single frame (cut matching, spot checks)
node $SK/scripts/seek1.js $SK/templates/balcony.html 5999 end.png
```
- If `require('playwright')` fails outside Claude Code's cloud sessions, install it (`npm i playwright && npx playwright install chromium`).
- The fonts are bundled, so renders don't depend on the machine's installed fonts.
- To learn from a new reference video, use `scripts/measure.py` (per-word position, opacity and sharpness per frame) and `scripts/pan.py` (pan speed per frame) on extracted frames, then fit eases as described in RULEBOOK §5.

## Examples
`examples/still1-4.jpg` are the approved still frames (hook, balcony, location, pricing). `examples/approved_sequence_keyframes.jpg` shows key frames from the approved 18 s balcony → location → pricing sequence.
