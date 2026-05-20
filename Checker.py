# PY5 IMPORTED MODE CODE

#checker class
class Checker:
    def __init__(self,position,col):
        self.position = position
        self.king = True;
        self.color = col;
    
    def display(self):
        if(self.color == "black"):
            fill(0)
        else:
            fill(255,0,0)
        stroke(255);
        if(self.position[1] % 2 == 0):
            circle(self.position[0]*width//8 * 2 + width//16,self.position[1]*height//8 + height//16,30)
        else:
            circle(self.position[0]*width//8 * 2 + width//16 + width//8,self.position[1]*height//8 + height//16,30)
        if(self.king):
            fill("#FFFF00")
            begin_shape()
            vertex(self.position[0]*width//8 * 2 + width//16 - 5, self.position[1]*height//8 + height//16 + 3)
            vertex(self.position[0]*width//8 * 2 + width//16 + 5, self.position[1]*height//8 + height//16 + 3)
            vertex(self.position[0]*width//8 * 2 + width//16 + 5, self.position[1]*height//8 + height//16 - 3)
            vertex(self.position[0]*width//8 * 2 + width//16 + 2, self.position[1]*height//8 + height//16)
            vertex(self.position[0]*width//8 * 2 + width//16 - 2, self.position[1]*height//8 + height//16 - 3)
            vertex(self.position[0]*width//8 * 2 + width//16 - 5, self.position[1]*height//8 + height//16)
            vertex(self.position[0]*width//8 * 2 + width//16 - 5, self.position[1]*height//8 + height//16 - 3)
            vertex(self.position[0]*width//8 * 2 + width//16 - 5, self.position[1]*height//8 + height//16 + 3)
            end_shape(CLOSE)
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