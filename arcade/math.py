def ab(a, b):
  return (a, b) if a <=b else (b, a)

def clamp(x, a=0, b=1):
  return max(a, min(b, x))