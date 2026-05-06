import numpy as np

def limit(value):
  # keeps color values between 0 and 255
  return max(0, min(255, int(value)))
def apply_temp(temp):
    global original
    # Temperature adjustment
    # positive = warm (more red, less blue)
    # negative = cool (more blue, less red)      
    for x in range(width):
        for y in range(height):
            clr = original[x][y]        
            nr = limit(red(clr) + temp)         		# modify red
            ng = limit(green(clr) + temp * 0.3)  	# modify green a little
            nb = limit(blue(clr) - temp)         	# modify blue       
            np_pixels[y:height,x:width, 1] = color(nr, ng, nb)
    update_np_pixels()
def get_pixelLst():
    pixelLst = [[0 for y in range(height)] for x in range(width)]
    for x in range(width): 
        for y in range(height): 
            pixelLst[x][y] = get_np_pixels(x,y)
    return pixelLst
def setup():
    global original
    size(350, 250)
    img = load_image("./Memes/Meme3.jpg")
    img.resize(width, height)    
    image(img, 0, 0)
    original = np_pixels.copy()
    load_np_pixels()
def mouse_clicked():
    temp = remap(mouse_x, 0, width, -100, 100)
    apply_temp(temp)
