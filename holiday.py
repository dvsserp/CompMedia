from IceCreamClass import *
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
    size(400,400)
    color_mode(HSB,360,100,100)
def draw():
    global colors
    background(255)
    translate(width/2,height/2)
    ice1 = IceCream(0,0, colors["red"], True, 2)
    ice1.drawIceCream()