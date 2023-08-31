from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title(" My PONG GAME ")
screen.tracer(0)

right_pad = Paddle((360, 0))
left_pad = Paddle((-360, 0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=right_pad.go_up, key="Up")
screen.onkey(fun=right_pad.go_down, key="Down")
screen.onkey(fun=left_pad.go_up, key="w")
screen.onkey(fun=left_pad.go_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detecting collision of ball with top and bottom walls and to bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with right and left paddle
    if (ball.distance(right_pad) < 20 or ball.distance(right_pad) < 54 and ball.xcor() == 340
            or ball.distance(left_pad) < 20 or ball.distance(left_pad) < 54 and ball.xcor() == -340):
        ball.bounce_x()

    # Detect if ball goes out of bound
    # For right wall
    if ball.xcor() == 390:
        scoreboard.l_point()
        ball.reset_position()

    # For left wall
    if ball.xcor() == -390:
        scoreboard.r_point()
        ball.reset_position()

    # For Game Over
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
