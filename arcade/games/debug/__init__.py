import gc

from arcade.scene import Scene
from arcade.input import Input
from arcade.image import Image
from arcade.color import BLACK, WHITE

hold_b = Image("/arcade/games/debug/hold_b.bmp")
l_up   = Image("/arcade/games/debug/l_up.bmp")
l_dn   = Image("/arcade/games/debug/l_dn.bmp")
r_up   = Image("/arcade/games/debug/r_up.bmp")
r_dn   = Image("/arcade/games/debug/r_dn.bmp")
a_up   = Image("/arcade/games/debug/a_up.bmp")
a_dn   = Image("/arcade/games/debug/a_dn.bmp")
b_up   = Image("/arcade/games/debug/b_up.bmp")
b_dn   = Image("/arcade/games/debug/b_dn.bmp")

class Debug(Scene):
  def __init__(self):
    self.hold_b = 0

  def on_attach(self, stage):
    stage.screen.fill (BLACK)
    stage.screen.image(hold_b, 16, 4)

  def on_update(self, c):
    if c.input.is_button_down(Input.BUTTON_B):
      self.hold_b += 4
    else:
      self.hold_b  = 0

  def on_render(self, c):
    c.rect(0, 126,         128, 2, BLACK)
    c.rect(0, 126, self.hold_b, 2, WHITE)

    if c.input.is_button_down(Input.BUTTON_L):
      c.image(l_dn, 4, 52)
    else:
      c.image(l_up, 4, 52)

    if c.input.is_button_down(Input.BUTTON_R):
      c.image(r_dn, 34, 52)
    else:
      c.image(r_up, 34, 52)

    if c.input.is_button_down(Input.BUTTON_A):
      c.image(a_dn, 78, 64)
    else:
      c.image(a_up, 78, 64)

    if c.input.is_button_down(Input.BUTTON_B):
      c.image(b_dn, 98, 40)
    else:
      c.image(b_up, 98, 40)

    gc.collect()