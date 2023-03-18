from turtle import Screen, Turtle
from paddle import Paddle



screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pingpong")
screen.tracer(0)

paddle_l = Paddle(-350,0)
paddle_r = Paddle(350,0)

screen.listen()
screen.onkey(paddle_l.go_w,"w")
screen.onkey(paddle_l.go_s,"s")

screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()