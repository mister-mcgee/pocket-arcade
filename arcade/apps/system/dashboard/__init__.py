from arcade       import Arcade
from arcade.input import Input
from arcade.scene import Scene

from arcade.color import BLACK, WHITE
from arcade.fonts import BLACK_ON_WHITE, WHITE_ON_BLACK

from arcade.apps.games.pong   import Pong
from arcade.apps.games.snake  import Snake
from arcade.apps.games.floppy import Floppy
from arcade.apps.games.memory import Memory
from arcade.apps.games.lights import Lights

from arcade.apps.system.loading import Loading

class Dashboard(Scene):
  def __init__(self):
    self.version = "Home" #Arcade.VERSION.moniker
    self.options = [
      ("Pong"  , Pong ),
      ("Snake" , Snake),
      ("Floppy", Loading(Floppy)),
      ("Memory", Loading(Memory)),
      ("Lights", Loading(Lights)),
    ]
    self.option = -1
    self.hold_b =  0

  def paint(self, c):
    c.fill(0)
    c.rect(0, 0, 128, 10, WHITE)
    c.text(BLACK_ON_WHITE, self.version, (128 - len(self.version) * 6) // 2, 1)

    for i, (title, _) in enumerate(self.options):
      if i == self.option:
        c.hline(4, i * 10 + 20, len(title) * 6, WHITE)
        c.text (WHITE_ON_BLACK, title, 5, i * 10 + 12)
      else:
        c.text (WHITE_ON_BLACK, title, 1, i * 10 + 12)

  def on_attach(self, c):
    self.paint(c)

  def on_update(self, c):
    if c.is_button_down(Input.BUTTON_B):
      self.hold_b += 8
    else:
      self.hold_b  = 0

    if self.hold_b > 128:
      from arcade.apps.system.device import Device
      c.stage.play(Device)

  def on_render(self, c):
    c.rect(0, 126,         128, 2, BLACK)
    c.rect(0, 126, self.hold_b, 2, WHITE)

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
