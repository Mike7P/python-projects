from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.speedy = 0.10

    def move(self):
        newx_cor = self.xcor() + self.xmove
        newy_cor = self.ycor() + self.ymove
        self.goto(newx_cor, newy_cor)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.speedy *= 0.9
        print(self.speedy)

    def reset_position(self):
        self.goto(0, 0)
        self.speedy = 0.1
        self.bounce_x()