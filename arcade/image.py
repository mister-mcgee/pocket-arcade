import gc
import adafruit_imageload
from arcade.canvas import Canvas

class Image(Canvas):
  def __init__(self, w, h, d):
    super().__init__(w, h)

  def at(self, where):
    return (
      where[1], 
      where[0]
    ) if type(where) is tuple else (
      where // self.w,
      where  % self.w
    )

  def __getitem__(self, where   ):
    return self.buffer[self.at(where)]

  def __setitem__(self, where, c):
    self.buffer[self.at(where)]  =  c

  def load(path):
    image, _ = adafruit_imageload.load(path, bitmap=Image)
    image.buffer.byteswap(inplace=True)
    gc.collect()

    return image
