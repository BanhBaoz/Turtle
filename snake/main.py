
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
sk = Snake()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(sk.up,"Up")
screen.onkey(sk.down,"Down")
screen.onkey(sk.left,"Left")
screen.onkey(sk.right,"Right")


gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)
    sk.Move()

    if sk.head.distance(food) < 15:  #compares distance between 2 obj
        food.refresh()
        scoreboard.refresh()
        sk.grow()

    #detect collision
    if  sk.head.xcor() >280 or sk.head.xcor()< -280 or sk.head.ycor()>280 or sk.head.ycor()<-280:
        gameOn=False
        scoreboard.gameOver()

    #tail collision
    for seg in sk.snake[1:]:
        if sk.head.distance(seg) <15:
            gameOn = False
            scoreboard.gameOver()
            break





screen.exitonclick()