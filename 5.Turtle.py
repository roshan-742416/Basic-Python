# Let's draw some cool drawings with turtle

# Import turtle
import turtle

# Let's get a nice set-up in turtle
turtle.bgcolor("black")
turtle.pensize(2)
#turtle.color("red")
turtle.speed(0)
# Let's draw a square
# for x in range(1,5):
#     turtle.forward(50)
#     turtle.left(90)
#
# for x in range(1,9):
#     turtle.forward(50)
#     turtle.left(45)
#
# turtle.done()
# Allows turtle to stay on the screen

# for colours in ["red", "orange", "yellow", "green", "purple", "blue"]:
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(60)
# turtle.done()

# Let's make it cooler
for i in range(5):
    for colours in ["red", "orange", "yellow", "green", "purple", "blue"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(12)
turtle.done()