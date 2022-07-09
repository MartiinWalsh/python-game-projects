from tkinter import CENTER
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGHSCORES_FILE = "highscores.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open(HIGHSCORES_FILE) as file:
            self.highscore = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} - High Score: {self.highscore}",
            align=CENTER,
            font=FONT,
        )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(HIGHSCORES_FILE, "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
