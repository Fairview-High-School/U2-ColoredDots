#turtle documentation:  https://docs.python.org/3/library/turtle.html

import turtle
import random

screen = turtle.Screen()

# The apple sits in the middle of the screen, at (0, 0)
appleCostume = "apple-clipart.gif"
screen.register_shape(appleCostume)
apple = turtle.Turtle()
apple.shape(appleCostume)

# The plotter is the invisible turtle that draws the dots
plotter = turtle.Turtle()
plotter.hideturtle()
plotter.penup()

# Half the width and height of the window.
# If the window is 500 wide, halfWidth is 250, so x goes from -250 to 250.
halfWidth = screen.window_width() // 2
halfHeight = screen.window_height() // 2


# ============================================================
#  YOUR JOB: change the condition in this function.
#  It gets the x and y of a dot, and returns the color to draw it.
# ============================================================
def pickColor(x, y):
  if x > 0 and apple.distance(x, y) > 100:
    return "purple"
  else:
    return "orange"

  # Another condition to try:
  # if x > y:
  #   return "purple"
  # else:
  #   return "orange"
# ============================================================


# main script
screen.tracer(0)  # turn off animation so the dots draw fast

for i in range(3000):  # draw 3000 dots
  x = random.randint(-halfWidth, halfWidth)
  y = random.randint(-halfHeight, halfHeight)
  color = pickColor(x, y)
  plotter.goto(x, y)
  plotter.dot(5, color)
  screen.update()  # show the new dot

screen.mainloop()  # keep the window open when the dots are done
