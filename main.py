from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from wall import Wall
import time
from snake import Snake

# set up the screen background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Old School Snake Game")
# ask user for difficulty
difficulty = screen.numinput("DIFFICULTY LEVEL", "1 for easy, 2 for difficult, 3 for hardcore: ")
# turn off tracer so that we can update the screen manually when we want it
# this is needed to avoid each snake segment from scurrying along
# instead it will move smoothly
screen.tracer(0)

snake = Snake()
food = Food()
wall = Wall()
scoreboard = Scoreboard()

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
    # adding a delay between each screen update to imitate the snake moving
    # this is based on the difficulty chosen by user
    if difficulty == 1:
        time.sleep(0.2)
    elif difficulty == 2:
        time.sleep(0.1)
    elif difficulty == 3:
        wall.create_wall()
        time.sleep(0.1)
    # function that moves the snake segments, last to second to last etc
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.refresh_counter()

    # detect collision with wall
    for wall_seg in wall.wall_segments:
        if snake.head.distance(wall_seg) < 10:
            game_is_on = False
            scoreboard.game_over()

    # detect collision with wall, if snake head goes over the limit
    # then appear from the other side of the screen
    if snake.head.xcor() > 290:
        snake.head.goto(-290, snake.head.ycor())
    elif snake.head.xcor() < -290:
        snake.head.goto(290, snake.head.ycor())
    elif snake.head.ycor() > 290:
        snake.head.goto(snake.head.xcor(), -290)
    elif snake.head.ycor() < -290:
        snake.head.goto(snake.head.xcor(), 290)

    # detect collision with tail
    # if head collides with any segment of the snake then trigger game over sequence
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()