from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Poeng")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.refresh_pos()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.vert_bounce()

    if ball.distance(r_paddle) < 75 and ball.xcor() > 330 or ball.distance(l_paddle) < 75 and ball.xcor() < -330:
        ball.hor_bounce()

    if ball.xcor() > 380:
        ball.point()
        scoreboard.point_to_left()
    if ball.xcor() < -380:
        ball.point()
        scoreboard.point_to_right()
screen.exitonclick()
