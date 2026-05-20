# PY5 IMPORTED MODE CODE

#checker class
class Checker:
    def __init__(self,position,col):
        self.position = position
        self.king = False;
        self.color = col;
    
    def display(self):
        if(self.color == "black"):
            fill(0)
        else:
            fill(255,0,0)
        circle(self.position[0]*width//8,self.position[1]*height//8,30)
        
    def move(self, newPositionX, newPositionY):
        if(self.king):
            if((self.position[0] + 1 == newPositionX or self.position[0] - 1 == newPositionX) and (self.position[1] + 1 == newPositionY or self.position[1] - 1 == newPositionY)):
                print("moved")
                self.position = [newPositionX, newPositionY]
        else:
            #normal move for black
            if (self.position[0] + 1 == newPositionX and (self.position[1] + 1 == newPositionY or self.position[1] - 1 == newPositionY) and self.color == "black"):
                print("moved")
                self.position = [newPositionX, newPositionY]
            #normal move for red
            elif (self.position[0] - 1 == newPositionX and (self.position[1] + 1 == newPositionY or self.position[1] - 1 == newPositionY) and self.color == "red"):
                print("moved")
                self.position = [newPositionX, newPositionY]
            else:
                print("cannot move here")