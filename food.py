from turtle import Turtle
import random


# create a Food class from Turtle superclass
class Food(Turtle):

    def __init__(self):
        super().__init__()
        # set up the shape,size, color and the location of a food object
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
