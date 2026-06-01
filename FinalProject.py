from Checker import *
#checkers
board = [[]]
selected = None
turn = "black"
winner = None

crownX = 200
crownY = 200
crownSpeedX = 3
crownSpeedY = 2
crownAngle = 0

def setup():
    global board, winner
    size(400,400)
    background(255,0,0)
    initialSetup()
    #print(board)
def draw():
    global board, selected
    if winner != None:
        showWinner()
        return
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
        if board[bx][row] != 0 and board[bx][row].color == turn.lower():
            print("selected checker")
            selected = board[bx][row]
    else:
        # second click try to move
        if board[bx][row] == 0:
            
            if selected.canJump(bx, row):
                midX = (selected.position[0] + bx) // 2
                midY = (selected.position[1] + row) // 2

                if midY % 2 == 0:
                    midX = max(selected.position[0], bx)
                else:
                    midX = min(selected.position[0], bx)
                print(f"midX: {midX}, midY: {midY}")
                print(f"midpiece: {board[midX][midY]}")
                if board[midX][midY] != 0 and board[midX][midY].color != selected.color:
                    print("jumping!")
                    board[midX][midY] = 0
                    board[selected.position[0]][selected.position[1]] = 0
                    selected.move(bx, row)
                    board[bx][row] = selected
                    checkKing()
                    switchTurn()
                    checkWinner()
                    selected = None
                            
            elif selected.canMove(bx, row):
                board[selected.position[0]][selected.position[1]] = 0
                selected.move(bx, row)
                board[bx][row] = selected
                switchTurn()
                checkKing()
                checkWinner()
                selected = None
            else:
                print(f"trying to move from {selected.position} to ({bx},{row})")
                print("cannot move here")
        else:
            # clicked another piece, re-select
            selected = board[bx][row]
            
def checkKing():
    for x in range(0,4):
        for y in range(0,8):
            if board[x][y] != 0:
                if board[x][y].color == "black" and y == 7:
                    board[x][y].changeStatus()
                elif board[x][y].color == "red" and y == 0:
                    board[x][y].changeStatus()
                    
def switchTurn():
    global turn
    if turn == "black":
        turn = "red"
    else:
        turn = "black"
        
def checkWinner():
    global winner
    blackCount = 0
    redCount = 0
    for x in range(0,4):
        for y in range(0,8):
            if board[x][y] != 0:
                if board[x][y].color == "black":
                    blackCount += 1
                elif board[x][y].color == "red":
                    redCount += 1
    if blackCount == 0:
        winner = "Red"
    elif redCount == 0:
        winner = "Black"

def drawCrown():
    fill("#FFFF00")
    stroke(200, 150, 0)
    stroke_weight(2)
    begin_shape()
    vertex(-20, 10)
    vertex(20, 10)
    vertex(20, -5)
    vertex(10, 5)
    vertex(0, -10)
    vertex(-10, 5)
    vertex(-20, -5)
    vertex(-20, 10)
    end_shape(CLOSE)

def showWinner():
    #Skill 12
    global winner, crownX, crownY, crownSpeedX, crownSpeedY, crownAngle
    load_np_pixels()
    #invert all pixels
    np_pixels[:, :, 0] = 255 - np_pixels[:, :, 0]
    np_pixels[:, :, 1] = 255 - np_pixels[:, :, 1]
    np_pixels[:, :, 2] = 255 - np_pixels[:, :, 2]
    #boost winner color channel
    if winner == "Red" or winner == "red":
        np_pixels[:, :, 0] = np.clip(np_pixels[:, :, 0] + 100, 0, 255)
        np_pixels[:, :, 1] = np_pixels[:, :, 1] // 2
        np_pixels[:, :, 2] = np_pixels[:, :, 2] // 2
    else:
        np_pixels[:, :, 2] = np.clip(np_pixels[:, :, 2] + 100, 0, 255)
        np_pixels[:, :, 0] = np_pixels[:, :, 0] // 2
        np_pixels[:, :, 1] = np_pixels[:, :, 1] // 2
    update_np_pixels()
    #Skill 11 and 9
    #update bouncing crown position
    crownX += crownSpeedX
    crownY += crownSpeedY
    #bounce off edges
    if crownX > width - 20 or crownX < 20:
        crownSpeedX *= -1
    if crownY > height - 20 or crownY < 20:
        crownSpeedY *= -1
    #spin the crown
    crownAngle += 0.05
 
    #draw bouncing rotating crown using transformations
    push_matrix()
    translate(crownX, crownY)
    rotate(crownAngle)
    drawCrown()
    pop_matrix()
    
    #draw winner text on top
    fill(255)
    stroke(0)
    #Skill 2
    stroke_weight(3)
    text_size(40)
    text_align(CENTER, CENTER)
    text(winner + " Wins!", width//2, height//2)
    text_size(16)
    text("Press R to restart", width//2, height//2 + 50)
    
def key_pressed():
    #R to restart W for winner screen
    #Skill 5
    global winner, selected, turn
    if key == 'r' or key == 'R':
        background(255,0,0)
        initialSetup()
        selected = None
        turn = "black"
        winner = None
    elif key == 'w' or key == 'W':
        winner = turn
            
