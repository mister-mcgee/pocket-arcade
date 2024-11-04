import ulab.numpy as np

__x0__ = 0
__y0__ = 0
__x1__ = 0
__y1__ = 0
__x2__ = 0
__y2__ = 0
__x3__ = 0
__y3__ = 0

__w__  = 0
__h__  = 0

def ab(a, b):
  return (a, b) if a <= b else (b, a)

def clamp(x, a, b):
  return max(a, min(b, x))

def clip(
  x0, y0, x1, y1,
  x2, y2, x3, y3
):
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
    global __x0__, __y0__, __x1__, __y1__

    # clip rectangle
    __x0__, __x1__ = ab(x , x + w)
    __y0__, __y1__ = ab(y , y + h)
    __x0__, __y0__, __x1__, __y1__ = clip(0, 0, self.w, self.h, __x0__, __y0__, __x1__, __y1__)

    if (
      __x0__ != __x1__ and 
      __y0__ != __y1__
    ):
      # populate buffer
      self.buffer[
        __y0__:__y1__,
        __x0__:__x1__
      ] = c

  def hline(self, x, y, w, c):
    self.rect(x, y, w, 1, c)

  def vline(self, x, y, h, c):
    self.rect(x, y, 1, h, c)

  def image(self, i, x=0, y=0, sx=0, sy=0, sw=None, sh=None):
    global __x0__, __y0__, __x1__, __y1__
    global __x2__, __y2__, __x3__, __y3__
    global __w__ , __h__

    __w__ = sw or i.w
    __h__ = sh or i.h

    # clip dst rectangle
    __x0__, __x1__ = ab(x, x + __w__)
    __y0__, __y1__ = ab(y, y + __h__)
    __x0__, __y0__, __x1__, __y1__ = clip(0, 0, self.w, self.h, __x0__, __y0__, __x1__, __y1__)

    __w__ = min(__w__, __x1__ - __x0__)
    __h__ = min(__h__, __y1__ - __y0__)

    # clip src rectangle
    __x2__, __x3__ = ab(sx, sx + __w__)
    __y2__, __y3__ = ab(sy, sy + __h__)
    __x2__, __y2__, __x3__, __y3__ = clip(0, 0, i.w, i.h, __x2__, __y2__, __x3__, __y3__)

    # populate buffer
    self.buffer[
      __y0__:__y1__,
      __x0__:__x1__
    ] = i.buffer [
      __y2__:__y3__,
      __x2__:__x3__
    ]

  def text(self, font, text, x=0, y=0):
    font.draw_text(self, text, x, y)
