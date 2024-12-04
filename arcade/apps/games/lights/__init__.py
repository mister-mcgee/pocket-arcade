from arcade.fonts import WHITE_ON_BLACK
from arcade.image import Image
from arcade.atlas import Atlas
from arcade.input import Input
from arcade.scene import Scene
from arcade.color import BLACK, WHITE, color

import random
import ulab.numpy as np

class Lights(Scene):
  def __init__(self):
    self.lamp_sprite = Atlas(Image.load("/arcade/apps/games/lights/lamp.bmp"), 2, 2)
    self.bg = color(51, 60, 87)

  def reset(self):
    self.board  = np.zeros((5, 5), dtype=np.uint8)
    self.cursor = (2, 2)
    self.moves  = 0

    self.complete = False

    for _ in range(10):
      self.toggle_random()

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
  
  def cursor_north(self):
    self.cursor = (
      (self.cursor[0]    )    ,
      (self.cursor[1] + 4) % 5,
    )

  def cursor_south(self):
    self.cursor = (
      (self.cursor[0]    )    ,
      (self.cursor[1] + 1) % 5,
    )

  def cursor_west(self):
    self.cursor = (
      (self.cursor[0] + 4) % 5,
      (self.cursor[1]    )    ,
    )

  def cursor_east(self):
    self.cursor = (
      (self.cursor[0] + 1) % 5,
      (self.cursor[1]    )    ,
    )
  
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

  def on_complete(self, c):
    if np.all(self.board == 0):
      s1 = "Good Night!"
    else:
      s1 = "Good Day!"
    s2 = f"Moves {self.moves}"
    w = max(len(s1), len(s2))

    c.rect(62 - w * 3, 54, w * 6 + 4, 20, WHITE)
    c.rect(63 - w * 3, 55, w * 6 + 2, 18, BLACK)
    c.text(WHITE_ON_BLACK, s1, 64 - len(s1) * 3, 56)
    c.text(WHITE_ON_BLACK, s2, 64 - len(s2) * 3, 64)

  def paint(self, c):    
    c.fill(self.bg)
    for i in range(5):
      for j in range(5):
        x = i * 24 + 4
        y = j * 24 + 4
        if self.cursor == (i, j):
          c.sprite(self.lamp_sprite, self.board_at((i, j)) + 2, x, y)
        else:
          c.sprite(self.lamp_sprite, self.board_at((i, j))    , x, y)

  def on_attach(self, c):
    self.reset( )
    self.paint(c)

  def on_button_down(self, c, button):
    if self.complete:
      self.complete = False
      self.reset( )
      self.paint(c)
      return
    
    if   button == Input.BUTTON_L:
      self.cursor_west()
      self.paint(c)
    elif button == Input.BUTTON_R:
      self.cursor_east()
      self.paint(c)
    elif button == Input.BUTTON_A:  
      self.cursor_south()
      self.paint(c)
    elif button == Input.BUTTON_B:
      self.toggle(self.cursor)
      self.moves += 1
      self.paint(c)

      if (
        np.all(self.board == 0) or
        np.all(self.board == 1)
      ):
        self.complete = True
        self.on_complete(c)
        return
  

