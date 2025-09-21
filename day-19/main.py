from random import randint
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500,height= 400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors= ["red","orange","yellow","green","blue","purple"]
all_turtles = []


def turtle_creator():
    y = -100
    for turtle_index in range(6):
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y= y + (turtle_index * 40))
        all_turtles.append(new_turtle)


turtle_creator()
if user_bet:
    is_race_on = True


while is_race_on:
        for turtle in all_turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You win! The {winning_color} turtle is the winner!")

                else:
                    print(f"You lose! The {winning_color} turtle is the winner!")

screen.exitonclick()