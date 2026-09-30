#turtle documentation:  https://docs.python.org/3/library/turtle.html
#https://inventwithpython.com/blog/complete-list-tkinter-colors-valid-and-tested.html

import turtle
import random

screen = turtle.Screen()

# The apple sits in the middle of the screen, at (0, 0)
appleCostume = "apple-clipart.gif"
screen.register_shape(appleCostume)
apple = turtle.Turtle()
apple.shape(appleCostume)
#apple.hideturtle()

# The plotter is the invisible turtle that draws the dots
plotter = turtle.Turtle()
plotter.hideturtle()
plotter.penup()

# Half the width and height of the window.
# If the window is 500 wide, halfWidth is 250, so x_position goes from -250 to 250.
halfWidth = screen.window_width() // 2
halfHeight = screen.window_height() // 2


# ============================================================
#  YOUR JOB: change the condition in this function.
#  It gets the x_position and y_position of a dot, and returns the color to draw it.
# ============================================================
def pickColor(x_position, y_position):
  distance_to_apple = apple.distance(x_position, y_position)
  if x_position > 0 and distance_to_apple> 100:
    return "purple"
  else:
    return "darkorange1"
 
  # Another condition to try:
  # if x_position > y_position:
  #   return "purple"
  # else:
  #   return "darkorange1"
# ============================================================


# main script
screen.tracer(0)  # turn off animation so the dots draw fast

for i in range(10000):  # draw 3000 dots
  x_position = random.randint(-halfWidth, halfWidth)
  y_position = random.randint(-halfHeight, halfHeight)
  color = pickColor(x_position, y_position)
  plotter.goto(x_position, y_position)
  plotter.dot(5, color)
  if i % 100 == 0:  # every 100 dots...
    screen.update()  # ...show the new dots

screen.mainloop()  # keep the window open when the dots are done