#turtle documentation:  https://docs.python.org/3/library/turtle.html

import turtle
import random

stage = turtle.Screen()

appleCostume = "apple-clipart.gif"
apple = turtle.Turtle()

stage.register_shape(appleCostume)
apple.shape(appleCostume)
apple.left(90)
apple.hideturtle()
plotter = turtle.Turtle()
plotter.penup()

#if the width (or height) of the window is 500, then we want a number between -250 and 250
def randomPosition():
  x = random.randint(int(-1 * stage.window_width()/2),int(stage.window_width()/2))
  y = random.randint(int(-1 * stage.window_height()/2), int(stage.window_height()/2))
  return (x,y)

def makeAPoint():
  plotter.pensize(5)
  plotter.pendown()
  plotter.forward(0)
  plotter.penup()


#main script
stage.tracer(0) #this will turn off screen updates, until stage.update() is called - it speeds things up
plotter.clear()
plotter.penup()  #plotter is the name of my turtle/Sprite
while (True):  #this is a forever loop.  It repeats while the (condition) is True.  And True is always True
  plotter.goto(randomPosition())
  apple.showturtle()
  
  if plotter.xcor() > 0 and plotter.distance(apple) > 100:
    plotter.pencolor("purple")
  else:
    plotter.pencolor("orange")
    
  # if plotter.xcor() > plotter.ycor():
  #   plotter.pencolor("purple")
  # else:
  #   plotter.pencolor("orange")
  
  makeAPoint()
  stage.update()
