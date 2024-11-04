from arcade.scene import Scene
from arcade.input import Input
from arcade.image import Image
from arcade.color import BLACK, WHITE

class Debug(Scene):
  def __init__(self):
    self.hold_b = 0

    self.hold_b_sprite = Image("/arcade/games/debug/hold_b.bmp")
    self.l_up_sprite   = Image("/arcade/games/debug/l_up.bmp")
    self.l_dn_sprite   = Image("/arcade/games/debug/l_dn.bmp")
    self.r_up_sprite   = Image("/arcade/games/debug/r_up.bmp")
    self.r_dn_sprite   = Image("/arcade/games/debug/r_dn.bmp")
    self.a_up_sprite   = Image("/arcade/games/debug/a_up.bmp")
    self.a_dn_sprite   = Image("/arcade/games/debug/a_dn.bmp")
    self.b_up_sprite   = Image("/arcade/games/debug/b_up.bmp")
    self.b_dn_sprite   = Image("/arcade/games/debug/b_dn.bmp")

  def on_attach(self, stage):
    stage.screen.fill (BLACK)
    stage.screen.image(self.hold_b_sprite, 16, 4)

  def on_update(self, c):
    if c.input.is_button_down(Input.BUTTON_B):
      self.hold_b += 4
    else:
      self.hold_b  = 0

  def on_render(self, c):
    c.rect(0, 126,         128, 2, BLACK)
    c.rect(0, 126, self.hold_b, 2, WHITE)

    if c.input.is_button_down(Input.BUTTON_L):
      c.image(self.l_dn_sprite, 4, 52)
    else:
      c.image(self.l_up_sprite, 4, 52)

    if c.input.is_button_down(Input.BUTTON_R):
      c.image(self.r_dn_sprite, 34, 52)
    else:
      c.image(self.r_up_sprite, 34, 52)

    if c.input.is_button_down(Input.BUTTON_A):
      c.image(self.a_dn_sprite, 78, 64)
    else:
      c.image(self.a_up_sprite, 78, 64)

    if c.input.is_button_down(Input.BUTTON_B):
      c.image(self.b_dn_sprite, 98, 40)
    else:
      c.image(self.b_up_sprite, 98, 40)