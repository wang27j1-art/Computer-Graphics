# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 12:59:59 2026

@author: zahuo
"""

from graphics import *
import random

win = GraphWin("Wheel", 1000, 500)
win.setBackground("lightgreen")
import time

border_color_list = ["red", "blue", "green"]
border_color = random.choice(border_color_list)

wheel = Circle(Point(200, 200), 75)
wheel.setFill("white")
wheel.setOutline(border_color)
wheel.setWidth(5)

wheel_line1 = Line(Point(125, 200), Point(275, 200))
wheel_line1.setFill(border_color)
wheel_line1.setWidth(5)

wheel_line2 = Line(Point(200, 125), Point(200, 275))
wheel_line2.setFill(border_color)
wheel_line2.setWidth(5)

ground = Line(Point(0, 275), Point(1000, 275))
ground.setWidth(5)
ground.setFill("brown")

ground.draw(win)
wheel.draw(win)
wheel_line1.draw(win)
wheel_line2.draw(win)

win.getMouse()
win.close()