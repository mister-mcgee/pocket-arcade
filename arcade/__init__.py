from arcade.version import Version
from arcade.stage   import Stage
from arcade.input   import Input
from arcade.image   import Image
from arcade.scene   import Scene
from arcade.canvas  import Canvas

from arcade.math  import *
from arcade.color import *

import board
import busio
import digitalio

from adafruit_rgb_display import st7735

class Arcade:
  VERSION = Version("Arcade", 0, 1, 0)

  CONFIGURE_FRAMERATE    =  20 # frames per second
  CONFIGURE_SCREEN_X     =   2 # pixels
  CONFIGURE_SCREEN_Y     =   3 # pixels
  CONFIGURE_SCREEN_W     = 128 # pixels
  CONFIGURE_SCREEN_H     = 128 # pixels
  CONFIGURE_PIN_CS       = board.D10
  CONFIGURE_PIN_RS       = board.D11
  CONFIGURE_PIN_DC       = board.D12
  CONFIGURE_PIN_SCK      = board.SCK
  CONFIGURE_PIN_MISO     = board.MISO
  CONFIGURE_PIN_MOSI     = board.MOSI
  CONFIGURE_PIN_LITE     = board.D13
  CONFIGURE_PIN_BUTTON_1 = board.A1
  CONFIGURE_PIN_BUTTON_2 = board.A2
  CONFIGURE_PIN_BUTTON_3 = board.A3
  CONFIGURE_PIN_BUTTON_4 = board.A4

  def __init__(self):
    self.w = self.CONFIGURE_SCREEN_W
    self.h = self.CONFIGURE_SCREEN_H

    self.screen = st7735.ST7735R(
      busio.SPI(
        clock=self.cfg_pin_sck , 
        MOSI =self.cfg_pin_mosi,
        MISO =self.cfg_pin_miso
      ), 
      width    = self.cfg_w, 
      height   = self.cfg_h, 
      rotation = 0,
      x_offset = self.cfg_x,
      y_offset = self.cfg_y,
      cs       = digitalio.DigitalInOut(self.cfg_pin_cs),
      dc       = digitalio.DigitalInOut(self.cfg_pin_dc),
      rst      = digitalio.DigitalInOut(self.cfg_pin_rs),
    )

