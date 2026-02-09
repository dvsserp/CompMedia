def setup():
    size(300,300)
    fill(225)
    
def draw():
    background(225)
    fill(190,0,0)
    circle(150,50,100)
    fill(190,190,0)
    circle(150,150,100)
    fill(0,190,0)
    circle(150,250,100)
    if(collidePointCircle(mouse_x, mouse_y, 150, 50, 100)):
       fill(255,0,0)
       circle(150,50,100)
    if(collidePointCircle(mouse_x, mouse_y, 150,150,100)):
        fill(255,255,0)
        circle(150,150,100)
    if(collidePointCircle(mouse_x, mouse_y, 150,250,100)):
        fill(0,255,0)
        circle(150,250,100)


def collidePointCircle(pointX, pointY, circX, circY, diameter):
  """Input coordinates for the point and x, y, and diameter (the width/height) of the circle.
  Returns true if the point and circle are touching.
  
  Does not work for ellipse/oval shapes."""
  
  distance = dist(pointX, pointY, circX, circY)
  radius = diameter/2
  
  if(distance <= radius):
    return True
  else:
    return False