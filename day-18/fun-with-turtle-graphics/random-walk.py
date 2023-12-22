from turtle import Screen, Turtle, pencolor
import random

pen = Turtle()
pen.width(8)
pen.speed(0)

colors = ["#DC7726", "#DDC077", "#57896A", "#4A545D", "#067593", "#055772", "#09A9C8"]
side = 20
border = 300

for x in range(3000):
    if abs(pen.xcor()) > border or abs(pen.ycor()) > border:
        pen.undo()

    pen.pencolor(random.choice(colors))
    pen.setheading(90*random.randrange(4))
    pen.forward(side)
    
    #side = random.randrange(28,33)

print("done")

screen = Screen()
screen.exitonclick()