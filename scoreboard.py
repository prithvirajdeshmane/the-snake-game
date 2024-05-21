from turtle import Turtle

SCORE_FONT = ("Arial", 12, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False,
                   align="center", font=SCORE_FONT)

    def update_score(self):
        self.score += 1
