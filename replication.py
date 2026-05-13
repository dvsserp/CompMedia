import numpy as np
def setup():
    size(200,200)
    background(0)
def changeState(x,y):
    if(np_pixels[y,x,1] == 255):
        np_pixels[y,x,:] == [100,0,0,0]
    else:
        np_pixels[y,x,1] = [100,255,0,0]
    update_np_pixels()
    
def initState():
    load_np_pixels()
    np_pixels[height//2:height//2+1, width//2-5:width//2+5,  :] = [100,255,0,0]
    np_pixels[height//2 - 10:height//2+10, width//2-5:width//2-4,  :] = [100,255,0,0]
    np_pixels[height//2 - 10:height//2+10, width//2+4:width//2+5,  :] = [100,255,0,0]
    update_np_pixels()
    
def checkNeighbor():
    BLACK = [100,0,0,0]
    RED = [100,255,0,0]
    count = 0
    for x in range(width):
        for y in range(height):
            if(np_pixels[y,x,:] == RED):
                count += 1
def draw():
    initState()