def setup_pixels(n):
    for x in range(width):
        for y in range(height):
            p = random(0,100)
            if p < n:
                np_pixels[y,x,2] = 255
            else:
                np_pixels[y,x,:] = [100,0,0,0]
    update_np_pixels()


def setup():
    global s
    size(400,400)
    s = [[[[0,0,0] for i in range(8)] for x in range(width)] for y in range(height)]
    background(0)
    load_np_pixels()
    setup_pixels(10)