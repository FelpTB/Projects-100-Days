from turtle import Turtle

FONT = ("Roboto", 14, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.goto(0,260)
        self.pencolor("blue")
        self.penup()
        self.hideturtle()
        self.att()

    def att(self):
        self.write(f"Score = {self.i}", True, "center", FONT)

    def count(self):
        self.goto(0, 260)
        self.i += 1
        self.clear()
        self.att()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER!", True, "center", FONT)


