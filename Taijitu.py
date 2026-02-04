def setup():
    size(400,400)
    
def draw():
    fill(255)
    circle(200,200,400)
    fill(0)
    arc(200,200,400,400,radians(90),radians(270), OPEN)
    arc(200,100, 200, 200, radians(270), radians(90 + 360), OPEN)
    circle(200,300,50)
    
    fill(255)
    arc(200,300, 200, 200, radians(90), radians(270), OPEN)
    fill(0)
    circle(200,300,50)
    fill(255)
    circle(200,100,50)