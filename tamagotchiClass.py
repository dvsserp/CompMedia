# PY5 IMPORTED MODE CODE
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 0
        self.age = 0
        self.size = 100
        self.x = random(width)
        self.y = random(height)
        self.color = color(random(255), random(255), random(255))
        self.xSpeed = random(-2,2)
        self.ySpeed = random(-2,2)
    
    def display(self):
        circle(self.x, self.y, self.size)
        
    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed
        
    def bounce(self):
        if(self.x < (0 + self.size/2) or self.x > (width - self.size/2)):
            self.health -= 2
            self.xSpeed *= -1
        if(self.y < (0 + self.size/2) or self.y > (height- self.size/2)):
            self.health -= 2
            self.ySpeed *= -1
        
    def feed(self):
        self.hunger -= 3
        if(self.hunger < 0):
            self.hunger = 0
        self.size += 1
        
    def heal(self):
        self.health += 3
        if(self.health > 100):
            self.health = 100