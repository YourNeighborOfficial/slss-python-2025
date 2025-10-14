
# Drawing and Loops
# Author: Me
# 14 october 2025


import turtle

window = turtle.Screen()  # Set up the window
window.bgcolor("red")

# create a turtle named mike
mike = turtle.Turtle()
mike.turtlesize(20) # set size
mike.shape("turtle") # shape
mike.color("orange") # color

# move mike around
mike.speed(1)
mike.penup()
mike.forward(1000)
mike.left(90)


window.exitonclick()
