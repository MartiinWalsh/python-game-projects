import turtle
import pandas

screen = turtle.Screen()
screen.title("Ireland Counties Game")
image = "Island_of_Ireland_blank_map.gif"
turtle.screensize(canvwidth=800, canvheight=600, bg="#99CCCC")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./counties.csv")
all_counties = data.county.to_list()
guessed_counties = []
missing_counties = []

while len(guessed_counties) < 32:
    answer_county = screen.textinput(
        title=f"{len(guessed_counties)}/32 Guess the county",
        prompt="What's another counties name?",
    ).title()

    if answer_county == "Exit":
        missing_counties = [
            county for county in all_counties if county not in guessed_counties
        ]
        new_data = pandas.DataFrame(missing_counties)
        new_data.to_csv("Counties_to_learn.csv")
        break

    if answer_county in all_counties:
        guessed_counties.append(answer_county)
        county_data = data[data.county == answer_county]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(county_data.x), int(county_data.y))
        t.write(answer_county, font=("Arial", 12, "bold"))
