import gc
import adafruit_imageload
from arcade.canvas import Canvas

class Image(Canvas):
  def __init__(self, path):
    gc.collect()
    raw , _ = adafruit_imageload.load(path)
    super().__init__(raw.width, raw.height)
    
    for y in range(raw.height):
      for x in range(raw.width):
        self.buffer[y, x] = raw[x, y]

    self.buffer.byteswap(inplace=True)
    gc.collect()