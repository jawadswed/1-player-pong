from turtle import Turtle

RIGHT = 0
LEFT = 180


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -210)

    def move_left(self):
        if self.xcor() > -190:
            new_x = self.xcor() - 25
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 190:
            new_x = self.xcor() + 25
            self.goto(new_x, self.ycor())
