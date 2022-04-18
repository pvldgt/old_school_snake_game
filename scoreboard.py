from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 15, "bold")

class Scoreboard(Turtle):
    # initialize scoreboard object
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.counter = 0
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(f"YOUR SCORE: {self.counter}", align=ALIGNMENT, font=FONT)

    # update the score counter, clear the previous sign and display the new score
    def refresh_counter(self):
        self.counter += 1
        self.clear()
        self.display_scoreboard()

    # display the game over message
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


