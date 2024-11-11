from arcade import VERSION_STRING

from arcade.scene import Scene
from arcade.color import WHITE , BLACK
from arcade.font  import WHITE_ON_BLACK, BLACK_ON_WHITE

from arcade.games.settings  import Settings
from arcade.games.snake     import Snake
from arcade.games.chess     import Chess
from arcade.games.lights    import Lights

class Home(Scene):
  def __init__(self):
    self.games = [     
      ("Chess" , Chess ),
      ("Snake" , Snake ),
      ("Lights", Lights),
      ("Settings", Settings),
    ]
    self.selected = -1

  def repaint(self, c):
    c.fill(0)

    c.rect(0, 0, 128, 10, WHITE)
    c.text(BLACK_ON_WHITE, VERSION_STRING, (128 - len(VERSION_STRING) * 6) // 2, 1)

    for i, (title, _) in enumerate(self.games):
      if i == self.selected:
        c.hline(4, i * 10 + 20, len(title) * 6, WHITE)
        c.text (WHITE_ON_BLACK, title, 5, i * 10 + 12)
      else:
        c.text (WHITE_ON_BLACK, title, 1, i * 10 + 12)

  def on_attach(self, stage):
    self.repaint(stage.screen)

  def on_button_down(self, button, input):
    if button == input.BUTTON_L:
      self.selected = (self.selected + len(self.games) - 1) % len(self.games)
      self.repaint(input.stage.screen)
    elif button == input.BUTTON_R:
      self.selected = (self.selected                   + 1) % len(self.games)
      self.repaint(input.stage.screen)
    elif button == input.BUTTON_A:
      for i, (_, game) in enumerate(self.games):
        if i == self.selected:
          input.stage.play(game)
    elif button == input.BUTTON_B:
      self.selected = -1
      self.repaint(input.stage.screen)