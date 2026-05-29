from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor,new_ycor)

    def bounce_wall(self):
        self.y_move *= -1 #reverses the direction of movement

    def bounce_paddle(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_paddle() #ball resets and goes in the direction of the opposite player

    def increase_speed(self):
        self.x_move += 1
        self.y_move += 1
        self.move()