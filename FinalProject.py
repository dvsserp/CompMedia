#checkers
tile = [[]]
def setup():
    size(400,400)
    background(255,0,0)

def draw():
    drawTiles()
    
def drawTiles():
    for x in range(0,width,width//8):
        for y in range(0,height,height//8):
            if(x % ((width//8) * 2) == 0 and y % ((height//8) * 2) == 0):
                fill(0)
                rect(x,y,width//8,height//8)
            elif (x % ((width//8) * 2) == width//8 and y % ((height//8) * 2) == height//8):
                fill(0)
                rect(x,y,width//8,height//8)
    
    