from IceCreamClass import *

movex = 0
movey = 0
colors = {
    "red": 0,
    "orange": 30,
    "yellow": 60,
    "green": 120,
    "cyan": 180,
    "blue": 210,
    "purple": 270,
    "pink": 300
}
sColor = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]
toppings = ["None", "Sprinkles", "Gummies", "Cherry", "Chocolate"]
cone_options = ["cone", "no cone"]
selected_color = 0
selected_topping = 0
selected_cone = 0
ice = None


def setup():
    global ice
    size(1000, 1000)
    color_mode(HSB, 360, 100, 100)
    ice = IceCream(colors[sColor[selected_color]], True, 3, toppings[selected_topping])
    ice.x = 0
    ice.y = 120


def draw():
    global ice
    background(210, 30, 100)
    translate(width / 2, height / 2)
    drawCardFrame()
    updateIceCream()
    ice.drawIceCream()
    ice.drawToppings()
    drawGreeting()
    drawHAPPY()
    drawDAY()
    Palette()


def updateIceCream():
    global ice
    ice.color = colors[sColor[selected_color]]
    ice.cone = selected_cone == 0
    ice.toppings = toppings[selected_topping]


def drawCardFrame():
    no_stroke()
    fill(0, 0, 100)
    rect(-width / 2 + 20, -height / 2 + 20, width - 40, height - 40, 40)
    fill(210, 20, 95)
    rect(-width / 2 + 40, -height / 2 + 40, width - 80, height - 80, 30)
    stroke(0)
    stroke_weight(4)
    no_fill()
    rect(-width / 2 + 40, -height / 2 + 40, width - 80, height - 80, 30)
    no_stroke()


def drawGreeting():
    fill(0)
    text_size(54)
    text("Happy Holidays!", -200, -height / 2 + 120)
    text_size(28)
    text("A sweet gift just for you.", -200, -height / 2 + 170)
    text_size(24)
    text("Select a color, topping, and cone style below.", -200, -height / 2 + 210)
    text("From: Your Holiday Helper", -200, height / 2 - 70)


def drawHAPPY():
    global movex, movey
    leftSideHappy = -width / 4
    happyHeight = -height / 3
    amt = min(movex, 50)
    dist = min(movey, 50)
    circle(leftSideHappy, happyHeight + dist, 10)
    circle(leftSideHappy + 50, happyHeight + dist, 10)
    circle(leftSideHappy + amt, happyHeight + 25, 10)
    circle(leftSideHappy + amt / 2 + 100, happyHeight - dist + 50, 10)
    circle(leftSideHappy + amt / 2 + 125, happyHeight + dist, 10)
    circle(leftSideHappy + amt / 2 + 110, happyHeight + 25, 10)
    circle(leftSideHappy + 175, happyHeight + dist, 10)
    l = remap(amt, 1, 50, 1, 180)
    circle(leftSideHappy + 190 + cos(l) * 15, happyHeight + 15 + sin(l) * 15, 10)
    circle(leftSideHappy + 240, happyHeight + dist, 10)
    circle(leftSideHappy + 255 + cos(l) * 15, happyHeight + 15 + sin(l) * 15, 10)
    circle(leftSideHappy + 280 + amt / 2, happyHeight + dist / 2, 10)
    circle(leftSideHappy + 330 - amt / 2, happyHeight + dist / 2, 10)
    circle(leftSideHappy + 305, happyHeight + 30 + dist / 2, 10)
    if movex < 50:
        movex += 1
    if movey < 50:
        movey += 1


def drawDAY():
    global movex, movey
    leftSideDay = -width / 5
    dayHeight = height / 8
    amt = min(movex, 50)
    dist = min(movey, 50)
    arc(leftSideDay + 150, dayHeight + 25, 80, 60, radians(270), radians(450), CHORD)
    circle(leftSideDay + amt / 2 + 200, dayHeight - dist + 50, 10)
    circle(leftSideDay + amt / 2 + 225, dayHeight + dist, 10)
    circle(leftSideDay + amt / 2 + 210, dayHeight + 25, 10)
    circle(leftSideDay + 280 + amt / 2, dayHeight + dist / 2, 10)
    circle(leftSideDay + 330 - amt / 2, dayHeight + dist / 2, 10)
    circle(leftSideDay + 305, dayHeight + 30 + dist / 2, 10)


def Palette():
    global colors, toppings, sColor, selected_color, selected_topping, selected_cone
    fill(0)
    text_size(24)
    text("Toppings", -width / 2 + 60, height / 2 - 240)
    text("Colors", -width / 2 + 30, height / 2 - 160)
    text("Cone", -40, height / 2 - 90)
    for i in range(len(toppings)):
        x = -width / 2 + i * 200 + 60
        if selected_topping == i:
            stroke(0)
            stroke_weight(4)
        else:
            no_stroke()
        fill(255)
        rect(x, height / 2 - 200, 70, 50, 12)
        no_stroke()
        fill(0)
        text(toppings[i], x + 10, height / 2 - 175)
    for i in range(len(sColor)):
        x = -width / 2 + i * 120 + 30
        if selected_color == i:
            stroke(0)
            stroke_weight(4)
        else:
            no_stroke()
        fill(colors[sColor[i]], 100, 100)
        rect(x, height / 2 - 120, 70, 50, 12)
        no_stroke()
        fill(0)
        text(sColor[i], x + 10, height / 2 - 95)
    for i in range(2):
        x = -40 + i * 80
        if selected_cone == i:
            stroke(0)
            stroke_weight(4)
        else:
            no_stroke()
        fill(255)
        rect(x, height / 2 - 50, 70, 50, 12)
        no_stroke()
        fill(0)
        text(cone_options[i], x + 5, height / 2 - 25)


def mouse_pressed():
    global selected_color, selected_topping, selected_cone
    mx = mouse_x - width / 2
    my = mouse_y - height / 2
    for i in range(len(toppings)):
        if collidePointRect(mx, my, -width / 2 + i * 200 + 60, height / 2 - 200, 70, 50):
            selected_topping = i
    for i in range(len(sColor)):
        if collidePointRect(mx, my, -width / 2 + i * 120 + 30, height / 2 - 120, 70, 50):
            selected_color = i
    for i in range(2):
        if collidePointRect(mx, my, -40 + i * 80, height / 2 - 50, 70, 50):
            selected_cone = i


def collidePointRect(pX, pY, rX, rY, rW, rH):
    """Input x,y coordinates of point and x, y, width, and height of rectangle.
    Returns true if the point and rectangle are touching."""
    if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
        return True
    else:
        return False
