from PIL import Image

memeList = []

def setup():
    size(300,300)
    for i in range(5):
        memeList.append('Memes/Meme' + str(i+1) + '.jpg')
    im = Image(memeList[int(random(5))])
def draw():
    image(im, 10, 10, 250, 250)