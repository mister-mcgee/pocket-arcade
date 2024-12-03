from arcade.scene import Scene
from arcade.image import Image
from arcade.input import Input
from arcade.color import WHITE, BLACK
from arcade.fonts import BLACK_ON_WHITE

class Diagnostic(Scene):
  def __init__(self):
    self.hold_b = 0
    
    self.l_up_sprite = Image.load("/arcade/apps/system/settings/diagnostic/l_up.bmp")
    self.l_dn_sprite = Image.load("/arcade/apps/system/settings/diagnostic/l_dn.bmp")
    self.r_up_sprite = Image.load("/arcade/apps/system/settings/diagnostic/r_up.bmp")
    self.r_dn_sprite = Image.load("/arcade/apps/system/settings/diagnostic/r_dn.bmp")
    self.a_up_sprite = Image.load("/arcade/apps/system/settings/diagnostic/a_up.bmp")
    self.a_dn_sprite = Image.load("/arcade/apps/system/settings/diagnostic/a_dn.bmp")
    self.b_up_sprite = Image.load("/arcade/apps/system/settings/diagnostic/b_up.bmp")
    self.b_dn_sprite = Image.load("/arcade/apps/system/settings/diagnostic/b_dn.bmp")

  def on_attach(self, c):
    c.fill(0)
    c.rect(0, 0, 128, 10, WHITE)
    c.text(BLACK_ON_WHITE, "Diagnostic", 34, 1)

  def on_update(self, c):
    if c.is_button_down(Input.BUTTON_B):
      self.hold_b += 8
    else:
      self.hold_b  = 0

    if self.hold_b > 128:
      from arcade.apps.system.settings import Settings
      c.stage.play(Settings)

  def on_render(self, c):
    c.rect(0, 126,         128, 2, BLACK)
    c.rect(0, 126, self.hold_b, 2, WHITE)

    c.rect(116, 0, 12, 10, WHITE)
    c.text(BLACK_ON_WHITE, str(c.stage.m_fps), 116, 1)

    if c.is_button_down(Input.BUTTON_L):
      c.image(self.l_dn_sprite, 4, 52)
    else:
      c.image(self.l_up_sprite, 4, 52)

    if c.is_button_down(Input.BUTTON_R):
      c.image(self.r_dn_sprite, 34, 52)
    else:
      c.image(self.r_up_sprite, 34, 52)

    if c.is_button_down(Input.BUTTON_A):
      c.image(self.a_dn_sprite, 78, 64)
    else:
      c.image(self.a_up_sprite, 78, 64)

    if c.is_button_down(Input.BUTTON_B):
      c.image(self.b_dn_sprite, 98, 40)
    else:
      c.image(self.b_up_sprite, 98, 40)
