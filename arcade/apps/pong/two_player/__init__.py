from arcade.image import Image
from arcade.input import Input
from arcade.scene import Scene

from arcade.color import BLACK, WHITE
from arcade.fonts import WHITE_ON_BLACK

import random

class TwoPlayer(Scene):
  def __init__(self):    
    self.zone_sprite = Image.load("/arcade/apps/pong/zone.bmp")
    self.pong_sprite = Image.load("/arcade/apps/pong/pong.bmp")

  def on_attach(self, c):
    self.x    = 64
    self.y    = 64
    self.vx   =  0
    self.vy   =  0
    self.p1_x = 64
    self.p2_x = 64
    self.p1_score = 0
    self.p2_score = 0
    self.p2_mode  = 0 # center
    self.suspended = True
    c.fill(0)

    c.image(self.zone_sprite, 0, 63, 0, 16, 128, 2)
    c.text(WHITE_ON_BLACK, "2 Player", 40, 60)

    if random.random() < 0.5:
      self.p1_serve()
    else:
      self.p2_serve()

  def p1_wins(self, c):
    self.suspended = True
    c.rect(41, 60, 46, 8, 0)
    c.text(WHITE_ON_BLACK, "P1 Wins", 43, 60)

  def p2_wins(self, c):
    self.suspended = True
    c.rect(41, 60, 46, 8, 0)
    c.text(WHITE_ON_BLACK, "P2 Wins", 43, 60)

  def p1_serve(self):
    self.x = 64
    self.y = 64
    self.vx =  0
    self.vy = -4

  def p2_serve(self):
    self.x = 64
    self.y = 64
    self.vx = 0
    self.vy = 4

  def on_button_down(self, c, button):
    if self.suspended:
      c.fill(0)
      self.p1_score = 0
      self.p2_score = 0
      self.suspended  =  False

  def on_render(self, c):
    # draw the zones
    c.image(self.zone_sprite, 0,   0, 0,  8, 128, 8)
    c.image(self.zone_sprite, 0, 120, 0,  0, 128, 8)

    if not self.suspended:
      # erase the ball
      c.rect(self.x - 4, self.y - 4, 8, 8, 0)

    # update the paddles
    if c.is_button_down(Input.BUTTON_L):
      self.p1_x = max( 16, self.p1_x - 4)

    if c.is_button_down(Input.BUTTON_R):
      self.p1_x = min(112, self.p1_x + 4)
    
    if c.is_button_down(Input.BUTTON_A):
      self.p2_x = max( 16, self.p2_x - 4)

    if c.is_button_down(Input.BUTTON_B):
      self.p2_x = min(112, self.p2_x + 4)

    if not self.suspended:
      # update the ball
      self.x += self.vx
      self.y += self.vy

      if self.x < 4 or self.x > 124:
        if self.x <   4: self.x =   4
        if self.x > 124: self.x = 124
        self.vx *= -1

      if(
        self.x + 4 >= self.p1_x - 16 and
        self.x - 4 <= self.p1_x + 16 and
        self.y >= 116
      ):
        self.y  = 116
        self.vy *= -1
        self.vx = (self.x - self.p1_x) / 4

      if(
        self.x + 4 >= self.p2_x - 16 and
        self.x - 4 <= self.p2_x + 16 and
        self.y <= 12
      ):
        self.y  = 12
        self.vy *= -1
        self.vx = (self.x - self.p2_x) / 4
      
      if self.y <  12:
        self.p1_score += 1
        self.p2_serve()

      if self.y > 116:
        self.p2_score += 1
        self.p1_serve()

    # draw the scores
    s1 = str(self.p1_score)
    s2 = str(self.p2_score)
    c.text(WHITE_ON_BLACK, s1, 64 - len(s1) * 3, 92)
    c.text(WHITE_ON_BLACK, s2, 64 - len(s2) * 3, 28)

    # draw the paddles
    c.image(self.pong_sprite, self.p2_x - 16,   0, 32, 0, 32, 8)
    c.image(self.pong_sprite, self.p1_x - 16, 120,  0, 0, 32, 8)

    if not self.suspended:
      c.image(self.zone_sprite, 0,  63, 0, 16, 128, 2)
      # draw the ball
      c.image(self.pong_sprite, self.x - 4, self.y - 4, 64, 0, 8, 8)

    if self.p1_score >= 11:
      self.p1_wins(c)

    if self.p2_score >= 11:
      self.p2_wins(c)



