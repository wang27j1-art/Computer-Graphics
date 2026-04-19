# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 12:59:59 2026

@author: zahuo
"""

from graphics import *
import numpy as np
import random

def rotate(aPoint, rPoint, angle):
    oldX = aPoint.getX()
    oldY = aPoint.getY()
    rX = rPoint.getX()
    rY = rPoint.getY()
    newX = (oldX-rX)*np.cos(angle) - (oldY-rY)*np.sin(angle) + rX
    newY = (oldX-rX)*np.sin(angle) + (oldY-rY)*np.cos(angle) + rY
    return Point(newX, newY)

win = GraphWin("Wheel on Ground", 1000, 500)
win.setBackground("lightgreen")
import time

border_color_list = ["red", "blue", "green"]
border_color = random.choice(border_color_list)

wheel_center = Point(200, 200)
wheel_radius = 75

wheel = Circle(wheel_center, wheel_radius)
wheel.setFill("white")
wheel.setOutline(border_color)
wheel.setWidth(5)

line1_point1 = Point(125, 200)
line1_point2 = Point(275, 200)

wheel_line1 = Line(line1_point1, line1_point2)
wheel_line1.setFill(border_color)
wheel_line1.setWidth(5)

line2_point1 = Point(200, 125)
line2_point2 = Point(200, 275)

wheel_line2 = Line(line2_point1, line2_point2)
wheel_line2.setFill(border_color)
wheel_line2.setWidth(5)

ground = Line(Point(0, 275), Point(1000, 275))
ground.setWidth(5)
ground.setFill("brown")

ground.draw(win)
wheel.draw(win)
wheel_line1.draw(win)
wheel_line2.draw(win)

for i in range(500):
    newPoint1 = rotate(line1_point1, wheel_radius, np.pi/90)
    newPoint2 = rotate(line1_point2, wheel_radius, np.pi/90)
    newPoint3 = rotate(line2_point1, wheel_radius, np.pi/90)
    newPoint4 = rotate(line2_point2, wheel_radius, np.pi/90)
    
    wheel_line1.undraw()
    wheel_line2.undraw()
    
    new_line1 = Line(newPoint1, newPoint2)
    new_line1.setFill(border_color)
    new_line1.setWidth(5)
    
    new_line2 = Line(newPoint3, newPoint4)
    new_line2.setFill(border_color)
    new_line2.setWidth(5)
    
    new_line1.draw(win)
    new_line2.draw(win)
    
    line1_point1 = newPoint1
    line1_point2 = newPoint2
    line2_point1 = newPoint3
    line2_point2 = newPoint4
    
    time.sleep(0.05)
       
win.getMouse()
win.close()