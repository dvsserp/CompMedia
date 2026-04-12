# PY5 IMPORTED MODE CODE
class IceCream:
    def __init__(self, color, cone, scoops, topping):
        self.x = 0
        self.y = 0
        self.color = color
        self.cone = cone
        self.scoops = scoops
        self.toppings = topping

    def drawIceCream(self):
        color_mode(HSB, 360, 100, 100)
        fill(self.color, 100, 100)
        no_stroke()
        for i in range(1, self.scoops * 50, 50):
            circle(self.x, self.y - i, 80)
        fill(28, 72, 41)
        if self.cone:
            triangle(self.x - 40, self.y + 20, self.x + 40, self.y + 20, self.x, self.y + 120)
        else:
            rect(self.x - 40, self.y + 20, 80, 60)

    def drawToppings(self):
        no_stroke()
        if self.toppings == "Sprinkles":
            fill(0)
            for scoop in range(self.scoops):
                scoop_y = self.y - scoop * 50 - 40
                for x_offset in (-25, -15, -5, 5, 15, 25):
                    circle(self.x + x_offset, scoop_y + 10, 8)
        elif self.toppings == "Gummies":
            gummies = [(0, 100, 100), (30, 100, 100), (120, 100, 100), (180, 100, 100)]
            for scoop in range(self.scoops):
                scoop_y = self.y - scoop * 50 - 40
                for x_offset, color_choice in zip((-25, 0, 25), gummies):
                    fill(*color_choice)
                    circle(self.x + x_offset, scoop_y + 10, 16)
        elif self.toppings == "Cherry":
            fill(345, 100, 100)
            circle(self.x, self.y - self.scoops * 50 - 35, 18)
            fill(120, 100, 80)
            rect(self.x + 5, self.y - self.scoops * 50 - 25, 4, 22)
        elif self.toppings == "Chocolate":
            no_fill()
            stroke(30, 100, 40)
            stroke_weight(8)
            arc(self.x, self.y - self.scoops * 50 - 15, 120, 60, PI, TWO_PI)
            stroke_weight(4)
            for x_offset in (-25, 0, 25):
                line(self.x + x_offset, self.y - self.scoops * 50 - 15, self.x + x_offset, self.y - self.scoops * 50 + 10)
            no_stroke()
