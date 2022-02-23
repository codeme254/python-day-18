from turtle import Turtle, Screen
turtle = Turtle()

for side in range(3, 11):
    num_sides = side
    for _ in range(num_sides):
        angle = 360/ num_sides
        turtle.forward(100)
        turtle.right(angle)
for side in range(3, 11):
    num_sides = side
    for _ in range(num_sides):
        angle = 360/ num_sides
        turtle.forward(100)
        turtle.left(angle)


Screen().exitonclick()