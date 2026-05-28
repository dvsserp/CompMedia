from Checker import *
#checkers
board = [[]]
selected = None
turn = "Black"
def setup():
    global board
    size(400,400)
    background(255,0,0)
    initialSetup()
    #print(board)
def draw():
    global board, selected
    drawTiles()
    for x in range(0,4):
        for y in range(0,8):
            if (board[x][y] != 0):
                board[x][y].display()
    if selected != None:
        fill(255,255,0,150)
        no_stroke()
        if selected.position[1] % 2 == 0:
            circle(selected.position[0]*width//8*2 + width//16, selected.position[1]*height//8 + height//16, 36)
        else:
            circle(selected.position[0]*width//8*2 + width//16 + width//8, selected.position[1]*height//8 + height//16, 36)
        
def drawTiles():
    stroke(0);
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
    board = [[0 for x in range(8)] for y in range(4)]
    for x in range(0,4):
        for y in range(0,3):
            board[x][y] = Checker([x,y], "black")
            
    for x in range(0,4):
        for y in range(5,8):
            board[x][y] = Checker([x,y], "red")
    #print(board);

            
def mouse_pressed():
    global selected
    row = mouse_y // (height // 8)
    
    if row % 2 == 0:
        px = mouse_x - width // 16
    else:
        px = mouse_x - width // 16 - width // 8
    
    bx = round(px / (width // 4))
    
    
    print(f"board: ({bx}, {row})")
    
    if selected == None:
        # first click select a piece
        if board[bx][row] != 0:
            print("selected checker")
            selected = board[bx][row]
    else:
        # second click try to move
        if board[bx][row] == 0:
            
            if selected.canJump(bx,row):
                if selected.color == "red":
                    if(row % 2 == 0):
                        #if a checker is between a canjump tile for red only
                        if board[bx - 1][row - 1] != 0:
                            print("jumpHere")
                        elif board[bx][row - 1] != 0:
                            print("jumpHere")
                    else:
                        if board[bx - 1][row - 1] != 0:
                            print("jumpHere")
                        elif board[bx][row - 1] != 0:
                            print("jumpHere")
                else:
                    if(row % 2 == 0):
                        #if a checker is between a canjump tile for black only
                        if (board[bx - 1][row + 1] != 0):
                            print("jumpHere")
                        elif board[bx][row + 1] != 0:
                            print("jumpHere")
                    else:
                        if board[bx - 1][row + 1] != 0:
                            print("jumpHere")
                        elif board[bx][row + 1] != 0:
                            print("jumpHere")
                            
            elif selected.canMove(bx, row):
                board[selected.position[0]][selected.position[1]] = 0
                selected.move(bx, row)
                board[bx][row] = selected
                selected = None
            else:
                print(f"trying to move from {selected.position} to ({bx},{row})")
                print("cannot move here")
        else:
            # clicked another piece, re-select
            selected = board[bx][row]
        
            