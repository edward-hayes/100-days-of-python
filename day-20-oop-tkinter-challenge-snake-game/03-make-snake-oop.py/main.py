from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("#4A545D")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

screen.listen()

time.sleep(2)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    snake.move()