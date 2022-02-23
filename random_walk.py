from turtle import Screen, Turtle
from random import choice, random, randint
colors = ['red', 'green', 'pink', 'crimson', 'blue', 'yellow']
headings = [0, 90, 180, 270]

turtle = Turtle()
turtle.pensize(5)
turtle.shape('turtle')
turtle.speed(1)
for _ in range(200):
    turtle.color(choice(colors))
    turtle.forward(20)
    turtle.setheading(choice(headings))

Screen().exitonclick()