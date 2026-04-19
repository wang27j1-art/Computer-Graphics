# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 16:31:58 2026

@author: zahuo
"""

from graphics import *
import time

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

draw_triangle(x1, y1, x2, y2, x3, y3)

def zoom_center_series(x1, y1, x2, y2, x3, y3, steps):
    for trials in range(steps): 
        mx12 = midpoint(x1, x2)
        mx23 = midpoint(x2, x3)
        mx31 = midpoint(x3, x1)
        my12 = midpoint(y1, y2)
        my23 = midpoint(y2, y3)
        my31 = midpoint(y3, y1)
        
        draw_triangle(mx12, my12, mx23, my23, mx31, my31)
        draw_triangle(x1, y1, mx12, my12, mx31, my31)
        draw_triangle(x2, y2, mx12, my12, mx23, my23)
        draw_triangle(x3, y3, mx31, my31, mx23, my23)
        
        x1 = mx12
        y1 = my12
        x2 = mx23
        y2 = my23
        x3 = mx31
        y3 = my31

mx12 = midpoint(x1, x2)
my12 = midpoint(y1, y2)
mx23 = midpoint(x2, x3)
my23 = midpoint(y2, y3)
mx31 = midpoint(x3, x1)
my31 = midpoint(y3, y1)

zoom_center_series(x1, y1, mx12, my12, mx31, my31, 5)
zoom_center_series(mx12, my12, mx23, my23, mx31, my31, 6)
zoom_center_series(x2, y2, mx12, my12, mx23, my23, 5)
zoom_center_series(x3, y3, mx31, my31, mx23, my23, 5)
     
win.getMouse()
win.close()