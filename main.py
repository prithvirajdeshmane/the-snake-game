from turtle import Turtle, Screen
import time

# Crete the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Set snake's starting positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# List of the snake body segments
snake_segments = []

# Create snake of length 3
for position in STARTING_POSITIONS:
    t = Turtle(shape="square")
    t.color("white")
    t.penup()
    t.goto(position)
    snake_segments.append(t)

# Snake head is green, tail end is red
snake_segments[0].color("green")
snake_segments[len(snake_segments)-1].color("red")

# Track if game is on
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(1)
    for i in range(len(snake_segments)-1, 0, -1):
        new_x = snake_segments[i-1].xcor()
        new_y = snake_segments[i-1].ycor()
        snake_segments[i].goto(new_x, new_y)
    snake_segments[0].forward(20)

# Close the screen
screen.exitonclick()