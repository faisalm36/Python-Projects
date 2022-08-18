from contextlib import redirect_stderr
from turtle import Turtle, Screen
import random


turtle = Turtle()
turtle.speed("fastest")
def drawingSpiro(size_gap):
  for x in range(int(360 / size_gap)):
    turtle.circle(100)
    turtle.setheading(turtle.heading() + size_gap)

drawingSpiro(5)

screen = Screen()
screen.exitonclick()