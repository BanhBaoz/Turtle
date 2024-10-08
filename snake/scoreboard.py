from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.sc = 0
        self.penup()
        self.goto(0, 270)
        self.updateSc()
        self.hideturtle()

    def updateSc(self):
        self.write(f"Score: {self.sc}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.sc += 1
        self.clear()
        self.updateSc()

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

