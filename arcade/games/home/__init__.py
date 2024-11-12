from arcade import VERSION_STRING

from arcade.input import Input
from arcade.scene import Scene
from arcade.color import WHITE , BLACK
from arcade.font  import WHITE_ON_BLACK, BLACK_ON_WHITE

from arcade.games.snake  import Snake
from arcade.games.chess  import Chess
from arcade.games.lights import Lights

class Home(Scene):
  def __init__(self):
    self.options = [     
      ("Chess" , Chess ),
      ("Snake" , Snake ),
      ("Lights", Lights)
    ]
    self.option = -1
    self.hold_b =  0

  def repaint(self, c):
    c.fill(0)

    c.rect(0, 0, 128, 10, WHITE)
    c.text(BLACK_ON_WHITE, VERSION_STRING, (128 - len(VERSION_STRING) * 6) // 2, 1)

    for i, (title, _) in enumerate(self.options):
      if i == self.option:
        c.hline(4, i * 10 + 20, len(title) * 6, WHITE)
        c.text (WHITE_ON_BLACK, title, 5, i * 10 + 12)
      else:
        c.text (WHITE_ON_BLACK, title, 1, i * 10 + 12)

  def on_attach(self, stage):
    self.repaint(stage.screen)

  def on_update(self, c):
    if c.input.is_button_down(Input.BUTTON_B):
      self.hold_b += 4
    else:
      self.hold_b  = 0

    if self.hold_b > 128:
      from arcade.games.settings import Settings
      c.stage.play(Settings)
  
  def on_render(self, c):
    c.rect(0, 126,         128, 2, BLACK)
    c.rect(0, 126, self.hold_b, 2, WHITE)

  def on_button_down(self, button, input):
    if   button == input.BUTTON_L:
      self.option = (self.option + len(self.options) - 1) % len(self.options)
      self.repaint(input.stage.screen)
    elif button == input.BUTTON_R:
      self.option = (self.option                    + 1) % len(self.options)
      self.repaint(input.stage.screen)
    elif button == input.BUTTON_A:
      for i, (_, module) in enumerate(self.options):
        if i == self.option:
          input.stage.play(module)
    elif button == input.BUTTON_B:
      self.option = -1
      self.repaint(input.stage.screen)