import turtle as tur
import math as m

"""
Imports 

math.cos(0)
turtle.getscreen()

imports can also be imported as shorter names

import turtle as tur
import math as m

m. cos(0)
tur.getscreen()

imports can also be from modules 

from myModule import myFunction
or 
from myModule import myFunction as fn
"""

tur.title("Fun with Turtles!")

myTurtle = tur.Turtle() # creates a turtle using the turtle initializer

myTurtle.home() # send turtle to home position

myTurtle.forward(100) # move turtle forward 100 pixels
myTurtle.right(90)
myTurtle.forward(100)
myTurtle.right(90)
myTurtle.forward(100)
myTurtle.right(90)
myTurtle.forward(100)
myTurtle.right(90)