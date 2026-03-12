class Brush:
    def __init__(self):
        self.color = color(0)
        self.draw = "true"
        self.size = 2
        self.x = mouse_x
        self.y = mouse_y
        
    def draw(self):