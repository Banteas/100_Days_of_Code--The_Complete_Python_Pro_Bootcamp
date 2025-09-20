import random
from turtle import *


color_list = [(99, 6, 51), (172, 158, 33), (75, 94, 172), (232, 209, 73), (10, 35, 127), (212, 91, 34), (177, 104, 155),
              (104, 122, 210), (25, 95, 40), (33, 103, 48), (112, 130, 212) , (183, 115, 161), (218, 92, 40)]


franklin = Turtle()
franklin.shape("turtle")
franklin.color('red')
franklin.hideturtle()
franklin.penup()
colormode(255)

start_x = -300
start_y = -300

dot_spacing = 50
dots_per_row = 10
dots_per_col = 10

for row in range(dots_per_col):
    y = start_y + (dot_spacing * row)
    for col in range(dots_per_col):
        x = start_x + (col * dot_spacing)
        franklin.goto(x, y)
        franklin.dot(20, random.choice(color_list))