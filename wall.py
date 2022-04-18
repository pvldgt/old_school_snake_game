from turtle import Turtle
import random

# create a 5 wall based on 5 segments / (a random amount of segments)
# make sure food doesn't get anywhere near

# set up the starting positions
random_x = random.randint(-250, 250)
random_y = random.randint(-250, 250)
WALL_POSITIONS = [(random_x, random_y), (random_x-20, random_y), (random_x-40, random_y), (random_x-60, random_y)]

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.wall_segments = []

    def create_wall(self):
        # a for loop to create the 3 initial segments
        for position in WALL_POSITIONS:
            self.add_wall_segment(position)

    def add_wall_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("orange")
        new_segment.penup()
        new_segment.goto(position)
        self.wall_segments.append(new_segment)