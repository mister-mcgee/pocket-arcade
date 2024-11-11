from arcade.input import Input
from arcade.scene import Scene
from arcade.color import WHITE, BLACK
from arcade.font  import WHITE_ON_BLACK


class Brightness(Scene):

  def __init__(self):
    self.frame = 0

  def on_update(self, c):
    self.frame += 1
    if self.frame % 3 == 0:
      if   c.input.is_button_down(Input.BUTTON_L):
        c.stage.screen.set_brightness(max(.1, c.stage.screen.get_brightness() - .05))
      elif c.input.is_button_down(Input.BUTTON_R):
        c.stage.screen.set_brightness(min( 1, c.stage.screen.get_brightness() + .05))

  def on_render(self, c):
    c.fill(0)
    string = f"{round(100 * c.stage.screen.get_brightness())}%"
    length =    round(118 * c.stage.screen.get_brightness())

    c.text(WHITE_ON_BLACK, string, (128 - len(string) * 6) // 2, 46)

    c.rect(4, 54,    120, 16, WHITE)
    c.rect(5, 55,    118, 14, BLACK)
    c.rect(5, 55, length, 14, WHITE)

  def on_button_down(self, button, input):
    if   button == Input.BUTTON_L:
      self.frame = 0
      input.stage.screen.set_brightness(max(.1, input.stage.screen.get_brightness() - .05))
    elif button == Input.BUTTON_R:
      self.frame = 0
      input.stage.screen.set_brightness(min( 1, input.stage.screen.get_brightness() + .05))
    elif button == Input.BUTTON_B:
      from arcade.games.settings import Settings
      input.stage.play(Settings)