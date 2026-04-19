# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 10:40:44 2026

@author: zahuo
"""

from graphics import *

def get_points():
    points = []
    for i in range(4):
        p = win.getMouse()
        points.append(p)
        c = Circle(p, 4)
        c.setFill("darkblue")
        c.draw(win)
    return points
        
def bcurve(p0, p1, p2, p3, num_points, win):
    for i in range(num_points + 1):
        t = i / num_points
        x = (1-t)**3 * p0.getX() + 3*(1-t)**2 * t * p1.getX() + 3*(1-t)*t**2 * p2.getX() + t**3 * p3.getX()
        y = (1-t)**3 * p0.getY() + 3*(1-t)**2 * t * p1.getY() + 3*(1-t)*t**2 * p2.getY() + t**3 * p3.getY()
        Point(x, y).draw(win)
    
win = GraphWin("Bezier", 1000, 1000)
win.setCoords(0, 0, 999, 999)

pts = get_points()
p0, p1, p2, p3 = pts
bcurve(p0, p1, p2, p3, 800, win)

win.getMouse()
win.close()