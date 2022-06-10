from turtle import Turtle, Screen

tony = Turtle()
tony.shape("turtle")
tony.color("green")

for _ in range(4):
    tony.forward(100)
    tony.left(90)


screen = Screen()
screen.exitonclick()
