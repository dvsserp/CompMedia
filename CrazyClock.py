seconds = second()
minutes = minute()
hours = hour()
morseCode = []
AM = True
def setup():
    global morseCode
    size(400,400)
    
def draw():
    global seconds, minutes, hours, AM
    background(255)
    if frame_count % 60 == 0:
        seconds += 1

    if (seconds == 60):
        seconds = 0
        minutes+=1
        
    if (minutes == 60):
        minutes = 0
        hours += 1
    
    if(hours == 12):
        #switches am to pm or pm to am
        if AM:
            AM = False
        else:
            AM = True
        hours = 0
    fill(0)
    text(str(hours) + str(minutes) + str(seconds), 200, 200)