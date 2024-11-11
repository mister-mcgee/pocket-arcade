from arcade.scene import Scene
from arcade.color import WHITE, BLACK
from arcade.font  import WHITE_ON_BLACK, BLACK_ON_WHITE

from arcade.games.settings.brightness import Brightness
from arcade.games.settings.diagnostic import Diagnostic

class Settings(Scene):
  def __init__(self):
    self.options = [
      ("Brightness", Brightness),
      ("Diagnostic", Diagnostic),
    ]
    self.option  = -1

  def repaint(self, c):
    c.fill(0)

    c.rect(0, 0, 128, 10, WHITE)
    c.text(BLACK_ON_WHITE, "Settings", (128 - len("Settings") * 6) // 2, 1)

    for i, (title, _) in enumerate(self.options):
      if i == self.option:
        c.hline(4, i * 10 + 20, len(title) * 6, WHITE)
        c.text (WHITE_ON_BLACK, title, 5, i * 10 + 12)
      else:
        c.text (WHITE_ON_BLACK, title, 1, i * 10 + 12)

  def on_attach(self, stage):
    self.repaint(stage.screen)

  def on_button_down(self, button, input):
    if   button == input.BUTTON_L:
      self.option = (self.option + len(self.options) - 1) % len(self.options)
      self.repaint(input.stage.screen)
    elif button == input.BUTTON_R:
      self.option = (self.option                     + 1) % len(self.options)
      self.repaint(input.stage.screen)
    elif button == input.BUTTON_A:
      for i, (_, game) in enumerate(self.options):
        if i == self.option:
          input.stage.play(game)
    elif button == input.BUTTON_B:
      from arcade.games.home import Home
      input.stage.play(Home)