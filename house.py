# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from graphics import *

win = GraphWin("My House", 500, 500)
win.setBackground("purple")

house = Rectangle(Point(125, 125), Point(375, 375))
house.setFill("lightblue")
roof = Polygon(Point(125, 125), Point(250, 50), Point(375, 125))
roof.setFill("darkblue")
window1 = Rectangle(Point(150, 200), Point(200, 250))
window1.setFill("lightpink")
window1.move(0, -25)
window2 = window1.clone()
window2.move(75, 0)
window3 = window2.clone()
window3.move(75, 0)
door = Rectangle(Point(375, 250), Point(275, 375))
door.setFill("magenta")
door.move(-75, 0)

house.draw(win)
roof.draw(win)
window1.draw(win)
window2.draw(win)
window3.draw(win)
door.draw(win)

win.getMouse()
win.close()