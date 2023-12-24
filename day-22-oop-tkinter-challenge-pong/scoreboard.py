from turtle import Turtle

HOME = (0,275)
SCORE_ALIGN = "center"
SCORE_FONT = "Verdana"
COLOR = "#DDC077"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.speed("fastest")
        self.pencolor(COLOR)
        self.write_score()

    def increase_score(self, side):
        if side == "left":
            self.left_score += 1
        if side == "right":
            self.right_score += 1

    def write_score(self):
        self.goto(HOME)
        self.clear()
        self.write(arg= f"{self.left_score}  Score  {self.right_score}",align=SCORE_ALIGN, font=(SCORE_FONT,24,'normal'))
        self.dashed_line()

    def game_over(self):
        self.write_score()
        self.penup()
        self.home()
        self.pendown()
        self.write(arg="GAME OVER", align=SCORE_ALIGN, font=(SCORE_FONT,24,'normal'))

    def dashed_line(self):
        self.penup()
        self.goto(x=0,y=-300)
        self.pensize(3)
        self.setheading(90)
        for x in range(57):
            if (x % 2) == 0:
                self.penup()
                self.forward(10)
            else:
                self.pendown()
                self.forward(10)
            