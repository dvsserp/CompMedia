from wigglerClass import *

def setup():
    size(510,350)
    global wiggler1, wiggler2	#global because we will use it in draw later!
    wiggler1 = Wiggler(35, 35)
    wiggler2 = Wiggler(35,35)

def draw():
    #background(220)
    no_stroke()
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    wiggler1.display()
    wiggler1.move()
    wiggler1.bounceOnEdge()
    wiggler1.animate()
    wiggler2.display()
    wiggler2.move()
    wiggler2.bounceOnEdge()
    wiggler2.animate()


