from Checker import *
#checkers
board = [[]]
def setup():
    global board
    size(400,400)
    background(255,0,0)
    initialSetup()
    print(board)
def draw():
    global board
    drawTiles()
    for x in range(0,8):
        for y in range(0,4):
            if (board[x][y] != 0):
                board[x][y].display()
        
def drawTiles():
    for x in range(0,width,width//8):
        for y in range(0,height,height//8):
            if(x % ((width//8) * 2) == 0 and y % ((height//8) * 2) == 0):
                fill(0)
                rect(x,y,width//8,height//8)
            elif (x % ((width//8) * 2) == width//8 and y % ((height//8) * 2) == height//8):
                fill(0)
                rect(x,y,width//8,height//8)
    
def initialSetup():
    global board
    board = [[0 for x in range(4)] for y in range(8)]
    for x in range(0,4):
        for y in range(0,3):
            board[x][y] = Checker([x,y], "black")
            
    for x in range(4,8):
        for y in range(0,3):
            board[x][y] = Checker([x,y], "red")
    #print(board);