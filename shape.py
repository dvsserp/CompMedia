def setup():
    size(400,400)
    
def draw():
    triangle(250,200,300,25, 30, 120)
    quad(200,150,250,300,200,150,200,100)
    begin_shape()
    vertex(120,100)
    vertex(200,120)
    vertex(150,200)
    vertex(140,210)
    vertex(160,160)
    vertex(200,100)
    end_shape(CLOSE)
    rect(200,100,20,30)
    rect(100,150,50,70)
    circle(200,300,200)
    arc(200,100, 100, 50,degrees(90), degrees(360), PIE)