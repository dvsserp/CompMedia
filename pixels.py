pixelLst = []
def setup():
    global pixelLst
    size(400,400)
    load_image("./Memes/Meme2.jpg")
    load_pixels()
    for x in range(width):
        for y in range(height):
            pixels.append(get_pixels(x,y))
    print(pixels)
def draw():
    load_image("./Memes/Meme2.jpg")
