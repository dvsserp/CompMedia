color1 = {}
def setup():
    size(800,800)
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
    color_mode(HSB, 360, 100, 100)
    n = 50
    for i in color1:
        fill(color1[i], 100, 100)
        square(n, 700, 50)
        n += 90
        if collidePointRect(mouse_x, mouse_y, n, 700, 50, 50) and is_mouse_pressed:
            fill(color1[i], 100, 100)
    if is_mouse_pressed:
        line(mouse_x, mouse_y, pmouse_x, pmouse_y)
            
def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False