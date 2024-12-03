
from arcade.input import Input
from arcade.scene import Scene
from arcade.image import Image
from arcade.atlas import Atlas
from arcade.color import BLACK, GREEN, RED, WHITE, YELLOW
from arcade.fonts import WHITE_ON_BLACK

import random

class Memory(Scene):
  def __init__(self):
    self.card_sprite = Atlas(Image.load("/arcade/apps/games/memory/card.bmp"), 9, 1)

    self.FACE_DOWN = 0b00000
    self.FACE_UP   = 0b10000

    self.CARD_W = 15
    self.CARD_H = 24

  def reset(self):
    self.cards = [
      1 | self.FACE_DOWN, 1 | self.FACE_DOWN,
      2 | self.FACE_DOWN, 2 | self.FACE_DOWN, 
      3 | self.FACE_DOWN, 3 | self.FACE_DOWN,
      4 | self.FACE_DOWN, 4 | self.FACE_DOWN,
      5 | self.FACE_DOWN, 5 | self.FACE_DOWN,
      6 | self.FACE_DOWN, 6 | self.FACE_DOWN,
      7 | self.FACE_DOWN, 7 | self.FACE_DOWN,
      8 | self.FACE_DOWN, 8 | self.FACE_DOWN
    ]
    self.shuffle(self.cards)
    self.shuffle(self.cards)
    self.shuffle(self.cards)

    self.hover    =  0
    self.select_a = -1
    self.select_b = -1
    self.guesses  =  0
    self.matches  =  0
    self.complete = False

  def shuffle(self, cards, n=1):
    for k in range(n):
      for i in range(len(cards)):
        j   =   random.randrange(0, len(cards))
        cards[i], cards[j] = cards[j], cards[i]
  
  def on_attach(self, c):
    self.reset( )
    self.paint(c)

  def paint_card(self, c, card, x=0, y=0):
    if card & self.FACE_UP:
      c.sprite(self.card_sprite, card & 0xf, x, y)
    else:
      c.sprite(self.card_sprite,          0, x, y)

  def increment_selector(self, i):
    i = (i + 1) % len(self.cards)
    while self.cards[i] & self.FACE_UP:
      i = (i + 1) % len(self.cards)
    return i
  
  def decrement_selector(self, i):
    i = (i + len(self.cards) - 1) % len(self.cards)
    while self.cards[i] & self.FACE_UP:
      i = (i + len(self.cards) - 1) % len(self.cards)
    return i

  def paint(self, c):
    c.fill(0)
    for i, card in enumerate(self.cards):
      x = (i  % 4) * 32 + 9
      y = (i // 4) * 32 + 4

      if self.select_b != -1:
        if i == self.select_a or i == self.select_b:
          if self.cards[self.select_a] == self.cards[self.select_b]:
            c.rect(x - 1, y - 1, self.CARD_W + 2, self.CARD_H + 2, GREEN)
          else:
            c.rect(x - 1, y - 1, self.CARD_W + 2, self.CARD_H + 2, RED  )
      else:
        if i == self.hover or i == self.select_a or i == self.select_b:
          c.rect(x - 1, y - 1, self.CARD_W + 2, self.CARD_H + 2, YELLOW)

      self.paint_card(c, card, x, y)

  def on_complete(self, c):
    s1 = "Game Over"
    s2 = f"Matches {self.matches}"
    s3 = f"Guesses {self.guesses}"
    w = max(len(s1), len(s2), len(s3))

    c.rect(62 - w * 3, 50, w * 6 + 4, 28, WHITE)
    c.rect(63 - w * 3, 51, w * 6 + 2, 26, BLACK)
    c.text(WHITE_ON_BLACK, s1, 64 - len(s1) * 3, 52)
    c.text(WHITE_ON_BLACK, s2, 64 - len(s2) * 3, 60)
    c.text(WHITE_ON_BLACK, s3, 64 - len(s3) * 3, 68)    

  def on_button_down(self, c, button):
    if self.complete:
      self.reset( )
      self.paint(c)
      return
    
    if self.select_b != -1:
      if self.cards[self.select_a] == self.cards[self.select_b]:
        self.guesses += 1
        self.matches += 1
        if self.matches == 8:
          self.complete = True
          self.on_complete(c)
          return
      else:
        self.hover = self.select_b
        self.cards[self.select_a] ^= self.FACE_UP
        self.cards[self.select_b] ^= self.FACE_UP
        self.guesses += 1
      self.select_a = -1
      self.select_b = -1
      self.paint(c)
      return
    
    if   button == Input.BUTTON_L:
      self.hover = self.decrement_selector(self.hover)
      self.paint(c)
    elif button == Input.BUTTON_R:
      self.hover = self.increment_selector(self.hover)
      self.paint(c)
    elif button == Input.BUTTON_A:
      if   self.select_a == -1:
        self.select_a = self.hover
        self.cards[self.select_a] ^= self.FACE_UP
        self.hover = self.increment_selector(self.hover)
      elif self.select_b == -1:
        self.select_b = self.hover
        self.cards[self.select_b] ^= self.FACE_UP
        self.hover = self.increment_selector(self.hover)
      self.paint(c)

