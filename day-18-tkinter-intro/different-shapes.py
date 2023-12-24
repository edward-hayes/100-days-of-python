from turtle import Screen, Turtle

pen = Turtle()
pen.color("coral")
pen.speed(0)
pen.up()
pen.goto(-15,-300)
length = 30
pen.down()

for sides in range(3,90):
    for i in range(sides):
        angle = 360/sides
        print(f"length is {length} / sides is {sides} / i is {i} / angle is {angle}")
        pen.forward(length)
        pen.left(angle)

screen = Screen()
screen.exitonclick()