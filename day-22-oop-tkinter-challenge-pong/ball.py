from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("cyan4")
        self.speed("fastest")
        self.turn = "right"
        self.refresh()
        self.move_distance = 4
        self.bounce = 1
    
    def move(self):
        self.forward(self.move_distance)

    def y_bounce(self):
        self.setheading(360-self.heading())
        self.bounce += 1
        if (self.bounce % 4):
            self.move_distance += 1

    def x_bounce(self):
        self.setheading(540-self.heading())
        self.bounce += 1
        if (self.bounce % 4):
            self.move_distance += 1

    def change_turn(self, current_turn):
        if current_turn == "left":
            self.turn = "right"
        elif current_turn == "right":
            self.turn = "left"
    
    def refresh(self):
        self.home()
        self.bounce = 1
        self.move_distance = 4
        if self.turn == "right":
            self.seth(random.randrange(315,405) % 360)
            self.change_turn(self.turn)
        elif self.turn == "left":
            self.seth(random.randrange(135,225) % 360)
            self.change_turn(self.turn)

    