import adafruit_imageload
from arcade.canvas import Canvas

class Image(Canvas):
  def __init__(self, where):
    raw, _ = adafruit_imageload.load(where)
    super().__init__(raw.width, raw.height)
    
    for y in range(raw.height):
      for x in range(raw.width):
        self.buffer[y, x] = raw[x, y]

    self.buffer.byteswap(inplace=True)