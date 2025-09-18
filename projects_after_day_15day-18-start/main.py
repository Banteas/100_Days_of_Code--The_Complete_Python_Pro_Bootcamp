from turtle import Turtle,Screen
import random

franklin = Turtle()
franklin.shape("turtle")
franklin.speed(3)

colours= ["red", "green","DarkOrchid","DeepSkyBlue","Pink","CornFlowerBlue","IndianRed","SlateGrey"]
def draw_shape(num_sides):
    for j in range(num_sides):
        angle = 360 / num_sides
        franklin.forward(100)
        franklin.right(angle)

for shape_side_num in range(3,11):
    franklin.color(random.choice(colours))
    draw_shape(shape_side_num)




screen = Screen()
screen.exitonclick()