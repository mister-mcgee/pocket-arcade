from arcade       import Arcade
from arcade.input import Input
from arcade.scene import Scene

from arcade.color import WHITE
from arcade.fonts import WHITE_ON_BLACK, BLACK_ON_WHITE

from arcade.apps.system.loading             import Loading
from arcade.apps.system.device.brightness import Brightness
from arcade.apps.system.device.diagnostic import Diagnostic

class Device(Scene):
  def __init__(self):
    self.version = f"{Arcade.VERSION.major}.{Arcade.VERSION.minor}.{Arcade.VERSION.patch}"
    self.options = [
      ("Brightness",         Brightness ),
      ("Diagnostic", Loading(Diagnostic)),
    ]
    self.option  = -1

  def paint(self, c):
    c.fill(0)
    c.rect(0, 0, 128, 10, WHITE)
    c.text(BLACK_ON_WHITE, "Device", 46, 1)

    for i, (title, _) in enumerate(self.options):
      if i == self.option:
        c.hline(4, i * 10 + 20, len(title) * 6, WHITE)
        c.text (WHITE_ON_BLACK, title, 5, i * 10 + 12)
      else:
        c.text (WHITE_ON_BLACK, title, 1, i * 10 + 12)

    c.text(WHITE_ON_BLACK, self.version, 0, 120)

  def on_attach(self, c):
    self.paint(c)

  def on_render(self, c):
    c.rect(116, 120, 12, 8, 0)
    c.text(WHITE_ON_BLACK, c.stage.m_fps, 116, 120)

  def on_button_down(self, c, button):
    if   button == Input.BUTTON_L:
      self.option = (self.option + len(self.options) - 1) % len(self.options)
      self.paint(c)
    elif button == Input.BUTTON_R:
      self.option = (self.option                     + 1) % len(self.options)
      self.paint(c)
    elif button == Input.BUTTON_A:
      for i, (_, scene) in enumerate(self.options):
        if i == self.option:
          c.stage.play(scene)
    elif button == Input.BUTTON_B:
      from arcade.apps.system.dashboard import Dashboard
      c.stage.play(Dashboard)