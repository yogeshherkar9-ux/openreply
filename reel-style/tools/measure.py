# Per-frame text measurements from the reference video (720x1280, 29.97fps).
# For each word box: ink (opacity proxy), weighted centroid y/x, sharpness (mean |grad| on ink).
import sys, numpy as np
from PIL import Image
D = sys.argv[1]
def load(n): return np.asarray(Image.open(f"{D}/all/{n+1:04d}.png").convert('RGB')).astype(float)

def word(img, x0, x1, y0, y1, bg=232):
    r = img[y0:y1, x0:x1]
    lum = r.mean(2); sat = r.max(2) - r.min(2)
    ink = np.clip(bg - lum, 0, None) * (sat < 40)          # neutral (non-blue) dark pixels only
    m = ink.sum()
    if m < 50: return 0, np.nan, np.nan, 0
    ys, xs = np.mgrid[y0:y1, x0:x1]
    gy, gx = np.gradient(lum)
    sharp = (np.hypot(gx, gy) * (ink > 20)).sum() / max((ink > 20).sum(), 1)
    return m, (ink * ys).sum() / m, (ink * xs).sum() / m, sharp

def run(name, frames, boxes):
    print(f"\n== {name} ==  (t in s; ink normalised to final; y/x in px @720w)")
    rows = []
    for n in frames:
        img = load(n); rows.append([word(img, *b) for b in boxes])
    fin = [rows[-1][i][0] or 1 for i in range(len(boxes))]
    hdr = "  ".join(f"{'w'+str(i)+' ink':>7} {'y':>6} {'x':>6} {'shp':>5}" for i in range(len(boxes)))
    print(f"{'f':>4} {'t':>6}  {hdr}")
    for n, r in zip(frames, rows):
        cells = "  ".join(f"{m/fin[i]:7.2f} {y:6.1f} {x:6.1f} {s:5.1f}" for i, (m, y, x, s) in enumerate(r))
        print(f"{n:4d} {n/29.97:6.3f}  {cells}")

which = sys.argv[2]
if which == "clutch":   # From / clutch / goals, line at y~260-330 (full res)
    run("From clutch goals", range(108, 141), [(110, 265, 255, 335), (265, 435, 255, 335), (435, 485, 255, 335)])
if which == "unmatch":  # to / unmatch : moving line, wide boxes; x tracks the pan
    run("to unmatch descipline", range(136, 169), [(0, 720, 540, 640)])
if which == "39":
    run("at 39 / he is not slowing down", range(330, 380), [(250, 470, 440, 530), (200, 520, 530, 575)])
