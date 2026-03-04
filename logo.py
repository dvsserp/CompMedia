logo = {}
def setup():
    global logo
    size(400,400)
    logo = {"x" : width/2, "y" : height/2, "xSpeed" : 2, "ySpeed" : 2}
def draw():
    background(255)
    pic(logo["x"], logo["y"])
    
def pic(x, y):
    