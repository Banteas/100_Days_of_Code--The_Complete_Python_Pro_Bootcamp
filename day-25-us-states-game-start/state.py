from turtle import Turtle

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def state_create(self, state, x, y):
        self.goto(x, y)
        self.write(state, align="center", font=("Arial", 7, "bold"))