from arcade.image import Image

class Font:
  def __init__(self, 
    path, 
    cols= 5,
    rows=19
  ):
    self.atlas = Image(path)
    self.cols  = cols
    self.rows  = rows
    self.col_w = self.atlas.w // cols
    self.row_h = self.atlas.h // rows

  def draw_char(self, c, char, x=0, y=0):
    n = ord(char) - 32
    i = n  % self.cols
    j = n // self.cols
    c.image(self.atlas, x, y, i * self.col_w, j * self.row_h, self.col_w, self.row_h)

  def draw_text(self, c, text, x=0, y=0):
    for char in text:
      self.draw_char(c, char, x, y)
      x += self.col_w

BLACK_ON_WHITE = Font("/arcade/fonts/black_on_white.bmp")
WHITE_ON_BLACK = Font("/arcade/fonts/white_on_black.bmp")