# PY5 IMPORTED MODE CODE
class Bubble:
    def __init__(self, color, size):
        self.x = int(random(0 + size, width - size))
        self.y = int(random(0 + size, width - size))
        self.size = size
        self.color = color
        self.xSpd = random(-3,3)
        self.ySpd = random(-3,3)
        
    def display(self):
        fill(self.color,50)
        no_stroke()
        circle(self.x, self.y, self.size)
        fill(self.color,100)
        circle(self.x + self.size/5, self.y + self.size/5, self.size/5)
    
    def move(self):
        self.x += self.xSpd
        self.y += self.ySpd
        
    def bounce(self):
        if(self.x < (0 + self.size/2) or self.x > (width - self.size/2)):
            self.xSpd *= int(random(-2,-1))
        if(self.y < (0 + self.size/2) or self.y > (height- self.size/2)):
            self.ySpd *= int(random(-2,-1))
