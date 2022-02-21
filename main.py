import random
import turtle
from turtle import Turtle, Screen

arr = ['red', 'cyan', 'green', 'DeepPink', 'purple', 'brown', 'black']
moves = [0, 90, -90]
screen = Screen()
screen.colormode(255)
jimmy = Turtle()
jimmy.pensize(12)
jimmy.speed(1000)


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# # while True:
for _ in range(100):
    jimmy.forward(3)
    jimmy.color(get_random_color())
    jimmy.right(random.choice(moves))
    jimmy.forward(10)

screen.exitonclick()
