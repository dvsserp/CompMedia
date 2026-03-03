inRace = []
def setup():
    global inRace
    size(600,400)
    for i in range(0,4):
        inRace.append(i)
        inRace[i] = {
            "x" : 0,
            "y" : 100 * (i+1),
            "speed" : int(random(1,10)),
            "lap" : 0,
            "number" : i + 1
            }
    #print(inRace)
def draw():
    global inRace
    background(225)
    for i in range(1,4):
        line(0, 100 * i, width, 100 * i)
    for i in range(0,4):
        circle(inRace[i]["x"], inRace[i]["y"] - 50, 30)
        inRace[i]["x"] += inRace[i]["speed"]
        if inRace[i]["x"] > width:
            inRace[i]["x"] = 0
            inRace[i]["speed"] = int(random(1,10))
            inRace[i]["lap"] += 1
        if inRace[i]["lap"] == 3:
            frame_rate(0)
            background(0,170,0)
            text_size(40)
            text("WINNER: " + str(inRace[i]["number"]), 200,200)
        else:
            fill(0)
            text("lap: " + str(inRace[i]["lap"]), width - 50, inRace[i]["y"] - 50)
            fill(255)