from turtle import Screen, Turtle
from random import choice

colors = ['red', 'green', 'pink', 'crimson', 'blue', 'yellow']

turtle = Turtle()
turtle.pensize(1.5)
turtle.speed('fastest')

def draw_spirograph(gap_size):

    for _ in range(int(360/gap_size)):
        turtle.color(choice(colors))
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading+10)
draw_spirograph(5)

Screen().exitonclick()

