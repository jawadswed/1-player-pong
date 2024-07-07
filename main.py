from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=paddle.move_right, key="Right")
screen.onkey(fun=paddle.move_left, key="Left")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.xcor() > 230 or ball.xcor() < -230:
        ball.bounce_x()
    if ball.ycor() > 230:
        ball.bounce_y()
    if ball.distance(paddle) < 50 and ball.ycor() < -190:
        ball.bounce_y()
        scoreboard.increase_score()
        ball.increase_speed()
    if ball.ycor() < -230:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
