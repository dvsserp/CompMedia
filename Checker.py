#checker class
class Checker:
    def __init__(self,position):
        self.position = position
        self.king = false;
    
    def move(self, newPosition):
        if(self.position + 1 == newPosition or self.position - 1 == newPosition):
            print("moved")