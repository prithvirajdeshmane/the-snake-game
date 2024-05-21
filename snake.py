from turtle import Turtle

# Set snake's starting positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Set directional heading angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """ create a new instance of the Snake object """
        # List of the snake body segments
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        """ create the body of the snake """
        # Create snake of length 3
        for position in STARTING_POSITIONS:
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(position)
            self.snake_segments.append(t)

        # Snake head is green, tail end is red
        self.snake_segments[0].color("green")
        self.snake_segments[len(self.snake_segments) - 1].color("red")

    def move(self):
        """ move the snake forward """
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """ Turns the snake in the UP (North) direction, as long as current heading is not DOWN """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ Turns the snake in the DOWN (South) direction, as long as current heading is not UP """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ Turns the snake LEFT (West), as long as current heading is not RIGHT """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ Turns the snake RIGHT (East), as long as current heading is not LEFT """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

