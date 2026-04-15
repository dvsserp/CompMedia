from math import *
timer = 9
def setup():
    size(400,400)
    
def draw():
    global timer
    background(220)
    translate(width/2,height/2)
    smileFace()
    if frame_count % 60 == 0 and timer > 0:
        timer -= 1
    if timer <= 6 and timer > 3:
        shockFace()
    if timer <= 3:
        sadFace()
    if timer == 0:
        timer = 9
        
def smileFace():
    fill(255,255,0)
    circle(0,0,200)
    fill(0)
    circle(-50,-50,50)
    circle(50,-50,50)
    no_fill()
    arc(0,0,100,100,radians(0),radians(180), OPEN)
    
def sadFace():
    fill(255,255,0)
    circle(0,0,200)
    fill(0)
    circle(-50,-50,50)
    circle(50,-50,50)
    no_fill()
    arc(0,50,100,100,radians(180),radians(360), OPEN)
    
def shockFace():
    fill(255,255,0)
    circle(0,0,200)
    fill(0)
    circle(-50,-50,50)
    circle(50,-50,50)
    fill(255,0,0)
    circle(0,50,50)
    no_fill()