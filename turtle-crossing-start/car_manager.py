import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_POSITIONING = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_timer = 0


    def car_creator(self):
        self.car_timer +=1
        if self.car_timer > 7:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(280, random.choice(LANE_POSITIONING))
            self.all_cars.append(new_car)
            self.car_timer = 0

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
