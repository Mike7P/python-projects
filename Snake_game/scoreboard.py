from turtle import Turtle

from snake import Snake

from snake import Snake
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle, Snake):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("blue")
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)

        if self.score == 1:
            points = "point"
        else:
            points = "points"

        self.write(f"GAME OVER!   \n    {self.score} {points}!!", align="center", font=("Arial", 24, "normal"))
