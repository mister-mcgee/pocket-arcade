class RenderContext:
  def __init__(self, stage):
    self.stage    = stage
    self.input    = stage.input
    self.canvas   = stage.canvas
    self.w        = stage.cfg_w
    self.h        = stage.cfg_h
    # timing
    self.t        = 0
    self.dt       = 0
    self.fixed_dt = 0
  
  def fill(self, c):
    self.canvas.fill(c)

  def rect(self, x, y, w, h, c):
    self.canvas.rect(x, y, w, h, c)

  def hline(self, x, y, w, c):
    self.canvas.hline(x, y, w, c)

  def vline(self, x, y, h, c):
    self.canvas.vline(x, y, h, c)

  def image(self, i, x=0, y=0, sx=0, sy=0, sw=None, sh=None):
    self.canvas.image(i, x, y, sx, sy, sw, sh)

class UpdateContext:
  def __init__(self, stage):
    self.stage    = stage
    self.input    = stage.input
    self.w        = stage.cfg_w
    self.h        = stage.cfg_h
    self.canvas   = stage.canvas
    # timing
    self.t        = 0
    self.dt       = 0
    self.fixed_dt = 0


class Scene:
  def on_attach (self, stage  ):
    pass

  def on_detach (self, stage  ):
    pass

  def on_update(self, context):
    pass

  def on_render(self, context):
    pass

  def on_button_up  (self, input, id):
    pass

  def on_button_down(self, input, id):
    pass