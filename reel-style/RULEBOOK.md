# Reel Motion-Graphics Rulebook

The approved style, layout and animation rules for 9:16 reels, built up and signed off over the session logged in [`CONVERSATION.md`](CONVERSATION.md) (16–17 Nov 2026). Everything here was approved by the user unless it is marked **Open** or **Not approved yet**.

| | |
|---|---|
| Format | 9:16, 1080 × 1920, 30 fps |
| Style reference | _buytheedit-style brand documentary motion graphics (15 still references) |
| Motion reference | "This is Cristiano Ronaldo…" edit, 14.4 s (analysed frame by frame) |
| First project | Mira Bhayandar East, 1 & 2 BHK property reel (Hinglish voiceover) |
| Approved beats | `approved/balcony.html` → `approved/location.html` → `approved/pricing.html` (18 s continuous) |

---

## 1. Visual style

**Approved:** "Approved this recent understood style".

### Canvas
- Light grey canvas with a soft vignette, never flat white: `radial-gradient(ellipse at 50% 40%, #f4f6f9 0%, #e6e9ee 60%, #cfd4dc 100%)`.
- A **halftone dot grain** over everything, footage included: 1px dots on a 5px grid, `rgba(0,0,0,.09)`, `mix-blend-mode: multiply`. This grain is what makes it feel editorial rather than templated.
- **Dark contrast scenes** are used now and then for numbers, stats and pricing, to change the pacing: `radial-gradient(ellipse at 50% 35%, #1d2129, #0b0c0f 55%, #000)`. On dark scenes the grain is white at 5% with `screen` blending.

### Colour
- Neutral base, charcoal ink `#16181d` / `#2a2d33`, grey supporting text `#4a4f59`.
- **One accent per video.** For this project it is royal blue `#1f5fff`, with a blue → cyan `#22b8f0` gradient on key words.

### Typography
- A tight-tracked grotesk: **Inter Display**. Mostly lowercase, with negative letter-spacing (−0.03 em on body text, −0.06 em on key words).
- **Two-tier contrast on every line:** the setup words are **light (300), grey and smaller**; the key word is **extra-bold (800), large and in the blue gradient**. Example: `sab kuch` at 60px light grey, then **`paas`** at 150px heavy blue.
- Key-word emphasis comes from **size, weight and colour**, plus one soft glow (`drop-shadow(0 0 26px rgba(31,95,255,.5))`).
- Text can be treated as layout: curved text on an SVG `textPath`, vertical labels, words on an arc.

### Composition
- Centred, with **plenty of negative space and one focal object per screen**.
- Footage and photos sit in **rounded cards** (radius 40px) with soft shadows (`0 50px 90px rgba(20,30,60,.25)`).
- **Circles and geometry** carry ideas: orbit rings, discs, pills, bars, measurement lines with end ticks.
- **Corner brackets** (44px, 4px stroke) frame the safe zone and stay fixed while everything else moves.

---

## 2. Layout rules

**Approved:** the user's feedback on the first stills was applied and signed off.

1. **Keep the footer clear.** No text in the bottom ~480px (y > 1440), where Instagram's caption, username and subtitles sit.
2. **Keep the right edge clear.** No text in the right ~140px, where the like and comment buttons are.
3. **Text safe zone:** y 220–1440, x 80–940.
4. **Choose the attention point first.** For each script line, decide whether the eye should land at the **top, middle or bottom**, then build the frame around that one point.
5. **One key word per line**, using the two-tier contrast in §1.
6. **No overlapping text.** Text never sits on other text, rings, lines, badges or pills. Pills go in clear space and are linked to their element by colour (blue pill ↔ blue ring, dark pill ↔ dark ring).
7. **Text must be readable on a phone.** Information the viewer needs gets ≥ 54px. Small place names become **icons** (graduation cap, college, train) instead of 30px labels.
8. **Cut secondary information** rather than shrink it. If it won't be read in the time it's on screen, it doesn't go on screen.
9. **Images:** either full-bleed and softly blurred behind the text (depth of field), or inside a rounded card. Generated images must not stand in for the real property in the final edit.

---

## 3. Content and engagement guidance

Agreed in the "Are you sure this will be engaging?" discussion.

