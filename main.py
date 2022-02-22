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
def random_color():
    r = int(random.randint(40,255))
    g = int(random.randint(40, 255))
    b = int(random.randint(30, 255))
    return  r,g,b
screen = Screen()
screen.colormode(255)
jimmy = Turtle()
n = 1
y = 30
# screen.bgcolor('black')
jimmy.penup()
jimmy.setposition(-250.00,-200)
jimmy.speed(100)
jimmy.hideturtle()
while n < 16:
    for i in range(10):
        jimmy.dot(20,random_color())
        jimmy.forward(50)
    jimmy.setposition(-250.00, -200 + y)
    n += 1
    y += 30


screen.exitonclick()
