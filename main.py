from turtle import Screen, Turtle
import time
from snake import Snake

# set up the screen background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Old School Snake Game")
# turn off tracer so that we can update the screen manually when we want it
# this is needed to avoid each snake segment from scurrying along
# instead it will move smoothly
screen.tracer(0)

snake = Snake()
# start listening for key presses that set the snake heading
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# a while loop to make the initial segments move along
game_is_on = True
while game_is_on:
    # since the tracer is off now we need to update the screen manually
    screen.update()
    # adding a 0.1 sec delay between each screen update to imitate the snake moving
    time.sleep(0.1)
    # function that moves the snake segments, last to second to last etc
    snake.move()



screen.exitonclick()