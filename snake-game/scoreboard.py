from turtle import Turtle

HOME = (0,275)
SCORE_ALIGN = "center"
SCORE_FONT = "Verdana"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.write_score()
        
    
        

    def increase_score(self):
        self.score += 1

    def write_score(self):
        self.goto(HOME)
        self.clear()
        self.write(arg= f"Score: {self.score} High Score: {self.high_score}",align=SCORE_ALIGN, font=(SCORE_FONT,24,'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt","w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()
    
