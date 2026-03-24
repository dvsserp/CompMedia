angle = 0

def setup():
    size(800, 800)
    
def draw():
    global angle
    background(0)
    no_fill()
    stroke_weight(2)
    
    for i in range(20):
        push_matrix()
        translate(random(width), random(height))
        rotate(angle + random(TWO_PI))
        scale(random(0.5, 2.0))
        
        # Random color
        stroke(random(255), random(255), random(255))
        
        # Random shape
        shape_type = int(random(4))
        if shape_type == 0:
            ellipse(0, 0, 50, 50)
        elif shape_type == 1:
            rect(-25, -25, 50, 50)
        elif shape_type == 2:
            triangle(-25, 25, 0, -25, 25, 25)
        elif shape_type == 3:
            line(-25, -25, 25, 25)
            line(25, -25, -25, 25)
        
        pop_matrix()
    
    angle += 0.05
    