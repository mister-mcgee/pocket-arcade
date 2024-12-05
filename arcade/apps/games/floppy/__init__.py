import gc
import random
import math

from arcade.image import Image
from arcade.input import Input
from arcade.scene import Scene

from arcade.color import WHITE, BLACK, RED
from arcade.fonts import WHITE_ON_BLACK

class Floppy(Scene):
  class Disk:
    def __init__(self):
      self.x  = 64
      self.y  = 64
      self.vy = -5
      self.ay =  1

  class Plug:
    def __init__(self, x=0, y=64, gap=80):
      self.x = x
      self.y = y
      self.     gap = gap
      self.half_gap = gap // 2

    def set_gap(self, gap):
      self.     gap = gap
      self.half_gap = gap // 2

  class Spark:
    def __init__(self, x=0, y=0):
      self.x = x
      self.y = y
      self.vx = 0
      self.vy = 0
      self.ay = 1
      self.t  = -1

  def __init__(self):
    self.disk_sprite = Image.load("/arcade/apps/games/floppy/disk.bmp")
    self.plug_sprite = Image.load("/arcade/apps/games/floppy/plug.bmp")
    self.bg = self.plug_sprite.buffer[0, 0]

  def on_attach(self, c):
    c.fill(self.bg)
    self.reset()
    

  def random_height(self, gap=80):
    return random.randint(
      16  + gap // 2,
      112 - gap // 2
    )

  def reset(self):
    self.hold_any = 0
    self.speed =  2
    self.score =  0
    self.frame =  0
    self.game_over = False
  
    self.disk = Floppy.Disk()
    self.plugs = [
      Floppy.Plug(112, self.random_height(64), 64),
      Floppy.Plug(212, self.random_height(63), 63),
      Floppy.Plug(312, self.random_height(62), 62),
    ]

    self.sparks = [
      Floppy.Spark(),
      Floppy.Spark(),
      Floppy.Spark(),
      Floppy.Spark(),
      Floppy.Spark(),
      Floppy.Spark(),
      Floppy.Spark(),
      Floppy.Spark()
    ]

  def is_disk_outside (self, disk      ):
    return disk.y < 0 or disk.y > 128

  def is_disk_touching(self, disk, plug):
    return (
      disk.x - 8 < plug.x + 16 and 
      disk.x + 8 > plug.x - 16 and
      (
        disk.y < plug.y - plug.half_gap or
        disk.y > plug.y + plug.half_gap
      )
    )

  def draw_plug(self, c, plug):
    c.image(self.plug_sprite, plug.x - 16, 0, 0, 116 - plug.y + plug.half_gap, 32, plug.y - plug.half_gap + 16)
    c.image(self.plug_sprite, plug.x - 16, plug.y + plug.half_gap - 16, 0, 0, 32, 144 - plug.y - plug.half_gap)

  def draw_disk(self, c, disk):
    c.image(self.disk_sprite, disk.x - 8, disk.y - 8)

  def draw_spark(self, c, spark):
    c.rect(spark.x - 1, spark.y - 1, 2, 2, WHITE)

  def spawn_spark(self, x, y):
    for spark in self.sparks:
      if spark.t < 0:
        a = - random.random() * math.pi
        spark.t = 8
        spark.x = x
        spark.y = y
        spark.vx = 3 * math.cos(a)
        spark.vy = 6 * math.sin(a)
        return

  def on_game_over(self, c):
    s1 = "Game Over"
    s2 = f"Score {self.score}"
    w = max(len(s1), len(s2))

    c.rect(62 - w * 3, 54, w * 6 + 4, 20, WHITE)
    c.rect(63 - w * 3, 55, w * 6 + 2, 18, BLACK)
    c.text(WHITE_ON_BLACK, s1, 64 - len(s1) * 3, 56)
    c.text(WHITE_ON_BLACK, s2, 64 - len(s2) * 3, 64)

  def on_render(self, c):
    if self.game_over:
      c.rect(0, 126,           128, 2, self.bg)
      c.rect(0, 126, self.hold_any, 2, RED    )
      return

    # erase elements
    for spark in self.sparks:
      c.rect(spark.x - 1, spark.y - 1, 2, 2, self.bg)
    for plug in self.plugs:
      c.rect(plug.x - self.speed + 16, 0, self.speed, 128, self.bg)
    c.rect(self.disk.x - 8, self.disk.y - 8, 16, 16, self.bg)

    # update and draw plugs
    for plug in self.plugs:
      plug.x -= self.speed
      if plug.x < -16:
        plug.x     += 300
        self.score +=   1
        plug.set_gap(max(64 - self.score , 32))
        plug.y = self.random_height( plug.gap )
      self.draw_plug(c, plug)

    # update and draw disk
    self.disk.vy += self.disk.ay
    self.disk. y += self.disk.vy
    self.draw_disk(c, self.disk)

    # check if disk is outside
    if self.is_disk_outside(self.disk):
      self.game_over = True
      self.on_game_over(c)
      return
    
    # check if disk is touching a plug
    for plug in self.plugs:
      if (
        self.disk.x - 8 < plug.x + 16 and 
        self.disk.x + 8 > plug.x - 16
      ):
        if (
          self.disk.y - 8 < plug.y - plug.half_gap or
          self.disk.y + 8 > plug.y + plug.half_gap
        ):          
          self.game_over = True
          self.on_game_over(c)
          return
        elif self.disk.y - 8 < plug.y - plug.half_gap + 16:
          self.spawn_spark(self.disk.x, self.disk.y - 8)
        elif self.disk.y + 8 > plug.y + plug.half_gap - 16:
          self.spawn_spark(self.disk.x, self.disk.y + 8)

    # update and draw sparks
    for spark in self.sparks:
      if spark.t < 0:
        continue
      spark.vy += spark.ay
      spark.x  += spark.vx
      spark.y  += spark.vy
      spark.t  -= 1
      self.draw_spark(c, spark)

  def on_update(self, c):
    if self.game_over:
      if (
        c.is_button_down(Input.BUTTON_L) or
        c.is_button_down(Input.BUTTON_R) or
        c.is_button_down(Input.BUTTON_A) or
        c.is_button_down(Input.BUTTON_B)
      ):
        self.hold_any += 8
      else:
        self.hold_any  = 0
      
      if self.hold_any >= 128:
        c.fill(self.bg)
        self.reset(   )

  def on_button_down(self, c, button):
    self.disk.vy = -6

    

  
