def setup():
    size(400,400)
    img = load_image("./Memes/Meme3.jpg")
    img.resize(width,height)
    image(img,0,0)
    load_pixels()
    