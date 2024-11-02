class RenderContext:
  def __init__(self, stage):
    self.stage    = stage
    self.input    = stage.input
    self.screen   = stage.screen
    self.w        = stage.screen.w
    self.h        = stage.screen.h
    # timing
    self.t        = 0
    self.dt       = 0
    self.fixed_dt = 0
  
  def fill(self, c):
    self.screen.fill(c)

  def rect(self, x, y, w, h, c):
    self.screen.rect(x, y, w, h, c)

  def hline(self, x, y, w, c):
    self.screen.hline(x, y, w, c)

  def vline(self, x, y, h, c):
    self.screen.vline(x, y, h, c)

  def image(self, i, x=0, y=0, sx=0, sy=0, sw=None, sh=None):
    self.screen.image(i, x, y, sx, sy, sw, sh)

  def text(self, font, text, x=0, y=0):
    self.screen.text(font, text, x, y)

class UpdateContext:
  def __init__(self, stage):
    self.stage    = stage
    self.input    = stage.input
    self.screen   = stage.screen
    self.w        = stage.screen.w
    self.h        = stage.screen.h
    # timing
    self.t        = 0
    self.dt       = 0
    self.fixed_dt = 0


class Scene:
  def on_attach (self, stage):
    pass

  def on_detach (self, stage):
    pass

  def on_update(self, c):
    pass

  def on_render(self, c):
    pass

  def on_button_up  (self, button, input=None):
    pass

  def on_button_down(self, button, input=None):
    pass