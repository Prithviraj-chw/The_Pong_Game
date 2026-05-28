from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()

    def move(self):
        new_xcor = self.xcor() + 10
        new_ycor = self.ycor() + 5
        self.goto(new_xcor,new_ycor)
