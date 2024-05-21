from turtle import Turtle
import random


class Food(Turtle):  # inherit from the Turtle class
    def __init__(self):
        # call init from super class Turtle
        super().__init__()
        self.shape("circle")
        self.penup()

        # default circle size will be 20x20, so change it to be 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")

        self.refresh_location()

    def refresh_location(self):
        # pick a random location to generate new food bit
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # set random location for food bit on screen
        self.goto(random_x, random_y)
