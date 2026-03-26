import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
t = turtle.Turtle()
t.pensize(2)
t.color("black", "yellow")
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.right(60)
t.end_fill()
turtle.done()