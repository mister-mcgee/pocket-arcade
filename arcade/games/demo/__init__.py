from arcade import Scene, Input, Image, BLACK, WHITE

hold_b = Image("/arcade/games/demo/hold_b.png")
l_up   = Image("/arcade/games/demo/l_up.png")
l_dn   = Image("/arcade/games/demo/l_dn.png")
r_up   = Image("/arcade/games/demo/r_up.png")
r_dn   = Image("/arcade/games/demo/r_dn.png")
a_up   = Image("/arcade/games/demo/a_up.png")
a_dn   = Image("/arcade/games/demo/a_dn.png")
b_up   = Image("/arcade/games/demo/b_up.png")
b_dn   = Image("/arcade/games/demo/b_dn.png")

class Demo(Scene):
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
    pass
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