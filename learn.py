# Turtle graphics
from turtle import Screen, Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(50)
timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()

# ==========================
# ways of importing modules#
# ==========================
# import turtle
# turtle = turtle.Turtle()

# from turtle import Turtle
# turtle = Turtle()

# # importing everything
# from turtle import *

# # importing with aliases
# import turtle as t