from turtle import Turtle
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
LEFT = 0
RIGHT = 180
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.snake = []
        self.CreateSnake()
        self.head = self.snake[0]

    def CreateSnake(self):
        for pos in STARTING_POS:
            block = Turtle("square")
            block.color("white")
            block.penup()
            block.goto(pos)
            self.snake.append(block)

    def Move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:  # Prevent 180-degree turn
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:  # Prevent 180-degree turn
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:  # Prevent 180-degree turn
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:  # Prevent 180-degree turn
            self.head.setheading(180)

    def grow(self):
        x = self.snake[-1].xcor()
        y = self.snake[-1].ycor()
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(x,y)
        self.snake.append(block)