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
        # self.high_score = get_high_score()
        with open("data.txt", mode="r") as score_file:
            self.high_score = int(score_file.read())

    # display the current score
    def show_score(self):
        self.clear()
        self.color(SCOREBOARD_COLOR)
        self.write(f"Score: {self.score} High score: {self.high_score}",
                   False, align=SCOREBOARD_ALIGNMENT, font=SCORE_FONT)

    # update score when food is consumed
    def update_score(self):
        self.score += 1

    # show game over
    def game_over(self):
        self.goto(0, 0)
        self.color(GAME_OVER_COLOR)
        self.write("GAME OVER!", False, align=SCOREBOARD_ALIGNMENT, font=SCORE_FONT)

    # when game ends, check if high score needs to be updated, and reset game
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # write high score to data.txt file
            with open("data.txt", mode="w") as score_file:
                score_file.write(str(self.score))
        self.score = 0
        self.show_score()