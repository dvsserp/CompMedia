color1 = {}
c = 0
s = 1
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
    background(255,255,255)
def draw():
    global c
    global s
    color_mode(HSB, 360, 100, 100)
    #create paint palette
    n = 50
    for i in color1:
        stroke_weight(1)
        stroke(0,0,0)
        fill(color1[i], 100, 100)
        square(n, 700, 50)
        n += 100 
    #changing size of brush
    stroke_weight(s)
    #changing color of brush
    if is_mouse_pressed and mouse_y < 700:
        stroke(c)
        line(mouse_x,mouse_y,pmouse_x,pmouse_y)
            
    #changing size and adding eraser when key pressed
    if is_key_pressed:
        if key == 's':
            stroke_weight(1)
            fill(0,0,100)
            rect(290,40,80,20)
            fill(0,0,0)
            text("size: " + str(s), 300, 50)
            stroke_weight(s)
            s += 0.5
        if key == 'e':
            c = 360
        if key == 'b':
            stroke_weight(1)
            fill(0,0,100)
            rect(390,40,80,20)
            fill(0,0,0)
            text("color: black", 400, 50)
            stroke_weight(s)
            c = 0

#changing color when mouse is clicked depending on which square
def mouse_pressed():
    global c
    x = 50
    for name in color1:
        if(collidePointRect(mouse_x, mouse_y, x, 700,50,50)):
           c = color(color1[name],100,100)
           fill(0,0,100)
           rect(390,40,80,20)
           fill(0,0,0)
           text("color: " + str(name), 400, 50)
        x += 100
        
def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False
