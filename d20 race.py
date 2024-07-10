import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(900, 500)
user_bet = screen.textinput(title="Turtle Race", prompt="Who will win the race?")
colours = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
y_cords = [-150, -100, -50, 0, 50, 100, 150]
is_race_on = False
all_turtles = []

for turtle_index in range(0,7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-400, y=y_cords[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    # random_turtle = random.randint(0, len(all_turtles) - 1)

    for turtle in all_turtles:
        random_distance = random.randint(-10,20)
        turtle.pendown()
        turtle.forward(random_distance)
        # turtle measures 40 x 40 pixels

        if turtle.xcor() >= 380:
            turtle_colour = turtle.pencolor()

            if user_bet == turtle_colour:
                print(f"You win! {turtle_colour} has won the race! ")
            else:
                print(f"You lose! {turtle_colour} has won the race! ")

            is_race_on = False

screen.exitonclick()
