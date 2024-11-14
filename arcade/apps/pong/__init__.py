from arcade.input import Input
from arcade.scene import Scene

from arcade.color import WHITE, BLACK

class Pong(Scene):
  def __init__(self):
    self.paddle1_x = 64
    self.paddle2_x = 64
    self.ball_x  = 64
    self.ball_y  = 64
    self.ball_vx =  1
    self.ball_vy =  1

  def on_update(self, c):
    if c.is_button_down(Input.BUTTON_L):
      self.paddle1_x = max( 12, self.paddle1_x - 4)

    if c.is_button_down(Input.BUTTON_R):
      self.paddle1_x = min(116, self.paddle1_x + 4)

    self.ball_x += self.ball_vx
    self.ball_y += self.ball_vy

    if self.ball_x < 6 or self.ball_x > 122:
      self.ball_vx *= -1

    if self.ball_y < 6 or self.ball_y > 122:
      self.ball_vy *= -1

  def on_render(self, c):
    c.fill(0)

    c.rect(self.paddle2_x - 12,   1, 24, 6, WHITE)
    c.rect(self.paddle1_x - 12, 121, 24, 6, WHITE)
    c.rect(
      self.ball_x - 3,
      self.ball_y - 3,
      6, 6, WHITE
    )

