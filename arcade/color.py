def color(r, g, b):
  r = (31 * r // 255) & 0x1F
  g = (63 * g // 255) & 0x3F
  b = (31 * b // 255) & 0x1F
  byte0 = ((r << 3) | (g >> 3)) & 0xFF
  byte1 = ((g << 5) | (b     )) & 0xFF
  return byte0 | (byte1 << 8)

WHITE   = color(255, 255, 255)
BLACK   = color(  0,   0,   0)
RED     = color(255,   0,   0)
GREEN   = color(  0, 255,   0)
BLUE    = color(  0,   0, 255)
CYAN    = color(  0, 255, 255)
MAGENTA = color(255,   0, 255)
YELLOW  = color(255, 255,   0)