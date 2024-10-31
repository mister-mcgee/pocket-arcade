from arcade.color import color, rgb
from arcade.math  import clamp, ab

import ulab.numpy as np

class Canvas:
  def __init__(self, w=0, h=0):
    self.w    = w
    self.h    = h
    self.buffer = np.zeros((h, w), dtype=np.uint16)

  def _clamp_x(self, x):
    return int(clamp(x, 0, self.w))
  
  def _clamp_y(self, y):
    return int(clamp(y, 0, self.h))

  def fill(self, c):
    self.buffer[::] = c

  def rect(self, x, y, w, h, c):
    x0, x1 = ab(x , x + w)
    y0, y1 = ab(y , y + h)
    x0 = self._clamp_x(x0)
    x1 = self._clamp_x(x1)
    y0 = self._clamp_y(y0)
    y1 = self._clamp_y(y1)
    self.buffer[y0:y1, x0:x1] = c

  def hline(self, x, y, w, c):
    self.rect(x, y, w, 1, c)

  def vline(self, x, y, h, c):
    self.rect(x, y, 1, h, c)

  def circle(self, x, y, r, c):
    pass

  def image(self, i, x=0, y=0, sx=0, sy=0, sw=None, sh=None):
    w = sw or i.w
    h = sh or i.h
    self.buffer[y:y+h, x:x+w] = i.buffer[sy:sy+h, sx:sx+w]