from email import header
from turtle import Screen, Turtle, heading
import random

pen = Turtle()
pen.width(2)
pen.speed(0)

colors = ["#DC7726", "#DDC077", "#57896A", "#4A545D", "#067593", "#055772", "#09A9C8"]
radius = 180

def draw_spirograph(size_of_gap, colors, radius):
    for i in range(int(360/size_of_gap)):
        pen.setheading(pen.heading() + size_of_gap)
        pen.pencolor(random.choice(colors))
        pen.circle(radius)

draw_spirograph(3, colors, radius)

print("done")

screen = Screen()
screen.exitonclick()