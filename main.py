from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

REFRESH_RATE_IN_SECONDS = 0.2
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BOUNDARY_LIMIT = 290

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

    # detect collision with wall
    if snake.head.xcor() < -1 * BOUNDARY_LIMIT \
            or snake.head.xcor() > BOUNDARY_LIMIT \
            or snake.head.ycor() < -1 * BOUNDARY_LIMIT \
            or snake.head.ycor() > BOUNDARY_LIMIT:
        scoreboard.game_over()
        is_game_on = False

# Close the screen
screen.exitonclick()
