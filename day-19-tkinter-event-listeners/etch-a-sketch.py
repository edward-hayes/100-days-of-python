from itertools import count
from turtle import Turtle, Screen, home

pen = Turtle()
screen = Screen()

def move_forward():
    pen.forward(10)
    print(pen.position())

def move_backward():
    pen.backward(10)
    print(pen.position())

def turn_clockwise():
    pen.setheading(pen.heading() + 10)
    print(pen.heading())

def turn_counterclockwise():
    pen.setheading(pen.heading() - 10)
    print(pen.heading())

def clear():
    pen.up()
    pen.home()
    pen.down()
    pen.clear()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_counterclockwise)
screen.onkey(key="a", fun=turn_clockwise)
screen.onkey(key="c", fun=clear)

screen.listen()

screen.exitonclick()