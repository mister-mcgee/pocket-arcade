import random

from arcade.fonts import WHITE_ON_BLACK
from arcade.scene import Scene
from arcade.image import Image
from arcade.atlas import Atlas

class Blackjack(Scene):
  def Card(self, face, suit=0):
    return face | (suit << 4)

  def Deck(self              ):
    deck = [ ]
    for suit in range(4):
      for face in range(13):
        deck.append(self.Card(face + 1, suit))
    return deck
  
  def __init__(self):
    self.card_sprite = Atlas(Image.load("/arcade/apps/games/blackjack/card.bmp"),  2, 1)
    self.face_sprite = Atlas(Image.load("/arcade/apps/games/blackjack/face.bmp"), 13, 2)
    self.suit_sprite = Atlas(Image.load("/arcade/apps/games/blackjack/suit.bmp"),  4, 1)

    self.MAXIMUM_BANK = 999_999
    self.MINIMUM_BET  =     100
    self.MAXIMUM_BET  =     999

    self.VALUES = [0, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  def on_attach(self, c):
    self.load_bank()

  def on_detach(self, c):
    self.save_bank()

  def load_bank(self):
    try:
      with open("/arcade/apps/games/blackjack/blackjack.dat", "r+") as f:
        self.bank = int(f.readline())
    except:
      self.bank = 500

  def save_bank(self):
    try:
      with open("/arcade/apps/games/blackjack/blackjack.dat", "w+") as f:
        f.write(str(self.bank))
    except:
      pass
  
  def suit_of(self, card):
    return (card & 0x30) >> 4
  
  def face_of(self, card):
    return (card & 0x0f)
  
  def value_of_card(self, card):
    return self.VALUES[self.face_of(card)] if card & 0x40 else 0
  
  def value_of_hand(self, hand):
    values = sorted(self.value_of_card(card) for card in hand)

    sum = 0
    for i, n in enumerate(values):
      if n == 11:
        if sum + len(hand) - i - 1 < 11:
          sum += 11
        else:
          sum +=  1
      else:
          sum += n
    return sum
  
  def shuffle(self, deck):
    for i in range(len(deck)):
      j = random.randrange(0 , len(deck))
      deck[i], deck[j] = deck[j], deck[i]

  def setup(self):
    self.deck = self.Deck()

    self.player = [ ]
    self.dealer = [ ]

    self.is_split = False
    self.split0 = [ ]
    self.split1 = [ ]

    self.bank = 0
    self.bet  = 0
    self.pot  = 0

    # triple shuffle
    self.shuffle(self.deck)
    self.shuffle(self.deck)
    self.shuffle(self.deck)

    self.deal(self.deck, self.dealer      )
    self.deal(self.deck, self.dealer, 0x40)
    self.deal(self.deck, self.player, 0x40)
    self.deal(self.deck, self.player, 0x40)

    print(self.value_of_hand(self.dealer))
    print(self.value_of_hand(self.player))
    print(self.value_of_hand([0x43, 0x43, 0x43, 0x42, 0x42, 0x42, 0x42, 0x41, 0x41, 0x41, 0x41]))
  
  def on_attach(self, c):
    c.fill(0)
    self.setup()
    self.paint_hand(c, self.player, 1, 105)
    self.paint_hand(c, self.dealer, 1, 1  )

  def deal(self, deck, hand, facing=0):
    card = deck.pop()
    card |= 0x40
    card ^= 0x40
    hand.append(card | facing)

  def paint_card(self, c, card, x, y):
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

  def paint_hand(self, c, hand, x, y, w=17):
    for i, card in enumerate(hand):
      self.paint_card(c, card, i * w + x, y)

  def paint_button(self, c, text, x, y):
    pass

  def h(self):
    pass

  def s(self):
    pass

  def can_dd(self, hand):
    return self.bet <= self.bank and len(hand) == 2
  
  def can_sp(self, hand):
    a = self.face_of(hand[0])
    b = self.face_of(hand[1])
    return self.bet <= self.bank and len(hand) == 2 and (a == b or (a >= 10 and b >= 10))

  def dd(self, hand):
    pass

  def sp(self, hand):
    self.is_split = True
    pass

