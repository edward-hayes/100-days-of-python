from turtle import Screen, Turtle

pen = Turtle()
pen.color("coral")
pen.speed(0)
side = 15

def spiral(side):
    pen.forward(side)
    pen.left(70)
    side += 30
    
for x in range(90):
    if (x % 2) == 0:
        pen.color("coral")
        pen.forward(side)
        pen.left(70)
        side += 5
    else:
        pen.color("cyan4")
        pen.forward(side)
        pen.left(70)
        side += 5

screen = Screen()
screen.exitonclick()