- **The hook is the most surprising fact or the best visual**, not the intro. For this project that is the 2 + 2 → 5 BHK merge or the creek and mountain view, not "1 & 2 BHK ready to move".
- **Real footage beats generated imagery** for trust. AI images are placeholders only.
- **Graphics are inserts, not slides:** 3–4 motion-graphic beats of about 1.5–6 s inside the walkthrough footage.
- **One idea per beat.** Viewers read the key word and the big numbers, and little else.
- **Something on screen changes every 2–3 s.**
- End with a clear call to action (for example, "comment 5BHK").

---

## 4. Motion principles

**Approved:** "Approved animation principles".

### 4.1 Speed curves
- **No linear movement, ever.** Every position, scale, rotation and opacity change is eased, including slow camera drifts.
- Entering elements: fast start, long soft stop. Leaving elements: slow start, then fast. Moves across the frame: ease in and out.
- Fast moves get **real motion blur** (see §8), which grows with speed and is gone when the element lands.

### 4.2 No dead frames
- At least one thing is always moving. During holds the camera pushes slowly (2–4%), and small secondary motion keeps going: pulses, ripples, glows, sweeps.
- A single element *may* sit perfectly still while something else moves (measured: "From" sits pixel-still for 7 frames while "goals" is still settling). The **frame** is never still.
- Each beat ends by starting the next motion, so beats overlap rather than finishing cleanly one at a time.

### 4.3 Transitions connect (no hard cuts between graphic beats)
| Type | How it works | Used in |
|---|---|---|
| **Whip pan** | Anticipation (a 2–4 frame lean the other way), then exponential acceleration with blur; the cut lands at peak speed and the next shot starts moving and decelerates | balcony card → location |
| **Carried element** | An element of the outgoing scene becomes part of the incoming one | the "3 ft" pill becomes the location disc |
| **Match cut / morph** | The same shape ends one scene and starts the next | full-screen blue → the 686 price bar |
| **Zoom through** | The camera pushes into an element and comes out in the next scene | the location disc zooms to solid blue |

- Direction stays consistent: if scene A leaves to the left, scene B enters from the right.
- Transitions take 0.3–0.6 s.
- **Text fades out (about 0.2 s with blur) before a zoom-through**, so it never smears across itself.
- When a beat ends where the next one begins, the last frame of A must **match the first frame of B** (checked with a pixel diff; see §9).

### 4.4 Classic animation principles
| Principle | Rule |
|---|---|
| Squash and stretch | **Shapes only.** Stretch 5–12% along the direction of travel at top speed; squash on landing (e.g. `scale(1.14, .86)`), then settle. **Never on letters.** |
| Anticipation | Before a big move, pull back 2–4 frames the opposite way, or scale to about 0.96–0.97, then go. |
| Follow-through / overlapping action | Parts don't stop together: card first, then its shadow and labels 2–4 frames later. Stagger children by 0.06–0.12 s. |
| Slow in / slow out | Covered by §4.1 and the curves in §6. |
| Arcs | Things travel on curves: animate X and Y on different eases; dots ride along rings (rotate around the ring centre while the icon counter-rotates to stay upright). |
| Timing | Key word holds about 1–1.5 s; supporting words 0.4–0.6 s; transitions 0.3–0.5 s; pops 0.35–0.5 s; land moves on voiceover beats. |
| Secondary action | Glow pulse, underline draw, ripple, light sweep. Supports the main move, never competes with it. |
| Staging | One focal point at a time; everything else dimmer, smaller or waiting its turn. |

---

## 5. Text motion (measured from the reference)

**Approved:** "Apply and re-render" after the frame-by-frame analysis. All pixel values are scaled from the 720px reference to our 1080px frame.

| Rule | Value |
|---|---|
| Supporting word entry | rise **36px** over **0.45 s** on `--txt: cubic-bezier(.2,.3,0,.8)` (fits the measured motion within 0.9%) |
| Blur and opacity | clear **before** the position settles: **0.2 s** on `--rev: cubic-bezier(.2,.7,.3,1)`, starting from `blur(16px)`, opacity 0 |
| Stagger between words | **0.17 s** at normal speaking pace; **0.07 s** for fast lists |
| Key word entry | rise 36px over **0.75 s** on `--key: cubic-bezier(.3,.65,.45,.85)`, blur/opacity over 0.3 s. **Slower and softer than supporting words, not punchier** |
| Key word hold | the word breathes **+2.5% scale** through the hold (`.kw` wrapper, `--io` ease), with one glow |
| No overshoot on text | Text moves in one direction only, straight to rest: **no bounce, no squash** |
| Land into drift | Text doesn't come to a dead stop; it lands into a slow drift or scale. The camera drift handles this |
| Camera follows the writing | When a line outgrows the frame, the line holds while a word arrives, then pans to make room: about **585px in 0.77 s** on `cubic-bezier(.3,.2,.25,1)` (peaks at about 22% of the move, long braking tail) |
| Selection box / brackets on text | resize to the text bounds every frame as words type in, then settle slowly |

