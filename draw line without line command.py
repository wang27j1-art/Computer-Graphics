# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 08:51:20 2026

@author: zahuo
"""

from graphics import *
import numpy as np

def dda(x1, y1, x2, y2):
    length = abs(x2 - x1)
    if abs(y2 - y2) > length:
        length = abs(y2 - y1)
    x_inc = (x2 - x1) / length
    y_inc = (y2 - y1) / length
    x = x1
    y = y1
    for i in range(length):
        x_to_plot = round(x)
        y_to_plot = round(y)
        nextPoint = Point(x_to_plot, y_to_plot)
        nextPoint.draw(win)
        x1 += x_inc
        y1 += y_inc
        
win = GraphWin("Draw Line Without Line Command", 500, 500)
win.setBackground("lightyellow")

point_1 = win.getMouse()
point_2 = win.getMouse()

x1, y1 = point_1.getX(), point_1.getY()
x2, y2 = point_2.getX(), point_2.getY()
point_1.draw(win)
point_2.draw(win)

dda(x1, y1, x2, y2)

win.getMouse()
win.close()