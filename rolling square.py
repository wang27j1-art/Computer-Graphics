# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 10:26:08 2026

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

point1 = Point(400, 500)
point2 = Point(400, 300)
point3 = Point(200, 300)
point4 = Point(200, 500)

rect = Polygon(point1, point2, point3, point4)
rect.setFill("purple")
rect.draw(win)
win.getMouse()

turn = 0
steps_per_turn = 15
angle_step = ((np.pi)/2) / steps_per_turn

for i in range(20):
    corners = [point1, point2, point3, point4]
    pivot = corners[turn % 4]
    
    for j in range(steps_per_turn):
        newPoint1 = rot(point1, pivot, angle_step)
        newPoint2 = rot(point2, pivot, angle_step)
        newPoint3 = rot(point3, pivot, angle_step)
        newPoint4 = rot(point4, pivot, angle_step)
    
        rect.undraw()
        rect = Polygon(newPoint1, newPoint2, newPoint3, newPoint4)
        rect.setFill("purple")
        rect.draw(win)
    
        point1 = newPoint1
        point2 = newPoint2
        point3 = newPoint3
        point4 = newPoint4
    
        win.update()
        time.sleep(0.05)
        
    turn += 1
    
win.getMouse()
win.close()