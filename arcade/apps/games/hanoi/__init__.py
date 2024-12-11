


from arcade.input import Input
from arcade.scene import Scene

from arcade.color import color


class Hanoi(Scene):
  def __init__(self):
    pass

  def reset(self):
    self.colors=[
      color(255,   0,   0),
      color(255, 255,   0),
      color(  0, 255,   0),
      color(  0, 255, 255),
      color(  0,   0, 255),
      color(255,   0, 255)
    ]
    self.towers= [
      [5, 4, 3, 2, 1],
      [],
      []
    ]

    self.hover      = -1
    self.selected_a = -1
    self.selected_b = -1

  def paint_tower(self, c, tower, x, y):
    for i, disk in enumerate(tower):
      c.rect(x - disk * 4, y - i * 4, disk * 8, 4, self.colors[disk - 1])

  def paint(self, c):
    c.fill(0)
    self.paint_tower(c, self.towers[0],   22, 64)
    self.paint_tower(c, self.towers[1],   62, 64)
    self.paint_tower(c, self.towers[2],  102, 64)

    # self.rect(self.hover * 40 - 20)
  def on_attach(self, c):
    self.reset( )
    self.paint(c)

  def on_button_down(self, c, button):
    if   button == Input.BUTTON_L:
      self.hover = (self.hover + len(self.towers) - 1) % len(self.towers)
      self.paint(c)
    elif button == Input.BUTTON_R:
      self.hover = (self.hover                     + 1) % len(self.towers)
      self.paint(c)