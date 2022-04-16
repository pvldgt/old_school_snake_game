from turtle import Screen, Turtle
import time

# set up the screen background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Old School Snake Game")
# turn off tracer so that we can update the screen manually when we want it
# this is needed to avoid each snake segment from scurrying along
# instead it will move smoothly
screen.tracer(0)

# set up the starting positions
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# a for loop to create the 3 initial segments
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# a while loop to make the initial segments move along
game_is_on = True
while game_is_on:
    # since the tracer is off now we need to update the screen manually
    screen.update()
    # adding a 0.1 sec delay between each screen update to imitate the snake moving
    time.sleep(0.1)
    # create a for loo[ that moves the snake segments, last to second to last etc
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    # and then move the very first element that will drag the rest of the elements
    # on the next iteration
    segments[0].forward(20)


# snake_segment_1 = Turtle(shape="square")
# snake_segment_1.color("white")
# snake_segment_1.goto(0, 0)
#
# snake_segment_2 = Turtle(shape="square")
# snake_segment_2.color("white")
# snake_segment_2.goto(-20, 0)
#
# snake_segment_3 = Turtle(shape="square")
# snake_segment_3.color("white")
# snake_segment_3.goto(-40, 0)



screen.exitonclick()