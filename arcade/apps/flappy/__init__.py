import random

from arcade.image import Image
from arcade.scene import Scene

from arcade.color import BLACK, WHITE
from arcade.fonts import WHITE_ON_BLACK

class Bird:
  def __init__(self, x=0, y=0):
    self.x  = x
    self.y  = y
    self.vy = 0
    self.ay = 1

class Pipe:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

class Flappy(Scene):

  def __init__(self):
    self.bird_sprite = Image.load("/arcade/apps/flappy/bird.bmp")
    self.pipe_sprite = Image.load("/arcade/apps/flappy/pipe.bmp")
    self.gap = 32    

  def on_attach(self, stage):
    stage.screen.fill(0)
    self.bird  = Bird(64, 64)
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
    c.image(self.pipe_sprite, pipe.x - 16, pipe.y - 64 - self.gap//2, 0, 48, 32, 64)
    c.image(self.pipe_sprite, pipe.x - 16, pipe.y      + self.gap//2, 0,  0, 32, 64)

  def on_update(self, c):
    pass

  def on_render(self, c):
    c.rect(self.bird.x, self.bird.y, 39, 15, BLACK)
    self.bird. y += self.bird.vy
    self.bird.vy += self.bird.ay    
    for pipe in self.pipes:
      self.erase_pipe (c, pipe)
      self.update_pipe(c, pipe)
      self.draw_pipe  (c, pipe)
    c.image(self.bird_sprite, self.bird.x, self.bird.y, 0, 0, 39, 15)

  def on_button_down(self, c, button):
    self.bird.vy = -5