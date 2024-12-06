class Context:
  def __init__(self, stage):
    self.stage = stage
    self.w = stage.screen.w
    self.h = stage.screen.h

    # timing
    self.t        = 0
    self.dt       = 0
    self.fixed_dt = 0

  def fill(self, c):
    self.stage.screen.fill(c)

  def rect(self, x, y, w, h, c):
    self.stage.screen.rect(x, y, w, h, c)

  def hline(self, x, y, w, c):
    self.stage.screen.hline(x, y, w, c)

  def vline(self, x, y, h, c):
    self.stage.screen.vline(x, y, h, c)

  def image(self, image, x=0, y=0, sx=0, sy=0, sw=None, sh=None, *, a=None):
    self.stage.screen.image(image, x, y, sx, sy, sw, sh, a=a)

  def text(self, atlas, text, x=0, y=0, *, a=None):
    self.stage.screen.text(atlas, text, x, y, a=a)

  def sprite(self, atlas, i=0, x=0, y=0, *, a=None):
    self.stage.screen.sprite(atlas, i, x, y, a=a)

  def is_button_up  (self, button):
    return self.stage.input.is_button_up  (button)

  def is_button_down(self, button):
    return self.stage.input.is_button_down(button)