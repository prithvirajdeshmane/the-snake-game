from turtle import Screen
import time
from snake import Snake
from food import Food

REFRESH_RATE_IN_SECONDS = 0.2
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

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
    time.sleep(REFRESH_RATE_IN_SECONDS)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        print("NOM NOM NOM")
        food.refresh_location()

# Close the screen
screen.exitonclick()
