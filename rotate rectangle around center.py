# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 09:07:09 2026

@author: zahuo
"""

from graphics import *
import numpy as np

def rot(aPoint, rPoint, angle):
    oldX = aPoint.getX()
    oldY = aPoint.getY()
    rX = rPoint.getX()
    rY = rPoint.getY()
    newX = (oldX-rX)*np.cos(angle) - (oldY-rY)*np.sin(angle) + rX
    newY = (oldX-rX)*np.sin(angle) + (oldY-rY)*np.cos(angle) + rY
    return Point(newX, newY)
 
# Main
win = GraphWin("Rotate Rectangle", 500, 500)
win.setBackground("lightgreen")

point1 = Point(100, 300)
point2 = Point(200, 300)
point3 = Point(200, 400)
point4 = Point(100, 400)

rect = Polygon(point1, point2, point3, point4)
rect.draw(win)
win.getMouse()

rect_center = Point(150, 350)

newPoint1 = rot(point1, rect_center, np.pi/4)
newPoint2 = rot(point2, rect_center, np.pi/4)
newPoint3 = rot(point3, rect_center, np.pi/4)
newPoint4 = rot(point4, rect_center, np.pi/4)

newRect = Polygon(newPoint1, newPoint2, newPoint3, newPoint4)
newRect.draw(win)

win.getMouse()
win.close()