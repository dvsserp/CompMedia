logo = {}
def setup():
    global logo
    size(800,400)
    logo = {"x" : width/2, "y" : height/2, "xSpeed" : 2, "ySpeed" : 2, "up" : True, "right": True}
def draw():
    global logo
    background(255)
    pic(logo["x"], logo["y"])
    if logo["up"]:
       logo["y"] -= logo["ySpeed"]
    else:
        logo["y"] += logo["ySpeed"]
        
    if logo["right"]:
        logo["x"] += logo["xSpeed"]
    else:
        logo["x"] -= logo["xSpeed"]
        
    if(logo["x"] > width):     
        logo["right"] = False
    if(logo["y"] > height):
        logo["up"] = True
    if(logo["x"] < 0):
        logo["right"] = True
    if(logo["y"] < 0):
        logo["up"] = False
def pic(x, y):
    rect(x-50,y-25, 100,50)
    circle(x,y,50)