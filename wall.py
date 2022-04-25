from turtle import Turtle
import random

# when counter reaches 15, add a wall

random_x = random.randint(-250, 250)
random_y = random.randint(-250, 250)
# WALL_POSITIONS = [(random_x, random_y), (random_x-20, random_y), (random_x-40, random_y), (random_x-60, random_y)]
WALL_POSITIONS = [(random.randint(-250, 250), random.randint(-250, 250)), (random.randint(-250, 250), random.randint(-250, 250)), (random.randint(-250, 250), random.randint(-250, 250)), (random.randint(-250, 250), random.randint(-250, 250))]


class Wall():

    def __init__(self):
        self.wall_segments = []

    def create_wall(self):
        # a for loop to create the walls blocks at random positions
        for position in WALL_POSITIONS:
            self.add_wall_segment(position)

    def add_wall_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("orange")
        new_segment.penup()
        new_segment.goto(position)
        self.wall_segments.append(new_segment)