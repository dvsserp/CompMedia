def setup():
    size(400,400)
    
def draw():
    background(255)
    translate(width/2,height/2)
    fill(0)
    w = 30
    h = 50
    s = 0
    scale(sin(s) * 100)
    for i in range(0,12):
        rotate(radians(30*i))
        ellipse(20 + cos(radians(20*i)),20 + sin(radians(20*i)),w,h)
    s += 0.05