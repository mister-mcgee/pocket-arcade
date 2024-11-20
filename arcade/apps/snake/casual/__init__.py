import random
import ulab.numpy as np

from arcade.scene import Scene
from arcade.input import Input
from arcade.image import Image
from arcade.atlas import Atlas

from arcade.color import WHITE, BLACK
from arcade.fonts import WHITE_ON_BLACK

class Casual(Scene):
  def __init__(self):
    self.snake_sprite = Atlas(Image.load("/arcade/apps/snake/snake.bmp"), 16, 5)
    
    self.DIRECTION = [
      ( 0,  0),
      ( 0, -1),
      (-1,  0),
      ( 0,  1),
      ( 1,  0)
    ]

    self.FROM_SOUTH =  1
    self.FROM_EAST  =  2
    self.FROM_NORTH =  3
    self.FROM_WEST  =  4

    self.TO_NORTH   = 16
    self.TO_WEST    = 32
    self.TO_SOUTH   = 48
    self.TO_EAST    = 64

    self.ON_LITE    =  0
    self.ON_DARK    =  8

    self.FRUIT_0 =  5
    self.FRUIT_1 =  6
    self.FRUIT_2 =  7
    self.FRUIT_3 = 21
    self.FRUIT_4 = 22
    self.FRUIT_5 = 23
    self.ICON    = 48
    self.SCORE   = 79

    self.FRUITS = [
      self.FRUIT_0,
      self.FRUIT_1,
      self.FRUIT_2,
      self.FRUIT_3,
      self.FRUIT_4,
      self.FRUIT_5
    ]

  def reset(self, c):
    self.grid = np.zeros((16, 15), dtype=np.uint8)

    self.grid[8, 7] =                self.FROM_WEST
    self.grid[7, 7] = self.TO_EAST | self.FROM_WEST
    self.grid[6, 7] = self.TO_EAST

    self.frame   = 0
    self.score   = 0
    self.fruit_0 = 0
    self.fruit_1 = 0
    self.fruit_2 = 0
    self.fruit_3 = 0
    self.fruit_4 = 0
    self.fruit_5 = 0

    self.last_move = self.FROM_WEST
    self.next_move = self.FROM_WEST
    self.head = (8, 7)
    self.tail = (6, 7)

    self.paint_board(c)
    self.paint_score(c)
    self.place_fruit(c)

    self.game_over = False
    self.hold_b    =     0

  def on_attach(self, c):
    self.reset(c)  

  def relative(self, where, to):
    return (
      where[0] + self.DIRECTION[to][0],
      where[1] + self.DIRECTION[to][1]
    )

  def in_bounds(self, where):
    return (
      0 <= where[0] < 16 and 
      0 <= where[1] < 15
    )

  def at(self, where):
    return self.grid[where] if self.in_bounds(where) else 127

  def paint_cell(self, c, where):
    cell = self.grid[where]
    if (where[0] + where[1]) & 1:
      cell |= self.ON_DARK
    c.sprite(
      self.snake_sprite, 
      cell, 
      where[0] * 8, 
      where[1] * 8
    )

  def paint_board(self, c):
    for i in range(16):
      for j in range(15):
        self.paint_cell(c, (i, j))

  def paint_score(self, c):
    c.rect(0, 120, 128, 8, 0)
    c.text(WHITE_ON_BLACK, self.score, 10, 121)
    c.sprite(self.snake_sprite, self.SCORE, 0, 120)

  def place_fruit(self, c):
    i = random.randint(0, 15)
    j = random.randint(0, 14)
    while self.grid[i, j] != 0:
      i = random.randint(0, 15)
      j = random.randint(0, 14)
    self.grid[i, j] = self.FRUITS[random.randint(0, 5)]
    self.paint_cell(c, (i, j))

  def paint_game_over(self, c):
    c.rect(35, 58, 58, 20, WHITE)
    c.rect(36, 59, 56, 18, BLACK)

    score = str(self.score)    
    c.text(WHITE_ON_BLACK, "Game Over", 37, 60)    
    c.text(WHITE_ON_BLACK, score, 64 - len(score) * 3, 68)
    c.sprite(self.snake_sprite, self.SCORE, 54 - len(score) * 3, 68)

    c.rect(0, 118, 128, 10, 0)

    c.sprite(self.snake_sprite, self.FRUIT_0 + self.ICON,  1, 118)
    c.text(WHITE_ON_BLACK, self.fruit_0, 10, 119)

    c.sprite(self.snake_sprite, self.FRUIT_1 + self.ICON, 22, 118)
    c.text(WHITE_ON_BLACK, self.fruit_1, 31, 119)

    c.sprite(self.snake_sprite, self.FRUIT_2 + self.ICON, 43, 118)
    c.text(WHITE_ON_BLACK, self.fruit_2, 52, 119)

    c.sprite(self.snake_sprite, self.FRUIT_3 + self.ICON, 64, 118)
    c.text(WHITE_ON_BLACK, self.fruit_3, 73, 119)

    c.sprite(self.snake_sprite, self.FRUIT_4 + self.ICON, 85, 118)
    c.text(WHITE_ON_BLACK, self.fruit_4, 94, 119)

    c.sprite(self.snake_sprite, self.FRUIT_5 + self.ICON, 106, 118)
    c.text(WHITE_ON_BLACK, self.fruit_5, 115, 119)

  def update_tail(self, c):
    next_move = (self.grid[self.tail] & 0x70) >> 4

    # erase the tail
    self.grid[self.tail] = 0
    self.paint_cell(c, self.tail)

    # move the tail
    self.tail = self.relative(self.tail, next_move)

    # paint the tail
    self.grid[self.tail] &= 0x70
    self.paint_cell(c, self.tail)

  def update_head(self, c):
    # erase the head
    self.grid[self.head] |= self.next_move << 4
    self.paint_cell(c, self.head)

    # move the head
    self.head = self.relative(self.head, self.next_move)

    # paint the head
    self.grid[self.head] = self.next_move
    self.paint_cell(c, self.head)

    # update last move
    self.last_move = self.next_move

  def on_update(self, c):
    if self.game_over:
      if (
        c.is_button_down(Input.BUTTON_L) or
        c.is_button_down(Input.BUTTON_R) or
        c.is_button_down(Input.BUTTON_A) or
        c.is_button_down(Input.BUTTON_B)
      ):
        self.hold_b += 4
      else:
        self.hold_b  = 0

      if self.hold_b > 128:
        self.reset(c)

  def on_render(self, c):
    if self.game_over: 
      c.rect(0, 126,         128, 2, BLACK)
      c.rect(0, 126, self.hold_b, 2, WHITE)
      return
    
    if self.frame % 3 == 0:
      cell = self.at(self.relative(self.head, self.next_move))

      if cell == 0:
        self.update_tail(c)
        self.update_head(c)
      elif (
        cell == self.FRUIT_0 or
        cell == self.FRUIT_1 or
        cell == self.FRUIT_2 or
        cell == self.FRUIT_3 or
        cell == self.FRUIT_4 or
        cell == self.FRUIT_5
      ):
        self.score += 1
        if cell == self.FRUIT_0: self.fruit_0 += 1
        if cell == self.FRUIT_1: self.fruit_1 += 1
        if cell == self.FRUIT_2: self.fruit_2 += 1
        if cell == self.FRUIT_3: self.fruit_3 += 1
        if cell == self.FRUIT_4: self.fruit_4 += 1
        if cell == self.FRUIT_5: self.fruit_5 += 1
        self.update_head(c)
        self.paint_score(c)
        self.place_fruit(c)
      else:
        n = self.at(self.relative(self.head, self.FROM_SOUTH))
        s = self.at(self.relative(self.head, self.FROM_NORTH))
        e = self.at(self.relative(self.head, self.FROM_WEST ))
        w = self.at(self.relative(self.head, self.FROM_EAST ))

        n = n == 0 or n == self.FRUIT_0 or n == self.FRUIT_1 or n == self.FRUIT_2 or n == self.FRUIT_3 or n == self.FRUIT_4 or n == self.FRUIT_5
        s = s == 0 or s == self.FRUIT_0 or s == self.FRUIT_1 or s == self.FRUIT_2 or s == self.FRUIT_3 or s == self.FRUIT_4 or s == self.FRUIT_5
        e = e == 0 or e == self.FRUIT_0 or e == self.FRUIT_1 or e == self.FRUIT_2 or e == self.FRUIT_3 or e == self.FRUIT_4 or e == self.FRUIT_5
        w = w == 0 or w == self.FRUIT_0 or w == self.FRUIT_1 or w == self.FRUIT_2 or w == self.FRUIT_3 or w == self.FRUIT_4 or w == self.FRUIT_5

        if not (n or s or e or w):
          self.game_over  =  True
          self.paint_game_over(c)
          return

    self.frame += 1

  def on_button_down(self, c, button):
    if button == Input.BUTTON_L:
      self.next_move = ((self.last_move - 1) + 1) % 4 + 1
    if button == Input.BUTTON_R:
      self.next_move = ((self.last_move - 1) + 3) % 4 + 1

