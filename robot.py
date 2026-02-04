def setup():
    size(400,400)
def draw():
    background(220)
    grid()
    displayCoordinates()
    head()
    body()
    
def grid():
  stroke(255)                    # white = 255
  for x in range(width):
    if x % 20 == 0:
      for y in range(height):
        if y % 20 == 0:
          line(x, 0, x, height)
          line(0, y, width, y)
  stroke(0)                        # black = 0
def displayCoordinates():
  fill(0)
  text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
  
def head():
    fill(255)
    circle(200,30,30)
    line(200,60,200,45)
    circle(200,90,60)
    rect(150,80,100,70)
    circle(175,110,30)
    circle(225,110,30)
    circle(175,110,15)
    circle(225,110,15)
    
def body():
    rect(196, 150, 8, 15)
    rect(165, 165, 70, 70)
    rect(175, 175, 50, 20)
    circle(200,215,20)
    line(180,235, 180, 270)
    line(220,235, 220, 270)
    circle(180, 280, 20)
    circle(220, 280, 20)
    line(170,280,190,280)
    line(210,280,230,280)
    fill(225)
    no_stroke()
    rect(150, 280, 100, 20)
    fill(0)
    stroke(0)
    line(170,280,190,280)
    line(210,280,230,280)