How our older ease compared with the reference: `easeOutExpo` (`.16,1,.3,1`) was **14–23% off** the measured curves (too much movement at the start, then a dead stop). Use the fitted curves above for text.

---

## 6. Ease tokens (copy into every beat)

```css
:root{
  /* shapes, cards, camera */
  --out: cubic-bezier(.16,1,.3,1);    /* fast start, long settle */
  --in:  cubic-bezier(.7,0,.84,0);    /* slow start, then fast (exits, whip-out) */
  --io:  cubic-bezier(.65,0,.35,1);   /* across-frame moves, drifts */
  --pop: cubic-bezier(.34,1.56,.64,1);/* shape pop with overshoot (never text) */
  /* text, measured from the reference */
  --txt: cubic-bezier(.2,.3,0,.8);    /* supporting word rise */
  --key: cubic-bezier(.3,.65,.45,.85);/* key word rise */
  --rev: cubic-bezier(.2,.7,.3,1);    /* blur + opacity reveal */
}
@keyframes rise36 {from{transform:translateY(36px)} to{transform:none}}
@keyframes reveal {from{opacity:0;filter:blur(16px)} to{opacity:1;filter:blur(0)}}
@keyframes breathe{from{transform:scale(1)} to{transform:scale(1.025)}}
.kw{display:inline-block;transform-origin:50% 60%;animation:breathe var(--bl) var(--io) var(--bd) both}
/* word:     animation: rise36 .45s var(--txt) D both, reveal .2s var(--rev) D both;            */
/* key word: animation: rise36 .75s var(--key) D both, reveal .3s var(--rev) D both,
             glow 1.1s var(--io) LATER forwards;   wrap in <span class="kw" style="--bd:..;--bl:..">  */
/* camera pan to follow text: cubic-bezier(.3,.2,.25,1), ~0.77s                                    */
```

Gotcha: give glows `forwards` (not `both`) so their fill doesn't override the reveal blur before they start.

---

## 7. Shape motion

- **Pops:** scale 0 → overshoot `scale(1.15–1.25, .8–.86)` → `scale(.92–.96, 1.04–1.08)` → rest, over 0.4–0.55 s.
- **Pills arriving:** come along a short arc (rise about 34px) with an overshoot and a small squash.
- **Rings** draw on (`stroke-dashoffset` with `pathLength=1`) while growing out of the centre element.
- **Bars** rise from the floor with a stretch, then settle; numbers **count up** as their bar lands (`@property --n` integer plus `counter()`; one keyframe per target value, with `inherits: true`).
- **Hold life:** pulses in sequence, ripples, a light sweep clipped *inside* each bar, a glow on the key word.
- **Light sweeps / ripples** are hidden (`opacity:0`) until their cue, so they never leak into early frames.

---

## 8. Production pipeline

Everything is plain HTML/CSS/SVG rendered frame-accurately by headless Chromium (Playwright), then encoded with ffmpeg. No video editor is needed.

```bash
# preview: 10 fps, no blur → contact sheet to check choreography
node tools/render.js approved/location.html /tmp/pv 6 10 1
ffmpeg -framerate 10 -i /tmp/pv/f%05d.jpg -vf "scale=180:-1,tile=12x5" sheet.png

# final: 30 fps × 8 shutter samples (180° shutter) → real motion blur
node tools/render.js approved/location.html /tmp/fr 6 30 8
ffmpeg -framerate 240 -i /tmp/fr/f%05d.jpg \
  -vf "tmix=frames=8:weights='1 1 1 1 1 1 1 1',select='eq(mod(n\,8)\,7)',setpts=N/30/TB" \
  -r 30 -an -c:v libx264 -pix_fmt yuv420p -crf 17 -movflags +faststart out.mp4

# one exact frame (for cut-matching and spot checks)
node tools/seek1.js approved/balcony.html 5999 end.png
```

