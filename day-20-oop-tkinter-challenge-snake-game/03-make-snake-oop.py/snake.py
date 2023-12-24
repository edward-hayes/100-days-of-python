from pickletools import UP_TO_NEWLINE
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, snake_length = 3):
        self.snake_body = []
        self.snake_length = snake_length
        self.create_snake(self.snake_length)
        self.head = self.snake_body[0]
        
    def create_snake(self, snake_length):
        for snake_segment in range(snake_length):
            new_snake_segment = Turtle(shape ="square")
            new_snake_segment.color("#DC7726")
            new_snake_segment.penup()
            new_snake_segment.goto(STARTING_POSITIONS[snake_segment])
            self.snake_body.append(new_snake_segment)

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment -1].ycor()
            self.snake_body[segment].goto(x=new_x, y =new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)