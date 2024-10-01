import board
import busio
import digitalio

from lib.adafruit_rgb_display import st7735

class Stage:
  WIDTH  = 128
  HEIGHT = 128
  __X_OFFSET__ = 2
  __Y_OFFSET__ = 3

  def __init__(self):
    self.display = st7735.ST7735R(
      busio.SPI(
        clock = board.SCK, 
        MOSI  = board.MOSI, 
        MISO  = board.MISO
      ), 
      width    = Stage.WIDTH , 
      height   = Stage.HEIGHT, 
      rotation = 0,
      x_offset = Stage.__X_OFFSET__,
      y_offset = Stage.__Y_OFFSET__,

      dc  = digitalio.DigitalInOut(board.D12),
      cs  = digitalio.DigitalInOut(board.D10),
      rst = digitalio.DigitalInOut(board.D11)
    )
    self.display.init()