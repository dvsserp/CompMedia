color1 = {}
c = None
def setup():
    size(900,800)
    global color1
    color1 = {
        "red" : 0,
        "orange" : 30,
        "yellow" : 60,
        "green" : 120,
        "cyan" : 180,
        "blue" : 210,
        "purple" : 270,
        "pink" : 300
        }
def draw():
    global c
    color_mode(HSB, 360, 100, 100)
    n = 50
    for i in color1:
        stroke(0,0,0)
        fill(color1[i], 100, 100)
        square(n, 700, 50)
        n += 100
    
    if is_mouse_pressed and mouse_y < 700:
        stroke(c)
        line(mouse_x,mouse_y,pmouse_x,pmouse_y)
            
def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False

def mouse_pressed():
    global c
    x = 50
    for name in color1:
        if(collidePointRect(mouse_x, mouse_y, x, 700,50,50)):
           c = color(color1[name],100,100)
        x += 100