import gc
import adafruit_imageload
from arcade.canvas import Canvas

class Image(Canvas):
  def __init__(self, w, h, d):
    super().__init__(w, h, d)

  def __at__(self, where):
    if type(where) is tuple:
      return (
        where[1],
        where[0]
      )
    else:
      return (
        where // self.w,
        where  % self.w
      )

  def __getitem__(self, where   ):
    c = self.buffer[self.__at__(where)]
    return c

  def __setitem__(self, where, c):
    self.buffer[self.__at__(where)] = c

  def load(path):
    image, _ = adafruit_imageload.load(path, bitmap=Image)
    image.buffer.byteswap(inplace=True)
    gc.collect()
    return image
