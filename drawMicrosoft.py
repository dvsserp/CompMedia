lineDict = {}
def setup():
    size(400,400)
    background(220)
    global lineDict
    lineDict = {
        "randOpacity": 150,
        "randWeight": 50,
        "weight": 10,
        "blue" : 255,
        "red": 255,
        "green": 255,
        }
def draw():
    opacity = 255
    if(int(random(10)) == 0):
        stroke_weight(lineDict["randWeight"])
        opacity = lineDict["randOpacity"]
    else:
        stroke_weight(lineDict["weight"])
        
    if(mouse_x > 200 and mouse_y > 200):
        stroke(lineDict["red"],lineDict["green"],0,opacity)
    if(mouse_x > 200 and mouse_y < 200):
        stroke(0,lineDict["green"],0,opacity)
    if(mouse_x < 200 and mouse_y > 200):
        stroke(0,0,lineDict["blue"],opacity)
    if(mouse_x < 200 and mouse_y < 200):
        stroke(lineDict["red"],0,0,opacity)
        
    line(mouse_x,mouse_y,pmouse_x,pmouse_y)