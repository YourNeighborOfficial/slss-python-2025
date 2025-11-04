# Turtle Artist
# Author: Julian Sauvageau
# 28 October

import turtle

# A one-of-a-kind drawing

# SET UP
wn = turtle.Screen()
t = turtle.Turtle()
turtle.bgcolor("midnight blue")

t.penup()
t.speed(0)
# t.goto(-630, -520)

# drawing the shape i will be using for the entire project


def draw_rectangle(width: int, height: int, x: int, y: int, colour: str):
    """Draws a rectangle in place"""
    t.pu()
    t.goto(x, y)  # go to the x and y location
    t.setheading(90)  # point up
    t.fillcolor(colour)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


# blueprint the first layer of buildings


def draw_building1(x: int, y: int):
    # Draw a building using draw_rectangle
    draw_rectangle(300, 75, x, y, "darkgrey")
    for counter in range(8):
        counter = counter * 35
        draw_rectangle(20, 20, x + 5, y + 270 - counter, "yellow")
    for counter in range(8):
        counter = counter * 35
        draw_rectangle(20, 20, x + 50, y + 270 - counter, "yellow")


def draw_building2(x: int, y: int):
    draw_rectangle(200, 400, x, y, "darkgrey")
    for counter in range(8):
        counter = counter * 50
        draw_rectangle(20, 20, x + 15 + counter, y + 170, "yellow")
    for counter in range(8):
        counter = counter * 50
        draw_rectangle(20, 20, x + 15 + counter, y + 130, "yellow")
    for counter in range(8):
        counter = counter * 50
        draw_rectangle(20, 20, x + 15 + counter, y + 90, "yellow")
    for counter in range(8):
        counter = counter * 50
        draw_rectangle(20, 20, x + 15 + counter, y + 50, "yellow")


def draw_building3(x: int, y: int):
    draw_rectangle(450, 250, x, y, "darkgrey")
    for counter in range(12):
        counter = counter * 35
        draw_rectangle(20, 20, x + 10, y + 420 - counter, "yellow")
    for counter in range(12):
        counter = counter * 35
        draw_rectangle(20, 20, x + 45, y + 420 - counter, "yellow")
    for counter in range(12):
        counter = counter * 35
        draw_rectangle(20, 20, x + 80, y + 420 - counter, "yellow")
    for counter in range(12):
        counter = counter * 35
        draw_rectangle(20, 20, x + 115, y + 420 - counter, "yellow")
    for counter in range(12):
        counter = counter * 35
        draw_rectangle(20, 20, x + 150, y + 420 - counter, "yellow")
    for counter in range(12):
        counter = counter * 35
        draw_rectangle(20, 20, x + 185, y + 420 - counter, "yellow")
    for counter in range(12):
        counter = counter * 35
        draw_rectangle(20, 20, x + 220, y + 420 - counter, "yellow")


def draw_building4(x: int, y: int):
    draw_rectangle(375, 500, x, y, "darkgrey")
    for counter in range(14):
        counter = counter * 30
        draw_rectangle(20, 20, x + 10 + counter, y + 340, "yellow")
    for counter in range(14):
        counter = counter * 30
        draw_rectangle(20, 20, x + 10 + counter, y + 300, "yellow")
    for counter in range(14):
        counter = counter * 30
        draw_rectangle(20, 20, x + 10 + counter, y + 150, "yellow")
    for counter in range(14):
        counter = counter * 30
        draw_rectangle(20, 20, x + 10 + counter, y + 110, "yellow")


def draw_funnel(x: int, y: int):
    draw_rectangle(125, 50, x, y, "darkgrey")


# blueprint for the second layer of buildings


def draw_layer1(x: int, y: int):
    draw_rectangle(575, 1500, x, y, "grey")


def draw_layer2(x: int, y: int):
    draw_rectangle(300, 500, x, y, "grey")


# blueprint for the third layer of the buildings


def draw_bg1(x: int, y: int):
    draw_rectangle(575, 3000, x, y, "#666666")


def draw_bg2(x: int, y: int):
    draw_rectangle(100, 250, x, y, "#666666")


def draw_bg3(x: int, y: int):
    draw_rectangle(200, 150, x, y, "#666666")


def draw_bg4(x: int, y: int):
    draw_rectangle(150, 300, x, y, "#666666")


def draw_bg5(x: int, y: int):
    draw_rectangle(125, 400, x, y, "#666666")


def draw_bg6(x: int, y: int):
    draw_rectangle(400, 125, x, y, "#666666")


# blueprint for the stars


def draw_star(radius: int, x: int, y: int, color: str):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y - radius)  # Move to the bottom of where the circle will be
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# time to draw
#
# drawing the third layer

draw_star(10, 500, 500, "yellow")
draw_star(8, -500, 440, "yellow")
draw_star(5, -323, 350, "yellow")
draw_star(2, 579, 401, "yellow")
draw_star(4, 476, 275, "yellow")
draw_star(1, -100, 300, "yellow")
draw_star(6, -20, 430, "yellow")
draw_star(3, 0, 245, "yellow")
draw_star(4, -439, 267, "yellow")
draw_star(3, -550, 390, "yellow")
draw_star(2, -80, 150, "yellow")
draw_star(4, -120, 127, "yellow")
draw_star(3, -100, 520, "yellow")
draw_star(5, 458, 509, "yellow")
draw_star(6, -300, 167, "yellow")
draw_star(4, -460, 180, "yellow")
draw_star(3, 395, 300, "yellow")
draw_star(2, 443, 432, "yellow")
draw_star(4, 470, 200, "yellow")
draw_star(3, 430, 150, "yellow")
draw_star(4, 350, 340, "yellow")
draw_star(3, 225, 300, "yellow")
draw_star(2, 200, 450, "yellow")
draw_star(6, 150, 378, "yellow")
draw_star(3, -500, 300, "yellow")


draw_bg1(-640, -540)
draw_bg2(-640, -40)
draw_bg3(-50, -40)
draw_bg4(-540, -40)
draw_bg5(150, -40)
draw_bg6(25, -40)
draw_bg3(100, 0)
draw_bg4(500, 0)

# drawing the second layer
draw_layer1(-640, -720)
draw_layer2(300, -400)
draw_layer2(-400, -350)

# drawing the first layer

draw_building1(-640, -540)
draw_building2(-535, -540)
draw_building3(-100, -540)
draw_building4(250, -540)
draw_funnel(300, -170)
draw_funnel(500, -170)


wn.exitonclick()
