from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(280, 280)   # top right corner
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 7, "bold"))

    def increase_score(self):
        self.score += 1
        self.write_score()