from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()



keys_pressed = {"Up": False, "Down": False, "w": False, "s": False}

# functions to update the dictionary
def press_up(): keys_pressed["Up"] = True
def release_up(): keys_pressed["Up"] = False
def press_down(): keys_pressed["Down"] = True
def release_down(): keys_pressed["Down"] = False
def press_w(): keys_pressed["w"] = True
def release_w(): keys_pressed["w"] = False
def press_s(): keys_pressed["s"] = True
def release_s(): keys_pressed["s"] = False

# key bindings
screen.listen()
screen.onkeypress(press_up, "Up")
screen.onkeyrelease(release_up, "Up")
screen.onkeypress(press_down, "Down")
screen.onkeyrelease(release_down, "Down")
screen.onkeypress(press_w, "w")
screen.onkeyrelease(release_w, "w")
screen.onkeypress(press_s, "s")
screen.onkeyrelease(release_s, "s")

game_is_on = True


def exit_game(x, y):
    global game_is_on
    game_is_on = False


screen.onclick(exit_game)


while game_is_on:
    if keys_pressed["Up"]:
        right_paddle.up()
    if keys_pressed["Down"]:
        right_paddle.down()
    if keys_pressed["w"]:
        left_paddle.up()
    if keys_pressed["s"]:
        left_paddle.down()

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if (((330 < ball.xcor() < 350) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50)) or
            ((-350 < ball.xcor() < -330) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50))):
        ball.paddle_bounce()
    # if right_paddle misses
    if ball.xcor() > 360:
        ball.restart()
        scoreboard.l_point()

    # if left_paddle misses
    if ball.xcor() < -360:
        ball.restart()
        scoreboard.r_point()




screen.bye()

