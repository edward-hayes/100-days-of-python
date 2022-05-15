from turtle import Screen, Turtle

pen = Turtle()
pen.color("coral")
pen.speed(0)

side = 20
pen.down

for x in range(180):
    for x in range(4):
        pen.forward(side)
        pen.left(90)
    pen.left(2)
    side += 5

pen.penup()
pen.goto(0,0)
pen.color("cyan4")
pen.pendown()
side = 19

for x in range(1,250):
    pen.forward(side)
    pen.left(118)
    side=side+2

screen = Screen()
screen.exitonclick()
