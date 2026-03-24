# PY5 IMPORTED MODE CODE
class IceCream:
    def __init__(self, x, y, color, cone, scoops):
        self.x = x
        self.y = y
        self.color = color
        self.cone = cone
        self.scoops = scoops
        
    def drawIceCream(self):
        color_mode(HSB,360,100,100)
        fill(self.color,100,100)
        no_stroke()
        for i in range(1, self.scoops*30, 30):
            circle(self.x, self.y-i, 40)
        fill(28,72,41)
        if(self.cone):
            triangle(self.x-20,self.y+10,self.x+20,self.y+10, self.x, self.y+60)
        else:
            rect(self.x-20,self.y+10,40,30)
        
        