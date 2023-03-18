from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.mspeed = 0.1

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x,y)

    def bouncey(self):
        self.ymove *= -1


    def bouncex(self):
        self.xmove *= -1
        self.mspeed /= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bouncex()
        self.mspeed = 0.1