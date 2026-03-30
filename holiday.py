from IceCreamClass import *
movex = 0;
movey = 0;
colors = {
    "red":0,
    "orange":30,
    "yellow":60,
    "green":120,
    "cyan":180,
    "blue":210,
    "purple":270,
    "pink":300}
toppings = ["None","Sprinkles", "Gummies", "Cherry", "Chocolate"] 
def setup():
    size(1000,1000)
    color_mode(HSB,360,100,100)
def draw():
    global colors,toppings
    translate(width/2,height/2)
    ice1 = IceCream(colors["red"], False, 2, toppings[0])
    ice1.drawIceCream()
    drawDAY()
    drawHAPPY()
    Palette()
    
def drawHAPPY():
    global movex, movey
    leftSideHappy = -width/4
    happyHeight= -height/3
    if(movey < 50):
        #H
        circle(leftSideHappy, happyHeight + movey, 10)
        circle(leftSideHappy + 50, happyHeight + movey, 10)
        circle(leftSideHappy + movex, happyHeight + 25, 10)
        
        #A
        circle(leftSideHappy+ movex/2 + 100, happyHeight - movey + 50,10)
        circle(leftSideHappy + movex/2 + 125, happyHeight + movey,10)
        circle(leftSideHappy + movex/2 + 110, happyHeight + 25, 10)
        
        #P
        circle(leftSideHappy + 175, happyHeight + movey, 10)
        l = remap(movex, 1, 50, 1, 180)
        circle(leftSideHappy +190 + cos(l)*15, happyHeight + 15 + sin(l)*15,10)
        
        circle(leftSideHappy + 240, happyHeight + movey, 10)
        l = remap(movex, 1, 50, 1, 180)
        circle(leftSideHappy + 255 + cos(l)*15, happyHeight + 15 + sin(l)*15,10)
        
        #Y
        circle(leftSideHappy + 280 + movex/2, happyHeight + movey/2, 10)
        circle(leftSideHappy + 330 - movex/2, happyHeight + movey/2, 10)
        circle(leftSideHappy + 305, happyHeight + 30 + movey/2,10)
        
        
    movex += 1
    movey += 1

def drawDAY():
    global movex,movey
    leftSideDay = -width / 5
    dayHeight = height/8
    if(movey < 50):
        #D
        arc(leftSideDay + 150, dayHeight+25, 80,60,radians(270),radians(270+180),CHORD)
        
        #A
        circle(leftSideDay+ movex/2 + 200, dayHeight - movey + 50,10)
        circle(leftSideDay + movex/2 + 225, dayHeight + movey,10)
        circle(leftSideDay + movex/2 + 210, dayHeight + 25, 10)
    
        #Y
        circle(leftSideDay + 280 + movex/2, dayHeight + movey/2, 10)
        circle(leftSideDay + 330 - movex/2, dayHeight + movey/2, 10)
        circle(leftSideDay + 305, dayHeight + 30 + movey/2,10)
        
        
def Palette():
    global colors, toppings
    fill(255)
    text("Topping", 0, height/2 - 230)
    for i in range(0,len(toppings)*200,200):
        rect(-width/2 + i + 60, height/2 - 200, 70,50)
    for i in range(0, len(colors)*120,120):
        rect(-width/2 + i + 30, height/2 - 120, 70, 50)
        
def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False
    