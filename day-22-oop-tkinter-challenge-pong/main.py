import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


WIDTH = 400
LEFT = (-350,0)
RIGHT = (350,0)

screen = Screen()
screen.bgcolor("#055772")
screen.setup(height=600,width=WIDTH*2)
screen.title("Pong!")
screen.tracer(0)


score_board = Scoreboard()
left_paddle = Paddle(LEFT)
right_paddle = Paddle(RIGHT)
screen.update()
time.sleep(1)
ball = Ball()
screen.update()
time.sleep(1)


screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

game_is_on = True
ball_is_free = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(.01)

    #detect collision with wall
    if abs(ball.ycor()) > 290:
        ball.y_bounce()

    #detect collision with paddle
    if ball.xcor() > 325 and ball.distance(right_paddle) < 50 or ball.xcor() < -325 and ball.distance(left_paddle) < 50:
        if ball_is_free:
            ball.x_bounce()
            ball_is_free = False

    #detect if ball past boundary
    if abs(ball.xcor()) > 410 and ball_is_free:
        if ball.xcor() > 0: 
            score_board.increase_score("left")
        elif ball.xcor() < 0:
            score_board.increase_score("right")
        score_board.write_score()
        ball.refresh()
        screen.update()
        time.sleep(1)

    #detect if ball is free:
    if abs(ball.xcor()) < 300:
        ball_is_free = True

screen.exitonclick()

