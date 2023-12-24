from turtle import Turtle, distance, down

MOVE_DISTANCE = 30
BOUNDARY = 240

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("#DC7726")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position)

    def up(self):
        y_position = self.ycor()
        if y_position < BOUNDARY:
            new_y = y_position + MOVE_DISTANCE
            self.setpos(y=new_y, x=self.xcor())
            print(self.position())
        else:
            print("out of bounds")
    def down(self):
        y_position = self.ycor()
        if y_position > -BOUNDARY:
            new_y = y_position - MOVE_DISTANCE
            self.setpos(y=new_y, x=self.xcor())
            print(self.position())
        else:
            print("out of bounds")

    

