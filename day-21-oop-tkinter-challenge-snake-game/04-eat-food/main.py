from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WALL = 310

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("#4A545D")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()
screen.update()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

screen.listen()

time.sleep(1)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    def game_over():
        snake.clear()
        food.ht()
        screen.update()
        score_board.game_over()
        global game_is_on
        game_is_on = False

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        score_board.write_score()
        snake.add_to_tail()

    #detect collision with wall
    if abs(snake.head.xcor()) > WALL or abs(snake.head.ycor()) > WALL:
        game_over()

    #detect collision with tail
    for segment in snake.snake_body[3:]:
        if snake.head.distance(segment) < 10:
            game_over()

screen.exitonclick()
