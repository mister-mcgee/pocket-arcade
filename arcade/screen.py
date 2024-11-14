import arcade.canvas

import board
import busio
import pwmio
import digitalio

import adafruit_rgb_display.st7735 as st7735

class Screen(arcade.canvas.Canvas):
  def __init__(self, stage): 
    super().__init__(129, 128)

    self.stage = stage
    self.w = 128
    self.h = 128

    self.display = st7735.ST7735R(
      busio.SPI(
        clock=board.SCK ,
        MOSI =board.MOSI,
        MISO =board.MISO
      ), 
      width    = 128, 
      height   = 128, 
      rotation =   0,
      x_offset =   2,
      y_offset =   3,
      cs       = digitalio.DigitalInOut(board.D10),
      dc       = digitalio.DigitalInOut(board.D12),
      rst      = digitalio.DigitalInOut(board.D11),
    )

    self.backlight = pwmio.PWMOut(board.D13, frequency=1000, duty_cycle=int(.5 * 65535))

  def set_brightness(self, brightness):
    self.backlight.duty_cycle = round(brightness * 65535)

  def get_brightness(self):
    return self.backlight.duty_cycle / 65535

  def blit(self):
    self.display._block(0, 0,
      self.w,
      self.h,
      self.buffer
    )