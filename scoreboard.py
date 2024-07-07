from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 220)
        self.show_score()
    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(self.score, align="center", font=("Courier", 10, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game over", align="center", font=("Courier", 30, "normal"))