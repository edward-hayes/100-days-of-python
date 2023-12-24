from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("#4A545D")
screen.title("My Snake Game")

snake_length = 3
snake_body = []
starting_positions = [(0,0), (-20,0), (-40,0)]

for snake_segment in range(snake_length):
    new_snake_segment = Turtle(shape="square")
    new_snake_segment.color("#DC7726")
    new_snake_segment.penup()
    new_snake_segment.goto(starting_positions[snake_segment])
    snake_body.append(new_snake_segment)





screen.exitonclick()

