from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ymove = 10
        self.xmove = 10
        self.spd = 0.1

    def move(self):
        y = self.ycor() + self.ymove
        x = self.xcor() + self.xmove
        self.goto(x,y)

    def bounce(self):
        self.ymove *= -1
        self.spd *=0.9

    def collision(self):
        self.xmove *=-1
        self.spd *= 0.9

