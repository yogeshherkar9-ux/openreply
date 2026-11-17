# Global horizontal shift between consecutive frames (phase correlation on a band), = camera/layer pan speed.
import sys, numpy as np
from PIL import Image
D, a, b, y0, y1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
def band(n):
    r = np.asarray(Image.open(f"{D}/all/{n+1:04d}.png").convert('L')).astype(float)[y0:y1]
    r = r - r.mean(); return r * np.hanning(r.shape[1])[None, :]
prev = band(a); tot = 0
print(f"{'f':>4} {'t':>6} {'dx px/frame':>11} {'cum':>7}")
for n in range(a + 1, b + 1):
    cur = band(n)
    R = np.fft.fft2(prev) * np.conj(np.fft.fft2(cur)); R /= np.abs(R) + 1e-9
    c = np.abs(np.fft.ifft2(R)).sum(0)                     # collapse rows -> x-shift profile
    k = int(np.argmax(c)); dx = k if k < c.size // 2 else k - c.size
    # sub-pixel parabolic refinement
    l, m, r = c[(k - 1) % c.size], c[k], c[(k + 1) % c.size]; dx += 0.5 * (l - r) / (l - 2 * m + r + 1e-9)
    tot += dx; print(f"{n:4d} {n/29.97:6.3f} {dx:11.2f} {tot:7.1f}"); prev = cur
