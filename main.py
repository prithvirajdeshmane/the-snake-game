from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

REFRESH_RATE_IN_SECONDS = 0.2
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BOUNDARY_LIMIT = 290
INTERVAL_LEVEL_SPEED_INCREASE = 3
FACTOR_SPEED_INCREASE = 0.9

# Crete the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# create a new snake object instance
snake = Snake()

# create food object instance
food = Food()

# create scoreboard instance
scoreboard = Scoreboard()

# start screen listener, and listen for arraw keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Track if game is on
is_game_on = True


# set the game end status
def end_game():
    """ sets the game end status on screen and for the game """
    scoreboard.game_over()
    global is_game_on
    is_game_on = False


def update_game_speed():
    global REFRESH_RATE_IN_SECONDS
    if scoreboard.score > 0 and \
            scoreboard.score % INTERVAL_LEVEL_SPEED_INCREASE == 0:
        REFRESH_RATE_IN_SECONDS *= FACTOR_SPEED_INCREASE


while is_game_on:
    screen.update()
    scoreboard.show_score()
    time.sleep(REFRESH_RATE_IN_SECONDS)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_location()
        scoreboard.update_score()
        snake.extend()
        update_game_speed()

    # detect collision with wall
    if snake.head.xcor() < -1 * BOUNDARY_LIMIT \
            or snake.head.xcor() > BOUNDARY_LIMIT \
            or snake.head.ycor() < -1 * BOUNDARY_LIMIT \
            or snake.head.ycor() > BOUNDARY_LIMIT:
        end_game()

    # detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            end_game()

# Close the screen
screen.exitonclick()
