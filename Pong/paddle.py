from turtle import Turtle
from venv import create

POSITIONS = [50,30,20,-10,-30]

class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(cords)

    def goUp(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def goDown(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

