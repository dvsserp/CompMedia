from bubbleClass import *

bubbles = []

def setup():
    size(1000,1000)
    for i in range(100):
        bubbles.append(Bubble(color(random(255),random(255), random(255)),int(random(30,80))))
    
def draw():
    background(255)
    for bubble in bubbles:
        bubble.display()
        bubble.move()
        bubble.bounce()
        
def collideCircleCircle(circ1x, circ1y, circ1d, circ2x, circ2y, circ2d):
  """Input x,y coordinates and diameter for both circles.
  Returns true if the two circles are touching.
  
  Does not work for ellipse/oval shapes."""
  
  distance = dist(circ1x, circ1y, circ2x, circ2y)
  circ1rad = circ1d/2
  circ2rad = circ2d/2
  
  if distance <= circ1rad + circ2rad:
    return True
  else:
    return False