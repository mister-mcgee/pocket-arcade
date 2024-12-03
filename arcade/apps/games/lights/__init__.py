from arcade.input import Input
from arcade.scene import Scene
from arcade.color import WHITE, BLACK, YELLOW

import random
import ulab.numpy as np

class Lights(Scene):
  def __init__(self):
    self.board  = np.zeros((5, 5), dtype=np.uint8)
    self.cursor = (2, 2)

  def put(self, where, what):
    if self.in_bounds(where):
      self.board[where] = what

  def in_bounds(self, where):
    return (
      where[0] >= 0 and where[0] < 5 and
      where[1] >= 0 and where[1] < 5
    )
  
  def board_at(self, where):
    return self.board[where] if self.in_bounds(where) else 0
  
  def north_of(self, where):
    return (where[0], where[1] - 1)
  
  def west_of(self, where):
    return (where[0] - 1, where[1])
  
  def south_of(self, where):
    return (where[0], where[1] + 1)
  
  def east_of(self, where):
    return (where[0] + 1, where[1])
  
  def toggle_at(self, where):
    self.put(where, self.board_at(where) ^ 1)
  
  def toggle(self, where):
    self.toggle_at(where)
    self.toggle_at(self.north_of(where))
    self.toggle_at(self.west_of (where))
    self.toggle_at(self.south_of(where))
    self.toggle_at(self.east_of (where))

  def toggle_random(self):
    i = random.randint(0, 4)
    j = random.randint(0, 4)
    self.toggle((i, j))

  def draw_board (self, c):    
    c.fill(0)
    for i in range(5):
      for j in range(5):
        c.rect(
          i * 24 + 4,
          j * 24 + 4,
          23, 23, WHITE
        )
        if not self.board_at((i, j)):
          c.rect(
            i * 24 + 5,
            j * 24 + 5,
            21, 21, BLACK
          )

  def draw_cursor(self, c):
    c.rect(
      self.cursor[0] * 24 + 4,
      self.cursor[1] * 24 + 4,
      23, 23, YELLOW
    )
    if not self.board_at(self.cursor):
      c.rect(
        self.cursor[0] * 24 + 6,
        self.cursor[1] * 24 + 6,
        19, 19, BLACK
      )

  def redraw(self, c):
    self.draw_board (c)
    self.draw_cursor(c)

  def on_attach(self, stage):
    for _ in range(10):
      self.toggle_random()
    self.redraw(stage.screen)

  def on_update(self, c):
    pass

  def on_render(self, c):
    pass

  def on_button_down(self, c, button):
    if button == Input.BUTTON_L:
      self.cursor = (
        (self.cursor[0]    ) ,
        (self.cursor[1] + 1) % 5
      )
      self.redraw(c)
    elif button == Input.BUTTON_R:
      self.cursor = (
        (self.cursor[0] + 1) % 5,
        (self.cursor[1]    ) 
      )
      self.redraw(c)
    elif button == Input.BUTTON_A or button == Input.BUTTON_B:
      self.toggle(self.cursor)
      self.redraw(c)
  

