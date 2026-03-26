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

def setup():
    size(1000,1000)
    color_mode(HSB,360,100,100)
def draw():
    global colors
    translate(width/2,height/2)
    ice1 = IceCream(colors["red"], True, 2)
    ice1.drawIceCream()
    drawHAPPY()
    drawDAY()
    
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
    leftSideDay = width/2
    dayHeight = height - height/6
    if(movey < 50):
        #A
        circle(leftSideDay+ movex/2 + 100, dayHeight - movey + 50,10)
        circle(leftSideDay + movex/2 + 125, dayHeight + movey,10)
        circle(leftSideDay + movex/2 + 110, dayHeight + 25, 10)
    
        #Y
        circle(leftSideDay + 280 + movex/2, dayHeight + movey/2, 10)
        circle(leftSideDay + 330 - movex/2, dayHeight + movey/2, 10)
        circle(leftSideDay + 305, dayHeight + 30 + movey/2,10)
    
    