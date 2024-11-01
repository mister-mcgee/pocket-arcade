import ulab.numpy as np

def ab(a, b):
  return (a, b) if a <= b else (b, a)

def clamp(x, a, b):
  return max(a, min(b, x))

def clip(
  x0, y0, x1, y1,
  x2, y2, x3, y3
):
  a0, b0 = ab(x0, x1)
  a1, b1 = ab(y0, y1)
  x0, x1 = ab(x2, x3)
  y0, y1 = ab(y2, y3)

  x0 = int(clamp(x0, a0, b0))
  x1 = int(clamp(x1, a0, b0))
  y0 = int(clamp(y0, a1, b1))
  y1 = int(clamp(y1, a1, b1))

  return x0, y0, x1, y1  

class Canvas:
  def __init__(self, w=0, h=0):
    self.w = w
    self.h = h
    self.buffer = np.zeros((h, w), dtype=np.uint16)

  def fill(self, c):
    self.buffer[::] = c

  def rect(self, x, y, w, h, c):
    # clip rectangle
    x0, x1 = ab(x , x + w)
    y0, y1 = ab(y , y + h)
    x0, x1, y0, y1 = clip(0, 0, self.w, self.h, x0, y0, x1, y1)

    # populate buffer
    self.buffer[y0:y1, x0:x1] = c

  def hline(self, x, y, w, c):
    self.rect(x, y, w, 1, c)

  def vline(self, x, y, h, c):
    self.rect(x, y, 1, h, c)

  def image(self, i, x=0, y=0, sx=0, sy=0, sw=None, sh=None):
    sw = sw if sw != None else i.w
    sh = sh if sh != None else i.h

    # clip dst rectangle
    dx0, dx1 = ab(x, x + sw)
    dy0, dy1 = ab(y, y + sh)
    dx0, dy0, dx1, dy1 = clip(0, 0, self.w, self.h, dx0, dy0, dx1, dy1)

    # clip src rectangle
    sw = dx1 - dx0
    sh = dy1 - dy0
    sx0, sx1 = ab(sx, sx + sw)
    sy0, sy1 = ab(sy, sy + sh)

    # populate buffer
    self.buffer[dy0:dy1, dx0:dx1] = i.buffer[sy0:sy1, sx0:sx1]