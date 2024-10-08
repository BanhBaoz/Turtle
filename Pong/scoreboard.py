from turtle import Turtle

FONT = ("Courier",80,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.goto(0,180)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"{self.lscore}:{self.rscore}", align="center", font=FONT)

    def lpoint(self):
        self.lscore+=1
        self.update()

    def rpoint(self):
        self.rscore+=1
        self.update()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
