from tamagotchiClass import *

def setup():
    size(500,500)
    global tamagotchi1
    tamagotchi1 = Tamagotchi("bob")
    
def draw():
    background(255)
    tamagotchi1.display()
    tamagotchi1.move()
    tamagotchi1.bounce()
    tamagotchi1.displayUI()