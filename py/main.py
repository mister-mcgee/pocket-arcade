import board

from busio     import SPI
from digitalio import DigitalInOut
from lib.adafruit_rgb_display import st7735, color565

# from arcade import Arcade

spi = SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
display = st7735.ST7735R(spi, 
  width    = 128, 
  height   = 128, 
  rotation =   0,
  x_offset =   2,
  y_offset =   3,
  dc  = DigitalInOut(board.D12),
  cs  = DigitalInOut(board.D10),
  rst = DigitalInOut(board.D11)
)

display.init()

# print(Arcade.VERSION)

cells = [0] * 16

def set_cell(i, j):
  if i < 0 or i >= 16 or j < 0 or j >= 16:
    return
  cells[j] |= (1 << i)

def get_cell(i, j):
  if i < 0 or i >= 16 or j < 0 or j >= 16:
    return 0
  return 1 if (cells[j] & (1 << i)) else 0

def count_neighbors(i, j):
  return (
    get_cell(i - 1, j - 1) +
    get_cell(i    , j - 1) +
    get_cell(i + 1, j - 1) +
    get_cell(i - 1, j    ) +   
    get_cell(i + 1, j    ) +
    get_cell(i - 1, j + 1) +
    get_cell(i    , j + 1) +
    get_cell(i + 1, j + 1)
  )

def setup_cells():
  set_cell(8, 7)
  set_cell(9, 7)
  set_cell(7, 8)
  set_cell(8, 8)
  set_cell(8, 9)  

def update_cells():
  global cells
  _cells = cells.copy()
  for row in range(16):
    for col in range(16): 
      n = count_neighbors(col, row)
      if n < 2 or n > 3:
        _cells[row] &= ~(1 << col)
      elif n == 3:
        _cells[row] |=  (1 << col)
  cells = _cells

def render_cells():
  for row in range(16):
    for col in range(16):
      if get_cell(col, row):
        display.fill_rectangle(col * 8, row * 8, 8, 8, color565(255, 255, 255))
      else:
        display.fill_rectangle(col * 8, row * 8, 8, 8, color565(  0,   0,   0))

setup_cells()
while True:
  render_cells()
  update_cells()


  
