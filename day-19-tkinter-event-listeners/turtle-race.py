import random
from turtle import Turtle, Screen, screensize

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
colors = ["#DC7726", "#DDC077", "#57896A", "#4A545D", "#067593", "#055772"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
        is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            print(f"{turtle} has won the race!")
            winning_color = turtle.pencolor()

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()