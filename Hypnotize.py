angle = 0

def setup():
    size(400,400)
    
def draw():
    global angle
    background(220)
    translate(100,100)
    rotate(angle)
    triangle(20,20,100,20,10,30)
    ellipse(20,100,20,10)
    rect(150,20,90,50)
    angle+=0.1
    