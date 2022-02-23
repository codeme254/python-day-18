# drawing a square with turtle
from turtle import Turtle, Screen

turtle = Turtle()
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)
# turtle.forward(80)
# turtle.right(90)
# turtle.forward(80)
# turtle.right(90)
# turtle.forward(80)

Screen().exitonclick()