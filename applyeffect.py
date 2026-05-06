def setup():
    global filter1, original
    size(400,400)
    img = load_image("./Memes/family1.jpg")
    img.resize(width,height)
    image(img,0,0)
    load_np_pixels()
    original = np_pixels.copy()
    quadrant_effect(0,width//2,0,height//2, "invert");
    quadrant_effect(width//2, width, 0, height//2, "gray")
            
def quadrant_effect(x0,x1,y0,y1,effect):
    global original
    A,r,g,b = 0, 1, 2, 3
    if effect == "invert":
        np_pixels[x0:x1,y0:y1,r] = np.clip(abs(255-original[x0:x1,y0:y1,r]),0,255)
        np_pixels[x0:x1,y0:y1,g] = np.clip(abs(255-original[x0:x1,y0:y1,g]),0,255)
        np_pixels[x0:x1,y0:y1,b] = np.clip(abs(255-original[x0:x1,y0:y1,b]),0,255)
    if effect == "gray":
        np_pixels[x0:x1, y0:y1, r] = np.clip((original[x0:x1,y0:y1,r] + original[x0:x1,y0:y1,g] + original[x0:x1,y0:y1,b])//3,0,255)
        np_pixels[x0:x1, y0:y1, g] = np.clip((original[x0:x1,y0:y1,r] + original[x0:x1,y0:y1,g] + original[x0:x1,y0:y1,b])//3,0,255)
        np_pixels[x0:x1, y0:y1, b] = np.clip((original[x0:x1,y0:y1,r] + original[x0:x1,y0:y1,g] + original[x0:x1,y0:y1,b])//3,0,255)
    update_np_pixels()