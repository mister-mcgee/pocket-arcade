from arcade.image import Image

class Font:
  def __init__(self, 
    atlas, 
    cols= 5,
    rows=19
  ):
    self.atlas = atlas
    self.cols  = cols
    self.rows  = rows
    self.col_w = self.atlas.w // cols
    self.row_h = self.atlas.h // rows

  def load(path, cols=5, rows=19):
    atlas    =    Image.load(path)
    return Font(atlas, cols, rows)

  def draw(self, c, text, x=0, y=0):
    for char in text:
      n = ord(char) - 32
      i = n  % self.cols
      j = n // self.cols
      c.image(self.atlas, x, y, i * self.col_w, j * self.row_h, self.col_w, self.row_h)
      x += self.col_w

BLACK_ON_WHITE = Font.load("/arcade/fonts/black_on_white.bmp")
WHITE_ON_BLACK = Font.load("/arcade/fonts/white_on_black.bmp")