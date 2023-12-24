from turtle import Turtle

HOME = (0,275)
SCORE_ALIGN = "center"
SCORE_FONT = "Verdana"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.write_score()
        


    def increase_score(self):
        self.score += 1

    def write_score(self):
        self.goto(HOME)
        self.clear()
        self.write(arg= f"Score: {self.score}",align=SCORE_ALIGN, font=(SCORE_FONT,24,'normal'))

    def game_over(self):
        self.write_score()
        self.penup()
        self.home()
        self.pendown()
        self.write(arg="GAME OVER", align=SCORE_ALIGN, font=(SCORE_FONT,24,'normal'))

    
