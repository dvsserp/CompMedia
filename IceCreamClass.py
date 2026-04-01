# PY5 IMPORTED MODE CODE
class IceCream:
    def __init__(self, color, cone, scoops,topping):
        self.x = 0
        self.y = 0
        self.color = color
        self.cone = cone
        self.scoops = scoops
        self.toppings = topping
        
    def drawIceCream(self):
        color_mode(HSB,360,100,100)
        fill(self.color,100,100)
        no_stroke()
        for i in range(1, self.scoops*50, 50):
            circle(self.x, self.y-i, 80)
        fill(28,72,41)
        if(self.cone):
            triangle(self.x-40,self.y+20,self.x+40,self.y+20, self.x, self.y+120)
        else:
            rect(self.x-40,self.y+20,80,60)
            
    def drawToppings(self):
        fill(0)
        #add spinkles
        #add chocolate syrup
        #add gummies
        #add cherry