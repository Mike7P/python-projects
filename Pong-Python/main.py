from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# player = input("Welcome to Pong! What's your name?: ")
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

paddleR = Paddle((350, 0))
paddleL = Paddle((-350, 0))

scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(paddleR.go_up, "Up")
screen.onkey(paddleR.go_down, "Down")

screen.onkey(paddleL.go_up, "w")
screen.onkey(paddleL.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.speedy)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        #
    if ball.distance(paddleR) < 50 and ball.xcor() > 320 or ball.distance(paddleL) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # right-side collision
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

        # left-side collision
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    screen.exitonclick()
