# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 15:12:48 2026

@author: zahuo
"""

from graphics import *

win = GraphWin("Triangle Series 1", 500, 500)
win.setBackground("lightblue")

def midpoint(point_1, point_2):
    midx = (point_1 + point_2) / 2
    return midx

def draw_triangle(x1, y1, x2, y2, x3, y3):
    triangle = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    triangle.setOutline("blue")
    triangle.setWidth(4)
    triangle.draw(win)

x1 = 250
y1 = 0
x2 = 0
y2 = 490
x3 = 490
y3 = 490

for trials in range(6):
    draw_triangle(x1, y1, x2, y2, x3, y3)
    old_x1 = x1
    old_y1 = y1
    old_x2 = x2
    old_y2 = y2
    old_x3 = x3
    old_y3 = y3
    x1 = midpoint(old_x1, old_x2)
    x2 = midpoint(old_x2, old_x3)
    x3 = midpoint(old_x3, old_x1)
    y1 = midpoint(old_y1, old_y2)
    y2 = midpoint(old_y2, old_y3)
    y3 = midpoint(old_y3, old_y1)

win.getMouse()
win.close()

                
            