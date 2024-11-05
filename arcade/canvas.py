import ulab.numpy as np

def ab(a, b):
  return (a, b) if a <= b else (b, a)

def clamp(x, a, b):
  return max(a, min(b, x))

def clip(
  x0, y0, x1, y1,
  x2, y2, x3, y3
):
  x0, x1 = ab(x0, x1)
  y0, y1 = ab(y0, y1)
  x2, x3 = ab(x2, x3)
  y2, y3 = ab(y2, y3)
  return (
    int(clamp(x2, x0, x1)),
    int(clamp(y2, y0, y1)),
    int(clamp(x3, x0, x1)),
    int(clamp(y3, y0, y1))
  )

class Canvas:
  def __init__(self, w=0, h=0, n=0):
    self.w = w
    self.h = h
    self.buffer = np.zeros((h, w), dtype=np.uint16)

  def __getitem__(self, at):
    return self.buffer[at]
  
  def __setitem__(self, at, c):
    self.buffer[at] = c

  def fill(self, c):
    self.buffer[::] = c

  def rect(self, x, y, w, h, c):
    # clip rectangle
    x0, y0, x1, y1 = clip(0, 0, self.w, self.h, x, y, x + w, y + h)

    if (x0 == x1 and y0 == y1):
      return

    # populate buffer
    self.buffer[y0:y1, x0:x1] = c

  def hline(self, x, y, w, c):
    self.rect(x, y, w, 1, c)

  def vline(self, x, y, h, c):
    self.rect(x, y, 1, h, c)

  def image(self, i, x=0, y=0, sx=0, sy=0, sw=None, sh=None):
    sw = sw or i.w
    sh = sh or i.h

    # clip dst rectangle
    x0, y0, x1, y1 = clip(0, 0, self.w, self.h, x, y, x + sw, y + sh)

    dx = x0 - x
    dy = y0 - y
    dw = (x1 - x0) - sw
    dh = (y1 - y0) - sh
    
    # clip src rectangle
    x2, y2, x3, y3 = clip(0, 0, i.w, i.h, 
      sx + dx, 
      sy + dy,
      sx + dx + sw + dw,
      sy + dy + sh + dh
    )

    x1 = x0 + x3 - x2
    y1 = y0 + y3 - y2

    if (x0 == x1 or y0 == y1):
      return

    # populate buffer
    self.buffer[y0: y1, x0: x1] = i.buffer[y2: y3, x2: x3]

  def text(self, font, text, x=0, y=0):
    for c in text:
      self.image(
        font.atlas, x, y, 
        ((ord(c) - 32)  % font.cols) * font.col_w, 
        ((ord(c) - 32) // font.cols) * font.row_h, 
        font.col_w, font.row_h
      )
      x += font.col_w
