from arcade.scene import Scene
from arcade.image import Image
from arcade.color import RED

import ulab.numpy as np

class Chess(Scene):
  def __init__(self):
    self.WHITE = 0b00000
    self.BLACK = 0b10000

    self.NONE   = 0
    self.PAWN   = 1
    self.KNIGHT = 2
    self.BISHOP = 3
    self.ROOK   = 4
    self.QUEEN  = 5
    self.KING   = 6

    self.ON_WHITE = 0b00000
    self.ON_BLACK = 0b01000
    self.chess_sprite = Image.load("/arcade/apps/chess/chess.bmp")   

    self.board = np.zeros((8, 8), dtype=np.uint8)

  def on_attach(self, stage):
    self.put((0, 0), self.BLACK | self.ROOK)
    self.put((1, 0), self.BLACK | self.KNIGHT)
    self.put((2, 0), self.BLACK | self.BISHOP)
    self.put((3, 0), self.BLACK | self.QUEEN)
    self.put((4, 0), self.BLACK | self.KING)
    self.put((5, 0), self.BLACK | self.BISHOP)
    self.put((6, 0), self.BLACK | self.KNIGHT)
    self.put((7, 0), self.BLACK | self.ROOK)

    self.put((0, 1), self.BLACK | self.PAWN)
    self.put((1, 1), self.BLACK | self.PAWN)
    self.put((2, 1), self.BLACK | self.PAWN)
    self.put((3, 1), self.BLACK | self.PAWN)
    self.put((4, 1), self.BLACK | self.PAWN)
    self.put((5, 1), self.BLACK | self.PAWN)
    self.put((6, 1), self.BLACK | self.PAWN)
    self.put((7, 1), self.BLACK | self.PAWN)

    self.put((0, 6), self.WHITE | self.PAWN)
    self.put((1, 6), self.WHITE | self.PAWN)
    self.put((2, 6), self.WHITE | self.PAWN)
    self.put((3, 6), self.WHITE | self.PAWN)
    self.put((4, 6), self.WHITE | self.PAWN)
    self.put((5, 6), self.WHITE | self.PAWN)
    self.put((6, 6), self.WHITE | self.PAWN)
    self.put((7, 6), self.WHITE | self.PAWN)

    self.put((0, 7), self.WHITE | self.ROOK)
    self.put((1, 7), self.WHITE | self.KNIGHT)
    self.put((2, 7), self.WHITE | self.BISHOP)
    self.put((3, 7), self.WHITE | self.QUEEN)
    self.put((4, 7), self.WHITE | self.KING)
    self.put((5, 7), self.WHITE | self.BISHOP)
    self.put((6, 7), self.WHITE | self.KNIGHT)
    self.put((7, 7), self.WHITE | self.ROOK)

    self.draw_board(stage.screen)

  def in_bounds(self, where):
    return (
      where[0] >= 0 and where[0] < 8 and
      where[1] >= 0 and where[1] < 8
    )
  
  def put(self, where, what):
    if self.in_bounds(where):
      self.board[where] = what

  def draw_piece(self, c, piece, where):
    if (where[0] + where[1]) & 1:
      piece = piece | self.ON_WHITE
    else:
      piece = piece | self.ON_BLACK

    c.image(self.chess_sprite,
      where[0]  * 16, 
      where[1]  * 16,
      (piece  % 8) * 16, 
      (piece // 8) * 16,
      16, 16
    )

  def draw_board(self, c):
    for i in range(8):
      for j in range(8):
        self.draw_piece(c, self.board[i, j], (i, j))

  def on_update(self, c):
    pass

  def on_render(self, c):
    pass