from turtle import Screen
import time
from snake import Snake

# Crete the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# create a new snake object instance
snake = Snake()

# Track if game is on
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(1)
    snake.move()

# Close the screen
screen.exitonclick()
