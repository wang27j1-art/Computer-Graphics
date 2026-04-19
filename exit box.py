# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 09:06:26 2026

@author: zahuo
"""

from graphics import *

win = GraphWin("Exit Box", 500, 500)
win.setBackground("pink")

exit_box = Rectangle(Point(500, 0), Point(460, 40))
exit_box.setFill("red")

x_line_1 = Line(Point(470, 10), Point(490, 30))
x_line_1.setOutline("white")
x_line_1.setWidth(5)

x_line_2 = Line(Point(490, 10), Point(470, 30))
x_line_2.setOutline("white")
x_line_2.setWidth(5)

exit_box.draw(win)
x_line_1.draw(win)
x_line_2.draw(win)

while True:
    clickPoint = win.getMouse()
    xVal = clickPoint.getX()
    yVal = clickPoint.getY()
    if xVal > 460 and yVal < 40:
        win.close()
        break
    

