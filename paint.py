color1 = {}
mode1 = "draw"
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
    color_mode(HSB,360,100,100)
    stroke_weight(1)
    fill(0,0,100)
    rect(390,40,80,20)
    rect(190,40,80,20)
    fill(0,0,0)
    text("color: black", 400, 50)
    text("mode: draw", 200, 50)
    stroke_weight(s)
def draw():
    global c
    global s
    global mode1
    color_mode(HSB, 360, 100, 100)
    
    #display the size
    stroke_weight(1)
    fill(0,0,100)
    stroke(0)
    rect(290,40,80,20)
    stroke(c)
    fill(0,0,0)
    text("size: " + str(s), 300, 50)
    stroke_weight(s)
    
    if mode1 == "erase":
        stroke_weight(1)
        fill(0,0,100)
        stroke(0)
        rect(390,40,80,20)
        rect(190,40,80,20)
        stroke(c)
        fill(0,0,0)
        text("mode: eraser", 200, 50)
        text("color: white", 400, 50)
        stroke_weight(s)
        
    if mode1 == "draw":
        stroke_weight(1)
        fill(0,0,100)
        stroke(0)
        rect(390,40,80,20)
        rect(190,40,80,20)
        stroke(c)
        fill(0,0,0)
        text("color: black", 400, 50)
        text("mode: draw", 200, 50) 
        stroke_weight(s)
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
            #display size
            stroke_weight(1)
            fill(0,0,100)
            rect(290,40,80,20)
            fill(0,0,0)
            text("size: " + str(s), 300, 50)
            stroke_weight(s)
        if key == 'w':
            s += 0.5
        if key == 'q' and s > 0.5:
            s -= 0.5
        if key == 'e':
            mode1 = "erase"
            c = 360
        if key == 'b':
            #displays black when reset
            stroke_weight(1)
            fill(0,0,100)
            rect(390,40,80,20)
            fill(0,0,0)
            text("color: black", 400, 50)
            stroke_weight(s)
        if key == 'r':
            mode1 = "draw"
            c = 0
        if key == 'c':
            background(0,0,100)
#changing color when mouse is clicked depending on which square
def mouse_pressed():
    global c
    global s
    x = 50
    for name in color1:
        if(collidePointRect(mouse_x, mouse_y, x, 700,50,50)):
            #display which color
           c = color(color1[name],100,100)
           stroke_weight(1)
           fill(0,0,100)
           rect(390,40,80,20)
           fill(0,0,0)
           text("color: " + str(name), 400, 50)
           stroke_weight(s)
        x += 100
        
def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False
