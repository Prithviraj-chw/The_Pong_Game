from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()
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

    #detect collision with upper walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    #detect collision with paddles
    if ball.xcor() > 330 and right_paddle.distance(ball) < 50:
        """ .distance() checks the distance between the center of the paddle and the ball
            so it glitches out when the ball hits the edge of the paddle"""
        ball.bounce_paddle()
        ball.increase_speed()

    if ball.xcor() < -330 and left_paddle.distance(ball) < 50:
        ball.bounce_paddle()
        ball.increase_speed()

    #detect if ball goes out of bounds
    if ball.xcor() > 390:
        ball.ball_reset()
        score.clear()
        score.l_point()

    if ball.xcor() < -390:
        ball.ball_reset()
        score.clear()
        score.r_point()
















screen.exitonclick()