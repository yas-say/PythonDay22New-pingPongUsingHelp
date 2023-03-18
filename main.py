from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pingpong")
screen.tracer(0)

paddle_l = Paddle(-350,0)
paddle_r = Paddle(350,0)
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(paddle_l.go_w,"w")
screen.onkey(paddle_l.go_s,"s")

screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.mspeed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bouncex()
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_l()
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_r()


screen.exitonclick()