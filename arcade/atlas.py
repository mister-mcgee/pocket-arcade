class Atlas:
  def __init__(self, 
    image, 
    cols=1,
    rows=1
  ):
    self.image = image
    self.cols  = cols
    self.rows  = rows
    self.col_w = self.image.w // cols
    self.row_h = self.image.h // rows