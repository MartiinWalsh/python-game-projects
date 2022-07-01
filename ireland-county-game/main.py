from email.mime import image
import turtle

screen = turtle.Screen()
screen.title("Ireland Counties Game")

image = "Island_of_Ireland_blank_map.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(
    title="Guess the county", prompt="What's another counties name?"
)

screen.exitonclick()
