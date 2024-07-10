import turtle
from turtle import Turtle, Screen


def move_upwards():
    tim.setheading(90)
    tim.forward(10)


def move_right():
    tim.setheading(0)
    tim.forward(10)


def move_downwards():
    tim.setheading(270)
    tim.forward(10)


def move_left():
    tim.setheading(180)
    tim.forward(10)


def clear_screen():
    screen.clearscreen()
    turtle.setposition(0, 0)


def penup():
    tim.penup()


def pendown():
    tim.pendown()


tim = Turtle()
screen = Screen()
screen.listen()

screen.onkey(fun=move_upwards, key='w')
screen.onkey(fun=move_right, key='d')
screen.onkey(fun=move_downwards, key='s')
screen.onkey(fun=move_left, key='a')
screen.onkey(fun=clear_screen, key='c')
screen.onkey(fun=penup, key='o')
screen.onkey(fun=pendown, key='p')

screen.exitonclick()

