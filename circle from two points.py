# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 09:24:27 2026

@author: zahuo
"""

from graphics import *

win = GraphWin("Exit Box", 500, 500)
win.setBackground("purple")

def radius(x1, x2, y1, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    
def draw_circle(myWin):
    message = Text(Point(250, 20), "Click on two points to draw a circle.")
    message.setTextColor("white")
    message.setStyle("bold")
    message.setSize(15)
    message.draw(myWin)
    p1 = myWin.getMouse()
    p1_x = p1.getX()
    p1_y = p1.getY()
    p1.draw(myWin)
    p2 = myWin.getMouse()
    p2_x = p2.getX()
    p2_y = p2.getY()
    r = radius(p1_x, p2_x, p1_y, p2_y)
    c = Circle(Point(p1_x, p1_y), r)
    c.setFill("lightblue")
    c.draw(win)
    
exit_box = Rectangle(Point(500, 0), Point(460, 40))
exit_box.setFill("pink")

x_line_1 = Line(Point(470, 10), Point(490, 30))
x_line_1.setOutline("blue")
x_line_1.setWidth(5)

x_line_2 = Line(Point(490, 10), Point(470, 30))
x_line_2.setOutline("blue")
x_line_2.setWidth(5)

exit_box.draw(win)
x_line_1.draw(win)
x_line_2.draw(win)

draw_circle(win)

while True:
    clickPoint = win.getMouse()
    xVal = clickPoint.getX()
    yVal = clickPoint.getY()
    if xVal > 460 and yVal < 40:
        win.close()
        break