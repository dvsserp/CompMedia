import numpy as np
def setup():
    size(200,200)
    background(0)
    initState()
def changeState(x,y):
    if(np_pixels[y,x,1] == 255):
        np_pixels[y,x,:] = [100,0,0,0]
    else:
        np_pixels[y,x,:] = [100,255,0,0]
    update_np_pixels()
    
def initState():
    load_np_pixels()
    np_pixels[height//2:height//2+1, width//2-5:width//2+5,  :] = [100,255,0,0]
    np_pixels[height//2 - 10:height//2+10, width//2-5:width//2-4,  :] = [100,255,0,0]
    np_pixels[height//2 - 10:height//2+10, width//2+4:width//2+5,  :] = [100,255,0,0]
    update_np_pixels()
    
def checkNeighbor():
    load_np_pixels()
    BLACK = [100,0,0,0]
    RED = [100,255,0,0]
    for x in range(width-1):
        for y in range(height-1):
            count = 0
            if np.array_equal(np_pixels[y,x,:], BLACK):
                if np.array_equal(np_pixels[y,x-1,:], RED):
                    count += 1
                if np.array_equal(np_pixels[y,x+1,:],RED):
                    count += 1
                if np.array_equal(np_pixels[y-1,x,:], RED):
                    count += 1
                if np.array_equal(np_pixels[y+1,x,:], RED):
                    count += 1
                if (count%2 == 1):
                    changeState(x,y)
            else:
                if np.array_equal(np_pixels[y,x-1,:], RED):
                    count += 1
                if np.array_equal(np_pixels[y,x+1,:], RED):
                    count += 1
                if np.array_equal(np_pixels[y-1,x,:], RED):
                    count += 1
                if np.array_equal(np_pixels[y+1,x,:], RED):
                    count += 1
                if(count%2 == 0):
                    changeState(x,y)
    update_np_pixels()
def draw():
    checkNeighbor()