- `render.js` pauses every CSS animation and seeks it to each frame time, so renders are deterministic.
- 4 samples per frame showed ghosting on fast zooms; **8 samples per frame is the standard.**
- `tools/measure.py` and `tools/pan.py` are the reference-analysis tools (per-word position, opacity and sharpness; phase-correlation pan speed). Use them on any new reference before copying its motion.

---

## 9. QA checklist (run on every beat before sending)

1. Preview contact sheet at 10 fps: check the choreography and that nothing shows before its cue.
2. Full-size frames at the busiest moment and in the hold: **no text overlaps** anything; footer and right edge are clear.
3. Text readable at phone size; key word clearly dominant.
4. No dead frames: something moves in every frame of the hold.
5. Cut match with the neighbouring beat: pixel diff of A's last frame against B's first frame (target mean < 1/255).
6. Frame count and duration verified with `ffprobe` (e.g. 180 frames = 6.0 s).
7. Final render at 8 samples; spot-check frames from the MP4 itself.

---

## 10. Sound

**Not approved yet.** Add **no sound effects** until the user shares their sound guide. All deliveries are silent. (A synthesized SFX test was made for the location beat and then removed at the user's request.)

---

## 11. Approved beats (reference implementations)

Continuity chain: **balcony → location → pricing**, 18 s, `renders/sequence_18s.mp4`.

### Balcony (`approved/balcony.html`, 6 s)
| Time | Motion |
|---|---|
| 0–0.15 s | full-screen balcony photo, slightly blurred (stands in for footage) |
| 0.15–1.3 s | anticipation push-in, then it shrinks into the rounded card, overshoots and settles, focusing on the way |
| 0.75–1.84 s | `sabse` → `beautiful` → **balcony** (key-word curve), then the breathe begins |
| 1.35–2.3 s | measurement line draws from its centre, end ticks pop, **3 ft** pill pops with a squash |
| 2.3–3.6 s | `khadi + mountain view` tag from the left; `lagbhag 700 sq ft` from the right, counting up |
| 3.8–5.3 s | pill pulse, key-word glow, slow camera push |
| 5.35–6 s | tags fade, leaving exactly the location beat's first frame |

### Location (`approved/location.html`, 6 s)
| Time | Motion |
|---|---|
| 0–0.62 s | balcony card leans back, then whips left in 3D with blur |
| 0.2–1.0 s | the **3 ft** pill breaks away on an arc (camera follows it), stretches at top speed and grows into the blue disc, squashing on landing |
| 0.45–1.54 s | `sab` → `kuch` → **paas** |
| 1.0–2.5 s | towers rise in the disc; blue inner ring draws; school/college badges ride the ring; **2–5 min walk** pill; outer ring draws; station badges ride it; **10–12 min** pill |
| 2.9–5.3 s | ripples, badge pulses in sequence, pill pulses, key-word breathe and glow |
| 5.3–6 s | text fades; anticipation dip; **zoom through the disc** to solid blue |

### Pricing (`approved/pricing.html`, 6 s, dark scene)
| Time | Motion |
|---|---|
| 0–0.8 s | starts on solid blue (the location exit); it pulls in, then collapses into the **686 bar**, revealing the dark scene |
| 0.85–1.6 s | the other bars rise in turn with stretch and settle; each number counts up as its bar lands; `CARPET AREA · SQ FT` |
| 1.7–2.8 s | `2 BHK pricing` → `₹1.10 –` (light) → **1.37 Cr** (key word) → GST note |
| 3.1–5.2 s | light sweep across the bars left to right, price glows, key word breathes |
| 5.2–6 s | text fades; the scene dips, then whips upward |

---

## 12. Open items

- **Real assets:** a real balcony photo or footage frame, and real building and drone shots (the generated images are low-res placeholders).
- **Sound guide** from the user before any SFX or music.
- **Script facts to confirm:** "khadi" read as creek; "foil area" read as foyer; "terah carpet area" but only five sizes listed; the real floor plan; project name and phone number for the end card.
- **Next beats:** hook frame (lead with the 5 BHK merge or the view) and the 2 + 2 → 5 BHK merge graphic.
