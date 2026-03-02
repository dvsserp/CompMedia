def setup():
    global race1, race2, race3, race4
    size(600,500)
    for i in range(1,5):
        varName = "race" + str(i)
        varName = {
            "x" : width,
            "y" : 100 * i,
            "speed" : int(random(5))
            }