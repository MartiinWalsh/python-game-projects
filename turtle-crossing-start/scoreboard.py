from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def reset(self):
        self.level = 0
        self.update_scoreboard()
