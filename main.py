from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) #turns off screen animations

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
screen.listen()
screen.onkey(left_paddle.paddle_up,"Up")
screen.onkey(left_paddle.paddle_down,"Down")

screen.onkey(right_paddle.paddle_up,"w")
screen.onkey(right_paddle.paddle_down,"s")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    



















screen.exitonclick()