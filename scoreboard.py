from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 15, "bold")
GAME_OVER_FONT = ("Courier New", 40, "bold")


class Scoreboard(Turtle):
    # initialize scoreboard object
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.counter = 0
        # read the high score from file
        with open("data.txt") as file:
            read_score = int(file.read())
        self.high_score = read_score
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(f"YOUR SCORE: {self.counter} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    # update the score counter, clear the previous sign and display the new score
    def refresh_counter(self):
        self.counter += 1
        self.clear()
        self.display_scoreboard()

    def reset(self):
        # update the high score if the score is higher and set the counter to 0 again
        if self.counter > self.high_score:
            # write the high score to file
            with open("data.txt", mode="w") as file:
                file.write(str(self.counter))
            self.high_score = self.counter
        self.counter = 0
        self.clear()
        self.display_scoreboard()

    # display the game over message
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -45)
        self.write(f"Final score is {self.counter}", align=ALIGNMENT, font=GAME_OVER_FONT)
