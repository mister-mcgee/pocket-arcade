class Atlas:
  def __init__(self, 
    image, 
    cols=19,
    rows= 5
  ):
    self.image = image
    self.cols  = cols
    self.rows  = rows
    self.col_w = self.image.w // cols
    self.row_h = self.image.h // rows