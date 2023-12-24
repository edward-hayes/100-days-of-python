from turtle import Screen, Turtle, colormode
import random

pen = Turtle()
pen.width(8)
pen.speed(0)
colormode(255)

side = 20
border = 300

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for x in range(3000):
    if abs(pen.xcor()) > border or abs(pen.ycor()) > border:
        pen.undo()

    pen.color(random_color())
    pen.setheading(90*random.randrange(4))
    pen.forward(side)
    
    #side = random.randrange(28,33)

print("done")

screen = Screen()
screen.exitonclick()