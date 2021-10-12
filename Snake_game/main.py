import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# snake_color = input("which color would you like the snake?")

name = input("Welcome to the snake game; what is your name?: ")
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"{name}'s Snake Game")
screen.tracer(0)

snake = Snake("square", "white", name)
food = Food()
scoreboard = Scoreboard()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.listen()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()



