from arcade.canvas import Canvas

import board
import busio
import pwmio
import digitalio

from adafruit_rgb_display import st7735

class Screen(Canvas):
  def __init__(self, stage,
    configure_x_offset =   2,
    configure_y_offset =   3,
    configure_w        = 128,
    configure_h        = 128,
    configure_pin_cs   = board.D10 ,
    configure_pin_rs   = board.D11 ,
    configure_pin_dc   = board.D12 ,
    configure_pin_sck  = board.SCK ,
    configure_pin_miso = board.MISO,
    configure_pin_mosi = board.MOSI,
    configure_pin_lite = board.D13 ,
  ):    
    super().__init__(
      configure_w + 1,
      configure_h    
    )
    self.stage = stage
    self.w = configure_w
    self.h = configure_h

    self.device = st7735.ST7735R(
      busio.SPI(
        clock=configure_pin_sck , 
        MOSI =configure_pin_mosi,
        MISO =configure_pin_miso
      ), 
      width    = configure_w, 
      height   = configure_h, 
      rotation = 0,
      x_offset = configure_x_offset,
      y_offset = configure_y_offset,
      cs       = digitalio.DigitalInOut(configure_pin_cs),
      dc       = digitalio.DigitalInOut(configure_pin_dc),
      rst      = digitalio.DigitalInOut(configure_pin_rs),
    )

  def blit(self):
    self.device._block(0, 0, 
      self.w,
      self.h,
      self.buffer
    )