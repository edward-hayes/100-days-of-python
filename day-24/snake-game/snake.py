from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def clear(self):
        for segment in self.snake_body:
            segment.hideturtle()

    def refresh(self):
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment -1].ycor()
            self.snake_body[segment].goto(x=new_x, y =new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_snake_segment = Turtle(shape ="square")
        new_snake_segment.color("#DC7726")
        new_snake_segment.penup()
        new_snake_segment.goto(position)
        self.snake_body.append(new_snake_segment)

    def add_to_tail(self):
        self.add_segment(self.snake_body[-1].position())

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