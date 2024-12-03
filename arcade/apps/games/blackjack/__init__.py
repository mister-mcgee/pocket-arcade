import random

from arcade.scene import Scene
from arcade.image import Image
from arcade.atlas import Atlas

class Blackjack(Scene):
  def __init__(self):
    self.card_sprite = Atlas(Image.load("/arcade/apps/blackjack/card.bmp"),  2, 1)
    self.face_sprite = Atlas(Image.load("/arcade/apps/blackjack/face.bmp"), 13, 2)
    self.suit_sprite = Atlas(Image.load("/arcade/apps/blackjack/suit.bmp"),  4, 1)

    self.CLUBS    = 0x00
    self.HEARTS   = 0x01
    self.SPADES   = 0x02
    self.DIAMONDS = 0x03

  def Card(self, face, suit=0):
    return face | (suit << 4)

  def Deck(self              ):
    deck = [ ]
    for suit in range(4):
      for face in range(13):
        deck.append(self.Card(face + 1, suit))
    return deck
  
  def suit_of(self, card):
    return (card & 0x30) >> 4
  
  def face_of(self, card):
    return (card & 0x0f)
  
  def value_of(self, hand, ):
    hand = sorted([self.face_of(card) for card in hand], reverse=True)

    value = 0
    for i, card in enumerate(hand):
      if card == 1:
        if value + len(hand) - i - 1 < 11:
          value += 11
        else:
          value +=  1
      else:
        value += card
    return value
  
  def shuffle(self, deck):
    for i in range(len(deck)):
      j = random.randrange(0 , len(deck))
      deck[i], deck[j] = deck[j], deck[i]

  def setup(self):
    self.deck = self.Deck()
    self.player = [ ]
    self.dealer = [ ]

    self.shuffle(self.deck)
    self.deal(self.deck, self.dealer      )
    self.deal(self.deck, self.dealer, 0x40)
    self.deal(self.deck, self.player, 0x40)
    self.deal(self.deck, self.player, 0x40)
  
  def on_attach(self, c):
    c.fill(0)
    self.setup()
    self.draw_hand(c, self.player, 1, 105)
    self.draw_hand(c, self.dealer, 1, 1  )

  def deal(self, deck, hand, facing=0):
    card = deck.pop()
    card |= 0x40
    card ^= 0x40
    hand.append(card | facing)

  def draw_card(self, c, card, x, y):
    if card & 0x40:
      c.sprite(self.card_sprite, 1, x, y)
      suit = self.suit_of(card)
      face = self.face_of(card)
      if suit & 1: # red
        c.sprite(self.face_sprite, face - 1 , x + 1, y + 1)
      else:
        c.sprite(self.face_sprite, face + 12, x + 1, y + 1)
      c.sprite(self.suit_sprite, suit, x + 5, y + 9)
    else:
      c.sprite(self.card_sprite, 0, x, y)

  def draw_hand(self, c, hand, x, y, w=17):
    for i, card in enumerate(hand):
      self.draw_card(c, card, i * w + x, y)

  def hit(self, c):
    self.deal(self.deck, self.player)
    self.draw_hand(c, self.player, 1, 105)

  def stand(self, c):
    pass

  def double(self, c):
    pass
