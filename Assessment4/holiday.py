from IceCreamClass import *

animation_frame = 0
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
    ice.y = -80


def draw():
    global ice, animation_frame
    background(210, 30, 100)
    translate(width / 2, height / 2)
    drawCardFrame()
    drawGreeting()
    
    # Animated bouncing ice cream
    updateIceCream()
    bounce = 20 * abs(sin(animation_frame * 0.08))
    push_matrix()
    translate(0, bounce)
    ice.drawIceCream()
    ice.drawToppings()
    pop_matrix()
    
    drawAnimatedDecorations()
    Palette()
    animation_frame += 1


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
    text_size(48)
    text_align(CENTER)
    text("Happy National Icecream Day!", 0, -height / 2 + 80)
    text_size(28)
    text("A sweet gift just for you.", 0, -height / 2 + 130)
    text_size(20)
    text("Select your ice cream below", 0, height / 2 - 100)
    text_align(LEFT)


def drawAnimatedDecorations():
    """Draw animated snowflakes and decorative elements"""
    global animation_frame
    
    # large floating snowflakes with wave motion
    fill(180, 100, 100)  # Cyan color
    no_stroke()
    snowflake_positions = [
        (-350, -300),
        (350, -250),
        (-300, 0),
        (300, 80),
        (-200, -150),
        (200, -350),
        (-280, 150),
        (280, -100)
    ]
    
    for sx, sy in snowflake_positions:
        # wave motion for snowflakes
        offset_x = 25 * sin(animation_frame * 0.03 + sx * 0.005)
        offset_y = 15 * cos(animation_frame * 0.04 + sy * 0.005)
        scale1 = 1.0 + 0.3 * sin(animation_frame * 0.05)
        circle(sx + offset_x, sy + offset_y, 12 * scale1)
    
    # button effect
    pulse = 1.0 + 0.1 * sin(animation_frame * 0.06)
    for i in range(len(toppings)):
        x = -width / 2 + i * 180 + 60 + 30
        y = height / 2 - 190 + 17.5
        push_matrix()
        translate(x, y)
        scale(pulse)
        translate(-x, -y)
        no_stroke()
        fill(255, 255, 255, 20)
        rect(x - 30, y - 17.5, 60, 35, 8)
        pop_matrix()





def Palette():
    global colors, toppings, sColor, selected_color, selected_topping, selected_cone
    no_stroke()
    fill(0)
    text_size(18)
    text_align(LEFT)
    
    # Toppings palette
    text("Toppings:", -width / 2 + 60, height / 2 - 220)
    for i in range(len(toppings)):
        x = -width / 2 + i * 180 + 60
        y = height / 2 - 190
        if selected_topping == i:
            stroke(0)
            stroke_weight(3)
        else:
            no_stroke()
        fill(255)
        rect(x, y, 60, 35, 8)
        no_stroke()
        fill(0)
        text_size(14)
        text(toppings[i], x + 8, y + 24)
    
    # Colors palette
    text("Colors:", -width / 2 + 60, height / 2 - 110)
    for i in range(len(sColor)):
        x = -width / 2 + (i % 4) * 130 + 60
        y = height / 2 - 80 if i < 4 else height / 2 - 35
        if selected_color == i:
            stroke(0)
            stroke_weight(3)
        else:
            no_stroke()
        fill(colors[sColor[i]], 100, 100)
        rect(x, y, 60, 35, 8)
        no_stroke()
        fill(0)
        text_size(12)
        text(sColor[i], x + 5, y + 23)
    
    # Cone options
    text("Cone:", -width / 2 + 60, height / 2 + 40)
    for i in range(2):
        x = -width / 2 + i * 120 + 60
        if selected_cone == i:
            stroke(0)
            stroke_weight(3)
        else:
            no_stroke()
        fill(255)
        rect(x, height / 2 + 55, 60, 35, 8)
        no_stroke()
        fill(0)
        text_size(14)
        text(cone_options[i], x + 3, height / 2 + 75)


def mouse_pressed():
    global selected_color, selected_topping, selected_cone
    mx = mouse_x - width / 2
    my = mouse_y - height / 2
    
    # Check toppings
    for i in range(len(toppings)):
        x = -width / 2 + i * 180 + 60
        if collidePointRect(mx, my, x, height / 2 - 190, 60, 35):
            selected_topping = i
    
    # Check colors
    for i in range(len(sColor)):
        x = -width / 2 + (i % 4) * 130 + 60
        y = height / 2 - 80 if i < 4 else height / 2 - 35
        if collidePointRect(mx, my, x, y, 60, 35):
            selected_color = i
    
    # Check cone options
    for i in range(2):
        x = -width / 2 + i * 120 + 60
        if collidePointRect(mx, my, x, height / 2 + 55, 60, 35):
            selected_cone = i


def collidePointRect(pX, pY, rX, rY, rW, rH):
    """Input x,y coordinates of point and x, y, width, and height of rectangle.
    Returns true if the point and rectangle are touching."""
    if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
        return True
    else:
        return False
