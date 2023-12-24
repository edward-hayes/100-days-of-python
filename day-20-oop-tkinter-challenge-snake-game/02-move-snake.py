from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("#4A545D")
screen.title("My Snake Game")
screen.tracer(0)

snake_length = 3
snake_body = []
starting_positions = [(0,0), (-20,0), (-40,0)]

for snake_segment in range(snake_length):
    new_snake_segment = Turtle(shape="square")
    new_snake_segment.color("#DC7726")
    new_snake_segment.penup()
    new_snake_segment.goto(starting_positions[snake_segment])
    snake_body.append(new_snake_segment)
screen.update()
time.sleep(2)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[segment - 1].xcor()
        new_y = snake_body[segment -1].ycor()
        snake_body[segment].goto(x=new_x, y =new_y)
    snake_body[0].forward(20)


screen.exitonclick()

