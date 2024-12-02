from arcade.input import Input
from arcade.scene import Scene

from arcade.color import WHITE, BLACK
from arcade.fonts import BLACK_ON_WHITE, WHITE_ON_BLACK

from arcade.apps.system.loading import Loading
from arcade.apps.snake.standard import Standard
from arcade.apps.snake.casual   import Casual

class Snake(Scene):
  def __init__(self):
    self.options = [
      ("Standard", Loading(Standard)),
      ("Casual"  , Loading(Casual  )),
    ]
    self.option  = -1

  def paint(self, c):
    c.fill(0)
    c.rect(0, 0, 128, 10, WHITE)
    c.text(BLACK_ON_WHITE, "Snake", 49, 1)

    for i, (title, _) in enumerate(self.options):
      if i == self.option:
        c.hline(4, i * 10 + 20, len(title) * 6, WHITE)
        c.text (WHITE_ON_BLACK, title, 5, i * 10 + 12)
      else:
        c.text (WHITE_ON_BLACK, title, 1, i * 10 + 12)

  def on_attach(self, c):
    self.paint(c)

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
