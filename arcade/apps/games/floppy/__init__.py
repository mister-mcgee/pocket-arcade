import random

from arcade.image import Image
from arcade.scene import Scene

from arcade.color import color, BLACK, WHITE
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

class Floppy(Scene):
  def __init__(self):
    self.bg  = color(115, 198, 225)
    self.bird_sprite = Image.load("/arcade/apps/games/floppy/bird.bmp")
    self.pipe_sprite = Image.load("/arcade/apps/games/floppy/pipe.bmp")
    self.gap = 32
    self.bird  = Bird(64 , 64)
    self.pipes = [
      Pipe(100, random.randint(32 + self.gap//2, 96 - self.gap//2)),
      Pipe(200, random.randint(32 + self.gap//2, 96 - self.gap//2)),
    ]
    self.speed = 1
    self.frame = 0
    self.score = 0
    self.game_over = False

  def on_attach(self, c):
    c.fill(self.bg)

  def update_pipe(self, c, pipe):
    pipe.x -= self.speed

    if pipe.x < -32:
      pipe.x += 200
      pipe.y = random.randint(32 + self.gap//2, 96 - self.gap//2)

  def erase_pipe(self, c, pipe):
    c.rect(pipe.x + 15, 0, 1, 128, self.bg)

  def draw_pipe (self, c, pipe):
    c.image(self.pipe_sprite, pipe.x - 16, pipe.y - 64 - self.gap//2, 0, 48, 32, 64)
    c.image(self.pipe_sprite, pipe.x - 16, pipe.y      + self.gap//2, 0,  0, 32, 64)

  def on_update(self, c):
    pass

  def on_render(self, c):
    # erase the bird
    c.rect(self.bird.x - 8, self.bird.y - 8, 16, 16, self.bg)
    
    # move the bird
    self.bird. y += self.bird.vy
    self.bird.vy += self.bird.ay

    # handle pipes
    for pipe in self.pipes:
      self.erase_pipe (c, pipe)
      self.update_pipe(c, pipe)
      self.draw_pipe  (c, pipe)

    # draw bird
    c.image(self.bird_sprite, self.bird.x - 8, self.bird.y - 8)

  def on_button_down(self, c, button):
    self.bird.vy = -5