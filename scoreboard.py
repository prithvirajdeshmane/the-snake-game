from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_X = 0
SCOREBOARD_Y = 250
SCOREBOARD_COLOR = "dark violet"
SCORE_FONT = ("Arial", 12, 'bold')
GAME_OVER_COLOR = "red"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(x=SCOREBOARD_X, y=SCOREBOARD_Y)
        self.score = 0

    def show_score(self):
        self.clear()
        self.color(SCOREBOARD_COLOR)
        self.write(f"Score: {self.score}", False,
                   align=SCOREBOARD_ALIGNMENT, font=SCORE_FONT)

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.color(GAME_OVER_COLOR)
        self.write("GAME OVER!", False, align=SCOREBOARD_ALIGNMENT, font=SCORE_FONT)
