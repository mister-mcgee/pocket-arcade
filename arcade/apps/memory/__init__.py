from arcade.scene import Scene
from arcade.image import Image
from arcade.atlas import Atlas


class Memory(Scene):


  def __init__(self):
    self.card_sprite = Atlas(Image.load("/arcade/apps/memory/card.bmp"), 7, 1)

    self.FACE_DOWN = 0b0000
    self.FACE_UP   = 0b1000

    self.CARD_W = 17
    self.CARD_H = 26

    self.cards = [
      1 | self.FACE_DOWN, 1 | self.FACE_DOWN,
      2 | self.FACE_DOWN, 2 | self.FACE_DOWN, 
      3 | self.FACE_DOWN, 3 | self.FACE_DOWN,
      4 | self.FACE_DOWN, 4 | self.FACE_DOWN,
      5 | self.FACE_DOWN, 5 | self.FACE_DOWN,
      6 | self.FACE_DOWN, 6 | self.FACE_DOWN
    ]
  
  def on_attach(self, c):
    c.fill(0)
    self.paint(c)

  def paint_card(self, c, card, x=0, y=0):
    if card & self.FACE_UP:
      c.sprite(self.card_sprite, card & 0x7, x, y)
    else:
      c.sprite(self.card_sprite,          0, x, y)

  def paint(self, c):
    for i, card in enumerate(self.cards):
      x = (i  % 4) * 32 + 8
      y = (i // 4) * 32 + 3
      self.paint_card(c, card, x, y)