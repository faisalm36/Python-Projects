from turtle import Turtle, Screen
import turtle
import random
from itertools import cycle

turtle = Turtle()

Race = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle will win the race")
print(user_bet)
colors = ["red", "green", "blue", "purple", "orange", "pink"]
y_position = [-120, -80, -40, 0, 40, 80]
the_color = random.choice(colors)
all_turtles = []

for turtle_index in range(0,6):
  turtle=Turtle(shape="turtle")
  # turtle.color(the_color)
  turtle.color(colors[turtle_index])
  turtle.penup()
  turtle.goto( x = -230 , y = y_position[turtle_index]) 
  all_turtles.append(turtle)
 
if user_bet:
  Race = True
#add a point to where the user can see the top 3 winners instead of just the first winner
while Race:

  for turtle in all_turtles:
    if turtle.xcor() > 230:
      Race = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You have won!!! The {winning_color} turte is the winner")
      else:
        print(f"You have lost, the winning color is {winning_color} !!")
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)

screen.exitonclick()
