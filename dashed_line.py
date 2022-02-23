from turtle import Turtle, Screen

turtle = Turtle()
turtle.pensize(3)
turtle.pencolor("crimson")

for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    

Screen().exitonclick()