from turtle import Screen
from paddle import Paddle
from ball import Ball

import time

from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle = Paddle((350,0))
enemy = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(paddle.goUp,"Up")
screen.onkeypress(paddle.goDown,"Down")
screen.onkeypress(enemy.goUp,"w")
screen.onkeypress(enemy.goDown,"s")

gameOn = True

while gameOn:
    time.sleep(ball.spd)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(paddle) < 50 and ball.xcor()>340:
        ball.collision()
        scoreboard.rpoint()

    if ball.distance(enemy) < 50 and ball.xcor()<-340 :
        ball.collision()
        scoreboard.lpoint()

    if ball.xcor()>400 or ball.xcor() < -400:
        gameOn = False
        scoreboard.gameOver()




screen.exitonclick()