seconds = second()
minutes = minute()
hours = hour()
morseCode = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
AM = True
def setup():
    size(400,400)
    
def draw():
    global seconds, minutes, hours, AM, morseCode
    background(255)
    if frame_count % 60 == 0:
        seconds += 1

    if (seconds == 60):
        seconds = 0
        minutes+=1
        
    if (minutes == 60):
        minutes = 0
        hours += 1
    
    if(hours >= 12):
        #switches am to pm or pm to am
        if AM:
            AM = False
        else:
            AM = True
        hours = 0
    if(AM):
        fill("#FFB74D")
    else:
        fill("#191970")
    text_size(50)
    if(hours > 9):
        text(morseCode[hours//10], 100, 100)
        text(morseCode[hours%10], 300, 100)
    else:
        text(morseCode[hours], 200, 100)
    
    if(minutes > 9):
        text(morseCode[minutes//10], 100, 200)
        text(morseCode[minutes%10], 300, 200)
    else:
        text(morseCode[minutes], 200, 200)
       
    if(seconds > 9):
        text(morseCode[seconds//10], 100, 300)
        text(morseCode[seconds%10], 300, 300)
    else:
        text(morseCode[seconds], 200, 300)
    
    