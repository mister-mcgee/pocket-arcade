from arcade.font  import WHITE_ON_BLACK
from arcade.input import Input
from arcade.scene import Scene
from arcade.image import Image
from arcade.color import BLACK

import random
import ulab.numpy as np

class Snake(Scene):
  def __init__(self):
    self.NORTH = 0
    self.WEST  = 1
    self.SOUTH = 2
    self.EAST  = 3

    self.DIRECTION = [
      (0, -1),
      (-1, 0),
      ( 0, 1),
      ( 1, 0),
    ]

    self.apple_sprite     = Image("/arcade/games/snake/apple.bmp")
    self.snake_sprite     = Image("/arcade/games/snake/snake.bmp")
    self.game_over_sprite = Image("/arcade/games/snake/game_over.bmp")
    self.setup()

  def setup(self):
    self.grid  = np.zeros((16, 16), dtype=np.int16)
    self.head  = (8, 8)
    self.tail  = (6, 8)
    self.fruit = (0, 0)

    self.last = 3
    self.next = 3
    self.size = 3

    self.game_over = False

    self.grid[8, 8] = 3
    self.grid[7, 8] = 2
    self.grid[6, 8] = 1

    self.frame = 0

    self.place_fruit()

  def put(self, where, what):
    self.grid[where[0], where[1]] = what

  def in_bounds(self, where):
    return (
      where[0] >= 0 and where[0] < 16 and
      where[1] >= 0 and where[1] < 16
    )
  
  def grid_at(self, where):
    return self.grid[where[0], where[1]] if self.in_bounds(where) else 32767  
  
  def north_of(self, where):
    return (where[0], where[1] - 1)
  
  def west_of (self, where):
    return (where[0] - 1, where[1])
  
  def south_of(self, where):
    return (where[0], where[1] + 1)
  
  def east_of (self, where):
    return (where[0] + 1, where[1])
  
  def adjacent(self, where, direction):
    return (
      where[0] + self.DIRECTION[direction][0],
      where[1] + self.DIRECTION[direction][1],
    )
  
  def place_fruit(self):
    i = random.randint(0, 15)
    j = random.randint(0, 15)
    while self.grid_at((i, j)) > 0:
      i = random.randint(0, 15)
      j = random.randint(0, 15)
    self.fruit = (i, j)

  def on_attach(self, stage):
    stage.screen.fill(0)

    self.draw_head(stage.screen , self.head, 3)
    self.draw_body(stage.screen , (7, 8), 3, 3)
    self.draw_tail(stage.screen , self.tail, 3)
    self.draw_fruit(stage.screen, self.fruit)

  def draw_fruit(self, screen, where):
    i, j = where
    screen.image(self.apple_sprite, i * 8, j * 8, 0, 0, 8, 8)

  def draw_head(self, screen, where, facing):
    i, j = where
    if facing == 0:
      screen.image(self.snake_sprite, i * 8, j * 8,  0, 0, 8, 8)
    elif facing == 1:
      screen.image(self.snake_sprite, i * 8, j * 8,  8, 0, 8, 8)
    elif facing == 2:
      screen.image(self.snake_sprite, i * 8, j * 8, 16, 0, 8, 8)
    elif facing == 3:
      screen.image(self.snake_sprite, i * 8, j * 8, 24, 0, 8, 8)

  def draw_tail(self, screen, where, facing):
    i, j = where
    if facing == 0:
      screen.image(self.snake_sprite, i * 8, j * 8,  0, 8, 8, 8)
    elif facing == 1:
      screen.image(self.snake_sprite, i * 8, j * 8,  8, 8, 8, 8)
    elif facing == 2:
      screen.image(self.snake_sprite, i * 8, j * 8, 16, 8, 8, 8)
    elif facing == 3:
      screen.image(self.snake_sprite, i * 8, j * 8, 24, 8, 8, 8)

  def draw_body(self, screen, where, next, last):
    i, j = where

    if next == self.NORTH:
      if   last == self.NORTH:
        screen.image(self.snake_sprite, i * 8, j * 8, 0, 16, 8, 8)
      elif last == self.WEST:
        screen.image(self.snake_sprite, i * 8, j * 8, 8, 24, 8, 8)
      elif last == self.EAST :
        screen.image(self.snake_sprite, i * 8, j * 8, 8, 32, 8, 8)

    elif next == self.WEST:
      if   last == self.NORTH:
        screen.image(self.snake_sprite, i * 8, j * 8,  0, 32, 8, 8)
      elif last == self.WEST :
        screen.image(self.snake_sprite, i * 8, j * 8,  8, 16, 8, 8)
      elif last == self.SOUTH:
        screen.image(self.snake_sprite, i * 8, j * 8, 16, 24, 8, 8)

    elif next == self.SOUTH:
      if   last == self.WEST :
        screen.image(self.snake_sprite, i * 8, j * 8, 24, 32, 8, 8)
      elif last == self.SOUTH:
        screen.image(self.snake_sprite, i * 8, j * 8, 16, 16, 8, 8)
      elif last == self.EAST :
        screen.image(self.snake_sprite, i * 8, j * 8, 24, 24, 8, 8)

    elif next == self.EAST:
      if   last == self.NORTH:
        screen.image(self.snake_sprite, i * 8, j * 8,  0, 24, 8, 8)
      elif last == self.EAST :
        screen.image(self.snake_sprite, i * 8, j * 8, 24, 16, 8, 8)
      elif last == self.SOUTH:
        screen.image(self.snake_sprite, i * 8, j * 8, 16, 32, 8, 8)

  def on_button_down(self, button, input):
    if self.game_over:
      self.setup()
      self.on_attach(input.stage)
      return
    
    if   button == Input.BUTTON_L or button == Input.BUTTON_A:
      self.next = (self.last + 1) % 4
    elif button == Input.BUTTON_R or button == Input.BUTTON_B:
      self.next = (self.last + 3) % 4

  def on_update(self, c):
    pass

  def on_render(self, c):
    if self.game_over:
      return
    
    if self.frame % 3 == 0:
      self.grid -= 1

      # check for game over
      if self.grid_at(self.adjacent(self.head, self.next)) > 0:
        c.image(self.game_over_sprite, 32, 60)
        c.text(WHITE_ON_BLACK, f"Score: {self.size}", 32, 68)
        self.game_over = True
        return
      
      # erase the tail
      c.rect(self.tail[0] * 8, self.tail[1] * 8, 8, 8, BLACK)

      # move the tail
      if   self.grid_at(self.north_of(self.tail)) == 1:
        self.tail = self.north_of(self.tail)
      elif self.grid_at(self.west_of (self.tail)) == 1:
        self.tail = self.west_of(self.tail)
      elif self.grid_at(self.south_of(self.tail)) == 1:
        self.tail = self.south_of(self.tail)
      elif self.grid_at(self.east_of (self.tail)) == 1:
        self.tail = self.east_of(self.tail)

      # draw the tail
      if   2 <= self.grid_at(self.north_of(self.tail)) <= 3:
        self.draw_tail(c, self.tail, self.NORTH)
      elif 2 <= self.grid_at(self.west_of (self.tail)) <= 3:
        self.draw_tail(c, self.tail, self.WEST )
      elif 2 <= self.grid_at(self.south_of(self.tail)) <= 3:
        self.draw_tail(c, self.tail, self.SOUTH)
      elif 2 <= self.grid_at(self.east_of (self.tail)) <= 3:
        self.draw_tail(c, self.tail, self.EAST )

      # draw the body
      self.draw_body(c, self.head, self.last, self.next)

      # move the head
      self.head = self.adjacent(self.head, self.next)
      self.put(
        self.head,
        self.size
      )

      if self.head == self.fruit:
        self.size += 1
        self.place_fruit()
        self.draw_fruit(c, self.fruit)
      
      # draw the head
      self.draw_head(c, self.head, self.next) 

      self.last = self.next

    self.frame += 1



    


  

    