# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 10:11:58 2026

@author: zahuo
"""

from graphics import *
import numpy as np
import time

def rot(aPoint, rPoint, angle):
    oldX = aPoint.getX()
    oldY = aPoint.getY()
    rX = rPoint.getX()
    rY = rPoint.getY()
    newX = (oldX-rX)*np.cos(angle) - (oldY-rY)*np.sin(angle) + rX
    newY = (oldX-rX)*np.sin(angle) + (oldY-rY)*np.cos(angle) + rY
    return Point(newX, newY)
 
# Main
win = GraphWin("Rotate Rectangle", 1500, 750)
win.setBackground("lightblue")

win.autoflush = False

point1 = Point(400, 300)
point2 = Point(500, 300)
point3 = Point(500, 400)
point4 = Point(400, 400)

rect = Polygon(point1, point2, point3, point4)
rect.setFill("purple")
rect.draw(win)
win.update()

rect_center = Point(450, 350)

for i in range(500):
    newPoint1 = rot(point1, rect_center, np.pi/90)
    newPoint2 = rot(point2, rect_center, np.pi/90)
    newPoint3 = rot(point3, rect_center, np.pi/90)
    newPoint4 = rot(point4, rect_center, np.pi/90)
    
    rect.undraw()
    rect = Polygon(newPoint1, newPoint2, newPoint3, newPoint4)
    rect.setFill("purple")
    rect.draw(win)
    
    point1 = newPoint1
    point2 = newPoint2
    point3 = newPoint3
    point4 = newPoint4
    
    win.update()
    time.sleep(0.01)
    
win.getMouse()
win.close()