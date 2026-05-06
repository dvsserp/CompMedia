import numpy as np

def apply_tint(tintx,tinty):
    global original
    A,r,g,b = 0,1,2,3 # unpack variables for the color indices
    np_pixels[:, :, r] = np.clip(original[:, :, r] + tintx, 0, 255)
    np_pixels[:, :, g] = np.clip(original[:, :, g] + tintx - tinty, 0,255)
    np_pixels[:, :, b] = np.clip(original[:, :, b] + tinty, 0, 255)
    
    update_np_pixels()

def setup():
    global original
    size(700, 500)
    
    img = load_image("./Memes/Meme4.jpg")
    img.resize(width, height)
    image(img, 0, 0)

    load_np_pixels()
    load_pixels()
    original = np_pixels.copy()
    q1 = get_pixels(0,0,width//2,height//2)
    tint(255,0,0)
    image(q1,0,0)
    q2 = get_pixels(width//2,0,width//2,height//2)
    tint(0,255,0)
    image(q2, width//2, 0)
    q3 = get_pixels(width//2,height//2,width//2,height//2)
    tint(0,0,255)
    image(q3,width//2, height//2)
    q4 = get_pixels(0, height//2, width//2,height//2)
    tint(0,0,0,70)
    image(q4, 0, height//2)
    
def draw():
    tintx = remap(mouse_x, 0, width, 0, 255)
    tinty = remap(mouse_y, 0, height, 0,255)
    apply_tint(tintx,tinty)