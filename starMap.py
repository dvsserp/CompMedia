starMap = []
def setup():
    global starMap
    size(400,400)
    for i in range(200):
        starMap.append({"x" : int(random(1,width)), "y" : int(random(1,height)), "c" : int(random(360))})
def draw():
    global starMap
    color_mode(HSB,360,100,100)
    background(0)
    for star in starMap:
        fill(star["c"], 100, 100)
        circle(star["x"], star["y"], 2)