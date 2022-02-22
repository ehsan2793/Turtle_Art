import random
from turtle import Turtle, Screen

import colorgram

colors = colorgram.extract('image.png', 20)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.b
    b = color.rgb.b
    rgb_colors.append((r, g, b))

screen = Screen()
screen.colormode(255)
jimmy = Turtle()
n = 1
y = 30
jimmy.penup()
jimmy.setposition(-100.00,-200)
jimmy.pendown()
while n < 10:
    for i in range(5):
        jimmy.dot(20,random.choice(rgb_colors))
        jimmy.penup()
        jimmy.forward(50)
        jimmy.pendown()
        jimmy.dot(20, random.choice(rgb_colors))
    jimmy.penup()
    jimmy.setposition(-100.00, -200 + y)
    n += 1
    y += 30


screen.exitonclick()
