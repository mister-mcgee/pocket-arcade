def color(r, g, b):
  r  = (31 * r // 255) & 0x1F
  g  = (63 * g // 255) & 0x3F
  b  = (31 * b // 255) & 0x1F
  b0 = ((r << 3) | (g >> 3)) & 0xFF
  b1 = ((g << 5) | (b     )) & 0xFF
  return b0 | (b1 << 8)

def r(c):
  return 255 * ((c >> 3) & 0x1F) // 31

def g(c):
  b0 = (c >> 13) & 0x7
  b1 = (c      ) & 0x7
  return 255 * ( b0 | (b1 << 3)) // 63

def b(c):
  return 255 * ((c >> 8) & 0x1F) // 31

def rgb(c):
  return (r(c), g(c), b(c))

WHITE   = color(255, 255, 255)
BLACK   = color(  0,   0,   0)
RED     = color(255,   0,   0)
GREEN   = color(  0, 255,   0)
BLUE    = color(  0,   0, 255)
CYAN    = color(  0, 255, 255)
MAGENTA = color(255,   0, 255)
YELLOW  = color(255, 255,   0)
