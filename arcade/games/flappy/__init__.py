from arcade.color import BLACK, WHITE
from arcade.font import WHITE_ON_BLACK
from arcade.image import Image
from arcade.scene import Scene

import random

class Bird:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

class Pipe:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

class Flappy(Scene):

  def __init__(self):
    self.flappy_sprite = Image.load("/arcade/games/flappy/flappy.bmp")
    self.gap = 32

  def on_attach(self, stage):
    self.pipes = [
      Pipe(100, random.randint(32 + self.gap//2, 96 - self.gap//2)),
      Pipe(200, random.randint(32 + self.gap//2, 96 - self.gap//2)),
    ]
    self.frame = 0
    self.speed = 1
    self.score = 0
    self.game_over = False

  def update_pipe(self, c, pipe):
    pipe.x -= self.speed

    if pipe.x < -32:
      pipe.x += 200
      pipe.y = random.randint(32 + self.gap//2, 96 - self.gap//2)

  def erase_pipe(self, c, pipe):
    c.rect(pipe.x - 16, 0, 32, 128, BLACK)

  def draw_pipe (self, c, pipe):
    c.image(self.flappy_sprite, pipe.x - 16, pipe.y - 64 - self.gap//2, 0, 48, 32, 64)
    c.image(self.flappy_sprite, pipe.x - 16, pipe.y      + self.gap//2, 0,  0, 32, 64)

  def on_update(self, c):
    pass

  def on_render(self, c):
    for pipe in self.pipes:
      self.erase_pipe (c, pipe)
      self.update_pipe(c, pipe)
      self.draw_pipe  (c, pipe)