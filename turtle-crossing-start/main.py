import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

keys_pressed = {"Up": False, "Down": False}

def press_up(): keys_pressed["Up"] = True
def release_up(): keys_pressed["Up"] = False
def press_down(): keys_pressed["Down"] = True
def release_down(): keys_pressed["Down"] = False


screen.listen()
screen.onkeypress(press_up, "Up")
screen.onkeyrelease(release_up, "Up")
screen.onkeypress(press_down, "Down")
screen.onkeyrelease(release_down, "Down")

game_is_on = True
while game_is_on:
    if keys_pressed["Up"]:
        player.up()
    if keys_pressed["Down"]:
        player.down()
    time.sleep(0.1)
    screen.update()

    car_manager.car_creator()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()