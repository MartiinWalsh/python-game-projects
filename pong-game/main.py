from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()
